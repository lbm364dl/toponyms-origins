# Content

Canonical public research content for the site.

## Stations

Station research lives in `content/stations/<station_id>/`.

Each completed station has:

```text
metadata.json
en/
  summary.short.md
  summary.md
  story.md
  confidence.md
  current-claim-assessment.md
  research-note.md
es/
  summary.short.md
  summary.md
  story.md
  confidence.md
  current-claim-assessment.md
  research-note.md
```

`scripts/run_station_research.py` writes this folder by default and skips
stations that already have `metadata.json` unless `--force` is used.

## Public and internal fields

The canonical reader-facing fields are `summary.short.md`, `summary.md`, and
`story.md` in each language, plus `sources[].relevance_es` in `metadata.json`
for the current Spanish site. These files must contain finished, neutral prose,
not research status, draft commentary, or instructions for an editor.

`confidence.md`, `current-claim-assessment.md`, `research-note.md`,
`corrections`, and `open_questions` are internal research/review fields. They
may discuss evidence gaps and follow-up work, but that workflow voice must not
be copied into public fields.

Public content problems are fixed here in the canonical source. Do not add a
renderer-only cleanup to `scripts/build_site.py` or hand-edit generated files
under `docs/`.
