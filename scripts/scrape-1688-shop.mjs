/**
 * Scrape 1688 shop offer list via browser (Edge/Chrome).
 * Usage: node scripts/scrape-1688-shop.mjs [output.json]
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const SHOP_URL = 'https://shop4b942d841w388.1688.com/page/offerlist.htm';
const OUT = path.resolve(process.argv[2] || path.join(ROOT, 'data', '1688-shop-raw.json'));

async function loadPlaywright() {
  try {
    return await import('playwright');
  } catch {
    return await import('playwright-core');
  }
}

async function launchBrowser(pw) {
  const channels = ['msedge', 'chrome', 'chromium'];
  for (const channel of channels) {
    try {
      const browser = await pw.chromium.launch({ channel, headless: true });
      console.log('Launched browser:', channel);
      return browser;
    } catch (e) {
      console.log('Channel failed:', channel, e.message?.slice(0, 80));
    }
  }
  throw new Error('No browser available. Install Edge/Chrome or run: npx playwright install chromium');
}

function pickImage(item) {
  const img =
    item.imageUrl ||
    item.image?.imgUrl ||
    item.offerImage?.imageUrl ||
    item.picUrl ||
    item.imgUrl ||
    (Array.isArray(item.imageList) && item.imageList[0]) ||
    '';
  if (!img) return '';
  return img.startsWith('//') ? `https:${img}` : img;
}

function pickPrice(item) {
  const p =
    item.price ||
    item.priceInfo?.price ||
    item.tradePrice?.offerPrice?.price ||
    item.offerPrice ||
    '';
  if (typeof p === 'number') return `¥${p}`;
  return String(p || '').trim();
}

function normalizeItem(raw) {
  const offerId = String(raw.offerId || raw.id || raw.productId || '').trim();
  const title = String(raw.subject || raw.title || raw.offerTitle || '').replace(/\s+/g, ' ').trim();
  if (!title) return null;
  return {
    offerId,
    title,
    price: pickPrice(raw),
    image: pickImage(raw),
    url: offerId ? `https://detail.1688.com/offer/${offerId}.html` : '',
    categoryHint: raw.categoryName || raw.leafCategoryName || raw.postCategoryName || '',
    moq: raw.moq || raw.minOrderQuantity || raw.tradeQuantity?.minQuantity || '',
  };
}

function extractFromJson(obj, out, seen) {
  if (!obj || typeof obj !== 'object') return;
  if (Array.isArray(obj)) {
    obj.forEach((x) => extractFromJson(x, out, seen));
    return;
  }
  const title = obj.subject || obj.title || obj.offerTitle;
  const id = obj.offerId || obj.id;
  if (title && (id || obj.imageUrl || obj.picUrl || obj.price)) {
    const n = normalizeItem(obj);
    if (n && !seen.has(n.title.toLowerCase())) {
      seen.add(n.title.toLowerCase());
      out.push(n);
    }
  }
  Object.values(obj).forEach((v) => extractFromJson(v, out, seen));
}

async function scrape() {
  const pw = await loadPlaywright();
  const browser = await launchBrowser(pw);
  const context = await browser.newContext({
    userAgent:
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    locale: 'zh-CN',
  });
  const page = await context.newPage();
  const collected = [];
  const seen = new Set();

  page.on('response', async (res) => {
    try {
      const url = res.url();
      if (!/mtop|offer|module|recommend|alisite|json/i.test(url)) return;
      const ct = res.headers()['content-type'] || '';
      if (!/json|javascript|text/i.test(ct)) return;
      const text = await res.text();
      const jsonText = text.replace(/^[^{[]*/, '').replace(/[);]+$/, '');
      const data = JSON.parse(jsonText);
      extractFromJson(data, collected, seen);
    } catch {
      /* ignore parse errors */
    }
  });

  console.log('Opening', SHOP_URL);
  await page.goto(SHOP_URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(5000);

  // Scroll to load lazy pages
  for (let i = 0; i < 12; i++) {
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await page.waitForTimeout(1500);
  }

  // DOM fallback
  const domItems = await page.evaluate(() => {
    const cards = [...document.querySelectorAll('[data-offer-id], .offer-list-item, .offer-card, .sm-offer-item, .offer-item')];
    const links = [...document.querySelectorAll('a[href*="detail.1688.com/offer/"]')];
    const out = [];
    const add = (title, href, img, price) => {
      const t = (title || '').replace(/\s+/g, ' ').trim();
      if (!t || t.length < 4) return;
      out.push({ title: t, url: href || '', image: img || '', price: price || '' });
    };
    cards.forEach((el) => {
      const a = el.querySelector('a[href*="offer"]') || el.closest('a');
      const img = el.querySelector('img');
      const title =
        el.getAttribute('title') ||
        el.querySelector('.title, .offer-title, .sm-offer-title, [class*="title"]')?.textContent;
      const price = el.querySelector('.price, [class*="price"]')?.textContent;
      add(title, a?.href, img?.src || img?.getAttribute('data-src'), price);
    });
    links.forEach((a) => {
      const card = a.closest('[class*="offer"], li, .card') || a;
      const img = card.querySelector('img');
      add(a.textContent, a.href, img?.src || img?.getAttribute('data-src'), '');
    });
    return out;
  });

  domItems.forEach((raw) => {
    const m = String(raw.url || '').match(/offer\/(\d+)/);
    const n = normalizeItem({
      subject: raw.title,
      offerId: m ? m[1] : '',
      imageUrl: raw.image,
      price: raw.price,
    });
    if (n && !seen.has(n.title.toLowerCase())) {
      seen.add(n.title.toLowerCase());
      collected.push(n);
    }
  });

  const html = await page.content();
  const title = await page.title();
  await browser.close();

  const payload = {
    shopUrl: SHOP_URL,
    scrapedAt: new Date().toISOString(),
    pageTitle: title,
    blocked: /captcha|验证|punish|nocaptcha/i.test(html) && collected.length === 0,
    count: collected.length,
    products: collected,
  };

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(payload, null, 2) + '\n');
  console.log('Saved', collected.length, 'products to', OUT);
  if (payload.blocked) {
    console.log('Page may be captcha-blocked. Open the shop in your browser, save the page HTML, then run import-1688-shop.js with that file.');
    process.exit(2);
  }
}

scrape().catch((err) => {
  console.error(err);
  process.exit(1);
});
