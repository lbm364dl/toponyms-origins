#!/usr/bin/env python3
"""Audit the generated static site for common crawlability and SEO regressions."""

import json
import os
import re
import sys
from collections import Counter, deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
BASE_URL = os.environ.get('SITE_BASE_URL', 'https://nombresdemadrid.es/').strip()
if not BASE_URL.endswith('/'):
    BASE_URL += '/'
BASE = urlparse(BASE_URL)
BASE_PREFIX = BASE.path.rstrip('/')
OLD_ORIGIN = 'https://lbm364dl.github.io/toponyms-origins'


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.in_title = False
        self.h1_parts = []
        self.h1_count = 0
        self.in_h1 = False
        self.meta = []
        self.links = []
        self.references = []
        self.json_ld_parts = []
        self.in_json_ld = False
        self.current_json_ld = []
        self.images = []
        self.in_main = False
        self.main_words = []

    def handle_starttag(self, tag, attrs):
        values = {key.lower(): value or '' for key, value in attrs}
        tag = tag.lower()
        if tag == 'title':
            self.in_title = True
        elif tag == 'h1':
            self.h1_count += 1
            self.in_h1 = True
        elif tag == 'meta':
            self.meta.append(values)
        elif tag == 'link':
            self.links.append(values)
        elif tag == 'script' and values.get('type', '').lower() == 'application/ld+json':
            self.in_json_ld = True
            self.current_json_ld = []
        elif tag == 'img':
            self.images.append(values)
        elif tag == 'main':
            self.in_main = True

        ref_attr = 'href' if tag in {'a', 'link'} else 'src' if tag in {'img', 'script', 'source'} else None
        if ref_attr and values.get(ref_attr):
            self.references.append((tag, values[ref_attr]))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            self.in_h1 = False
        elif tag == 'script' and self.in_json_ld:
            self.json_ld_parts.append(''.join(self.current_json_ld).strip())
            self.current_json_ld = []
            self.in_json_ld = False
        elif tag == 'main':
            self.in_main = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)
        if self.in_json_ld:
            self.current_json_ld.append(data)
        if self.in_main:
            self.main_words.extend(re.findall(r'[\wÁÉÍÓÚÜÑáéíóúüñ]+', data))

    @property
    def title(self):
        return ' '.join(''.join(self.title_parts).split())

    @property
    def h1(self):
        return ' '.join(''.join(self.h1_parts).split())

    def meta_content(self, key, value):
        return [item.get('content', '').strip() for item in self.meta if item.get(key, '').lower() == value]

    def linked(self, rel):
        return [
            item.get('href', '').strip()
            for item in self.links
            if rel in item.get('rel', '').lower().split()
        ]


def route_for_file(path):
    relative = path.relative_to(DOCS)
    if relative.name == 'index.html':
        parent = relative.parent.as_posix()
        return f'{parent}/' if parent != '.' else ''
    return relative.as_posix()


def canonical_for_route(route):
    return urljoin(BASE_URL, route)


def local_target(page_url, reference):
    reference = reference.strip()
    if not reference or reference.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:', 'blob:')):
        return None
    parsed = urlparse(urljoin(page_url, reference))
    if parsed.scheme not in {'http', 'https'} or parsed.netloc != BASE.netloc:
        return None

    path = unquote(parsed.path)
    if BASE_PREFIX:
        if path == BASE_PREFIX:
            path = '/'
        elif path.startswith(f'{BASE_PREFIX}/'):
            path = path[len(BASE_PREFIX):]
        else:
            return ('outside-base-path', parsed.geturl())

    relative = path.lstrip('/')
    target = DOCS / relative
    if path.endswith('/') or not relative:
        target = target / 'index.html'
    return target.resolve()


def json_types(value):
    found = set()
    if isinstance(value, dict):
        kind = value.get('@type')
        if isinstance(kind, str):
            found.add(kind)
        elif isinstance(kind, list):
            found.update(item for item in kind if isinstance(item, str))
        for child in value.values():
            found.update(json_types(child))
    elif isinstance(value, list):
        for child in value:
            found.update(json_types(child))
    return found


def json_nodes_of_type(value, expected_type):
    nodes = []
    if isinstance(value, dict):
        kind = value.get('@type')
        kinds = {kind} if isinstance(kind, str) else set(kind or []) if isinstance(kind, list) else set()
        if expected_type in kinds:
            nodes.append(value)
        for child in value.values():
            nodes.extend(json_nodes_of_type(child, expected_type))
    elif isinstance(value, list):
        for child in value:
            nodes.extend(json_nodes_of_type(child, expected_type))
    return nodes


def main():
    errors = []
    warnings = []
    pages = {}
    indexable_canonicals = {}
    title_owners = {}
    graph = {}

    html_files = sorted(DOCS.rglob('*.html'))
    if not html_files:
        errors.append('No HTML files found under docs/.')

    for path in html_files:
        route = route_for_file(path)
        page_url = canonical_for_route(route)
        text = path.read_text(encoding='utf-8')
        parser = PageParser()
        parser.feed(text)
        pages[route] = (path, parser, text)

        if OLD_ORIGIN in text:
            errors.append(f'{route or "/"}: old GitHub Pages origin remains in HTML')
        if not parser.title:
            errors.append(f'{route or "/"}: missing title')
        elif len(parser.title) > 65:
            warnings.append(f'{route or "/"}: long title ({len(parser.title)} characters)')

        descriptions = parser.meta_content('name', 'description')
        if len(descriptions) != 1 or not descriptions[0]:
            errors.append(f'{route or "/"}: expected one non-empty meta description')
        elif len(descriptions[0]) > 160:
            warnings.append(f'{route or "/"}: long description ({len(descriptions[0])} characters)')

        robots_values = parser.meta_content('name', 'robots')
        noindex = any('noindex' in value.lower() for value in robots_values)
        canonicals = parser.linked('canonical')
        if len(canonicals) != 1:
            errors.append(f'{route or "/"}: expected one canonical, found {len(canonicals)}')
        else:
            canonical = canonicals[0]
            expected = page_url
            if canonical != expected:
                errors.append(f'{route or "/"}: canonical {canonical!r} should be {expected!r}')
            if not noindex:
                previous = indexable_canonicals.setdefault(canonical, route)
                if previous != route:
                    errors.append(f'{route or "/"}: duplicate canonical also used by {previous or "/"}')

        if not noindex and parser.title:
            previous = title_owners.setdefault(parser.title.casefold(), route)
            if previous != route:
                errors.append(f'{route or "/"}: duplicate title also used by {previous or "/"}')

        if parser.h1_count != 1 or not parser.h1:
            errors.append(f'{route or "/"}: expected one non-empty h1, found {parser.h1_count}')

        alternates = {
            item.get('hreflang', '').lower(): item.get('href', '')
            for item in parser.links
            if 'alternate' in item.get('rel', '').lower().split() and item.get('hreflang')
        }
        if not noindex:
            for language in ('es', 'x-default'):
                if alternates.get(language) != page_url:
                    errors.append(f'{route or "/"}: invalid or missing {language} hreflang')

        structured_types = set()
        structured_documents = []
        if not parser.json_ld_parts:
            errors.append(f'{route or "/"}: missing JSON-LD')
        for raw_json in parser.json_ld_parts:
            try:
                document = json.loads(raw_json)
                structured_documents.append(document)
                structured_types.update(json_types(document))
            except json.JSONDecodeError as exc:
                errors.append(f'{route or "/"}: invalid JSON-LD ({exc})')

        if not noindex and route and 'BreadcrumbList' not in structured_types:
            errors.append(f'{route}: JSON-LD missing BreadcrumbList')

        if route.startswith('stations/'):
            for required in ('Article', 'Place', 'ImageObject', 'BreadcrumbList', 'Organization'):
                if required not in structured_types:
                    errors.append(f'{route}: JSON-LD missing {required}')
            for marker in (
                'class="breadcrumbs"',
                'class="quick-answer"',
                'class="sources"',
                'class="related-stations"',
            ):
                if marker not in text:
                    errors.append(f'{route}: missing station element {marker}')

            articles = []
            for document in structured_documents:
                articles.extend(json_nodes_of_type(document, 'Article'))
            if len(articles) != 1:
                errors.append(f'{route}: expected one Article node, found {len(articles)}')
            else:
                article = articles[0]
                for field in ('headline', 'image', 'datePublished', 'dateModified', 'author', 'publisher'):
                    if not article.get(field):
                        errors.append(f'{route}: Article missing {field}')

            cover_images = [
                image for image in parser.images
                if 'station-cover-image' in image.get('class', '').split()
            ]
            if len(cover_images) != 1:
                errors.append(f'{route}: expected one station cover image, found {len(cover_images)}')
            else:
                cover = cover_images[0]
                if not cover.get('alt', '').strip():
                    errors.append(f'{route}: station cover image has empty alt text')
                if cover.get('width') != '1200' or cover.get('height') != '675':
                    errors.append(f'{route}: station cover image dimensions must be 1200x675')

            if len(parser.main_words) < 300:
                warnings.append(f'{route}: short main content ({len(parser.main_words)} words)')

        local_routes = set()
        for tag, reference in parser.references:
            target = local_target(page_url, reference)
            if target is None:
                continue
            if isinstance(target, tuple):
                errors.append(f'{route or "/"}: internal URL escapes configured base path: {target[1]}')
                continue
            if not target.exists():
                errors.append(f'{route or "/"}: broken local {tag} reference {reference!r}')
                continue
            if target.suffix == '.html':
                try:
                    local_routes.add(route_for_file(target))
                except ValueError:
                    pass
        graph[route] = local_routes

    sitemap_path = DOCS / 'sitemap.xml'
    sitemap_urls = []
    sitemap_images = {}
    if not sitemap_path.exists():
        errors.append('Missing docs/sitemap.xml')
    else:
        try:
            sitemap = ElementTree.parse(sitemap_path)
            namespace = {
                's': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                'image': 'http://www.google.com/schemas/sitemap-image/1.1',
            }
            for url_node in sitemap.findall('.//s:url', namespace):
                loc_node = url_node.find('s:loc', namespace)
                if loc_node is None or not loc_node.text:
                    continue
                loc = loc_node.text.strip()
                sitemap_urls.append(loc)
                sitemap_images[loc] = [
                    node.text.strip()
                    for node in url_node.findall('image:image/image:loc', namespace)
                    if node.text
                ]
        except ElementTree.ParseError as exc:
            errors.append(f'Invalid sitemap.xml: {exc}')

    duplicates = [url for url, count in Counter(sitemap_urls).items() if count > 1]
    if duplicates:
        errors.append(f'Duplicate sitemap URLs: {duplicates[:5]}')
    sitemap_set = set(sitemap_urls)
    indexable_set = set(indexable_canonicals)
    for url in sorted(indexable_set - sitemap_set):
        errors.append(f'Indexable page absent from sitemap: {url}')
    for url in sorted(sitemap_set - indexable_set):
        errors.append(f'Sitemap URL is missing or not indexable: {url}')

    robots_path = DOCS / 'robots.txt'
    expected_sitemap = canonical_for_route('sitemap.xml')
    if not robots_path.exists() or f'Sitemap: {expected_sitemap}' not in robots_path.read_text(encoding='utf-8'):
        errors.append('robots.txt does not advertise the configured sitemap')

    cname_path = DOCS / 'CNAME'
    if not cname_path.exists() or cname_path.read_text(encoding='utf-8').strip() != BASE.netloc:
        errors.append(f'docs/CNAME must contain only {BASE.netloc}')

    # Every station should be reachable from the homepage in at most two links:
    # homepage -> complete station directory -> station.
    depths = {'': 0}
    queue = deque([''])
    while queue:
        route = queue.popleft()
        if depths[route] >= 2:
            continue
        for linked_route in graph.get(route, set()):
            if linked_route not in depths:
                depths[linked_route] = depths[route] + 1
                queue.append(linked_route)
    station_routes = {route for route in pages if route.startswith('stations/')}
    unreachable = sorted(route for route in station_routes if depths.get(route, 99) > 2)
    if unreachable:
        errors.append(f'{len(unreachable)} station pages are more than two links from home (examples: {unreachable[:5]})')

    if len(station_routes) != 368:
        errors.append(f'Expected 368 station pages, found {len(station_routes)}')

    station_images = sorted((DOCS / 'images' / 'stations').glob('*.png'))
    if len(station_images) != len(station_routes):
        errors.append(
            f'Expected {len(station_routes)} station social images, found {len(station_images)}'
        )
    for route in sorted(station_routes):
        page_url = canonical_for_route(route)
        slug = route.rstrip('/').split('/')[-1]
        expected_image = canonical_for_route(f'images/stations/{slug}.png')
        if expected_image not in sitemap_images.get(page_url, []):
            errors.append(f'{route}: station image absent from sitemap')

    homepage_text = pages.get('', (None, None, ''))[2]
    if 'class="home-editorial"' not in homepage_text or 'class="featured-stories"' not in homepage_text:
        errors.append('/: homepage is missing static editorial and featured content')

    if errors:
        print(f'SEO audit failed with {len(errors)} error(s):')
        for error in errors:
            print(f'  ERROR {error}')
    else:
        print(
            f'SEO audit passed: {len(html_files)} HTML files, '
            f'{len(indexable_set)} indexable URLs, {len(station_routes)} station pages.'
        )

    if warnings:
        def warning_kind(warning):
            if 'long title' in warning:
                return 'long title'
            if 'long description' in warning:
                return 'long description'
            if 'short main content' in warning:
                return 'short content'
            return 'other advisory'

        counts = Counter(warning_kind(warning) for warning in warnings)
        print('Advisories: ' + ', '.join(f'{count} {label}(s)' for label, count in sorted(counts.items())))
        for warning in warnings[:10]:
            print(f'  WARN  {warning}')
        if len(warnings) > 10:
            print(f'  WARN  ... {len(warnings) - 10} more')

    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
