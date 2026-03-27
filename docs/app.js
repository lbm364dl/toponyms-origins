let entries = [];
const CATEGORY_LABELS = {
  metro: 'Metro', cercanias: 'Cercanias', metro_ligero: 'ML / Tranvia',
  districts: 'District', neighbourhoods: 'Neighbourhood',
  plazas_parks: 'Plaza / Park', streets: 'Street'
};

async function init() {
  const res = await fetch('data/entries.json');
  entries = await res.json();
  renderStats();
  render();
  document.getElementById('search').addEventListener('input', render);
  document.getElementById('filter-category').addEventListener('change', render);
  document.getElementById('filter-type').addEventListener('change', render);
  document.getElementById('filter-confidence').addEventListener('change', render);
  document.getElementById('modal-overlay').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeModal();
  });
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
}

function renderStats() {
  const v = entries.filter(e => e.confidence === 'verified').length;
  const p = entries.filter(e => e.confidence === 'probable').length;
  const u = entries.filter(e => e.confidence === 'uncertain').length;
  document.getElementById('stats').innerHTML = `
    <div class="stat"><span class="stat-value">${entries.length}</span><span class="stat-label">Entries</span></div>
    <div class="stat"><span class="stat-value">${v}</span><span class="stat-label">Verified</span></div>
    <div class="stat"><span class="stat-value">${p}</span><span class="stat-label">Probable</span></div>
    <div class="stat"><span class="stat-value">${u}</span><span class="stat-label">Uncertain</span></div>
  `;
}

function getFiltered() {
  const q = document.getElementById('search').value.toLowerCase();
  const cat = document.getElementById('filter-category').value;
  const typ = document.getElementById('filter-type').value;
  const conf = document.getElementById('filter-confidence').value;
  return entries.filter(e => {
    if (cat && e._category !== cat) return false;
    if (typ && e.etymology_type !== typ) return false;
    if (conf && e.confidence !== conf) return false;
    if (q) {
      const haystack = [e.name, e.etymology_summary, e.named_after, e.etymology_type,
        e.person_profession, e.district, e.neighbourhood].filter(Boolean).join(' ').toLowerCase();
      return haystack.includes(q);
    }
    return true;
  });
}

function render() {
  const filtered = getFiltered();
  document.getElementById('result-count').textContent =
    `Showing ${filtered.length} of ${entries.length} entries`;

  const container = document.getElementById('entries');
  if (filtered.length > 200) {
    container.innerHTML = filtered.slice(0, 200).map(cardHTML).join('') +
      `<div style="text-align:center;padding:24px;color:var(--text-muted)">Showing first 200 of ${filtered.length} results. Refine your search.</div>`;
  } else {
    container.innerHTML = filtered.map(cardHTML).join('');
  }
}

function cardHTML(e) {
  const catLabel = CATEGORY_LABELS[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';
  const summary = e.etymology_summary || '';
  return `<div class="entry-card" onclick="openModal('${e.id}')">
    <div class="entry-header">
      <span class="entry-name">${esc(e.name)}</span>
      <div class="entry-badges">
        <span class="badge badge-category">${catLabel}</span>
        <span class="badge badge-type ${etType}">${etType}</span>
        <span class="badge badge-confidence ${e.confidence || ''}">${e.confidence || '?'}</span>
      </div>
    </div>
    ${summary ? `<div class="entry-summary">${esc(summary)}</div>` : ''}
  </div>`;
}

function openModal(id) {
  const e = entries.find(x => x.id === id);
  if (!e) return;
  const catLabel = CATEGORY_LABELS[e._category] || e._category;
  const etType = e.etymology_type || 'unknown';

  let details = '';
  const addDetail = (label, value) => {
    if (value) details += `<div class="detail-label">${label}</div><div class="detail-value">${value}</div>`;
  };

  addDetail('Named after', esc(e.named_after || ''));
  if (e.etymology_type === 'person') {
    addDetail('Gender', e.person_gender === 'M' ? 'Male' : e.person_gender === 'F' ? 'Female' : e.person_gender || '');
    if (e.person_birth_year || e.person_death_year)
      addDetail('Dates', `${e.person_birth_year || '?'} - ${e.person_death_year || '?'}`);
    addDetail('Profession', esc(e.person_profession || ''));
    addDetail('Nationality', esc(e.person_nationality || ''));
  }
  addDetail('District', esc(e.district || ''));
  addDetail('Neighbourhood', esc(e.neighbourhood || ''));
  if (e.line) addDetail('Line(s)', esc(e.line));
  if (e.opening_year) addDetail('Opened', e.opening_year);
  if (e.naming_date) addDetail('Named in', e.naming_date);
  if (e.previous_names) addDetail('Previous names', esc(e.previous_names));
  if (e.municipality) addDetail('Municipality', esc(e.municipality));

  const sources = formatSources(e.source || '');
  const wikidata = e.named_after_wikidata
    ? `<a class="wikidata-link" href="https://www.wikidata.org/wiki/${e.named_after_wikidata}" target="_blank" rel="noopener">Wikidata: ${e.named_after_wikidata}</a>`
    : '';

  document.getElementById('modal-content').innerHTML = `
    <h2>${esc(e.name)}</h2>
    <div class="modal-subtitle">${catLabel}${e.operator ? ' &middot; ' + esc(e.operator) : ''}</div>
    <div class="modal-badges">
      <span class="badge badge-type ${etType}">${etType}</span>
      <span class="badge badge-confidence ${e.confidence || ''}">${e.confidence || '?'}</span>
    </div>
    <div class="etymology-summary">${esc(e.etymology_summary || 'No etymology summary available.')}</div>
    ${details ? `<div class="detail-grid">${details}</div>` : ''}
    ${wikidata}
    <div class="sources">
      <strong>Sources:</strong><br>${sources}
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
  if (!src) return '<em>None</em>';
  return src.split(';').map(s => {
    s = s.trim();
    // If it looks like a URL, make it clickable
    const urlMatch = s.match(/([\w.-]+\.\w{2,}\/\S*)/);
    if (urlMatch) {
      const url = urlMatch[1];
      const display = s.replace(url, `<a class="source-link" href="https://${url}" target="_blank" rel="noopener">${url}</a>`);
      return display;
    }
    return esc(s);
  }).join('<br>');
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

init();
