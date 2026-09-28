# -*- coding: utf-8 -*-
"""Inject the 2026-09-28 multilingual blog articles into blog.html and sitemap.xml.
Idempotent. Adds all 8 URLs (4 EN, FR, ES, AR for each topic) to sitemap.xml.
"""
import json
import os
import re

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-09-28'

# English cards for blog.html
ENGLISH_POSTS = [
    dict(
        slug='industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter',
        title='Industrial Grid Interconnection & Reactive Power: What Is a Four-Quadrant Energy Meter?',
        kw='what is a four quadrant energy meter &middot; four quadrant meter &middot; bidirectional energy meter &middot; reactive power billing'
    ),
    dict(
        slug='anti-tamper-revenue-protection-what-is-a-split-prepaid-meter',
        title='Utility Revenue Protection & Anti-Tamper: What Is a Split Prepaid Meter?',
        kw='what is a split prepaid meter &middot; split prepayment meter &middot; sts prepaid meter &middot; customer interface unit ciu'
    ),
]

# All 8 URLs for sitemap.xml
ALL_SITEMAP_SLUGS = [
    'industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter',
    'industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-fr',
    'industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-es',
    'industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-ar',
    'anti-tamper-revenue-protection-what-is-a-split-prepaid-meter',
    'anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-fr',
    'anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-es',
    'anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-ar',
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
