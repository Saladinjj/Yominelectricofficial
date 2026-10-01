# -*- coding: utf-8 -*-
"""Inject the 2026-10-01 multilingual blog articles into blog.html and sitemap.xml.
Idempotent. Adds all 8 URLs (4 EN, FR, ES, AR for each topic) to sitemap.xml.
"""
import json
import os
import re

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-10-01'

# English cards for blog.html
ENGLISH_POSTS = [
    dict(
        slug='abc-cable-distribution-what-is-an-insulation-piercing-connector',
        title='Low-Voltage ABC Cable Networks: What Is an Insulation Piercing Connector (IPC)?',
        kw='what is an insulation piercing connector &middot; insulation piercing connector &middot; piercing connector &middot; abc cable piercing connector &middot; insulated piercing clamp'
    ),
    dict(
        slug='industrial-power-billing-what-is-a-maximum-demand-meter',
        title='Industrial Power Billing & Grid Capacity: What Is a Maximum Demand Meter?',
        kw='what is maximum demand &middot; maximum demand meter &middot; maximum demand indicator &middot; what is a maximum demand meter &middot; maximum demand controller'
    ),
]

# All 8 URLs for sitemap.xml
ALL_SITEMAP_SLUGS = [
    'abc-cable-distribution-what-is-an-insulation-piercing-connector',
    'abc-cable-distribution-what-is-an-insulation-piercing-connector-fr',
    'abc-cable-distribution-what-is-an-insulation-piercing-connector-es',
    'abc-cable-distribution-what-is-an-insulation-piercing-connector-ar',
    'industrial-power-billing-what-is-a-maximum-demand-meter',
    'industrial-power-billing-what-is-a-maximum-demand-meter-fr',
    'industrial-power-billing-what-is-a-maximum-demand-meter-es',
    'industrial-power-billing-what-is-a-maximum-demand-meter-ar',
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
