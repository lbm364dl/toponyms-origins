#!/bin/bash
# Query Wikidata SPARQL endpoint for Madrid streets with "named after" (P138) data
# and for biographical data of people that Madrid streets/stations are named after

OUTPUT_DIR="$(dirname "$0")/../data/wikidata"
mkdir -p "$OUTPUT_DIR"

echo "=== Querying Wikidata for Madrid name origin data ==="

# Query 1: All Madrid streets in Wikidata that have P138 ("named after")
echo ""
echo "--- Query 1: Madrid streets with 'named after' property ---"
SPARQL_QUERY_1=$(cat <<'SPARQL'
SELECT ?street ?streetLabel ?namedAfter ?namedAfterLabel ?namedAfterDescription
       ?genderLabel ?birthYear ?deathYear ?occupationLabel ?nationalityLabel
WHERE {
  ?street wdt:P31 wd:Q79007 .           # instance of: street
  ?street wdt:P131+ wd:Q2807 .          # located in: Madrid (recursive)
  ?street wdt:P138 ?namedAfter .         # named after
  OPTIONAL { ?namedAfter wdt:P21 ?gender . }
  OPTIONAL { ?namedAfter wdt:P569 ?birth . BIND(YEAR(?birth) AS ?birthYear) }
  OPTIONAL { ?namedAfter wdt:P570 ?death . BIND(YEAR(?death) AS ?deathYear) }
  OPTIONAL { ?namedAfter wdt:P106 ?occupation . }
  OPTIONAL { ?namedAfter wdt:P27 ?nationality . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" . }
}
ORDER BY ?streetLabel
SPARQL
)

curl -s -G "https://query.wikidata.org/sparql" \
  --data-urlencode "query=$SPARQL_QUERY_1" \
  -H "Accept: text/csv" \
  -o "$OUTPUT_DIR/madrid_streets_named_after.csv"

if [ $? -eq 0 ]; then
  LINES=$(wc -l < "$OUTPUT_DIR/madrid_streets_named_after.csv" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_streets_named_after.csv ($LINES rows)"
else
  echo "ERROR: Failed to query streets"
fi

# Query 2: Madrid Metro stations in Wikidata with P138
echo ""
echo "--- Query 2: Madrid Metro stations with 'named after' property ---"
SPARQL_QUERY_2=$(cat <<'SPARQL'
SELECT ?station ?stationLabel ?namedAfter ?namedAfterLabel ?namedAfterDescription
       ?genderLabel ?birthYear ?deathYear ?occupationLabel
       ?lineLabel ?openingDate ?coords
WHERE {
  ?station wdt:P31 wd:Q928830 .          # instance of: metro station
  ?station wdt:P361 wd:Q54300 .          # part of: Metro de Madrid
  OPTIONAL { ?station wdt:P138 ?namedAfter .
    OPTIONAL { ?namedAfter wdt:P21 ?gender . }
    OPTIONAL { ?namedAfter wdt:P569 ?birth . BIND(YEAR(?birth) AS ?birthYear) }
    OPTIONAL { ?namedAfter wdt:P570 ?death . BIND(YEAR(?death) AS ?deathYear) }
    OPTIONAL { ?namedAfter wdt:P106 ?occupation . }
  }
  OPTIONAL { ?station wdt:P81 ?line . }
  OPTIONAL { ?station wdt:P1619 ?openingDate . }
  OPTIONAL { ?station wdt:P625 ?coords . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" . }
}
ORDER BY ?stationLabel
SPARQL
)

curl -s -G "https://query.wikidata.org/sparql" \
  --data-urlencode "query=$SPARQL_QUERY_2" \
  -H "Accept: text/csv" \
  -o "$OUTPUT_DIR/madrid_metro_named_after.csv"

if [ $? -eq 0 ]; then
  LINES=$(wc -l < "$OUTPUT_DIR/madrid_metro_named_after.csv" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_metro_named_after.csv ($LINES rows)"
else
  echo "ERROR: Failed to query metro stations"
fi

# Query 3: All Madrid districts and barrios in Wikidata
echo ""
echo "--- Query 3: Madrid districts and barrios ---"
SPARQL_QUERY_3=$(cat <<'SPARQL'
SELECT ?place ?placeLabel ?placeDescription ?namedAfter ?namedAfterLabel ?coords
WHERE {
  {
    ?place wdt:P31 wd:Q3382768 .         # district of Madrid
  } UNION {
    ?place wdt:P31 wd:Q15715365 .        # barrio of Madrid
    ?place wdt:P131+ wd:Q2807 .
  }
  OPTIONAL { ?place wdt:P138 ?namedAfter . }
  OPTIONAL { ?place wdt:P625 ?coords . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" . }
}
ORDER BY ?placeLabel
SPARQL
)

curl -s -G "https://query.wikidata.org/sparql" \
  --data-urlencode "query=$SPARQL_QUERY_3" \
  -H "Accept: text/csv" \
  -o "$OUTPUT_DIR/madrid_districts_barrios.csv"

if [ $? -eq 0 ]; then
  LINES=$(wc -l < "$OUTPUT_DIR/madrid_districts_barrios.csv" 2>/dev/null || echo "?")
  echo "Downloaded: $OUTPUT_DIR/madrid_districts_barrios.csv ($LINES rows)"
else
  echo "ERROR: Failed to query districts/barrios"
fi

echo ""
echo "=== Done ==="
echo "Output files in: $OUTPUT_DIR/"
