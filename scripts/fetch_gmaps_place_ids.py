#!/usr/bin/env python3
"""
Fetch Google Maps Place IDs for all stations.
Usage: python3 scripts/fetch_gmaps_place_ids.py YOUR_API_KEY

Requires: Places API enabled on your Google Cloud project.
Free tier: $200/month credit (~40,000 requests).
"""
import csv
import json
import sys
import time
import urllib.request
import urllib.parse

if len(sys.argv) < 2:
    print("Usage: python3 scripts/fetch_gmaps_place_ids.py YOUR_API_KEY")
    sys.exit(1)

API_KEY = sys.argv[1]

def find_place(query, lat, lng):
    """Search for a place near given coordinates."""
    params = urllib.parse.urlencode({
        'input': query,
        'inputtype': 'textquery',
        'fields': 'place_id,name,formatted_address,geometry',
        'locationbias': f'circle:2000@{lat},{lng}',
        'key': API_KEY,
    })
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?{params}'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

# Load all stations
stations = []
for fname in ['data/madrid_metro_stations.csv', 'data/madrid_cercanias_stations.csv', 'data/madrid_metro_ligero_stations.csv']:
    cat = 'metro' if 'metro_stations' in fname else 'cercanias' if 'cercanias' in fname else 'metro_ligero'
    with open(fname, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            stations.append({
                'id': r['id'], 'name': r['name'], 'category': cat,
                'lat': r.get('latitude', ''), 'lng': r.get('longitude', ''),
            })

print(f"Looking up {len(stations)} stations...")

results = {}
ambiguous = []
not_found = []

for i, s in enumerate(stations):
    # Try different query formats
    queries = [
        f"Metro {s['name']}",
        f"Estación de {s['name']}",
        f"{s['name']} metro Madrid",
    ]
    if s['category'] == 'cercanias':
        queries = [
            f"Cercanías {s['name']}",
            f"Estación de Cercanías {s['name']}",
            f"{s['name']} cercanías Madrid",
        ]
    elif s['category'] == 'metro_ligero':
        queries = [
            f"Metro Ligero {s['name']}",
            f"Estación {s['name']}",
            f"{s['name']} metro ligero Madrid",
        ]

    found = False
    for query in queries:
        try:
            result = find_place(query, s['lat'], s['lng'])
            candidates = result.get('candidates', [])

            if len(candidates) == 1:
                c = candidates[0]
                place_id = c['place_id']
                gmaps_url = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
                results[s['id']] = {
                    'place_id': place_id,
                    'gmaps_name': c.get('name', ''),
                    'gmaps_url': gmaps_url,
                    'query_used': query,
                }
                found = True
                break
            elif len(candidates) > 1:
                # Multiple results -- try next query or flag
                continue
        except Exception as e:
            print(f"  Error for {s['name']}: {e}")
            continue

        time.sleep(0.05)  # Rate limit

    if not found:
        # Try one more time with the best query
        try:
            result = find_place(queries[0], s['lat'], s['lng'])
            candidates = result.get('candidates', [])
            if candidates:
                c = candidates[0]  # Take first result
                place_id = c['place_id']
                results[s['id']] = {
                    'place_id': place_id,
                    'gmaps_name': c.get('name', ''),
                    'gmaps_url': f"https://www.google.com/maps/place/?q=place_id:{place_id}",
                    'query_used': queries[0],
                    'ambiguous': len(candidates) > 1,
                }
                if len(candidates) > 1:
                    ambiguous.append(s['name'])
            else:
                not_found.append(s['name'])
        except:
            not_found.append(s['name'])

    if (i + 1) % 50 == 0:
        print(f"  {i + 1}/{len(stations)} done...")
    time.sleep(0.05)

# Save results
with open('docs/data/gmaps_place_ids.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone! {len(results)} Place IDs found, {len(ambiguous)} ambiguous, {len(not_found)} not found.")
if ambiguous:
    print(f"\nAmbiguous (needs manual review): {ambiguous}")
if not_found:
    print(f"\nNot found: {not_found}")

# Update app.js to use place IDs
print(f"\nSaved to docs/data/gmaps_place_ids.json")
print("Now run: python3 scripts/build_site.py")
