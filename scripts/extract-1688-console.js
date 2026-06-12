/**
 * Run this in the browser DevTools console on:
 * https://shop4b942d841w388.1688.com/page/offerlist.htm
 *
 * Scroll to the bottom first so all products load, then paste & run.
 * Copy the printed JSON into data/1688-shop-raw.json and run:
 *   node scripts/import-1688-shop.js
 */
(function extract1688Shop() {
  const seen = new Set();
  const products = [];

  function add(item) {
    const title = (item.title || '').replace(/\s+/g, ' ').trim();
    if (!title || title.length < 4) return;
    const key = title.toLowerCase();
    if (seen.has(key)) return;
    seen.add(key);
    products.push({
      title,
      price: (item.price || '').trim(),
      image: item.image || '',
      url: item.url || '',
      offerId: item.offerId || '',
    });
  }

  document.querySelectorAll('a[href*="detail.1688.com/offer/"]').forEach((a) => {
    const card = a.closest('li,div,article') || a;
    const img = card.querySelector('img');
    const m = a.href.match(/offer\/(\d+)/);
    add({
      title: a.getAttribute('title') || a.textContent,
      url: a.href,
      offerId: m ? m[1] : '',
      image: (img && (img.src || img.getAttribute('data-src') || img.getAttribute('data-lazy-src'))) || '',
      price: (card.querySelector('[class*="price"]') || {}).textContent || '',
    });
  });

  // Fallback: window state blobs some shops expose
  try {
    const dump = JSON.stringify(window);
    const re = /"subject":"([^"]{4,})".{0,400}?"offerId":(\d+)/g;
    let m;
    while ((m = re.exec(dump))) {
      add({ title: m[1], offerId: m[2], url: `https://detail.1688.com/offer/${m[2]}.html` });
    }
  } catch (e) {
    /* ignore */
  }

  const payload = {
    shopUrl: location.href,
    scrapedAt: new Date().toISOString(),
    count: products.length,
    products,
  };

  console.log(`Found ${products.length} products`);
  console.log(JSON.stringify(payload, null, 2));
  return payload;
})();
