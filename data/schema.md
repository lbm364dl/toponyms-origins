# Dataset Schema

All CSV files use UTF-8 encoding, comma separator, and double-quote escaping.

## Common Fields (all entity types)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier: `{type}_{sequential}` (e.g., `district_01`, `metro_042`) |
| `name` | string | yes | Official current name |
| `type` | enum | yes | `street` / `metro_station` / `cercanias_station` / `metro_ligero_station` / `district` / `neighbourhood` / `plaza` / `park` / `monument` |
| `subtype` | string | no | Further classification (e.g., `calle`, `avenida`, `paseo`, `glorieta` for streets; line number for stations) |
| `district` | string | no | Distrito name |
| `neighbourhood` | string | no | Barrio name |
| `latitude` | float | no | WGS84 |
| `longitude` | float | no | WGS84 |
| `etymology_type` | enum | no | `person` / `event` / `place` / `descriptive` / `historical` / `occupation` / `religious` / `mythological` / `literary` / `unknown` |
| `etymology_summary` | string | no | 1-3 sentence explanation of name origin |
| `named_after` | string | no | Who/what (human-readable) |
| `named_after_wikidata` | string | no | Wikidata Q-identifier |
| `person_gender` | enum | no | `M` / `F` / `NB` (if etymology_type=person) |
| `person_birth_year` | int | no | (if person) |
| `person_death_year` | int | no | (if person) |
| `person_profession` | string | no | (if person) |
| `person_nationality` | string | no | (if person) |
| `naming_date` | string | no | Year or date when current name was given |
| `previous_names` | string | no | Semicolon-separated former names |
| `source` | string | no | Citation for etymology information |
| `confidence` | enum | no | `verified` / `probable` / `uncertain` / `unknown` |

## Etymology Type Definitions

- **person**: Named after a specific individual (historical, literary, mythological)
- **event**: Named after a historical event (battle, treaty, revolution)
- **place**: Named after another geographic location (city, country, region)
- **descriptive**: Describes a physical characteristic (terrain, vegetation, water)
- **historical**: Refers to historical usage or feature that no longer exists (convents, gates, trades)
- **occupation**: Named after a trade or profession practiced in the area
- **religious**: Named after a saint, religious figure, or religious institution
- **mythological**: Named after mythological figures
- **literary**: Named after literary works or characters
- **unknown**: Origin not yet determined

## Station-Specific Fields

| Field | Type | Description |
|-------|------|-------------|
| `line` | string | Line number(s), semicolon-separated |
| `opening_year` | int | Year the station opened |
| `operator` | string | Metro de Madrid / CRTM / Renfe Cercanias |

## Confidence Levels

- **verified**: Etymology confirmed by multiple authoritative sources (academic works, official records)
- **probable**: Etymology supported by one reliable source or widely accepted tradition
- **uncertain**: Multiple competing theories exist; most likely one noted
- **unknown**: No etymology information found yet
