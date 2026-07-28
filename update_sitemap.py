import json, re, html, os
from datetime import datetime, timezone

SLUG = {
    'Energy Meter': 'energy-meter', 'Voltage Stabilizer/Regulator': 'voltage-stabilizer-regulator',
    'Current Transformer': 'current-transformer', 'Screw Machine': 'screw-machine',
    'Screw Machines': 'screw-machine', 'Terminal & Connector': 'terminal-connector',
    'Solar/PV Products': 'solar-pv-products', 'Fuse & Protection': 'fuse-protection',
    'Voltage Protector': 'voltage-protector', 'Socket & Wiring': 'socket-wiring',
    'Tools & Hardware': 'tools-hardware', 'Security Seal': 'security-seal', 'Other': 'other',
    'Aluminum Busbar': 'aluminum-busbar', 'Flexible Busbar': 'flexible-busbar',
    'Rigid Busbar': 'rigid-busbar', 'Energy Storage Busbar': 'energy-storage-busbar',
    'Busbar Protection': 'busbar-protection', 'Composite Laminated Busbar': 'composite-laminated-busbar',
    'CCS Integrated Busbar': 'ccs-integrated-busbar', 'Heavy Duty Busbar': 'heavy-duty-busbar'
}

today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

new_pages = [
    ('https://www.yominelectric.com/guide/energy-meter-types', 'monthly', '0.7', today),
    ('https://www.yominelectric.com/guide/current-transformer-selection', 'monthly', '0.7', today),
    ('https://www.yominelectric.com/guide/voltage-stabilizer-buying-guide', 'monthly', '0.7', today),
    ('https://www.yominelectric.com/compare/single-phase-vs-three-phase-meter', 'monthly', '0.7', today),
    ('https://www.yominelectric.com/compare/prepaid-vs-postpaid-meter', 'monthly', '0.7', today),
]

with open('data/products.json', 'r', encoding='utf8') as f:
    products = json.load(f)

urls = []

# Static pages
static = [
    ('https://www.yominelectric.com/', 'weekly', '1.0'),
    ('https://www.yominelectric.com/products', 'daily', '0.9'),
    ('https://www.yominelectric.com/about', 'monthly', '0.7'),
    ('https://www.yominelectric.com/contact', 'monthly', '0.7'),
    ('https://www.yominelectric.com/process', 'monthly', '0.6'),
    ('https://www.yominelectric.com/solutions', 'monthly', '0.7'),
    ('https://www.yominelectric.com/blog', 'weekly', '0.8'),
    ('https://www.yominelectric.com/privacy-policy', 'monthly', '0.5'),
    ('https://www.yominelectric.com/shipping-policy', 'monthly', '0.5'),
    ('https://www.yominelectric.com/return-policy', 'monthly', '0.5'),
    ('https://www.yominelectric.com/terms-and-conditions', 'monthly', '0.5'),
    ('https://www.yominelectric.com/blog-nepal-loading', 'monthly', '0.6'),
]
for url, freq, pri in static:
    urls.append((url, freq, pri, today))

# NEW guide and compare pages
for url, freq, pri, lm in new_pages:
    urls.append((url, freq, pri, lm))

# Categories
cats = set(p['category'] for p in products)
for cat in sorted(cats):
    slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
    urls.append((f'https://www.yominelectric.com/products?category={slug}', 'daily', '0.8', today))

# Products
for p in products:
    cat = p['category']
    slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
    prod_id = p['id']
    title = html.unescape(p['title'])
    title_slug = title.lower().replace('&', 'and').replace('/', '-').replace('"', '')
    title_slug = re.sub(r'[^a-z0-9-]', '', title_slug).strip('-')[:60]
    full_url = f'https://www.yominelectric.com/products?category={slug}&id={prod_id}&product={title_slug}'
    urls.append((full_url, 'weekly', '0.6', today))

# Build XML
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url, freq, pri, lm in urls:
    clean = url.replace('&', '&amp;')
    xml += f'  <url>\n    <loc>{clean}</loc>\n    <lastmod>{lm}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>\n'
xml += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf8') as f:
    f.write(xml)

print(f"Sitemap regenerated with {len(urls)} URLs (+5 new guide/compare pages)")
