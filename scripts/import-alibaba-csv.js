/**
 * Import Alibaba store CSV export (Table Scraper) into data/products.json
 *
 * Usage: node scripts/import-alibaba-csv.js path/to/export.csv
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const productsPath = path.join(ROOT, 'data/products.json');

const CAT_RULES = [
  [/energy\s*meter|kwh|kilowatt|electricity\s*meter|电表|电能表/i, 'Energy Meter'],
  [/current\s*transformer|\bct\b|lzzb|lzzw|lmz|laj-|lzzbj/i, 'Current Transformer'],
  [/voltage\s*transformer|\bpt\b|\bvt\b|jdz|jdzx|jdzc|potential\s*transformer/i, 'Current Transformer'],
  [/vacuum\s*circuit|vcb\b|zn63|vs1-|zw32|circuit\s*breaker/i, 'Fuse & Protection'],
  [/disconnector|isolat(ing|or)\s*switch|knife\s*switch|cutout|fuse\s*switch/i, 'Fuse & Protection'],
  [/surge\s*arrester|lightning|spd\b/i, 'Fuse & Protection'],
  [/over[- ]?voltage|under[- ]?voltage|voltage\s*protector/i, 'Voltage Protector'],
  [/voltage\s*stabilizer|voltage\s*regulator|\bavr\b/i, 'Voltage Stabilizer/Regulator'],
  [/power\s*transformer|distribution\s*transformer|oil\s*immersed|s11\s*series/i, 'Variac/Transformer'],
  [/transformer/i, 'Variac/Transformer'],
  [/busbar|铜排|母线/i, 'Flexible Busbar'],
  [/solar|pv|光伏/i, 'Solar/PV Products'],
  [/socket|plug|插座|插头/i, 'Socket & Wiring'],
  [/terminal|connector|wire\s*clamp|piercing/i, 'Terminal & Connector'],
  [/seal|铅封/i, 'Security Seal'],
  [/switchgear|ring\s*network|cabinet/i, 'Fuse & Protection'],
];

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = '';
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    const next = text[i + 1];

    if (inQuotes) {
      if (c === '"' && next === '"') {
        field += '"';
        i++;
      } else if (c === '"') {
        inQuotes = false;
      } else {
        field += c;
      }
      continue;
    }

    if (c === '"') {
      inQuotes = true;
    } else if (c === ',') {
      row.push(field);
      field = '';
    } else if (c === '\n') {
      row.push(field);
      field = '';
      if (row.length > 1 || row[0] !== '') rows.push(row);
      row = [];
    } else if (c !== '\r') {
      field += c;
    }
  }

  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }

  return rows;
}

function decodeHtml(s) {
  return String(s || '')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/\s+/g, ' ')
    .trim();
}

function firstUrl(...values) {
  for (const v of values) {
    const text = String(v || '');
    const m = text.match(/https?:\/\/[^\s"'<>]+/i);
    if (m) return m[0].replace(/[?&]hasNWGrade=1/, '').replace(/_(\d+x\d+)(q\d+)?\.(jpg|png|webp)/i, '.$3');
  }
  return '';
}

function parsePrice(row, headers) {
  const pick = (...names) => {
    for (const n of names) {
      const i = headers.indexOf(n);
      if (i >= 0 && row[i]) return decodeHtml(row[i]);
    }
    return '';
  };
  let price = pick('data', 'price', 'minimum_order_quantity_2');
  if (price && /min\.?\s*order/i.test(price)) price = pick('data', 'price');
  if (price && !/^\$/.test(price)) {
    const m = price.match(/\$[\d,.]+(?:-\$?[\d,.]+)?/);
    if (m) price = m[0];
  }
  return price;
}

function parseMoq(row, headers) {
  const pick = (...names) => {
    for (const n of names) {
      const i = headers.indexOf(n);
      if (i >= 0 && row[i]) return decodeHtml(row[i]);
    }
    return '';
  };
  const raw = pick('data2', 'minimum_order_quantity', 'minimum_order_quantity_2');
  const m = raw.match(/min\.?\s*order[:\s]*([^,]+)/i);
  return m ? m[1].trim() : raw.replace(/^Min\.?\s*Order:\s*/i, '').trim();
}

function guessCategory(title) {
  for (const [re, cat] of CAT_RULES) {
    if (re.test(title)) return cat;
  }
  return 'Other';
}

function rowToProduct(row, headers) {
  const get = (name) => {
    const i = headers.indexOf(name);
    return i >= 0 ? decodeHtml(row[i]) : '';
  };

  const title = get('title') || get('title_1') || get('item_page_title');
  if (!title || title.length < 4) return null;

  const url = get('item_page_link');
  const image = firstUrl(
    get('image2'),
    get('image'),
    get('image_1'),
    get('image_2'),
    get('image_4'),
    get('image_5')
  );
  const price = parsePrice(row, headers);
  const moq = parseMoq(row, headers);
  const supplier = get('supplier_name') || get('name') || get('name_1') || get('name_2');

  const specs = {};
  if (moq) specs.MOQ = moq;
  if (price) specs['List Price'] = price;
  ['rated_voltage', 'rated_voltage_1', 'rated_current_1', 'rated_capacity', 'lead_time', 'lead_time_1'].forEach((k) => {
    const v = get(k);
    if (v) specs[k.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())] = v;
  });
  if (supplier) specs.Supplier = supplier;

  const cat = guessCategory(title);
  return {
    title,
    category: cat,
    price: price || undefined,
    description: supplier
      ? `Listed on Alibaba (${supplier}). Contact us for export pricing, MOQ, and lead time.`
      : 'Listed on Alibaba. Contact us for export pricing, MOQ, and lead time.',
    specs,
    image: image || 'https://www.yominelectric.com/logo.png',
    url: url || 'https://ctpt.en.alibaba.com/productlist.html',
    source: 'alibaba',
    isNew: true,
    keywords: ['alibaba', supplier ? supplier.toLowerCase().slice(0, 40) : 'ctpt', cat.toLowerCase(), title.toLowerCase().slice(0, 50)],
  };
}

function main() {
  const input = process.argv[2];
  if (!input || !fs.existsSync(input)) {
    console.error('Usage: node scripts/import-alibaba-csv.js path/to/export.csv');
    process.exit(1);
  }

  const text = fs.readFileSync(path.resolve(input), 'utf8');
  const rows = parseCsv(text);
  if (rows.length < 2) {
    console.error('CSV has no data rows');
    process.exit(1);
  }

  const headers = rows[0].map((h) => h.trim());
  const parsed = [];
  const seen = new Set();
  for (let i = 1; i < rows.length; i++) {
    const p = rowToProduct(rows[i], headers);
    if (!p) continue;
    const key = p.url && p.url.includes('product-detail') ? p.url.toLowerCase() : p.title.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    parsed.push(p);
  }

  const existing = JSON.parse(fs.readFileSync(productsPath, 'utf8'));
  let maxNum = 0;
  existing.forEach((p) => {
    const n = parseInt(String(p.id).replace(/\D/g, ''), 10);
    if (n > maxNum) maxNum = n;
  });

  const existingTitles = new Set(existing.map((p) => p.title.toLowerCase()));
  const existingUrls = new Set(
    existing.map((p) => (p.url || '').toLowerCase()).filter((u) => u.includes('product-detail'))
  );

  const added = [];
  parsed.forEach((p) => {
    if (existingTitles.has(p.title.toLowerCase())) return;
    if (p.url && existingUrls.has(p.url.toLowerCase())) return;
    existingTitles.add(p.title.toLowerCase());
    if (p.url) existingUrls.add(p.url.toLowerCase());
    maxNum += 1;
    added.push({ id: `ym-${String(maxNum).padStart(4, '0')}`, ...p });
  });

  const merged = [...existing, ...added];
  fs.writeFileSync(productsPath, JSON.stringify(merged, null, 2) + '\n');

  const byCat = {};
  added.forEach((p) => {
    byCat[p.category] = (byCat[p.category] || 0) + 1;
  });

  console.log('Input:', path.resolve(input));
  console.log('Parsed:', parsed.length);
  console.log('Added:', added.length);
  console.log('Skipped (duplicates):', parsed.length - added.length);
  console.log('Total products:', merged.length);
  console.log('Added by category:', byCat);
}

main();
