'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const productsPath = path.join(ROOT, 'data/products.json');
const screwPath = path.join(ROOT, 'data/screw-machines.json');
const haiyanPath = path.join(ROOT, 'data/haiyan-busbar-meta.json');

const products = JSON.parse(fs.readFileSync(productsPath, 'utf8'));
const screws = JSON.parse(fs.readFileSync(screwPath, 'utf8'));

let haiyan = {};
if (fs.existsSync(haiyanPath)) {
  haiyan = JSON.parse(fs.readFileSync(haiyanPath, 'utf8'));
}

const CATEGORY_DEFAULTS = {
  'Flexible Busbar': {
    description: 'Designed for flexibility and ease of installation, flexible busbars are ideal for adaptable, space-saving electrical connections in new energy battery packs.',
    keywords: ['flexible busbar', 'nickel plated copper', 'LiFePO4 battery', 'EV battery pack', 'energy storage', 'power distribution', 'insulated busbar', 'OEM custom'],
    specs: { Application: 'New energy battery packs, EV modules, ESS', Material: 'Copper / nickel plated', Type: 'Flexible' },
  },
  'Rigid Busbar': {
    description: 'Rigid busbars provide durable, high-performance electrical connections with reliable current distribution for industrial and power applications.',
    keywords: ['rigid busbar', 'copper busbar', 'inflexible busbar', 'battery interconnect', 'high current', 'switchgear', 'industrial power'],
    specs: { Application: 'Fixed installations, battery packs, switchgear', Material: 'Copper / aluminum', Type: 'Rigid' },
  },
  'Aluminum Busbar': {
    description: 'Lightweight yet strong, aluminum busbars offer excellent conductivity and corrosion resistance for energy-efficient electrical solutions.',
    keywords: ['aluminum busbar', 'electrical aluminum flat bar', 'lightweight conductor', 'energy storage', 'solar battery', 'corrosion resistant'],
    specs: { Application: 'ESS, solar arrays, lightweight power links', Material: 'Aluminum', Type: 'Insulated / bare' },
  },
  'Composite Laminated Busbar': {
    description: 'Composite laminated busbars are flexible and highly durable, accommodating movement and vibration in dynamic battery systems.',
    keywords: ['composite laminated busbar', 'laminated shunt', 'hybrid EV', 'rail transit', 'multi-layer conductor', 'vibration tolerant'],
    specs: { Application: 'Hybrid EV, rail, high-voltage distribution', Material: 'Copper-aluminum laminated', Type: 'Composite' },
  },
  'CCS Integrated Busbar': {
    description: 'Cell Contact System (CCS) integrated busbars provide strong, stable conductivity for fixed installations requiring minimal maintenance.',
    keywords: ['CCS busbar', 'cell contact system', 'solid connection', 'module integration', 'battery assembly', 'EV manufacturing'],
    specs: { Application: 'Cell contact systems, module integration', Material: 'Copper / aluminum', Type: 'CCS integrated' },
  },
  'Heavy Duty Busbar': {
    description: 'Heavy-duty connectors are engineered for high power applications with robust, secure connections for demanding industrial environments.',
    keywords: ['heavy duty busbar', 'heavy duty connector', 'high current connector', 'ESS', 'industrial power', 'welded busbar'],
    specs: { Application: 'High-current ESS, industrial power', Material: 'Copper', Type: 'Heavy duty' },
  },
  'Energy Storage Busbar': {
    description: 'Specialized connectors for energy storage systems, ensuring safe, efficient, and reliable connections between batteries and components.',
    keywords: ['energy storage busbar', 'energy storage connector', 'battery connector', 'container ESS', 'DC distribution', 'microgrid'],
    specs: { Application: 'Container ESS, commercial storage', Material: 'Copper / aluminum', Type: 'Storage connector' },
  },
  'Busbar Protection': {
    description: 'PVC battery terminal covers offer protection against short circuits, corrosion, and environmental damage for safer battery terminals.',
    keywords: ['busbar protection', 'PVC terminal cover', 'battery terminal cover', 'insulation cover', 'battery safety'],
    specs: { Application: 'Terminal protection, ESS safety', Material: 'PVC / insulation', Type: 'Protection' },
  },
};

function mergeSpecs(base, extra) {
  const out = { ...base };
  Object.entries(extra || {}).forEach(([k, v]) => {
    if (!out[k]) out[k] = v;
  });
  return out;
}

function enrichBusbar(p) {
  if (!p.quoteOnly && !CATEGORY_DEFAULTS[p.category]) return p;
  const cat = CATEGORY_DEFAULTS[p.category];
  const hy = haiyan[p.category];
  if (!cat && !hy) return p;

  const keywords = [
    ...(p.keywords || []),
    ...(hy?.keywords || []),
    ...(cat?.keywords || []),
  ];
  const uniqueKw = [...new Set(keywords.map((k) => k.toLowerCase()))].slice(0, 14);

  const specs = mergeSpecs(cat?.specs || {}, p.specs || {});
  if (hy?.specs) Object.assign(specs, hy.specs);
  if (!specs.Application && hy?.description) specs.Application = hy.description.slice(0, 120);

  const desc = p.description && p.description.length > 80
    ? p.description
    : (hy?.description || cat?.description || p.description);

  return {
    ...p,
    description: desc,
    specs,
    keywords: uniqueKw.length ? uniqueKw : p.keywords,
  };
}

const existingIds = new Set(products.map((p) => p.id));
const existingTitles = new Set(products.map((p) => p.title.toLowerCase()));

let maxNum = 0;
products.forEach((p) => {
  const n = parseInt(String(p.id).replace(/\D/g, ''), 10);
  if (n > maxNum) maxNum = n;
});

const newScrews = screws.filter((s) => !existingIds.has(s.id) && !existingTitles.has(s.title.toLowerCase()));
const enriched = products.map(enrichBusbar);
const merged = [...enriched, ...newScrews];

fs.writeFileSync(productsPath, JSON.stringify(merged, null, 2) + '\n');
console.log('Added screw machines:', newScrews.length);
console.log('Total products:', merged.length);
console.log('Busbar enriched:', enriched.filter((p) => p.quoteOnly).length);
