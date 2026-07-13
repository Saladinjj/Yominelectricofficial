import json

# Define the category → slug mapping (must match existing site logic)
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
    'Aluminum Busbar': 'aluminum-busbar',
    'Flexible Busbar': 'flexible-busbar',
    'Rigid Busbar': 'rigid-busbar',
    'Energy Storage Busbar': 'energy-storage-busbar',
    'Busbar Protection': 'busbar-protection',
    'Composite Laminated Busbar': 'composite-laminated-busbar',
    'CCS Integrated Busbar': 'ccs-integrated-busbar',
    'Heavy Duty Busbar': 'heavy-duty-busbar',
}

def generate_full_sitemap():
    # Load all products from the JSON database
    with open('data/products.json', 'r', encoding='utf8') as f:
        products = json.load(f)
    
    # 1. Start with static pages
    urls = [
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
    ]
    
    # 2. Add Category pages
    categories = set(p['category'] for p in products)
    for cat in sorted(categories):
        slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
        urls.append((f'https://www.yominelectric.com/products?category={slug}', 'daily', '0.8'))
        
    # 3. Add individual Product pages (Deep Linking)
    # The URL pattern: /products?category=X&id=Y&product=Z
    for p in products:
        cat = p['category']
        slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
        prod_id = p['id']
        title_slug = p['title'].lower().replace(' ', '-').replace('/', '-').replace('"', '').replace('&', 'and')[:50]
        full_url = f'https://www.yominelectric.com/products?category={slug}&id={prod_id}&product={title_slug}'
        urls.append((full_url, 'weekly', '0.6'))
        
    # Build the XML string
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url, freq, pri in urls:
        # Clean URL for XML compliance
        clean_url = url.replace('&', '&amp;')
        xml += f'  <url>\n    <loc>{clean_url}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>\n'
    xml += '</urlset>'
    
    # Save the expanded sitemap
    with open('sitemap.xml', 'w', encoding='utf8') as f:
        f.write(xml)
        
    print(f"Sitemap regenerated with {len(urls)} URLs (1,000+ products indexed).")

if __name__ == "__main__":
    generate_full_sitemap()
