# -*- coding: utf-8 -*-
"""Generate the 2026-09-20 canonical blog pages.

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
from blog_content_0920 import BLOGS

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
TEMPLATE = os.path.join(BASE, 'blog', 'air-circuit-breaker-guide.html')
SITE = 'https://www.yominelectric.com'
ISO = '2026-09-20'
DATE = 'September 20, 2026'

CTA = {
    'mechanical-lug-guide': (
        'Sourcing dual-rated mechanical lugs for panelboards or switchgear?',
        'Tell us your conductor sizes, wire combinations (copper or aluminium), and busbar stud configurations. '
        'YOMIN supplies dual-rated AL9CU mechanical lugs and custom neutral/ground bars with complete material certificates.',
        'Browse the terminal and connector range', '/products/terminal-connector'),
    'test-terminal-block-guide': (
        'Specifying test terminal blocks for secondary metering and protection panels?',
        'Share your circuit scheme (3-phase 3-wire or 3-phase 4-wire) and utility revenue protection requirements. '
        'YOMIN manufactures precision CT shorting test blocks with transparent sealing covers and utility approval.',
        'Browse the terminal and connector range', '/products/terminal-connector'),
    'central-battery-system-guide': (
        'Designing centralized emergency lighting systems for commercial projects?',
        'Send us your emergency luminaire load schedule, required battery autonomy (90 or 180 min), and civil defence specifications. '
        'YOMIN engineers and manufactures EN 50171 certified Central Battery Systems and EPS cabinets.',
        'Browse the emergency lighting range', '/products/emergency-lighting'),
    'dc-surge-protector-guide': (
        'Protecting solar PV arrays and inverters against lightning transients?',
        'Specify your maximum string open-circuit voltage (1000V or 1500V DC) and installation environment. '
        'YOMIN manufactures TUV and CE certified Type 2 and Type 1+2 DC surge protective devices engineered to IEC 61643-31.',
        'Browse the solar and PV products range', '/products/solar-pv-products'),
}

tpl = open(TEMPLATE, encoding='utf-8').read()
head_tpl = tpl[:tpl.index('<main>')]
tail = tpl[tpl.index('</main>'):]
nav = head_tpl  # head + nav + mobile drawer, reused verbatim

written = []
for a in BLOGS:
    slug = a['slug']
    title_tag = '%s | Yomin Electric' % a['title']
    desc = a['desc']
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
                    {"@type": "Question", "name": item[0],
                     "acceptedAnswer": {"@type": "Answer", "text": item[1]}}
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
        faq_html += f'<h3>{htmlmod.escape(f[0])}</h3><p>{htmlmod.escape(f[1])}</p>'
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
''' % dict(crumb=a['breadcrumb'], tag=a['category'], title=a['title'], date=DATE, read=a['read'],
           hero_webp=hero_webp, hero_rel=hero_rel, hero_alt=htmlmod.escape(a['alt'], quote=True),
           body=a['body'], faqs=faq_html, cta_h=cta_h, cta_p=cta_p, cta_a=cta_a, cta_u=cta_u)

    out = h + body + tail
    dest = os.path.join(BASE, 'blog', slug + '.html')
    open(dest, 'w', encoding='utf-8', newline='').write(out)
    written.append(slug)
    print('wrote %s (%d chars)' % (dest, len(out)))

print('Successfully generated %d canonical blog pages!' % len(written))
