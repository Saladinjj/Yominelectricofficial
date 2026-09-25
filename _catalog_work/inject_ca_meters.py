# -*- coding: utf-8 -*-
"""Add the four Central Asia & Metering blogs to blog.html (cards + blogPost JSON-LD) and
sitemap.xml. Idempotent."""
import json
import os
import re

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-09-25'

POSTS = [
    dict(slug='substation-measurement-what-is-a-current-transformer',
         title='Substation & Industrial Power Measurement: What Is a Current Transformer?',
         kw='what is a current transformer &middot; substation current transformer &middot; askue metering ct &middot; class 0.5s ct'),
    dict(slug='din-rail-sub-metering-what-is-a-single-phase-energy-meter',
         title='DIN Rail Electrical Sub-Metering: What Is a Single Phase Energy Meter?',
         kw='what is a single phase energy meter &middot; din rail energy meter &middot; single phase kwh meter &middot; modbus energy meter'),
    dict(slug='commercial-grid-metering-what-is-a-three-phase-energy-meter',
         title='Commercial Grid Power Metering: What Is a Three Phase Energy Meter?',
         kw='what is a three phase energy meter &middot; three phase smart meter &middot; commercial energy meter &middot; dlms cosem energy meter'),
    dict(slug='utility-revenue-protection-what-is-a-prepaid-energy-meter',
         title='Utility Revenue Protection & Smart Prepayment: What Is a Prepaid Energy Meter?',
         kw='what is a prepaid energy meter &middot; sts prepaid meter &middot; keypad electricity meter &middot; revenue protection meter'),
]

h = open(BLOG_HTML, encoding='utf-8').read()

block = ''
for p in POSTS:
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
for p in POSTS:
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

s = open(SITEMAP, encoding='utf-8').read()
before = s.count('<loc>')
new = []
for p in POSTS:
    u = '%s/blog/%s' % (SITE, p['slug'])
    if '<loc>%s</loc>' % u in s:
        continue
    s = s.replace('</urlset>',
                  '  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                  '    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n</urlset>'
                  % (u, DATE))
    new.append(p['slug'])
open(SITEMAP, 'w', encoding='utf-8', newline='').write(s)
print('sitemap <loc>: %d -> %d   added: %s' % (before, s.count('<loc>'), new or 'none'))
