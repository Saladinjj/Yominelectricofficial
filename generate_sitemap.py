import json

with open('data/products.json', 'r', encoding='utf8') as f:
    products = json.load(f)

# Get unique categories from products
categories = set(p['category'] for p in products)

# Category → slug mapping (same as generate-category-pages.ps1)
SLUG = {
    'Energy Meter': 'energy-meter',
    'Voltage Stabilizer/Regulator': 'voltage-stabilizer-regulator',
    'Current Transformer': 'current-transformer',
    'Variac/Transformer': 'variac-transformer',
    'Screw Machine': 'screw-machine',
    'Terminal & Connector': 'terminal-connector',
    'Solar/PV Products': 'solar-pv-products',
    'Fuse & Protection': 'fuse-protection',
    'Voltage Protector': 'voltage-protector',
    'Socket & Wiring': 'socket-wiring',
    'Tools & Hardware': 'tools-hardware',
    'Security Seal': 'security-seal',
    'Other': 'other',
    # Busbar subcategories
    'Aluminum Busbar': 'aluminum-busbar',
    'Flexible Busbar': 'flexible-busbar',
    'Rigid Busbar': 'rigid-busbar',
    'Energy Storage Busbar': 'energy-storage-busbar',
    'Busbar Protection': 'busbar-protection',
    'Composite Laminated Busbar': 'composite-laminated-busbar',
    'CCS Integrated Busbar': 'ccs-integrated-busbar',
    'Heavy Duty Busbar': 'heavy-duty-busbar',
}

urls = [
    ('https://www.yominelectric.com/', 'weekly', '1.0'),
    ('https://www.yominelectric.com/products', 'daily', '0.9'),
    ('https://www.yominelectric.com/about', 'monthly', '0.7'),
    ('https://www.yominelectric.com/contact', 'monthly', '0.7'),
    ('https://www.yominelectric.com/process', 'monthly', '0.6'),
    ('https://www.yominelectric.com/solutions', 'monthly', '0.7'),
    ('https://www.yominelectric.com/blog', 'weekly', '0.8'),
    ('https://www.yominelectric.com/product-details', 'monthly', '0.7'),
]

# Add all category URLs
for cat in sorted(categories):
    slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
    urls.append((f'https://www.yominelectric.com/products?category={slug}', 'daily', '0.8'))

# Build XML
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url, freq, pri in urls:
    xml += f'  <url><loc>{url}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>\n'
xml += '</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf8') as f:
    f.write(xml)

print(f'Generated sitemap with {len(urls)} URLs')
print(f'Categories: {len(categories)}')
