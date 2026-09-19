# -*- coding: utf-8 -*-
"""Generate the 2026-09-19 canonical blog pages.

Template = blog/air-circuit-breaker-guide.html (canonical article page: full site
nav, mobile drawer, blog-hero, content-section, cta-section, canonical footer).
NEVER template from ct-ratio-guide.html.
"""
import html as htmlmod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_content_0919 import FC, EMS, BML

ARTICLES = [FC, EMS, BML]
BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
TEMPLATE = os.path.join(BASE, 'blog', 'air-circuit-breaker-guide.html')
SITE = 'https://www.yominelectric.com'
ISO = '2026-09-19'
DATE = 'September 19, 2026'

CTA = {
    'fuse-cutout-guide': (
        'Sourcing fuse cutouts for an overhead or LV distribution project?',
        'Tell us your system voltage, continuous current rating, and fault interruption capacity. YOMIN manufactures '
        'heavy-duty J-type LV cutouts (up to 630A) and expulsion dropout cutouts (up to 36kV) with full KEMA / ASTA type test reports.',
        'Browse the fuse and protection range', '/products/fuse-protection'),
    'electric-meter-seal-guide': (
        'Specifying tamper-evident security seals for revenue protection?',
        'Send us your required wire length, laser marking specifications, and annual volume. YOMIN supplies '
        'polycarbonate twist-tite meter seals, ultrasonic anchor seals, and barcode-traceable meter security systems.',
        'Browse the security seals range', '/products/security-seal'),
    'bimetallic-lug-guide': (
        'Terminating aluminium feeder cables onto copper switchgear busbars?',
        'Provide your cable cross-section (16 mm² to 800 mm²), palm stud diameter, and project environmental class. '
        'YOMIN manufactures friction-welded DTL-1 and DTL-2 bimetallic lugs certified to IEC 61238-1 Class A.',
        'Browse the terminal and connector range', '/products/terminal-connector'),
}

tpl = open(TEMPLATE, encoding='utf-8').read()
head_tpl = tpl[:tpl.index('<main>')]
tail = tpl[tpl.index('</main>'):]
nav = head_tpl  # head + nav + mobile drawer, reused verbatim

written = []
for a in ARTICLES:
    slug = a['slug']
    title_tag = '%s | Yomin Electric' % a['title']
    desc = a['meta_desc']
    hero_rel = '/assets/images/blog/%s/hero.png' % slug
    hero_webp = '/assets/images/blog/%s/hero.webp' % slug
    card_abs = '%s/assets/images/blog/%s/card.png' % (SITE, slug)
    canon = '%s/blog/%s' % (SITE, slug)

    h = nav
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % htmlmod.escape(title_tag, quote=False), h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="%s">' % htmlmod.escape(desc, quote=True), h, count=1, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">',
               '<meta property="og:image" content="%s">' % card_abs, h, count=1, flags=re.S)
    h = re.sub(r'<link rel="canonical" href=".*?">',
               '<link rel="canonical" href="%s">' % canon, h, count=1, flags=re.S)

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "headline": a['title'],
                "description": desc,
                "image": SITE + hero_rel,
                "datePublished": ISO,
                "dateModified": ISO,
                "inLanguage": "en",
                "author": {"@type": "Organization", "name": "YOMIN Electric Co., Ltd."},
                "publisher": {"@type": "Organization", "name": "YOMIN Electric Co., Ltd.",
                              "logo": {"@type": "ImageObject", "url": SITE + "/assets/images/logo.png"}},
                "mainEntityOfPage": {"@type": "WebPage", "@id": canon},
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": item['q'],
                     "acceptedAnswer": {"@type": "Answer", "text": item['a']}}
                    for item in a['faqs']
                ],
            },
        ],
    }
    h = re.sub(r'<script type="application/ld\+json">.*?</script>',
               '<script type="application/ld+json">\n%s\n</script>' % json.dumps(ld, ensure_ascii=False, indent=2),
               h, count=1, flags=re.S)

    cta_h, cta_p, cta_a, cta_u = CTA[slug]

    faq_html = '<div class="faq-section"><h2>Frequently Asked Questions</h2>'
    for f in a['faqs']:
        faq_html += f'<h3>{htmlmod.escape(f["q"])}</h3><p>{htmlmod.escape(f["a"])}</p>'
    faq_html += '</div>'

    body = '''<main>

  <section class="blog-hero">
    <div class="bh-breadcrumb"><a href="/">Home</a> &middot; <a href="/blog">Blog</a> &middot; <span>%(crumb)s</span></div>
    <span class="bh-tag">%(tag)s</span>
    <h1 class="bh-title">%(title)s</h1>
    <div class="bh-meta">
      <div class="avatar">ET</div>
      <strong style="color:var(--tx)">ET Engineering Team</strong>
      <span class="divider"></span>
      <span>%(date)s</span>
      <span class="divider"></span>
      <span>%(read)s</span>
    </div>
  </section>

  <section class="content-section">
    <picture>
      <source srcset="%(hero_webp)s" type="image/webp">
      <img class="hero-img" src="%(hero_rel)s" alt="%(hero_alt)s" loading="eager" fetchpriority="high" decoding="async">
    </picture>
%(body)s
%(faqs)s
  </section>

  <section class="cta-section">
    <h2>%(cta_h)s</h2>
    <p>%(cta_p)s</p>
    <a class="btn btn-primary" href="/contact">Request a quote</a>
    <p style="margin-top:14px"><a href="%(cta_u)s">%(cta_a)s</a></p>
  </section>
''' % dict(crumb=a['breadcrumb'], tag=a['tag'], title=a['title'], date=DATE, read=a['read'],
           hero_webp=hero_webp, hero_rel=hero_rel, hero_alt=htmlmod.escape(a['alt'], quote=True),
           body=a['body'], faqs=faq_html, cta_h=cta_h, cta_p=cta_p, cta_a=cta_a, cta_u=cta_u)

    out = h + body + tail
    dest = os.path.join(BASE, 'blog', slug + '.html')
    open(dest, 'w', encoding='utf-8', newline='').write(out)
    written.append(slug)
    print('wrote %s (%d chars)' % (dest, len(out)))

print('Successfully generated %d canonical blog pages!' % len(written))
