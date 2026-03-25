# Street Name Origins: Datasets, Databases & Projects

**Research Date:** 2026-03-25
**Scope:** Datasets and projects documenting WHY streets are named the way they are (etymology, origin, historical context of street names).

---

## Table of Contents

1. [Madrid (City)](#1-madrid-city)
2. [Madrid (Community/Region)](#2-madrid-communityregion)
3. [Barcelona](#3-barcelona)
4. [Other Spanish Cities](#4-other-spanish-cities)
5. [International Projects - City-Specific](#5-international-projects---city-specific)
6. [International Projects - Multi-City / Global](#6-international-projects---multi-city--global)
7. [OpenStreetMap + Wikidata Ecosystem](#7-openstreetmap--wikidata-ecosystem)
8. [Academic Research with Published Datasets](#8-academic-research-with-published-datasets)
9. [Summary & Recommendations](#9-summary--recommendations)

---

## 1. Madrid (City)

### 1.1 Callejero Oficial del Ayuntamiento de Madrid (Open Data)

- **URL:** https://datos.madrid.es/dataset/213605-0-callejero-oficial-madrid
- **Publisher:** Ayuntamiento de Madrid
- **What it contains:** Official municipal street directory, updated daily. Two subsets: (a) current street directory; (b) historical evolution of streets. Contains street codes, street class, name, accented name, beginning/ending cross-streets.
- **Key CSV columns:** COD_VIA, VIA_CLASE, VIA_PAR, VIA_NOMBRE, VIA_NOMBRE_ACENTOS, COD_VIA_COMIENZA, CLASE_COMIENZA, PARTICULA_COMIENZA, NOMBRE_COMIENZA, etc.
- **Format:** CSV (downloadable), also available as web service
- **Number of entries:** ~9,139 streets (as of 2010 count); the CSV with historical evolution is 59.6 MB
- **License:** Open data (reuse permitted)
- **Does it contain ORIGINS/ETYMOLOGY?** **NO.** This is a purely administrative/geographic dataset. It has street names, codes, and cross-references but does NOT explain why streets are named the way they are.
- **Quality:** High for administrative purposes; useless for etymology research on its own.
- **Download:** https://datos.madrid.es/dataset/213605-0-callejero-oficial-madrid/downloads

### 1.2 Calles de Madrid (callesdemadrid.cc)

- **URL:** https://callesdemadrid.cc/
- **Methodology:** https://callesdemadrid.cc/informe/metodologia/
- **Publisher:** Civic project from Datatón Ciudad de Madrid 2017 (Medialab-Prado + Ayuntamiento de Madrid)
- **What it contains:** Categorization of all 8,014 Madrid streets by naming type. Each street classified into categories:
  - **Primary:** Persona (Person), Personaje (Character), Colectivo (Collective), Hecho (Event), Lugar (Place), Animal, Vegetal (Plant), Objeto (Object), Otros (Others)
  - **Secondary (for persons):** Nobleza, Religión, Ejército, Política, Méritos, Mitología, Ficción, Profesión
  - **Gender:** Masculino / Femenino
- **Key findings:** 3,025 streets named after people; 2,496 (89%) after men, 529 (11%) after women.
- **Format:** Web-based (maps, infographics). Started from Madrid open data CSV. The categorized spreadsheet was built collaboratively in Google Sheets but **no direct download link to the enriched/categorized dataset is published on the site**.
- **License:** CC-BY-SA 4.0
- **Does it contain ORIGINS/ETYMOLOGY?** **PARTIALLY.** It categorizes WHY streets have their names (person, place, event, etc.) but does NOT provide per-street narrative explanations of origins.
- **Quality:** Good categorization methodology. Limitation: no interactive query tool, only static maps. The underlying enriched data is not easily downloadable.

### 1.3 Madripedia (Wiki)

- **URL:** https://madripedia.wikis.cc/wiki/Calles_(Historia)
- **Publisher:** Community wiki project
- **What it contains:** A wiki encyclopedia about Madrid with 4,667+ articles and 1,518 uploaded files. Contains individual articles about specific streets with their history and name origins. For example, explains that "Cuchilleros" comes from the knife-makers trade, "Arenal" from sandy terrain, "Preciados" from property owners, etc.
- **Format:** Wiki (HTML). Would need scraping to extract structured data.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** -- narrative explanations per street.
- **Quality:** Variable. Community-contributed, so coverage is uneven. Some streets have detailed articles, many are missing.

### 1.4 Wikipedia - Nomenclátor callejero de Madrid

- **URL:** https://es.wikipedia.org/wiki/Nomencl%C3%A1tor_callejero_de_Madrid
- **What it contains:** Overview article with statistics: 56% of streets named after historical personalities, 22.5% political geography toponyms, 12% physical geography, 7% abstract concepts. Includes categories of naming origins (topography, property owners, convents, trade guilds, etc.)
- **Format:** Wikipedia article (narrative)
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** -- but only as a summary/overview, not a per-street database.

### 1.5 Revista Madrid Histórico / Blog Sources

- **URL:** https://www.revistamadridhistorico.es/2021/06/las-calles-de-madrid/
- **URL:** https://callesdemadrid.blogspot.com/ (blog "Madrid: sus viejas calles")
- **What they contain:** Narrative articles explaining street name origins one by one.
- **Format:** Blog posts (HTML). Would need scraping.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** -- but unstructured, narrative format.

---

## 2. Madrid (Community/Region)

### 2.1 Nomecalles - Nomenclátor y Callejero de la Comunidad de Madrid

- **URL:** https://gestiona.comunidad.madrid/nomecalles_web/
- **Statistics PDF (2022):** https://www.madrid.org/iestadis/fijas/efemerides/descarga/viales22not.pdf
- **Publisher:** Instituto de Estadística de la Comunidad de Madrid
- **What it contains:** Interactive map viewer + nomenclátor covering ALL municipalities in the Community of Madrid. 48,622 streets as of 2022. Includes aerial photography integration. Statistical analysis: 34.5% of streets have unique names, most common name is "iglesia" (164 streets). Gender stats: of 6,563 person-named streets, 81.1% male, 18.9% female.
- **Format:** Web viewer (map-based). Statistics available as PDF. The underlying data feeds from INE census callejero.
- **Does it contain ORIGINS/ETYMOLOGY?** **NO.** It's a geographic/statistical tool. Contains names and locations but not explanations.
- **Quality:** Very high for geographic data. Not useful for etymology.

---

## 3. Barcelona

### 3.1 Nomenclàtor de la Ciutat de Barcelona (Official Open Data) -- BEST FIND FOR STRUCTURED ORIGIN DATA

- **URL:** https://opendata-ajuntament.barcelona.cat/data/ca/dataset/nomenclator-bcn
- **Download:** https://opendata-ajuntament.barcelona.cat/data/dataset/6beb9044-b84a-4bdf-9509-8cd6fc6c7c6c/resource/1a07ea44-f88d-4d86-ae0d-ff6e6a3d0bf2/download
- **Publisher:** Ajuntament de Barcelona
- **What it contains:** Official nomenclature of all public streets in Barcelona with **10 structured fields**:
  1. `CODI` -- Street code
  2. `TIPUS_VIA` -- Street type (carrer, plaça, avinguda, etc.)
  3. `PARTICULES` -- Auxiliary particles (de, del, d', etc.)
  4. `NOM` -- Street name
  5. `DATA_APROV` -- Official approval date of current name
  6. `NOTES_DATA` -- Notes about dating
  7. **`DESCRIPCIO1` -- Historical description / origin of street name**
  8. **`DESCRIPCIO2` -- Continuation of historical description**
  9. **`FONTS_DOC` -- Documentary sources/references**
  10. `ALTRES_NOMS` -- Previous/alternative names
- **Format:** CSV (inside ZIP file)
- **License:** CC-BY 4.0
- **Last updated:** December 14, 2023
- **Does it contain ORIGINS/ETYMOLOGY?** **YES!** Fields DESCRIPCIO1, DESCRIPCIO2, and FONTS_DOC provide structured etymology data per street. This is one of the best structured open datasets found.
- **Quality:** HIGH. Official government data, structured CSV, openly licensed, includes documentary sources. The descriptions may be somewhat dated (the municipal nomenclator hasn't been aggressively updated for content).
- **Also available on:** https://datos.gob.es/en/catalogo/l01080193-nomenclator-de-la-ciudad-de-barcelona1 and https://data.europa.eu/data/datasets/https-opendata-ajuntament-barcelona-cat-data-dataset-nomenclator-bcn

### 3.2 bcn.cat/nomenclator (Official Municipal Website)

- **URL:** https://www.bcn.cat/nomenclator/
- **English version:** https://www.bcn.cat/nomenclator/english/diccionari.htm
- **Publisher:** Ajuntament de Barcelona (Ponència de Nomenclàtor dels Carrers)
- **What it contains:** Dictionary of all street names in alphabetical order. For each street: the year of naming, origin of the current name, and all historical name changes across different periods. Available in Catalan, Spanish, and English.
- **Format:** Web interface (searchable). Uses older Flash technology in parts. Same underlying data as the open data CSV above.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Narrative explanations per street.
- **Quality:** Good content but poor technological implementation (partly Flash-based, outdated).

### 3.3 carrers.barcelona (Civic Project)

- **URL:** https://carrers.barcelona/
- **About:** https://carrers.barcelona/quant-a/
- **Full index:** https://carrers.barcelona/tot
- **Publisher:** Independent civic project (contact: [email protected])
- **What it contains:** An enhanced, modern web presentation of Barcelona street nomenclature data. Sources: Barcelona open data portal CSV + information obtained via public information requests (transparència). Each street entry includes:
  - Official name and historical forms
  - Origin/etymology of the name
  - Street descriptions and context
  - Intersection data (from OpenStreetMap Overpass API)
  - Header images (from Google Street View API)
- **Format:** Searchable web interface. No bulk download available.
- **Last updated:** December 2022
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Enriched version of the official data.
- **Quality:** Good. Modernized presentation of the official nomenclàtor data with additional enrichment. The creators note they've corrected some outdated terminology. Not maintained very recently.

### 3.4 UB Omnia Nomina - Nomenclàtor dels carrers de Barcelona

- **URL:** https://www.ub.edu/omnia-nomina/nomenclator-dels-carrers-de-barcelona/
- **Publisher:** Universitat de Barcelona
- **What it contains:** Academic resource portal for Barcelona street nomenclature. Part of the university's multilingual proper-noun validation portal. Links to and contextualizes the official Barcelona nomenclàtor.
- **Format:** Web portal with links to resources.
- **Does it contain ORIGINS/ETYMOLOGY?** References the official nomenclator which does.
- **Quality:** Academic curation, good as a gateway resource.

### 3.5 Museu d'Història de Catalunya - Carrers de l'Eixample

- **URL:** https://www.mhcat.cat/recursos_i_recerca/recursos_projectes/recursos_en_linia/carrers_de_l_eixample_de_barcelona_de_victor_balaguer
- **What it contains:** Online resource about the naming of Eixample streets by Víctor Balaguer.
- **Format:** Web resource.
- **Does it contain ORIGINS/ETYMOLOGY?** YES, for the Eixample district specifically.

---

## 4. Other Spanish Cities

### 4.1 Donostia/San Sebastián - Historia de los Nombres de Calle -- EXCELLENT STRUCTURED DATASET

- **URL (datos.gob.es):** https://datos.gob.es/en/catalogo/l01200697-historia-de-los-nombres-de-calle
- **Direct CSV download:** https://www.donostia.eus/datosabiertos/recursos/historia_nomcalle/kaleizenhistorioa.csv
- **Also on:** https://opendata.euskadi.eus/webopd00-dataset/es/contenidos/ds_localizaciones/aaa113u97aaaaaad5oaaf/es_def/index.shtml
- **Publisher:** Ayuntamiento de Donostia/San Sebastián
- **What it contains:** Bilingual (Basque/Spanish) CSV with **6 columns**:
  1. `KodKalea/Cod.Calle` -- Street code
  2. `Izena/Nombre` -- Street name (bilingual)
  3. **`Historioa/Historia` -- Historical description / etymology / origin**
  4. `Kokapena/Localización` -- Location details
  5. `Bildura data/Fecha pleno` -- Official council approval date
  6. `Auzoa/Barrio` -- Neighborhood
- **Format:** CSV
- **Number of entries:** ~200+ documented streets
- **License:** CC BY-SA 3.0
- **Last updated:** February 2021 (annual updates)
- **Does it contain ORIGINS/ETYMOLOGY?** **YES!** The `Historioa/Historia` field contains narrative explanations of why each street has its name.
- **Quality:** HIGH. Structured, bilingual, openly licensed, directly downloadable. Smaller city so fewer entries, but excellent model.

### 4.2 Bilbao - BilbaoIzan "¿Por qué se llama...?"

- **URL:** https://www.bilbao.eus/cs/Satellite?c=Page&cid=1272986939596&language=es&pageid=1272986939596&pagename=BilbaoIzan/Page/BIZ_ListadoCallejero
- **Publisher:** Ayuntamiento de Bilbao
- **What it contains:** Searchable database of Bilbao street names with historical explanations. For each street: official name, name variations, historical name changes, background on honored individuals, etymology and historical significance. Based on the book "Calles y rincones de Bilbao" by Javier González Oiver.
- **Format:** Web interface (searchable). No bulk download available.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Narrative explanations per street.
- **Quality:** Good content. Limitation: web-only, would need scraping for bulk data.

### 4.3 L'Hospitalet de Llobregat - Nomenclàtor dels Carrers

- **URL:** https://opendata.l-h.cat/Urbanisme-i-infraestructures/Guia-oficial-de-noms-de-carrers/mxs6-mjeq
- **Also:** https://datos.gob.es/en/catalogo/l01081017-guia-oficial-de-nombres-de-calles-de-lhospitalet
- **Publisher:** Ajuntament de L'Hospitalet de Llobregat
- **What it contains:** Official guide to street names. 564 street entries as of 2021.
- **Format:** CSV, JSON, API, XML
- **License:** Open data
- **Does it contain ORIGINS/ETYMOLOGY?** Partially -- it's primarily a nomenclàtor (official names registry). Check if description fields exist.
- **Quality:** Good open data practices but smaller scope.

### 4.4 Sevilla - Calles de Sevilla

- **URL:** https://callesdesevilla.com/
- **What it contains:** Web encyclopedia covering etymology, history, and curiosities about Seville's streets, neighborhoods, fountains, monuments, churches, and convents. Also covers biographies of mayors and officials.
- **Historical reference:** Based partly on "Noticia histórica del origen de los nombres de las calles de esta ciudad de Sevilla" by Félix González de León (1839, public domain).
- **Format:** Web-only. No bulk download.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Narrative per-street explanations.
- **Quality:** Rich historical content but unstructured, incomplete, web-scraping would be needed.

### 4.5 Zaragoza - Historical Street Name Research

- **URL (academic PDF):** https://ifc.dpz.es/recursos/publicaciones/09/23/23gimenez.pdf
- **URL (blog):** https://www.soydezaragoza.es/toponimos-de-zaragoza-nombres-calles-plazas-lugares/
- **What it contains:** Academic research on 15th-century Zaragoza street names (urban toponymy). The blog provides a more accessible overview.
- **Format:** PDF (academic), web blog.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** -- academic research on historical origins.
- **Quality:** Academic quality but limited to historical period; not a comprehensive modern database.

### 4.6 Catalonia (Region) - ICGC Street Names Dataset

- **URL:** https://datos.gob.es/en/catalogo/a09002970-nombre-de-calles-de-cataluna
- **Publisher:** Institut Cartogràfic i Geològic de Catalunya (ICGC)
- **What it contains:** Street names (noms de carrers) associated with populated units across all Catalan municipalities. Updated with 13,000+ place names.
- **Format:** Open data format (check datos.gob.es for specific formats)
- **Does it contain ORIGINS/ETYMOLOGY?** **NO.** This is a geographic/cartographic dataset. Names only, no explanations.
- **Quality:** High for geographic data. Not useful for etymology.

---

## 5. International Projects - City-Specific

### 5.1 Paris - Dénominations des Emprises des Voies Actuelles -- EXCELLENT

- **URL:** https://opendata.paris.fr/explore/dataset/denominations-emprises-voies-actuelles/
- **Publisher:** Ville de Paris
- **What it contains:** Official nomenclature of ALL current Paris streets. For each street:
  - Official denomination
  - Arrondissement and quartier
  - Dimensions/length
  - Start and end locations
  - **Former/historical names**
  - **Origin of the current name** (narrative explanation)
  - Regulatory texts (letters patent, ordinances, decrees)
  - Date of denomination
- **Format:** Multiple formats available on Paris Open Data (CSV, JSON, API)
- **License:** ODbL
- **Does it contain ORIGINS/ETYMOLOGY?** **YES!** Includes "information on the history and origin of the name" per street.
- **Quality:** VERY HIGH. Official, structured, well-maintained, openly licensed.

### 5.2 Paris - Paristique (Interactive Map)

- **URL:** https://www.paristique.fr/
- **Creator:** Guillaume Derolez (Google engineer, personal project)
- **What it contains:** Interactive map of Paris showing, for each street: name, creation date, origin of name, and district. Built from ParisData + Open Knowledge Foundation data.
- **Format:** Interactive web map. Data sourced from the Paris Open Data dataset above.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Visualization of the Paris open data.
- **Quality:** Excellent user experience. Free, no ads.

### 5.3 Vienna - Wien Geschichte Wiki (Straßennamen)

- **URL:** https://www.geschichtewiki.wien.gv.at/Straßennamen
- **Official city page:** https://www.wien.gv.at/kultur/strassennamen/index.html
- **Publisher:** Stadt Wien (City of Vienna)
- **What it contains:** Comprehensive wiki with ~6,600 traffic areas documented, of which 4,379 are person-related names. Each entry includes:
  - Current official name
  - Historical names and variants
  - Person honored (if applicable) with biographical details
  - Date ranges
  - District location
  - Historical context
  - Images and source references
  - Gender attribution
- **Coverage:** All 23 Vienna districts, medieval through contemporary
- **Format:** Wiki (HTML) with RDF export functionality. Also linked to the official digital city map.
- **Language:** German
- **Does it contain ORIGINS/ETYMOLOGY?** **YES!** Very detailed per-street explanations.
- **Quality:** VERY HIGH. Official government wiki, comprehensive coverage, RDF export for structured data. A historians' commission investigated all person-named streets 2011-2013.
- **Note:** Open Government Data Austria (data.gv.at) has the Vienna street graph data: https://www.data.gv.at/katalog/dataset/stadt-wien_straengraphwien

### 5.4 Lviv, Ukraine - "Lviv Streets" Project

- **URL:** https://streets.lvivcenter.org/en/
- **Street list:** https://streets.lvivcenter.org/en/streets/
- **Publisher:** Center for Urban History of East Central Europe
- **What it contains:** Database of current AND historical names of all Lviv streets and squares. Compiled from reference books, guide books, address books, historical maps, and archival materials. Tracks renaming history through Polish, Soviet, German, and Ukrainian rule periods. Example: Prospekt Svobody has had 17 name changes in 200 years.
- **Format:** Interactive Google Maps-based web interface. No bulk download from the main site.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Detailed renaming history and origin explanations.
- **Quality:** HIGH. Thorough academic project with rich historical layering.

### 5.5 Lviv - Historical Urbanonymy Dataset (Zenodo) -- FAIR DATA

- **URL:** https://zenodo.org/records/17512160
- **Interactive visualization:** https://map.humaniora.ucu.edu.ua/en/
- **Publisher:** PhD research, published via NFDI4Memory FAIR Data Fellowship at Leibniz-Institut für Europäische Geschichte
- **What it contains:** 3,342 records documenting historical references to street names and urban features from 1382-1768. Each record contains:
  - Original Latin/German/Polish form as in primary documents
  - Modern Ukrainian and English translations
  - Date of mention
  - Bibliographical source information
- **Format:** Structured dataset on Zenodo (DOI-assigned, FAIR-compliant)
- **License:** CC BY 4.0
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Historical attestations of street names with original-language forms.
- **Quality:** VERY HIGH for historical research. FAIR principles, persistent DOI, academic rigor.

---

## 6. International Projects - Multi-City / Global

### 6.1 Mapping Diversity (EDJNet) -- 30 European Cities

- **URL:** https://mappingdiversity.eu/
- **GitHub:** https://github.com/EDJNet/mapping_diversity
- **Full dataset release:** https://www.europeandatajournalism.eu/cp_data_news/mapping-diversity-full-dataset-release/
- **Publisher:** European Data Journalism Network (OBC Transeuropa coordination)
- **What it contains:** Analysis of 145,933 streets across **30 major European cities** in 17 countries. For streets named after persons, links to Wikidata to extract: gender, occupation, birth/death dates, geographic origin. Cities include: Athens, Berlin, Brussels, Bucharest, Budapest, Copenhagen, Kyiv, Lisbon, **Madrid**, Paris, Prague, Rome, Stockholm, Vienna, Warsaw, Zagreb, **Sevilla**, and more.
- **Data file:** `street names aggregate results.xlsx` (Excel)
- **Format:** Excel spreadsheet, R scripts for processing
- **Methodology:** Automatic matching of OpenStreetMap street data (via Geofabrik) to Wikidata identifiers, then manual street-by-street verification.
- **License:** CC BY-SA 4.0
- **Does it contain ORIGINS/ETYMOLOGY?** **PARTIALLY.** For person-named streets, it identifies WHO the person was (via Wikidata) but does not provide narrative etymology for non-person streets.
- **Quality:** HIGH. Professional journalism project, manually verified, well-documented methodology.

### 6.2 EqualStreetNames -- 63 Cities in 21 Countries

- **URL:** https://github.com/EqualStreetNames/equalstreetnames
- **Brussels instance:** https://equalstreetnames.brussels/en/index.html
- **Publisher:** Open Knowledge Belgium + community replicators
- **What it contains:** Interactive maps visualizing street names by gender for 63 cities across 21 countries. Links OpenStreetMap streets to Wikidata entries. Per-street data: name, Wikidata link, gender of honoree, biographical summary.
- **Format:** Web maps + GitHub repos with JSON/GeoJSON data per city. Each city is a separate sub-module.
- **Methodology:** Community volunteers add Wikidata tags to OpenStreetMap streets, then the visualization is auto-generated.
- **License:** Open source (MIT for code, ODbL for data)
- **Does it contain ORIGINS/ETYMOLOGY?** **PARTIALLY.** Links person-named streets to Wikidata bios, but doesn't cover non-person etymologies.
- **Quality:** GOOD. Active open-source project. Coverage varies dramatically by city depending on volunteer effort.

### 6.3 STNAMES LAB (Street Names Lab) -- Spain, Europe, North America

- **URL:** https://en.stnameslab.com/the-project/
- **GitHub:** https://github.com/StNamesLab/StreetNamesDatabase
- **Publisher:** Universidad Pablo de Olavide (Seville), research group
- **What it contains:** Street names database for North America and large part of Europe. CSV files with street names organized by administrative divisions.
  - **Europe:** Streets assigned to communes (from OpenStreetMap, autumn 2022)
  - **North America:** Streets by counties (US), census divisions (Canada), municipalities (Mexico)
  - **Spain special:** Dedicated dataset from INE (Instituto Nacional de Estadística) covering 2001-2022
- **Format:** CSV files (delimiter: `$`), compressed with WinRAR. UTF-8 encoding (Latin-1 for Spain).
- **License:** ODbL (OpenStreetMap data), CC BY-SA 4.0 (Spain/INE data)
- **Web app:** Interactive map to visualize spatial distribution of street names, search for terms, and download query results as spreadsheets. Spain app allows year selection 2001-2022.
- **Does it contain ORIGINS/ETYMOLOGY?** **NO.** Contains street names and locations, but not explanations of origins. However, the search functionality (e.g., search for "santo" or "reina") enables pattern analysis.
- **Quality:** HIGH for quantitative analysis. Well-documented, academic backing. Not useful for individual etymology.
- **Citation:** Carmona-Derqui, D., Gutiérrez-Mora, D., & Oto-Peralías, D. (2023). "Tabulating and visualizing street-name data in the US and Europe." *Environment and Planning B*, 50(7), 1981-1987.

### 6.4 Streetonomics Dataset -- Paris, Vienna, London, New York

- **URL (paper):** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0252869
- **Data:** https://social-dynamics.net/streetonomics/data
- **Publisher:** Academic research (PLOS ONE, 2021)
- **What it contains:** 4,932 honorific streets across 4 cities. Per street:
  - District
  - Renaming date
  - Person name (honoree)
  - Honoree's gender
  - Occupation/profession
  - Country of origin
  - Dates of birth and death
- **Format:** Downloadable dataset (check URL for format)
- **License:** Open access
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** for person-named streets (who, what profession, when, where from). Not for non-person streets.
- **Quality:** HIGH. Peer-reviewed academic research. Limited to 4 cities and honorific streets only.

---

## 7. OpenStreetMap + Wikidata Ecosystem

### 7.1 OSM `name:etymology` and `name:etymology:wikidata` Tags -- THE GLOBAL INFRASTRUCTURE

- **OSM Wiki:** https://wiki.openstreetmap.org/wiki/Key:name:etymology
- **OSM Wiki (Wikidata):** https://wiki.openstreetmap.org/wiki/Key:name:etymology:wikidata
- **Taginfo stats:** https://taginfo.openstreetmap.org/keys/name:etymology:wikidata
- **What it is:** OpenStreetMap has a standardized tagging system for recording street name etymology:
  - `name:etymology` = human-readable text of the namesake
  - `name:etymology:wikidata` = Wikidata Q-identifier linking to structured data about the namesake
  - `name:etymology:wikipedia` = Wikipedia article link
- **Scale:** ~**1.7 million OSM objects** tagged with `name:etymology:wikidata` globally, edited by 25,435+ different users.
- **Format:** Part of the OpenStreetMap database. Accessible via Overpass API, bulk planet file downloads, or SPARQL queries against Wikidata.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** This is the largest crowd-sourced etymology dataset in the world. Via Wikidata links, each tagged street connects to structured data: who/what the street is named after, with occupation, gender, dates, description, etc.
- **Quality:** VARIABLE. Coverage is extremely uneven -- some cities have most streets tagged, others have almost none. Person-named streets are better covered than descriptive/topographic names. The data is crowd-sourced so there can be errors.
- **Key insight:** This is the most scalable approach. Rather than building a database from scratch, contributing etymology data to OSM/Wikidata creates a globally interoperable resource.

### 7.2 Open Etymology Map (etymology.dsantini.it)

- **URL:** https://etymology.dsantini.it/
- **GitHub:** (by Daniele Santini)
- **What it is:** Interactive world map showing street name etymology based on OSM + Wikidata data. Click any street to see who/what it was named after, with Wikidata details.
- **Technology:** Leaflet + PostgreSQL + FlatGeobuf
- **Does it contain ORIGINS/ETYMOLOGY?** **YES.** Visualizes OSM etymology tags on a map.
- **Quality:** Depends on underlying OSM data quality. Excellent visualization layer.

### 7.3 MapComplete Etymology Theme

- **URL:** https://mapcomplete.org/etymology
- **What it is:** Both a viewer AND an editor. Allows anyone to see existing etymology data on a map AND contribute new `name:etymology:wikidata` tags directly to OpenStreetMap. Low barrier to entry -- no OSM expertise needed.
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** (viewer + contributor tool).
- **Quality:** Excellent as a contribution tool. The quality of data shown depends on what has been contributed in each area.

### 7.4 osmetymology (Peter Brodersen)

- **URL:** https://github.com/PeterBrodersen/osmetymology
- **What it is:** Open-source toolkit for creating local etymology maps from OSM + Wikidata. Creates PostgreSQL database, generates FlatGeobuf and CSV outputs. Originally focused on Denmark but adaptable to any region.
- **Format:** PostgreSQL, FlatGeobuf, CSV outputs
- **Does it contain ORIGINS/ETYMOLOGY?** **YES** (tooling to extract and display etymology data).

---

## 8. Academic Research with Published Datasets

### 8.1 "Cultura histórica y nombres de calles" (Barcelona & Madrid)

- **URL:** https://revistas.unav.edu/index.php/myc/article/view/33712
- **Also:** https://www.researchgate.net/publication/364576021
- **Publisher:** *Memoria y Civilización* journal (Universidad de Navarra)
- **What it contains:** Academic comparative study of street naming patterns in Barcelona and Madrid. Analyzes the contemporary nomenclátor of both cities.
- **Format:** Academic paper (PDF)
- **Does it contain ORIGINS/ETYMOLOGY?** YES, analytical framework for understanding naming patterns.

### 8.2 "Street Name Data as a Reflection of Migration and Settlement History"

- **URL:** https://www.mdpi.com/2413-8851/4/4/74
- **What it contains:** Research on how European immigrant street names in North America reflect migration patterns. Uses OpenStreetMap data.
- **Format:** Academic paper with data references.

### 8.3 "Street Naming Practices: A Systematic Review"

- **URL:** https://www.researchgate.net/publication/357187452
- **What it contains:** Systematic review of 121 peer-reviewed articles on street naming from Scopus. Comprehensive literature review of the field.
- **Format:** Academic paper.

---

## 9. Summary & Recommendations

### Datasets with Actual Street Name ORIGINS/ETYMOLOGY (Structured Data)

| Dataset | City/Region | Format | Entries | Etymology? | Quality | Direct Download? |
|---------|-------------|--------|---------|------------|---------|-----------------|
| **Barcelona Nomenclàtor (Open Data)** | Barcelona | CSV | All streets | YES (DESCRIPCIO1/2 fields) | HIGH | YES |
| **Donostia Historia de Nombres** | San Sebastián | CSV | ~200+ | YES (Historia field) | HIGH | YES |
| **Paris Dénominations des Voies** | Paris | CSV/JSON/API | All streets | YES (origin field) | VERY HIGH | YES |
| **Vienna Geschichte Wiki** | Vienna | Wiki + RDF | ~6,600 | YES (detailed articles) | VERY HIGH | Partial (RDF) |
| **OSM name:etymology:wikidata** | Global | OSM/API | ~1.7M objects | YES (via Wikidata) | VARIABLE | YES (Overpass) |
| **Mapping Diversity** | 30 EU cities | Excel | 145,933 streets | Partial (persons) | HIGH | YES |
| **Streetonomics** | 4 cities | Dataset | 4,932 streets | YES (persons) | HIGH | YES |
| **Lviv Zenodo** | Lviv (historical) | Structured | 3,342 records | YES | VERY HIGH | YES |

### Best Resources by Use Case

1. **If building a street origin database for Madrid:** Start with the official callejero CSV from datos.madrid.es (for the base list), then enrich using Madripedia articles, callesdemadrid.cc categories, and OSM etymology tags. There is no single structured dataset for Madrid street origins -- it would need to be assembled.

2. **If building for Barcelona:** The official Nomenclàtor CSV is excellent -- start there. It already has structured DESCRIPCIO1/DESCRIPCIO2 fields with origin text. Supplement with carrers.barcelona content.

3. **If building for any city globally:** Use the OSM `name:etymology:wikidata` infrastructure. Check coverage for your target city, then contribute missing data via MapComplete.

4. **Model to emulate:** Barcelona's open data nomenclàtor and Donostia's dataset are the best models for what a structured street-name-origins dataset should look like. Paris is the gold standard internationally.

### Key Gap for Madrid

Madrid does NOT have a structured, downloadable dataset of street name origins. The callejero oficial has names but no etymology. Callesdemadrid.cc has categories but no per-street narratives and no downloadable enriched data. Madripedia has narratives but is a wiki, not a database. Building a Madrid street etymology dataset would require:
1. Starting with the callejero CSV (8,014 streets)
2. Adding categorization from callesdemadrid.cc methodology
3. Scraping/extracting origin narratives from Madripedia, Wikipedia, and literary sources
4. Cross-referencing with OSM etymology:wikidata tags
5. Possibly using the historical "Los nombres de las calles de Madrid" book (available as PDF: https://edicioneslalibreria.com/wp-content/uploads/2021/02/Los-nombres-de-las-calles-de-Madrid.pdf)
