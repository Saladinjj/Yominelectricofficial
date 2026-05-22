'use strict';
const fs = require('fs');
const path = require('path');

const htmlPath = path.join(process.env.TEMP || '/tmp', 'zhongyan-products.html');
const productsPath = path.join(__dirname, '../data/products.json');

const html = fs.readFileSync(htmlPath, 'utf8');
const products = JSON.parse(fs.readFileSync(productsPath, 'utf8'));

const byTitle = new Map();
html.split('<div class="product-full-card').slice(1).forEach((chunk) => {
  const titleM = chunk.match(/product-full-name">([^<]+)</);
  const specBlock = chunk.match(/product-specs">([\s\S]*?)<\/div>/);
  if (!titleM) return;
  const title = titleM[1].trim().replace(/…$/, '').trim();
  const tags = specBlock
    ? [...specBlock[1].matchAll(/spec-tag">([^<]+)</g)].map((m) => m[1])
    : [];
  const specs = {};
  tags.forEach((tag) => {
    if (/^\d+\s*piece/i.test(tag)) specs.MOQ = tag;
    else if (/A|V|kV|mm|μm|Cu|Al/i.test(tag) && tag.length < 40) specs.Rating = specs.Rating ? `${specs.Rating}, ${tag}` : tag;
    else specs.Type = specs.Type ? `${specs.Type}, ${tag}` : tag;
  });
  byTitle.set(title.toLowerCase(), specs);
});

let fixed = 0;
products.forEach((p) => {
  if (!p.quoteOnly) return;
  const key = p.title.toLowerCase();
  const specs = byTitle.get(key);
  if (!specs) return;
  const bad = JSON.stringify(p.specs || {}).length > 200;
  if (bad || !p.specs || Object.keys(p.specs).length === 0) {
    p.specs = specs;
    fixed++;
  }
});

fs.writeFileSync(productsPath, JSON.stringify(products, null, 2) + '\n');
console.log('Fixed specs for', fixed, 'busbar products');
