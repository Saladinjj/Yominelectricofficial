const fs = require('fs');
const path = require('path');
const jsonPath = path.join(__dirname, '..', 'data', 'products.json');
const products = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

const BASE = 'https://www.yominelectric.com';

const CAT_SLUG = {
  'Energy Meter': 'energy-meter',
  'Voltage Stabilizer/Regulator': 'voltage-stabilizer-regulator',
  'Current Transformer': 'current-transformer',
  'Screw Machine': 'screw-machine',
  'Variac/Transformer': 'variac-transformer',
  'Terminal & Connector': 'terminal-connector',
  'Solar/PV Products': 'solar-pv-products',
  'Fuse & Protection': 'fuse-protection',
  'Voltage Protector': 'voltage-protector',
  'Socket & Wiring': 'socket-wiring',
  'Tools & Hardware': 'tools-hardware',
  'Security Seal': 'security-seal',
  'Flexible Busbar': 'flexible-busbar',
  'Rigid Busbar': 'rigid-busbar',
  'Aluminum Busbar': 'aluminum-busbar',
  'Composite Laminated Busbar': 'composite-laminated-busbar',
  'CCS Integrated Busbar': 'ccs-integrated-busbar',
  'Heavy Duty Busbar': 'heavy-duty-busbar',
  'Energy Storage Busbar': 'energy-storage-busbar',
  'Busbar Protection': 'busbar-protection',
  'Other': 'other',
};

let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${BASE}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>${BASE}/products</loc><changefreq>daily</changefreq><priority>0.9</priority></url>
  <url><loc>${BASE}/about</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>${BASE}/contact</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>${BASE}/process</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>
  <url><loc>${BASE}/solutions</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>${BASE}/blog</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>${BASE}/blog-nepal-loading</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>\n`;

// Category pages
const cats = [...new Set(products.map(p => p.category))];
cats.forEach(cat => {
  const slug = CAT_SLUG[cat];
  if (slug) {
    xml += `  <url><loc>${BASE}/products?category=${slug}</loc><changefreq>daily</changefreq><priority>0.8</priority></url>\n`;
  }
});

// Product pages
products.forEach(p => {
  const slug = CAT_SLUG[p.category] || 'other';
  xml += `  <url><loc>${BASE}/products?category=${slug}&amp;id=${p.id}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>\n`;
});

xml += '</urlset>';

const outPath = path.join(__dirname, '..', 'sitemap.xml');
fs.writeFileSync(outPath, xml);
console.log(`Sitemap written: ${products.length} products, ${cats.length} categories`);
