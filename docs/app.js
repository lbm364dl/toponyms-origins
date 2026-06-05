let entries = [];
let activeCategory = '';
let activeLine = '';
let map = null;
let markers = null;
let lineLayer = null;
let fullEntries = null;
let fullEntriesPromise = null;
let mapAssetsPromise = null;
let currentView = 'map';
let lang = localStorage.getItem('lang') || 'es';
let initialized = false;
let renderLimit = 80;
let pendingStationId = '';
let activeModalId = '';
let modalCloseTimer = null;

const DEFAULT_RENDER_LIMIT = 80;
const RENDER_INCREMENT = 80;
const STATION_CATEGORIES = new Set(['metro', 'cercanias', 'metro_ligero']);
const APP_ROOT_PATH = (() => {
  const path = window.location.pathname;
  if (path.endsWith('/index.html')) return path.slice(0, -'index.html'.length);
  return path.endsWith('/') ? path : path.replace(/[^/]*$/, '');
})();
const SITE_TITLES = {
  en: 'Madrid Station Name Origins',
  es: 'Origen de nombres de estaciones de Madrid'
};

const CATEGORY_LABELS = {
  en: { metro: 'Metro', cercanias: 'Cercanías', metro_ligero: 'ML / Tranvía' },
  es: { metro: 'Metro', cercanias: 'Cercanías', metro_ligero: 'ML / Tranvía' }
};

const I18N = {
  en: {
    siteTitle: SITE_TITLES.en,
    pageTitle: `${SITE_TITLES.en} | Metro and Cercanías`,
    title: 'Madrid Station<br>Name Origins',
    subtitle: 'An atlas of {count} Madrid station-name origins — Metro, Cercanías, Metro Ligero & Tranvía — explaining why each station is named the way it is.',
    eyebrow: 'Open dataset',
    searchPlaceholder: 'Search names, etymologies, people, places...',
    allStations: 'All stations', list: 'List', map: 'Map',
    allTypes: 'Types', allConfidence: 'Confidence', allLines: 'Lines',
    person: 'Person', place: 'Place', descriptive: 'Descriptive', historical: 'Historical',
    religious: 'Religious', event: 'Event', occupation: 'Occupation', mythological: 'Mythological', unknown: 'Unknown',
    verified: 'Verified', probable: 'Probable', uncertain: 'Uncertain',
    places: 'Stations', sources: 'Sources', namedAfter: 'Named after',
    footerTitle: 'Madrid Station Name Origins Dataset',
    gender: 'Gender', male: 'Male', female: 'Female', lived: 'Lived',
    profession: 'Profession', nationality: 'Nationality', district: 'District',
    neighbourhood: 'Neighbourhood', lines: 'Line(s)', opened: 'Opened',
    namedIn: 'Named in', formerNames: 'Former names', operator: 'Operator',
    municipality: 'Municipality', coordinates: 'Coordinates',
    readMore: 'Read full etymology →',
    footer: '{count} station-name origins · CC-BY-SA 4.0',
    showing: 'Showing', of: 'of', entries: 'entries',
    loadMore: 'Show more',
    loadingEntry: 'Loading entry...',
    loadingMap: 'Loading map...',
    mapPromptTitle: 'Choose a line to open the map',
    mapPromptBody: 'The full network stays off the home page for speed. Pick a line or narrow the list with search and filters.',
    narrowMapTitle: 'Narrow the results to map them',
    narrowMapBody: 'This selection is still too broad for a fast mobile map.',
  },
  es: {
    siteTitle: SITE_TITLES.es,
    pageTitle: `${SITE_TITLES.es} | Metro y Cercanías`,
    title: 'Origen de nombres<br>de estaciones de Madrid',
    subtitle: 'Un atlas de {count} orígenes de nombres de estaciones de Madrid — Metro, Cercanías, Metro Ligero y Tranvía — que explica por qué cada estación se llama así.',
    eyebrow: 'Nombres de estaciones',
    searchPlaceholder: 'Buscar nombres, etimologías, personas, lugares...',
    allStations: 'Todas', list: 'Lista', map: 'Mapa',
    allTypes: 'Tipos', allConfidence: 'Confianza', allLines: 'Líneas',
    person: 'Persona', place: 'Lugar', descriptive: 'Descriptivo', historical: 'Histórico',
    religious: 'Religioso', event: 'Evento', occupation: 'Oficio', mythological: 'Mitológico', unknown: 'Desconocido',
    verified: 'Verificado', probable: 'Probable', uncertain: 'Incierto',
    places: 'Estaciones', sources: 'Fuentes', namedAfter: 'Origen del nombre',
    footerTitle: 'Dataset de orígenes de nombres de estaciones',
    gender: 'Género', male: 'Masculino', female: 'Femenino', lived: 'Vivió',
    profession: 'Profesión', nationality: 'Nacionalidad', district: 'Distrito',
    neighbourhood: 'Barrio', lines: 'Línea(s)', opened: 'Inauguración',
    namedIn: 'Nombrado en', formerNames: 'Nombres anteriores', operator: 'Operador',
    municipality: 'Municipio', coordinates: 'Coordenadas',
    readMore: 'Leer etimología completa →',
    footer: '{count} orígenes de nombres de estaciones · CC-BY-SA 4.0',
    showing: 'Mostrando', of: 'de', entries: 'entradas',
    loadMore: 'Mostrar más',
    loadingEntry: 'Cargando entrada...',
    loadingMap: 'Cargando mapa...',
    mapPromptTitle: 'Elige una línea para abrir el mapa',
    mapPromptBody: 'La red completa queda fuera de la portada para que cargue rápido. Elige una línea o acota la lista con búsqueda y filtros.',
    narrowMapTitle: 'Acota los resultados para mapearlos',
    narrowMapBody: 'Esta selección todavía es demasiado amplia para un mapa móvil rápido.',
  }
};

function t(key) { return I18N[lang][key] || I18N.en[key] || key; }
function tt(key) { return t(key).replace('{count}', entries.length); }
function modalDocumentTitle(name) { return `${name} - ${t('siteTitle')}`; }

const LINE_COLORS = {
  '1':'#38a3dc','2':'#d8232a','3':'#ffd520','4':'#944735','5':'#96bf0d',
  '6':'#9ba2a5','7':'#f6a800','8':'#ea6da8','9':'#a3228d','10':'#064480',
  '11':'#2a993c','12':'#a69938','R':'#003da5',
  'ML1':'#38a3dc','ML2':'#d8232a','ML3':'#ffd520',
  'Tranvia Parla':'#5bc236',
  'C-1':'#62a0d8','C-2':'#00806a','C-3':'#a94394','C-4':'#0071ce',
  'C-5':'#f5d327','C-7':'#e77128','C-8':'#c5c625','C-9':'#8d1c8c','C-10':'#0097b5',
  'C-3a':'#a94394','C-4a':'#0071ce','C-4b':'#0071ce',
};

const LOOP_LINES = new Set(['6', '12', 'Tranvia Parla']);
const LINE_ALIAS_PARENTS = { 'C-4a': 'C-4', 'C-4b': 'C-4' };

async function init() {
  normalizeDocumentLinks();

  if (typeof ENTRIES_INDEX_DATA !== 'undefined') {
    entries = ENTRIES_INDEX_DATA.filter(e => STATION_CATEGORIES.has(e._category));
  } else {
    try {
      const res = await fetch('data/entries_index.json');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const all = await res.json();
      entries = all.filter(e => STATION_CATEGORIES.has(e._category));
    } catch (err) {
      document.getElementById('entries').innerHTML =
        `<div style="padding:40px;text-align:center;color:var(--text-secondary)">
          <p>Could not load data. Run: <code>cd docs && python3 -m http.server 8080</code></p>
        </div>`;
      return;
    }
  }

  applyLang();
  renderStats();
  buildLineFilter();

  // Restore state from URL query params
  restoreFromURL();

  render();
  setView(currentView);

  document.getElementById('search').addEventListener('input', () => { filtersChanged(); });
  document.getElementById('filter-type').addEventListener('change', () => { filtersChanged(); });
  document.getElementById('filter-confidence').addEventListener('change', () => { filtersChanged(); });
  document.getElementById('filter-line').addEventListener('change', function() {
    activeLine = this.value;
    filtersChanged();
  });

  document.querySelectorAll('#category-pills .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#category-pills .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.dataset.v;
      filtersChanged();
    });
  });

  document.getElementById('modal-overlay').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeModal();
  });
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

  document.getElementById('btn-list').addEventListener('click', () => setView('list'));
  document.getElementById('btn-map').addEventListener('click', () => setView('map'));
  window.addEventListener('popstate', syncModalFromURL);
  document.getElementById('lang-toggle').addEventListener('click', e => {
    const btn = e.target.closest('.lang-opt');
    if (!btn || btn.dataset.lang === lang) return;
    toggleLang();
  });
  initialized = true;
  if (pendingStationId && entries.some(e => e.id === pendingStationId)) {
    openModal(pendingStationId, { push: false });
    history.replaceState({ station: pendingStationId }, '', stationURL(pendingStationId));
  }
}

function normalizeDocumentLinks() {
  const icon = document.querySelector('link[rel="icon"]');
  if (icon) icon.href = assetURL(icon.getAttribute('href'));
}

function filtersChanged() {
  renderLimit = DEFAULT_RENDER_LIMIT;
  render();
  pushURL();
}

function toggleLang() {
  lang = lang === 'en' ? 'es' : 'en';
  localStorage.setItem('lang', lang);
  applyLang();
  renderStats();
  render();
  pushURL();
}

function pushURL() {
  if (!initialized) return;
  if (activeModalId) {
    history.replaceState({ station: activeModalId }, '', stationURL(activeModalId));
    return;
  }
  history.replaceState(null, '', appStateURL());
}

function appStateURL() {
  const params = new URLSearchParams();
  const q = document.getElementById('search').value;
  if (q) params.set('q', q);
  if (activeCategory) params.set('cat', activeCategory);
  if (activeLine) params.set('line', activeLine);
  const typ = document.getElementById('filter-type').value;
  if (typ) params.set('type', typ);
  const conf = document.getElementById('filter-confidence').value;
  if (conf) params.set('conf', conf);
  params.set('view', currentView);
  const str = params.toString();
  return str ? `${APP_ROOT_PATH}?${str}` : APP_ROOT_PATH;
}

function stationURL(id) {
  const entry = entries.find(e => e.id === id);
  if (entry && entry.page_path) return APP_ROOT_PATH + entry.page_path;
  const url = appStateURL();
  return `${url}${url.includes('?') ? '&' : '?'}station=${encodeURIComponent(id)}`;
}

function setStationURL(id) {
  if (!initialized) return;
  history.pushState({ station: id }, '', stationURL(id));
}

function clearStationURL() {
  if (!initialized) return;
  history.replaceState(null, '', appStateURL());
}

function syncModalFromURL() {
  const stationId = stationIdFromCurrentURL();
  if (stationId && stationId !== activeModalId) {
    openModal(stationId, { push: false });
    return;
  }
  if (!stationId && activeModalId) {
    closeModal({ updateURL: false });
  }
}

function stationIdFromCurrentURL() {
  const queryId = new URLSearchParams(window.location.search).get('station') || '';
  if (queryId) return queryId;
  if (!window.location.pathname.startsWith(APP_ROOT_PATH)) return '';
  const relPath = normalizeRelativePath(window.location.pathname.slice(APP_ROOT_PATH.length));
  if (!relPath.startsWith('stations/')) return '';
  const entry = entries.find(e => normalizeRelativePath(e.page_path) === relPath);
  return entry ? entry.id : '';
}

function normalizeRelativePath(path) {
  const cleaned = String(path || '').replace(/^\/+/, '');
  return cleaned ? cleaned.replace(/\/?$/, '/') : '';
}

function restoreFromURL() {
  const params = new URLSearchParams(window.location.search);

  const q = params.get('q');
  if (q) document.getElementById('search').value = q;

  const cat = params.get('cat');
  if (cat) {
    activeCategory = cat;
    document.querySelectorAll('#category-pills .pill').forEach(b => {
      b.classList.toggle('active', b.dataset.v === cat);
    });
  }

  const line = params.get('line');
  if (line) {
    activeLine = line;
    document.getElementById('filter-line').value = line;
  }

  const typ = params.get('type');
  if (typ) document.getElementById('filter-type').value = typ;

  const conf = params.get('conf');
  if (conf) document.getElementById('filter-confidence').value = conf;

  const view = params.get('view');
  if (view === 'map' || view === 'list') currentView = view;

  pendingStationId = stationIdFromCurrentURL();

}

function applyLang() {
  document.documentElement.lang = lang;
  document.querySelectorAll('#lang-toggle .lang-opt').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  document.querySelector('.hero-eyebrow').textContent = t('eyebrow');
  document.querySelector('header h1').innerHTML = t('title');
  document.querySelector('.subtitle').textContent = tt('subtitle');
  document.getElementById('search').placeholder = t('searchPlaceholder');
  document.querySelector('[data-v=""]').textContent = t('allStations');
  document.getElementById('btn-list').lastChild.textContent = ' ' + t('list');
  document.getElementById('btn-map').lastChild.textContent = ' ' + t('map');
  document.querySelector('.footer-note').textContent = tt('footer');
  document.getElementById('footer-title').textContent = t('footerTitle');
  const activeEntry = activeModalId ? entries.find(e => e.id === activeModalId) : null;
  document.title = activeEntry ? modalDocumentTitle(activeEntry.name) : t('pageTitle');

  // Update selects
  const typeOpts = ['', 'person','place','descriptive','historical','religious','event','occupation','mythological','unknown'];
  const typeEl = document.getElementById('filter-type');
  typeOpts.forEach((v, i) => {
    if (typeEl.options[i]) typeEl.options[i].text = v ? t(v) : t('allTypes');
  });
  const confOpts = ['', 'verified','probable','uncertain'];
  const confEl = document.getElementById('filter-confidence');
  confOpts.forEach((v, i) => {
    if (confEl.options[i]) confEl.options[i].text = v ? t(v) : t('allConfidence');
  });
  // Update line filter first option
  const lineEl = document.getElementById('filter-line');
  if (lineEl.options[0]) lineEl.options[0].text = t('allLines');
}

function renderStats() {
  const v = entries.filter(e => e.confidence === 'verified').length;
  const p = entries.filter(e => e.confidence === 'probable').length;
  const u = entries.filter(e => e.confidence === 'uncertain').length;
  document.getElementById('stats').innerHTML = `
    <div class="stat"><span class="stat-value">${entries.length}</span><span class="stat-label">${t('places')}</span></div>
    <div class="stat"><span class="stat-value">${v}</span><span class="stat-label">${t('verified')}</span></div>
    <div class="stat"><span class="stat-value">${p}</span><span class="stat-label">${t('probable')}</span></div>
    <div class="stat"><span class="stat-value">${u}</span><span class="stat-label">${t('uncertain')}</span></div>
  `;
}

function buildLineFilter() {
  const lines = new Set();
  entries.forEach(e => {
    if (e.line) e.line.split(';').forEach(l => lines.add(l.trim()));
  });
  const sorted = sortLines([...lines]);
  const sel = document.getElementById('filter-line');
  sel.innerHTML = `<option value="">${t('allLines')}</option>` +
    sorted.map(l => `<option value="${l}">${l}</option>`).join('');
}

function sortLines(lines) {
  return lines.sort((a, b) => {
    const ka = lineSortKey(a);
    const kb = lineSortKey(b);
    for (let i = 0; i < Math.max(ka.length, kb.length); i++) {
      if (ka[i] === kb[i]) continue;
      if (typeof ka[i] === 'number' && typeof kb[i] === 'number') return ka[i] - kb[i];
      return String(ka[i] || '').localeCompare(String(kb[i] || ''));
    }
    return a.localeCompare(b);
  });
}

function lineSortKey(line) {
  if (/^\d+$/.test(line)) return [0, Number(line)];
  if (line === 'R') return [0, 99];
  const ml = line.match(/^ML(\d+)$/);
  if (ml) return [1, Number(ml[1])];
  if (line === 'Tranvia Parla') return [2, 0];
  const cerc = line.match(/^C-(\d+)([a-z]?)$/i);
  if (cerc) return [3, Number(cerc[1]), cerc[2] || ''];
  return [9, line];
}

function getFiltered() {
  const q = document.getElementById('search').value.toLowerCase();
  const typ = document.getElementById('filter-type').value;
  const conf = document.getElementById('filter-confidence').value;
  return entries.filter(e => {
    if (activeCategory && e._category !== activeCategory) return false;
    if (typ && e.etymology_type !== typ) return false;
    if (conf && e.confidence !== conf) return false;
    if (activeLine && !(e.line || '').split(';').some(l => l.trim() === activeLine)) return false;
    if (q) {
      const haystack = [
        e.name, e.etymology_summary, e.etymology_summary_es,
        e.content_summary_short_en, e.content_summary_short_es,
        e.content_summary_en, e.content_summary_es,
        e.content_story_en, e.content_story_es,
        e.named_after, e.named_after_es, e.etymology_type,
        e.person_profession, e.district, e.neighbourhood, e.line, e.id
      ].filter(Boolean).join(' ').toLowerCase();
      return haystack.includes(q);
    }
    return true;
  });
}

function render() {
  const filtered = getFiltered();
  const countEl = document.getElementById('result-count');
  countEl.textContent = filtered.length === entries.length
    ? `${entries.length} ${t('entries')}`
    : `${t('showing')} ${filtered.length} ${t('of')} ${entries.length} ${t('entries')}`;

  const container = document.getElementById('entries');
  const visible = filtered.slice(0, renderLimit);
  container.innerHTML = visible.map(cardHTML).join('');
  if (filtered.length > renderLimit) {
    container.insertAdjacentHTML('beforeend',
      `<div class="load-more-wrap">
        <button class="load-more-btn" onclick="loadMoreEntries()">${t('loadMore')}</button>
        <span>${t('showing')} ${renderLimit} ${t('of')} ${filtered.length}</span>
      </div>`);
  }
  if (currentView === 'map') renderMapView(filtered);
}

function loadMoreEntries() {
  renderLimit += RENDER_INCREMENT;
  render();
}

function cardHTML(e) {
  const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';
  const summary = entryCardSummary(e);
  const district = e.district || '';
  const line = e.line ? `${t('lines').split('(')[0]} ${formatLineList(e.line)}` : '';
  const meta = [catLabel, district, line].filter(Boolean).join(' \u00b7 ');
  const href = stationURL(e.id);

  return `<article class="entry-card">
    <a class="entry-card-link" href="${escAttr(href)}" data-station-id="${escAttr(e.id)}" onclick="event.preventDefault(); openModal(this.dataset.stationId)">
      <div class="entry-header"><span class="entry-name">${esc(e.name)}</span></div>
      <div class="entry-meta">${esc(meta)}</div>
      <div class="entry-badges">
        <span class="badge badge-type ${etType}">${t(etType)}</span>
        <span class="badge badge-confidence ${e.confidence || ''}">${t(e.confidence || '')}</span>
      </div>
      ${summary ? `<div class="entry-summary">${esc(summary)}</div>` : ''}
    </a>
  </article>`;
}

function openModal(id, options = {}) {
  const fallback = entries.find(x => x.id === id);
  if (!fallback) {
    if (!options.push) clearStationURL();
    return;
  }

  activeModalId = id;
  if (modalCloseTimer) {
    clearTimeout(modalCloseTimer);
    modalCloseTimer = null;
  }
  if (options.push !== false) setStationURL(id);

  document.getElementById('modal-content').innerHTML = `
    <h2>${esc(fallback.name)}</h2>
    <div class="modal-subtitle">${t('loadingEntry')}</div>
    <div class="modal-loading"></div>
  `;
  const overlay = document.getElementById('modal-overlay');
  overlay.classList.remove('closing');
  overlay.classList.add('active');
  document.body.style.overflow = 'hidden';
  document.title = modalDocumentTitle(fallback.name);

  loadFullEntry(id)
    .then(entry => {
      if (activeModalId === id) renderModalEntry(entry);
    })
    .catch(() => {
      if (activeModalId !== id) return;
      document.getElementById('modal-content').innerHTML = `
        <h2>${esc(fallback.name)}</h2>
        <div class="modal-subtitle">${esc(entryCardSummary(fallback) || '')}</div>
      `;
    });
}

async function loadFullEntry(id) {
  const all = await loadFullEntries();
  return all.find(x => x.id === id);
}

async function loadFullEntries() {
  if (fullEntries) return fullEntries;
  if (fullEntriesPromise) return fullEntriesPromise;

  fullEntriesPromise = new Promise((resolve, reject) => {
    const useGlobalData = () => {
      if (typeof ENTRIES_DATA === 'undefined') return false;
      fullEntries = ENTRIES_DATA.filter(e => STATION_CATEGORIES.has(e._category));
      resolve(fullEntries);
      return true;
    };

    if (useGlobalData()) return;

    loadScriptOnce('data/entries.js', 'entries-full-script')
      .then(() => {
        if (!useGlobalData()) reject(new Error('Full entries data was not available'));
      })
      .catch(reject);
  });

  return fullEntriesPromise;
}

function loadScriptOnce(src, id) {
  return new Promise((resolve, reject) => {
    const existing = document.getElementById(id);
    if (existing) {
      if (existing.dataset.loaded === 'true') resolve();
      else {
        existing.addEventListener('load', () => resolve(), { once: true });
        existing.addEventListener('error', reject, { once: true });
      }
      return;
    }

    const script = document.createElement('script');
    script.id = id;
    script.src = assetURL(src);
    script.onload = () => {
      script.dataset.loaded = 'true';
      resolve();
    };
    script.onerror = reject;
    document.body.appendChild(script);
  });
}

function assetURL(src) {
  if (!src || /^(https?:)?\/\//.test(src) || src.startsWith('data:')) return src;
  if (src.startsWith('/')) return src;
  return APP_ROOT_PATH + src.replace(/^\/+/, '');
}

function renderModalEntry(e) {
  if (!e) return;
  const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';
  const hasContent = e.has_content_entry === 'true';
  const story = entryStory(e);

  let details = '';
  const add = (label, value) => {
    if (value) details += `<div class="detail-label">${label}</div><div class="detail-value">${value}</div>`;
  };

  add(t('namedAfter'), esc((lang === 'es' && e.named_after_es) ? e.named_after_es : (e.named_after || '')));
  if (e.etymology_type === 'person') {
    const gender = e.person_gender === 'M' ? t('male') : e.person_gender === 'F' ? t('female') : '';
    if (gender) add(t('gender'), gender);
    if (e.person_birth_year || e.person_death_year)
      add(t('lived'), `${e.person_birth_year || '?'}\u2013${e.person_death_year || '?'}`);
    add(t('profession'), esc(trField(e.person_profession || '', PROF_ES)));
    add(t('nationality'), esc(trField(e.person_nationality || '', NAT_ES)));
  }
  add(t('district'), esc(e.district || ''));
  add(t('neighbourhood'), esc(e.neighbourhood || ''));
  if (e.line) add(t('lines'), esc(e.line));
  if (e.opening_year) add(t('opened'), e.opening_year);
  if (e.naming_date) add(t('namedIn'), e.naming_date);
  if (e.previous_names) add(t('formerNames'), esc(e.previous_names));
  if (e.operator) {
    const opEs = {'Metro de Madrid':'Metro de Madrid','Renfe Cercanias':'Renfe Cercanías','CRTM':'CRTM','Metro Ligero Madrid':'Metro Ligero Madrid','Metro Ligero Oeste':'Metro Ligero Oeste','Tranvia de Parla':'Tranvía de Parla'};
    add(t('operator'), esc(lang === 'es' ? (opEs[e.operator] || e.operator) : e.operator));
  }
  if (e.municipality) add(t('municipality'), esc(e.municipality));
  if (e.latitude && e.longitude) {
    const gmapsUrl = e.gmaps_url ||
      `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent((e._category === 'cercanias' ? 'Cercanías' : e._category === 'metro_ligero' ? 'Metro Ligero' : 'Metro') + ' ' + e.name + ', Madrid, Spain')}`;
    add(t('coordinates'),
      `<a class="source-link" href="https://www.openstreetmap.org/?mlat=${e.latitude}&mlon=${e.longitude}#map=16/${e.latitude}/${e.longitude}" target="_blank" rel="noopener">OpenStreetMap</a> · ` +
      `<a class="source-link" href="${gmapsUrl}" target="_blank" rel="noopener">Google Maps</a>`);
  }

  const sources = formatEntrySources(e);
  const wikidata = e.named_after_wikidata
    ? `<a class="wikidata-link" href="https://www.wikidata.org/wiki/${e.named_after_wikidata}" target="_blank" rel="noopener">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M1 2h2v12H1zm3 0h1v12H4zm7 0h1v12h-1zm3 0h2v12h-2zM6 2h1v4H6zm0 5h1v3H6zm0 4h1v1H6zm3-9h1v1H9zm0 2h1v3H9zm0 4h1v4H9z"/></svg>
        ${e.named_after_wikidata}
       </a>` : '';

  document.getElementById('modal-content').innerHTML = `
    <h2>${esc(e.name)}</h2>
    <div class="modal-subtitle">${catLabel}${e.operator ? ' \u00b7 ' + esc(e.operator) : ''}</div>
    <div class="modal-badges">
      <span class="badge badge-type ${etType}">${t(etType)}</span>
      <span class="badge badge-confidence ${e.confidence || ''}">${t(e.confidence || '')}</span>
    </div>
    <div class="etymology-summary ${hasContent ? 'markdown-content' : ''}">
      ${hasContent ? markdownToHTML(story) : formatParagraphs(story)}
    </div>
    ${details ? `<div class="detail-grid">${details}</div>` : ''}
    ${wikidata}
    <div class="sources"><strong>${t('sources')}</strong><br>${sources}</div>
  `;

  document.getElementById('modal-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
  document.title = modalDocumentTitle(e.name);
}

function closeModal(options = {}) {
  const overlay = document.getElementById('modal-overlay');
  if (!overlay.classList.contains('active') || overlay.classList.contains('closing')) return;

  activeModalId = '';
  document.title = t('pageTitle');
  if (options.updateURL !== false) clearStationURL();

  overlay.classList.add('closing');
  modalCloseTimer = setTimeout(() => {
    overlay.classList.remove('active', 'closing');
    document.body.style.overflow = '';
    modalCloseTimer = null;
  }, 180);
}

function formatSources(src) {
  if (!src) return '<em>—</em>';
  return src.split(';').map(s => {
    s = s.trim(); if (!s) return '';
    const urlMatch = s.match(/([\w.-]+\.\w{2,}\/[^\s)]*)/);
    if (urlMatch) {
      const url = urlMatch[1];
      return s.replace(url, `<a class="source-link" href="https://${url}" target="_blank" rel="noopener">${url}</a>`);
    }
    return esc(s);
  }).filter(Boolean).join('<br>');
}

function localized(e, base) {
  return e[`${base}_${lang}`] || e[`${base}_en`] || e[`${base}_es`] || '';
}

function legacySummary(e) {
  return (lang === 'es' && e.etymology_summary_es) ? e.etymology_summary_es : (e.etymology_summary || '');
}

function entryCardSummary(e) {
  return localized(e, 'content_summary_short') || legacySummary(e);
}

function entryStory(e) {
  return localized(e, 'content_story') || localized(e, 'content_summary') || legacySummary(e);
}

function formatEntrySources(e) {
  if (Array.isArray(e.sources_structured) && e.sources_structured.length) {
    return e.sources_structured.map(source => {
      const title = esc(source.title || source.url || 'Source');
      const relevance = esc(source[`relevance_${lang}`] || source.relevance_en || source.relevance_es || '');
      const type = source.type ? `<span class="source-type">${esc(source.type)}</span>` : '';
      const titleHTML = source.url
        ? `<a class="source-link source-title" href="${escAttr(source.url)}" target="_blank" rel="noopener">${title}</a>`
        : `<span class="source-title">${title}</span>`;
      return `<div class="source-item">${titleHTML}${type}${relevance ? `<div class="source-relevance">${relevance}</div>` : ''}</div>`;
    }).join('');
  }
  return formatSources(e.source || '');
}

function inlineMarkdown(text) {
  return esc(text)
    .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, (_m, label, url) =>
      `<a class="source-link" href="${escAttr(url)}" target="_blank" rel="noopener">${label}</a>`)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}

function markdownToHTML(text) {
  if (!text) return '';
  const blocks = text.replace(/\r\n/g, '\n').trim().split(/\n{2,}/);
  return blocks.map(block => {
    const lines = block.split('\n').map(line => line.trim()).filter(Boolean);
    if (!lines.length) return '';
    const heading = lines[0].match(/^(#{2,4})\s+(.+)$/);
    if (heading && lines.length === 1) {
      const level = Math.min(4, heading[1].length + 1);
      return `<h${level}>${inlineMarkdown(heading[2])}</h${level}>`;
    }
    if (lines.every(line => /^[-*]\s+/.test(line))) {
      return `<ul>${lines.map(line => `<li>${inlineMarkdown(line.replace(/^[-*]\s+/, ''))}</li>`).join('')}</ul>`;
    }
    return `<p>${inlineMarkdown(lines.join(' '))}</p>`;
  }).join('');
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function escAttr(s) {
  return esc(String(s || '')).replace(/"/g, '&quot;');
}

function formatLineList(value) {
  return String(value || '').split(';').map(v => v.trim()).filter(Boolean).join(', ');
}

// Field value translations for ES mode
const PROF_ES = {
  'architect':'arquitecto','painter':'pintor','poet':'poeta','writer':'escritor',
  'novelist':'novelista','composer':'compositor','politician':'político',
  'military':'militar','king':'rey','queen':'reina','monarch':'monarca',
  'empress':'emperatriz','explorer':'explorador','navigator':'navegante',
  'conquistador':'conquistador','general':'general','regent':'regente',
  'senator':'senador','lawyer':'abogado','jurist':'jurista','physician':'médico',
  'scientist':'científico','historian':'historiador','journalist':'periodista',
  'playwright':'dramaturgo','sculptor':'escultor','engineer':'ingeniero',
  'inventor':'inventor','aviator':'aviador','saint':'santo','friar':'fraile',
  'priest':'sacerdote','bishop':'obispo','deacon':'diácono','martyr':'mártir',
  'nurse':'enfermero/a','educator':'educador/a','pedagogue':'pedagogo/a','teacher':'maestro/a',
  'urban planner':'urbanista','urbanist':'urbanista','developer':'promotor',
  'landowner':'terrateniente','merchant':'comerciante','nobleman':'noble',
  'aristocrat':'aristócrata','prince':'príncipe','princess':'princesa',
  'military officer':'oficial militar','military commander':'comandante militar',
  'prime minister':'presidente del gobierno','mayor':'alcalde','minister':'ministro',
  'football club president':'presidente de club de fútbol',
  'flamenco guitarist':'guitarrista flamenco','guitarist':'guitarrista',
  'musician':'músico','actor':'actor','literary critic':'crítico literario',
  'philologist':'filólogo','endocrinologist':'endocrinólogo','hygienist':'higienista',
  'biochemist':'bioquímico','neuroscientist':'neurocientífico',
  'Nobel laureate':'Premio Nobel','satirist':'satírico',
  'INI president':'presidente del INI','naval engineer':'ingeniero naval',
  'businesswoman':'empresaria','fashion designer':'diseñadora de moda',
  'philanthropist':'filántropo','financier':'financiero',
  'real estate developer':'promotor inmobiliario','orator':'orador',
  'hospital founder':'fundador de hospital','councillor':'concejal',
  'governor':'gobernador','ceramics historian':'historiador de cerámica',
  'seamstress':'costurera','mathematician':'matemático',
  'royal':'real','corregidor (chief magistrate)':'corregidor','military; regent':'militar; regente',
};
const NAT_ES = {
  'Spanish':'español/a','Italian':'italiano/a','French':'francés/a',
  'English':'inglés/a','Nicaraguan':'nicaragüense','Roman':'romano/a',
  'Roman (Gallo-Roman)':'romano (galorromano)','Portuguese/Spanish':'portugués/español',
  'Genoese/Spanish':'genovés/español','Spanish (Castilian-Leonese)':'español (castellano-leonés)',
  'Spanish (Basque)':'español (vasco)',
};

function trField(value, dict) {
  if (lang !== 'es' || !value) return value;
  // Translate semicolon-separated values (e.g., "painter; sculptor")
  return value.split(';').map(v => {
    v = v.trim();
    return dict[v] || dict[v.toLowerCase()] || v;
  }).join('; ');
}

function formatParagraphs(text) {
  if (!text || text.length < 300) return esc(text);
  // Split into sentences and group into paragraphs of ~3 sentences
  const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
  if (sentences.length <= 3) return '<p>' + esc(text) + '</p>';
  const paragraphs = [];
  for (let i = 0; i < sentences.length; i += 3) {
    paragraphs.push(esc(sentences.slice(i, i + 3).join('').trim()));
  }
  return paragraphs.map(p => '<p>' + p + '</p>').join('');
}

// ---- MAP ----
const TYPE_COLORS = {
  person: '#6d28d9', place: '#1d4ed8', descriptive: '#047857',
  historical: '#b45309', religious: '#be185d', event: '#dc2626',
  occupation: '#4338ca', mythological: '#7e22ce', unknown: '#737373'
};

function setView(view) {
  currentView = view === 'map' ? 'map' : 'list';
  document.getElementById('btn-list').classList.toggle('active', currentView === 'list');
  document.getElementById('btn-map').classList.toggle('active', currentView === 'map');
  document.getElementById('entries').hidden = currentView !== 'list';
  document.getElementById('map-container').hidden = currentView !== 'map';
  if (currentView === 'map') renderMapView(getFiltered());
  pushURL();
}

function renderMapView(filtered) {
  const prompt = document.getElementById('map-prompt');
  const mapEl = document.getElementById('map');
  if (!prompt || !mapEl) return;

  if (map) {
    prompt.hidden = true;
    mapEl.hidden = false;
    updateMap(filtered);
    setTimeout(() => map.invalidateSize(), 100);
    return;
  }

  prompt.hidden = false;
  prompt.innerHTML = `<div class="map-loading">${t('loadingMap')}</div>`;
  mapEl.hidden = true;

  ensureMapAssets()
    .then(() => {
      if (currentView !== 'map') return;
      prompt.hidden = true;
      mapEl.hidden = false;
      if (!map) initMap();
      updateMap(filtered);
      setTimeout(() => map.invalidateSize(), 100);
    })
    .catch(() => {
      prompt.hidden = false;
      prompt.innerHTML = `<div class="map-empty"><h2>${t('narrowMapTitle')}</h2><p>${t('narrowMapBody')}</p></div>`;
      mapEl.hidden = true;
    });
}

function mapPromptHTML(filtered) {
  const broad = !hasMapNarrowing();
  const title = broad ? t('mapPromptTitle') : t('narrowMapTitle');
  const body = broad ? t('mapPromptBody') : `${t('narrowMapBody')} ${t('showing')} ${filtered.length} ${t('entries')}.`;
  const buttons = lineOptionsForPrompt()
    .map(line => `<button class="map-line-btn" onclick="chooseLine('${escAttr(line)}')">${esc(line)}</button>`)
    .join('');

  return `
    <div class="map-empty">
      <h2>${title}</h2>
      <p>${body}</p>
      <div class="map-line-grid">${buttons}</div>
    </div>
  `;
}

function lineOptionsForPrompt() {
  const lines = new Set();
  entries.forEach(e => {
    if (activeCategory && e._category !== activeCategory) return;
    if (e.line) e.line.split(';').forEach(l => lines.add(l.trim()));
  });
  return sortLines([...lines]);
}

function chooseLine(line) {
  activeLine = line;
  document.getElementById('filter-line').value = line;
  filtersChanged();
  setView('map');
}

function ensureMapAssets() {
  if (mapAssetsPromise) return mapAssetsPromise;
  mapAssetsPromise = Promise.all([
    loadStylesheetOnce('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css', 'leaflet-css'),
    loadScriptOnce('https://unpkg.com/leaflet@1.9.4/dist/leaflet.js', 'leaflet-script'),
    loadScriptOnce('data/line_orders.js', 'line-orders-script'),
  ]).then(() => {
    if (typeof L === 'undefined') throw new Error('Leaflet was not available');
  });
  return mapAssetsPromise;
}

function loadStylesheetOnce(href, id) {
  return new Promise((resolve, reject) => {
    const existing = document.getElementById(id);
    if (existing) {
      resolve();
      return;
    }

    const link = document.createElement('link');
    link.id = id;
    link.rel = 'stylesheet';
    link.href = href;
    link.onload = resolve;
    link.onerror = reject;
    document.head.appendChild(link);
  });
}

function initMap() {
  map = L.map('map', {
    zoomControl: true,
    scrollWheelZoom: true,
  }).setView([40.42, -3.70], 12);
  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> &copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 19
  }).addTo(map);
  lineLayer = L.layerGroup().addTo(map);
  markers = L.layerGroup().addTo(map);
  map.on('zoomend', updateMarkerScale);
}

function stationIcon(color) {
  const size = markerSizeForZoom(map ? map.getZoom() : 9);
  return L.divIcon({
    className: 'map-marker',
    html: `<div class="station-dot" style="width:${size}px;height:${size}px;background:${color}"></div>`,
    iconSize: [size, size],
    iconAnchor: [size / 2, size / 2]
  });
}

function stationMarkerColor(e) {
  const lines = (e.line || '').split(';').map(l => l.trim()).filter(Boolean);
  if (activeLine && lines.includes(activeLine)) {
    return LINE_COLORS[activeLine] || '#8a9690';
  }
  if (lines.length === 1) {
    return LINE_COLORS[lines[0]] || TYPE_COLORS[e.etymology_type] || '#8a9690';
  }
  return '#9aa39d';
}

function updateMap(filtered) {
  if (!markers || !lineLayer) return;
  markers.clearLayers();
  lineLayer.clearLayers();
  const bounds = [];
  const linesToDraw = activeLine ? [activeLine] : [];

  if (!activeLine) {
    const allLines = new Set();
    filtered.forEach(e => {
      if (e.line) e.line.split(';').forEach(l => allLines.add(l.trim()));
    });
    Object.entries(LINE_ALIAS_PARENTS).forEach(([alias, parent]) => {
      if (allLines.has(parent)) allLines.delete(alias);
    });
    linesToDraw.push(...allLines);
  }

  // Build coord lookup from ALL entries, keyed by name → array of {coords, lines}
  // This handles name collisions (e.g. "Reyes Católicos" in Line 10 vs Tranvía de Parla)
  const stationCoordsByName = {};
  entries.forEach(e => {
    if (e.latitude && e.longitude) {
      if (!stationCoordsByName[e.name]) stationCoordsByName[e.name] = [];
      stationCoordsByName[e.name].push({
        coords: [parseFloat(e.latitude), parseFloat(e.longitude)],
        lines: (e.line || '').split(';').map(l => l.trim())
      });
    }
  });

  function getStationCoords(name, forLine) {
    const candidates = stationCoordsByName[name];
    if (!candidates) return null;
    if (candidates.length === 1) return candidates[0].coords;
    // Prefer the entry whose line field includes the line being drawn
    const match = candidates.find(c => c.lines.includes(forLine));
    return match ? match.coords : candidates[0].coords;
  }

  linesToDraw.forEach(lineName => {
    if (typeof LINE_ORDERS === 'undefined' || !LINE_ORDERS[lineName]) return;
    const rawOrder = LINE_ORDERS[lineName];
    const branches = Array.isArray(rawOrder[0]) ? rawOrder : [rawOrder];
    branches.forEach(order => {
      const coords = [];
      order.forEach(name => {
        const c = getStationCoords(name, lineName);
        if (c) coords.push(c);
      });
      if (LOOP_LINES.has(lineName) && coords.length >= 3) {
        coords.push(coords[0]);
      }
      if (coords.length >= 2) {
        const color = LINE_COLORS[lineName] || '#999';
        L.polyline(coords, { color, weight: 3.5, opacity: 0.6 }).addTo(lineLayer);
      }
    });
  });

  // Draw station markers
  filtered.forEach(e => {
    if (!e.latitude || !e.longitude) return;
    const lat = parseFloat(e.latitude);
    const lng = parseFloat(e.longitude);
    if (isNaN(lat) || isNaN(lng)) return;

    const color = stationMarkerColor(e);

    const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
    const rawSummary = entryCardSummary(e);
    const summary = rawSummary ? esc(rawSummary).substring(0, 180) + (rawSummary.length > 180 ? '...' : '') : '';
    const lineMeta = e.line ? formatLineList(e.line) : '';
    const href = stationURL(e.id);
    const popup = `
      <div class="map-popup-name">${esc(e.name)}</div>
      <div class="map-popup-meta">${catLabel}${lineMeta ? ' · ' + esc(lineMeta) : ''}</div>
      <div class="map-popup-summary">${summary}</div>
      <a class="map-popup-link" href="${escAttr(href)}" onclick="event.preventDefault(); closePopupsAndOpen('${e.id}')">${t('readMore')}</a>
    `;

    markers.addLayer(L.marker([lat, lng], {
      icon: stationIcon(color),
      stationColor: color
    }).bindPopup(popup));
    bounds.push([lat, lng]);
  });

  if (bounds.length > 0) map.fitBounds(bounds, { padding: [20, 20], maxZoom: activeLine ? 13 : 14 });
  updateMarkerScale();
}

function markerSizeForZoom(zoom) {
  if (zoom <= 9) return 4;
  if (zoom === 10) return 5;
  if (zoom === 11) return 6;
  if (zoom === 12) return 7;
  if (zoom === 13) return 8;
  return 9;
}

function updateMarkerScale() {
  if (!map || !markers) return;
  const size = markerSizeForZoom(map.getZoom());
  const ringOpacity = size <= 5 ? '0.22' : '0.38';
  const mapEl = document.getElementById('map');
  if (mapEl) mapEl.style.setProperty('--station-dot-ring-opacity', ringOpacity);
  markers.eachLayer(marker => {
    const color = marker.options.stationColor;
    if (color) marker.setIcon(stationIcon(color));
  });
}

function closePopupsAndOpen(id) {
  map.closePopup();
  openModal(id);
}

init();
