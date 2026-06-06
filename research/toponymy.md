# Research: Origins of Madrid Neighbourhood/District/Barrio Names

## Date: 2026-03-25

---

## 1. OPEN DATA / STRUCTURED DATASETS

### 1.1 Barrios municipales de Madrid (Municipal Neighbourhoods Dataset)
- **URL**: https://datos.madrid.es/dataset/300496-0-barrios-madrid
- **What it contains**: Delimitation of the 131 neighbourhoods (barrios) of Madrid, with names, codes, and associated district information. Geographic boundaries included.
- **Formats**: CSV, KML, XLSX, TXT, SHP (including historical administrative divisions shapefile)
- **License**: CC BY 4.0
- **Quality/Completeness**: Official municipal data. Complete for boundaries and names of all 131 barrios across 21 districts. Does NOT contain etymological/origin information -- purely administrative/geographic.
- **Notes**: 16,079 downloads. Last significant update: Oct 2017 (addition of 2 new neighbourhoods in Vicálvaro, renamed neighbourhood in Villaverde).

### 1.2 Callejero Oficial del Ayuntamiento de Madrid (Official Street Directory)
- **URL**: https://datos.madrid.es/dataset/213605-0-callejero-oficial-madrid
- **Downloads page**: https://datos.madrid.es/dataset/213605-0-callejero-oficial-madrid/downloads
- **What it contains**: Two subsets -- (a) current street directory (daily updates) and (b) street directory with historical evolution. Includes street names, denominations, administrative data, police numbers, district/neighbourhood classifications, numbering intervals. The historical subset tracks denomination changes and numbering modifications.
- **Formats**: CSV, Shapefile, GeoLocator SCN format
- **Quality/Completeness**: Official, daily updates. CAVEAT: "historical information is not complete as it is not fully computerized." Contains ~9,139 streets (as of 2010 count). Does not contain etymological explanations, but historical name changes are partially tracked.
- **API**: REST OGC Feature Server, WFS services, geocoding services available.

### 1.3 Callejero Oficial -- Geoportal (with Historical Numbering)
- **URL**: https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/dataset.iam?id=9be44652-2490-11e9-a99c-ecb1d752b636
- **What it contains**: Current and historical numbering of streets, with geographic data.
- **Formats**: Shapefile (ZIP), CSV
- **Direct downloads**:
  - SHP: https://geoportal.madrid.es/fsdescargas/IDEAM_WBGEOPORTAL/CALLEJERO/NDPS_VIGENTES_HISTORICOS/NDPS_VIG_HIS_SHP.zip
  - CSV: https://datos.madrid.es/egob/catalogo/213605-5-callejero-oficial-madrid.csv
- **Quality/Completeness**: Comprehensive for current streets; historical data partially computerized.

### 1.4 Panel de indicadores de distritos y barrios (Sociodemographic Indicators)
- **URL**: https://datos.madrid.es/dataset/300087-0-indicadores-distritos
- **What it contains**: Socioeconomic, health, demographic, educational, quality of life, housing, environment, municipal facilities data for all districts and barrios. Annual studies.
- **Formats**: XLS, CSV
- **Quality/Completeness**: Comprehensive sociodemographic data. No etymological content, but useful for correlating district/barrio names with geographic/demographic context.

### 1.5 Nomenclátor Geográfico de la Comunidad de Madrid
- **URL**: https://datos.gob.es/en/catalogo/a13002908-nomenclator-geografico-de-la-comunidad-de-madrid
- **What it contains**: Geographic names (localities, cities, settlements, topographic features) of public/historical interest in the Madrid Community region. Coordinates in ETRS89.
- **Formats**: Database, ATOM download service, WMS visualization service
- **Quality/Completeness**: Official geographic nomenclature from Spain's Basic Geographic Nomenclature (NGBE). Covers the whole Community of Madrid, not just the city.

### 1.6 Nomecalles -- Nomenclator y Callejero de la Comunidad de Madrid
- **URL**: https://gestiona.comunidad.madrid/nomecalles_web/
- **ArcGIS hub**: https://hub.arcgis.com/documents/a5893803f5ee413da8168ddbaa46fc9f
- **What it contains**: Official nomenclature and street directory for the entire Community of Madrid. Includes geographic boundaries, street directories, cadastral records, aerial photographs, georeferenced statistical information.
- **Format**: Web application / GIS layers
- **Quality/Completeness**: Comprehensive official tool, but oriented toward current geographic information rather than historical etymology.

---

## 2. ACADEMIC / SCHOLARLY RESOURCES

### 2.1 "Toponimia madrileña: proceso evolutivo" -- Luis Miguel Aparisi Laporta (2001)
- **Dialnet entry**: https://dialnet.unirioja.es/servlet/libro?codigo=42882
- **Publisher**: Gerencia Municipal de Urbanismo, Ayuntamiento de Madrid
- **ISBN**: 84-7812-525-6
- **What it contains**: A major scholarly work on Madrid toponymy. 2 volumes + 1 CD-ROM. Over 20,000 toponyms of the city of Madrid catalogued, with historical documentation. Product of 14 years of research. Won the Premio Antonio Maura for Madrid research (1997).
- **Format**: Physical book (2 vols + CD-ROM). Not freely available online.
- **Quality/Completeness**: EXCELLENT. The most comprehensive single work on Madrid street/place name origins. Cited by virtually all subsequent researchers. The CD-ROM reportedly contains a searchable database.

### 2.2 "Algunos topónimos madrileños de origen celta" -- Joaquín Caridad Arias (2004)
- **Dialnet entry**: https://dialnet.unirioja.es/servlet/articulo?codigo=3012173
- **Publication**: Anales del Instituto de Estudios Madrileños, No. 44, pp. 821-830
- **ISSN**: 0584-6374
- **What it contains**: Academic article examining Celtic-origin place names in Madrid: Aravaca, Alcobendas, Carabanchel, Carabaña, Chamberí, Las Vistillas, Vallecas. Traces transformations through Latin and Romance language evolution.
- **Format**: Journal article (accessible via Dialnet)
- **Quality/Completeness**: Focused and scholarly. Covers 7 specific toponyms with detailed linguistic analysis. Peer-reviewed.

### 2.3 "En torno a la toponimia madrileña" -- Jairo Javier García Sánchez (2010)
- **Academia.edu**: https://www.academia.edu/10965316/En_torno_a_la_toponimia_madrile%C3%B1a
- **Publication**: Chapter in "Toponimia de España. Estado actual y perspectivas de la investigación" (De Gruyter)
- **DOI**: 10.1515/9783110233490.259
- **What it contains**: Survey of the state of Madrid toponymic research. Identifies significant research gaps. Reviews etymology of "Madrid" itself (Latin MATRICE = water source being most credible). References Aparisi Laporta's 20,000-toponym catalogue. Calls for systematic collaborative research.
- **Format**: Book chapter (accessible via Academia.edu)
- **Quality/Completeness**: HIGH. Authoritative academic overview. Best single summary of the state of the field.

### 2.4 "Toponimia geográfica madrileña" -- Fernando Jiménez de Gregorio
- **ResearchGate**: https://www.researchgate.net/publication/27590627_Toponimia_geografica_madrilena
- **Also on Dialnet** (multiple parts: articles coded 3012169, 3015655, etc.)
- **Publication**: Anales del Instituto de Estudios Madrileños (multiple parts)
- **What it contains**: Multi-part series ("Materiales para una toponimia de la provincia de Madrid") examining toponyms in their geographical and historical-social aspects. Over 10,000 toponym index cards compiled.
- **Format**: Journal articles
- **Quality/Completeness**: Extensive series, but covers the entire province, not just the city. Foundational scholarly work.

### 2.5 "La información codificada en la toponimia urbana" -- Ayar Rodríguez de Castro (2017)
- **URL**: https://oa.upm.es/45243/
- **Institution**: E.T.S.I. en Topografía, Geodesia y Cartografía (UPM)
- **What it contains**: Doctoral thesis on geographic analysis of urban toponymy (focused on Toledo periphery, but methodology applicable to Madrid). Analyses how toponymy encodes information about urban development and landscape evolution.
- **Format**: PDF (open access from UPM repository)
- **Quality/Completeness**: Methodologically relevant. Not Madrid-specific but provides analytical framework.

### 2.6 "Contribución al estudio toponomástico del Sur de Madrid. I. La toponimia de Móstoles" -- Azucena García Romero
- **URL**: https://www.academia.edu/4466835/
- **What it contains**: Toponymic study of Móstoles (southern Madrid metropolitan area).
- **Format**: Academic paper
- **Quality/Completeness**: Limited to Móstoles; relevant for methodology and southern Madrid context.

---

## 3. BOOKS (Key Reference Works)

### 3.1 "Los nombres de las calles de Madrid" -- María Isabel Gea Ortigas
- **Publisher**: Ediciones La Librería
- **Editions**: 1993 (1st), 1995, 1999 (3rd, 386 pp), 2012 (324 pp), 2020 (324 pp)
- **ISBN**: 9788498734362 (2012 ed.), 9788498731828
- **Amazon**: https://www.amazon.es/Los-nombres-las-calles-Madrid/dp/8498731828
- **What it contains**: Over 1,000 entries covering streets, passages, plazas, and avenues in central Madrid. Explains the origin of each name and different historical denominations.
- **Format**: Current editions are physical/bookshop items; a publisher sample/intro PDF exists, but no complete open scan was found.
- **Quality/Completeness**: VERY GOOD. Regularly updated. One of the most popular and accessible references. Focuses on central Madrid.

### 3.2 "Origen histórico y etimológico de las calles de Madrid" -- Antonio de Capmany y de Montpalau (1863)
- **Digital library record**: https://bibliotecavirtualmadrid.comunidad.madrid/bvmadrid_publicacion/es/consulta/registro.do?id=87766
- **Publisher**: Madrid: Manuel B. de Quirós, 1863
- **What it contains**: 431 pages examining historical origins and etymological backgrounds of Madrid streets, incorporating legends. The earliest major work on this subject.
- **Format**: Physical book (held in Biblioteca Histórica Municipal, Fundación Universitaria Española, and others). May be digitized in the Biblioteca Digital de la Comunidad de Madrid.
- **Quality/Completeness**: HISTORICALLY IMPORTANT. The foundational 19th-century reference. Methodology reflects its era but invaluable for historical context.

### 3.3 "Las calles de Madrid" -- Pedro de Répide (original early 20th c., reprinted 2011)
- **Publisher**: Ediciones La Librería (2011 reprint)
- **What it contains**: Classic literary-historical guide to Madrid's streets by the famous Madrid chronicler.
- **Format**: Physical book
- **Quality/Completeness**: Classic reference, literary in style. Still widely cited.

### 3.4 "Los nombres de las calles de Madrid" -- Federico Bravo Morata (1984)
- **What it contains**: Comprehensive guide to Madrid street names and their origins.
- **Format**: Physical book
- **Quality/Completeness**: Good 1980s reference; predates many modern nomenclature changes.

### 3.5 "Las calles de Madrid: noticias, tradiciones y curiosidades" -- Hilario Peñasco de la Puente & Carlos Cambronero (1889)
- **What it contains**: Historical anecdotes, traditions, and curiosities about Madrid streets.
- **Format**: Physical book (19th century)
- **Quality/Completeness**: Valuable primary historical source.

### 3.6 "Diccionario de Madrid (las calles, sus nombres, su historia, su ambiente)" -- Juan Antonio Cabezas (1972)
- **What it contains**: Dictionary format covering street names, history, and atmosphere.
- **Format**: Physical book
- **Quality/Completeness**: Useful mid-20th century reference.

---

## 4. ONLINE ARTICLES & BLOGS (with etymological content)

### 4.1 Civitatis Blog: "Barrios de Madrid: orígenes de sus nombres"
- **URL**: https://www.civitatis.com/blog/origen-nombre-barrios-madrid/
- **What it contains**: Origins of major neighbourhood names: Malasaña (Manuela Malasaña, 1808 uprising heroine), La Latina (Beatriz Galindo, Latin scholar), Lavapiés (Jewish foot-washing fountain OR muddy Manzanares waters), Chueca (composer Federico Chueca), Salamanca (José de Salamanca y Mayol, developer), Barrio de las Letras (Golden Age writers).
- **Format**: Web article (Spanish)
- **Quality/Completeness**: GOOD for popular audience. Covers ~6-8 major barrios with concise etymologies. Not comprehensive for all 131 barrios.

### 4.2 El Mirador de Madrid: "Distritos de Madrid: origen e historia"
- **URL**: https://elmiradordemadrid.es/distritos-madrid-origen-historia/
- **What it contains**: History and evolution of all 21 districts from medieval origins to present.
- **Format**: Web article (Spanish)
- **Quality/Completeness**: Covers all 21 districts but historical depth varies.

### 4.3 Walks of Italy / TakeWalks: "Madrid Neighborhood Names -- 10 Most Interesting Origins"
- **URL**: https://www.takewalks.com/blog/madrid-neighborhood-names
- **What it contains**: 10 neighbourhood etymologies in English: Los Austrias (Habsburg dynasty), Puerta del Sol (sun gate), La Latina, Barrio de las Letras, Salamanca, Malasaña, Lavapiés, Chueca, Vallecas ("Valle de Cas" = oak valley, documented 1202), Prosperidad (Prospero Soynard, 1862 land developer).
- **Format**: Web article (English)
- **Quality/Completeness**: GOOD for English-language reference. 10 well-researched entries.

### 4.4 Historias Matritenses Blog: Toponymy Series
- **URL**: https://historias-matritenses.blogspot.com/2010/11/algo-de-toponimia-iii.html
- **Also**: https://historias-matritenses.blogspot.com/2014/07/la-fabula-del-nombre-de-hortaleza.html
- **What it contains**: Detailed blog posts on specific Madrid toponyms. The "Algo de Toponimía" series covers street name changes from municipal annexations (1948-1954) -- documenting how Franco-era names were replaced. The Hortaleza article examines the contested etymology (Orta Lucis vs. Hortus vs. Fortaleza).
- **Format**: Blog posts (Spanish)
- **Quality/Completeness**: GOOD. Well-researched, uses primary sources. Covers niche topics not found elsewhere.

### 4.5 Madripedia Wiki
- **URL**: https://madripedia.wikis.cc/wiki/Calles_(Historia)
- **Also**: https://madripedia.wikis.cc/wiki/Origen_del_nombre_de_Madrid
- **What it contains**: Wiki-format encyclopedia of Madrid. The Calles (Historia) article covers: the 1749 census (557 blocks, 7,049 houses), the 1765 numbering system, Fermín Caballero's 1840 classification of 15 types of thoroughfares, etymology categories (topographical, religious, occupational, etc.), the Marquis of Pontejos' 1835 renaming of ~240 streets.
- **Format**: Wiki (Spanish)
- **Quality/Completeness**: GOOD. Systematic and well-organized. Covers administrative history of street naming.

### 4.6 Wikilengua: Topónimos de España/Madrid/Madrid
- **URL**: https://www.wikilengua.org/index.php/Top%C3%B3nimos_de_Espa%C3%B1a/Madrid/Madrid
- **What it contains**: List of all 21 districts, notable barrios, popular streets. Some etymological notes (Malasaña, Moncloa, La Latina). Includes gentilicios (demonyms) for each district.
- **Format**: Wiki (Spanish)
- **Quality/Completeness**: MODERATE. Good as an index/overview, but etymological detail is sparse.

### 4.7 Wikipedia: Nomenclátor callejero de Madrid
- **URL**: https://es.wikipedia.org/wiki/Nomencl%C3%A1tor_callejero_de_Madrid
- **What it contains**: History of Madrid's street nomenclature from 1750 to present. Key data: ~9,139 streets (2010), 56% named after historical personalities, 22.5% political geography, 12% physical geography, 7% abstract concepts. Documents name changes across political periods (Restoration, Republic, Franco, Democracy).
- **Format**: Wikipedia article (Spanish)
- **Quality/Completeness**: GOOD. Well-sourced Wikipedia article with broad historical sweep.

### 4.8 Wikipedia: Barrios administrativos de Madrid
- **URL**: https://es.wikipedia.org/wiki/Anexo:Barrios_administrativos_de_Madrid
- **What it contains**: Complete list of all 131 barrios organized by the 21 districts. Names and codes only.
- **Format**: Wikipedia article (Spanish)
- **Quality/Completeness**: COMPLETE for the list of all barrio names. No etymological information.

### 4.9 Wikipedia: Calles y plazas del Madrid medieval
- **URL**: https://es.wikipedia.org/wiki/Calles_y_plazas_del_Madrid_medieval
- **What it contains**: Medieval street and plaza names, their origins in the Arab citadel (al-mudena wall, Muhammad I, 852-886). Categories: topographical, occupational (Cuchilleros, Esparteros), religious, geographical routes (streets named Toledo, Hortaleza as ancient roads).
- **Format**: Wikipedia article (Spanish)
- **Quality/Completeness**: GOOD for medieval period. Links street names to specific historical periods and functions.

### 4.10 Calles de Madrid (Research Project)
- **URL**: https://callesdemadrid.cc/
- **Bibliography**: https://callesdemadrid.cc/informe/bibliografia/
- **What it contains**: Systematic analysis of 8,014 Madrid streets. 3,025 streets named after people (89% men, 11% women). Includes maps, working notes, methodology, and bibliography of key reference works. Licensed CC-BY-SA 4.0.
- **Format**: Research website with interactive maps and reports
- **Quality/Completeness**: VERY GOOD. Modern, data-driven approach. Strong on gender analysis and categorization. Excellent bibliography page listing all major reference works.

### 4.11 The Making of Madrid: "Street Signs in Madrid: a Brief History"
- **URL**: http://themakingofmadrid.com/2020/02/21/when-the-streets-had-no-names/
- **What it contains**: English-language history of Madrid street naming. Pre-literate naming practices (descriptions becoming names: "street of the lemon tree," "street of the sword makers"). The Marqués de Pontejos' formalization in the 19th century. Ceramic street signs by Alfredo Ruiz de Luna (1990s) that illustrate name origins.
- **Format**: Blog post (English)
- **Quality/Completeness**: GOOD. Accessible English-language overview.

### 4.12 Secretos de Madrid: "Origen del nombre 'Chamberí'"
- **URL**: https://www.secretosdemadrid.es/origen-del-nombre-chamberi/
- **What it contains**: Five competing theories for Chamberí's name: (1) French regiment "Chambery" during War of Independence; (2) Queen Luisa Gabriela de Saboya; (3) Doña Bárbara de Braganza and Salesas Reales convent (nuns from Chambéry, Savoy); (4) Celtic origin; (5) Others.
- **Format**: Web article (Spanish)
- **Quality/Completeness**: GOOD. Shows the complexity/uncertainty of etymological research.

### 4.13 Carabanchel Alto: "Origen del Nombre de Carabanchel"
- **URL**: https://carabanchelalto.es/historia/origen-del-nombre-de-carabanchel/
- **Also**: https://caminandopormadrid.com/el-origen-del-nombre-de-carabanchel
- **What it contains**: Multiple theories: (1) "Karavan" (caravans for commerce); (2) "tierra pedregosa/garbanzal" (stony/chickpea land); (3) Jaime Oliver Asín's "Carab" (cultivable land holder).
- **Format**: Web articles (Spanish)
- **Quality/Completeness**: GOOD. Multiple sourced theories.

---

## 5. HISTORICAL CARTOGRAPHY & DIGITAL TOOLS

### 5.1 HISDI-MAD (CSIC Historical Spatial Data Infrastructure)
- **URL**: https://idehistoricamadrid.csic.es/
- **About**: https://www.ilc.csic.es/es/webpage/hisdi-mad-infraestructura-datos-espaciales-ide-historica-ciudad-madrid
- **What it contains**: Geoportal of historical cartography and demography for Madrid, 1860-present. Three viewers: cartographic visualizer, map comparator, sociodemographic visualizer. Based on Facundo Cañada López 1902 map. Tracks population data 1890-1935.
- **Format**: Web GIS platform (OGC standards)
- **Quality/Completeness**: EXCELLENT for historical spatial analysis. Free access. Allows overlaying historical maps with current ones. Not specifically about name origins but invaluable for understanding when/how areas were named.

### 5.2 EsconD: Mapas históricos de Madrid
- **URL**: https://www.escond.es/planosdemadrid
- **What it contains**: Georeferenced historical maps from 1622 (Mancelli plan) to 1940s. Includes the 1656 Texeira plan (20 sheets, ~1:1,840 scale). Can compare historical street layouts with current maps.
- **Format**: Interactive web viewer
- **Quality/Completeness**: VERY GOOD. Beautiful georeferenced maps. Street names visible on historical plans allow tracking of name evolution.

### 5.3 Ayuntamiento de Madrid Cartoteca: Planos de Madrid y su época
- **URL**: https://www.madrid.es/portales/munimadrid/es/Inicio/Vivienda-urbanismo-y-obras/Urbanismo/Cartografia/Cartoteca/Planos-de-Madrid-y-su-epoca/
- **What it contains**: Official municipal cartographic archive. Historical plans from the Archivo de Villa and Museo de Historia de Madrid.
- **Format**: Digital reproductions of historical maps
- **Quality/Completeness**: Authoritative municipal source. Primary documents.

### 5.4 IGN Historical Map Comparator
- **URL**: Referenced via https://www.cartografiadigital.es/2025/01/planos-historicos-de-madrid-1622-1960.html
- **What it contains**: Instituto Geográfico Nacional tool with 10 historical plans (1622, 1656, 1761, 1769, 1785, 1848, 1900, 1910, 1929, 1940) that can be compared with current street grid.
- **Format**: Interactive web comparator
- **Quality/Completeness**: Official government tool. Excellent for visual comparison.

### 5.5 Wikipedia: Evolución histórica del plano de Madrid
- **URL**: https://es.wikipedia.org/wiki/Evoluci%C3%B3n_hist%C3%B3rica_del_plano_de_Madrid
- **What it contains**: Overview article on the historical evolution of Madrid's urban plan.
- **Format**: Wikipedia article
- **Quality/Completeness**: Good overview with references to primary sources.

---

## 6. SPECIFIC ETYMOLOGIES FOUND (Summary by District)

### Districts with well-documented etymologies:

| District | Etymology |
|----------|-----------|
| **Centro** | Self-explanatory: the historic centre of Madrid |
| **Arganzuela** | From "Arganduela" = "Pequeña Arganda" (little Arganda), settlers from Arganda del Rey on the Manzanares riverbank |
| **Retiro** | From the Palacio del Buen Retiro (1633), built by Felipe IV as a "retreat" (retiro) for rest/contemplation. Origin traces to San Jerónimo monastery where monarchs retired during Lent/mourning |
| **Salamanca** | José de Salamanca y Mayol (1811-1883), Marquis of Salamanca, politician and developer who planned and built the neighbourhood |
| **Chamartín** | Former independent municipality annexed in 1948. Etymology disputed. |
| **Tetuán** | Named "Tetuán de las Victorias" after Spanish troops returning from victory at Tétouan (Morocco) in the African War of 1860 camped here |
| **Chamberí** | Disputed: (1) French regiment "Chambery" in War of Independence; (2) Salesas nuns from Chambéry, Savoy; (3) Queen connection to Saboya; (4) Possible Celtic origin |
| **Fuencarral-El Pardo** | Fuencarral: "Fuente del Carral" or similar water source. El Pardo: from the brownish/dark (pardo) colour of the landscape or hunting estate |
| **Moncloa-Aravaca** | Moncloa: from Palacio de la Moncloa. Aravaca: Celtic origin (per Caridad Arias 2004) |
| **Latina** | From Beatriz Galindo "La Latina" (1465-1534), Latin scholar and advisor to Isabel la Católica |
| **Carabanchel** | Disputed: (1) Celtic origin; (2) "Karavan" (caravans); (3) "Garbanzal" (chickpea field); (4) Arabic "Carab" (cultivable land) |
| **Usera** | Named after Marcelo de Usera, 19th-century landowner |
| **Puente de Vallecas** | "Vallecas" from "Valle de Cas" (oak valley), documented as "Balecas" in the 1202 Fuero de Madrid; "Puente" refers to the bridge |
| **Moratalaz** | Possibly Arabic origin: from "morata" (a type of blackberry plant) + Arabic suffix |
| **Ciudad Lineal** | From Arturo Soria's 1882/1885 "Ciudad Lineal" (linear city) urban planning concept |
| **Hortaleza** | Disputed: (1) Latin "Orta Lucis" (sunrise, due to eastern location); (2) Latin "Hortus" (garden/orchards); (3) Corruption of "Fortaleza" (fortress) |
| **Villaverde** | "Villa verde" = green village/town, descriptive of the landscape |
| **Villa de Vallecas** | See Vallecas above. "Villa" denotes its former status as an independent municipality |
| **Vicálvaro** | Former independent municipality. "Vico Álvaro" = Álvaro's village/settlement |
| **San Blas-Canillejas** | San Blas: patron saint of the original parish. Canillejas: ancient municipality (13th century), annexed 1949 |
| **Barajas** | Former municipality (annexed 1949). Arabic origin possible: from "baraha" or similar |

### Notable Barrio etymologies:

| Barrio | Etymology |
|--------|-----------|
| **Malasaña** | Manuela Malasaña (1791-1808), seamstress killed resisting Napoleon's troops on 2 May 1808. Formerly "Barrio de las Maravillas" (Virgen de las Maravillas convent). Name adopted in the 1980s Movida |
| **Lavapiés** | Disputed: (1) Fountain where Jews washed feet before synagogue; (2) Manzanares river mud washing feet |
| **Chueca** | Composer Federico Chueca (1846-1908), zarzuela master. Plaza named after him; barrio adopted name as LGBTQ+ community grew |
| **Barrio de las Letras** | Golden Age writers who lived there: Cervantes, Lope de Vega, Quevedo, Góngora |
| **Delicias** | "Las delicias del río" (the delights of the river) -- pleasant area leading to the Manzanares |
| **Prosperidad** | Prospero Soynard, who bought land north of Madrid in 1862 and subdivided it |
| **Leganitos** | Arabic "algannet" = the orchards |

---

## 7. STREET NAME CATEGORIES (from Wikipedia/Madripedia)

Madrid's ~9,139 streets break down as:
- **56%** -- Historical personalities
- **22.5%** -- Political geography toponyms
- **12%** -- Physical geography
- **7%** -- Abstract concepts
- **2.5%** -- Other

Historical categories of name origins (per Fermín Caballero, 1840):
- Topographical: Barranco, Arenal, Vega, Cerro
- Owner/patron names: Preciados, Conde de Miranda
- Religious: Cuesta de Santo Domingo
- Occupational/guild: Cuchilleros, Esparteros, Latoneros, Cabestreros
- Route destinations: Toledo, Hortaleza (ancient roads to those towns)
- Vegetation: Almendro, Limón
- Descriptive: Angosta, Transversal, Ronda

---

## 8. KEY GAPS & NOTES

1. **No single comprehensive open dataset exists** that combines barrio/district names with their etymologies. The structured datasets (datos.madrid.es) contain names and geographic data but not origins.
2. **A major Madrid-specific scholarly work** is Aparisi Laporta (2001-2005) with 20,000+ toponyms, but it remains a physical/catalogue lookup rather than an open full-text source.
3. **The historical street directory** at datos.madrid.es tracks name *changes* over time but does not explain *why* streets were originally named.
4. **Building a dataset of name origins would require** combining the structured data from datos.madrid.es (names, codes, boundaries) with etymological information manually extracted from scholarly sources (especially Aparisi Laporta, Gea Ortigas, and the various blog/wiki sources documented above).
5. **The Capmany (1863) work** is available through the Biblioteca Digital de la Comunidad de Madrid and belongs in the digitized-first source group.
6. **For district names specifically**, many derive from former independent municipalities (Carabanchel, Vallecas, Barajas, Vicálvaro, Hortaleza, Canillejas, Aravaca, Fuencarral, El Pardo, Chamartín) whose etymologies predate their incorporation into Madrid (1948-1954).
