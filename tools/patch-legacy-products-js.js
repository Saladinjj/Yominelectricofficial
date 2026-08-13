// Hygiene: point the legacy assets/js/products.js card href at the new static pages
const fs = require('fs');
const f = 'C:/Users/Saladin/Desktop/yominelectric-main/assets/js/products.js';
let c = fs.readFileSync(f, 'utf8');
c = c.replace('href="/products?category=${catSlug}&id=${esc(p.id)}"', 'href="/products/${catSlug}/${esc(p.slug || slugify(p.title))}"');
if (!c.includes('function slugify')) {
  c = c.replace('function esc(', "function slugify(s){return String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');}\nfunction esc(");
}
fs.writeFileSync(f, c, 'utf8');
console.log('newHref:', c.includes('href="/products/${catSlug}/${esc(p.slug || slugify(p.title))}"'));
console.log('slugify added:', c.includes('function slugify'));
