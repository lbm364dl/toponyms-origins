#!/bin/bash
# Fetch all streets in Madrid that have etymology data in OpenStreetMap
# Uses the Overpass API to query for name:etymology:wikidata tags

OUTPUT_DIR="$(dirname "$0")/../data/osm"
mkdir -p "$OUTPUT_DIR"

echo "=== Fetching Madrid streets with etymology data from OpenStreetMap ==="
echo "Using Overpass API..."

# Query 1: Streets with name:etymology:wikidata tag
echo ""
echo "--- Query 1: Streets with Wikidata etymology tags ---"
curl -s -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:120];
area["name"="Madrid"]["admin_level"="8"]->.madrid;
(
  way["highway"]["name:etymology:wikidata"](area.madrid);
  way["highway"]["name:etymology"](area.madrid);
);
out body;
>;
out skel qt;' \
  -o "$OUTPUT_DIR/madrid_streets_etymology.json"

if [ $? -eq 0 ]; then
  COUNT=$(python3 -c "import json; d=json.load(open('$OUTPUT_DIR/madrid_streets_etymology.json')); print(len([e for e in d.get('elements',[]) if e.get('type')=='way']))" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_streets_etymology.json ($COUNT ways with etymology)"
else
  echo "ERROR: Failed to fetch street etymology data"
fi

# Query 2: Metro stations with etymology
echo ""
echo "--- Query 2: Metro stations with Wikidata etymology tags ---"
curl -s -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:60];
area["name"="Madrid"]["admin_level"="4"]->.madrid;
(
  node["railway"="station"]["network"~"Metro"](area.madrid);
  node["railway"="station"]["operator"~"Metro"](area.madrid);
  node["station"="subway"](area.madrid);
);
out body;' \
  -o "$OUTPUT_DIR/madrid_metro_stations_osm.json"

if [ $? -eq 0 ]; then
  COUNT=$(python3 -c "import json; d=json.load(open('$OUTPUT_DIR/madrid_metro_stations_osm.json')); print(len(d.get('elements',[])))" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_metro_stations_osm.json ($COUNT stations)"
else
  echo "ERROR: Failed to fetch metro station data"
fi

# Query 3: All named places with etymology in Madrid community
echo ""
echo "--- Query 3: All named features with etymology in Community of Madrid ---"
curl -s -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode 'data=[out:json][timeout:120];
area["name"="Comunidad de Madrid"]["admin_level"="4"]->.cm;
(
  way["name:etymology:wikidata"](area.cm);
  node["name:etymology:wikidata"](area.cm);
  relation["name:etymology:wikidata"](area.cm);
);
out body;
>;
out skel qt;' \
  -o "$OUTPUT_DIR/madrid_community_etymology.json"

if [ $? -eq 0 ]; then
  COUNT=$(python3 -c "import json; d=json.load(open('$OUTPUT_DIR/madrid_community_etymology.json')); print(len([e for e in d.get('elements',[]) if 'tags' in e]))" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_community_etymology.json ($COUNT features with etymology)"
else
  echo "ERROR: Failed to fetch community etymology data"
fi

echo ""
echo "=== Done ==="
echo "Output files in: $OUTPUT_DIR/"
echo ""
echo "Next steps:"
echo "  1. Run scripts/query_wikidata.sh to get structured person data"
echo "  2. Run scripts/process_osm_data.py to convert to CSV"
