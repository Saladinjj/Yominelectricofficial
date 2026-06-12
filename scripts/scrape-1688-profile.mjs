/**
 * Scrape 1688 using local Edge profile (may work if user is logged in).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright-core';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const SHOP_URL = 'https://shop4b942d841w388.1688.com/page/offerlist.htm';
const OUT = path.join(ROOT, 'data', '1688-shop-raw.json');
const PROFILE = path.join(process.env.LOCALAPPDATA || '', 'Microsoft', 'Edge', 'User Data');

function normalize(raw) {
  const offerId = String(raw.offerId || raw.id || '').trim();
  const title = String(raw.subject || raw.title || '').replace(/\s+/g, ' ').trim();
  if (!title || title.length < 4) return null;
  let image = raw.imageUrl || raw.picUrl || raw.image || '';
  if (image.startsWith('//')) image = `https:${image}`;
  const m = String(raw.url || '').match(/offer\/(\d+)/);
  const id = offerId || (m ? m[1] : '');
  return {
    offerId: id,
    title,
    price: String(raw.price || '').trim(),
    image,
    url: id ? `https://detail.1688.com/offer/${id}.html` : (raw.url || ''),
  };
}

async function main() {
  console.log('Using Edge profile:', PROFILE);
  const context = await chromium.launchPersistentContext(PROFILE, {
    channel: 'msedge',
    headless: false,
    args: ['--profile-directory=Default'],
  });
  const page = context.pages()[0] || await context.newPage();
  const products = [];
  const seen = new Set();

  page.on('response', async (res) => {
    try {
      const url = res.url();
      if (!/mtop|offer|module|recommend|alisite/i.test(url)) return;
      const text = await res.text();
      const json = JSON.parse(text.replace(/^[^{[]*/, '').replace(/[);]+$/, ''));
      const stack = [json];
      while (stack.length) {
        const cur = stack.pop();
        if (!cur || typeof cur !== 'object') continue;
        if (Array.isArray(cur)) {
          cur.forEach((x) => stack.push(x));
          continue;
        }
        if (cur.subject || cur.title) {
          const n = normalize(cur);
          if (n && !seen.has(n.title.toLowerCase())) {
            seen.add(n.title.toLowerCase());
            products.push(n);
          }
        }
        Object.values(cur).forEach((v) => stack.push(v));
      }
    } catch {
      /* ignore */
    }
  });

  await page.goto(SHOP_URL, { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.waitForTimeout(6000);
  for (let i = 0; i < 15; i++) {
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await page.waitForTimeout(1200);
  }

  const dom = await page.evaluate(() =>
    [...document.querySelectorAll('a[href*="detail.1688.com/offer/"]')].map((a) => {
      const card = a.closest('li,div') || a;
      const img = card.querySelector('img');
      return {
        title: (a.getAttribute('title') || a.textContent || '').trim(),
        url: a.href,
        image: img?.src || img?.getAttribute('data-src') || '',
        price: card.querySelector('[class*="price"]')?.textContent?.trim() || '',
      };
    })
  );

  dom.forEach((d) => {
    const n = normalize(d);
    if (n && !seen.has(n.title.toLowerCase())) {
      seen.add(n.title.toLowerCase());
      products.push(n);
    }
  });

  const title = await page.title();
  const html = await page.content();
  await context.close();

  const payload = {
    shopUrl: SHOP_URL,
    scrapedAt: new Date().toISOString(),
    pageTitle: title,
    blocked: /captcha|登录|punish|nocaptcha/i.test(html) && products.length === 0,
    count: products.length,
    products,
  };
  fs.writeFileSync(OUT, JSON.stringify(payload, null, 2) + '\n');
  console.log('title:', title);
  console.log('products:', products.length);
  console.log('saved:', OUT);
  process.exit(payload.blocked ? 2 : 0);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
