# Madrid Name Origins Dataset

A comprehensive dataset documenting **why things in Madrid are named the way they are** — streets, metro stations, Cercanias stations, Metro Ligero stops, neighbourhoods, districts, plazas, and more.

## Status

**Phase 1: Research** (complete) — Identified 140+ sources worldwide: datasets, books, academic papers, blogs, institutional programs.
**Phase 2: Dataset Design** (complete) — Schema designed, all CSV files structured and validated.
**Phase 3: Data Collection** (in progress) — 475 hand-curated transport station entries with etymology + 1,427 programmatic entries from OSM + 488 from Wikidata.

## What's Here

```
├── README.md                              # This file
├── SOURCES.md                             # Master catalogue of all 140+ sources
├── data/
│   ├── schema.md                          # Dataset schema documentation
│   ├── madrid_metro_stations.csv          # 243 Metro stations with etymology (ALL lines 1-12 + Ramal)
│   ├── madrid_cercanias_stations.csv      # 95 Cercanias stations with etymology (ALL lines)
│   ├── madrid_metro_ligero_stations.csv   # 52 Metro Ligero + Tranvia stations (ALL lines)
│   ├── madrid_districts.csv              # All 21 distritos with etymology
│   ├── madrid_neighbourhoods.csv          # 20 key barrios with etymology
│   ├── madrid_plazas_parks.csv            # 14 plazas, parks, monuments
│   ├── madrid_streets.csv                 # 30 seed streets with etymology
│   ├── osm/
│   │   ├── madrid_streets_etymology.json  # Raw OSM Overpass data (6.5 MB)
│   │   └── madrid_osm_etymology_processed.csv  # 1,427 unique streets with Wikidata IDs
│   └── wikidata/
│       └── madrid_streets_named_after.csv # 488 streets with biographical data
├── research/
│   ├── street-name-origins.md             # Street name datasets worldwide (73 sources)
│   ├── transport-stations.md              # Metro/Cercanias/ML deep research (67 KB)
│   ├── correspondencia-con-la-historia.md # 55 RAH biographical metro stations
│   ├── toponymy.md                        # Neighbourhood/district toponymy
│   ├── international.md                   # International projects & models
│   └── physical-books-guide.md            # Library research guide (11 books + articles)
└── scripts/
    ├── fetch_osm_etymology.sh             # Query OSM Overpass for etymology data
    ├── query_wikidata.sh                  # Query Wikidata SPARQL for "named after"
    └── process_osm_data.py                # Deduplicate OSM ways into unique streets
```

## Dataset Summary

| File | Entries | Coverage |
|------|---------|----------|
| `madrid_metro_stations.csv` | **243** | ALL Metro stations (lines 1-12 + Ramal), all with etymology |
| `madrid_cercanias_stations.csv` | **95** | ALL Cercanias Madrid stations (C-1 to C-10), all with etymology |
| `madrid_metro_ligero_stations.csv` | **52** | ALL ML1/ML2/ML3 + Tranvia de Parla stations |
| `madrid_districts.csv` | **21** | All 21 distritos |
| `madrid_neighbourhoods.csv` | **20** | Key barrios |
| `madrid_plazas_parks.csv` | **14** | Major plazas, parks, monuments |
| `madrid_streets.csv` | **30** | Seed streets (hand-curated) |
| `osm_etymology_processed.csv` | **1,427** | Unique streets with Wikidata etymology IDs (from OSM) |
| `wikidata_streets_named_after.csv` | **488** | Streets with full biographical "named after" data |
| **Total hand-curated** | **475** | Transport stations + districts + neighbourhoods + streets |
| **Total with any etymology** | **~2,100** | |

## Key Finding

**No single open dataset exists for Madrid name origins.** Paris, Barcelona, and Donostia have structured municipal etymology datasets. Madrid does not. This project fills that gap.

## Key Books (for metro station etymology)

| Book | Author | Year | What |
|------|--------|------|------|
| **Metro de Madrid: Por que sus estaciones se llaman asi?** | Jose Felipe Alonso Fernandez-Checa | 2023 | ALL 302+ station name origins (THE definitive resource) |
| **El alma del suburbano madrileno** (565pp) | Olivares & Molina / Comunidad de Madrid | 2025 | First 42 stations 1919-1944 ([FREE PDF at COAM](https://www.fundacioncoam.org/media/Default%20Files/fundacion/biblioteca/donativos%20editoriales%20institucionales%202025/el-alma-del-suburbano-madrileno.pdf)) |
| **100 Anos de la Linea Norte-Sur: De Cuatro Caminos a Sol** | Antonio Martinez Moreno | 2019 | Line 1 first 8 stations (Kindle available) |
| **De Sol al Puente de Vallecas** | Antonio Martinez Moreno | 2021 | Line 1 southern extension |
| **Metro de Madrid 1919-2009: Noventa anos de historia** (544pp) | Aurora Moya Rodriguez | 2009 | Definitive network history |
| **Toponimia madrilena: proceso evolutivo** (2 vols + CD) | Luis Miguel Aparisi Laporta | 2001 | 20,000+ Madrid toponyms (streets + places) |
| **Los nombres de las calles de Madrid** | Maria Isabel Gea Ortigas | 1993-2020 | 1,000+ street name origins |
| **Historias de las calles de Madrid** (456pp) | Jose Luis Rodriguez-Checa | 2021 | 959 streets with origins |

## "Correspondencia con la Historia" Program

Metro de Madrid + Real Academia de la Historia collaboration (2015-2016). Biographical panels installed in **55 confirmed stations** (of 58 announced) named after historical figures, with QR codes to RAH's Diccionario Biografico Espanol. Full documentation in `research/correspondencia-con-la-historia.md`.

## Data Sources

See [SOURCES.md](SOURCES.md) for the complete catalogue of 140+ sources.

## Etymology Type Breakdown (Metro stations)

| Type | Count | Examples |
|------|-------|---------|
| place | 91 | Bilbao, Colombia, Ibiza, Oporto, Alcorcon Central, Ciudad de los Angeles |
| person | 64 | Goya, Tirso de Molina, Paco de Lucia, Miguel Hernandez, La Elipa |
| descriptive | 45 | Cuatro Caminos, Almendrales, Arroyofresno, Arroyo Culebro |
| historical | 21 | Sol, Embajadores, Tribunal, Casa del Reloj, La Peseta |
| religious | 19 | Noviciado, Iglesia, Santo Domingo, San Nicasio, Pan Bendito |
| event | 3 | Callao, Tetuan, Aviacion Espanola |

## License

Dataset: CC-BY-SA 4.0 (compatible with OSM/Wikidata sources)
