# Station Etymology Status Report

**Date**: 2026-03-28
**Scope**: All 390 transport station entries (243 metro + 95 cercanías + 52 ML/tranvía)

## Current State

| Confidence | Metro | Cercanías | ML/Tranvía | Total |
|-----------|-------|-----------|------------|-------|
| **verified** | 200 | 53 | 36 | **289** |
| **probable** | 35 | 35 | 16 | **86** |
| **uncertain** | 7 | 7 | 0 | **14** |
| **unknown** | 1 | 0 | 0 | **1** (Pitis) |
| **Total** | 243 | 95 | 52 | **390** |

- **0** entries with generic "Wikipedia" as only source
- **~66** entries cite web sources without full URLs (e.g. "Muy Interesante", "Civitatis") -- resolvable with the Alonso Fernández-Checa book

## Key Findings from This Research Session

### Factual Error Corrected
- **Barrio del Pilar** (metro_126): Was listed as religious/Virgen del Pilar. Actually named after **Pilar, wife of developer José Banús** (1961 wedding gift). Source: El Español investigative article 2023.

### Wikidata Audit
- ~90% of original QIDs were fabricated (capybara, asteroids, etc.)
- All 148 unique QIDs corrected via Wikidata API verification

### Stations Upgraded to Verified (this session)
1. Aranjuez (García Sánchez CVC confirms Basque arantza)
2. El Escorial (García Sánchez CVC Part II + Lorenzo Arribas CVC)
3. Aluche x2 (Arroyo Luche documented in Felipe II Real Cédula 1580)
4. Collado Mediano (García Pérez UPM dissertation)
5. Zarzaquemada (RAE + Dialnet article on slash-and-burn)
6. Vallecas (Fuero de Madrid 1202 at Cervantes Virtual)
7. La Gavia (RAE + Iedra + Complutum UCM peer-reviewed archaeology)
8. San Fermín-Orcasur (Federico Mayo Gayarre documented + Isabel Gea for Orcasitas)
9. La Moraleja (Toponomasticon Hispaniae scholarly entry)
10. Barrio del Pilar (etymology corrected + verified with investigative source)
11. Cruz del Rayo (Ayto. Madrid + Urban Idade 1928 colonia documentation)

### New Scholarly Sources Discovered
- García Sánchez CVC Rinconete series (4 parts) with specific URLs
- Toponomasticon Hispaniae entries for Moraleja, Fuenlabrada, Valdemoro, Pinto
- Diago Hernando (Sefarad/CSIC 1993) for La Garena
- García Sánchez "En torno a la toponimia madrileña" (De Gruyter 2010) for Coslada
- Sánchez González "De Alarnes a Getafe" (1989) for Getafe
- Caridad Arias's CIL epigraphy for Aravaca (Arevaci)
- IGN digitized Chalmandrier 1761 map for Chamberí
- Facundo Cañada López 1900 map at CSIC for Opanel/Pitis
- García Pérez UPM dissertation on Sierra de Guadarrama toponymy
- Aparisi Laporta "Toponimia e iconografía en Fuencarral-El Pardo" (2005) -- 70-page focused work, KEY for Pitis

## 14 Uncertain Stations -- Detailed Status

### Genuinely disputed (7) -- uncertain is correct
| Station | # of theories | Top scholarly source |
|---------|--------------|---------------------|
| Lavapies | 4 | Lorenzo Arribas CVC 2008 + Bazaco Palacios 2013 |
| Carabanchel | 5 | Menéndez Pidal 1953 + Caridad Arias 2004 |
| Barajas | 4 | Nieto Ballester 1997 + Caridad Arias 2007 |
| Getafe x2 | 3 | García Sánchez CVC 2007 (explicit "genuinely uncertain") |
| Coslada | 3 | Menéndez Pidal 1952 + García Sánchez 2010 |
| Valdemoro | 6 | Toponomasticon Hispaniae + García Sánchez CVC 2008 |
| Meco | 3 | Quadernillos + Rodríguez Morales (Miacum rejection) |

### Enriched with new sources (5) -- uncertain, needs physical books
| Station | Key new finding | Book needed |
|---------|----------------|-------------|
| Aravaca | Caridad Arias CIL epigraphy for Arevaci | Full article PDF on Dialnet |
| La Garena | Diago Hernando (CSIC 1993) for Lucena family | Municipal archive Alcalá de Henares |
| Opanel | Villar Liébana typological (not direct) connection | Full Palaeohispanica article |
| Valdecarros | 1296 document + Valle de Navarros theory | Aparisi Laporta vol. 2 |
| Pitis x2 | Arroyo de los Pinos nearby; area had poplar grove + stream | Aparisi Laporta Fuencarral-El Pardo (2005) |

## Remaining "Probable" Stations (86 total)

### Could be upgraded to verified with the Alonso Fernández-Checa book:
Essentially ALL 35 remaining probable metro stations. The book covers every station.

### Cercanías probable that need specific sources:
Most of the 35 probable cercanías are descriptive/transparent names (Fuente de la Mora, Cantoblanco, Tres Cantos, Las Matas, etc.) where the etymology is clear but no scholarly source directly addresses them.

### ML/Tranvía probable (16):
Mostly transparent names in Pozuelo/Boadilla/Parla developments. Can be verified with municipal documentation.

## What the Alonso Fernández-Checa Book Would Solve

This ~16 EUR book covers ALL metro stations. It would:
1. Provide a citable scholarly source for every metro entry
2. Potentially resolve Pitis (the only genuinely unknown station)
3. Upgrade most of the 35 probable metro stations to verified
4. Replace ~31 entries that cite web sources without full URLs

**Estimated impact**: Could push metro verified count from 200 to ~230+.

## Online Resources Still Unexploited

| Resource | URL | What to look for |
|----------|-----|-----------------|
| PARES Catastro de Ensenada | pares.cultura.gob.es | Fuencarral 1749-53 survey for Pitis |
| IGN minutas cartográficas | datos.gob.es (visualizador mapas antiguos) | Pre-railway Pitis attestation |
| Facundo Cañada López 1900 map | digital.csic.es/handle/10261/28971 | Pitis on 1:7,500 map |
| BNE hemeroteca digital | hemerotecadigital.bne.es | Pre-1964 newspaper mentions of Pitis |
| Memoria de Madrid | memoriademadrid.es | Fuencarral municipal documents |
| IGN Chalmandrier 1761 interactive | ign.es/web/catalogo-cartoteca/resources/webmaps/chalmandrier.html | Already used for Chamberí |
