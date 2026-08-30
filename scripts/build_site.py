#!/usr/bin/env python3
"""Build static site data from CSV files."""
import csv
import html
import json
import os
import re
import shutil
import unicodedata
from collections import Counter
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
SITE_PUBLISHED_DATE = os.environ.get('SITE_PUBLISHED_DATE', '2026-08-27').strip()
SITE_LASTMOD_DATE = os.environ.get('SITE_LASTMOD_DATE', '2026-08-28').strip()
FEATURED_STATION_IDS = (
    'metro_001',       # Sol
    'metro_029',       # Atocha
    'metro_002',       # Gran Vía
    'metro_010',       # Chamberí
    'metro_007',       # Chueca
    'metro_009',       # Lavapiés
    'metro_025',       # Santiago Bernabéu
    'cercanias_004',   # Chamartín-Clara Campoamor
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
LINE_LABELS_ES = {
    'Tranvia Parla': 'Tranvía de Parla',
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

def inline_markdown_to_html(text):
    """Render the small, safe inline-Markdown subset used by station copy."""
    rendered = esc(text)
    code_fragments = []

    def stash_code(match):
        code_fragments.append(f'<code>{match.group(1)}</code>')
        return f'\x00CODE{len(code_fragments) - 1}\x00'

    rendered = re.sub(r'`([^`\n]+)`', stash_code, rendered)
    rendered = re.sub(
        r'\[([^\]\n]+)\]\((https?://[^)\s]+)\)',
        r'<a href="\2">\1</a>',
        rendered,
    )
    rendered = re.sub(r'\*\*([^*\n]+)\*\*', r'<strong>\1</strong>', rendered)
    rendered = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', rendered)
    for index, fragment in enumerate(code_fragments):
        rendered = rendered.replace(f'\x00CODE{index}\x00', fragment)
    return rendered

def slugify(value):
    value = unicodedata.normalize('NFKD', value or '')
    value = ''.join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower().replace('ñ', 'n')
    value = re.sub(r'[^a-z0-9]+', '-', value)
    value = re.sub(r'-+', '-', value).strip('-')
    return value or 'estacion'

def absolute_url(path=''):
    return SITE_BASE_URL + str(path or '').lstrip('/')

def station_image_path(entry):
    slug = Path(entry.get('page_path', '').rstrip('/')).name
    return f'images/stations/{slug}.png'

def station_image_alt(entry):
    network = STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), 'transporte de Madrid')
    return f'Origen del nombre de la estación {entry.get("name", "")} de {network}'

def format_date_es(iso_date):
    months = (
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
    )
    parsed = date.fromisoformat(iso_date)
    return f'{parsed.day} de {months[parsed.month - 1]} de {parsed.year}'

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
            rendered.append(f'<h{level}>{inline_markdown_to_html(heading.group(2))}</h{level}>')
            continue
        if all(re.match(r'^[-*]\s+', line) for line in lines):
            item_texts = [re.sub(r'^[-*]\s+', '', line) for line in lines]
            items = ''.join(
                f'<li>{inline_markdown_to_html(item)}</li>'
                for item in item_texts
            )
            rendered.append(f'<ul>{items}</ul>')
            continue
        rendered.append(f'<p>{inline_markdown_to_html(" ".join(lines))}</p>')
    return '\n'.join(rendered)

def station_description(entry):
    summary = station_summary(entry, 'es')
    if summary:
        return truncate_text(f'{entry.get("name", "")}: {summary}', 160)
    line = entry.get('line')
    line_text = f' en la línea {format_lines(line)}' if line else ''
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
    return ', '.join(
        LINE_LABELS_ES.get(part.strip(), part.strip())
        for part in str(value or '').split(';')
        if part.strip()
    )

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
    seo_title = entry.get('seo_title_es', '').strip()
    if seo_title:
        candidates = (
            f'{seo_title} | {SITE_NAME_ES}',
            seo_title,
        )
        return next((candidate for candidate in candidates if len(candidate) <= 65), candidates[-1])
    candidates = (
        f'¿Por qué se llama {display_name}? | {SITE_NAME_ES}',
        f'{display_name}: origen del nombre | {SITE_NAME_ES}',
        f'{display_name}: origen del nombre',
    )
    return next((candidate for candidate in candidates if len(candidate) <= 65), candidates[-1])

def station_lastmod(entry):
    return entry.get('last_modified', '').strip() or SITE_LASTMOD_DATE

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
    image_url = absolute_url(station_image_path(entry))
    citations = [
        source.get('url')
        for source in entry.get('sources_structured', [])
        if isinstance(source, dict) and source.get('url')
    ]
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

    article = {
        '@type': 'Article',
        '@id': f'{url}#article',
        'headline': headline,
        'description': station_description(entry),
        'image': [image_url],
        'datePublished': SITE_PUBLISHED_DATE,
        'dateModified': station_lastmod(entry),
        'inLanguage': 'es',
        'isAccessibleForFree': True,
        'license': 'https://creativecommons.org/licenses/by-sa/4.0/',
        'mainEntityOfPage': {'@id': url},
        'about': {'@id': f'{url}#station'},
        'author': {'@id': absolute_url('#organization')},
        'publisher': {'@id': absolute_url('#organization')},
        'wordCount': len(strip_markdown(station_story(entry)).split()),
        'keywords': [
            keyword
            for keyword in (
                'toponimia de Madrid',
                'origen de nombres',
                entry.get('name', ''),
                network_label,
                entry.get('named_after_es') or entry.get('named_after', ''),
            )
            if keyword
        ],
    }
    if citations:
        article['citation'] = citations

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
                'primaryImageOfPage': {
                    '@type': 'ImageObject',
                    '@id': f'{url}#primaryimage',
                    'url': image_url,
                    'contentUrl': image_url,
                    'width': 1200,
                    'height': 675,
                    'caption': station_image_alt(entry),
                },
            },
            article,
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
                f'<a class="source-link source-title" href="{esc(url)}">{inline_markdown_to_html(title)}</a>'
                if url else f'<span class="source-title">{inline_markdown_to_html(title)}</span>'
            )
            type_html = f'<span class="source-type">{esc(source.get("type"))}</span>' if source.get('type') else ''
            relevance_html = (
                f'<div class="source-relevance">{inline_markdown_to_html(relevance)}</div>'
                if relevance else ''
            )
            items.append(f'<div class="source-item">{title_html}{type_html}{relevance_html}</div>')
        return '\n'.join(items)

    raw = entry.get('source') or ''
    items = []
    for source in raw.split(';'):
        source = source.strip()
        if source:
            items.append(
                f'<div class="source-item"><span class="source-title">'
                f'{inline_markdown_to_html(source)}</span></div>'
            )
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
    quick_answer = station_summary(entry, 'es') or description
    named_after = entry.get('named_after_es') or entry.get('named_after') or ''
    title = station_title(entry)
    image_path = station_image_path(entry)
    image_url = absolute_url(image_path)
    image_alt = station_image_alt(entry)
    source_count = len(entry.get('sources_structured', []))
    publication_label = format_date_es(SITE_PUBLISHED_DATE)
    type_label = ETYM_TYPE_LABELS_ES.get(entry.get('etymology_type'), entry.get('etymology_type'))
    badges = []
    if type_label:
        badges.append(f'<a class="badge" href="{root}{type_path(entry.get("etymology_type"))}">{esc(type_label)}</a>')
    confidence_label = CONFIDENCE_LABELS_ES.get(entry.get('confidence'), entry.get('confidence'))
    if confidence_label:
        badges.append(f'<span class="badge">{esc(confidence_label)}</span>')
    for line in entry_lines(entry):
        badges.append(f'<a class="badge" href="{root}{line_path(line)}">Línea {esc(format_lines(line))}</a>')
    badges = ''.join(badges)
    detail_items = (
        ('Origen del nombre', named_after, None),
        (
            'Distrito',
            entry.get('district'),
            f'{root}{district_path(entry.get("district"))}' if entry.get('district') else None,
        ),
        ('Barrio', entry.get('neighbourhood'), None),
        ('Municipio', entry.get('municipality'), None),
        ('Operador', format_operator(entry.get('operator')), None),
        ('Inauguración', entry.get('opening_year'), None),
    )
    detail_parts = []
    for label, value, href in detail_items:
        if not value:
            continue
        value_html = f'<a href="{esc(href)}">{esc(value)}</a>' if href else esc(value)
        detail_parts.append(
            f'<div class="detail-label">{label}</div><div class="detail-value">{value_html}</div>'
        )
    details = ''.join(detail_parts)
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
<meta property="og:image" content="{esc(image_url)}">
<meta property="og:image:secure_url" content="{esc(image_url)}">
<meta property="og:image:alt" content="{esc(image_alt)}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="675">
<meta property="article:published_time" content="{esc(SITE_PUBLISHED_DATE)}">
<meta property="article:modified_time" content="{esc(station_lastmod(entry))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(image_url)}">
<meta name="twitter:image:alt" content="{esc(image_alt)}">
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
    <figure class="station-cover">
      <img class="station-cover-image" src="{root}{esc(image_path)}" alt="{esc(image_alt)}" width="1200" height="675" fetchpriority="high" decoding="async">
    </figure>
    <div class="entry-badges">{badges}</div>
    <p class="editorial-note">Publicado el <time datetime="{esc(SITE_PUBLISHED_DATE)}">{esc(publication_label)}</time> · Investigación de <a href="{root}sobre-el-proyecto/">{esc(SITE_NAME_ES)}</a> · <a href="{root}metodologia/">Cómo verificamos cada origen</a>{f' · {source_count} fuentes consultadas' if source_count else ''}</p>
    <section class="quick-answer" aria-labelledby="quick-answer-heading">
      <h2 id="quick-answer-heading">Respuesta rápida</h2>
      <p>{esc(quick_answer)}</p>
    </section>
    <section class="etymology-summary markdown-content" aria-labelledby="story-heading">
      <h2 id="story-heading">La historia del nombre</h2>
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

def _card_font(size, bold=False, serif=False):
    from PIL import ImageFont

    candidates = []
    if serif:
        candidates.extend([
            '/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
        ])
    elif bold:
        candidates.extend([
            '/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        ])
    else:
        candidates.extend([
            '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        ])
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default(size=size)

def _wrap_card_text(draw, text, font, max_width):
    lines = []
    current = ''
    for word in str(text or '').split():
        candidate = f'{current} {word}'.strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines

def build_station_social_images(entries, out_root):
    try:
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise RuntimeError('Pillow is required to generate station social images. Install requirements.txt.') from exc

    station_entries = [entry for entry in entries if entry.get('_category') in STATION_CATEGORIES]
    image_root = Path(out_root) / 'images' / 'stations'
    if image_root.exists():
        shutil.rmtree(image_root)
    image_root.mkdir(parents=True, exist_ok=True)

    palette = {
        'metro': '#d22b36',
        'cercanias': '#318fc3',
        'metro_ligero': '#178a72',
    }
    for entry in station_entries:
        image = Image.new('RGB', (1200, 675), '#101615')
        draw = ImageDraw.Draw(image)
        accent = palette.get(entry.get('_category'), '#9bc7b7')
        muted_accent = '#30423b'

        # A restrained transport-map motif keeps the family resemblance while
        # the station name and origin make every card meaningfully distinct.
        draw.line([(760, 96), (910, 165), (1120, 115)], fill=muted_accent, width=14, joint='curve')
        draw.line([(720, 560), (900, 480), (1125, 545)], fill=accent, width=16, joint='curve')
        for x, y in ((760, 96), (910, 165), (900, 480), (1125, 545)):
            draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill='#b9d2c8', outline='#465d54', width=5)

        sans_small = _card_font(25, bold=True)
        sans_medium = _card_font(34)
        sans_meta = _card_font(24)
        draw.text((72, 58), SITE_NAME_ES.upper(), font=sans_small, fill='#9bc7b7')
        network_label = STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), 'Transporte de Madrid')
        line_label = format_lines(entry.get('line'))
        eyebrow = f'{network_label}{f" · Línea {line_label}" if line_label else ""}'
        draw.text((72, 112), eyebrow, font=sans_meta, fill='#92a093')

        name = entry.get('name', '')
        name_font = None
        name_lines = []
        for font_size in range(88, 47, -4):
            candidate_font = _card_font(font_size, serif=True)
            candidate_lines = _wrap_card_text(draw, name, candidate_font, 980)
            if len(candidate_lines) <= 2 and all(
                draw.textbbox((0, 0), line, font=candidate_font)[2] <= 980
                for line in candidate_lines
            ):
                name_font = candidate_font
                name_lines = candidate_lines
                break
        if name_font is None:
            name_font = _card_font(48, serif=True)
            name_lines = _wrap_card_text(draw, name, name_font, 980)[:2]

        y = 170
        line_height = name_font.getbbox('Ág')[3] - name_font.getbbox('Ág')[1] + 10
        for line in name_lines:
            draw.text((72, y), line, font=name_font, fill='#eef4ef')
            y += line_height
        draw.text((72, y + 18), '¿Por qué se llama así?', font=sans_medium, fill='#c9d4ca')

        named_after = entry.get('named_after_es') or entry.get('named_after') or ''
        if named_after:
            origin = truncate_text(f'El nombre procede de: {named_after}', 70)
            origin_font = _card_font(27)
            origin_lines = _wrap_card_text(draw, origin, origin_font, 620)[:2]
            origin_y = 470
            for line in origin_lines:
                draw.text((72, origin_y), line, font=origin_font, fill='#b9c5ba')
                origin_y += 39

        type_label = ETYM_TYPE_LABELS_ES.get(entry.get('etymology_type'), 'Origen documentado')
        confidence = CONFIDENCE_LABELS_ES.get(entry.get('confidence'), entry.get('confidence', ''))
        footer_meta = ' · '.join(part for part in (type_label, confidence) if part)
        draw.rounded_rectangle((72, 594, 370, 636), radius=20, fill='#17201d', outline='#30423b', width=2)
        draw.text((92, 602), footer_meta[:34], font=_card_font(20, bold=True), fill='#9bc7b7')
        site_text = 'nombresdemadrid.es'
        site_box = draw.textbbox((0, 0), site_text, font=sans_small)
        draw.text((1128 - (site_box[2] - site_box[0]), 600), site_text, font=sans_small, fill='#92a093')

        output_path = Path(out_root) / station_image_path(entry)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path, format='PNG', optimize=True, compress_level=9)
    return len(station_entries)

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

SECTION_BREADCRUMBS = {
    'redes': 'Redes de transporte',
    'lineas': 'Líneas de Metro y Cercanías',
    'distritos': 'Distritos de Madrid',
    'origenes': 'Tipos de origen',
}

def breadcrumb_items(title, path):
    parts = [part for part in path.strip('/').split('/') if part]
    items = [(SITE_NAME_ES, absolute_url())]
    if len(parts) > 1 and parts[0] in SECTION_BREADCRUMBS:
        items.append((SECTION_BREADCRUMBS[parts[0]], absolute_url(f'{parts[0]}/')))
    items.append((title, absolute_url(path)))
    return items

def breadcrumb_html(title, path, root):
    crumbs = breadcrumb_items(title, path)
    rendered = []
    for index, (name, url) in enumerate(crumbs):
        if index == len(crumbs) - 1:
            rendered.append(f'<span aria-current="page">{esc(name)}</span>')
        else:
            if url == absolute_url():
                href = root
            else:
                href = f'{root}{url.removeprefix(SITE_BASE_URL)}'
            rendered.append(f'<a href="{esc(href)}">{esc(name)}</a><span aria-hidden="true">/</span>')
    return ''.join(rendered)

def collection_json_ld(title, description, path, entries=None, page_type='CollectionPage'):
    url = absolute_url(path)
    crumbs = breadcrumb_items(title, path)
    page = {
        '@type': page_type,
        '@id': url,
        'url': url,
        'name': title,
        'description': description,
        'inLanguage': 'es',
        'isPartOf': {'@id': absolute_url('#website')},
        'publisher': {'@id': absolute_url('#organization')},
        'breadcrumb': {'@id': f'{url}#breadcrumb'},
    }
    if entries:
        page['mainEntity'] = {'@id': f'{url}#list'}
    graph = [
        page,
        {
            '@type': 'BreadcrumbList',
            '@id': f'{url}#breadcrumb',
            'itemListElement': [
                {
                    '@type': 'ListItem',
                    'position': index,
                    'name': name,
                    'item': item_url,
                }
                for index, (name, item_url) in enumerate(crumbs, 1)
            ],
        },
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

def collection_insights_html(entries, root):
    if not entries:
        return ''

    confidence_counts = Counter(entry.get('confidence') for entry in entries if entry.get('confidence'))
    confidence_count_labels = {
        'verified': ('verificado', 'verificados'),
        'probable': ('probable', 'probables'),
        'uncertain': ('incierto', 'inciertos'),
    }
    confidence_parts = [
        f'{confidence_counts[key]} {confidence_count_labels[key][confidence_counts[key] != 1]}'
        for key in CONFIDENCE_LABELS_ES
        if confidence_counts.get(key)
    ]
    type_counts = Counter(entry.get('etymology_type') for entry in entries if entry.get('etymology_type'))
    common_types = type_counts.most_common(3)
    type_text = ', '.join(
        f'{ETYM_TYPE_LABELS_ES.get(key, key).lower()} ({count})'
        for key, count in common_types
    )
    years = sorted(
        int(entry['opening_year'])
        for entry in entries
        if str(entry.get('opening_year', '')).isdigit()
    )

    paragraphs = [
        f'La colección reúne {len(entries)} estaciones. Por nivel de evidencia hay {", ".join(confidence_parts)}.'
        if confidence_parts else f'La colección reúne {len(entries)} estaciones documentadas.'
    ]
    if len(type_counts) > 1:
        paragraphs.append(f'Los orígenes más frecuentes son de tipo {type_text}.')
    if years:
        if years[0] == years[-1]:
            paragraphs.append(f'Las estaciones de esta selección se inauguraron en {years[0]}.')
        else:
            paragraphs.append(f'Las fechas de apertura abarcan desde {years[0]} hasta {years[-1]}.')

    def documentation_score(entry):
        return (
            len(entry.get('sources_structured', [])) * 1000
            + len(strip_markdown(station_story(entry)))
        )

    highlights = sorted(
        entries,
        key=lambda entry: (-documentation_score(entry), (entry.get('name') or '').casefold()),
    )[:3]
    highlight_items = ''.join(
        f'<li><a href="{root}{esc(entry["page_path"])}"><strong>{esc(entry.get("name"))}</strong>'
        f'<span>{esc(truncate_text(station_summary(entry, "es"), 170))}</span></a></li>'
        for entry in highlights
    )
    return f'''<section class="collection-insights" aria-labelledby="collection-insights-heading">
      <h2 id="collection-insights-heading">Qué encontrarás en esta colección</h2>
      <p>{esc(' '.join(paragraphs))}</p>
      <h3>Historias con más documentación</h3>
      <ul>{highlight_items}</ul>
    </section>'''

def content_page_html(
    title,
    description,
    path,
    body_html,
    depth=1,
    entries=None,
    robots='index, follow, max-snippet:-1, max-image-preview:large',
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
    breadcrumbs = breadcrumb_html(title, path, root)
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
<meta property="og:image:secure_url" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<meta property="og:image:alt" content="Mapa tipográfico de nombres de estaciones de Madrid">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(page_title)}">
<meta name="twitter:description" content="{esc(truncate_text(description, 160))}">
<meta name="twitter:image" content="{esc(absolute_url(SITE_OG_IMAGE))}">
<meta name="twitter:image:alt" content="Mapa tipográfico de nombres de estaciones de Madrid">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">{json_ld(schema)}</script>
</head>
<body class="content-page">
<header>
  <div class="container content-hero">
    {primary_nav_html(root)}
    <nav class="breadcrumbs" aria-label="Migas de pan">{breadcrumbs}</nav>
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
      {collection_insights_html(stations, '../')}
      {directory_entries_html(stations, '../')}
    </section>'''
    write_page(out_root, 'estaciones/', content_page_html('Todas las estaciones', description, 'estaciones/', body, 1, stations))
    generated.append('estaciones/')

    network_links = []
    for category, network_entries in sorted(networks.items(), key=lambda item: STATION_CATEGORY_LABELS_ES.get(item[0], item[0])):
        label = STATION_CATEGORY_LABELS_ES.get(category, category)
        path = f'redes/{STATION_CATEGORY_SLUGS.get(category, slugify(category))}/'
        network_description = f'Origen de los nombres de {len(network_entries)} estaciones de {label}, con investigación y fuentes consultables.'
        body = f'''<section class="page-section"><h2>Estaciones de {esc(label)}</h2><p>{esc(network_description)}</p>{collection_insights_html(network_entries, '../../')}{directory_entries_html(network_entries, '../../')}</section>'''
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de {label}', network_description, path, body, 2, network_entries))
        generated.append(path)
        network_links.append((label, path, f'{len(network_entries)} estaciones documentadas'))
    path = 'redes/'
    body = f'''<section class="page-section"><h2>Explora por red</h2>
      <p>La red condiciona cómo nacen y se conservan los nombres. Metro combina topónimos históricos, calles y personajes; Cercanías amplía el mapa a municipios y paisajes regionales; Metro Ligero y el Tranvía reflejan desarrollos urbanos más recientes.</p>
      {link_directory_html(network_links, "../")}</section>'''
    write_page(out_root, path, content_page_html('Redes de transporte', 'Consulta los nombres de estaciones por red de transporte de Madrid.', path, body, 1))
    generated.append(path)

    line_links = []
    for line, line_entries in sorted(lines.items(), key=lambda item: natural_sort_key(item[0])):
        path = line_path(line)
        label = f'Línea {format_lines(line)}'
        line_description = f'Por qué se llaman así las {len(line_entries)} estaciones de la {label} en Madrid, con fuentes y nivel de confianza.'
        body = f'''<section class="page-section"><h2>Origen de los nombres de la {esc(label)}</h2><p>{esc(line_description)}</p>{collection_insights_html(line_entries, '../../')}{directory_entries_html(line_entries, '../../')}</section>'''
        indexable = len(line_entries) >= 3
        robots = 'index, follow, max-snippet:-1, max-image-preview:large' if indexable else 'noindex, follow'
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de la {label}', line_description, path, body, 2, line_entries, robots=robots))
        if indexable:
            generated.append(path)
        line_links.append((label, path, f'{len(line_entries)} estaciones'))
    path = 'lineas/'
    body = f'''<section class="page-section"><h2>Explora por línea</h2>
      <p>Recorre cada línea como una secuencia de nombres: barrios atravesados, antiguas puertas, personajes, municipios y paisajes. Las colecciones enlazan cada estación con su explicación completa y permiten comparar cómo cambia la toponimia a lo largo del trayecto.</p>
      {link_directory_html(line_links, "../")}</section>'''
    write_page(out_root, path, content_page_html('Líneas de Metro y Cercanías', 'Índice de líneas para explorar el origen de los nombres de sus estaciones.', path, body, 1))
    generated.append(path)

    district_links = []
    for district, district_entries in sorted(districts.items(), key=lambda item: item[0].casefold()):
        path = district_path(district)
        district_description = f'Origen de los nombres de {len(district_entries)} estaciones situadas en el distrito de {district}, Madrid.'
        body = f'''<section class="page-section"><h2>Estaciones de {esc(district)}</h2><p>{esc(district_description)}</p>{collection_insights_html(district_entries, '../../')}{directory_entries_html(district_entries, '../../')}</section>'''
        indexable = len(district_entries) >= 3
        robots = 'index, follow, max-snippet:-1, max-image-preview:large' if indexable else 'noindex, follow'
        write_page(out_root, path, content_page_html(f'Nombres de estaciones de {district}', district_description, path, body, 2, district_entries, robots=robots))
        if indexable:
            generated.append(path)
        district_links.append((district, path, f'{len(district_entries)} estaciones'))
    path = 'distritos/'
    body = f'''<section class="page-section"><h2>Explora por distrito</h2>
      <p>Los nombres del transporte forman una geografía histórica de Madrid. Agrupar las estaciones por distrito permite reconocer antiguos pueblos, fincas, arroyos, caminos y figuras locales que siguen presentes en el mapa contemporáneo.</p>
      {link_directory_html(district_links, "../")}</section>'''
    write_page(out_root, path, content_page_html('Distritos de Madrid', 'Explora los orígenes de nombres de estaciones por distrito madrileño.', path, body, 1))
    generated.append(path)

    type_links = []
    for etymology_type, type_entries in sorted(types.items(), key=lambda item: ETYM_TYPE_LABELS_ES.get(item[0], item[0])):
        label = ETYM_TYPE_LABELS_ES.get(etymology_type, etymology_type)
        path = type_path(etymology_type)
        type_description = f'Estaciones de Madrid cuyo nombre tiene un origen de tipo {label.lower()}: {len(type_entries)} casos documentados.'
        body = f'''<section class="page-section"><h2>Origen {esc(label.lower())}</h2><p>{esc(type_description)}</p>{collection_insights_html(type_entries, '../../')}{directory_entries_html(type_entries, '../../')}</section>'''
        indexable = len(type_entries) >= 3
        robots = 'index, follow, max-snippet:-1, max-image-preview:large' if indexable else 'noindex, follow'
        write_page(out_root, path, content_page_html(f'Nombres de origen {label.lower()}', type_description, path, body, 2, type_entries, robots=robots))
        if indexable:
            generated.append(path)
        type_links.append((label, path, f'{len(type_entries)} estaciones'))
    path = 'origenes/'
    body = f'''<section class="page-section"><h2>Explora por tipo de origen</h2>
      <p>Esta clasificación separa nombres heredados de lugares, personas, hechos históricos, descripciones del terreno, advocaciones religiosas y oficios. Es una puerta de entrada comparativa; cada ficha explica los matices y las dudas que una categoría resumida no puede mostrar.</p>
      {link_directory_html(type_links, "../")}</section>'''
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

def homepage_featured_html(entries):
    by_id = {entry.get('id'): entry for entry in entries}
    featured = [by_id[station_id] for station_id in FEATURED_STATION_IDS if station_id in by_id]
    cards = ''.join(
        f'''<li><a href="{esc(entry['page_path'])}">
          <span class="featured-network">{esc(STATION_CATEGORY_LABELS_ES.get(entry.get('_category'), 'Estación'))}</span>
          <strong>{esc(entry.get('name'))}</strong>
          <span>{esc(truncate_text(station_summary(entry, 'es'), 155))}</span>
        </a></li>'''
        for entry in featured
    )
    return f'''<section class="home-editorial" aria-labelledby="home-editorial-heading">
    <div class="home-editorial-copy">
      <span class="section-kicker">Del andén al origen</span>
      <h2 id="home-editorial-heading">Un nombre no empieza en la estación</h2>
      <p>La mayoría de las estaciones heredan el nombre de una calle, plaza, barrio, municipio o personaje. Este atlas sigue esa cadena completa: identifica el referente inmediato y después investiga de dónde procede realmente el topónimo.</p>
      <p>Cada ficha distingue hechos documentados, explicaciones probables y versiones inciertas. Las fuentes se muestran junto al texto para que puedas comprobarlas y proponer correcciones.</p>
      <p><a class="text-link" href="metodologia/">Consulta la metodología editorial</a> o empieza por una de estas historias.</p>
    </div>
    <div>
      <h2>Historias para empezar</h2>
      <ul class="featured-stories">{cards}</ul>
    </div>
  </section>'''

def sync_homepage_domain(out_root, entries):
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
    text = re.sub(r'"datePublished": "\d{4}-\d{2}-\d{2}"', f'"datePublished": "{SITE_PUBLISHED_DATE}"', text)
    text = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{SITE_LASTMOD_DATE}"', text)
    featured_pattern = r'<!-- featured-stories:start -->.*?<!-- featured-stories:end -->'
    if not re.search(featured_pattern, text, flags=re.DOTALL):
        raise RuntimeError('docs/index.html is missing the featured-stories markers')
    text = re.sub(
        featured_pattern,
        f'<!-- featured-stories:start -->\n{homepage_featured_html(entries)}\n  <!-- featured-stories:end -->',
        text,
        count=1,
        flags=re.DOTALL,
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
    urls = [
        (absolute_url(), SITE_LASTMOD_DATE, '1.0', None),
    ]
    urls.extend(
        (absolute_url(path), SITE_LASTMOD_DATE, '0.7', None)
        for path in (generated_paths or [])
    )
    urls.extend(
        (
            absolute_url(entry['page_path']),
            station_lastmod(entry),
            '0.8',
            absolute_url(station_image_path(entry)),
        )
        for entry in entries
        if entry.get('_category') in STATION_CATEGORIES and entry.get('page_path')
    )
    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    for loc, lastmod, priority, image_url in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{xml_escape(loc)}</loc>')
        xml.append(f'    <lastmod>{lastmod}</lastmod>')
        xml.append(f'    <priority>{priority}</priority>')
        if image_url:
            xml.append('    <image:image>')
            xml.append(f'      <image:loc>{xml_escape(image_url)}</image:loc>')
            xml.append('    </image:image>')
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
        seo_title = meta.get('seo_title_es', '').strip()
        if seo_title:
            entry_content['seo_title_es'] = seo_title
        last_modified = meta.get('last_modified', '').strip()
        if last_modified:
            entry_content['last_modified'] = last_modified

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

    sync_homepage_domain(os.path.join(ROOT, 'docs'), all_entries)
    images_built = build_station_social_images(all_entries, os.path.join(ROOT, 'docs'))
    pages_built = build_station_pages(all_entries, os.path.join(ROOT, 'docs'))
    directory_pages = build_directory_pages(all_entries, os.path.join(ROOT, 'docs'))
    trust_pages = build_trust_pages(os.path.join(ROOT, 'docs'), pages_built)
    build_auxiliary_files(os.path.join(ROOT, 'docs'))
    build_sitemap(all_entries, os.path.join(ROOT, 'docs'), directory_pages + trust_pages)

    print(f"Built {len(all_entries)} entries -> docs/data/entries.json + entries.js")
    print(f"Built lightweight index -> docs/data/entries_index.json + entries_index.js")
    print(f"Built {pages_built} station pages -> docs/stations/")
    print(f"Built {images_built} station social images -> docs/images/stations/")
    print(f"Built {len(directory_pages)} crawlable directory pages")
    print(f"Built {len(trust_pages)} editorial and privacy pages")
    print("Built SEO files -> docs/sitemap.xml + docs/robots.txt")
    if station_content:
        merged = sum(1 for e in all_entries if e.get('has_content_entry') == 'true')
        print(f"  Merged {merged} station content entries from content/stations")

if __name__ == '__main__':
    build()
