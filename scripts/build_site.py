#!/usr/bin/env python3
"""Build static site data from CSV files."""
import csv
import json
import os
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = Path(ROOT)

FILES = {
    'metro': 'data/madrid_metro_stations.csv',
    'cercanias': 'data/madrid_cercanias_stations.csv',
    'metro_ligero': 'data/madrid_metro_ligero_stations.csv',
    'districts': 'data/madrid_districts.csv',
    'neighbourhoods': 'data/madrid_neighbourhoods.csv',
    'plazas_parks': 'data/madrid_plazas_parks.csv',
    'streets': 'data/madrid_streets.csv',
}

TRANSLATIONS_FILE = os.path.join(ROOT, 'docs', 'data', 'translations_es.json')
LINE_ORDER_FILE = os.path.join(ROOT, 'docs', 'data', 'line_orders.json')
GMAPS_FILE = os.path.join(ROOT, 'docs', 'data', 'gmaps_place_ids.json')
NAMED_AFTER_ES_FILE = os.path.join(ROOT, 'docs', 'data', 'named_after_es.json')
CONTENT_STATIONS_DIR = ROOT_PATH / 'content' / 'stations'

CONTENT_MARKDOWN_FILES = {
    'summary.short.md': 'content_summary_short',
    'summary.md': 'content_summary',
    'story.md': 'content_story',
    'confidence.md': 'content_confidence_reason',
    'current-claim-assessment.md': 'content_current_claim_assessment',
    'research-note.md': 'content_research_note',
}

def read_text_if_exists(path):
    if not path.exists():
        return ''
    return path.read_text(encoding='utf-8').strip()

def load_station_content():
    content = {}
    if not CONTENT_STATIONS_DIR.exists():
        return content

    for station_dir in sorted(CONTENT_STATIONS_DIR.iterdir()):
        if not station_dir.is_dir():
            continue
        meta_path = station_dir / 'metadata.json'
        if not meta_path.exists():
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            continue

        station_id = meta.get('id') or station_dir.name
        entry_content = {
            'has_content_entry': 'true',
            'content_metadata_path': str(meta_path.relative_to(ROOT_PATH)),
            'content_status': meta.get('status', ''),
            'content_confidence': meta.get('confidence', ''),
            'sources_structured': meta.get('sources', []),
            'corrections': meta.get('corrections', []),
            'open_questions': meta.get('open_questions', []),
        }

        field_map = {
            'recommended_etymology_type': 'etymology_type',
            'recommended_named_after': 'named_after',
            'previous_names': 'previous_names',
            'naming_date': 'naming_date',
            'confidence': 'confidence',
        }
        for src, dest in field_map.items():
            value = meta.get(src)
            if isinstance(value, str) and value.strip():
                entry_content[dest] = value.strip()

        for lang in ('en', 'es'):
            lang_dir = station_dir / lang
            for filename, field_base in CONTENT_MARKDOWN_FILES.items():
                value = read_text_if_exists(lang_dir / filename)
                if value:
                    entry_content[f'{field_base}_{lang}'] = value

        content[station_id] = entry_content

    return content

def build():
    all_entries = []
    station_content = load_station_content()
    for key, relpath in FILES.items():
        path = os.path.join(ROOT, relpath)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                entry = {}
                for k, v in row.items():
                    if v is None:
                        continue
                    if isinstance(v, list):
                        v = ','.join(v)
                    v = v.strip()
                    if v:
                        entry[k] = v
                entry['_category'] = key
                content_entry = station_content.get(entry.get('id', ''))
                if content_entry:
                    entry.update(content_entry)
                all_entries.append(entry)

    # Merge Google Maps Place IDs if available
    if os.path.exists(GMAPS_FILE):
        with open(GMAPS_FILE, 'r', encoding='utf-8') as f:
            gmaps = json.load(f)
        for entry in all_entries:
            gdata = gmaps.get(entry.get('id', ''))
            if gdata and 'gmaps_url' in gdata:
                entry['gmaps_url'] = gdata['gmaps_url']
        print(f"  Merged {sum(1 for e in all_entries if 'gmaps_url' in e)} Google Maps Place URLs")

    # Merge named_after Spanish translations
    if os.path.exists(NAMED_AFTER_ES_FILE):
        with open(NAMED_AFTER_ES_FILE, 'r', encoding='utf-8') as f:
            na_es = json.load(f)
        for entry in all_entries:
            es_text = na_es.get(entry.get('id', ''))
            if es_text:
                entry['named_after_es'] = es_text
        print(f"  Merged {sum(1 for e in all_entries if 'named_after_es' in e)} named_after ES translations")

    # Merge Spanish translations if available
    if os.path.exists(TRANSLATIONS_FILE):
        with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
            translations = json.load(f)
        for entry in all_entries:
            es_text = translations.get(entry.get('id', ''))
            if es_text:
                entry['etymology_summary_es'] = es_text
        print(f"  Merged {sum(1 for e in all_entries if 'etymology_summary_es' in e)} Spanish translations")

    out_dir = os.path.join(ROOT, 'docs', 'data')
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, 'entries.json'), 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False)

    with open(os.path.join(out_dir, 'entries.js'), 'w', encoding='utf-8') as f:
        f.write('const ENTRIES_DATA = ')
        json.dump(all_entries, f, ensure_ascii=False)
        f.write(';')

    print(f"Built {len(all_entries)} entries -> docs/data/entries.json + entries.js")
    if station_content:
        merged = sum(1 for e in all_entries if e.get('has_content_entry') == 'true')
        print(f"  Merged {merged} station content entries from content/stations")

if __name__ == '__main__':
    build()
