# i18n Audit Report — Yomin Electric (2026-08-17)

Scope: EN/FR/ES/AR coverage across all HTML pages. Scripts under `temp/` reproduce the audit.

## Status: PASS for all pages except the two gaps below

## Fixed in this pass

### 1. Footer keys missing on every page (fr/ar) and most pages (es)
HTML uses `ft_ab / ft_pr / ft_co / ft_cn / ft_cp`, but the dictionaries defined
`ft_products / ft_company / ft_contact / ft_desc / ft_copy` — a key-name mismatch, and
`ft_ab` + `ft_cp` existed nowhere outside `i18n-index-es.js`.
- Added `ft_ab, ft_pr, ft_co, ft_cn, ft_cp` to `assets/js/main.js` `_YM_BASE` for `en`, `fr`, `ar`
- Added `ft_ab, ft_cn, ft_cp` to `assets/js/i18n-es.js` (es)
- Covers: index, products, all category pages, all detail pages, about, contact, process, solutions, policy pages

### 2. Process page step details untranslated
`process_s1_d1..s4_d5` were missing in fr/ar (es had them); `process_s5_detail1..6` and
`process_s6_detail1..6` were missing in fr/es/ar.
- Added all 33 keys (fr + ar) to `assets/js/main.js`
- Added the 12 s5/s6 keys (es) to `assets/js/i18n-es.js`

### 3. Homepage (index.html) not translated in fr/ar
Hero, products, solutions, process, testimonials, FAQ, CTA, buy-online sections (~75 keys) only
existed in Spanish (`i18n-index-es.js`).
- Created `assets/js/i18n-index-fr.js` and `assets/js/i18n-index-ar.js` (full homepage translations)
- Registered both in `index.html`

### 4. Homepage buy-section keys missing in es
`buy_fb, buy_fb_d, buy_gs, buy_gs_d, buy_nh, buy_nh_d` existed nowhere.
- Added to `assets/js/i18n-index-es.js` (and included in the new fr/ar files)

## Known gaps (not fixed — content work required)

### A. Blog pages have no translation runtime or dictionaries
- `blog.html` loads no i18n scripts; its 98 `data-i18n` keys are inert. It carries its own
  self-contained language/menu/theme script (loading `main.js` would conflict — duplicate
  handlers). The `blog_*` / `cat_*` / `team_*` keys exist in no dictionary.
- `blog/*.html` articles load only `i18n-es.js`.
- Recommendation: build `blog_*` dictionaries (titles + excerpts of the 10 guides / 12 product
  posts) and load them from blog.html.

### B. Product detail pages: dict key format does not match page pids
- 608 of 670 detail pages use numeric Alibaba offer IDs as `data-pid`
  (e.g. `60572260147`), but `data/i18n-detail-*.js` and `assets/js/i18n-products-*.js` contain
  keys in `ym-xxx` format (e.g. `ym-0058-desc`) — no numeric keys at all.
- Consequence: detail-page titles, features and specs render in English for fr/es/ar on those
  608 pages (only the 3 `ym-sm-*` screw-machine pages match).
- Recommendation: regenerate the detail translation files keyed by the numeric Alibaba IDs
  (or add `ym-xxx` ↔ numeric ID mapping) — a content-generation task, not a wiring bug.

## Audit tooling (kept in `temp/` for reproducibility)
- `audit_i18n3.js` — page-vs-dictionary coverage checker (per-language sources)
- `count_pid_types.js`, `check_pid_format.js` — detail-page pid analysis
