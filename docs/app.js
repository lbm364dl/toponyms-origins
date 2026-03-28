let entries = [];
let activeCategory = '';
let activeLine = '';
let map = null;
let markers = null;
let lineLayer = null;
let currentView = 'list';
let lang = localStorage.getItem('lang') || 'en';

const CATEGORY_LABELS = {
  en: { metro: 'Metro', cercanias: 'Cercanías', metro_ligero: 'ML / Tranvía' },
  es: { metro: 'Metro', cercanias: 'Cercanías', metro_ligero: 'ML / Tranvía' }
};

const I18N = {
  en: {
    title: 'Madrid<br>Toponymy',
    subtitle: 'An etymological atlas of 390 station names — Metro, Cercanías, Metro Ligero & Tranvía — tracing why each is named the way it is.',
    eyebrow: 'Open dataset',
    searchPlaceholder: 'Search names, etymologies, people, places...',
    allStations: 'All stations', list: 'List', map: 'Map',
    allTypes: 'All types', allConfidence: 'All confidence', allLines: 'All lines',
    person: 'Person', place: 'Place', descriptive: 'Descriptive', historical: 'Historical',
    religious: 'Religious', event: 'Event', occupation: 'Occupation', mythological: 'Mythological', unknown: 'Unknown',
    verified: 'Verified', probable: 'Probable', uncertain: 'Uncertain',
    places: 'Stations', sources: 'Sources', namedAfter: 'Named after',
    gender: 'Gender', male: 'Male', female: 'Female', lived: 'Lived',
    profession: 'Profession', nationality: 'Nationality', district: 'District',
    neighbourhood: 'Neighbourhood', lines: 'Line(s)', opened: 'Opened',
    namedIn: 'Named in', formerNames: 'Former names', operator: 'Operator',
    municipality: 'Municipality', coordinates: 'Coordinates',
    readMore: 'Read full etymology →',
    footer: '390 station etymologies · CC-BY-SA 4.0',
    showing: 'Showing', of: 'of', entries: 'entries',
  },
  es: {
    title: 'Toponimia<br>de Madrid',
    subtitle: 'Un atlas etimológico de 390 nombres de estaciones — Metro, Cercanías, Metro Ligero y Tranvía — descubriendo el origen de cada nombre.',
    eyebrow: 'Datos abiertos',
    searchPlaceholder: 'Buscar nombres, etimologías, personas, lugares...',
    allStations: 'Todas', list: 'Lista', map: 'Mapa',
    allTypes: 'Todos los tipos', allConfidence: 'Toda confianza', allLines: 'Todas las líneas',
    person: 'Persona', place: 'Lugar', descriptive: 'Descriptivo', historical: 'Histórico',
    religious: 'Religioso', event: 'Evento', occupation: 'Oficio', mythological: 'Mitológico', unknown: 'Desconocido',
    verified: 'Verificado', probable: 'Probable', uncertain: 'Incierto',
    places: 'Estaciones', sources: 'Fuentes', namedAfter: 'Nombrado por',
    gender: 'Género', male: 'Hombre', female: 'Mujer', lived: 'Vivió',
    profession: 'Profesión', nationality: 'Nacionalidad', district: 'Distrito',
    neighbourhood: 'Barrio', lines: 'Línea(s)', opened: 'Inauguración',
    namedIn: 'Nombrado en', formerNames: 'Nombres anteriores', operator: 'Operador',
    municipality: 'Municipio', coordinates: 'Coordenadas',
    readMore: 'Leer etimología completa →',
    footer: '390 etimologías de estaciones · CC-BY-SA 4.0',
    showing: 'Mostrando', of: 'de', entries: 'entradas',
  }
};

function t(key) { return I18N[lang][key] || I18N.en[key] || key; }

const LINE_COLORS = {
  '1':'#38a3dc','2':'#d8232a','3':'#ffd520','4':'#944735','5':'#96bf0d',
  '6':'#9ba2a5','7':'#f6a800','8':'#ea6da8','9':'#a3228d','10':'#064480',
  '11':'#2a993c','12':'#a69938','R':'#003da5',
  'ML1':'#38a3dc','ML2':'#d8232a','ML3':'#ffd520',
  'Tranvia Parla':'#5bc236',
  'C-1':'#62a0d8','C-2':'#00806a','C-3':'#a94394','C-4':'#0071ce',
  'C-5':'#f5d327','C-7':'#e77128','C-8':'#c5c625','C-9':'#8d1c8c','C-10':'#0097b5',
  'C-4b':'#0071ce',
};

async function init() {
  const STATION_CATEGORIES = new Set(['metro', 'cercanias', 'metro_ligero']);
  if (typeof ENTRIES_DATA !== 'undefined') {
    entries = ENTRIES_DATA.filter(e => STATION_CATEGORIES.has(e._category));
  } else {
    try {
      const res = await fetch('data/entries.json');
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
  render();
  // Default to map view
  setView('map');

  document.getElementById('search').addEventListener('input', render);
  document.getElementById('filter-type').addEventListener('change', render);
  document.getElementById('filter-confidence').addEventListener('change', render);
  document.getElementById('filter-line').addEventListener('change', function() {
    activeLine = this.value;
    render();
  });

  document.querySelectorAll('#category-pills .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#category-pills .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.dataset.v;
      render();
    });
  });

  document.getElementById('modal-overlay').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeModal();
  });
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

  document.getElementById('btn-list').addEventListener('click', () => setView('list'));
  document.getElementById('btn-map').addEventListener('click', () => setView('map'));
  document.getElementById('lang-toggle').addEventListener('click', toggleLang);
}

function toggleLang() {
  lang = lang === 'en' ? 'es' : 'en';
  localStorage.setItem('lang', lang);
  applyLang();
  renderStats();
  render();
}

function applyLang() {
  document.getElementById('lang-toggle').textContent = lang === 'en' ? 'ES' : 'EN';
  document.querySelector('.hero-eyebrow').textContent = t('eyebrow');
  document.querySelector('header h1').innerHTML = t('title');
  document.querySelector('.subtitle').textContent = t('subtitle');
  document.getElementById('search').placeholder = t('searchPlaceholder');
  document.querySelector('[data-v=""]').textContent = t('allStations');
  document.getElementById('btn-list').lastChild.textContent = ' ' + t('list');
  document.getElementById('btn-map').lastChild.textContent = ' ' + t('map');
  document.querySelector('.footer-note').textContent = t('footer');

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
  const sorted = [...lines].sort((a, b) => {
    const na = parseFloat(a.replace(/\D/g,'')) || 999;
    const nb = parseFloat(b.replace(/\D/g,'')) || 999;
    return na - nb || a.localeCompare(b);
  });
  const sel = document.getElementById('filter-line');
  sel.innerHTML = `<option value="">${t('allLines')}</option>` +
    sorted.map(l => `<option value="${l}">${l}</option>`).join('');
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
      const haystack = [e.name, e.etymology_summary, e.named_after, e.etymology_type,
        e.person_profession, e.district, e.neighbourhood, e.line, e.id].filter(Boolean).join(' ').toLowerCase();
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
  const limit = 300;
  container.innerHTML = filtered.slice(0, limit).map(cardHTML).join('');
  if (filtered.length > limit) {
    container.insertAdjacentHTML('beforeend',
      `<div style="grid-column:1/-1;text-align:center;padding:24px;color:var(--text-muted);font-size:0.85rem">
        ${t('showing')} ${limit} ${t('of')} ${filtered.length}.
      </div>`);
  }
  if (currentView === 'map') updateMap();
}

function cardHTML(e) {
  const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';
  const summary = (lang === 'es' && e.etymology_summary_es) ? e.etymology_summary_es : (e.etymology_summary || '');
  const district = e.district || '';
  const line = e.line ? `${t('lines').split('(')[0]} ${e.line}` : '';
  const meta = [catLabel, district, line].filter(Boolean).join(' \u00b7 ');

  return `<article class="entry-card" onclick="openModal('${e.id}')">
    <div class="entry-header"><span class="entry-name">${esc(e.name)}</span></div>
    <div class="entry-meta">${esc(meta)}</div>
    <div class="entry-badges">
      <span class="badge badge-type ${etType}">${t(etType)}</span>
      <span class="badge badge-confidence ${e.confidence || ''}">${t(e.confidence || '')}</span>
    </div>
    ${summary ? `<div class="entry-summary">${esc(summary)}</div>` : ''}
  </article>`;
}

function openModal(id) {
  const e = entries.find(x => x.id === id);
  if (!e) return;
  const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';

  let details = '';
  const add = (label, value) => {
    if (value) details += `<div class="detail-label">${label}</div><div class="detail-value">${value}</div>`;
  };

  add(t('namedAfter'), esc(e.named_after || ''));
  if (e.etymology_type === 'person') {
    const gender = e.person_gender === 'M' ? t('male') : e.person_gender === 'F' ? t('female') : '';
    if (gender) add(t('gender'), gender);
    if (e.person_birth_year || e.person_death_year)
      add(t('lived'), `${e.person_birth_year || '?'}\u2013${e.person_death_year || '?'}`);
    add(t('profession'), esc(e.person_profession || ''));
    add(t('nationality'), esc(e.person_nationality || ''));
  }
  add(t('district'), esc(e.district || ''));
  add(t('neighbourhood'), esc(e.neighbourhood || ''));
  if (e.line) add(t('lines'), esc(e.line));
  if (e.opening_year) add(t('opened'), e.opening_year);
  if (e.naming_date) add(t('namedIn'), e.naming_date);
  if (e.previous_names) add(t('formerNames'), esc(e.previous_names));
  if (e.operator) add(t('operator'), esc(e.operator));
  if (e.municipality) add(t('municipality'), esc(e.municipality));
  if (e.latitude && e.longitude) {
    const gmapsUrl = e.gmaps_url ||
      `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent((e._category === 'cercanias' ? 'Cercanías' : e._category === 'metro_ligero' ? 'Metro Ligero' : 'Metro') + ' ' + e.name + ', Madrid, Spain')}`;
    add(t('coordinates'),
      `<a class="source-link" href="https://www.openstreetmap.org/?mlat=${e.latitude}&mlon=${e.longitude}#map=16/${e.latitude}/${e.longitude}" target="_blank" rel="noopener">OpenStreetMap</a> · ` +
      `<a class="source-link" href="${gmapsUrl}" target="_blank" rel="noopener">Google Maps</a>`);
  }

  const sources = formatSources(e.source || '');
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
    <div class="etymology-summary">${esc((lang === 'es' && e.etymology_summary_es) ? e.etymology_summary_es : (e.etymology_summary || ''))}</div>
    ${details ? `<div class="detail-grid">${details}</div>` : ''}
    ${wikidata}
    <div class="sources"><strong>${t('sources')}</strong><br>${sources}</div>
  `;

  document.getElementById('modal-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('modal-overlay').classList.remove('active');
  document.body.style.overflow = '';
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

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

// ---- MAP ----
const TYPE_COLORS = {
  person: '#6d28d9', place: '#1d4ed8', descriptive: '#047857',
  historical: '#b45309', religious: '#be185d', event: '#dc2626',
  occupation: '#4338ca', mythological: '#7e22ce', unknown: '#737373'
};

function setView(view) {
  currentView = view;
  document.getElementById('btn-list').classList.toggle('active', view === 'list');
  document.getElementById('btn-map').classList.toggle('active', view === 'map');
  document.getElementById('entries').style.display = view === 'list' ? '' : 'none';
  document.getElementById('map-container').style.display = view === 'map' ? '' : 'none';
  if (view === 'map') {
    if (!map) initMap();
    updateMap();
    setTimeout(() => map.invalidateSize(), 100);
  }
}

function initMap() {
  map = L.map('map').setView([40.42, -3.70], 12);
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> &copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 19
  }).addTo(map);
  markers = L.layerGroup().addTo(map);
  lineLayer = L.layerGroup().addTo(map);
}

function updateMap() {
  if (!markers) return;
  markers.clearLayers();
  lineLayer.clearLayers();
  const filtered = getFiltered();
  const bounds = [];

  // Draw line traces
  // When a specific line is filtered, only draw THAT line
  // When no line filter, draw all lines that have 2+ visible stations
  const linesToDraw = activeLine ? [activeLine] : [];

  if (!activeLine) {
    // Collect all lines from visible stations
    const allLines = new Set();
    filtered.forEach(e => {
      if (e.line) e.line.split(';').forEach(l => allLines.add(l.trim()));
    });
    linesToDraw.push(...allLines);
  }

  // Build coord lookup from ALL entries (not just filtered) so line traces are complete
  const allStationCoords = {};
  entries.forEach(e => {
    if (e.latitude && e.longitude) {
      allStationCoords[e.name] = [parseFloat(e.latitude), parseFloat(e.longitude)];
    }
  });

  linesToDraw.forEach(lineName => {
    if (typeof LINE_ORDERS === 'undefined' || !LINE_ORDERS[lineName]) return;
    const order = LINE_ORDERS[lineName];
    const coords = [];
    order.forEach(name => {
      if (allStationCoords[name]) coords.push(allStationCoords[name]);
    });
    if (coords.length >= 2) {
      const color = LINE_COLORS[lineName] || '#999';
      L.polyline(coords, { color, weight: 3.5, opacity: 0.6 }).addTo(lineLayer);
    }
  });

  // Draw station markers
  filtered.forEach(e => {
    if (!e.latitude || !e.longitude) return;
    const lat = parseFloat(e.latitude);
    const lng = parseFloat(e.longitude);
    if (isNaN(lat) || isNaN(lng)) return;

    const firstLine = (e.line || '').split(';')[0].trim();
    const color = LINE_COLORS[firstLine] || TYPE_COLORS[e.etymology_type] || '#737373';
    const icon = L.divIcon({
      className: 'map-marker',
      html: `<div style="width:10px;height:10px;border-radius:50%;background:${color};border:2px solid white;box-shadow:0 1px 3px rgba(0,0,0,0.3)"></div>`,
      iconSize: [14, 14], iconAnchor: [7, 7]
    });

    const catLabel = (CATEGORY_LABELS[lang] || CATEGORY_LABELS.en)[e._category] || e._category;
    const rawSummary = (lang === 'es' && e.etymology_summary_es) ? e.etymology_summary_es : (e.etymology_summary || '');
    const summary = rawSummary ? esc(rawSummary).substring(0, 180) + '...' : '';
    const popup = `
      <div class="map-popup-name">${esc(e.name)}</div>
      <div class="map-popup-meta">${catLabel}${e.line ? ' · ' + e.line : ''}</div>
      <div class="map-popup-summary">${summary}</div>
      <div class="map-popup-link" onclick="closePopupsAndOpen('${e.id}')">${t('readMore')}</div>
    `;

    markers.addLayer(L.marker([lat, lng], { icon }).bindPopup(popup));
    bounds.push([lat, lng]);
  });

  if (bounds.length > 0) map.fitBounds(bounds, { padding: [30, 30], maxZoom: 14 });
}

function closePopupsAndOpen(id) {
  map.closePopup();
  openModal(id);
}

init();
