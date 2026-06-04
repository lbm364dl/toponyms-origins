#!/usr/bin/env python3
"""
Spawn one Codex subagent per transport station for station-name research.

By default this reads all station CSVs, sends each station row to an isolated
Codex agent, and writes resumable per-station artifacts plus aggregate indexes.

Usage:
    python scripts/run_station_research.py --limit 3 --concurrency 1
    python scripts/run_station_research.py --station-id metro_001 --station-id cercanias_001
    python scripts/run_station_research.py --output-dir runs/station-research/full --concurrency 6
    python scripts/run_station_research.py --limit 50 --concurrency 4

Canonical public Markdown/metadata is written to content/stations/ by default.
Stations already present there are skipped unless --force is used. Raw Codex
transcripts and per-run indexes stay under runs/.
"""

from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime, timezone
import json
import os
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AGENT_INSTRUCTIONS = PROJECT_ROOT / ".codex" / "agents" / "station-research.md"

DEFAULT_INPUTS = [
    PROJECT_ROOT / "data" / "madrid_metro_stations.csv",
    PROJECT_ROOT / "data" / "madrid_cercanias_stations.csv",
    PROJECT_ROOT / "data" / "madrid_metro_ligero_stations.csv",
]
DEFAULT_CONTENT_ROOT = PROJECT_ROOT / "content" / "stations"

DEFAULT_CONCURRENCY = int(os.getenv("STATION_RESEARCH_CONCURRENCY", "4"))
CODEX_MODEL = os.getenv("STATION_RESEARCH_CODEX_MODEL", "gpt-5.5")
CODEX_REASONING = os.getenv("STATION_RESEARCH_CODEX_REASONING", "medium")
CODEX_JSON_EVENTS = os.getenv("STATION_RESEARCH_CODEX_JSON_EVENTS", "1").lower() not in {
    "0",
    "false",
    "no",
}
MAX_RETRIES = int(os.getenv("STATION_RESEARCH_MAX_RETRIES", "1"))
RETRY_DELAY = int(os.getenv("STATION_RESEARCH_RETRY_DELAY", "20"))

RESULT_TAG = "station-research-result"

INDEX_FIELDS = [
    "idx",
    "id",
    "name",
    "operator",
    "line",
    "input_file",
    "return_code",
    "status",
    "confidence",
    "thread_id",
    "result_path",
    "final_path",
    "stdout_path",
    "stderr_path",
    "started_at",
    "finished_at",
]

MARKDOWN_FIELDS = [
    ("summary_short", "en", "summary_short_en", "summary.short.md"),
    ("summary_short", "es", "summary_short_es", "summary.short.md"),
    ("summary", "en", "recommended_summary_en", "summary.md"),
    ("summary", "es", "recommended_summary_es", "summary.md"),
    ("story", "en", "story_en", "story.md"),
    ("story", "es", "story_es", "story.md"),
    ("confidence", "en", "confidence_reason_en", "confidence.md"),
    ("confidence", "es", "confidence_reason_es", "confidence.md"),
    ("current_claim_assessment", "en", "current_claim_assessment_en", "current-claim-assessment.md"),
    ("current_claim_assessment", "es", "current_claim_assessment_es", "current-claim-assessment.md"),
    ("research_note", "en", "research_note_en", "research-note.md"),
    ("research_note", "es", "research_note_es", "research-note.md"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_slug(value: object, max_len: int = 80) -> str:
    text = str(value or "").lower()
    text = (
        text.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ü", "u")
        .replace("ñ", "n")
    )
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text[:max_len].strip("-") or "station")


def read_rows(paths: list[Path]) -> list[tuple[int, dict]]:
    rows: list[tuple[int, dict]] = []
    for path in paths:
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["_input_file"] = str(path.relative_to(PROJECT_ROOT))
                rows.append((len(rows), row))
    return rows


def build_prompt(instructions: str, row: dict) -> str:
    payload = json.dumps(row, ensure_ascii=False, indent=2)
    note = """
## Codex Runtime Note

You are running as a Codex CLI subagent with web search enabled. Use web search
and open pages as needed. You may read local project files for context, but do
not edit files. Return only the required final fenced JSON result block.
"""
    return f"{instructions}\n{note}\n\n## Input Station\n\n```json\n{payload}\n```\n"


def extract_result(text: str) -> dict | None:
    match = re.search(rf"```{RESULT_TAG}\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(1).strip())
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def extract_codex_json_summary(output: str) -> tuple[str | None, str | None]:
    thread_id: str | None = None
    agent_messages: list[str] = []
    for line in output.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started":
            thread_id = event.get("thread_id") or thread_id
        item = event.get("item")
        if isinstance(item, dict) and item.get("type") == "agent_message":
            text = item.get("text")
            if isinstance(text, str) and text.strip():
                agent_messages.append(text)
    return thread_id, agent_messages[-1] if agent_messages else None


def station_dir(output_dir: Path, idx: int, row: dict) -> Path:
    name = f"{row.get('id', idx)}-{safe_slug(row.get('name'))}"
    return output_dir / "agent-transcripts" / f"{idx:04d}-{name}"


def write_jsonl(path: Path, data: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n")


def write_indexes(output_dir: Path, rows: list[dict]) -> None:
    with (output_dir / "index.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=INDEX_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    with (output_dir / "index.json").open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
        f.write("\n")


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def station_content_id(value: object) -> str:
    raw_id = str(value or "").strip()
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", raw_id).strip("-")


def write_markdown_content(content_root: Path, result: dict) -> dict[str, dict[str, str]]:
    raw_id = str(result.get("id") or "").strip()
    station_id = station_content_id(raw_id) if raw_id else safe_slug(result.get("name") or "station")
    content_dir = content_root / station_id
    content_dir.mkdir(parents=True, exist_ok=True)

    files: dict[str, dict[str, str]] = {"en": {}, "es": {}}
    missing_pairs: list[str] = []
    fields_by_key: dict[str, dict[str, str]] = {}
    for content_key, lang, field, _filename in MARKDOWN_FIELDS:
        fields_by_key.setdefault(content_key, {})[lang] = field

    for content_key, lang_fields in fields_by_key.items():
        for lang in ("en", "es"):
            field = lang_fields.get(lang, "")
            if not isinstance(result.get(field), str) or not str(result.get(field)).strip():
                missing_pairs.append(f"{content_key}_{lang}")

    for content_key, lang, field, filename in MARKDOWN_FIELDS:
        value = result.get(field)
        if not isinstance(value, str) or not value.strip():
            continue
        lang_dir = content_dir / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        path = lang_dir / filename
        path.write_text(value.strip() + "\n", encoding="utf-8")
        files[lang][content_key] = display_path(path)

    files = {lang: lang_files for lang, lang_files in files.items() if lang_files}
    if missing_pairs:
        result["missing_bilingual_markdown_fields"] = missing_pairs

    if files:
        (content_dir / "metadata.json").write_text(
            json.dumps(
                {
                    "id": result.get("id", ""),
                    "name": result.get("name", ""),
                    "status": result.get("status", ""),
                    "confidence": result.get("confidence", ""),
                    "recommended_etymology_type": result.get("recommended_etymology_type", ""),
                    "recommended_named_after": result.get("recommended_named_after", ""),
                    "previous_names": result.get("previous_names", ""),
                    "naming_date": result.get("naming_date", ""),
                    "sources": result.get("sources", []),
                    "corrections": result.get("corrections", []),
                    "open_questions": result.get("open_questions", []),
                    "missing_bilingual_markdown_fields": missing_pairs,
                    "markdown_files": files,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return files


def completed_content_ids(content_root: Path) -> set[str]:
    done: set[str] = set()
    if not content_root.exists():
        return done
    for meta_path in content_root.glob("*/metadata.json"):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            meta = {}
        station_id = meta.get("id") if isinstance(meta, dict) else None
        if isinstance(station_id, str) and station_id.strip():
            done.add(station_id.strip())
        else:
            done.add(meta_path.parent.name)
    return done


def completed_ids(output_dir: Path) -> set[str]:
    done: set[str] = set()
    path = output_dir / "results.jsonl"
    if not path.exists():
        return done
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            result = json.loads(line)
        except json.JSONDecodeError:
            continue
        station_id = result.get("id")
        if isinstance(station_id, str) and station_id:
            done.add(station_id)
    return done


async def run_one(
    idx: int,
    row: dict,
    instructions: str,
    output_dir: Path,
    content_root: Path,
    semaphore: asyncio.Semaphore,
) -> dict:
    name = str(row.get("name") or "?")[:48]
    row_dir = station_dir(output_dir, idx, row)
    row_dir.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(instructions, row)
    (row_dir / "prompt.md").write_text(prompt, encoding="utf-8")

    async with semaphore:
        for attempt in range(MAX_RETRIES + 1):
            print(f"  [{idx:04d}] {name:<48s} running attempt {attempt + 1}", flush=True)
            cmd = [
                "codex",
                "--search",
                "--ask-for-approval",
                "never",
                "--model",
                CODEX_MODEL,
                "--config",
                f'model_reasoning_effort="{CODEX_REASONING}"',
                "exec",
            ]
            if CODEX_JSON_EVENTS:
                cmd.append("--json")
            cmd.extend(["--cd", str(PROJECT_ROOT), "--sandbox", "danger-full-access", "-"])

            started_at = utc_now()
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout_b, stderr_b = await proc.communicate(input=prompt.encode())
            finished_at = utc_now()
            stdout = stdout_b.decode(errors="replace")
            stderr = stderr_b.decode(errors="replace")
            thread_id, final_text = extract_codex_json_summary(stdout)
            final_text = final_text or stdout

            prefix = f"attempt-{attempt + 1}"
            stdout_path = row_dir / (f"{prefix}-events.jsonl" if CODEX_JSON_EVENTS else f"{prefix}-stdout.md")
            stderr_path = row_dir / f"{prefix}-stderr.log"
            final_path = row_dir / f"{prefix}-final.md"
            result_path = row_dir / f"{prefix}-result.json"
            stdout_path.write_text(stdout, encoding="utf-8")
            stderr_path.write_text(stderr, encoding="utf-8")
            final_path.write_text(final_text, encoding="utf-8")

            result = extract_result(final_text) or extract_result(stdout)
            if proc.returncode == 75 and attempt < MAX_RETRIES:
                print(f"  [{idx:04d}] {name:<48s} rate limited; retrying", flush=True)
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
                continue

            if result is None:
                result = {
                    "id": row.get("id", ""),
                    "name": row.get("name", ""),
                    "operator": row.get("operator", ""),
                    "line": row.get("line", ""),
                    "status": "error",
                    "confidence": "unknown",
                    "research_note": f"no {RESULT_TAG} block returned; codex exit {proc.returncode}",
                }
            markdown_files = write_markdown_content(content_root, result)
            if markdown_files:
                result["markdown_files"] = markdown_files
            result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            index_row = {
                "idx": idx,
                "id": row.get("id", ""),
                "name": row.get("name", ""),
                "operator": row.get("operator", ""),
                "line": row.get("line", ""),
                "input_file": row.get("_input_file", ""),
                "return_code": proc.returncode,
                "status": result.get("status", "error"),
                "confidence": result.get("confidence", ""),
                "thread_id": thread_id or "",
                "result_path": str(result_path.relative_to(output_dir)),
                "final_path": str(final_path.relative_to(output_dir)),
                "stdout_path": str(stdout_path.relative_to(output_dir)),
                "stderr_path": str(stderr_path.relative_to(output_dir)),
                "started_at": started_at,
                "finished_at": finished_at,
            }
            print(
                f"  [{idx:04d}] {name:<48s} {index_row['status']} ({index_row['confidence']})",
                flush=True,
            )
            return {"index": index_row, "result": result}

    raise RuntimeError("unreachable")


async def run(args: argparse.Namespace) -> int:
    input_paths = [Path(p).resolve() for p in args.input_csv] if args.input_csv else DEFAULT_INPUTS
    missing = [p for p in [AGENT_INSTRUCTIONS, *input_paths] if not p.exists()]
    if missing:
        for path in missing:
            print(f"ERROR: not found: {path}", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir).resolve() if args.output_dir else (
        PROJECT_ROOT / "runs" / "station-research" / datetime.now().strftime("%Y%m%d-%H%M%S")
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "agent-transcripts").mkdir(exist_ok=True)
    content_root = Path(args.content_root).resolve()
    content_root.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_paths)
    if args.station_id:
        wanted = set(args.station_id)
        rows = [(idx, row) for idx, row in rows if row.get("id") in wanted]
    skipped_content = 0
    if not args.force:
        done_content = completed_content_ids(content_root)
        before = len(rows)
        rows = [(idx, row) for idx, row in rows if row.get("id") not in done_content]
        skipped_content = before - len(rows)
    if args.resume:
        done = completed_ids(output_dir)
        rows = [(idx, row) for idx, row in rows if row.get("id") not in done]
    if args.limit is not None:
        rows = rows[: args.limit]

    instructions = AGENT_INSTRUCTIONS.read_text(encoding="utf-8")
    print(f"Station research: {len(rows)} stations, concurrency={args.concurrency}")
    print(f"Output: {output_dir}")
    print(f"Content: {content_root}")
    if skipped_content:
        print(f"Skipped existing content: {skipped_content}")
    print(f"Model: {CODEX_MODEL}, reasoning={CODEX_REASONING}")

    semaphore = asyncio.Semaphore(args.concurrency)
    tasks = [run_one(idx, row, instructions, output_dir, content_root, semaphore) for idx, row in rows]
    results = await asyncio.gather(*tasks)

    index_rows: list[dict] = []
    for item in results:
        index_rows.append(item["index"])
        write_jsonl(output_dir / "results.jsonl", item["result"])
    write_indexes(output_dir, index_rows)

    counts: dict[str, int] = {}
    for item in results:
        status = str(item["index"].get("status") or "error")
        counts[status] = counts.get(status, 0) + 1
    print("\nRun summary:")
    for status, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {status:<10s} {count}")
    return 0 if not counts.get("error") else 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Agent-based Madrid station etymology research")
    parser.add_argument("--input-csv", action="append", help="Station CSV to process; repeatable")
    parser.add_argument("--output-dir", help="Output directory; default is runs/station-research/<timestamp>")
    parser.add_argument(
        "--content-root",
        default=str(DEFAULT_CONTENT_ROOT),
        help=f"Canonical Markdown/metadata directory (default: {DEFAULT_CONTENT_ROOT.relative_to(PROJECT_ROOT)})",
    )
    parser.add_argument("--station-id", action="append", help="Run only this station id; repeatable")
    parser.add_argument("--limit", "-n", type=int, help="Process only first N selected rows")
    parser.add_argument(
        "--concurrency",
        "-c",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max parallel Codex agents (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument("--resume", action="store_true", help="Skip station ids already present in results.jsonl")
    parser.add_argument("--force", action="store_true", help="Rerun stations even if canonical content already exists")
    args = parser.parse_args()
    sys.exit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
