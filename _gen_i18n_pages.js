/*
 * Generate standalone localized blog pages (fr / es / ar) from the embedded
 * _BLOG_T translation dictionaries in the 10 blog posts that carry them.
 * Also wires the top language buttons (desktop dropdown + mobile) to navigate
 * between language versions on those posts and the 3 pre-existing localized
 * 60-amp pages.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const BLOG_DIR = path.join(__dirname, 'blog');
const SITE = 'https://www.yominelectric.com';
const LANG_CODES = { en: '', fr: '-fr', es: '-es', ar: '-ar' };
const LANGS = [
  { code: 'fr', dir: 'ltr', flag: 'https://flagcdn.com/16x12/fr.png', read: 'Lire ce guide en : ' },
  { code: 'es', dir: 'ltr', flag: 'https://flagcdn.com/16x12/es.png', read: 'Leer esta guía en: ' },
  { code: 'ar', dir: 'rtl', flag: null, read: 'اقرأ هذا الدليل بـ: ' }
];
const LANG_NAMES = { en: 'English', fr: 'Français', es: 'Español', ar: 'العربية' };

function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

/* Extract the _BLOG_T object literal (string-literal aware, brace balanced). */
function extractBlogT(html) {
  const m = html.match(/_BLOG_T\s*=\s*\{/);
  if (!m) return null;
  const start = m.index + m[0].length - 1; // index of '{'
  let depth = 0, inStr = null;
  for (let i = start; i < html.length; i++) {
    const ch = html[i];
    if (inStr) {
      if (ch === '\\') { i++; continue; }
      if (ch === inStr) inStr = null;
      continue;
    }
    if (ch === "'" || ch === '"' || ch === '`') { inStr = ch; continue; }
    if (ch === '{') depth++;
    else if (ch === '}') {
      depth--;
      if (depth === 0) {
        try {
          const ctx = {};
          vm.runInNewContext('var _BLOG_T = ' + html.slice(start, i + 1), ctx);
          return ctx._BLOG_T || null;
        } catch (e) { return null; }
      }
    }
  }
  return null;
}

/* Find the matching close tag for an element starting after openEnd. */
function findClose(html, from, tag) {
  let depth = 0, i = from;
  const closeRe = new RegExp('^</\\s*' + tag + '\\s*>');
  const openRe = new RegExp('^<\\s*' + tag + '(?=[\\s/>])');
  while (i < html.length) {
    const lt = html.indexOf('<', i);
    if (lt === -1) return null;
    const rest = html.slice(lt);
    const mc = rest.match(closeRe);
    if (mc) {
      if (depth === 0) return { start: lt, len: mc[0].length };
      depth--;
      i = lt + mc[0].length;
      continue;
    }
    const mo = rest.match(openRe);
    if (mo) { depth++; i = lt + mo[0].length; continue; }
    i = lt + 1;
  }
  return null;
}

/* Replace the inner content of every element carrying data-i18n/data-t="key". */
function replaceAll(html, key, val) {
  const a1 = 'data-i18n="' + key + '"';
  const a2 = 'data-t="' + key + '"';
  let out = '', last = 0;
  while (true) {
    const i1 = html.indexOf(a1, last);
    const i2 = html.indexOf(a2, last);
    let start = -1;
    if (i1 === -1) start = i2;
    else if (i2 === -1) start = i1;
    else start = Math.min(i1, i2);
    if (start === -1) { out += html.slice(last); break; }
    const tagStart = html.lastIndexOf('<', start);
    const openEnd = html.indexOf('>', start);
    if (tagStart === -1 || openEnd === -1 || openEnd < tagStart) { out += html.slice(last, start + 1); last = start + 1; continue; }
    const open = html.slice(tagStart, openEnd + 1);
    const tm = open.match(/^<\s*([a-zA-Z0-9]+)/);
    if (!tm) { out += html.slice(last, start + 1); last = start + 1; continue; }
    const close = findClose(html, openEnd + 1, tm[1]);
    if (!close) { out += html.slice(last, start + 1); last = start + 1; continue; }
    out += html.slice(last, openEnd + 1) + val + html.slice(close.start, close.start + close.len);
    last = close.start + close.len;
  }
  return out;
}

function makeHreflang(slug) {
  const rows = ['en', 'fr', 'es', 'ar'].map(function (c) {
    return '<link rel="alternate" hreflang="' + c + '" href="' + SITE + '/blog/' + slug + LANG_CODES[c] + '">';
  });
  rows.push('<link rel="alternate" hreflang="x-default" href="' + SITE + '/blog/' + slug + '">');
  return rows.join('\n');
}

function makeReadBar(slug, lang, readPrefix) {
  const parts = ['en', 'fr', 'es', 'ar'].map(function (c) {
    const txt = LANG_NAMES[c];
    if (c === lang) return '<strong>' + txt + '</strong>';
    return '<a href="' + SITE + '/blog/' + slug + LANG_CODES[c] + '">' + txt + '</a>';
  });
  return '<p style="margin-bottom:20px"><em>' + readPrefix + parts.join(' · ') + '</em></p>';
}

function makeNavScript(lang, setOnLoad) {
  let s = '<script>(function(){';
  if (setOnLoad) s += "try{localStorage.setItem('ym_lang','" + lang + "')}catch(e){}";
  s += "var M={en:'',fr:'-fr',es:'-es',ar:'-ar'};var h=location.pathname.split('/').pop()||'';var b=h.replace(/-(?:fr|es|ar)$/,'').replace(/\\.html$/,'');var ext=/\\.html$/.test(h)?'.html':'';document.querySelectorAll('.lopt,.mlb').forEach(function(btn){var l=btn.getAttribute('data-lang');if(!l||!M[l])return;btn.addEventListener('click',function(ev){ev.stopImmediatePropagation();ev.preventDefault();try{localStorage.setItem('ym_lang',l)}catch(e){}location.href=b+M[l]+ext;},true);});})();</script>";
  return s;
}

/* Add hreflang (if missing) + nav script to a source/localized page. */
function patchSource(file, slug) {
  const orig = fs.readFileSync(file, 'utf8');
  let html = orig;
  if (!html.includes('hreflang=')) {
    html = html.replace(/<link rel="canonical"[^>]*>/, '$&\n' + makeHreflang(slug));
  }
  if (!html.includes('stopImmediatePropagation')) {
    html = html.replace(/<\/body>/, makeNavScript(null, false) + '\n</body>');
  }
  if (html !== orig) { fs.writeFileSync(file, html, 'utf8'); return true; }
  return false;
}

const files = fs.readdirSync(BLOG_DIR).filter(function (f) { return f.endsWith('.html'); });
const generated = [];
const patched = [];
const skipped = [];

for (const f of files) {
  const full = path.join(BLOG_DIR, f);
  const html0 = fs.readFileSync(full, 'utf8');
  const dict = extractBlogT(html0);
  const slug = f.replace(/\.html$/, '');

  if (dict) {
    for (const L of LANGS) {
      const t = dict[L.code];
      if (!t || typeof t !== 'object') { skipped.push(f + ' (no ' + L.code + ' dict)'); continue; }
      let out = html0;
      // Drop the embedded _BLOG_T script block (content is now hardcoded).
      out = out.replace(/<script>((?:(?!<\/script>)[\s\S])*?)var _BLOG_T[\s\S]*?<\/script>/, '');
      // Apply translations.
      for (const k of Object.keys(t)) {
        if (typeof t[k] === 'string') out = replaceAll(out, k, t[k]);
      }
      // Language / direction.
      out = out.replace(/<html\s+lang="en"\s+dir="ltr">/, '<html lang="' + L.code + '" dir="' + L.dir + '">');
      if (L.code === 'ar') out = out.replace(/<body(?=[\s>])/, '<body class="ar"');
      // Title + social + JSON-LD.
      const tTitle = t.blog_title;
      if (tTitle) {
        out = out.replace(/<title>[^<]*<\/title>/, '<title>' + tTitle + ' | Zhejiang Yomin Electric</title>');
        out = out.replace(/<meta property="og:title" content="[^"]*"/, '<meta property="og:title" content="' + tTitle + '"');
        out = out.replace(/<meta name="twitter:title" content="[^"]*"/, '<meta name="twitter:title" content="' + tTitle + '"');
        out = out.replace(/("headline"\s*:\s*")[^"]*(")/, '$1' + tTitle.replace(/"/g, '\\"') + '$2');
      }
      out = out.replace(/<link rel="canonical" href="[^"]*"/, '<link rel="canonical" href="' + SITE + '/blog/' + slug + '-' + L.code + '"');
      out = out.replace(/<meta property="og:url" content="[^"]*"/, '<meta property="og:url" content="' + SITE + '/blog/' + slug + '-' + L.code + '"');
      if (!out.includes('hreflang=')) out = out.replace(/<link rel="canonical"[^>]*>/, '$&\n' + makeHreflang(slug));
      out = out.replace(/("@type"\s*:\s*"BlogPosting")/, '$1,\n    "inLanguage": "' + L.code + '"');
      // Active language button state.
      for (const cls of ['lopt', 'mlb']) {
        out = out.split('class="' + cls + ' act" data-lang="en"').join('class="' + cls + '" data-lang="en"');
        out = out.split('class="' + cls + '" data-lang="' + L.code + '"').join('class="' + cls + ' act" data-lang="' + L.code + '"');
      }
      // Flag + code in the language button.
      if (L.code === 'ar') {
        out = out.replace(/<span id="lf">[\s\S]*?<\/span>/, '<span id="lf"><span class="flag flag-txt">AR</span></span>');
      } else {
        out = out.replace(/<span id="lf"><img src="[^"]*"[^>]*><\/span>/, '<span id="lf"><img src="' + L.flag + '" class="flag" alt="' + L.code.toUpperCase() + '"></span>');
      }
      out = out.replace(/<span id="lc">[A-Za-z]{2}<\/span>/, '<span id="lc">' + L.code.toUpperCase() + '</span>');
      // In-content language bar.
      out = out.replace(/(<section class="content-section">)/, '$1\n    ' + makeReadBar(slug, L.code, L.read));
      // Nav script + persist language (only if not already present).
      if (!out.includes('stopImmediatePropagation')) {
        out = out.replace(/<\/body>/, makeNavScript(L.code, true) + '\n</body>');
      }
      const outFile = path.join(BLOG_DIR, slug + '-' + L.code + '.html');
      fs.writeFileSync(outFile, out, 'utf8');
      generated.push(path.basename(outFile));
    }
    if (patchSource(full, slug)) patched.push(f);
  } else if (/-(?:ar|es|fr)\.html$/.test(f)) {
    if (patchSource(full, slug)) patched.push(f);
  } else {
    skipped.push(f);
  }
}

console.log('GENERATED (' + generated.length + '):');
generated.forEach(function (g) { console.log('  + ' + g); });
console.log('PATCHED (' + patched.length + '):');
patched.forEach(function (p) { console.log('  ~ ' + p); });
console.log('SKIPPED (' + skipped.length + '):');
skipped.forEach(function (s) { console.log('  - ' + s); });
