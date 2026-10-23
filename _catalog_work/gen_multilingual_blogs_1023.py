# -*- coding: utf-8 -*-
"""Generate the canonical multilingual 2026-10-23 blog pages.

Two topics x 4 languages (EN, FR, ES, AR):
1. DIN rail terminal block wiring (Terminal & Connector)
2. Voltage stabilizer for air conditioners (Voltage Stabilizer/Regulator)

Template = blog/air-circuit-breaker-guide.html (canonical article page).
Adds self-canonical, reciprocal hreflang, language switcher, JSON-LD.
"""
import html as htmlmod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_content_1023 import ALL_POSTS_1023

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(BASE, 'blog', 'air-circuit-breaker-guide.html')
SITE = 'https://www.yominelectric.com'
ISO = '2026-10-23'

CTA_BUTTON = {
    'en': 'Request a technical proposal',
    'fr': 'Demander une étude technique',
    'es': 'Solicitar propuesta técnica',
    'ar': 'طلب دراسة فنية وتسعيرة',
}

CTA_LINK_TEXT = {
    'en': 'Explore our full electrical equipment range',
    'fr': 'Découvrir notre gamme complète d\'équipements',
    'es': 'Ver catálogo completo de equipamiento eléctrico',
    'ar': 'استعراض كتالوج المعدات والأجهزة الكهربائية الكامل',
}

DATES = {
    'en': 'October 23, 2026',
    'fr': '23 Octobre 2026',
    'es': '23 de Octubre de 2026',
    'ar': '23 أكتوبر 2026',
}

BREADCRUMB_HOME = {
    'en': ('Home', 'Blog'),
    'fr': ('Accueil', 'Blog'),
    'es': ('Inicio', 'Blog'),
    'ar': ('الرئيسية', 'المدونة'),
}

FAQ_TITLE = {
    'en': 'Frequently Asked Questions',
    'fr': 'Foire Aux Questions',
    'es': 'Preguntas Frecuentes',
    'ar': 'الأسئلة الشائعة',
}

WHATSAPP_LINE = {
    'en': 'Prefer to write first? WhatsApp <a href="https://wa.me/8619016543301">+86 190 1654 3301</a> &middot; Email <a href="mailto:info@yominelectric.com">info@yominelectric.com</a> &mdash; send requirements and drawings, and the technical team responds within 24 hours.',
    'fr': 'Vous préférez écrire d&rsquo;abord ? WhatsApp <a href="https://wa.me/8619016543301">+86 190 1654 3301</a> &middot; E-mail <a href="mailto:info@yominelectric.com">info@yominelectric.com</a> &mdash; envoyez vos exigences et vos plans, l&rsquo;équipe technique répond sous 24 heures.',
    'es': '¿Prefiere escribir primero? WhatsApp <a href="https://wa.me/8619016543301">+86 190 1654 3301</a> &middot; Correo <a href="mailto:info@yominelectric.com">info@yominelectric.com</a> &mdash; envíe requisitos y planos y el equipo técnico responde en 24 horas.',
    'ar': 'هل تفضل المراسلة أولًا؟ واتساب <a href="https://wa.me/8619016543301">+86 190 1654 3301</a> &middot; البريد <a href="mailto:info@yominelectric.com">info@yominelectric.com</a> &mdash; أرسل المتطلبات والمخططات ويرد الفريق الفني خلال 24 ساعة.',
}

SPECS_TITLE = {
    'en': ('Technical Specifications', 'Technical Specification & Parameter', 'Standard Metric Rating & Engineering Compliance'),
    'fr': ('Spécifications Techniques', 'Paramètre Technique', 'Valeur Standard & Norme'),
    'es': ('Especificaciones Técnicas', 'Parámetro Técnico', 'Valor Estándar y Cumplimiento'),
    'ar': ('المواصفات الفنية', 'المعلمة الفنية الهندسية', 'القيمة ومستوى الأداء المعياري'),
}

tpl = open(TEMPLATE, encoding='utf-8').read()
head_tpl = tpl[:tpl.index('<main>')]
tail = tpl[tpl.index('</main>'):]

written = []

for a in ALL_POSTS_1023:
    slug = a['slug']
    lang = a['lang']
    direction = a['dir']
    base_slug = re.sub(r'-(fr|es|ar)$', '', slug)

    title_tag = '%s | Yomin Electric' % a['title']
    desc = a['desc']
    hero_rel = '/assets/images/blog/%s/hero.png' % base_slug
    hero_webp = '/assets/images/blog/%s/hero.webp' % base_slug
    card_abs = '%s/assets/images/blog/%s/card.png' % (SITE, base_slug)
    canon = '%s/blog/%s' % (SITE, slug)

    h = head_tpl
    h = re.sub(r'<html\s+lang=".*?"\s+dir=".*?"', '<html lang="%s" dir="%s"' % (lang, direction), h, count=1)
    if lang == 'ar':
        h = h.replace('<body>', '<body class="ar">')

    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % htmlmod.escape(title_tag, quote=False), h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="%s">' % htmlmod.escape(desc, quote=True), h, count=1, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">',
               '<meta property="og:image" content="%s">' % card_abs, h, count=1, flags=re.S)

    hreflangs = (
        '<link rel="canonical" href="%s/blog/%s">\n'
        '  <link rel="alternate" hreflang="en" href="%s/blog/%s">\n'
        '  <link rel="alternate" hreflang="fr" href="%s/blog/%s-fr">\n'
        '  <link rel="alternate" hreflang="es" href="%s/blog/%s-es">\n'
        '  <link rel="alternate" hreflang="ar" href="%s/blog/%s-ar">\n'
        '  <link rel="alternate" hreflang="x-default" href="%s/blog/%s">'
        % (SITE, slug, SITE, base_slug, SITE, base_slug, SITE, base_slug, SITE, base_slug, SITE, base_slug)
    )
    h = re.sub(r'<link rel="canonical" href=".*?">(\s*<link rel="alternate" hreflang=".*?" href=".*?">)*',
               hreflangs, h, count=1, flags=re.S)

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

    faq_html = '<div class="faq-section"><h2>%s</h2>' % FAQ_TITLE[lang]
    for f in a['faqs']:
        faq_html += '<h3>%s</h3><p>%s</p>' % (htmlmod.escape(f[0]), htmlmod.escape(f[1]))
    faq_html += '</div>'

    st, th1, th2 = SPECS_TITLE[lang]
    specs_html = ('<h2>%s</h2>\n<table>\n  <thead>\n    <tr><th>%s</th><th>%s</th></tr>\n  </thead>\n  <tbody>\n'
                  % (st, th1, th2))
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
    <p style="margin-top:14px"><a href="%s">%s &rarr;</a></p>
    <p style="margin-top:18px;font-size:14px;color:var(--mt)">%s</p>
  </section>
''' % (b_home, b_blog, a['breadcrumb'], a['category'], a['title'], DATES[lang], a['read'],
       hero_webp, hero_rel, htmlmod.escape(a['alt'], quote=True),
       a['body'], specs_html, faq_html,
       a['title'], a['cta'], CTA_BUTTON[lang], a['product_url'], CTA_LINK_TEXT[lang], WHATSAPP_LINE[lang])

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
      location.href = '/blog/' + b + M[l];
    }, true);
  });
})();
</script>
''' % base_slug

    out = h + body + switcher_script + tail
    dest = os.path.join(BASE, 'blog', slug + '.html')
    with open(dest, 'w', encoding='utf-8', newline='') as fh:
        fh.write(out)
    written.append(slug)
    print('wrote %s (%d chars)' % (dest, len(out)))

print('Generated %d multilingual blog pages for 2026-10-23' % len(written))
