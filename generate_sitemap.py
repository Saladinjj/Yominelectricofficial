import json
import html
import os
import re
from datetime import datetime, timezone

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

# Map static pages to their HTML files for lastmod detection
STATIC_PAGE_FILES = {
    'https://www.yominelectric.com/': 'index.html',
    'https://www.yominelectric.com/products': 'products.html',
    'https://www.yominelectric.com/about': 'about.html',
    'https://www.yominelectric.com/contact': 'contact.html',
    'https://www.yominelectric.com/process': 'process.html',
    'https://www.yominelectric.com/solutions': 'solutions.html',
    'https://www.yominelectric.com/blog': 'blog.html',
    'https://www.yominelectric.com/privacy-policy': 'privacy-policy.html',
    'https://www.yominelectric.com/shipping-policy': 'shipping-policy.html',
    'https://www.yominelectric.com/return-policy': 'return-policy.html',
    'https://www.yominelectric.com/terms-and-conditions': 'terms-and-conditions.html',
}

def get_file_lastmod(filename):
    """Get ISO-8601 last modified date for a file. Falls back to today."""
    try:
        mtime = os.path.getmtime(filename)
        return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%d')
    except OSError:
        return datetime.now(timezone.utc).strftime('%Y-%m-%d')

def clean_title_for_slug(title):
    """Decode HTML entities, then create a URL-safe slug."""
    # First decode any HTML entities like &amp; &quot; etc.
    decoded = html.unescape(title)
    # Lowercase and replace special characters
    slug = decoded.lower()
    slug = slug.replace('&', 'and')
    slug = slug.replace('/', '-')
    slug = slug.replace('"', '')
    slug = re.sub(r'[^a-z0-9-]', '', slug)  # remove non-alphanumeric (keep hyphens)
    slug = re.sub(r'-+', '-', slug)  # collapse multiple hyphens
    slug = slug.strip('-')
    return slug[:50]

def xml_escape(url):
    """Escape & to &amp; for XML compliance."""
    return url.replace('&', '&amp;')

def generate_full_sitemap():
    # Load all products from the JSON database
    with open('data/products.json', 'r', encoding='utf8') as f:
        products = json.load(f)
    
    # Get master lastmod from products.json timestamp
    master_lastmod = get_file_lastmod('data/products.json')
    
    urls = []
    
    # 1. Static pages with individual file lastmod
    static_pages = [
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
    for url, freq, pri in static_pages:
        filename = STATIC_PAGE_FILES.get(url, 'index.html')
        lastmod = get_file_lastmod(filename)
        urls.append((url, freq, pri, lastmod))
    
    # 2. Category pages
    categories = set(p['category'] for p in products)
    for cat in sorted(categories):
        slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
        urls.append((f'https://www.yominelectric.com/products?category={slug}', 'daily', '0.8', master_lastmod))
        
    # 3. Individual Product pages
    for p in products:
        cat = p['category']
        slug = SLUG.get(cat, cat.lower().replace(' & ', '-').replace('/', '-').replace(' ', '-'))
        prod_id = p['id']
        title_slug = clean_title_for_slug(p['title'])
        full_url = f'https://www.yominelectric.com/products?category={slug}&id={prod_id}&product={title_slug}'
        urls.append((full_url, 'weekly', '0.6', master_lastmod))
        
    # Build the XML string
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url, freq, pri, lastmod in urls:
        clean_url = xml_escape(url)
        xml += f'  <url>\n'
        xml += f'    <loc>{clean_url}</loc>\n'
        xml += f'    <lastmod>{lastmod}</lastmod>\n'
        xml += f'    <changefreq>{freq}</changefreq>\n'
        xml += f'    <priority>{pri}</priority>\n'
        xml += f'  </url>\n'
    xml += '</urlset>'
    
    # Save the expanded sitemap
    with open('sitemap.xml', 'w', encoding='utf8') as f:
        f.write(xml)
        
    print(f"Sitemap regenerated with {len(urls)} URLs ({len(products)} products + {len(static_pages)} pages + {len(categories)} categories).")
    print(f"Lastmod dates included for all URLs.")

if __name__ == "__main__":
    generate_full_sitemap()
