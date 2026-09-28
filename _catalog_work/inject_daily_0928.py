# -*- coding: utf-8 -*-
"""Add the three 2026-09-28 blogs to blog.html (cards + blogPost JSON-LD) and
sitemap.xml. Idempotent."""
import json
import os
import re

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
BLOG_HTML = os.path.join(BASE, 'blog.html')
SITEMAP = os.path.join(BASE, 'sitemap.xml')
SITE = 'https://www.yominelectric.com'
DATE = '2026-09-28'

POSTS = [
    dict(slug='earth-fault-protection-what-is-a-core-balance-current-transformer',
         title='Earth Fault & Leakage Protection: What Is a Core Balance Current Transformer?',
         kw='what is core balance current transformer &middot; core balance current transformer &middot; cbct current transformer &middot; zero sequence ct'),
    dict(slug='dual-power-generator-backup-what-is-an-automatic-transfer-switch',
         title='Dual-Power Grid & Generator Backup: What Is an Automatic Transfer Switch?',
         kw='what is an automatic transfer switch &middot; automatic transfer switch &middot; ats switch &middot; generator transfer switch'),
    dict(slug='earth-leakage-protection-what-is-an-rcbo',
         title='Earth Leakage & Overcurrent Protection: What Is an RCBO?',
         kw='what is an rcbo &middot; rcbo breaker &middot; rcbo circuit breaker &middot; difference between rcd and rcbo'),
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
