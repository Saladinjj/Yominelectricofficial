# -*- coding: utf-8 -*-
"""Deterministic pre-commit validation for the 2026-10-23 blog batch."""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.yominelectric.com'
SLUGS = [
    'din-rail-terminal-block-wiring-how-to',
    'air-conditioner-voltage-stabilizer-sizing',
]
LANGS = ['', '-fr', '-es', '-ar']
BASE_SLUGS = SLUGS

problems = []
CJK = re.compile(r'[\u4e00-\u9fff]')

for base in BASE_SLUGS:
    for suf in LANGS:
        slug = base + suf
        p = os.path.join(BASE, 'blog', slug + '.html')
        if not os.path.exists(p):
            problems.append('MISSING FILE %s' % slug)
            continue
        s = open(p, encoding='utf-8').read()

        canon_expected = '%s/blog/%s' % (SITE, slug)
        m = re.search(r'<link rel="canonical" href="([^"]+)">', s)
        if not m or m.group(1) != canon_expected:
            problems.append('%s canonical mismatch: %s' % (slug, m.group(1) if m else None))

        hl = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', s))
        for code, target in [('en', base), ('fr', base + '-fr'), ('es', base + '-es'), ('ar', base + '-ar'), ('x-default', base)]:
            want = '%s/blog/%s' % (SITE, target)
            if hl.get(code) != want:
                problems.append('%s hreflang %s -> %s (want %s)' % (slug, code, hl.get(code), want))

        lang = suf[1:] if suf else 'en'
        if '<html lang="%s"' % lang not in s:
            problems.append('%s html lang not %s' % (slug, lang))
        if lang == 'ar':
            if 'dir="rtl"' not in s or '<body class="ar">' not in s:
                problems.append('%s arabic rtl/body class missing' % slug)
        else:
            if 'dir="ltr"' not in s:
                problems.append('%s dir=ltr missing' % slug)

        # JSON-LD parse
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(block)
            except Exception as e:
                problems.append('%s JSON-LD invalid: %s' % (slug, e))

        # CJK leakage outside Chinese pages (site has no zh pages)
        if CJK.search(s):
            problems.append('%s contains CJK characters' % slug)

        # placeholders (case-sensitive for TODO so Spanish "todo" does not trip it)
        for bad in ['TODO:', 'TODO ', 'Lorem ipsum', '[Brand', '{{', 'XX kWh', 'placeholder']:
            if bad in s:
                problems.append('%s contains placeholder token %r' % (slug, bad))

        # body word count
        body = s[s.find('<main>'):s.find('</main>')]
        text = re.sub(r'<script.*?</script>', ' ', body, flags=re.S)
        text = re.sub(r'<[^>]+>', ' ', text)
        words = len(text.split())
        if words < 700:
            problems.append('%s thin content: %d words' % (slug, words))

        # hero + card exist and are referenced
        for asset in ['hero.png', 'hero.webp', 'card.png', 'card.webp']:
            ap = os.path.join(BASE, 'assets', 'images', 'blog', base, asset)
            if not os.path.exists(ap):
                problems.append('%s missing asset %s' % (base, asset))
        if '/assets/images/blog/%s/hero.png' % base not in s:
            problems.append('%s hero not referenced' % slug)

        # internal links resolve
        for href in set(re.findall(r'href="(/[^"#?]*)"', s)):
            if href.startswith('/assets') or href.endswith('.css') or href.endswith('.ico') or href.endswith('.txt'):
                continue
            rel = href.strip('/')
            cand = [os.path.join(BASE, rel), os.path.join(BASE, rel + '.html'), os.path.join(BASE, rel, 'index.html')]
            if not any(os.path.exists(c) for c in cand):
                problems.append('%s dead internal link %s' % (slug, href))

print('checked %d pages' % (len(BASE_SLUGS) * 4))
if problems:
    print('PROBLEMS (%d):' % len(problems))
    for p in problems:
        print(' -', p)
    sys.exit(1)
print('ALL CHECKS PASSED')
