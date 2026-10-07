# -*- coding: utf-8 -*-
"""Inject the 2026-10-07 multilingual blog articles into blog.html and sitemap.xml.
Idempotent. Adds all 8 URLs (4 EN, FR, ES, AR for each topic) to sitemap.xml.
"""
import json
import os
import re

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-10-07'

# English cards for blog.html
ENGLISH_POSTS = [
    dict(
        slug='bess-battery-safety-what-is-a-manual-service-disconnect',
        title='Battery Energy Storage Systems (BESS): What Is a Manual Service Disconnect (MSD)?',
        kw='what is a manual service disconnect &middot; manual service disconnect &middot; msd connector &middot; high voltage msd &middot; bess manual service disconnect'
    ),
    dict(
        slug='feeder-pillars-what-is-a-j-type-fuse-cutout',
        title='Utility Feeder Pillars & Substation Protection: What Is a J-Type Fuse Cutout?',
        kw='what is a j type fuse cutout &middot; j type fuse cutout &middot; j-type fuse cut out &middot; feeder pillar fuse &middot; wedge type fuse carrier'
    ),
]

# All 8 URLs for sitemap.xml
ALL_SITEMAP_SLUGS = [
    'bess-battery-safety-what-is-a-manual-service-disconnect',
    'bess-battery-safety-what-is-a-manual-service-disconnect-fr',
    'bess-battery-safety-what-is-a-manual-service-disconnect-es',
    'bess-battery-safety-what-is-a-manual-service-disconnect-ar',
    'feeder-pillars-what-is-a-j-type-fuse-cutout',
    'feeder-pillars-what-is-a-j-type-fuse-cutout-fr',
    'feeder-pillars-what-is-a-j-type-fuse-cutout-es',
    'feeder-pillars-what-is-a-j-type-fuse-cutout-ar',
]

# 1. Update blog.html
h = open(BLOG_HTML, encoding='utf-8').read()

block = ''
for p in ENGLISH_POSTS:
    if 'href="/blog/%s"' % p['slug'] in h:
        continue
    block += (
        '    <a class="blog-line" data-category="guides" data-lang="en" href="/blog/%(slug)s">\n'
        '      <img class="blog-line-img" src="/assets/images/blog/%(slug)s/card.png" alt="%(title)s" loading="lazy" onerror="this.style.display=\'none\'">\n'
        '      <div class="blog-line-body">\n'
        '        <h3 class="blog-line-title">%(title)s</h3>\n'
        '        <p class="blog-line-kw">%(kw)s</p>\n'
        '      </div>\n'
        '    </a>\n' % p)

if block:
    m = re.search(r'(<div class="post-grid" id="post-grid">\s*\n)', h)
    if not m:
        raise SystemExit('post-grid anchor not found')
    h = h[:m.end()] + block + h[m.end():]

added = []
for p in ENGLISH_POSTS:
    if '"%s/blog/%s"' % (SITE, p['slug']) in h:
        continue
    entry = json.dumps({
        "@type": "BlogPosting",
        "headline": p['title'],
        "url": "%s/blog/%s" % (SITE, p['slug']),
        "datePublished": DATE,
        "dateModified": DATE,
        "image": "%s/assets/images/blog/%s/card.png" % (SITE, p['slug']),
    }, ensure_ascii=False)
    m = re.search(r'"blogPost"\s*:\s*\[', h)
    if not m:
        raise SystemExit('blogPost array not found')
    h = h[:m.end()] + entry + ',\n    ' + h[m.end():]
    added.append(p['slug'])

open(BLOG_HTML, 'w', encoding='utf-8', newline='').write(h)
print('blog.html cards+jsonld added: %s' % (added or 'none (already present)'))

# 2. Update sitemap.xml with all 8 multilingual URLs
s = open(SITEMAP, encoding='utf-8').read()
before = s.count('<loc>')
new_urls = []
for slug in ALL_SITEMAP_SLUGS:
    u = '%s/blog/%s' % (SITE, slug)
    if '<loc>%s</loc>' % u in s:
        continue
    s = s.replace('</urlset>',
                  '  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                  '    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n</urlset>'
                  % (u, DATE))
    new_urls.append(slug)
open(SITEMAP, 'w', encoding='utf-8', newline='').write(s)
print('sitemap <loc>: %d -> %d   added: %s' % (before, s.count('<loc>'), new_urls or 'none'))
