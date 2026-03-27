# Wikidata QID Audit Report

**Date**: 2026-03-27
**Scope**: All 7 hand-curated CSV files (475 entries, 148 unique QIDs)

## Summary

~90% of the original Wikidata QIDs were fabricated/hallucinated. They pointed to completely unrelated entities (capybara, asteroids, Gerry Scotti, the 1986 Mexican Grand Prix, etc.). All 148 unique QIDs were verified against the Wikidata API and corrected.

## Methodology

1. Extracted all unique QIDs from all 7 CSV files using Python/csv
2. Batch-verified against `wbgetentities` API endpoint (50 per request)
3. For mismatches, searched for correct QID using `wbsearchentities` API
4. Applied bulk corrections, then manually fixed ~15 entries where auto-search returned wrong results
5. Ran final verification pass -- all remaining "issues" are accent mismatches (Alcorcón, Leganés, etc.)

## Corrections Applied

### Confirmed wrong QIDs (sample of most egregious)

| Old QID | What it pointed to | Correct QID | Correct entity |
|---------|-------------------|-------------|----------------|
| Q131538 | Capybara (rodent) | Q201315 | Francisco de Quevedo |
| Q171590 | 1986 Mexican Grand Prix | Q427163 | Puerta del Sol |
| Q363498 | Gerry Scotti (Italian TV) | Q515741 | Francisco Serrano |
| Q157054 | Giorgio Armani | Q157130 | Eugenia de Montijo |
| Q165017 | Sarah Thompson | Q18363 | Alfonso XIII |
| Q218837 | The Supremes | Q153300 | Paco de Lucía |
| Q380344 | Descriptive statistics | Q164027 | Santiago Bernabéu |
| Q329270 | Stone Temple Pilots | Q789966 | Bank of Spain |
| Q2655587 | 1943 NY Giants season | Q1708316 | Beatriz Galindo |
| Q727677 | Oliver Winchester | Q652534 | Federico Chueca |
| Q734642 | Michele Lega (cardinal) | Q3177141 | José de Salamanca |
| Q187923 | Ginny Weasley | Q186851 | Catholic Monarchs |
| Q454tried | Invalid QID format | Q71992 | Jenaro Pérez Villaamil |
| Q332 | Neptune (planet) | Q3954 | Neptune (god) |
| Q5765 | Balearic Islands | Q5836/Q52631 | Toledo/Ibiza |
| Q8717 | Seville (misused for airport) | Q166276 | Madrid-Barajas Airport |

### Total corrections by file

| File | QIDs corrected |
|------|---------------|
| madrid_metro_stations.csv | ~95 |
| madrid_cercanias_stations.csv | ~10 |
| madrid_metro_ligero_stations.csv | ~15 |
| madrid_districts.csv | ~7 |
| madrid_neighbourhoods.csv | ~11 |
| madrid_plazas_parks.csv | ~5 |
| madrid_streets.csv | ~8 |
| **Total** | **~151** |

### QIDs that were already correct (survived audit)

Q29 (Spain), Q297 (Velázquez), Q332 was planet not god -- FIXED, Q5432 (Goya), Q5682 (Cervantes), Q7322 (Columbus), Q739 (Colombia), Q414 (Argentina), Q928 (Philippines), Q8692 (Bilbao), Q36433 (Porto), Q597 (Lisbon), Q676555 (St Francis), Q82674 (Mary I), Q16508 (Jarama), Q16510 (Henares), Q2058663 (Peñagrande), Q2054035 (El Capricho), Q243122 (Ferdinand III), Q113773643 (Margarita Lacoma), Q1142 (Alsace), Q8717 (Seville -- correct for Sevilla station).

## Other fixes applied during audit

### Cross-file inconsistencies
- **Aluche**: harmonized etymology_type and named_after between metro and cercanías
- **Casa del Reloj** (metro_240): named_after wrongly referenced "Arganzuela" instead of "Leganés"
- **Laguna cercanías**: wrongly referenced "Parla" instead of "Latina district"

### Source copy-paste errors
- **Barrio del Pilar** (metro_126): Wikipedia URL linked to Herrera Oria
- **Ventilla** (metro_127): same error

### Wikipedia-only sources eliminated
- 22 entries previously citing only "Wikipedia" now have specific URLs and/or secondary sources
- Current count of Wikipedia-only entries: **0**

## Verification of final state

Final API verification shows:
- **163 OK** (verified match between QID and named_after)
- **12 accent-only mismatches** (e.g., Alcorcón/Alcorcon, Leganés/Leganes) -- all correct
- **0 missing** QIDs on Wikidata
- **0 true mismatches**

## Recommendation

Any future QID additions MUST be verified against the Wikidata API before insertion. Use:
```
https://www.wikidata.org/w/api.php?action=wbgetentities&ids=QXXXXX&props=labels&languages=en|es&format=json
```
