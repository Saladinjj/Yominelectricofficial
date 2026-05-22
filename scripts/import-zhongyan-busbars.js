/**
 * Parse zhongyan products.html and append busbar products to data/products.json
 */
'use strict';
const fs = require('fs');
const path = require('path');

const htmlPath = path.join(process.env.TEMP || '/tmp', 'zhongyan-products.html');
const productsPath = path.join(__dirname, '../data/products.json');

const html = fs.readFileSync(htmlPath, 'utf8');
const cardRe = /<div class="product-full-card[^"]*" data-cat="([^"]+)">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;

const CAT_LABEL_NORM = {
  'Energy Storage': 'Energy Storage Busbar',
  Protection: 'Busbar Protection',
  'Composite Laminated': 'Composite Laminated Busbar',
  'CCS Integrated': 'CCS Integrated Busbar',
  'Heavy Duty Connector': 'Heavy Duty Busbar',
};

const CAT_MAP = {
  flexible: 'Flexible Busbar',
  rigid: 'Rigid Busbar',
  aluminum: 'Aluminum Busbar',
  composite: 'Composite Laminated Busbar',
  ccs: 'CCS Integrated Busbar',
  heavy: 'Heavy Duty Busbar',
  storage: 'Energy Storage Busbar',
  protection: 'Busbar Protection',
};

const DESC =
  'Custom busbar solution for new energy battery packs and power distribution. Request a quotation first — our team will review your drawings and specifications, then negotiate pricing and lead time for your project.';

function parseCard(block, dataCat) {
  const imgM = block.match(/src="([^"]+)"/);
  const catM = block.match(/product-full-cat">([^<]+)</);
  const titleM = block.match(/product-full-name">([^<]+)</);
  const specTags = [...block.matchAll(/spec-tag">([^<]+)</g)].map((m) => m[1]);
  if (!imgM || !titleM) return null;
  let category = (catM && catM[1].trim()) || CAT_MAP[dataCat] || 'Busbar';
  if (CAT_LABEL_NORM[category]) category = CAT_LABEL_NORM[category];
  const specs = {};
  specTags.forEach((tag) => {
    if (/^\d+\s*piece/i.test(tag)) specs['MOQ'] = tag;
    else if (/A|V|kV|mm|μm/i.test(tag)) specs['Rating'] = specs['Rating'] ? `${specs['Rating']}, ${tag}` : tag;
    else specs['Type'] = specs['Type'] ? `${specs['Type']}, ${tag}` : tag;
  });
  return {
    title: titleM[1].trim().replace(/…$/, '').trim(),
    category,
    description: DESC,
    specs,
    image: imgM[1],
    quoteOnly: true,
    dataCat,
  };
}

const parsed = [];
let m;
while ((m = cardRe.exec(html))) {
  const p = parseCard(m[2], m[1]);
  if (p) parsed.push(p);
}

// Fallback: simpler split if regex missed cards
if (parsed.length < 50) {
  const chunks = html.split('product-full-card');
  chunks.slice(1).forEach((chunk) => {
    const dc = chunk.match(/data-cat="([^"]+)"/);
    if (!dc) return;
    const p = parseCard(chunk, dc[1]);
    if (p) parsed.push(p);
  });
}

const existing = JSON.parse(fs.readFileSync(productsPath, 'utf8'));
let maxNum = 0;
existing.forEach((p) => {
  const n = parseInt(String(p.id).replace(/\D/g, ''), 10);
  if (n > maxNum) maxNum = n;
});

const existingTitles = new Set(existing.map((p) => p.title.toLowerCase()));
const newOnes = [];
parsed.forEach((p) => {
  const key = p.title.toLowerCase();
  if (existingTitles.has(key)) return;
  existingTitles.add(key);
  maxNum += 1;
  newOnes.push({
    id: `ym-${String(maxNum).padStart(4, '0')}`,
    title: p.title,
    category: p.category,
    description: p.description,
    specs: p.specs,
    image: p.image,
    quoteOnly: true,
  });
});

const merged = [...existing, ...newOnes];
fs.writeFileSync(productsPath, JSON.stringify(merged, null, 2) + '\n');
console.log('Parsed from HTML:', parsed.length);
console.log('Added new:', newOnes.length);
console.log('Total products:', merged.length);
const by = {};
newOnes.forEach((p) => {
  by[p.category] = (by[p.category] || 0) + 1;
});
console.log('New by category:', by);
