# -*- coding: utf-8 -*-
"""Generate the canonical multilingual 2026-10-20 (GSC Query Optimization) blog pages.

Generates 8 complete HTML files:
1. Substation Engineering: Current Transformer Sizing Calculation Guide: EN, FR, ES, AR
2. Utility Metering: Difference Between Prepaid and Postpaid Electricity: EN, FR, ES, AR

Template = blog/air-circuit-breaker-guide.html (canonical article page: full site
nav, mobile drawer, blog-hero, content-section, cta-section, canonical footer).
Includes self-canonical, reciprocal hreflang, language switcher script, and JSON-LD.
"""
import html as htmlmod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_content_multilingual_1020_gsc import ALL_MULTILINGUAL_POSTS_1020_GSC

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
TEMPLATE = os.path.join(BASE, 'blog', 'air-circuit-breaker-guide.html')
SITE = 'https://www.yominelectric.com'
ISO = '2026-10-20'
DATE_EN = 'October 20, 2026'

BASE_SLUGS = {
    'substation-engineering-current-transformer-sizing-calculation': 'substation-engineering-current-transformer-sizing-calculation',
    'substation-engineering-current-transformer-sizing-calculation-fr': 'substation-engineering-current-transformer-sizing-calculation',
    'substation-engineering-current-transformer-sizing-calculation-es': 'substation-engineering-current-transformer-sizing-calculation',
    'substation-engineering-current-transformer-sizing-calculation-ar': 'substation-engineering-current-transformer-sizing-calculation',
    'utility-metering-difference-between-prepaid-and-postpaid-electricity': 'utility-metering-difference-between-prepaid-and-postpaid-electricity',
    'utility-metering-difference-between-prepaid-and-postpaid-electricity-fr': 'utility-metering-difference-between-prepaid-and-postpaid-electricity',
    'utility-metering-difference-between-prepaid-and-postpaid-electricity-es': 'utility-metering-difference-between-prepaid-and-postpaid-electricity',
    'utility-metering-difference-between-prepaid-and-postpaid-electricity-ar': 'utility-metering-difference-between-prepaid-and-postpaid-electricity',
}

CTA_BUTTON = {
    'en': 'Request a technical proposal',
    'fr': 'Demander une étude technique',
    'es': 'Solicitar propuesta técnica',
    'ar': 'طلب دراسة فنية وتسعيرة'
}

CTA_LINK_TEXT = {
    'en': 'Explore our full electrical equipment range',
    'fr': 'Découvrir notre gamme complète d\'équipements',
    'es': 'Ver catálogo completo de equipamiento eléctrico',
    'ar': 'استعراض كتالوج المعدات والأجهزة الكهربائية الكامل'
}

DATES = {
    'en': 'October 20, 2026',
    'fr': '20 Octobre 2026',
    'es': '20 de Octubre de 2026',
    'ar': '20 أكتوبر 2026'
}

BREADCRUMB_HOME = {
    'en': ('Home', 'Blog'),
    'fr': ('Accueil', 'Blog'),
    'es': ('Inicio', 'Blog'),
    'ar': ('الرئيسية', 'المدونة')
}

FAQ_TITLE = {
    'en': 'Frequently Asked Questions',
    'fr': 'Foire Aux Questions',
    'es': 'Preguntas Frecuentes',
    'ar': 'الأسئلة الشائعة'
}

tpl = open(TEMPLATE, encoding='utf-8').read()
head_tpl = tpl[:tpl.index('<main>')]
tail = tpl[tpl.index('</main>'):]

written = []
for a in ALL_MULTILINGUAL_POSTS_1020_GSC:
    slug = a['slug']
    lang = a['lang']
    direction = a['dir']
    base_slug = BASE_SLUGS[slug]

    title_tag = '%s | Yomin Electric' % a['title']
    desc = a['desc']
    hero_rel = '/assets/images/blog/%s/hero.png' % base_slug
    hero_webp = '/assets/images/blog/%s/hero.webp' % base_slug
    card_abs = '%s/assets/images/blog/%s/card.png' % (SITE, base_slug)
    canon = '%s/blog/%s' % (SITE, slug)

    h = head_tpl
    # Update html lang and dir
    h = re.sub(r'<html\s+lang=".*?"\s+dir=".*?"', '<html lang="%s" dir="%s"' % (lang, direction), h, count=1)
    if lang == 'ar':
        h = h.replace('<body>', '<body class="ar">')

    # Update title, desc, og:image
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % htmlmod.escape(title_tag, quote=False), h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="%s">' % htmlmod.escape(desc, quote=True), h, count=1, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">',
               '<meta property="og:image" content="%s">' % card_abs, h, count=1, flags=re.S)

    # Construct Canonical and Reciprocal Hreflangs
    hreflangs = (
        '  <link rel="canonical" href="%s/blog/%s">\n'
        '  <link rel="alternate" hreflang="en" href="%s/blog/%s">\n'
        '  <link rel="alternate" hreflang="fr" href="%s/blog/%s-fr">\n'
        '  <link rel="alternate" hreflang="es" href="%s/blog/%s-es">\n'
        '  <link rel="alternate" hreflang="ar" href="%s/blog/%s-ar">\n'
        '  <link rel="alternate" hreflang="x-default" href="%s/blog/%s">\n'
        % (SITE, slug, SITE, base_slug, SITE, base_slug, SITE, base_slug, SITE, base_slug, SITE, base_slug)
    )
    h = re.sub(r'<link rel="canonical" href=".*?">(\s*<link rel="alternate" hreflang=".*?" href=".*?">)*',
               hreflangs.strip(), h, count=1, flags=re.S)

    # JSON-LD Graph matching page language
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
                "inLanguage": lang,
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

    # Active state on language button
    active_flag = {'en': 'gb.png', 'fr': 'fr.png', 'es': 'es.png', 'ar': 'ar'}[lang]
    lbtn_markup = (
        '<button class="lbtn" id="lbtn" aria-label="Current language: %s">\n'
        '        <span id="lf">%s</span><span id="lc">%s</span>\n'
        '        <svg viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l5 5 5-5"></path></svg>\n'
        '      </button>'
        % (lang.upper(),
           '<span>AR</span>' if lang == 'ar' else '<img src="https://flagcdn.com/16x12/%s" class="flag" alt="%s">' % (active_flag, lang.upper()),
           lang.upper())
    )
    h = re.sub(r'<button class="lbtn".*?</button>', lbtn_markup, h, count=1, flags=re.S)

    # Build FAQ HTML
    faq_html = '<div class="faq-section"><h2>%s</h2>' % FAQ_TITLE[lang]
    for f in a['faqs']:
        faq_html += f'<h3>{htmlmod.escape(f[0])}</h3><p>{htmlmod.escape(f[1])}</p>'
    faq_html += '</div>'

    # Build Technical Specs Table HTML
    specs_html = '<h2>Technical Specifications & Formulas</h2>\n<table>\n  <thead>\n    <tr><th>Technical Specification & Sizing Parameter</th><th>Engineering Formula & Standard Metric Rating</th></tr>\n  </thead>\n  <tbody>\n'
    if lang == 'fr':
        specs_html = '<h2>Spécifications Techniques & Formules</h2>\n<table>\n  <thead>\n    <tr><th>Paramètre Technique & Formule</th><th>Valeur d\'Ingénierie & Norme</th></tr>\n  </thead>\n  <tbody>\n'
    elif lang == 'es':
        specs_html = '<h2>Especificaciones Técnicas y Fórmulas</h2>\n<table>\n  <thead>\n    <tr><th>Parámetro Técnico y Fórmula</th><th>Valor de Ingeniería y Norma</th></tr>\n  </thead>\n  <tbody>\n'
    elif lang == 'ar':
        specs_html = '<h2>المواصفات الفنية والمعادلات الهندسية</h2>\n<table>\n  <thead>\n    <tr><th>المعلمة الفنية الهندسية والمعادلة</th><th>القيمة ومستوى الأداء المعياري</th></tr>\n  </thead>\n  <tbody>\n'

    for sp in a['specs']:
        specs_html += '    <tr><td><strong>%s</strong></td><td>%s</td></tr>\n' % (sp[0], sp[1])
    specs_html += '  </tbody>\n</table>\n'

    b_home, b_blog = BREADCRUMB_HOME[lang]

    body = '''<main>

  <section class="blog-hero">
    <div class="bh-breadcrumb"><a href="/">%s</a> &middot; <a href="/blog">%s</a> &middot; <span>%s</span></div>
    <span class="bh-tag">%s</span>
    <h1 class="bh-title">%s</h1>
    <div class="bh-meta">
      <div class="avatar">ET</div>
      <strong style="color:var(--tx)">ET Engineering Team</strong>
      <span class="divider"></span>
      <span>%s</span>
      <span class="divider"></span>
      <span>%s</span>
    </div>
  </section>

  <section class="content-section">
    <picture>
      <source srcset="%s" type="image/webp">
      <img class="hero-img" src="%s" alt="%s" loading="eager" fetchpriority="high" decoding="async">
    </picture>
%s
%s
%s
  </section>

  <section class="cta-section">
    <h2>%s</h2>
    <p>%s</p>
    <a class="btn btn-primary" href="/contact">%s</a>
    <p style="margin-top:14px"><a href="/products">%s &rarr;</a></p>
  </section>
''' % (b_home, b_blog, a['breadcrumb'], a['category'], a['title'], DATES[lang], a['read'],
       hero_webp, hero_rel, htmlmod.escape(a['alt'], quote=True),
       a['body'], specs_html, faq_html,
       a['title'], a['cta'], CTA_BUTTON[lang], CTA_LINK_TEXT[lang])

    # Language Switcher Script attached to bottom before </body>
    switcher_script = '''
<script>
(function(){
  var M = {en:'', fr:'-fr', es:'-es', ar:'-ar'};
  var b = "%s";
  document.querySelectorAll('.lopt, .mlb').forEach(function(btn){
    var l = btn.getAttribute('data-lang');
    if (!l || !(l in M)) return;
    btn.addEventListener('click', function(ev){
      ev.stopImmediatePropagation();
      ev.preventDefault();
      try { localStorage.setItem('ym_lang', l); } catch(e){}
      var targetSlug = b + M[l];
      location.href = '/blog/' + targetSlug;
    }, true);
  });
})();
</script>
''' % base_slug

    modified_tail = switcher_script + tail

    out = h + body + modified_tail
    dest = os.path.join(BASE, 'blog', slug + '.html')
    open(dest, 'w', encoding='utf-8', newline='').write(out)
    written.append(slug)
    print('wrote %s (%d chars)' % (dest, len(out)))

print('Successfully generated %d canonical multilingual blog pages for 2026-10-20 GSC queries!' % len(written))
