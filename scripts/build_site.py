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
from urllib.parse import urlparse
from xml.sax.saxutils import escape as xml_escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = Path(ROOT)
SITE_BASE_URL = os.environ.get('SITE_BASE_URL', 'https://nombresdemadrid.es/').strip()
if not SITE_BASE_URL.endswith('/'):
    SITE_BASE_URL += '/'
SITE_NAME_ES = 'Nombres de Madrid'
SITE_NAME_EN = 'Madrid Station Name Origins'
SITE_DESCRIPTION_ES = (
    'Descubre por qué se llaman así las estaciones de Madrid: Metro, Cercanías, '
    'Metro Ligero y Tranvía, con fuentes y nivel de confianza.'
)
SITE_OWNER_NAME = os.environ.get('SITE_OWNER_NAME', 'lbm364dl').strip()
SITE_REPOSITORY_URL = 'https://github.com/lbm364dl/toponyms-origins'
SITE_OG_IMAGE = 'og-image.png'
SITE_PATH_PREFIX = urlparse(SITE_BASE_URL).path.rstrip('/')
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

def site_path(path=''):
    """Return a root-relative URL that also works under a temporary path prefix."""
    clean_path = str(path or '').lstrip('/')
    prefix = f'{SITE_PATH_PREFIX}/' if SITE_PATH_PREFIX else '/'
    return prefix + clean_path

def relative_root(depth):
    return '../' * depth

def network_path(entry):
    slug = STATION_CATEGORY_SLUGS.get(entry.get('_category'), slugify(entry.get('_category')))
    return f'redes/{slug}/'

def line_path(line):
    return f'lineas/linea-{slugify(line)}/'

def district_path(district):
    return f'distritos/{slugify(district)}/'

def type_path(etymology_type):
    plural_slugs = {
        'person': 'personas',
        'place': 'lugares',
        'descriptive': 'descriptivos',
        'historical': 'historicos',
        'religious': 'religiosos',
        'event': 'eventos',
        'occupation': 'oficios',
        'mythological': 'mitologicos',
        'unknown': 'desconocidos',
    }
    return f'origenes/{plural_slugs.get(etymology_type, slugify(etymology_type))}/'

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
    name_counts = {}
    for entry in entries:
        if entry.get('_category') in STATION_CATEGORIES:
            normalized_name = (entry.get('name') or '').casefold()
            name_counts[normalized_name] = name_counts.get(normalized_name, 0) + 1

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
        if name_counts.get((entry.get('name') or '').casefold(), 0) > 1:
            entry['_title_disambiguator'] = STATION_CATEGORY_LABELS_ES.get(
                entry.get('_category'), entry.get('_category', '')
            )

def station_title(entry):
    name = entry.get('name', '')
    disambiguator = entry.get('_title_disambiguator')
    display_name = f'{name} ({disambiguator})' if disambiguator else name
    candidates = (
        f'¿Por qué se llama {display_name}? | {SITE_NAME_ES}',
        f'{display_name}: origen del nombre | {SITE_NAME_ES}',
        f'{display_name}: origen del nombre',
    )
    return next((candidate for candidate in candidates if len(candidate) <= 65), candidates[-1])

def station_heading(entry):
    name = entry.get('name', '')
    disambiguator = entry.get('_title_disambiguator')
    display_name = f'{name} ({disambiguator})' if disambiguator else name
    return f'¿Por qué se llama {display_name}?'

def entry_lines(entry):
    return [part.strip() for part in str(entry.get('line') or '').split(';') if part.strip()]

def related_stations(entry, entries, limit=6):
    current_lines = set(entry_lines(entry))
    scored = []
    for other in entries:
        if other is entry or other.get('_category') not in STATION_CATEGORIES:
            continue
        shared_lines = current_lines.intersection(entry_lines(other))
        score = len(shared_lines) * 10
        if entry.get('district') and entry.get('district') == other.get('district'):
            score += 4
        if entry.get('municipality') and entry.get('municipality') == other.get('municipality'):
            score += 3
        if entry.get('_category') == other.get('_category'):
            score += 1
        if score:
            scored.append((-score, (other.get('name') or '').casefold(), other))
    scored.sort(key=lambda item: (item[0], item[1], item[2].get('id', '')))
    return [item[2] for item in scored[:limit]]

def json_ld(data):
    return json.dumps(data, ensure_ascii=False, separators=(',', ':'))

def organization_json_ld():
    return {
        '@type': 'Organization',
        '@id': absolute_url('#organization'),
        'name': SITE_NAME_ES,
        'url': absolute_url(),
        'logo': {
            '@type': 'ImageObject',
            'url': absolute_url('icon-512.png'),
            'width': 512,
            'height': 512,
        },
        'sameAs': SITE_REPOSITORY_URL,
    }

def station_json_ld(entry):
    url = absolute_url(entry['page_path'])
    title = station_title(entry)
    headline = station_heading(entry).rstrip('?')
    network_label = STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), 'Estaciones')
    contained_name = entry.get('municipality') or 'Madrid'
    place = {
        '@type': 'Place',
        'name': f'Estación de {entry.get("name", "")}',
        'containedInPlace': {'@type': 'AdministrativeArea', 'name': contained_name},
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
                'name': title,
                'description': station_description(entry),
                'inLanguage': 'es',
                'isPartOf': {'@id': absolute_url('#website')},
                'about': {'@id': f'{url}#station'},
                'breadcrumb': {'@id': f'{url}#breadcrumb'},
            },
            {
                '@type': 'Article',
                '@id': f'{url}#article',
                'headline': headline,
                'description': station_description(entry),
                'inLanguage': 'es',
                'isAccessibleForFree': True,
                'license': 'https://creativecommons.org/licenses/by-sa/4.0/',
                'mainEntityOfPage': {'@id': url},
                'about': {'@id': f'{url}#station'},
                'author': {'@id': absolute_url('#organization')},
                'publisher': {'@id': absolute_url('#organization')},
                'keywords': [
                    'toponimia de Madrid',
                    'origen de nombres',
                    entry.get('name', ''),
                    network_label,
                ],
            },
            {
                **place,
                '@id': f'{url}#station',
            },
            {
                '@type': 'BreadcrumbList',
                '@id': f'{url}#breadcrumb',
                'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': SITE_NAME_ES, 'item': absolute_url()},
                    {'@type': 'ListItem', 'position': 2, 'name': 'Estaciones', 'item': absolute_url('estaciones/')},
                    {'@type': 'ListItem', 'position': 3, 'name': network_label, 'item': absolute_url(network_path(entry))},
                    {'@type': 'ListItem', 'position': 4, 'name': entry.get('name', ''), 'item': url},
                ],
            },
            organization_json_ld(),
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

def primary_nav_html(root):
    return f'''<nav class="site-nav" aria-label="Navegación principal">
      <a href="{root}">Inicio</a>
      <a href="{root}estaciones/">Estaciones</a>
      <a href="{root}redes/metro/">Metro</a>
      <a href="{root}redes/cercanias/">Cercanías</a>
      <a href="{root}metodologia/">Metodología</a>
      <a href="{root}sobre-el-proyecto/">Sobre el proyecto</a>
    </nav>'''

def footer_html(root):
    return f'''<footer>
  <div class="container footer-inner">
    <div>
      <strong>{esc(SITE_NAME_ES)}</strong><br>
      <span class="footer-note">Toponimia madrileña documentada · CC-BY-SA 4.0</span>
    </div>
    <nav class="footer-links" aria-label="Información legal">
      <a href="{root}metodologia/">Metodología</a>
      <a href="{root}sobre-el-proyecto/">Quiénes somos</a>
      <a href="{root}privacidad/">Privacidad</a>
      <a href="{root}cookies/">Cookies</a>
      <a href="https://creativecommons.org/licenses/by-sa/4.0/">Licencia</a>
      <a href="{SITE_REPOSITORY_URL}">Código y datos</a>
    </nav>
  </div>
</footer>'''

def related_stations_html(entry, entries, root):
    related = related_stations(entry, entries)
    if not related:
        return ''
    items = []
    for other in related:
        summary = truncate_text(station_summary(other, 'es'), 120)
        items.append(
            f'<li><a href="{root}{esc(other["page_path"])}">'
            f'<strong>{esc(other.get("name"))}</strong>'
            f'{f"<span>{esc(summary)}</span>" if summary else ""}</a></li>'
        )
    return f'''<section class="related-stations" aria-labelledby="related-heading">
      <h2 id="related-heading">Sigue explorando nombres relacionados</h2>
      <ul>{''.join(items)}</ul>
    </section>'''

def station_page_html(entry, entries):
    root = '../../'
    url = absolute_url(entry['page_path'])
    description = station_description(entry)
    story_html = markdown_to_html(station_story(entry))
    named_after = entry.get('named_after_es') or entry.get('named_after') or ''
    title = station_title(entry)
    type_label = ETYM_TYPE_LABELS_ES.get(entry.get('etymology_type'), entry.get('etymology_type'))
    badges = []
    if type_label:
        badges.append(f'<a class="badge" href="{root}{type_path(entry.get("etymology_type"))}">{esc(type_label)}</a>')
    confidence_label = CONFIDENCE_LABELS_ES.get(entry.get('confidence'), entry.get('confidence'))
    if confidence_label:
        badges.append(f'<span class="badge">{esc(confidence_label)}</span>')
    for line in entry_lines(entry):
        badges.append(f'<a class="badge" href="{root}{line_path(line)}">Línea {esc(line)}</a>')
    badges = ''.join(badges)
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
<link rel="alternate" hreflang="es" href="{esc(url)}">
<link rel="alternate" hreflang="x-default" href="{esc(url)}">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{esc(SITE_NAME_ES)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<meta property="og:image:alt" content="Mapa tipográfico de nombres de estaciones de Madrid">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">{json_ld(station_json_ld(entry))}</script>
</head>
<body class="station-page">
<header>
  <div class="container station-hero">
    {primary_nav_html(root)}
    <nav class="breadcrumbs" aria-label="Migas de pan">
      <a href="{root}">Inicio</a><span aria-hidden="true">/</span>
      <a href="{root}estaciones/">Estaciones</a><span aria-hidden="true">/</span>
      <a href="{root}{network_path(entry)}">{esc(STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), 'Red'))}</a><span aria-hidden="true">/</span>
      <span aria-current="page">{esc(entry.get('name'))}</span>
    </nav>
    <div class="hero-left">
      <span class="hero-eyebrow">{esc(station_meta(entry))}</span>
      <h1>{esc(station_heading(entry))}</h1>
      <p class="subtitle">Historia y origen documentado del nombre de la estación de {esc(entry.get('name', ''))}.</p>
    </div>
  </div>
</header>
<main class="container station-main">
  <article class="station-article">
    <div class="entry-badges">{badges}</div>
    <p class="editorial-note">Investigación de <a href="{root}sobre-el-proyecto/">{esc(SITE_NAME_ES)}</a> · <a href="{root}metodologia/">Cómo verificamos cada origen</a></p>
    <section class="etymology-summary markdown-content" aria-label="Origen del nombre">
      {story_html or f'<p>{esc(description)}</p>'}
    </section>
    {f'<div class="detail-grid">{details}</div>' if details else ''}
    <section class="sources">
      <h2>Fuentes</h2>
      {source_items_html(entry)}
    </section>
    {related_stations_html(entry, entries, root)}
  </article>
</main>
{footer_html(root)}
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
        (page_dir / 'index.html').write_text(station_page_html(entry, entries), encoding='utf-8')
        count += 1
    return count

def collection_json_ld(title, description, path, entries=None, page_type='CollectionPage'):
    url = absolute_url(path)
    graph = [
        {
            '@type': page_type,
            '@id': url,
            'url': url,
            'name': title,
            'description': description,
            'inLanguage': 'es',
            'isPartOf': {'@id': absolute_url('#website')},
            'publisher': {'@id': absolute_url('#organization')},
        }
    ]
    if entries:
        graph.append({
            '@type': 'ItemList',
            '@id': f'{url}#list',
            'numberOfItems': len(entries),
            'itemListElement': [
                {
                    '@type': 'ListItem',
                    'position': index,
                    'name': entry.get('name', ''),
                    'url': absolute_url(entry.get('page_path', '')),
                }
                for index, entry in enumerate(entries, 1)
            ],
        })
    graph.append(organization_json_ld())
    return {'@context': 'https://schema.org', '@graph': graph}

def directory_entries_html(entries, root):
    items = []
    for entry in sorted(entries, key=lambda item: ((item.get('name') or '').casefold(), item.get('id', ''))):
        meta = station_meta(entry)
        summary = truncate_text(station_summary(entry, 'es'), 135)
        items.append(f'''<li>
          <a href="{root}{esc(entry['page_path'])}">
            <strong>{esc(entry.get('name'))}</strong>
            <span class="directory-meta">{esc(meta)}</span>
            {f'<span class="directory-summary">{esc(summary)}</span>' if summary else ''}
          </a>
        </li>''')
    return f'<ul class="station-directory">{"".join(items)}</ul>'

def link_directory_html(items, root):
    links = ''.join(
        f'<li><a href="{root}{esc(path)}"><strong>{esc(name)}</strong><span>{esc(description)}</span></a></li>'
        for name, path, description in items
    )
    return f'<ul class="hub-directory">{links}</ul>'

def content_page_html(
    title,
    description,
    path,
    body_html,
    depth=1,
    entries=None,
    robots='index, follow',
    page_type='CollectionPage',
):
    root = relative_root(depth)
    url = absolute_url(path)
    page_title = f'{title} | {SITE_NAME_ES}'
    if len(page_title) > 65 and title.startswith('Nombres de '):
        compact_title = title[len('Nombres de '):]
        compact_title = compact_title[:1].upper() + compact_title[1:]
        page_title = f'{compact_title} | {SITE_NAME_ES}'
    schema = collection_json_ld(title, description, path, entries, page_type)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(page_title)}</title>
<meta name="description" content="{esc(truncate_text(description, 160))}">
<meta name="robots" content="{esc(robots)}">
<link rel="canonical" href="{esc(url)}">
<link rel="alternate" hreflang="es" href="{esc(url)}">
<link rel="alternate" hreflang="x-default" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{esc(SITE_NAME_ES)}">
<meta property="og:title" content="{esc(page_title)}">
<meta property="og:description" content="{esc(truncate_text(description, 160))}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<meta property="og:image:alt" content="Mapa tipográfico de nombres de estaciones de Madrid">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(page_title)}">
<meta name="twitter:description" content="{esc(truncate_text(description, 160))}">
<meta name="twitter:image" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">{json_ld(schema)}</script>
</head>
<body class="content-page">
<header>
  <div class="container content-hero">
    {primary_nav_html(root)}
    <nav class="breadcrumbs" aria-label="Migas de pan"><a href="{root}">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">{esc(title)}</span></nav>
    <span class="hero-eyebrow">Toponimia madrileña</span>
    <h1>{esc(title)}</h1>
    <p class="subtitle">{esc(description)}</p>
  </div>
</header>
<main class="container content-main">
  {body_html}
</main>
{footer_html(root)}
</body>
</html>
'''

def write_page(out_root, path, html_text):
    page_dir = Path(out_root) / path
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / 'index.html').write_text(html_text, encoding='utf-8')

def build_directory_pages(entries, out_root):
    stations = [entry for entry in entries if entry.get('_category') in STATION_CATEGORIES]
    generated = []

    networks = {}
    lines = {}
    districts = {}
    types = {}
    for entry in stations:
        networks.setdefault(entry.get('_category'), []).append(entry)
        for line in entry_lines(entry):
            lines.setdefault(line, []).append(entry)
        if entry.get('district'):
            districts.setdefault(entry['district'], []).append(entry)
        if entry.get('etymology_type'):
            types.setdefault(entry['etymology_type'], []).append(entry)

    description = (
        f'Índice alfabético de {len(stations)} estaciones de Metro, Cercanías, Metro Ligero y Tranvía '
        'con el origen de cada nombre, fuentes y nivel de confianza.'
    )
    body = f'''<section class="page-section">
      <h2>Todos los nombres, de la A a la Z</h2>
      <p>Entra en cualquier estación para consultar de dónde procede su nombre, qué parte de la explicación está documentada y qué fuentes la respaldan.</p>
      {directory_entries_html(stations, '../')}
    </section>'''
    write_page(out_root, 'estaciones/', content_page_html('Todas las estaciones', description, 'estaciones/', body, 1, stations))
    generated.append('estaciones/')

    network_links = []
    for category, network_entries in sorted(networks.items(), key=lambda item: STATION_CATEGORY_LABELS_ES.get(item[0], item[0])):
        label = STATION_CATEGORY_LABELS_ES.get(category, category)
        path = f'redes/{STATION_CATEGORY_SLUGS.get(category, slugify(category))}/'
        network_description = f'Origen de los nombres de {len(network_entries)} estaciones de {label}, con investigación y fuentes consultables.'
        body = f'''<section class="page-section"><h2>Estaciones de {esc(label)}</h2><p>{esc(network_description)}</p>{directory_entries_html(network_entries, '../../')}</section>'''
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de {label}', network_description, path, body, 2, network_entries))
        generated.append(path)
        network_links.append((label, path, f'{len(network_entries)} estaciones documentadas'))
    path = 'redes/'
    body = f'<section class="page-section"><h2>Explora por red</h2>{link_directory_html(network_links, "../")}</section>'
    write_page(out_root, path, content_page_html('Redes de transporte', 'Consulta los nombres de estaciones por red de transporte de Madrid.', path, body, 1))
    generated.append(path)

    line_links = []
    for line, line_entries in sorted(lines.items(), key=lambda item: natural_sort_key(item[0])):
        path = line_path(line)
        label = f'Línea {line}'
        line_description = f'Por qué se llaman así las {len(line_entries)} estaciones de la {label} en Madrid, con fuentes y nivel de confianza.'
        body = f'''<section class="page-section"><h2>Origen de los nombres de la {esc(label)}</h2><p>{esc(line_description)}</p>{directory_entries_html(line_entries, '../../')}</section>'''
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de la {label}', line_description, path, body, 2, line_entries))
        generated.append(path)
        line_links.append((label, path, f'{len(line_entries)} estaciones'))
    path = 'lineas/'
    body = f'<section class="page-section"><h2>Explora por línea</h2>{link_directory_html(line_links, "../")}</section>'
    write_page(out_root, path, content_page_html('Líneas de Metro y Cercanías', 'Índice de líneas para explorar el origen de los nombres de sus estaciones.', path, body, 1))
    generated.append(path)

    district_links = []
    for district, district_entries in sorted(districts.items(), key=lambda item: item[0].casefold()):
        path = district_path(district)
        district_description = f'Origen de los nombres de {len(district_entries)} estaciones situadas en el distrito de {district}, Madrid.'
        body = f'''<section class="page-section"><h2>Estaciones de {esc(district)}</h2><p>{esc(district_description)}</p>{directory_entries_html(district_entries, '../../')}</section>'''
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de {district}', district_description, path, body, 2, district_entries))
        generated.append(path)
        district_links.append((district, path, f'{len(district_entries)} estaciones'))
    path = 'distritos/'
    body = f'<section class="page-section"><h2>Explora por distrito</h2>{link_directory_html(district_links, "../")}</section>'
    write_page(out_root, path, content_page_html('Distritos de Madrid', 'Explora los orígenes de nombres de estaciones por distrito madrileño.', path, body, 1))
    generated.append(path)

    type_links = []
    for etymology_type, type_entries in sorted(types.items(), key=lambda item: ETYM_TYPE_LABELS_ES.get(item[0], item[0])):
        label = ETYM_TYPE_LABELS_ES.get(etymology_type, etymology_type)
        path = type_path(etymology_type)
        type_description = f'Estaciones de Madrid cuyo nombre tiene un origen de tipo {label.lower()}: {len(type_entries)} casos documentados.'
        body = f'''<section class="page-section"><h2>Origen {esc(label.lower())}</h2><p>{esc(type_description)}</p>{directory_entries_html(type_entries, '../../')}</section>'''
        write_page(out_root, path, content_page_html(f'Nombres de origen {label.lower()}', type_description, path, body, 2, type_entries))
        generated.append(path)
        type_links.append((label, path, f'{len(type_entries)} estaciones'))
    path = 'origenes/'
    body = f'<section class="page-section"><h2>Explora por tipo de origen</h2>{link_directory_html(type_links, "../")}</section>'
    write_page(out_root, path, content_page_html('Tipos de origen', 'Personas, lugares, hechos históricos, descripciones y otros orígenes de nombres de estaciones.', path, body, 1))
    generated.append(path)

    return generated

def natural_sort_key(value):
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r'(\d+)', str(value))]

def build_trust_pages(out_root, station_count):
    pages = {
        'sobre-el-proyecto/': (
            'Sobre Nombres de Madrid',
            'Un proyecto independiente y abierto que documenta por qué los lugares y estaciones de Madrid se llaman así.',
            f'''<article class="prose">
              <h2>Un atlas abierto de los nombres de Madrid</h2>
              <p>Nombres de Madrid es un proyecto independiente de investigación y divulgación sobre toponimia madrileña. Su primera colección reúne {station_count} estaciones de Metro, Cercanías, Metro Ligero y Tranvía de Parla.</p>
              <p>El objetivo no es repetir una leyenda sin más, sino reconstruir la cadena completa: de la estación al lugar que le dio nombre y, desde allí, al origen histórico, lingüístico o biográfico del topónimo.</p>
              <h2>Quién mantiene el proyecto</h2>
              <p>El proyecto está mantenido por <a href="https://github.com/lbm364dl">{esc(SITE_OWNER_NAME)}</a>. Los datos, el historial de cambios y las fuentes de construcción del sitio pueden consultarse en el <a href="{SITE_REPOSITORY_URL}">repositorio público</a>.</p>
              <h2>Independencia editorial</h2>
              <p>Las fuentes se eligen por su valor documental. Una futura publicidad o colaboración comercial no decidirá qué explicaciones se publican ni su nivel de confianza.</p>
              <h2>Correcciones y contacto</h2>
              <p>Si encuentras un error o una fuente mejor, puedes <a href="{SITE_REPOSITORY_URL}/issues/new">abrir una propuesta de corrección</a>. Indica el nombre afectado y, si es posible, enlaza la fuente.</p>
            </article>''',
        ),
        'metodologia/': (
            'Metodología editorial',
            'Cómo investigamos, contrastamos y clasificamos el origen de cada nombre publicado en Nombres de Madrid.',
            '''<article class="prose">
              <h2>Qué intentamos demostrar</h2>
              <p>Cada entrada separa dos preguntas: de qué lugar o persona tomó el nombre la estación y de dónde procede, a su vez, ese topónimo o antropónimo. Esa separación evita convertir una asociación inmediata en una etimología no demostrada.</p>
              <h2>Jerarquía de fuentes</h2>
              <ol><li>Documentos oficiales, archivos, cartografía histórica y publicaciones de los operadores.</li><li>Investigación académica, diccionarios especializados y monografías.</li><li>Prensa contemporánea y publicaciones locales con autoría identificable.</li><li>Fuentes colaborativas, utilizadas como pista y contrastadas siempre que es posible.</li></ol>
              <h2>Niveles de confianza</h2>
              <dl class="confidence-list"><dt>Verificado</dt><dd>La cadena del nombre está respaldada por una fuente primaria o especializada suficientemente directa.</dd><dt>Probable</dt><dd>La explicación encaja con varias fuentes, pero falta una prueba directa o subsiste una alternativa razonable.</dd><dt>Incierto</dt><dd>Hay versiones enfrentadas, tradición oral o evidencia insuficiente. Se publican las dudas en lugar de ocultarlas.</dd></dl>
              <h2>Cómo se actualiza una entrada</h2>
              <p>Las correcciones conservan su fuente y quedan reflejadas en el historial público del proyecto. No cambiamos fechas para simular actualidad ni elevamos automáticamente una hipótesis por repetirse en muchas páginas.</p>
              <h2>Uso de herramientas</h2>
              <p>El procesamiento de datos y la generación del sitio se automatizan. La valoración de fuentes, las contradicciones y el nivel de confianza forman parte del trabajo editorial y deben poder auditarse.</p>
            </article>''',
        ),
        'privacidad/': (
            'Política de privacidad',
            'Información sobre los datos técnicos y preferencias que utiliza Nombres de Madrid.',
            '''<article class="prose">
              <p><strong>Última actualización:</strong> 27 de agosto de 2026.</p>
              <h2>Datos que recoge el sitio</h2>
              <p>No hay cuentas de usuario, comentarios ni formularios. El navegador guarda únicamente la preferencia de idioma para recordar la interfaz elegida.</p>
              <h2>Alojamiento y registros técnicos</h2>
              <p>El proveedor de alojamiento y la red de distribución pueden tratar direcciones IP, cabeceras y registros técnicos necesarios para entregar y proteger el sitio. Esos registros no se usan aquí para crear perfiles personales.</p>
              <h2>Mapas y recursos externos</h2>
              <p>Al abrir el mapa, el navegador puede solicitar recursos a OpenStreetMap, CARTO y el proveedor técnico de la biblioteca cartográfica. Los enlaces a fuentes y mapas externos aplican las políticas de sus respectivos sitios.</p>
              <h2>Publicidad y analítica</h2>
              <p>Actualmente no se sirven anuncios ni se instala analítica publicitaria. Antes de activar cualquiera de esos servicios, esta política y el mecanismo de consentimiento se actualizarán.</p>
              <h2>Consultas</h2>
              <p>Las consultas sobre privacidad pueden enviarse mediante el <a href="https://github.com/lbm364dl/toponyms-origins/issues/new">canal de contacto del proyecto</a>, sin publicar datos personales sensibles.</p>
            </article>''',
        ),
        'cookies/': (
            'Política de cookies',
            'Qué almacenamiento local y servicios externos utiliza actualmente Nombres de Madrid.',
            '''<article class="prose">
              <p><strong>Última actualización:</strong> 27 de agosto de 2026.</p>
              <h2>Estado actual</h2>
              <p>Nombres de Madrid no instala cookies publicitarias. Guarda en <code>localStorage</code> la preferencia de idioma (<code>lang</code>) para mantener la interfaz en español o inglés.</p>
              <h2>Contenido externo</h2>
              <p>Los mapas se cargan después de una acción del visitante y pueden implicar solicitudes técnicas a OpenStreetMap y CARTO.</p>
              <h2>Cambios futuros</h2>
              <p>Si se incorpora publicidad personalizada o una herramienta que requiera consentimiento, se mostrará un gestor de consentimiento compatible antes de activar esos servicios.</p>
            </article>''',
        ),
    }
    generated = []
    for path, (title, description, body) in pages.items():
        write_page(
            out_root,
            path,
            content_page_html(title, description, path, body, 1, page_type='WebPage'),
        )
        generated.append(path)
    return generated

def sync_homepage_domain(out_root):
    index_path = Path(out_root) / 'index.html'
    text = index_path.read_text(encoding='utf-8')
    match = re.search(r'<!-- site-base-url: (https?://[^ ]+/) -->', text)
    if not match:
        raise RuntimeError('docs/index.html is missing the site-base-url marker')
    previous_url = match.group(1)
    text = text.replace(previous_url, SITE_BASE_URL)
    text = re.sub(
        r'<!-- site-base-url: https?://[^ ]+/ -->',
        f'<!-- site-base-url: {SITE_BASE_URL} -->',
        text,
        count=1,
    )
    index_path.write_text(text, encoding='utf-8')

def build_auxiliary_files(out_root):
    root = Path(out_root)
    not_found_body = '''<article class="prose">
      <h2>Esta dirección no existe</h2>
      <p>Puede que el nombre haya cambiado o que el enlace esté incompleto. Vuelve al índice para buscar la estación por su nombre, línea o distrito.</p>
      <p><a href="./estaciones/">Explorar todas las estaciones</a></p>
    </article>'''
    (root / '404.html').write_text(
        content_page_html(
            'Página no encontrada',
            'La página solicitada no existe en Nombres de Madrid.',
            '404.html',
            not_found_body,
            0,
            robots='noindex, follow',
            page_type='WebPage',
        ),
        encoding='utf-8',
    )
    manifest = {
        'name': SITE_NAME_ES,
        'short_name': SITE_NAME_ES,
        'description': SITE_DESCRIPTION_ES,
        'start_url': site_path(),
        'scope': site_path(),
        'display': 'standalone',
        'background_color': '#101615',
        'theme_color': '#101615',
        'lang': 'es',
        'icons': [
            {'src': site_path('favicon.svg'), 'sizes': 'any', 'type': 'image/svg+xml'},
            {'src': site_path('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'},
        ],
    }
    (root / 'manifest.webmanifest').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (root / 'humans.txt').write_text(
        f'''/* TEAM */
Maintainer: {SITE_OWNER_NAME}
Project: {SITE_NAME_ES}
Repository: {SITE_REPOSITORY_URL}

/* SITE */
Language: Spanish
Standards: HTML5, CSS, JavaScript, Schema.org
License: CC-BY-SA 4.0
''',
        encoding='utf-8',
    )
    (root / '_headers').write_text(
        '''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  X-Frame-Options: SAMEORIGIN

/data/*
  Cache-Control: public, max-age=3600

/stations/*
  Cache-Control: public, max-age=600
''',
        encoding='utf-8',
    )

def build_sitemap(entries, out_root, generated_paths=None):
    today = date.today().isoformat()
    urls = [
        (absolute_url(), today, '1.0'),
    ]
    urls.extend(
        (absolute_url(path), today, '0.7')
        for path in (generated_paths or [])
    )
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

    sync_homepage_domain(os.path.join(ROOT, 'docs'))
    pages_built = build_station_pages(all_entries, os.path.join(ROOT, 'docs'))
    directory_pages = build_directory_pages(all_entries, os.path.join(ROOT, 'docs'))
    trust_pages = build_trust_pages(os.path.join(ROOT, 'docs'), pages_built)
    build_auxiliary_files(os.path.join(ROOT, 'docs'))
    build_sitemap(all_entries, os.path.join(ROOT, 'docs'), directory_pages + trust_pages)

    print(f"Built {len(all_entries)} entries -> docs/data/entries.json + entries.js")
    print(f"Built lightweight index -> docs/data/entries_index.json + entries_index.js")
    print(f"Built {pages_built} station pages -> docs/stations/")
    print(f"Built {len(directory_pages)} crawlable directory pages")
    print(f"Built {len(trust_pages)} editorial and privacy pages")
    print("Built SEO files -> docs/sitemap.xml + docs/robots.txt")
    if station_content:
        merged = sum(1 for e in all_entries if e.get('has_content_entry') == 'true')
        print(f"  Merged {merged} station content entries from content/stations")

if __name__ == '__main__':
    build()
