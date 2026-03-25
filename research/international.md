# International Examples: Street Name Etymology Datasets & Projects

Research conducted 2026-03-25. Summary of datasets, projects, and structured data sources
documenting the origins/etymology of place names (streets, stations, neighbourhoods) worldwide.

---

## 1. CORE INFRASTRUCTURE: Wikidata + OpenStreetMap

### 1a. Wikidata Property P138 ("named after")

- **URL**: https://www.wikidata.org/wiki/Property:P138
- **What it contains**: A structured property linking any Wikidata entity (including streets)
  to the entity it was named after. Related properties: P825 (dedicated to), P547 (commemorates).
- **Format**: Wikidata triples, queryable via SPARQL at https://query.wikidata.org/
- **Coverage**: Global, but uneven. Some cities (e.g., San Francisco, Paris, Vienna) have
  extensive P138 data for streets; others (e.g., London) have far less.
- **Key SPARQL properties for streets**:
  - P31 = Q79007 (instance of: street)
  - P17 (country)
  - P131 (located in administrative entity)
  - P138 (named after)
  - P21 (sex or gender of the person named after)
- **Madrid relevance**: Can query Wikidata for all Madrid streets (P131 = Q2807) that have
  P138 set. This would be the foundation for a structured dataset. Currently, coverage
  for Madrid streets in Wikidata is incomplete but growing.

### 1b. OpenStreetMap `name:etymology` Tags

- **Wiki page**: https://wiki.openstreetmap.org/wiki/Key:name:etymology
- **Wikidata variant**: https://wiki.openstreetmap.org/wiki/Key:name:etymology:wikidata
- **TagInfo stats**: https://taginfo.openstreetmap.org/keys/name:etymology
- **What it contains**: OSM tags that record what a street/place is named after.
  - `name:etymology=*` -- free text description of namesake
  - `name:etymology:wikidata=*` -- Wikidata Q-identifier of namesake (machine-readable)
  - `name:etymology:wikipedia=*` -- Wikipedia article about namesake
- **Format**: OSM tags on way/node/relation elements. Queryable via Overpass API.
- **Status**: De facto community standard. Used by multiple consumer projects.
- **Madrid relevance**: Can query all Madrid streets with etymology data via Overpass:
  ```
  [out:json][timeout:60];
  area["name"="Madrid"]["admin_level"="8"]->.madrid;
  way["highway"]["name:etymology:wikidata"](area.madrid);
  out body;
  ```

---

## 2. INTERACTIVE MAP PROJECTS

### 2a. Open Etymology Map (by Daniele Santini)

- **URL**: https://etymology.dsantini.it/
- **Source code**: https://github.com/Danysan1/open-etymology-map
  (mirror of https://gitlab.com/openetymologymap/open-etymology-map)
- **What it does**: Global interactive map showing etymology of street names and POIs.
  Click any street to see who/what it is named after, with biographical details.
- **Data sources**: Combines OSM (`name:etymology:wikidata`, `subject:wikidata`) with
  Wikidata SPARQL lookups for biographical metadata.
- **Tech stack**: Python, PHP, TypeScript, SPARQL, MapLibre GL JS, Overpass API,
  PostGIS, Apache Airflow.
- **Format**: GeoJSON via API, backed by PostGIS.
- **Madrid relevance**: Already works for Madrid -- displays whatever etymology data exists
  in OSM+Wikidata for Madrid streets. Could be used as a front-end model or data validation
  tool. The architecture (OSM + Wikidata SPARQL) is exactly the pattern to follow.

### 2b. OSMetymology (by Peter Brodersen)

- **URL**: https://navne.findvej.dk/ (Denmark-focused)
- **Source code**: https://github.com/PeterBrodersen/osmetymology
- **What it does**: Etymology map for Denmark, showing gender breakdown by municipality.
- **Data sources**: OSM + Wikidata.
- **Tech stack**: PostgreSQL/PostGIS, generates FlatGeobuf and CSV files.
- **Format**: FlatGeobuf, CSV, PostGIS tables.
- **Madrid relevance**: Good technical model for generating static export files (CSV,
  FlatGeobuf) from the OSM+Wikidata pipeline. The gender-breakdown approach could be
  replicated.

### 2c. MapComplete Etymology Theme

- **URL**: https://mapcomplete.org/etymology
- **Source code**: https://github.com/pietervdvn/MapComplete
- **What it does**: A browser-based editor for adding/editing etymology data directly
  in OpenStreetMap. Shows existing etymology data and prompts users to add missing data.
- **Data sources**: Reads/writes OSM directly.
- **Format**: OSM tags (direct editing).
- **Madrid relevance**: This is the primary tool for crowdsourcing etymology data for
  Madrid streets. Could be promoted to local Madrid OSM contributors to improve coverage.

### 2d. Paristique

- **URL**: https://www.paristique.fr/
- **Creator**: Guillaume Derolez
- **What it does**: Interactive map of Paris showing the origin of every street name.
  Click a point to see name origin, date of creation, arrondissement, and neighbourhood.
- **Data source**: Paris Open Data ("Denominations des emprises des voies actuelles").
- **Format**: Web application consuming open data CSV/JSON.
- **Madrid relevance**: Excellent UX model for a Madrid equivalent. Demonstrates how a
  single municipal open data source can power an engaging interactive experience.
  Madrid's callejero dataset could serve a similar role.

---

## 3. GENDER & DIVERSITY ANALYSIS PROJECTS

### 3a. EqualStreetNames

- **URL**: https://equalstreetnames.org/ / https://equalstreetnames.eu/
- **Source code**: https://github.com/EqualStreetNames/equalstreetnames
- **What it does**: Visualizes street names by gender across 63 cities in 21 countries.
  Color-codes streets by gender of the person they are named after.
- **Data sources**: OSM (highway/place/leisure ways) + Wikidata (P138 + P21 for gender).
- **Coverage**: 63 cities including many European capitals.
- **Format**: GeoJSON, web visualization.
- **Madrid relevance**: Madrid is not yet in EqualStreetNames but could be added.
  The methodology (match OSM streets to Wikidata via name:etymology:wikidata, then
  query P21 for gender) is directly applicable.

### 3b. EDJNet Mapping Diversity

- **URL**: https://mappingdiversity.eu/
- **Source code**: https://github.com/EDJNet/mapping_diversity
- **Dataset release**: https://www.europeandatajournalism.eu/cp_data_news/mapping-diversity-full-dataset-release/
- **What it does**: Largest journalistic analysis of street name diversity in Europe.
  Covers 155,468 streets across 32 cities in 19 countries. Analyzes gender, profession,
  nationality of namesakes.
- **Data sources**: OSM (via Geofabrik extracts) + Wikidata (automated matching + manual
  verification).
- **Cities covered**: Athens, Berlin, Brussels, Bucharest, Budapest, Chisinau, Copenhagen,
  Kyiv, Lisbon, **Madrid**, Paris, Prague, Rome, Stockholm, Vienna, Warsaw, Zagreb, and more.
- **Format**: R scripts for processing, Excel aggregate results, CC BY-SA 4.0 license.
- **Occupations categorized into**: politics/government, military, religion,
  culture/science/arts, other professions.
- **Key finding for Madrid**: Madrid has 18.7% streets named after women (2nd highest
  in the study after Stockholm at 19.5%). However, Madrid was excluded from detailed
  profiling due to <75% Wikidata coverage of women.
- **Madrid relevance**: HIGH. This project already has partial Madrid data and demonstrates
  the exact methodology. The gap (<75% Wikidata coverage) is precisely what a Madrid
  etymology project should aim to fill.

---

## 4. STRUCTURED DATASETS

### 4a. Streetonomics Dataset

- **Paper**: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0252869
- **Data**: https://social-dynamics.net/streetonomics/data
- **What it contains**: 4,932 honorific street names across Paris, Vienna, London, and
  New York with structured data about the person each street is named after.
- **Fields include**: Street name, city, honoree name, gender, nationality, birth/death
  year, profession, whether local or foreign.
- **Format**: Downloadable dataset (CSV).
- **License**: Open for research use.
- **Madrid relevance**: While Madrid is not covered, this is the gold standard for a
  structured "street + honoree" dataset. The schema (street, person, gender, profession,
  birth/death, nationality) is directly applicable as a model for Madrid.

### 4b. StNamesLab / StreetNamesDatabase

- **URL**: https://github.com/StNamesLab/StreetNamesDatabase
- **Website**: https://en.stnameslab.com/data/
- **Paper**: "Tabulating and Visualizing Street Name Data in the US and Europe" (2023)
- **What it contains**: Processed street name database for North America and much of Europe,
  derived from OpenStreetMap. Includes a specific Spain dataset with historical data
  (2001-2022) from the Instituto Nacional de Estadistica.
- **Format**: CSV files ($ delimiter), EPSG:4326 CRS, UTF-8 encoding.
  Spain 2001-2022 files use Latin1 encoding.
- **Countries**: Europe (multiple), US, Canada, Mexico. Spain has special treatment
  with INE historical data.
- **License**: ODbL (OSM data), CC BY-SA 4.0 (Spain INE data).
- **Madrid relevance**: HIGH. Contains Spain-specific data with historical evolution.
  The StNamesLab web apps allow searching and visualizing spatial distribution of
  street names. This could be a starting data source for Madrid street names, though
  it focuses on the names themselves rather than their etymology.

### 4c. Paris Open Data -- "Denominations des emprises des voies actuelles"

- **URL**: https://opendata.paris.fr/explore/dataset/denominations-emprises-voies-actuelles/
- **Also on**: https://www.data.gouv.fr/datasets/denominations-des-emprises-des-voies-actuelles
- **What it contains**: Official nomenclature of all Paris streets including:
  - Official name
  - Arrondissement and quarter
  - Physical dimensions
  - Start and end points
  - **Previous names** (historical evolution)
  - **Origin of the current name** (etymology/reason for naming)
  - Date of designation
  - Regulatory texts (decrees, ordinances)
- **Format**: CSV, JSON, API (ODbL license).
- **Source**: Department of Topography and Land Documentation, City of Paris.
- **Madrid relevance**: VERY HIGH. This is the closest model to what a Madrid project
  should produce. The Madrid callejero dataset exists but lacks the "origin of name"
  field. Adding etymology data to Madrid's existing callejero would create an equivalent
  resource.

---

## 5. MADRID-SPECIFIC EXISTING RESOURCES

### 5a. Madrid Open Data -- Callejero Oficial

- **URL**: https://datos.madrid.es/ (search "callejero")
- **Datasets**:
  - Callejero vigente (current streets, daily updates)
  - Callejero con evolucion historica (historical street name changes)
  - Additional info: postal codes, SER zones, fiscal categories
- **Records**: ~9,139 current streets + ~2,819 historical streets + ~2,170 toponyms
  + ~195,000 portal numbers.
- **Format**: CSV, RDF.
- **Limitation**: Does NOT include etymology/origin of names. Contains street names,
  codes, districts, coordinates, but not WHY a street has its name.
- **Madrid relevance**: This is the base dataset to which etymology data should be added.

### 5b. Calles de Madrid (callesdemadrid.cc)

- **URL**: https://callesdemadrid.cc/
- **What it does**: Research project analyzing Madrid streets named after people.
  Includes interviews with historians, gender analysis, bibliography.
- **Key data**: Of streets dedicated to people, 2,496 (89%) are named after men,
  529 (11%) after women.
- **Format**: Web content, not a downloadable structured dataset.
- **Madrid relevance**: Contains curated research and bibliography that could inform
  an etymology dataset. The categorization work (person vs. non-person) is valuable.

### 5c. Nomenclator Geografico de la Comunidad de Madrid

- **URL**: https://datos.gob.es/en/catalogo/a13002908-nomenclator-geografico-de-la-comunidad-de-madrid
- **What it contains**: Geographic names including cities, towns, and topographic features
  of public or historical interest within the Community of Madrid.
- **Format**: Open data via datos.gob.es.
- **Madrid relevance**: Useful for broader place name research beyond just streets.

---

## 6. UK RESOURCES

### 6a. Key to English Place-Names (KEPN)

- **URL**: https://kepn.nottingham.ac.uk/
- **Institution**: Institute of Name-Studies, University of Nottingham.
- **What it contains**: Searchable database of English place-name etymologies. For each
  place: meaning, breakdown of name elements, language of elements (Old English, Norse,
  Latin, etc.), historical forms.
- **Format**: Web database with clickable map interface.
- **Funded by**: Arts and Humanities Research Council (AHRC).
- **Madrid relevance**: Excellent academic model for rigorous etymological documentation.
  The element-based breakdown approach could inform how to structure etymology data
  (e.g., distinguishing between personal names, descriptive terms, historical references).

### 6b. OS Open Names (Ordnance Survey)

- **URL**: https://osdatahub.os.uk/downloads/open/OpenNames
- **What it contains**: Open dataset of place names, road numbers, and postcodes for
  Great Britain.
- **Format**: CSV, GeoPackage.
- **Limitation**: Names and locations only, no etymology.
- **Madrid relevance**: Limited -- comparable to Madrid's callejero as a base layer
  without etymology.

### 6c. National Street Gazetteer (NSG)

- **URL**: https://www.data.gov.uk/dataset/fe8453c9-ec74-485d-abde-aa6807645b37/national-street-gazetteer
- **What it contains**: Authoritative reference dataset of streets in England and Wales.
- **Format**: Open data.
- **Madrid relevance**: Comparable administrative dataset, no etymology.

### 6d. ARCHI UK Place Name Finder

- **URL**: https://www.archiuk.com/archi/find_place_name_map.htm
- **What it contains**: Search for archaeologically significant place names and
  place-name elements (e.g., *ton, *chester). Generates distribution maps.
  Includes Domesday Book historical names.
- **Format**: Web interface, free access.
- **Madrid relevance**: The element-based search and distribution mapping could inspire
  analysis of common Madrid street name patterns (e.g., streets with "de", "del",
  patronymic patterns).

---

## 7. GERMAN RESOURCES

### 7a. Geofabrik / Die Zeit Street Analysis

- **URL**: https://www.geofabrik.de/projects/strassennamen_zeit/index.html
- **What it did**: Calculated a list of ALL streets in Germany for Die Zeit newspaper
  article "Erst die Nazis, dann die Blumchen" analyzing political patterns in German
  street naming.
- **Data source**: OpenStreetMap via Geofabrik extracts.
- **Madrid relevance**: Demonstrates how OSM data can be used for large-scale street
  name analysis with political/historical framing.

### 7b. EqualStreetNames Berlin

- **URL**: https://github.com/EqualStreetNames/equalstreetnames-berlin
- **What it does**: Berlin-specific instance of EqualStreetNames, showing gender
  breakdown of street names via OSM + Wikidata.
- **Madrid relevance**: Template for creating a Madrid-specific instance.

---

## 8. US RESOURCES

### 8a. Geographic Names Information System (GNIS)

- **URL**: https://www.usgs.gov/tools/geographic-names-information-system-gnis
- **What it contains**: 2+ million physical and cultural feature names for the US.
  Includes current names, variant names, coordinates, state, county, USGS map reference.
- **Format**: Downloadable database, web search.
- **Limitation**: No etymology data. Focus is on standardization, not origin.
- **Madrid relevance**: Low for etymology, but good model for a comprehensive
  gazetteer structure.

### 8b. Data.gov Street Name Datasets

- **URL**: https://catalog.data.gov/dataset?tags=street-name
- **Notable**: NYC Street Name Dictionary (street names + codes).
- **Madrid relevance**: Low -- administrative data without etymology.

---

## 9. GENERAL GEOGRAPHIC / TOPONYMIC RESOURCES

### 9a. Getty Thesaurus of Geographic Names (TGN)

- **URL**: https://www.getty.edu/research/tools/vocabularies/tgn/
- **What it contains**: ~2.98 million records of place names with hierarchical
  relationships, coordinates, place types, historical names, and source documentation.
- **Format**: Linked Open Data (N-Triples, JSON, RDF, N3/Turtle), SPARQL endpoint,
  XML, relational tables, APIs.
- **License**: Open Data Commons Attribution License (ODC-By) 1.0.
- **Madrid relevance**: Could provide authoritative historical place name variants
  and hierarchical context for Madrid locations. The LOD format enables integration
  with Wikidata-based workflows.

### 9b. GeoNames

- **URL**: https://www.geonames.org/
- **What it contains**: 25+ million geographical names for 11.8 million features
  worldwide. Includes coordinates, elevation, population, admin subdivisions, postal codes.
- **Format**: REST API (40+ webservices), daily database dumps, Creative Commons BY license.
- **Limitation**: No etymology data. Focuses on name standardization and geocoding.
- **Madrid relevance**: Useful as a geographic reference layer but not for etymology.

### 9c. LinkedWiki SPARQL Street Names Query

- **URL**: https://linkedwiki.com/query/noms_de_rues_par_villes?lang=EN
- **What it does**: Pre-built SPARQL query showing French streets named after real
  people, grouped by city. Demonstrates the P31/P17/P131/P138 query pattern.
- **Madrid relevance**: The query pattern can be adapted for Madrid by changing the
  country filter from France to Spain and the city filter to Madrid.

---

## 10. ACADEMIC RESEARCH

### 10a. "Street Naming Practices: A Systematic Review" (2021)

- **Source**: Onoma journal, based on 121 peer-reviewed articles from Scopus.
- **Madrid relevance**: Provides methodological framework for analyzing street naming.

### 10b. Neotoponymy Research Network

- **URL**: https://neotopo.hypotheses.org/
- **What it does**: Tracks gender gap visualization initiatives in street naming worldwide.
- **Madrid relevance**: Network for connecting with other researchers doing similar work.

---

## SYNTHESIS: Recommended Approach for a Madrid Project

### Data Sources to Combine

1. **Base layer**: Madrid Open Data callejero (9,139 current streets + historical)
2. **Etymology from OSM**: Overpass API query for `name:etymology:wikidata` in Madrid
3. **Etymology from Wikidata**: SPARQL query for Madrid streets (P131=Q2807) with P138
4. **Biographical data**: Wikidata properties for honorees (gender, profession,
   birth/death, nationality)
5. **Historical context**: Calles de Madrid (callesdemadrid.cc) research
6. **StNamesLab Spain data**: Historical evolution 2001-2022

### Data Schema (modeled on Streetonomics + Paris Open Data)

For each street:
- `street_name` -- official name
- `street_type` -- calle, avenida, plaza, paseo, etc.
- `district` -- distrito
- `neighbourhood` -- barrio
- `geometry` -- line/polygon from OSM or callejero
- `etymology_type` -- person | event | place | descriptive | historical | unknown
- `named_after` -- free text description
- `named_after_wikidata` -- Q-identifier
- `person_gender` -- if person
- `person_birth_year` -- if person
- `person_death_year` -- if person
- `person_profession` -- if person
- `person_nationality` -- if person
- `naming_date` -- when the street received this name
- `previous_names` -- historical names
- `source` -- where the etymology info comes from
- `confidence` -- verified | probable | uncertain

### Best Model Projects to Follow

1. **Paris Open Data** -- for the official municipal dataset model (etymology included)
2. **Open Etymology Map** -- for the technical architecture (OSM + Wikidata + PostGIS)
3. **Streetonomics** -- for the structured research dataset schema
4. **EDJNet Mapping Diversity** -- for the methodology of matching OSM to Wikidata at scale
5. **MapComplete** -- for crowdsourcing etymology data contributions
6. **Paristique** -- for the user-facing interactive visualization
