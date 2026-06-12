/**
 * Import 1688 shop products into data/products.json
 *
 * Input (first match wins):
 *   1) node scripts/import-1688-shop.js path/to/offerlist.html
 *   2) node scripts/import-1688-shop.js path/to/1688-shop-raw.json
 *   3) data/1688-offerlist.html
 *   4) data/1688-shop-raw.json
 *   5) path/to/shop-export.csv  (image + title columns)
 *
 * Multiple files: node scripts/import-1688-shop.js file1.csv file2.csv
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const productsPath = path.join(ROOT, 'data/products.json');
const SHOP_URL = 'https://shop4b942d841w388.1688.com/page/offerlist.htm';

const CAT_RULES = [
  [/energy\s*meter|kwh|kilowatt|electricity\s*meter|电表|电能表/i, 'Energy Meter'],
  [/current\s*transformer|\bct\b|互感器/i, 'Current Transformer'],
  [/over[- ]?voltage|under[- ]?voltage|voltage\s*protector|voltage\s*monitor/i, 'Voltage Protector'],
  [/voltage\s*stabilizer|voltage\s*regulator|\bavr\b|稳压|调压/i, 'Voltage Stabilizer/Regulator'],
  [/variac|autotransformer|变压器/i, 'Variac/Transformer'],
  [/circuit\s*breaker|\bmcb\b|miniature\s*circuit/i, 'Fuse & Protection'],
  [/isolat(ing|or)\s*switch|knife\s*switch|disconnect\s*switch|fuse\s*switch/i, 'Fuse & Protection'],
  [/wire\s*clamp|piercing\s*clamp|tension\s*clamp|brancher|power\s*fittings?/i, 'Terminal & Connector'],
  [/busbar|铜排|母线/i, 'Flexible Busbar'],
  [/screw\s*machine|攻丝|钻孔/i, 'Screw Machine'],
  [/solar|pv|光伏/i, 'Solar/PV Products'],
  [/fuse|fire\s*extinguish|断路|保护器/i, 'Fuse & Protection'],
  [/socket|plug|插座|插头/i, 'Socket & Wiring'],
  [/terminal|connector|端子/i, 'Terminal & Connector'],
  [/seal|铅封/i, 'Security Seal'],
  [/tool|hardware|工具/i, 'Tools & Hardware'],
  [/tile\s*level/i, 'Tile Leveling System'],
  [/transfer\s*switch/i, 'Fuse & Protection'],
];

function guessCategory(title, hint) {
  const text = `${title} ${hint || ''}`;
  for (const [re, cat] of CAT_RULES) {
    if (re.test(text)) return cat;
  }
  return 'Other';
}

function decodeHtml(s) {
  return String(s || '')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

function fixImage(url) {
  if (!url) return '';
  let u = decodeHtml(url);
  if (u.startsWith('//')) u = `https:${u}`;
  u = u.replace(/\.\d+x\d+\.(jpg|png|webp)/i, '.$1');
  return u;
}

function parseFromCsv(filePath) {
  const lines = fs.readFileSync(filePath, 'utf8').split(/\r?\n/).filter(Boolean);
  const out = [];
  for (let i = 0; i < lines.length; i++) {
    if (i === 0 && /main-picture|tablescraper|title|subject/i.test(lines[i])) continue;
    const m = lines[i].match(/^"([^"]*)"\s*,\s*"([^"]*)"\s*$/);
    if (!m) continue;
    const image = fixImage(m[1]);
    const title = decodeHtml(m[2]);
    if (!title || title.length < 4) continue;
    out.push({ title, image, price: '', url: SHOP_URL, categoryHint: '', moq: '' });
  }
  return out;
}

function parseFile(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (ext === '.json') return parseFromJson(filePath);
  if (ext === '.csv') return parseFromCsv(filePath);
  return parseFromHtml(fs.readFileSync(filePath, 'utf8'));
}

function mergeParsed(lists) {
  const out = [];
  const seen = new Set();
  lists.flat().forEach((p) => {
    const key = p.title.toLowerCase();
    if (seen.has(key)) return;
    seen.add(key);
    out.push(p);
  });
  return out;
}

function parsePrice(raw) {
  const p = decodeHtml(raw).replace(/[^\d.,¥$\-–—\s]/g, ' ').replace(/\s+/g, ' ').trim();
  if (!p) return '';
  if (/^[\d.,]+(\s*[-–—]\s*[\d.,]+)?$/.test(p)) return `¥${p}`;
  return p;
}

function parseFromJson(filePath) {
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const list = Array.isArray(data) ? data : data.products || [];
  return list
    .map((p) => ({
      title: decodeHtml(p.title || p.subject || ''),
      price: parsePrice(p.price || p.priceRange || ''),
      image: fixImage(p.image || p.imageUrl || p.picUrl || ''),
      url: p.url || (p.offerId ? `https://detail.1688.com/offer/${p.offerId}.html` : ''),
      categoryHint: p.categoryHint || p.category || '',
      moq: p.moq ? String(p.moq) : '',
    }))
    .filter((p) => p.title.length > 3);
}

function parseFromHtml(html) {
  const out = [];
  const seen = new Set();

  const add = (item) => {
    const title = decodeHtml(item.title);
    if (!title || title.length < 4) return;
    const key = title.toLowerCase();
    if (seen.has(key)) return;
    seen.add(key);
    out.push({
      title,
      price: parsePrice(item.price),
      image: fixImage(item.image),
      url: item.url || '',
      categoryHint: item.categoryHint || '',
      moq: item.moq || '',
    });
  };

  // Embedded JSON blobs
  const jsonRe = /"subject"\s*:\s*"([^"]{4,})"/g;
  let m;
  while ((m = jsonRe.exec(html))) {
    const block = html.slice(m.index, m.index + 2500);
    const offerM = block.match(/"offerId"\s*:\s*"?(\d+)"?/);
    const imgM = block.match(/"(?:imageUrl|imgUrl|picUrl)"\s*:\s*"([^"]+)"/);
    const priceM = block.match(/"price"\s*:\s*"([^"]+)"/);
    add({
      title: m[1],
      url: offerM ? `https://detail.1688.com/offer/${offerM[1]}.html` : '',
      image: imgM ? imgM[1] : '',
      price: priceM ? priceM[1] : '',
    });
  }

  // Anchor cards
  const linkRe = /<a[^>]+href="([^"]*detail\.1688\.com\/offer\/(\d+)[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi;
  while ((m = linkRe.exec(html))) {
    const href = m[1].startsWith('http') ? m[1] : `https:${m[1]}`;
    const inner = m[3];
    const title =
      (inner.match(/title="([^"]+)"/) || [])[1] ||
      decodeHtml(inner.replace(/<[^>]+>/g, ' '));
    const imgM = inner.match(/<img[^>]+(?:src|data-src|data-lazy-src)="([^"]+)"/i);
    const priceM = inner.match(/class="[^"]*price[^"]*"[^>]*>([^<]+)/i);
    add({ title, url: href, image: imgM ? imgM[1] : '', price: priceM ? priceM[1] : '' });
  }

  return out;
}

function resolveInputs(args) {
  if (args.length) {
    return args.map((a) => path.resolve(a)).filter((p) => fs.existsSync(p));
  }
  const defaults = [
    path.join(ROOT, 'data/1688-offerlist.html'),
    path.join(ROOT, 'data/1688-shop-raw.json'),
    path.join(process.env.TEMP || '', '1688-offerlist.html'),
  ];
  const hit = defaults.find((p) => fs.existsSync(p));
  return hit ? [hit] : [];
}

function buildProduct(parsed, idNum) {
  const specs = {};
  if (parsed.moq) specs.MOQ = parsed.moq;
  if (parsed.price) specs['Price (1688)'] = parsed.price;
  const cat = guessCategory(parsed.title, parsed.categoryHint);
  const catLabel = cat.replace(/\//g, ' ').toLowerCase();
  return {
    id: `ym-${String(idNum).padStart(4, '0')}`,
    title: parsed.title,
    category: cat,
    price: parsed.price || undefined,
    description: `Listed on Yomin Electric 1688 shop. Contact us for export pricing, MOQ, and lead time.`,
    specs,
    image: parsed.image || 'https://www.yominelectric.com/logo.png',
    url: parsed.url || SHOP_URL,
    source: '1688',
    isNew: true,
    keywords: ['1688', 'yomin electric', catLabel, parsed.title.toLowerCase().slice(0, 60)],
  };
}

function main() {
  const inputs = resolveInputs(process.argv.slice(2));
  if (!inputs.length) {
    console.error('No input file found. Pass CSV/JSON/HTML paths or save data/1688-shop-raw.json');
    process.exit(1);
  }

  const parsed = mergeParsed(inputs.map(parseFile));

  if (!parsed.length) {
    console.error('No products parsed from', inputs.join(', '));
    process.exit(1);
  }

  const existing = JSON.parse(fs.readFileSync(productsPath, 'utf8'));
  let maxNum = 0;
  existing.forEach((p) => {
    const n = parseInt(String(p.id).replace(/\D/g, ''), 10);
    if (n > maxNum) maxNum = n;
  });

  const genericUrls = new Set([SHOP_URL.toLowerCase()]);
  const existingTitles = new Set(existing.map((p) => p.title.toLowerCase()));
  const existingUrls = new Set(
    existing
      .map((p) => (p.url || '').toLowerCase())
      .filter((u) => u && !genericUrls.has(u))
  );
  const added = [];

  parsed.forEach((p) => {
    const key = p.title.toLowerCase();
    if (existingTitles.has(key)) return;
    const urlKey = (p.url || '').toLowerCase();
    if (urlKey && !genericUrls.has(urlKey) && existingUrls.has(urlKey)) return;
    existingTitles.add(key);
    if (urlKey && !genericUrls.has(urlKey)) existingUrls.add(urlKey);
    maxNum += 1;
    added.push(buildProduct(p, maxNum));
  });

  const merged = [...existing, ...added];
  fs.writeFileSync(productsPath, JSON.stringify(merged, null, 2) + '\n');

  const byCat = {};
  added.forEach((p) => {
    byCat[p.category] = (byCat[p.category] || 0) + 1;
  });

  console.log('Input:', inputs.join(', '));
  console.log('Parsed:', parsed.length);
  console.log('Added:', added.length);
  console.log('Skipped (duplicates):', parsed.length - added.length);
  console.log('Total products:', merged.length);
  console.log('Added by category:', byCat);
}

main();
