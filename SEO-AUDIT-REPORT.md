# Yomin Electric — Indexing Issue Audit Report

Auditor: indexing-issue-auditor skill | Date: 2026-08-12 | Scope: www.yominelectric.com (local source + deployment config)

## Executive Summary

The site has a clean URL architecture (cleanUrls, no .html in sitemap) and solid on-page SEO (canonicals on 33/35 pages, JSON-LD, meta tags). Three high-priority indexing issues were found and two are already fixed. The main remaining issue is a sitemap–canonical mismatch on 1,095 product URLs that wastes crawl budget and generates "Duplicate, Google chose different canonical than user" noise in Search Console. Fixes below are ordered by the skill's 10-phase audit.

---

## Master Issue Control Table

| # | Issue | Layer (SEO/Crawl/Server/Content) | Affected URLs/Patterns | Root Cause | Fix (Technical) | Fix (Structural) | Priority | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Sitemap–canonical mismatch: 1,095 URLs submit `&id=`/`&product=` params but canonicalize to the category page | SEO | /products?category=*&id=*&product=* | Canonical builder drops query params (products.html JS: `canonUrl = /products?category=<slug>`), sitemap generator emitted deep links | Regenerate sitemap with only canonical-representative URLs (/, /products, 22 category URLs, static pages, blog, guide, compare) | Use /product-details?product=* as the canonical product URL form and list those instead | High | In progress (sitemap regeneration pending new posts) |
| 2 | Soft-404 catch-all: unmatched paths 301 → home | Server | /<any-unknown-path> | vercel.json route `{src:"/(.*)", dest:"/", status:301}` redirected all misses to homepage, hiding real 404s from Google | Removed the 301 catch-all; added `{src:"/(.*)", dest:"/404.html", status:404}` + branded 404.html | Add /404 to internal error handling | High | **Fixed** |
| 3 | robots.txt blocks JS-rendering data | Crawl | /data/products.json (plus wildcard /*.json) | `Disallow: /data/` + `Disallow: /*.json` prevented Googlebot from fetching products.json, which the products page needs for client-side rendering → risk of empty renders / "crawled but not indexed" | Added `Allow: /data/products.json` (most-specific rule wins) | Serve products data under /assets/ (unblocked) or pre-render product pages | High | **Fixed** |
| 4 | Duplicate category content: static /energy-meter.html vs JS /products?category=energy-meter | SEO | /<category>.html × 22 | Two URL forms for the same category with separate files | Verify static category pages canonicalize to /products?category=<slug> | Consolidate into one canonical form | Medium | Open |
| 5 | No hreflang (i18n via JS-swap on same URL) | SEO | /blog/* (EN/FR/ES/AR) | Translations swap via localStorage; Googlebot sees English default. No per-language URLs exist | Acceptable for current model; ensure HTML lang stays "en" and content defaults to English for crawlers | Consider static /fr/ /es/ /ar/ URL sets for true international SEO | Low | Accepted |
| 6 | Products depend on client-side rendering | Crawl | /products*, /product-details | Static HTML shell + JS render from products.json | Keep products.json crawlable (done, #3) and rely on Google's JS rendering; verify with URL Inspection "View as Google" | Pre-render product detail pages to static HTML | Medium | Open |
| 7 | Old /blog-* URLs | SEO | /blog-<slug> × 7 | Previous blog URL scheme | 301 redirects added in vercel.json to /blog/<slug> | Single-hop redirects; verify after deploy | High | Fixed (pending deploy) |
| 8 | Deployment blocked | Server | All | Push to GitHub failing on network (port 443 connection resets) | Retry push; commit local state is correct (2 commits ahead) | - | High | Open (blocker) |

---

## Phase-by-Phase Notes

- **Phase 1 (Indexing health):** No hard noindex on indexable pages. products.html sets noindex dynamically only for invalid `?id=` deep links — correct. Soft-404 pattern fixed (#2). Verification files (google003d37053b3f964e.html, pinterest-744fe.html) intentionally lack canonicals — correct.
- **Phase 2 (Crawl architecture):** Depth is flat: home → category → product (2 clicks). Blog posts are 2 clicks from home and cross-link to products. No orphan pages among sitemap entries; all static HTML files are reachable from nav/footer.
- **Phase 3 (Sitemap):** 1,140 URLs — 1,095 of them are non-canonical deep links (#1). Sitemap must be regenerated with only representative URLs. No redirect/404 targets currently in sitemap.
- **Phase 4 (URL architecture):** Products use query parameters; canonical consolidation recommended (#1, #4). Blog URLs now clean `/blog/<slug>`.
- **Phase 5 (Redirects):** All legacy .asp and old /blog-* redirects are single-hop 301s. No chains or loops.
- **Phase 6 (Content):** 22 thin category pages risk duplication (#4). Blog posts are 700–900 words, no thin content. Product detail pages are template-driven — verify uniqueness of titles/descriptions.
- **Phase 7 (Server):** vercel.json routes verified. 404 handling fixed (#2). No 5xx patterns. /api/* routes to backend/server.js — confirm it exists or remove the route.
- **Phase 8 (Performance):** Fonts load non-blocking (media print trick). Images lazy-loaded. No render-blocking patterns found in audit scope.
- **Phase 9 (Internal linking):** Blog ↔ product silo established (posts link to /products?category=* and guide pages). Guide pages form the hub for metering topics.
- **Phase 10 (Rebuild plan):** (1) Deploy pending push (#8). (2) Regenerate sitemap (#1). (3) Verify category canonicals (#4). (4) Submit sitemap + request indexing for new blog URLs in GSC. (5) 30-day: monitor GSC coverage; pre-render product details if "crawled not indexed" persists.

---

## Actions Completed This Audit

- robots.txt: `Allow: /data/products.json` (fixes JS-render crawl block)
- vercel.json: replaced 301-to-home catch-all with real 404 route; created 404.html
- Blog URL migration to /blog/<slug> with 301s (previous session)
