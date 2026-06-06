#!/usr/bin/env python3
"""Build static site data from CSV files."""
import csv
import html
import json
import os
import re
import shutil
import unicodedata
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = Path(ROOT)
SITE_BASE_URL = 'https://lbm364dl.github.io/toponyms-origins/'
SITE_NAME_ES = 'Origen de nombres de estaciones de Madrid'
SITE_NAME_EN = 'Madrid Station Name Origins'
SITE_DESCRIPTION_ES = (
    'Atlas de los orígenes de nombres de estaciones de Madrid: Metro, Cercanías, '
    'Metro Ligero y Tranvía de Parla, con mapa, fuentes y nivel de confianza.'
)
STATION_CATEGORIES = {'metro', 'cercanias', 'metro_ligero'}
STATION_CATEGORY_LABELS_ES = {
    'metro': 'Metro de Madrid',
    'cercanias': 'Cercanías Madrid',
    'metro_ligero': 'Metro Ligero y Tranvía',
}
STATION_CATEGORY_SLUGS = {
    'metro': 'metro',
    'cercanias': 'cercanias',
    'metro_ligero': 'metro-ligero',
}
ETYM_TYPE_LABELS_ES = {
    'person': 'Persona',
    'place': 'Lugar',
    'descriptive': 'Descriptivo',
    'historical': 'Histórico',
    'religious': 'Religioso',
    'event': 'Evento',
    'occupation': 'Oficio',
    'mythological': 'Mitológico',
    'unknown': 'Desconocido',
}
CONFIDENCE_LABELS_ES = {
    'verified': 'Verificado',
    'probable': 'Probable',
    'uncertain': 'Incierto',
}
OPERATOR_LABELS_ES = {
    'Renfe Cercanias': 'Renfe Cercanías',
    'Tranvia de Parla': 'Tranvía de Parla',
}

FILES = {
    'metro': 'data/madrid_metro_stations.csv',
    'cercanias': 'data/madrid_cercanias_stations.csv',
    'metro_ligero': 'data/madrid_metro_ligero_stations.csv',
    'districts': 'data/madrid_districts.csv',
    'neighbourhoods': 'data/madrid_neighbourhoods.csv',
    'plazas_parks': 'data/madrid_plazas_parks.csv',
    'streets': 'data/madrid_streets.csv',
}

TRANSLATIONS_FILE = os.path.join(ROOT, 'docs', 'data', 'translations_es.json')
LINE_ORDER_FILE = os.path.join(ROOT, 'docs', 'data', 'line_orders.json')
GMAPS_FILE = os.path.join(ROOT, 'docs', 'data', 'gmaps_place_ids.json')
NAMED_AFTER_ES_FILE = os.path.join(ROOT, 'docs', 'data', 'named_after_es.json')
CONTENT_STATIONS_DIR = ROOT_PATH / 'content' / 'stations'

CONTENT_MARKDOWN_FILES = {
    'summary.short.md': 'content_summary_short',
    'summary.md': 'content_summary',
    'story.md': 'content_story',
    'confidence.md': 'content_confidence_reason',
    'current-claim-assessment.md': 'content_current_claim_assessment',
    'research-note.md': 'content_research_note',
}

INDEX_FIELDS = (
    'id',
    'name',
    '_category',
    'district',
    'neighbourhood',
    'latitude',
    'longitude',
    'etymology_type',
    'confidence',
    'line',
    'operator',
    'named_after',
    'named_after_es',
    'content_summary_short_en',
    'content_summary_short_es',
    'person_profession',
    'page_path',
)

def read_text_if_exists(path):
    if not path.exists():
        return ''
    return path.read_text(encoding='utf-8').strip()

def esc(value):
    return html.escape(str(value or ''), quote=True)

def strip_markdown(value):
    value = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'\1', value or '')
    value = re.sub(r'[*_`#>-]+', ' ', value)
    return re.sub(r'\s+', ' ', value).strip()

def truncate_text(value, limit=155):
    value = re.sub(r'\s+', ' ', strip_markdown(value)).strip()
    if len(value) <= limit:
        return value
    return value[:limit - 1].rsplit(' ', 1)[0].rstrip('.,;:') + '…'

def slugify(value):
    value = unicodedata.normalize('NFKD', value or '')
    value = ''.join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower().replace('ñ', 'n')
    value = re.sub(r'[^a-z0-9]+', '-', value)
    value = re.sub(r'-+', '-', value).strip('-')
    return value or 'estacion'

def absolute_url(path=''):
    return SITE_BASE_URL + str(path or '').lstrip('/')

def station_summary(entry, lang='es'):
    if lang == 'es':
        return (
            entry.get('content_summary_short_es')
            or entry.get('content_summary_es')
            or entry.get('etymology_summary_es')
            or entry.get('content_summary_short_en')
            or entry.get('content_summary_en')
            or entry.get('etymology_summary')
            or ''
        )
    return (
        entry.get('content_summary_short_en')
        or entry.get('content_summary_en')
        or entry.get('etymology_summary')
        or entry.get('content_summary_short_es')
        or entry.get('content_summary_es')
        or entry.get('etymology_summary_es')
        or ''
    )

def station_story(entry):
    return (
        entry.get('content_story_es')
        or entry.get('content_summary_es')
        or entry.get('etymology_summary_es')
        or entry.get('content_story_en')
        or entry.get('content_summary_en')
        or entry.get('etymology_summary')
        or ''
    )

def markdown_to_html(text):
    text = (text or '').replace('\r\n', '\n').strip()
    if not text:
        return ''
    blocks = re.split(r'\n{2,}', text)
    rendered = []
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not lines:
            continue
        heading = re.match(r'^(#{2,4})\s+(.+)$', lines[0])
        if heading and len(lines) == 1:
            level = min(4, len(heading.group(1)) + 1)
            rendered.append(f'<h{level}>{esc(heading.group(2))}</h{level}>')
            continue
        if all(re.match(r'^[-*]\s+', line) for line in lines):
            item_texts = [re.sub(r'^[-*]\s+', '', line) for line in lines]
            items = ''.join(
                f'<li>{esc(item)}</li>'
                for item in item_texts
            )
            rendered.append(f'<ul>{items}</ul>')
            continue
        rendered.append(f'<p>{esc(" ".join(lines))}</p>')
    return '\n'.join(rendered)

def station_description(entry):
    summary = station_summary(entry, 'es')
    if summary:
        return truncate_text(f'{entry.get("name", "")}: {summary}', 160)
    line = entry.get('line')
    line_text = f' en la línea {line}' if line else ''
    return truncate_text(
        f'Por qué la estación {entry.get("name", "")}{line_text} se llama así: origen del nombre, fuentes y nivel de confianza.',
        160,
    )

def station_meta(entry):
    line = entry.get('line')
    pieces = [
        STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), entry.get('_category', '')),
        line and f'Línea {format_lines(line)}',
        entry.get('district'),
        entry.get('municipality'),
    ]
    return ' · '.join(str(piece) for piece in pieces if piece)

def format_lines(value):
    return ', '.join(part.strip() for part in str(value or '').split(';') if part.strip())

def format_operator(value):
    return '; '.join(
        OPERATOR_LABELS_ES.get(part.strip(), part.strip())
        for part in str(value or '').split(';')
        if part.strip()
    )

def assign_station_pages(entries):
    used = set()
    for entry in entries:
        if entry.get('_category') not in STATION_CATEGORIES:
            continue
        id_slug = slugify(entry.get('id'))
        name_slug = slugify(entry.get('name'))
        slug = f'{id_slug}-{name_slug}'
        if slug in used:
            slug = f'{slug}-{STATION_CATEGORY_SLUGS.get(entry.get("_category"), entry.get("_category", ""))}'
        used.add(slug)
        entry['page_path'] = f'stations/{slug}/'

def json_ld(data):
    return json.dumps(data, ensure_ascii=False, separators=(',', ':'))

def station_json_ld(entry):
    url = absolute_url(entry['page_path'])
    place = {
        '@type': 'Place',
        'name': f'Estación de {entry.get("name", "")}',
        'containedInPlace': {'@type': 'City', 'name': 'Madrid'},
    }
    if entry.get('latitude') and entry.get('longitude'):
        place['geo'] = {
            '@type': 'GeoCoordinates',
            'latitude': entry['latitude'],
            'longitude': entry['longitude'],
        }

    return {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'WebPage',
                '@id': url,
                'url': url,
                'name': f'{entry.get("name", "")}: origen del nombre de la estación',
                'description': station_description(entry),
                'inLanguage': 'es',
                'isPartOf': {'@id': absolute_url('#website')},
                'about': {'@id': f'{url}#station'},
            },
            {
                '@type': 'Article',
                '@id': f'{url}#article',
                'headline': f'{entry.get("name", "")}: origen del nombre de la estación',
                'description': station_description(entry),
                'inLanguage': 'es',
                'isAccessibleForFree': True,
                'license': 'https://creativecommons.org/licenses/by-sa/4.0/',
                'mainEntityOfPage': {'@id': url},
                'about': {'@id': f'{url}#station'},
            },
            {
                **place,
                '@id': f'{url}#station',
            },
        ],
    }

def source_items_html(entry):
    sources = entry.get('sources_structured')
    if isinstance(sources, list) and sources:
        items = []
        for source in sources:
            title = source.get('title') or source.get('url') or 'Fuente'
            relevance = source.get('relevance_es') or source.get('relevance_en') or ''
            url = source.get('url')
            title_html = (
                f'<a class="source-link source-title" href="{esc(url)}">{esc(title)}</a>'
                if url else f'<span class="source-title">{esc(title)}</span>'
            )
            type_html = f'<span class="source-type">{esc(source.get("type"))}</span>' if source.get('type') else ''
            relevance_html = f'<div class="source-relevance">{esc(relevance)}</div>' if relevance else ''
            items.append(f'<div class="source-item">{title_html}{type_html}{relevance_html}</div>')
        return '\n'.join(items)

    raw = entry.get('source') or ''
    items = []
    for source in raw.split(';'):
        source = source.strip()
        if source:
            items.append(f'<div class="source-item"><span class="source-title">{esc(source)}</span></div>')
    return '\n'.join(items) or '<em>Sin fuentes registradas.</em>'

def station_page_html(entry):
    url = absolute_url(entry['page_path'])
    description = station_description(entry)
    story_html = markdown_to_html(station_story(entry))
    named_after = entry.get('named_after_es') or entry.get('named_after') or ''
    title = f'{entry.get("name", "")}: origen del nombre de la estación | Madrid'
    badges = ''.join(
        f'<span class="badge">{esc(value)}</span>'
        for value in (
            ETYM_TYPE_LABELS_ES.get(entry.get('etymology_type'), entry.get('etymology_type')),
            CONFIDENCE_LABELS_ES.get(entry.get('confidence'), entry.get('confidence')),
            entry.get('line') and f'Línea {format_lines(entry.get("line"))}',
        )
        if value
    )
    details = ''.join(
        f'<div class="detail-label">{label}</div><div class="detail-value">{esc(value)}</div>'
        for label, value in (
            ('Origen del nombre', named_after),
            ('Distrito', entry.get('district')),
            ('Barrio', entry.get('neighbourhood')),
            ('Municipio', entry.get('municipality')),
            ('Operador', format_operator(entry.get('operator'))),
            ('Inauguración', entry.get('opening_year')),
        )
        if value
    )
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{esc(SITE_NAME_ES)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(absolute_url('og-image.png'))}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(absolute_url('og-image.png'))}">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css">
<script type="application/ld+json">{json_ld(station_json_ld(entry))}</script>
</head>
<body class="station-page">
<header>
  <div class="container station-hero">
    <a class="back-link" href="../../">Todas las estaciones</a>
    <div class="hero-left">
      <span class="hero-eyebrow">{esc(station_meta(entry))}</span>
      <h1>{esc(entry.get('name', ''))}</h1>
      <p class="subtitle">Origen del nombre de la estación.</p>
    </div>
  </div>
</header>
<main class="container station-main">
  <article class="station-article">
    <div class="entry-badges">{badges}</div>
    <section class="etymology-summary markdown-content">
      {story_html or f'<p>{esc(description)}</p>'}
    </section>
    {f'<div class="detail-grid">{details}</div>' if details else ''}
    <section class="sources">
      <h2>Fuentes</h2>
      {source_items_html(entry)}
    </section>
  </article>
</main>
<footer>
  <div class="container footer-inner">
    <div>
      <strong>{esc(SITE_NAME_ES)}</strong><br>
      <span class="footer-note">Orígenes de nombres de estaciones · CC-BY-SA 4.0</span>
    </div>
    <div class="footer-links"><a href="../../">Inicio</a><a href="https://creativecommons.org/licenses/by-sa/4.0/">Licencia</a></div>
  </div>
</footer>
</body>
</html>
'''

def build_station_pages(entries, out_root):
    station_root = Path(out_root) / 'stations'
    if station_root.exists():
        shutil.rmtree(station_root)
    station_root.mkdir(parents=True, exist_ok=True)
    count = 0
    for entry in entries:
        if entry.get('_category') not in STATION_CATEGORIES:
            continue
        page_dir = Path(out_root) / entry['page_path']
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / 'index.html').write_text(station_page_html(entry), encoding='utf-8')
        count += 1
    return count

def build_sitemap(entries, out_root):
    today = date.today().isoformat()
    urls = [
        (absolute_url(), today, '1.0'),
    ]
    urls.extend(
        (absolute_url(entry['page_path']), today, '0.8')
        for entry in entries
        if entry.get('_category') in STATION_CATEGORIES and entry.get('page_path')
    )
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, priority in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{xml_escape(loc)}</loc>')
        xml.append(f'    <lastmod>{lastmod}</lastmod>')
        xml.append(f'    <priority>{priority}</priority>')
        xml.append('  </url>')
    xml.append('</urlset>')
    Path(out_root, 'sitemap.xml').write_text('\n'.join(xml) + '\n', encoding='utf-8')
    Path(out_root, 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\n\nSitemap: {absolute_url("sitemap.xml")}\n',
        encoding='utf-8',
    )

def load_station_content():
    content = {}
    if not CONTENT_STATIONS_DIR.exists():
        return content

    for station_dir in sorted(CONTENT_STATIONS_DIR.iterdir()):
        if not station_dir.is_dir():
            continue
        meta_path = station_dir / 'metadata.json'
        if not meta_path.exists():
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            continue

        station_id = meta.get('id') or station_dir.name
        entry_content = {
            'has_content_entry': 'true',
            'content_metadata_path': str(meta_path.relative_to(ROOT_PATH)),
            'content_status': meta.get('status', ''),
            'content_confidence': meta.get('confidence', ''),
            'sources_structured': meta.get('sources', []),
            'corrections': meta.get('corrections', []),
            'open_questions': meta.get('open_questions', []),
        }

        field_map = {
            'recommended_etymology_type': 'etymology_type',
            'recommended_named_after': 'named_after',
            'previous_names': 'previous_names',
            'naming_date': 'naming_date',
            'confidence': 'confidence',
        }
        for src, dest in field_map.items():
            value = meta.get(src)
            if isinstance(value, str) and value.strip():
                entry_content[dest] = value.strip()

        for lang in ('en', 'es'):
            lang_dir = station_dir / lang
            for filename, field_base in CONTENT_MARKDOWN_FILES.items():
                value = read_text_if_exists(lang_dir / filename)
                if value:
                    entry_content[f'{field_base}_{lang}'] = value

        content[station_id] = entry_content

    return content

def build():
    all_entries = []
    station_content = load_station_content()
    for key, relpath in FILES.items():
        path = os.path.join(ROOT, relpath)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                entry = {}
                for k, v in row.items():
                    if v is None:
                        continue
                    if isinstance(v, list):
                        v = ','.join(v)
                    v = v.strip()
                    if v:
                        entry[k] = v
                entry['_category'] = key
                content_entry = station_content.get(entry.get('id', ''))
                if content_entry:
                    entry.update(content_entry)
                all_entries.append(entry)

    # Merge Google Maps Place IDs if available
    if os.path.exists(GMAPS_FILE):
        with open(GMAPS_FILE, 'r', encoding='utf-8') as f:
            gmaps = json.load(f)
        for entry in all_entries:
            gdata = gmaps.get(entry.get('id', ''))
            if gdata and 'gmaps_url' in gdata:
                entry['gmaps_url'] = gdata['gmaps_url']
        print(f"  Merged {sum(1 for e in all_entries if 'gmaps_url' in e)} Google Maps Place URLs")

    # Merge named_after Spanish translations
    if os.path.exists(NAMED_AFTER_ES_FILE):
        with open(NAMED_AFTER_ES_FILE, 'r', encoding='utf-8') as f:
            na_es = json.load(f)
        for entry in all_entries:
            es_text = na_es.get(entry.get('id', ''))
            if es_text:
                entry['named_after_es'] = es_text
        print(f"  Merged {sum(1 for e in all_entries if 'named_after_es' in e)} named_after ES translations")

    # Merge Spanish translations if available
    if os.path.exists(TRANSLATIONS_FILE):
        with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
            translations = json.load(f)
        for entry in all_entries:
            es_text = translations.get(entry.get('id', ''))
            if es_text:
                entry['etymology_summary_es'] = es_text
        print(f"  Merged {sum(1 for e in all_entries if 'etymology_summary_es' in e)} Spanish translations")

    assign_station_pages(all_entries)

    out_dir = os.path.join(ROOT, 'docs', 'data')
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, 'entries.json'), 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False)

    with open(os.path.join(out_dir, 'entries.js'), 'w', encoding='utf-8') as f:
        f.write('const ENTRIES_DATA = ')
        json.dump(all_entries, f, ensure_ascii=False)
        f.write(';')

    index_entries = [
        {key: entry[key] for key in INDEX_FIELDS if key in entry}
        for entry in all_entries
    ]

    with open(os.path.join(out_dir, 'entries_index.json'), 'w', encoding='utf-8') as f:
        json.dump(index_entries, f, ensure_ascii=False)

    with open(os.path.join(out_dir, 'entries_index.js'), 'w', encoding='utf-8') as f:
        f.write('const ENTRIES_INDEX_DATA = ')
        json.dump(index_entries, f, ensure_ascii=False)
        f.write(';')

    pages_built = build_station_pages(all_entries, os.path.join(ROOT, 'docs'))
    build_sitemap(all_entries, os.path.join(ROOT, 'docs'))

    print(f"Built {len(all_entries)} entries -> docs/data/entries.json + entries.js")
    print(f"Built lightweight index -> docs/data/entries_index.json + entries_index.js")
    print(f"Built {pages_built} station pages -> docs/stations/")
    print("Built SEO files -> docs/sitemap.xml + docs/robots.txt")
    if station_content:
        merged = sum(1 for e in all_entries if e.get('has_content_entry') == 'true')
        print(f"  Merged {merged} station content entries from content/stations")

if __name__ == '__main__':
    build()
