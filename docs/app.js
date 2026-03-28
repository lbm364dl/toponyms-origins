let entries = [];
let activeCategory = '';
let map = null;
let markers = null;
let currentView = 'list';

const CATEGORY_LABELS = {
  metro: 'Metro', cercanias: 'Cercanias', metro_ligero: 'ML / Tranvia',
  districts: 'District', neighbourhoods: 'Neighbourhood',
  plazas_parks: 'Plaza / Park', streets: 'Street'
};
const CATEGORY_ICONS = {
  metro: 'M', cercanias: 'C', metro_ligero: 'ML',
  districts: 'D', neighbourhoods: 'B',
  plazas_parks: 'P', streets: 'St'
};

async function init() {
  const STATION_CATEGORIES = new Set(['metro', 'cercanias', 'metro_ligero']);

  // Try fetch first (works on http://), fall back to inline script (works on file://)
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
  renderStats();
  render();

  document.getElementById('search').addEventListener('input', render);
  document.getElementById('filter-type').addEventListener('change', render);
  document.getElementById('filter-confidence').addEventListener('change', render);

  // Category pill buttons
  document.querySelectorAll('#category-pills .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#category-pills .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.dataset.v;
      render();
    });
  });

  // Modal
  document.getElementById('modal-overlay').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeModal();
  });
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

  // View toggle
  document.getElementById('btn-list').addEventListener('click', () => setView('list'));
  document.getElementById('btn-map').addEventListener('click', () => setView('map'));
}

function renderStats() {
  const v = entries.filter(e => e.confidence === 'verified').length;
  const p = entries.filter(e => e.confidence === 'probable').length;
  const u = entries.filter(e => e.confidence === 'uncertain').length;
  const pct = Math.round(v / entries.length * 100);
  document.getElementById('stats').innerHTML = `
    <div class="stat"><span class="stat-value">${entries.length}</span><span class="stat-label">Places</span></div>
    <div class="stat"><span class="stat-value">${v}</span><span class="stat-label">Verified</span></div>
    <div class="stat"><span class="stat-value">${p}</span><span class="stat-label">Probable</span></div>
    <div class="stat"><span class="stat-value">${u}</span><span class="stat-label">Uncertain</span></div>
  `;
}

function getFiltered() {
  const q = document.getElementById('search').value.toLowerCase();
  const typ = document.getElementById('filter-type').value;
  const conf = document.getElementById('filter-confidence').value;
  return entries.filter(e => {
    if (activeCategory && e._category !== activeCategory) return false;
    if (typ && e.etymology_type !== typ) return false;
    if (conf && e.confidence !== conf) return false;
    if (q) {
      const haystack = [e.name, e.etymology_summary, e.named_after, e.etymology_type,
        e.person_profession, e.district, e.neighbourhood, e.id].filter(Boolean).join(' ').toLowerCase();
      return haystack.includes(q);
    }
    return true;
  });
}

function render() {
  const filtered = getFiltered();
  const countEl = document.getElementById('result-count');
  countEl.textContent = filtered.length === entries.length
    ? `${entries.length} entries`
    : `${filtered.length} of ${entries.length} entries`;

  const container = document.getElementById('entries');
  const limit = 300;
  const show = filtered.slice(0, limit);
  container.innerHTML = show.map(cardHTML).join('');
  if (filtered.length > limit) {
    container.insertAdjacentHTML('beforeend',
      `<div style="grid-column:1/-1;text-align:center;padding:24px;color:var(--text-muted);font-size:0.85rem">
        Showing ${limit} of ${filtered.length}. Refine your search to see more.
      </div>`);
  }
}

function cardHTML(e) {
  const catLabel = CATEGORY_LABELS[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';
  const summary = e.etymology_summary || '';
  const district = e.district ? e.district : '';
  const line = e.line ? `Line ${e.line}` : '';
  const meta = [catLabel, district, line].filter(Boolean).join(' \u00b7 ');

  return `<article class="entry-card" onclick="openModal('${e.id}')">
    <div class="entry-header">
      <span class="entry-name">${esc(e.name)}</span>
    </div>
    <div class="entry-meta">${esc(meta)}</div>
    <div class="entry-badges">
      <span class="badge badge-type ${etType}">${etType}</span>
      <span class="badge badge-confidence ${e.confidence || ''}">${e.confidence || ''}</span>
    </div>
    ${summary ? `<div class="entry-summary">${esc(summary)}</div>` : ''}
  </article>`;
}

function openModal(id) {
  const e = entries.find(x => x.id === id);
  if (!e) return;
  const catLabel = CATEGORY_LABELS[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';

  let details = '';
  const add = (label, value) => {
    if (value) details += `<div class="detail-label">${label}</div><div class="detail-value">${value}</div>`;
  };

  add('Named after', esc(e.named_after || ''));
  if (e.etymology_type === 'person') {
    const gender = e.person_gender === 'M' ? 'Male' : e.person_gender === 'F' ? 'Female' : '';
    if (gender) add('Gender', gender);
    if (e.person_birth_year || e.person_death_year)
      add('Lived', `${e.person_birth_year || '?'}\u2013${e.person_death_year || '?'}`);
    add('Profession', esc(e.person_profession || ''));
    add('Nationality', esc(e.person_nationality || ''));
  }
  add('District', esc(e.district || ''));
  add('Neighbourhood', esc(e.neighbourhood || ''));
  if (e.line) add('Line(s)', esc(e.line));
  if (e.opening_year) add('Opened', e.opening_year);
  if (e.naming_date) add('Named in', e.naming_date);
  if (e.previous_names) add('Former names', esc(e.previous_names));
  if (e.operator) add('Operator', esc(e.operator));
  if (e.municipality) add('Municipality', esc(e.municipality));
  if (e.latitude && e.longitude) {
    add('Coordinates', `<a class="source-link" href="https://www.openstreetmap.org/?mlat=${e.latitude}&mlon=${e.longitude}#map=16/${e.latitude}/${e.longitude}" target="_blank" rel="noopener">${e.latitude}, ${e.longitude}</a>`);
  }

  const sources = formatSources(e.source || '');
  const wikidata = e.named_after_wikidata
    ? `<a class="wikidata-link" href="https://www.wikidata.org/wiki/${e.named_after_wikidata}" target="_blank" rel="noopener">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M1 2h2v12H1zm3 0h1v12H4zm7 0h1v12h-1zm3 0h2v12h-2zM6 2h1v4H6zm0 5h1v3H6zm0 4h1v1H6zm3-9h1v1H9zm0 2h1v3H9zm0 4h1v4H9z"/></svg>
        ${e.named_after_wikidata}
       </a>`
    : '';

  document.getElementById('modal-content').innerHTML = `
    <h2>${esc(e.name)}</h2>
    <div class="modal-subtitle">${catLabel}${e.operator ? ' \u00b7 ' + esc(e.operator) : ''}</div>
    <div class="modal-badges">
      <span class="badge badge-type ${etType}">${etType}</span>
      <span class="badge badge-confidence ${e.confidence || ''}">${e.confidence || ''}</span>
    </div>
    <div class="etymology-summary">${esc(e.etymology_summary || 'No etymology summary available.')}</div>
    ${details ? `<div class="detail-grid">${details}</div>` : ''}
    ${wikidata}
    <div class="sources">
      <strong>Sources</strong><br>${sources}
    </div>
  `;

  document.getElementById('modal-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('modal-overlay').classList.remove('active');
  document.body.style.overflow = '';
}

function formatSources(src) {
  if (!src) return '<em>None listed</em>';
  return src.split(';').map(s => {
    s = s.trim();
    if (!s) return '';
    const urlMatch = s.match(/([\w.-]+\.\w{2,}\/[^\s)]*)/);
    if (urlMatch) {
      const url = urlMatch[1];
      const display = s.replace(url,
        `<a class="source-link" href="https://${url}" target="_blank" rel="noopener">${url}</a>`);
      return display;
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
}

function updateMap() {
  if (!markers) return;
  markers.clearLayers();
  const filtered = getFiltered();
  const bounds = [];

  filtered.forEach(e => {
    if (!e.latitude || !e.longitude) return;
    const lat = parseFloat(e.latitude);
    const lng = parseFloat(e.longitude);
    if (isNaN(lat) || isNaN(lng)) return;

    const color = TYPE_COLORS[e.etymology_type] || '#737373';
    const icon = L.divIcon({
      className: 'map-marker',
      html: `<div style="width:10px;height:10px;border-radius:50%;background:${color};border:2px solid white;box-shadow:0 1px 3px rgba(0,0,0,0.3)"></div>`,
      iconSize: [14, 14],
      iconAnchor: [7, 7]
    });

    const catLabel = CATEGORY_LABELS[e._category] || e._category;
    const summary = e.etymology_summary ? esc(e.etymology_summary).substring(0, 180) + '...' : '';
    const popup = `
      <div class="map-popup-name">${esc(e.name)}</div>
      <div class="map-popup-meta">${catLabel}${e.line ? ' · Line ' + e.line : ''}</div>
      <div class="map-popup-summary">${summary}</div>
      <div class="map-popup-link" onclick="closePopupsAndOpen('${e.id}')">Read full etymology →</div>
    `;

    const marker = L.marker([lat, lng], { icon }).bindPopup(popup);
    markers.addLayer(marker);
    bounds.push([lat, lng]);
  });

  if (bounds.length > 0) {
    map.fitBounds(bounds, { padding: [30, 30], maxZoom: 14 });
  }
}

function closePopupsAndOpen(id) {
  map.closePopup();
  openModal(id);
}

// Re-render map when filters change
const origRender = render;
render = function() {
  origRender();
  if (currentView === 'map') updateMap();
};

init();
