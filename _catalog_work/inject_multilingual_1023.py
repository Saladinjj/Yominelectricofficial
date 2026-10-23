# -*- coding: utf-8 -*-
"""Inject the 2026-10-23 articles into blog.html and sitemap.xml (idempotent)."""
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-10-23'

ENGLISH_POSTS = [
    dict(
        slug='din-rail-terminal-block-wiring-how-to',
        title='DIN Rail Terminal Block Wiring: A Step-by-Step Installation Guide',
        kw='how to use din rail terminal blocks &middot; din rail terminal block &middot; how to wire din rail terminal blocks &middot; din rail terminal block wiring',
    ),
    dict(
        slug='air-conditioner-voltage-stabilizer-sizing',
        title='Voltage Stabilizer for Air Conditioners: Sizing, Types and Installation',
        kw='voltage stabilizer for air conditioner &middot; air conditioner voltage stabilizer &middot; voltage stabilizer for ac &middot; air conditioner stabilizer',
    ),
]

SLUGS = []
for p in ENGLISH_POSTS:
    SLUGS += [p['slug'], p['slug'] + '-fr', p['slug'] + '-es', p['slug'] + '-ar']

# 1. blog.html cards
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
        '    </a>\n' % p
    )

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

# 2. sitemap.xml
s = open(SITEMAP, encoding='utf-8').read()
before = s.count('<loc>')
new_urls = []
for slug in SLUGS:
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
