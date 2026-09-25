# -*- coding: utf-8 -*-
"""Generate the canonical Central Asia & Metering blog pages.

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
from blog_content_ca_meters import CA_BLOGS

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
TEMPLATE = os.path.join(BASE, 'blog', 'air-circuit-breaker-guide.html')
SITE = 'https://www.yominelectric.com'
ISO = '2026-09-25'
DATE = 'September 25, 2026'

CTA = {
    'substation-measurement-what-is-a-current-transformer': (
        'Specifying Class 0.2S or 0.5S measuring current transformers for substation switchgear, motor control centers, or Central Asian ASKUE power accounting projects?',
        'Tell us your primary busbar dimensions, required transformation ratio (e.g. 200/5A to 5000/5A), accuracy class, and rated burden (VA). '
        'YOMIN manufactures precision busbar and split-core CTs tested to IEC 61869 standards.',
        'Browse the current transformer range', '/products/current-transformer'),
    'din-rail-sub-metering-what-is-a-single-phase-energy-meter': (
        'Looking to deploy compact 1-module or 2-module single-phase DIN rail energy meters with RS485 Modbus for building sub-metering, solar arrays, or smart automation panels?',
        'Specify your current capacity (e.g. 5(60)A or 10(100)A), communication protocol requirements, and pulse output options. '
        'YOMIN supplies certified Class 1.0 digital meters engineered to IEC 62053 standards.',
        'Browse the energy meter range', '/products/energy-meter'),
    'commercial-grid-metering-what-is-a-three-phase-energy-meter': (
        'Need high-accuracy Class 0.5S or 0.2S three-phase multi-function smart energy meters with DLMS/COSEM, RS485 Modbus, or 4G IoT connectivity for Central Asian industrial switchboards or ASKUE projects?',
        'Specify your system voltage (3x220/380V or 3x57.7/100V), connection mode (direct or CT operated), and remote communication requirements. '
        'YOMIN supplies fully certified grid meters engineered for utility substation applications.',
        'Browse the energy meter range', '/products/energy-meter'),
    'utility-revenue-protection-what-is-a-prepaid-energy-meter': (
        'Planning utility electrification, municipal revenue protection, or residential prepayment deployments with STS-certified keypad meters and vending software?',
        'Specify your grid architecture (integrated keypad or split-unit with CIU), single-phase or three-phase ratings, and vending integration needs. '
        'YOMIN supplies certified STS prepayment meters and smart vending solutions.',
        'Browse the energy meter range', '/products/energy-meter'),
}

tpl = open(TEMPLATE, encoding='utf-8').read()
head_tpl = tpl[:tpl.index('<main>')]
tail = tpl[tpl.index('</main>'):]
nav = head_tpl

written = []
for a in CA_BLOGS:
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
    ld_json_str = json.dumps(ld, ensure_ascii=False, indent=2)
    h = re.sub(r'<script type="application/ld\+json">.*?</script>',
               lambda m, s=ld_json_str: '<script type="application/ld+json">\n%s\n</script>' % s,
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

print('Successfully generated %d canonical Central Asia & Metering blog pages!' % len(written))
