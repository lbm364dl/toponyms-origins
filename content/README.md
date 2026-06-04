# Content

Canonical public research content for the site.

## Stations

Station research lives in `content/stations/<station_id>/`.

Each completed station has:

```text
metadata.json
en/
  summary.short.md
  summary.md
  story.md
  confidence.md
  current-claim-assessment.md
  research-note.md
es/
  summary.short.md
  summary.md
  story.md
  confidence.md
  current-claim-assessment.md
  research-note.md
```

`scripts/run_station_research.py` writes this folder by default and skips
stations that already have `metadata.json` unless `--force` is used.
