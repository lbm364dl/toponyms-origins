#!/usr/bin/env python3
"""Build static site data from CSV files."""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

def build():
    all_entries = []
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

if __name__ == '__main__':
    build()
