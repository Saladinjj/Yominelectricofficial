/* ═══════════════════════════════════════════════════════════════
   YOMIN ELECTRIC — products.js  v11.2
   Single-page catalog: sidebar + grid + inline detail panel
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const BUSBAR_FILTER = '__busbar__';
const BUSBAR_PARENT = { id:BUSBAR_FILTER, label:'Busbars', icon:'🔌', tKey:'prod_cat_busbar' };
const BUSBAR_SUBCATS = [
  { id:'Flexible Busbar',              label:'Flexible Busbar',        icon:'〰️', tKey:'prod_cat_flexible_busbar' },
  { id:'Rigid Busbar',                 label:'Rigid Busbar',           icon:'▬', tKey:'prod_cat_rigid_busbar' },
  { id:'Aluminum Busbar',              label:'Aluminum Busbar',        icon:'🔶', tKey:'prod_cat_aluminum_busbar' },
  { id:'Composite Laminated Busbar',   label:'Composite Laminated',    icon:'🧩', tKey:'prod_cat_composite_busbar' },
  { id:'CCS Integrated Busbar',        label:'CCS Integrated',         icon:'🔋', tKey:'prod_cat_ccs_busbar' },
  { id:'Heavy Duty Busbar',            label:'Heavy Duty Busbar',      icon:'⚙️', tKey:'prod_cat_heavy_busbar' },
  { id:'Energy Storage Busbar',        label:'Energy Storage',         icon:'🔋', tKey:'prod_cat_storage_busbar' },
  { id:'Busbar Protection',            label:'Busbar Protection',      icon:'🛡️', tKey:'prod_cat_busbar_protection' },
];
const BUSBAR_SUB_IDS = new Set(BUSBAR_SUBCATS.map(c => c.id));

const CATS = [
  { id:'Energy Meter',                 label:'Energy Meters',          icon:'⚡', tKey:'prod_cat_energy_meter' },
  { id:'Voltage Stabilizer/Regulator', label:'Voltage Stabilizers',    icon:'🔄', tKey:'prod_cat_voltage_stabilizer' },
  { id:'Current Transformer',          label:'Current Transformers',   icon:'🔵', tKey:'prod_cat_current_transformer' },
  { id:'New',                          label:'New Products',           icon:'🆕', tKey:'prod_cat_new' },
  { id:'Screw Machine',                label:'Screw Machines',         icon:'⚙️', tKey:'prod_cat_screw_machine' },
  { id:'Variac/Transformer',           label:'Variac / Transformers',  icon:'🔃', tKey:'prod_cat_variac' },
  { id:'Terminal & Connector',         label:'Terminals & Connectors', icon:'🔩', tKey:'prod_cat_terminal' },
  { id:'Solar/PV Products',            label:'Solar & PV',             icon:'☀️',  tKey:'prod_cat_solar' },
  { id:'Fuse & Protection',            label:'Fuses & Protection',     icon:'⚠️',  tKey:'prod_cat_fuse' },
  { id:'Voltage Protector',            label:'Voltage Protectors',     icon:'🛡️',  tKey:'prod_cat_voltage_protector' },
  { id:'Socket & Wiring',              label:'Sockets & Wiring',       icon:'🔌', tKey:'prod_cat_socket' },
  { id:'New',                          label:'New Products',           icon:'🆕', tKey:'prod_cat_new' },
  { id:'Tile Leveling System',         label:'Tile Leveling',          icon:'🧱', tKey:'prod_cat_tile' },
  { id:'Tools & Hardware',             label:'Tools & Hardware',       icon:'🔧', tKey:'prod_cat_tools' },
  { id:'Security Seal',                label:'Security Seals',         icon:'🔒', tKey:'prod_cat_seal' },
  { id:'Other',                        label:'Other Products',         icon:'📦', tKey:'prod_cat_other' },
];

function isQuoteOnly(p){ return p && p.quoteOnly === true; }
function isNewProduct(p){ return p && p.isNew === true; }
function isBusbarProduct(p){ return isQuoteOnly(p) || BUSBAR_SUB_IDS.has(p.category); }
function productMatchesFilter(p, filter){
  if(filter==='all') return true;
  if(filter===BUSBAR_FILTER) return isBusbarProduct(p);
  if(filter==='New') return isNewProduct(p);
  return p.category===filter;
}
function busbarTotal(counts){ return BUSBAR_SUBCATS.reduce((n,c)=>n+(counts[c.id]||0),0); }
function getFilterMeta(val){
  if(val===BUSBAR_FILTER) return BUSBAR_PARENT;
  const sub=BUSBAR_SUBCATS.find(c=>c.id===val);
  if(sub) return sub;
  return CATS.find(c=>c.id===val);
}
function newProductsTotal(){ return ALL.reduce((n,p)=>n+(isNewProduct(p)?1:0),0); }

const CAT_SLUG = {
  'Energy Meter': 'energy-meter',
  'Voltage Stabilizer/Regulator': 'voltage-stabilizer-regulator',
  'Current Transformer': 'current-transformer',
  'New': 'new-products',
  'Screw Machine': 'screw-machine',
  [BUSBAR_FILTER]: 'busbar',
  'Flexible Busbar': 'flexible-busbar',
  'Rigid Busbar': 'rigid-busbar',
  'Aluminum Busbar': 'aluminum-busbar',
  'Composite Laminated Busbar': 'composite-laminated-busbar',
  'CCS Integrated Busbar': 'ccs-integrated-busbar',
  'Heavy Duty Busbar': 'heavy-duty-busbar',
  'Energy Storage Busbar': 'energy-storage-busbar',
  'Busbar Protection': 'busbar-protection',
  'Variac/Transformer': 'variac-transformer',
  'Terminal & Connector': 'terminal-connector',
  'Solar/PV Products': 'solar-pv-products',
  'Fuse & Protection': 'fuse-protection',
  'Voltage Protector': 'voltage-protector',
  'Socket & Wiring': 'socket-wiring',
  'Tile Leveling System': 'tile-leveling-system',
  'Tools & Hardware': 'tools-hardware',
  'Security Seal': 'security-seal',
  'Other': 'other',
};
const SLUG_TO_CAT = Object.fromEntries(Object.entries(CAT_SLUG).map(([id, slug]) => [slug, id]));

/* ── Translation helper ── */
function catLabel(c) {
  const d = (typeof T !== 'undefined' && typeof currentLang !== 'undefined') ? T[currentLang] : null;
  return (d && c.tKey && d[c.tKey]) ? d[c.tKey] : c.label;
}

const CAT_APPS = {
  'Energy Meter':['Residential Buildings','Commercial Premises','Industrial Panels','Sub-metering','Solar Grid-tie','Smart Grid AMI'],
  'Voltage Stabilizer/Regulator':['Household Appliances','Medical Equipment','CNC Machines','HVAC Systems','Data Centers','Sensitive Electronics'],
  'New':['Recently Added','New Listings','Latest Uploads','Fresh Arrivals','New on Alibaba','New Products'],
  'Variac/Transformer':['Lab & Testing','Voltage Adjustment','Motor Speed Control','Audio Equipment','R&D Applications','Industrial Testing'],
  'New':['Recently Added','New Listings','Latest Uploads','Fresh Arrivals','New on Alibaba','New Products'],
  'Current Transformer':['LV Panel Metering','Protection Relays','Revenue Metering','Energy Audits','Sub-metering','SCADA Integration'],
  'Screw Machine':['Brass & Aluminum Busbar Processing','Automatic Drilling & Tapping','Screw Assembly Lines','Terminal Block Production','OEM Machine Customization','Factory Automation'],
  'Flexible Busbar':['LiFePO4 Battery Packs','EV Battery Modules','Energy Storage Systems','Power Distribution','Nickel-plated Connections','Custom OEM'],
  'Rigid Busbar':['Battery Pack Interconnect','Industrial Switchgear','EV Power Distribution','High-current Panels','Copper Bus Systems','OEM Projects'],
  'Aluminum Busbar':['Energy Storage','Solar Battery Banks','Lightweight Power Links','EV Applications','Insulated Bus Systems','Custom Fabrication'],
  'Composite Laminated Busbar':['Hybrid EV','Rail Transit','High-voltage Distribution','Laminated Shunts','Multi-layer Conductors','OEM Design'],
  'CCS Integrated Busbar':['Cell Contact Systems','Module Integration','Battery Assembly','Automated Production','EV Manufacturing','ESS Plants'],
  'Heavy Duty Busbar':['High-current ESS','Industrial Power','Utility-scale Storage','Welded Connections','Heavy-duty Connectors','Custom Spec'],
  'Energy Storage Busbar':['Container ESS','Commercial Storage','Solar + Storage','Microgrid','DC Distribution','Battery Cabinets'],
  'Busbar Protection':['Insulation Systems','Safety Covers','Thermal Management','Panel Protection','ESS Safety','Compliance'],
  [BUSBAR_FILTER]:['LiFePO4 Battery Packs','EV Modules','Energy Storage','Power Distribution','Custom OEM','Quote-based Projects'],
  'Terminal & Connector':['Panel Wiring','Control Cabinets','DIN Rail Systems','Cable Management','Industrial Installations','Switchboards'],
  'Fuse & Protection':['Overcurrent Protection','Solar PV Systems','Distribution Boards','Industrial Safety','LV Networks','Panel Protection'],
  'Solar/PV Products':['Solar Arrays','Grid-tie Systems','Off-grid Power','PV Combiner Boxes','Renewable Energy','EV Charging'],
  'Tile Leveling System':['Floor Tile Installation','Wall Tiling','Ceramic Tiles','Porcelain Tiles','Construction Projects','Professional Use'],
  'Voltage Protector':['Household Appliances','Refrigerators & ACs','Small Business','Surge Protection','Motor Protection','Phase Protection'],
  'Socket & Wiring':['Smart Homes','Office Automation','Kitchen Appliances','EV Charging','Commercial Spaces','App Control'],
  'Tools & Hardware':['Industrial Control','Machine Tool','Isolation Power','Factory Equipment','Control Panels','OEM Projects'],
  'Security Seal':['Meter Sealing','Revenue Protection','Anti-tampering','Utility Metering','Smart Grid','Compliance'],
  'Other':['Industrial Use','Commercial Buildings','Export Ready','OEM Available','CE Certified','ISO9001'],
};

let ALL=[],FILTERED=[],activeFilter='all',searchQuery='',sortMode='default',shown=60;
const PAGE=60;

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('data/products.json');
    if (!r.ok) throw new Error('HTTP '+r.status);
    ALL = await r.json();
  } catch(e) {
    console.warn('products.json failed:', e);
    const g = document.getElementById('prod-grid');
    if(g) g.innerHTML='<div class="empty-state"><h3>Could not load products</h3><p>Ensure data/products.json is present.</p></div>';
    const m = document.getElementById('area-meta');
    if(m) m.textContent='Load error';
    return;
  }
  const params = new URLSearchParams(location.search);
  const legacyCat = params.get('cat');
  if (legacyCat) {
    const name = decodeURIComponent(legacyCat.replace(/\+/g, ' '));
    const slug = CAT_SLUG[name];
    location.replace(slug ? `/products?category=${slug}` : '/products');
    return;
  }
  const urlCat = params.get('category');
  if (urlCat && urlCat !== 'all') {
    const slug = decodeURIComponent(urlCat).toLowerCase();
    activeFilter = SLUG_TO_CAT[slug] || activeFilter;
  }
  syncUrlAndMeta();

  buildSidebar(); buildMobileFilter(); buildBusbarSubBar(); initSbSearch(); initSort(); initLoadMore();
  applyAndRender();

  const urlId = new URLSearchParams(location.search).get('id');
  if(urlId){ const p=ALL.find(x=>x.id===urlId); if(p) setTimeout(()=>openDetail(p),400); }
});

/* ── Sidebar ── */
function buildSidebar(){
  const list=document.getElementById('sb-list'); if(!list) return;
  const counts={};
  ALL.forEach(p=>{counts[p.category]=(counts[p.category]||0)+1;});
  const newCount=newProductsTotal();
  const allLabel = (typeof T !== 'undefined' && typeof currentLang !== 'undefined' && T[currentLang] && T[currentLang].prod_all) ? T[currentLang].prod_all : 'All Products';
  let html=`<button class="sb-all ${activeFilter==='all'?'active':''}" data-filter="all" data-t="prod_all">
    <span style="display:flex;align-items:center;gap:8px"><span style="font-size:14px">🗂</span>${esc(allLabel)}</span>
    <span class="sb-count">${ALL.length}</span></button>`;
  const appendNewSidebar=()=>{
    if(!newCount) return;
    const newActive=activeFilter==='New';
    html+=`<button class="sb-item ${newActive?'active':''}" data-filter="New">
      <span class="sb-item-inner"><span class="sb-item-icon">🆕</span><span class="sb-item-label">${esc(catLabel({label:'New Products',tKey:'prod_cat_new'}))}</span></span>
      <span class="sb-count">${newCount}</span></button>`;
  };
  const appendBusbarSidebar=()=>{
    const busTotal=busbarTotal(counts);
    if(!busTotal) return;
    const busActive=activeFilter===BUSBAR_FILTER||BUSBAR_SUB_IDS.has(activeFilter);
    html+=`<button class="sb-item sb-item-parent ${busActive?'active':''}" data-filter="${esc(BUSBAR_FILTER)}">
      <span class="sb-item-inner"><span class="sb-item-icon">${BUSBAR_PARENT.icon}</span><span class="sb-item-label">${esc(catLabel(BUSBAR_PARENT))}</span></span>
      <span class="sb-count">${busTotal}</span></button>`;
  };
  appendNewSidebar();
  let busbarPlaced=false;
  CATS.forEach(c=>{
    const n=counts[c.id]||0; if(!n) return;
    html+=`<button class="sb-item ${activeFilter===c.id?'active':''}" data-filter="${esc(c.id)}">
      <span class="sb-item-inner"><span class="sb-item-icon">${c.icon}</span><span class="sb-item-label">${esc(catLabel(c))}</span></span>
      <span class="sb-count">${n}</span></button>`;
    if(c.id==='Current Transformer'){ appendBusbarSidebar(); busbarPlaced=true; }
  });
  if(!busbarPlaced) appendBusbarSidebar();
  list.innerHTML=html;
  list.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>setFilter(b.dataset.filter)));
}

function buildMobileFilter(){
  const bar=document.getElementById('mob-filter'); if(!bar) return;
  const counts={};
  ALL.forEach(p=>{counts[p.category]=(counts[p.category]||0)+1;});
  const newCount=newProductsTotal();
  const mAllLabel = (typeof T !== 'undefined' && typeof currentLang !== 'undefined' && T[currentLang] && T[currentLang].prod_all) ? T[currentLang].prod_all : 'All Products';
  let html=`<button class="mfbtn ${activeFilter==='all'?'active':''}" data-filter="all">${esc(mAllLabel)} (${ALL.length})</button>`;
  const appendNewMobile=()=>{
    if(!newCount) return;
    html+=`<button class="mfbtn ${activeFilter==='New'?'active':''}" data-filter="New">🆕 ${esc(catLabel({label:'New Products',tKey:'prod_cat_new'}))} (${newCount})</button>`;
  };
  const appendBusbarMobile=()=>{
    const busTotal=busbarTotal(counts);
    if(!busTotal) return;
    const busActive=activeFilter===BUSBAR_FILTER||BUSBAR_SUB_IDS.has(activeFilter);
    html+=`<button class="mfbtn ${busActive?'active':''}" data-filter="${esc(BUSBAR_FILTER)}">${BUSBAR_PARENT.icon} ${esc(catLabel(BUSBAR_PARENT))} (${busTotal})</button>`;
  };
  appendNewMobile();
  let busbarMobPlaced=false;
  CATS.forEach(c=>{
    const n=counts[c.id]||0; if(!n) return;
    html+=`<button class="mfbtn ${activeFilter===c.id?'active':''}" data-filter="${esc(c.id)}">${c.icon} ${esc(catLabel(c))} (${n})</button>`;
    if(c.id==='Current Transformer'){ appendBusbarMobile(); busbarMobPlaced=true; }
  });
  if(!busbarMobPlaced) appendBusbarMobile();
  bar.innerHTML=html;
  bar.querySelectorAll('.mfbtn').forEach(b=>b.addEventListener('click',()=>setFilter(b.dataset.filter)));
}

function isBusbarView(filter){
  return filter===BUSBAR_FILTER||BUSBAR_SUB_IDS.has(filter);
}

function buildBusbarSubBar(){
  const wrap=document.getElementById('busbar-sub-wrap');
  const chips=document.getElementById('busbar-sub-chips');
  if(!wrap||!chips) return;
  const inBusbar=isBusbarView(activeFilter);
  wrap.classList.toggle('show',inBusbar);
  wrap.hidden=!inBusbar;
  if(!inBusbar) return;
  const counts={};
  ALL.forEach(p=>{if(isBusbarProduct(p)) counts[p.category]=(counts[p.category]||0)+1;});
  const d=(typeof T!=='undefined'&&typeof currentLang!=='undefined')?T[currentLang]:null;
  const allLbl=(d&&d.prod_busbar_all)?d.prod_busbar_all:'All Busbars';
  const busTotal=busbarTotal(counts);
  let html=`<button type="button" class="busbar-chip ${activeFilter===BUSBAR_FILTER?'active':''}" data-busbar-sub="${esc(BUSBAR_FILTER)}">${BUSBAR_PARENT.icon} ${esc(allLbl)} (${busTotal})</button>`;
  BUSBAR_SUBCATS.forEach(c=>{
    const n=counts[c.id]||0; if(!n) return;
    html+=`<button type="button" class="busbar-chip ${activeFilter===c.id?'active':''}" data-busbar-sub="${esc(c.id)}">${c.icon} ${esc(catLabel(c))} (${n})</button>`;
  });
  chips.innerHTML=html;
  chips.querySelectorAll('.busbar-chip').forEach(btn=>btn.addEventListener('click',()=>setFilter(btn.dataset.busbarSub)));
}

function setFilter(val){
  activeFilter=val; searchQuery='';
  const sb=document.getElementById('sb-search'); if(sb) sb.value='';
  const busActive=isBusbarView(val);
  document.querySelectorAll('.sb-item,.sb-all').forEach(b=>{
    const f=b.dataset.filter;
    const isParent=b.classList.contains('sb-item-parent');
    if(isParent) b.classList.toggle('active',busActive);
    else b.classList.toggle('active',f===val);
  });
  document.querySelectorAll('.mfbtn').forEach(b=>{
    const f=b.dataset.filter;
    if(f===BUSBAR_FILTER) b.classList.toggle('active',busActive);
    else b.classList.toggle('active',f===val);
  });
  const t=document.getElementById('area-title');
  if(t){
    const allLbl = (typeof T !== 'undefined' && typeof currentLang !== 'undefined' && T[currentLang] && T[currentLang].prod_all) ? T[currentLang].prod_all : 'All Products';
    if(val==='all'){t.textContent=allLbl;}
    else if(val===BUSBAR_FILTER){t.textContent=catLabel(BUSBAR_PARENT);}
    else{const meta=getFilterMeta(val);t.textContent=meta?catLabel(meta):val;}
  }
  buildBusbarSubBar();
  shown=PAGE; applyAndRender();
  syncUrlAndMeta();
}

function syncUrlAndMeta() {
  const slug = activeFilter === 'all' ? '' : CAT_SLUG[activeFilter];
  const path = slug ? `/products?category=${slug}` : '/products';
  if (location.pathname.replace(/\.html$/, '').endsWith('/products') && location.search !== (slug ? `?category=${slug}` : '')) {
    history.replaceState(null, '', path);
  }
  const canonical = document.querySelector('link[rel="canonical"]');
  if (canonical) {
    canonical.href = slug
      ? `https://www.yominelectric.com/products?category=${slug}`
      : 'https://www.yominelectric.com/products';
  }
  const c = activeFilter === 'all' ? null : getFilterMeta(activeFilter);
  if (c) {
    document.title = `${catLabel(c)} | Yomin Electric Products`;
    const desc = document.querySelector('meta[name="description"]');
    if (desc) desc.content = `Browse Yomin Electric ${catLabel(c)} — factory-direct export pricing, ISO9001 certified, low MOQ.`;
  }
}

function initSbSearch(){
  const sb=document.getElementById('sb-search'); if(!sb) return;
  sb.addEventListener('input',e=>{searchQuery=e.target.value.trim().toLowerCase();shown=PAGE;applyAndRender();});
}

/* ── Sort ── */
function initSort(){
  const btn=document.getElementById('sort-btn'),drop=document.getElementById('sort-drop');
  if(!btn||!drop) return;
  btn.addEventListener('click',e=>{e.stopPropagation();drop.classList.toggle('op');});
  document.addEventListener('click',()=>drop.classList.remove('op'));
  drop.querySelectorAll('.sort-opt').forEach(opt=>opt.addEventListener('click',()=>{
    sortMode=opt.dataset.sort;
    drop.querySelectorAll('.sort-opt').forEach(o=>o.classList.remove('act')); opt.classList.add('act');
    drop.classList.remove('op');
    const d = (typeof T !== 'undefined' && typeof currentLang !== 'undefined') ? T[currentLang] : null;
    const lbl={default:(d&&d.prod_sort)||'Sort','price-asc':(d&&d.prod_price_asc)||'Price ↑','price-desc':(d&&d.prod_price_desc)||'Price ↓',az:(d&&d.prod_az)||'A–Z',za:(d&&d.prod_za)||'Z–A'};
    const fn=btn.childNodes[0]; if(fn) fn.textContent=(lbl[sortMode]||((d&&d.prod_sort)||'Sort'))+' ';
    shown=PAGE; applyAndRender();
  }));
}

/* ── Load More ── */
function initLoadMore(){
  const btn=document.getElementById('load-more'); if(!btn) return;
  btn.addEventListener('click',()=>{
    shown=Math.min(shown+PAGE,FILTERED.length);
    renderGrid(false); updateMeta(); updateLoadMore();
  });
}

/* ── Apply + Render ── */
function applyAndRender(){
  FILTERED=activeFilter==='all'?[...ALL]:ALL.filter(p=>productMatchesFilter(p,activeFilter));
  if(searchQuery){
    const q=searchQuery;
    FILTERED=FILTERED.filter(p=>
      p.title.toLowerCase().includes(q)||
      (p.description||'').toLowerCase().includes(q)||
      p.category.toLowerCase().includes(q)||
      (p.keywords||[]).some(k=>String(k).toLowerCase().includes(q))||
      Object.values(p.specs||{}).some(v=>String(v).toLowerCase().includes(q))
    );
  }
  if(sortMode==='az') FILTERED.sort((a,b)=>a.title.localeCompare(b.title));
  else if(sortMode==='za') FILTERED.sort((a,b)=>b.title.localeCompare(a.title));
  else if(sortMode==='price-asc') FILTERED.sort((a,b)=>priceMin(a)-priceMin(b));
  else if(sortMode==='price-desc') FILTERED.sort((a,b)=>priceMin(b)-priceMin(a));
  else if(activeFilter==='all') FILTERED.sort((a,b)=>(b.category==='Screw Machine'?1:0)-(a.category==='Screw Machine'?1:0));
  else if(activeFilter==='New') FILTERED.sort((a,b)=>(b.isNew===true)-(a.isNew===true)||a.title.localeCompare(b.title));
  shown=PAGE; renderGrid(true); updateMeta(); updateLoadMore();
}

function priceMin(p){
  if(isQuoteOnly(p)) return 99999;
  const s=p.price;
  if(!s) return 9999;
  const m=String(s).match(/[\d.]+/);
  return m?parseFloat(m[0]):9999;
}

/* ── Grid render ── */
function renderGrid(animate){
  const grid=document.getElementById('prod-grid'); if(!grid) return;
  const slice=FILTERED.slice(0,shown);
  if(!slice.length){
    grid.innerHTML='<div class="empty-state"><div style="font-size:40px;opacity:.3;margin-bottom:16px">🔍</div><h3>No products found</h3><p>Try a different search or category.</p></div>';
    return;
  }
  grid.innerHTML=slice.map(p=>productCard(p)).join('');
  grid.querySelectorAll('.pcard').forEach(card=>{
    card.addEventListener('click',e=>{
      e.preventDefault();
      const p=ALL.find(x=>x.id===card.dataset.id);
      if(p) openDetail(p);
    });
  });
  if(animate){
    grid.querySelectorAll('.pcard').forEach((el,i)=>{
      el.style.opacity='0'; el.style.transform='translateY(16px)';
      requestAnimationFrame(()=>setTimeout(()=>{
        el.style.transition='opacity .3s ease,transform .3s ease,border-color .25s,box-shadow .25s';
        el.style.opacity='1'; el.style.transform='translateY(0)';
      },Math.min(i*18,500)));
    });
  }
}

function productCard(p){
  const specs=p.specs||{};
  const pills=Object.keys(specs).slice(0,3).map(k=>`<span class="spec-pill">${esc(specs[k])}</span>`).join('');
  const thumb=(p.image|| (Array.isArray(p.images) && p.images[0]) || '');
  const imgHtml=thumb
    ?`<img src="${esc(thumb)}" alt="${esc(p.title)}" loading="lazy" decoding="async" onerror="var fb=this.nextElementSibling;this.style.display='none';fb.style.display='flex'"><div class="pcard-img-fb" style="display:none">${catSvg(p.category)}</div>`
    :`<div class="pcard-img-fb">${catSvg(p.category)}</div>`;
  const d=(typeof T!=='undefined'&&typeof currentLang!=='undefined')?T[currentLang]:null;
  const inquiryLbl=(d&&d.prod_request_quote)?d.prod_request_quote.replace('Request Quote','Inquiry for Price'):'Inquiry for Price';
  return `<a class="pcard${isQuoteOnly(p)?' pcard-quote':''}" href="#" data-id="${esc(p.id)}" title="${esc(p.title)}">
    <div class="pcard-img">${imgHtml}</div>
    <div class="pcard-body">
      <div class="pcard-cat">${esc(p.category)}</div>
      <div class="pcard-name">${esc(p.title)}</div>
      ${pills?`<div class="pcard-specs">${pills}</div>`:''}
    </div>
    <div class="pcard-foot">
      <span class="pcard-price">${inquiryLbl}</span>
      <span class="pcard-arrow">View →</span>
    </div>
  </a>`;
}

function updateMeta(){
  const el=document.getElementById('area-meta'); if(!el) return;
  el.textContent=`Showing ${Math.min(shown,FILTERED.length)} of ${FILTERED.length} product${FILTERED.length!==1?'s':''}`;
}
function updateLoadMore(){
  const btn=document.getElementById('load-more'); if(!btn) return;
  const rem=FILTERED.length-shown;
  if(rem<=0){btn.style.display='none';return;}
  btn.style.display='inline-flex';
  const loadMoreLbl = (typeof T !== 'undefined' && typeof currentLang !== 'undefined' && T[currentLang] && T[currentLang].prod_load_more) ? T[currentLang].prod_load_more : 'Load More';
  btn.textContent=`${loadMoreLbl} (${Math.min(rem,PAGE)})`;
}

/* ══ DETAIL PANEL ════════════════════════════════════════════ */
function openDetail(p){
  const panel=document.getElementById('detail-panel'); if(!panel) return;
  const specs=p.specs||{};
  const apps=CAT_APPS[p.category]||CAT_APPS['Other'];
  const cfg=getFilterMeta(p.category)||CATS.find(c=>c.id===p.category);
  const icon=cfg?cfg.icon:'📦';

  const galleryImgs=(p.images&&p.images.length)?p.images:(p.image?[p.image]:[]);
  const imgHtml=galleryImgs[0]
    ?`<img src="${esc(galleryImgs[0])}" alt="${esc(p.title)}" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'"><div class="dp-img-fb" style="display:none">${catSvg(p.category,90)}</div>`
    :`<div class="dp-img-fb">${catSvg(p.category,90)}</div>`;

  const specRows=Object.entries(specs).map(([k,v])=>
    `<div class="dp-spec-row"><span class="dp-spec-key">${esc(k)}</span><span class="dp-spec-val">${esc(String(v))}</span></div>`
  ).join('');
  const kwHtml=(p.keywords&&p.keywords.length)?`<div class="dp-section-label" style="margin-top:18px">Keywords</div><div class="dp-apps">${p.keywords.map(k=>`<span class="dp-app-chip">${esc(k)}</span>`).join('')}</div>`:'';

  const isScrewMachine = p.category === 'Screw Machine';
  const certDocLinks = isScrewMachine ? `
    <div class="dp-section-label" style="margin-top:18px">Certifications</div>
    <div class="dp-cert-docs">
      <a href="/assets/docs/screw-machine-ce-certificate.pdf" target="_blank" class="dp-cert-doc-link">📄 CE Certificate</a>
      <a href="/assets/docs/screw-machine-ce-report.pdf" target="_blank" class="dp-cert-doc-link">📋 CE Report</a>
      <a href="/assets/docs/screw-machine-technical-construction.pdf" target="_blank" class="dp-cert-doc-link">📐 Technical Construction File</a>
    </div>` : '';
  const extraRows=`
    <div class="dp-spec-row"><span class="dp-spec-key">Certification</span><span class="dp-spec-val">CE, ISO 9001</span></div>
    <div class="dp-spec-row"><span class="dp-spec-key">Warranty</span><span class="dp-spec-val">2 Years</span></div>
    <div class="dp-spec-row"><span class="dp-spec-key">Lead Time</span><span class="dp-spec-val">15–25 days</span></div>
    <div class="dp-spec-row"><span class="dp-spec-key">Min. Order</span><span class="dp-spec-val">100 units</span></div>
    <div class="dp-spec-row"><span class="dp-spec-key">Origin</span><span class="dp-spec-val">Zhejiang, China</span></div>`;

  const appIcons=['🏠','🏪','⚡','🏭','🌐','🔌','📡','🔧'];
  const appChips=apps.map((a,i)=>`<span class="dp-app-chip">${appIcons[i%appIcons.length]} ${esc(a)}</span>`).join('');

  panel.innerHTML=`
    <div class="dp-inner">
      <button class="dp-close" id="dp-close" aria-label="Close">✕</button>
      <div class="dp-left">
        <div class="dp-img-wrap">${imgHtml}</div>
        <div class="dp-price-wrap">
          ${isQuoteOnly(p)
            ? `<p class="dp-quote-note">${esc((typeof T!=='undefined'&&typeof currentLang!=='undefined'&&T[currentLang]&&T[currentLang].prod_quote_busbar_desc)?T[currentLang].prod_quote_busbar_desc:'Busbar pricing is project-specific. Request a quotation first — we review your specs and negotiate terms with you.')}</p>`
            : ''}
          <a class="dp-quote-btn" href="contact.html?product=${encodeURIComponent(p.title)}">${esc((typeof T!=='undefined'&&typeof currentLang!=='undefined'&&T[currentLang]&&T[currentLang].prod_request_quote)?T[currentLang].prod_request_quote:'Request Quote')} →</a>
          <a class="dp-wa-btn" href="https://wa.me/8619016543301?text=${encodeURIComponent('Hi Yomin Electric, I am interested in: '+p.title+' (ID: '+p.id+')')}" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            WhatsApp
          </a>
        </div>
      </div>
      <div class="dp-right">
        <div class="dp-badge">${icon} ${esc(p.category)}</div>
        <h2 class="dp-title">${esc(p.title)}</h2>
        <p class="dp-desc">${esc(p.description||buildAutoDesc(p))}</p>
        <div class="dp-section-label">Specifications</div>
        <div class="dp-specs-grid">${specRows||'<div class="dp-spec-row"><span class="dp-spec-key">Category</span><span class="dp-spec-val">'+esc(p.category)+'</span></div>'}${extraRows}</div>
        ${certDocLinks}
        ${kwHtml}
        <div class="dp-section-label" style="margin-top:22px">Applications</div>
        <div class="dp-apps">${appChips}</div>
      </div>
    </div>`;

  panel.style.display='block';
  panel.classList.remove('dp-visible');
  requestAnimationFrame(()=>requestAnimationFrame(()=>panel.classList.add('dp-visible')));

  document.querySelectorAll('.pcard').forEach(c=>c.classList.toggle('pcard-active',c.dataset.id===p.id));
  document.getElementById('dp-close')?.addEventListener('click',closeDetail);
}

function closeDetail(){
  const panel=document.getElementById('detail-panel'); if(!panel) return;
  panel.classList.remove('dp-visible');
  setTimeout(()=>{panel.style.display='none';panel.innerHTML='';},320);
  document.querySelectorAll('.pcard').forEach(c=>c.classList.remove('pcard-active'));
}

function buildAutoDesc(p){
  const s=p.specs||{},parts=[];
  if(s.Phase) parts.push(s.Phase);
  if(s.Voltage) parts.push(s.Voltage+' rated');
  if(s.Capacity) parts.push(s.Capacity);
  if(s.Communication) parts.push(s.Communication+' connectivity');
  return (parts.length?parts.join(' · ')+'. ':'')+
    `High-quality ${p.category.toLowerCase()} from Zhejiang Yomin Electric Co., Ltd. CE certified, ISO9001, exported to 95+ countries.`;
}

/* ── SVG fallbacks ── */
function catSvg(cat,size=64){
  const p={
    'Energy Meter':`<path d="M14 12h36v18H14z" fill="rgba(200,169,110,.1)" stroke="#c8a96e" stroke-width="1.5" rx="3"/><text x="32" y="25" text-anchor="middle" fill="#c8a96e" font-size="9" font-family="monospace">kWh</text><line x1="18" y1="38" x2="46" y2="38" stroke="#c8a96e" stroke-width="1.2"/><circle cx="32" cy="48" r="6" stroke="#c8a96e" stroke-width="1.2" fill="none"/>`,
    'Voltage Stabilizer/Regulator':`<rect x="8" y="14" width="48" height="36" rx="4" fill="rgba(200,169,110,.07)" stroke="#c8a96e" stroke-width="1.5"/><path d="M14 38L22 22L30 42L38 28L46 38L52 32" stroke="#c8a96e" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    'Current Transformer':`<circle cx="32" cy="32" r="22" stroke="#c8a96e" stroke-width="1.5" fill="rgba(200,169,110,.05)"/><circle cx="32" cy="32" r="10" stroke="#c8a96e" stroke-width="1.2" fill="rgba(200,169,110,.12)"/><line x1="32" y1="10" x2="32" y2="22" stroke="#c8a96e" stroke-width="1.5"/><line x1="32" y1="42" x2="32" y2="54" stroke="#c8a96e" stroke-width="1.5"/>`,
    'Variac/Transformer':`<circle cx="22" cy="32" r="14" stroke="#c8a96e" stroke-width="1.5" fill="rgba(200,169,110,.06)"/><circle cx="42" cy="32" r="14" stroke="#c8a96e" stroke-width="1.5" fill="rgba(200,169,110,.06)"/><line x1="8" y1="32" x2="13" y2="32" stroke="#c8a96e" stroke-width="1.5"/><line x1="51" y1="32" x2="56" y2="32" stroke="#c8a96e" stroke-width="1.5"/>`,
    'Solar/PV Products':`<circle cx="32" cy="32" r="10" fill="rgba(200,169,110,.15)" stroke="#c8a96e" stroke-width="1.5"/><path d="M32 10v8M32 46v8M10 32h8M46 32h8M16 16l6 6M42 42l6 6M42 16l-6 6M16 42l6-6" stroke="#c8a96e" stroke-width="1.5" stroke-linecap="round"/>`,
    'Tile Leveling System':`<rect x="8" y="16" width="20" height="20" rx="2" fill="rgba(200,169,110,.1)" stroke="#c8a96e" stroke-width="1.5"/><rect x="36" y="16" width="20" height="20" rx="2" fill="rgba(200,169,110,.1)" stroke="#c8a96e" stroke-width="1.5"/><rect x="22" y="32" width="20" height="20" rx="2" fill="rgba(200,169,110,.1)" stroke="#c8a96e" stroke-width="1.5"/>`,
    'Terminal & Connector':`<rect x="12" y="22" width="40" height="24" rx="3" fill="rgba(200,169,110,.07)" stroke="#c8a96e" stroke-width="1.5"/><line x1="24" y1="22" x2="24" y2="46" stroke="#c8a96e" stroke-width="1"/><line x1="40" y1="22" x2="40" y2="46" stroke="#c8a96e" stroke-width="1"/><rect x="19" y="12" width="10" height="12" rx="2" fill="rgba(200,169,110,.25)"/><rect x="35" y="12" width="10" height="12" rx="2" fill="rgba(200,169,110,.25)"/>`,
    'Fuse & Protection':`<rect x="24" y="10" width="16" height="44" rx="4" fill="rgba(200,169,110,.1)" stroke="#c8a96e" stroke-width="1.5"/><line x1="32" y1="10" x2="32" y2="4" stroke="#c8a96e" stroke-width="2"/><line x1="32" y1="54" x2="32" y2="60" stroke="#c8a96e" stroke-width="2"/><line x1="26" y1="32" x2="38" y2="32" stroke="#c8a96e" stroke-width="1.5"/>`,
  };
  const d=p[cat]||`<rect x="10" y="10" width="44" height="44" rx="4" fill="rgba(200,169,110,.07)" stroke="#c8a96e" stroke-width="1.5"/><path d="M22 46L22 30M32 46L32 20M42 46L42 36" stroke="#c8a96e" stroke-width="2.5" stroke-linecap="round"/>`;
  return `<svg viewBox="0 0 64 64" fill="none" width="${size}" height="${size}">${d}</svg>`;
}

function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
