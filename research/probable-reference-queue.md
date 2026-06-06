# Probable Station Reference Queue

**Updated**: 2026-06-06
**Scope**: `content/stations` entries where `confidence == probable`.

The station metadata is the authoritative per-entry queue. This file is a compact triage view for the 144 probable entries and their 291 `open_questions`, grouped by source family so research can be done in batches.

## Counts

| Source family | Matching probable entries | Best first action |
|---|---:|---|
| Municipal, street, and planning records | 103 | Search official callejero history, municipal naming files, planning-sector files, and local council minutes before adding more books. |
| Transport naming and opening records | 71 | Check CRTM/Metro/Comunidad de Madrid publications first; use Docutren or railway archives for Cercanías naming and timetable questions. |
| Historical maps, cadastre, and land records | 64 | Check IGN/CNIG historical layers, old municipal maps, cadastral plans, and land inventories for rural microtoponyms. |
| Archives and primary documents | 49 | Use Archivo de Villa, municipal archives, BNE/Hemeroteca, BOE/BOCM, and edited primary-source collections. |
| Printed books, articles, and toponymy references | 31 | Use targeted page lookups only; do not reopen broad books unless the station metadata names them. |

The categories overlap: a station may need both a map and a transport naming file.

## Digital-First Resources

| Resource | Use for | Access |
|---|---|---|
| Madrid Callejero Municipal and Geoportal | Current official street names, vials, historical changes, codes, and likely street-derived station names inside Madrid municipality. | <https://www.madrid.es/go/INFORMACION-CALLEJERO>. Local ignored mirror downloaded from the CKAN API on 2026-06-06 under `research/local-sources/callejero-oficial-madrid-2026-06-01/`. |
| Madrid Callejero file description | Explains the downloadable CSVs, including historical vial-name evolution and date fields. | <https://www.madrid.es/FWProjects/egob/Catalogo/UrbanismoInfraestructura/Ficheros/Callejero%20oficial%20-%20descripci%C3%B3n%20de%20ficheros.pdf> |
| Madrid calle-name change consultation | Use after the CSV when the open question asks for a formal street-name or numbering change file. | <https://sede.madrid.es/portal/site/tramites/menuitem.62876cb64654a55e2dbd7003a8a409a0/?vgnextoid=f794d1d1a8e1b810VgnVCM1000001d4a900aRCRD&vgnextchannel=183737c190180210VgnVCM100000c90da8c0RCRD> |
| Nomecalles, Comunidad de Madrid | Official nomenclator/callejero for municipalities outside Madrid city: Parla, Pozuelo, Boadilla, Leganés, Alcorcón, Getafe, Alcobendas, etc. | <https://web.comunidad.madrid/nomecalles_web/> |
| IGN/CNIG historical map services | Planimetrías, Hojas Kilométricas, Planos de Madrid 1622-1960, first MTN edition, historical PNOA, and names/geographic layers. | <https://www.ign.es/web/ide-area-nodo-ide-ign> |
| IGN Cartoteca catalogue | Specific old maps and scanned sheets; use when metadata names a map sheet or when WMS inspection is inconclusive. | <https://www.ign.es/web/catalogo-cartoteca/> |
| Archivo de Villa catalogue | Books of agreements, maps, drawings, royal documents, bandos, and records for Madrid and annexed municipalities. | <https://catalogoarchivodevilla.madrid.es/ms-opac/> |
| Memoria de Madrid | Digitized Madrid archival records, old books, plans, and municipal material. | <https://www.memoriademadrid.es/> |
| Comunidad de Madrid Metro expansion publications | Official construction books for Metro/Metro Ligero projects; good for station opening context and sometimes project names. | <https://www.comunidad.madrid/infraestructuras/publicaciones-ampliacion-metro-madrid> |
| CRTM historical Metro chronology PDF | Quick opening-date and connection check for Metro/ML stations. | <https://www.crtm.es/media/161811/metro_historico_cronologia_2.pdf> |
| Renfe Data Cercanías stations | Current station codes and official Cercanías station list. | <https://data.renfe.com/es/dataset/estaciones-cercanias-madrid> |
| Docutren / Archivo Histórico Ferroviario | Bibliographic and archival references for railway history, timetables, station names, and old company/RENFE files. | <https://www.docutren.com/> |

## Newly Confirmed Leads

These are not all new to the repo, but they are now useful as probable-entry search targets.

| Lead | Best targets | Note |
|---|---|---|
| Aparisi Laporta, "La toponimia madrileña. Proceso evolutivo" (1993 article) | Methodology for Madrid street/toponym work; not a station-entry source. | Checked locally from the Dialnet PDF, *Anales del Instituto de Estudios Madrileños* XXXIII, pp. 515-543. It explains source base and planned fields for the later full nomenclator, but does not resolve Pitis, Coslada, Aravaca, Valdecarros, Orcasitas, Fuente de la Mora, La Elipa, or similar open entries. |
| *Relaciones topográficas de Felipe II: Madrid*, Alfredo Alvar Ezquerra et al. | Leganés, Fuencarral, Carabanchel Alto, Somosaguas, and other old municipalities. | Google Books preview exists; physical or library lookup still needed for exact pages. UCM record: <https://produccioncientifica.ucm.es/documentos/689e238a755b275bc684ed65> |
| Madrid official Callejero historical-vial CSVs | Already applied to a first batch of Madrid street-derived entries: Ibiza, Valdeacederas, Oporto, San Cipriano, Almendrales, Tres Olivos, Acacias, Puerta del Ángel, Lucero, Laguna, Duque de Pastrana, Bambú, Vinateros, Avenida de América, Valdezarza, Opañel, La Elipa, Ascao, Urgel, Abrantes, Buenos Aires, Sierra de Guadalupe, Congosto, Alsacia, and Las Suertes. | Use next for remaining Madrid-municipality entries where the station name is plausibly a street/plaza/road name. Treat `01/01` dates as possible placeholders unless corroborated. |
| IGN historical layers | Fuente de la Mora, Puente Alcocer, El Goloso, Las Águilas, Almendrales, La Poveda, Tres Olivos, Montecarmelo, Las Tablas, Opañel, Valdezarza, Pan Bendito, El Bercial, Las Suertes. | Best for proving a pre-station rural paraje, bridge, road, stream, or field name. |
| Comunidad Metro publication *Prolongación de la línea 2 del Metro de Madrid a Las Rosas* | La Elipa, Las Rosas, Alsacia, and Line 2 extension context. | Free PDF found at `BVCM006087`; use for project context, not as final etymology. |
| Comunidad Metro publication *La ampliación del Metro de Madrid* | Valdebernardo, Alto del Arenal, and early expansion context. | Free PDF found at `BVCM006221`; useful for openings/design, usually not naming motive. |
| *De los tranvías a los metros ligeros en la Comunidad de Madrid* | ML2/ML3 and Tranvía de Parla station-name context. | Listed by Comunidad de Madrid; likely physical/bookshop item unless a PDF is found. |
| María Isabel Gea Ortigas, *Historia de los distritos de Madrid* series | San Blas, Hortaleza, Fuencarral-El Pardo, Carabanchel, Usera/Villaverde, Vallecas, Vicálvaro, Moncloa, and similar district/barrio cases. | Use the district-specific volume only when metadata asks for local barrio history. |
| Sánchez Molledo / Ferrando, *Retiro y sus barrios* | Estrella and Ibiza. | Bookshop records confirm the title and scope; no open full scan found. |
| Paloma Olmedo del Rosal, *Boadilla del Monte: Historia y testimonios* | Montepríncipe and Boadilla ML3 local context. | Physical/secondhand lead; Casa del Libro record confirms the 2007 title and ISBN. |
| Alejandro Peris Barrio, *Móstoles: de pequeña aldea a ciudad populosa* | Móstoles and Móstoles Central. | Móstoles municipal page confirms the work and editions; physical lookup still needed. |
| José Luis García Heras / Vallecas VA material on Vallecas | Villa de Vallecas and Vallecas-related probable entries. | Useful online lead to Federico Corriente and Matilde Fernández Montes; still verify against the cited specialist source before changing confidence. |

## Next Source Choices

| Priority | Source | Why it is next |
|---:|---|---|
| 1 | Luis Miguel Aparisi Laporta, *Toponimia madrileña: proceso evolutivo* (full book/CD) | The 1993 article confirms the later full work is the real lookup target: it was designed as a structured Madrid nomenclator with current names, former names, municipal agreements, districts, barrios, and historical attestations. Highest expected payoff for Pitis, La Elipa, Valdecarros, Fuente de la Mora, Orcasitas, Valdebebas, Canillejas, and Avenida de la Paz. |
| 2 | Madrid Callejero historical-vial CSVs and municipal naming files | First CSV batch is now applied to 25 station entries. Use the CSVs for remaining Madrid-municipality street/plaza cases, then use municipal naming files when the CSV date is a placeholder or the motive still needs explanation. |
| 3 | IGN/CNIG historical maps and Cartoteca | Best digital-first route for inherited rural microtoponyms, bridges, roads, streams, and parajes. |
| 4 | José Felipe Alonso Fernández-Checa, *Metro de Madrid. ¿Por qué sus estaciones se llaman así?* | Best quick Metro cross-check and still important for Pitis, but the free sample shows it is selective and not enough by itself. |
| 5 | María Isabel Gea Ortigas, *Los nombres de las calles de Madrid* plus district-specific Gea volumes | Useful after the official Callejero pass, especially for street-derived names and district/barrio historical context. |
| 6 | Emilio Nieto Ballester, *Breve diccionario de topónimos españoles* | Best compact philological lookup for older municipality names: Parla, Chamartín, Manoteras, Móstoles, Leganés, Aravaca/Arevaci if present. |

## Source Family Station Batches

### Municipal, Street, and Planning Records

`cercanias_006` Fuente de la Mora; `cercanias_014` Orcasitas; `cercanias_015` Puente Alcocer; `cercanias_016` San Cristóbal de los Ángeles; `cercanias_021` Las Margaritas Universidad; `cercanias_027` Parla; `cercanias_031` El Goloso; `cercanias_033` Asamblea de Madrid-Entrevías; `cercanias_035` Santa Eugenia; `cercanias_039` Soto del Henares; `cercanias_043` Meco; `cercanias_048` Las Águilas; `cercanias_053` Las Retamas; `cercanias_057` Parque Polvoranca; `cercanias_060` Humanes; `cercanias_069` Galapagar-La Navata; `cercanias_070` San Yago; `cercanias_073` Santa María de la Alameda-Peguerinos; `cercanias_084` Tres Cantos; `cercanias_091` Valdelasfuentes; `cercanias_092` Zarzaquemada; `cercanias_094` Las Zorreras; `metro_040` Ibiza; `metro_049` Estrecho; `metro_050` Valdeacederas; `metro_053` Oporto; `metro_075` San Cipriano; `metro_077` Almendrales; `metro_080` Puerta de Arganda; `metro_081` Arganda del Rey; `metro_082` La Poveda; `metro_083` Tres Olivos; `metro_084` Montecarmelo; `metro_085` Las Tablas; `metro_096` Acacias; `metro_110` Nueva Numancia; `metro_111` Portazgo; `metro_114` Lucero; `metro_115` Laguna; `metro_124` Duque de Pastrana; `metro_126` Barrio del Pilar; `metro_127` Ventilla; `metro_128` Mirasierra; `metro_132` Quintana; `metro_135` Simancas; `metro_137` San Blas; `metro_138` Pueblo Nuevo; `metro_140` Bambú; `metro_141` Estrella; `metro_142` Vinateros; `metro_144` Avenida de América; `metro_148` Colonia Jardín; `metro_149` Opañel; `metro_150` Rivas Vaciamadrid; `metro_159` Alto del Arenal; `metro_170` La Elipa; `metro_171` Peñagrande; `metro_172` Parque de las Avenidas; `metro_173` Barrio de la Concepción; `metro_174` Ascao; `metro_179` Jarama; `metro_182` Urgel; `metro_195` La Rambla; `metro_204` Puerta del Sur; `metro_207` Aviación Española; `metro_208` Begoña; `metro_211` La Granja; `metro_212` La Moraleja; `metro_218` San Francisco; `metro_219` Pan Bendito; `metro_220` Abrantes; `metro_223` Parque Oeste; `metro_226` Pradillo; `metro_235` Getafe Central; `metro_237` Los Espartales; `metro_238` El Bercial; `metro_239` El Carrascal; `metro_241` Leganés Central; `metro_243` Buenos Aires; `metro_245` Sierra de Guadalupe; `metro_247` Congosto; `metro_248` Valdecarros; `metro_249` Las Rosas; `metro_251` Alsacia; `metro_253` San Fermín-Orcasur; `metro_254` Ciudad de los Ángeles; `metro_256` San Cristóbal; `metro_258` Las Suertes; `ml_003` Virgen del Cortijo; `ml_008` Palas de Rey; `ml_011` Prado de la Vega; `ml_013` Prado del Rey; `ml_014` Somosaguas Sur; `ml_018` Dos Castillas; `ml_027` Retamares; `ml_028` Montepríncipe; `ml_030` Prado del Espino; `ml_031` Cantabria; `ml_034` Nuevo Mundo; `ml_037` Puerta de Boadilla; `ml_045` Isabel II; `ml_046` Parque Parla Este; `ml_051` Jaime I.

### Transport Naming and Opening Records

`cercanias_013` Doce de Octubre; `cercanias_014` Orcasitas; `cercanias_016` San Cristóbal de los Ángeles; `cercanias_017` San Cristóbal Industrial; `cercanias_018` Getafe Industrial; `cercanias_021` Las Margaritas Universidad; `cercanias_024` Valdemoro; `cercanias_026` Aranjuez; `cercanias_029` Cantoblanco Universidad; `cercanias_031` El Goloso; `cercanias_033` Asamblea de Madrid-Entrevías; `cercanias_039` Soto del Henares; `cercanias_043` Meco; `cercanias_053` Las Retamas; `cercanias_060` Humanes; `cercanias_069` Galapagar-La Navata; `cercanias_070` San Yago; `cercanias_071` El Escorial; `cercanias_073` Santa María de la Alameda-Peguerinos; `cercanias_076` Collado Mediano; `cercanias_084` Tres Cantos; `cercanias_092` Zarzaquemada; `cercanias_094` Las Zorreras; `metro_009` Lavapiés; `metro_036` Moncloa; `metro_040` Ibiza; `metro_053` Oporto; `metro_057` Esperanza; `metro_073` Valdebernardo; `metro_074` Vicálvaro; `metro_080` Puerta de Arganda; `metro_082` La Poveda; `metro_084` Montecarmelo; `metro_096` Acacias; `metro_112` Puerta del Ángel; `metro_115` Laguna; `metro_135` Simancas; `metro_147` Valdezarza; `metro_148` Colonia Jardín; `metro_159` Alto del Arenal; `metro_161` Hortaleza; `metro_172` Parque de las Avenidas; `metro_173` Barrio de la Concepción; `metro_179` Jarama; `metro_195` La Rambla; `metro_204` Puerta del Sur; `metro_206` Cuatro Vientos; `metro_207` Aviación Española; `metro_208` Begoña; `metro_209` Fuencarral; `metro_212` La Moraleja; `metro_218` San Francisco; `metro_219` Pan Bendito; `metro_223` Parque Oeste; `metro_225` Móstoles Central; `metro_226` Pradillo; `metro_235` Getafe Central; `metro_241` Leganés Central; `metro_245` Sierra de Guadalupe; `metro_246` Villa de Vallecas; `metro_255` Villaverde Bajo-Cruce; `metro_257` Villaverde Alto; `metro_258` Las Suertes; `ml_011` Prado de la Vega; `ml_014` Somosaguas Sur; `ml_016` Pozuelo Oeste; `ml_031` Cantabria; `ml_037` Puerta de Boadilla; `ml_045` Isabel II; `ml_046` Parque Parla Este; `ml_051` Jaime I.

### Historical Maps, Cadastre, and Land Records

`cercanias_006` Fuente de la Mora; `cercanias_015` Puente Alcocer; `cercanias_017` San Cristóbal Industrial; `cercanias_021` Las Margaritas Universidad; `cercanias_029` Cantoblanco Universidad; `cercanias_031` El Goloso; `cercanias_033` Asamblea de Madrid-Entrevías; `cercanias_039` Soto del Henares; `cercanias_048` Las Águilas; `cercanias_053` Las Retamas; `cercanias_070` San Yago; `cercanias_084` Tres Cantos; `cercanias_085` Valdebebas; `cercanias_092` Zarzaquemada; `cercanias_094` Las Zorreras; `metro_010` Chamberí; `metro_049` Estrecho; `metro_050` Valdeacederas; `metro_073` Valdebernardo; `metro_075` San Cipriano; `metro_077` Almendrales; `metro_082` La Poveda; `metro_083` Tres Olivos; `metro_084` Montecarmelo; `metro_085` Las Tablas; `metro_112` Puerta del Ángel; `metro_114` Lucero; `metro_115` Laguna; `metro_126` Barrio del Pilar; `metro_138` Pueblo Nuevo; `metro_141` Estrella; `metro_142` Vinateros; `metro_144` Avenida de América; `metro_147` Valdezarza; `metro_149` Opañel; `metro_159` Alto del Arenal; `metro_161` Hortaleza; `metro_171` Peñagrande; `metro_173` Barrio de la Concepción; `metro_182` Urgel; `metro_195` La Rambla; `metro_206` Cuatro Vientos; `metro_208` Begoña; `metro_211` La Granja; `metro_212` La Moraleja; `metro_219` Pan Bendito; `metro_223` Parque Oeste; `metro_225` Móstoles Central; `metro_238` El Bercial; `metro_239` El Carrascal; `metro_248` Valdecarros; `metro_249` Las Rosas; `metro_253` San Fermín-Orcasur; `metro_254` Ciudad de los Ángeles; `metro_258` Las Suertes; `ml_003` Virgen del Cortijo; `ml_013` Prado del Rey; `ml_014` Somosaguas Sur; `ml_027` Retamares; `ml_029` Ventorro del Cano; `ml_030` Prado del Espino; `ml_031` Cantabria; `ml_037` Puerta de Boadilla; `ml_045` Isabel II.

### Archives and Primary Documents

`cercanias_013` Doce de Octubre; `cercanias_014` Orcasitas; `cercanias_017` San Cristóbal Industrial; `cercanias_021` Las Margaritas Universidad; `cercanias_026` Aranjuez; `cercanias_027` Parla; `cercanias_030` Alcobendas-San Sebastián de los Reyes; `cercanias_033` Asamblea de Madrid-Entrevías; `cercanias_035` Santa Eugenia; `cercanias_056` Leganés; `cercanias_057` Parque Polvoranca; `cercanias_060` Humanes; `cercanias_069` Galapagar-La Navata; `cercanias_070` San Yago; `cercanias_086` Vallecas; `metro_009` Lavapiés; `metro_036` Moncloa; `metro_050` Valdeacederas; `metro_055` Carabanchel; `metro_073` Valdebernardo; `metro_075` San Cipriano; `metro_077` Almendrales; `metro_081` Arganda del Rey; `metro_083` Tres Olivos; `metro_085` Las Tablas; `metro_111` Portazgo; `metro_126` Barrio del Pilar; `metro_132` Quintana; `metro_138` Pueblo Nuevo; `metro_142` Vinateros; `metro_148` Colonia Jardín; `metro_149` Opañel; `metro_162` Manoteras; `metro_171` Peñagrande; `metro_173` Barrio de la Concepción; `metro_207` Aviación Española; `metro_209` Fuencarral; `metro_217` Carabanchel Alto; `metro_226` Pradillo; `metro_238` El Bercial; `metro_241` Leganés Central; `metro_243` Buenos Aires; `metro_247` Congosto; `metro_254` Ciudad de los Ángeles; `metro_255` Villaverde Bajo-Cruce; `ml_013` Prado del Rey; `ml_014` Somosaguas Sur; `ml_022` Estación de Aravaca; `ml_029` Ventorro del Cano.

### Printed Books, Articles, and Toponymy References

| Resource | Targets |
|---|---|
| Alvar Ezquerra et al., *Relaciones topográficas de Felipe II: Madrid* | `cercanias_056` Leganés; `metro_209` Fuencarral; `metro_217` Carabanchel Alto; `metro_241` Leganés Central; `ml_014` Somosaguas Sur. |
| Emilio Nieto Ballester, *Breve diccionario de topónimos españoles* | `cercanias_004` Chamartín-Clara Campoamor; `cercanias_027` Parla; `metro_162` Manoteras; `metro_179` Jarama; `metro_225` Móstoles Central. |
| María Isabel Gea Ortigas works | `cercanias_014` Orcasitas; `metro_112` Puerta del Ángel; `metro_137` San Blas; `metro_172` Parque de las Avenidas; `metro_253` San Fermín-Orcasur. |
| Jairo J. García Sánchez works | `cercanias_006` Fuente de la Mora; `cercanias_051` Alcorcón; `metro_222` Alcorcón Central. |
| Luis Miguel Aparisi Laporta, *Toponimia madrileña* | `metro_170` La Elipa; `metro_248` Valdecarros. |
| Oliver Asín / Madrid-name studies | `cercanias_085` Valdebebas; `metro_055` Carabanchel; `metro_217` Carabanchel Alto. |
| Edelmiro Bascuas, *Hidronimia y léxico de origen paleoeuropeo en Galicia* | `cercanias_060` Humanes; `ml_008` Palas de Rey. |
| Lapesa, *Historia de la lengua española* | `cercanias_026` Aranjuez. |
| Casiano de Prado, *Descripción física y geológica de la provincia de Madrid* | `cercanias_071` El Escorial. |
| Alejandro Peris Barrio, *Móstoles: de pequeña aldea a ciudad populosa* | `cercanias_054` Móstoles. |
| *Leganés. Una ciudad, una historia* | `cercanias_057` Parque Polvoranca. |
| Sánchez Molledo / Ferrando, *Retiro y sus barrios* | `metro_141` Estrella. |
| Matilde Fernández Montes / Federico Corriente on Vallecas | `metro_246` Villa de Vallecas. |
| Paloma Olmedo del Rosal, *Boadilla del Monte: Historia y testimonios* | `ml_028` Montepríncipe. |

## What to Capture

For any source lookup, capture:

1. Exact source title, author/institution, edition/date, URL or library/catalogue record.
2. Page, folio, map sheet, file code, or CSV row fields.
3. The minimum wording needed to support the claim, paraphrased in station prose.
4. Whether the source resolves the open question, only improves context, or contradicts the current entry.

Do not upgrade `probable` to `verified` just because a source repeats the same theory. Upgrade only when the missing naming act, primary place-name attestation, or authoritative specialist entry has actually been checked.
