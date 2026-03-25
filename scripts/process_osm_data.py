#!/usr/bin/env python3
"""
Process OSM etymology data into a structured CSV.
Extracts name:etymology:wikidata tags from the Overpass API JSON output
and produces a deduplicated list of unique street names with their Wikidata etymology IDs.
"""

import json
import csv
import os
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
OSM_FILE = os.path.join(DATA_DIR, 'osm', 'madrid_streets_etymology.json')
OUTPUT_FILE = os.path.join(DATA_DIR, 'osm', 'madrid_osm_etymology_processed.csv')

def main():
    with open(OSM_FILE) as f:
        data = json.load(f)

    # Group by street name to deduplicate (same street = many OSM ways)
    streets = defaultdict(lambda: {
        'name': '',
        'wikidata_ids': set(),
        'etymology_text': set(),
        'highway_types': set(),
        'count': 0,
    })

    for element in data['elements']:
        if element.get('type') != 'way' or 'tags' not in element:
            continue

        tags = element['tags']
        name = tags.get('name', '')
        if not name:
            continue

        ety_wd = tags.get('name:etymology:wikidata', '')
        ety_txt = tags.get('name:etymology', '')
        highway = tags.get('highway', '')

        entry = streets[name]
        entry['name'] = name
        if ety_wd:
            # Some entries have multiple Q-ids separated by ;
            for qid in ety_wd.split(';'):
                entry['wikidata_ids'].add(qid.strip())
        if ety_txt:
            entry['etymology_text'].add(ety_txt)
        if highway:
            entry['highway_types'].add(highway)
        entry['count'] += 1

    # Write CSV
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'name',
            'etymology_wikidata_ids',
            'etymology_text',
            'highway_types',
            'osm_way_count',
        ])

        for name in sorted(streets.keys()):
            entry = streets[name]
            writer.writerow([
                entry['name'],
                ';'.join(sorted(entry['wikidata_ids'])),
                '; '.join(sorted(entry['etymology_text'])) if entry['etymology_text'] else '',
                ';'.join(sorted(entry['highway_types'])),
                entry['count'],
            ])

    print(f"Processed {len(streets)} unique street names from {sum(s['count'] for s in streets.values())} OSM ways")
    print(f"Output: {OUTPUT_FILE}")

    # Stats
    with_wd = sum(1 for s in streets.values() if s['wikidata_ids'])
    with_txt = sum(1 for s in streets.values() if s['etymology_text'])
    print(f"\nStats:")
    print(f"  Streets with Wikidata etymology: {with_wd}")
    print(f"  Streets with text etymology: {with_txt}")
    print(f"  Total unique streets: {len(streets)}")

    # Sample some interesting ones
    print(f"\nSample entries:")
    for name in sorted(streets.keys())[:15]:
        entry = streets[name]
        qids = ';'.join(sorted(entry['wikidata_ids']))
        txt = '; '.join(sorted(entry['etymology_text']))[:50] if entry['etymology_text'] else ''
        print(f"  {name}: {qids} {txt}")

if __name__ == '__main__':
    main()
