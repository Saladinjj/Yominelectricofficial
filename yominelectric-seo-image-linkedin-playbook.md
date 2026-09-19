# yominelectric.com — SEO → Real-Product Image → LinkedIn Playbook

> **What this file is:** a reusable operating procedure. Hand it to an agent (or follow it yourself) to go from 3UE Semrush keyword research → real-product marketing images → a publish-ready LinkedIn B2B post.
> **What this file is NOT:** a report. It contains no keyword data — the data is produced each time you run it.

**How to use:** paste this file into a session and say *"run this playbook for yominelectric.com"*, or work the phases manually in order. Phases are sequential — Phase 2 cannot start before Phase 1 produces the keyword table.

---

## 0. Ground truth — YOMIN product reality

Everything generated must trace back to a product that actually exists. This is the authoritative reference.

### Company facts (approved claim set)

| Fact | Value |
|---|---|
| Legal name | Zhejiang Yomin Electric Co., Ltd. |
| Established | 1996 (30+ years) |
| Countries served | 95+ |
| Employees | 370+ |
| Manufacturing area | 12,000 ㎡ |
| Factory | Qiaoqian Industry Area, Liushi Town, Yueqing City, Zhejiang Province |
| Ports | Ningbo / Shanghai |
| MOQ | 100 units standard · 500 units OEM/custom |
| Lead time | 15–25 working days standard · 30–45 days OEM |
| Warranty | 2 years against manufacturing defects |
| Protocols | RS485/MODBUS RTU · Zigbee · GPRS/4G · LoRa · M-Bus |
| Certifications | IEC 62053-21/22/23 · IEC 61036 · ANSI C12 · MID · CE · RoHS · ISO 9001 · KEMA · CB · BV · CCC · CMC |

**Brand colors:** orange `#ED6512` · green `#81A331`
**Website:** `www.yominelectric.com`
**LinkedIn company page:** `linkedin.com/company/yominelectric`

> Never state a certification, statistic or spec that is not in this table or on the specific product page you are featuring.

### The 12 product categories

| # | Category | URL path |
|---|---|---|
| 1 | Energy Meters | `/products/energy-meter` |
| 2 | Current Transformers | `/products/current-transformer` |
| 3 | Voltage Stabilizer / Regulator | `/products/voltage-stabilizer-regulator` |
| 4 | Variac Transformer | `/products/variac-transformer` |
| 5 | Flexible Busbar | `/products/flexible-busbar` |
| 6 | Aluminum Busbar | `/products/aluminum-busbar` |
| 7 | Fuse & Protection | `/products/fuse-protection` |
| 8 | Sockets & Wiring | `/products/socket-wiring` |
| 9 | Solar & PV | `/products/solar-pv-products` |
| 10 | Terminals & Connectors | `/products/terminal-connector` |
| 11 | Security Seals | `/products/security-seal` |
| 12 | Screw Machines / Tools & Hardware | `/products/screw-machine` · `/products/tools-hardware` |

### Verified real models (examples — confirm current list per run)

| Category | Real model / product |
|---|---|
| Energy Meters | YEM024SJ-N — 4P, 3-phase 400V, 3×5(80)A DIN rail, Class 1.0 |
| Energy Meters | Single Phase 230V 5(30)A DIN rail kWh meter, Class 1.0 |
| Energy Meters | EP12D single-phase two-wire digital watt-hour meter, Class 0.5, 45A |
| Energy Meters | 3-phase 4-wire multifunction meter w/ maximum demand, Class 1.0, 60A |
| Energy Meters | 3×5(80A) 7P three-phase four-wire **WiFi** DIN rail smart meter, Class 1 |
| Current Transformers | NLH Series split-core CT, 5–4000A, flame-retardant PC+ABS, Class 0.5 |
| Current Transformers | NSQ Series toroidal CT 200/5, 5–4000A |
| Current Transformers | MSQ-60-250/5 — 50 turns, 720V AC, Class 0.5 |
| Current Transformers | MES Series toroidal CT, 5–4000A, Class 0.5/1, 50Hz |
| Current Transformers | MBO 0.66kV electromagnetic copper CT, 5–4000A |
| Tools & Hardware | Hydraulic Busbar Cutter — max 10mm thickness × 150mm width |
| Screw Machines | Automatic Screw Tightening Machine — 1600×730×1750 mm |

### Where the real product images live

**Live site:**
```
https://www.yominelectric.com/assets/images/products/{hash}.jpg|png
https://www.yominelectric.com/assets/images/home/products/{category}.png
```

**Local repo (4,127 files — the authoritative source for cutouts):**
```
assets/images/products/
assets/images/home/products/
```

> **Before generating any image, fetch the actual product page and read the real `src`.** Filenames are content hashes — never guess one.

---

## Phase 1 — Keyword research via 3UE Semrush

### 1.1 Access

1. Go to `https://dash.3ue.co/en-US/#/page/m/home`
2. Find the **SEO Tools / Semrush** subscription card → click **OPEN**
3. Lands you in the Semrush node at `sem.3ue.co`
4. If not logged in: **stop and report.** Never attempt credentials.

Login-gated — requires a real browser session. Delegate to a browser agent and pass the skill `[Harvest-SubAgent] 3UE Semrush Node Research` so the UI quirks are handled.

### 1.2 Domain baseline

```
https://sem.3ue.co/analytics/overview/?q=yominelectric.com&db=us
```

Record: **Authority Score · Organic Traffic · Organic Keywords count · Top Organic Keywords · AI mentions / cited pages.**
Log this every run — it is the only real proof the program is working.

### 1.3 Keyword Overview — seed list

Run **Keyword Overview** on seeds drawn from the 12 categories:

```
energy meter / kwh meter / din rail energy meter
smart energy meter / prepaid electricity meter
three phase energy meter / single phase kwh meter
electricity meter box / energy meter price
current transformer / split core current transformer
toroidal current transformer / CT accuracy class / CT ratio
voltage stabilizer / automatic voltage regulator / variac transformer
flexible busbar / aluminum busbar / busbar cutter
fuse switch disconnector / isolating switch fuse unit
industrial waterproof socket / PV combiner box / solar net meter
terminal block / security seal / meter sealing
RS485 modbus energy meter / wifi energy meter / IEC 62053
```

For each keyword record: **US Volume · Global Volume · KD · Intent · CPC · Top 3 ranking domains.**

> **Pitfall:** low-volume keywords often return an empty SERP table — record `n/a`, never fabricate a ranking.
> **Pitfall:** if US volume is 0 but the term is clearly commercial, check **IN · PK · NG · KE · ZA · AE · SA · BD · PH · BR · RU** databases. YOMIN's buyers are in Africa, the Middle East, South/SE Asia, Europe/CIS and the Americas — US-only volume badly understates real demand.

### 1.4 Keyword Gap

```
https://sem.3ue.co/analytics/keywordgap/?q=yominelectric.com&db=us
```

Click **Add more competitors** → add `archmeter.com`, `acrel-electric.ke`, plus one more metering manufacturer → click **Compare**.
Extract keywords where competitors rank and yominelectric.com does not.

> **Pitfall:** competitors are not active until explicitly selected AND **Compare** is clicked. Auto-suggestions alone do nothing.

### 1.5 Output of Phase 1

Write `_catalog_work/semrush-3ue-YYYY-MM-DD.md`:
- Domain baseline table (+ delta vs previous run)
- Full keyword table, `n/a` where missing
- Gap keyword list
- **Notes**: databases queried, SERP tables that failed, UI limits hit

---

## Phase 2 — Selecting keywords worth acting on

Apply all four filters. A keyword must pass **every** one.

| Filter | Rule | Reject if |
|---|---|---|
| **Real product** | Maps to one of the 12 categories AND a specific published model | No matching product in the catalog |
| **Buyer intent** | Commercial / transactional / technical-evaluation — the searcher is specifying, comparing or sourcing | Pure informational with no purchase path |
| **Cannibalization** | No existing yominelectric.com page or blog already targets it | An existing page already owns the term |
| **Winnability** | KD realistic vs current Authority Score; prefer specific long-tail | Head term owned by IEC/Schneider/ABB-tier domains |

**Prioritize specification-shaped queries** — `YEM024SJ-N 3 phase din rail meter`, `NLH split core CT 0.5 class`, `3×5(80)A energy meter`, `0.66kV toroidal CT 200/5`. The searcher already knows what they need and is hunting a supplier. Those convert.

**Reject example (real precedent):** *tile leveling* scored 2.4K US volume at KD 8 — attractive on paper, rejected because there is no genuine matching product depth in the catalog. Volume never overrides the real-product filter.

Output: **5 keywords max per run**, each with assigned category, target model, and the buyer question it answers.

---

## Phase 3 — Keyword → real-product image (Real-Life In-Use Imagery, Pinterest-Style Chrome)

One image per selected keyword. Each must feature the equipment in an authentic, active operational setting.

### 3.1 Non-negotiable image rules

1. **Authentic on-site in-use scene.** Every product image must depict the equipment actively in service in a realistic, on-site application/installation environment (bolted, wired, mounted, and operating just like in real life). Do NOT paste or composite raw studio cutouts randomly on top of backgrounds (which looks uninstalled); instead, generate the complete integrated scene depicting the product actively in use, wired, bolted, and seamlessly integrated into the site.
2. **Mandatory Pinterest inspiration.** Before generating the image, search Pinterest for the product's real-world installations and use cases (e.g. `site:pinterest.com "<product>" installation / use / panel`) to inspect how it is deployed in real life, and use those real-life pins as direct visual inspiration for the scene composition.
3. **No text clipping inside blogs.** All blog hero images must display unclipped (`.content-section .hero-img { width: 100%; height: auto; display: block; }` without `object-fit: cover` or fixed aspect-ratio constraints). The title banner, green spec chips, and bottom `#0A50A0` domain footer must remain 100% visible across all desktop and mobile viewports.
4. **Pinterest-style chrome.** Overlay the brand chrome: real YOMIN logo chip, clean industrial title banner (`MODEL | Application`), green-check spec chips, and the `#0A50A0` footer with `www.yominelectric.com`.
5. **No invented specifications.** Every number on the image (accuracy class, current rating, model code, protocol, standard) must come from the published product page. If unsure, leave it off.
6. **Approved claims only** — from the §0 table.
7. **Real logo only.** Never let a model draw the YOMIN wordmark — composite the real logo asset.
8. **Legible at thumbnail** — headline readable at 400px wide.

### 3.2 Keyword shape → image concept

| Keyword shape | Image concept | Product treatment |
|---|---|---|
| Product-type (`din rail energy meter`) | Hero — single unit, dramatic light, model + class | Full cutout, 3/4 angle, centered |
| Spec/model (`YEM024SJ-N`) | Spec card — product left, 4 specs right | Cutout + clean spec panel |
| Comparison (`class 1.0 vs 0.5S`) | Split composition, real product each side | Two cutouts, symmetric, labeled |
| Selection (`how to choose a CT ratio`) | Decision visual — product anchor + criteria | Cutout offset, criteria overlay |
| Standard (`IEC 62053`) | Trust card — product + certification marks | Cutout + badge row (real certs only) |
| Cost (`energy meter price`) | Value card — product + cost-driver list | Cutout + tiered list |

### 3.3 Prompt template — product hero

```
Professional B2B product marketing image for an international electrical
manufacturer.

SUBJECT (from reference image — preserve exactly):
The {MODEL CODE} {product name}. Keep the product's exact geometry,
proportions, housing color, terminal layout, LCD/display, button placement,
nameplate and printed labels untouched. Do not redraw, restyle or
re-proportion the hardware.

COMPOSITION:
Product as clean cutout, {centered / offset right}, ~55% of frame.
Background: {#ED6512 orange gradient / #81A331 green accent / dark industrial
gradient} — background only, no clutter behind the product.
Realistic shadow, professional studio lighting, photorealistic rendering.

TEXT:
Headline: "{HEADLINE — max 6 words}"
Sub: "{MODEL CODE} · {RATING} · {ACCURACY CLASS}"
Footer: real YOMIN logo + www.yominelectric.com
Typography: clean industrial sans-serif, high contrast, thumbnail-legible.

CONSTRAINTS:
- Do not alter the product in any way
- No invented specifications, certifications, awards or statistics
- No fake logos, no fake customer logos, no watermarks
- No human figures
```

**must_keep:** exact product geometry, housing color, proportions, nameplate, terminal layout, display
**must_change:** background, added text, lighting treatment only

### 3.4 Prompt template — spec card

```
B2B specification card for {MODEL CODE} {product name}.

LEFT 45%: the real product as a transparent cutout from the reference image,
completely unmodified.
RIGHT 55%: four specification rows, icon + label + value:
  {SPEC 1} / {SPEC 2} / {SPEC 3} / {SPEC 4}
  (all values copied verbatim from the published product page)

Footer strip: real YOMIN logo · "Since 1996 · 95+ Countries" ·
www.yominelectric.com
Background: clean #ED6512 / white panel, generous whitespace, technical-catalog feel.

Preserve the product exactly. Invent no specification values.
```

### 3.5 Per-image QA — all must pass

- [ ] Product is the **real** unit, visibly unmodified
- [ ] Transparent-cutout composite, not a photo box
- [ ] Every number traces to a published product page
- [ ] Model code spelled exactly as published
- [ ] Only §0 approved claims used
- [ ] Real logo asset composited, not model-drawn
- [ ] Headline legible at 400px
- [ ] No fabricated certifications, awards, statistics or customer logos
- [ ] Keyword's buyer intent visibly answered

---

## Phase 4 — LinkedIn post generation

### 4.1 The master image prompt (fill the brackets, use verbatim)

> Copy this whole block, replace every `[BRACKET]` with real values from the product page, and use it as the image-generation instruction. Do not soften the authenticity rules.

```
Create a premium, professional LinkedIn B2B marketing post for YOMIN Electric,
an international manufacturer and supplier of electrical products.

### BRAND & SOURCE REQUIREMENTS — VERY IMPORTANT

Use the REAL YOMIN Electric product, not an invented or generic replacement.

Website: https://www.yominelectric.com/

Use the REAL YOMIN logo exactly as provided on the official website:
YOMIN Electric

Use the REAL product appearance, shape, dimensions, materials, colors,
terminals, buttons, display, labels, connectors and technical details from the
official YOMIN website/product source.

Do NOT redesign, simplify, replace, fictionalize or hallucinate the product.

If a reference product image is provided, preserve the actual product
appearance and use it as the primary visual reference.

### PRODUCT

Featured product: [INSERT YOMIN PRODUCT NAME / MODEL]
Product category: [INSERT CATEGORY]
Official product/source page: [INSERT PRODUCT URL FROM YOMINELECTRIC.COM]

Main selling points:
* [FEATURE 1]
* [FEATURE 2]
* [FEATURE 3]
* [FEATURE 4]

### VISUAL STYLE

Create a high-end industrial B2B electrical engineering advertisement suitable
for LinkedIn.

Visual direction:
* Premium international electrical industry aesthetic
* Clean modern composition
* Professional engineering atmosphere
* Photorealistic product rendering
* Realistic lighting
* High-quality commercial product photography
* Subtle electrical/energy/industrial environment
* Sophisticated technical background
* Strong visual hierarchy
* Modern corporate design
* Minimal but powerful
* Trustworthy and suitable for international buyers, distributors, importers,
  contractors and electrical companies

The product must be the main visual focus.

Create a composition that immediately communicates:
Professional electrical technology + reliability + industrial quality +
global B2B supply.

### TEXT ON THE IMAGE

Include only concise marketing text.

Headline: [SHORT POWERFUL HEADLINE]
Optional supporting text: [SHORT BENEFIT / APPLICATION]

Include the REAL YOMIN logo prominently but naturally.
Include the REAL website: www.yominelectric.com

Do not add fake certifications, fake awards, fake statistics, fake customer
logos, fake contact information or invented specifications.

### TYPOGRAPHY

Use clean, modern, highly readable corporate typography.

The text must be:
* Correctly spelled
* Clearly readable
* Professionally aligned
* Not distorted
* Not overlapping the product
* Not excessive

Avoid filling the image with text.

### COMPOSITION

Use a LinkedIn-friendly 4:5 vertical composition (1080 × 1350).
Place the real product prominently in the foreground.
Use depth, realistic shadows and professional lighting.
Create enough negative space for the headline and supporting information.

The final image should look like it was produced by a professional
international electrical manufacturer's marketing department — not like an
AI-generated advertisement.

### AUTHENTICITY RULE

The final image must visually preserve the identity of the actual YOMIN product.

Do not:
* Invent another product
* Change the product model
* Change the logo
* Modify product labels
* Invent technical specifications
* Use generic stock electrical products
* Replace the product with an AI-designed equivalent
* Create a fake website
* Add fake company information
```

**Technical settings:** `aspect_ratio: "4:5"` · `size: "1080x1350"` · `resolution: "2K"`
**Tool:** image **edit** with the real product image as `reference_images` — never text-to-image for the product.

### 4.2 Caption structure

```
HOOK
Strong industry-focused opening that stops electrical engineers, distributors,
importers, contractors and B2B buyers mid-scroll.

PROBLEM / NEED
The common challenge this product addresses — one short paragraph.

SOLUTION
How the featured YOMIN product solves it.

KEY BENEFITS
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]
• [Benefit 4]

APPLICATIONS
Relevant industrial / commercial / utility applications.

B2B CTA
Invite distributors, wholesalers, electrical contractors, system integrators
and international buyers to contact YOMIN for product information, quotation
and cooperation.

www.yominelectric.com

#YOMIN #ElectricalProducts #ElectricalEngineering #EnergyManagement
#PowerDistribution #ElectricalEquipment #B2B #IndustrialAutomation
#SmartEnergy #ElectricalIndustry
```

### 4.3 Caption quality rules

- **Insight-led, not spam.** Open with a real field observation, not "Check out our latest product!"
- **3–4 hashtags** for organic posts; the 10-tag set above is for product-launch posts only. Never both styles at once.
- **One link, one CTA, one engagement question.** The question goes near the end and must be genuinely answerable by an engineer.
- **Every spec in the caption must be real** — same rule as the image.
- **The buyer's language.** Copy targets importers and engineers, not consumers.

### 4.4 Publishing

Order is fixed:
1. Publish blogs / push site changes
2. Generate the LinkedIn post + real-product image
3. **STOP and WAIT** for explicit go-ahead
4. Only then publish to the Zhejiang Yomin **company page**

**Route:** the Accio Browser Relay (authenticated Chrome admin session).
**Not the MCP connector** — that posts to the personal feed, not the company page.

| Fact | Value |
|---|---|
| Company page | `linkedin.com/company/yominelectric` |
| Admin company ID | **136016152** (the short ID 13601615 has NO admin access) |
| Admin posts URL | `linkedin.com/company/136016152/admin/page-posts/published/` |

**Relay pitfalls:**
- The "Start a post" button decays after 1–2 posts — **reload the page between every post**.
- Verify the composer header reads "Zhejiang Yomin Electric Co., Ltd." before every post — never the personal profile.
- Keep each URL on its own line so LinkedIn generates the preview card; don't delete the card.
- Confirm the post in the feed before marking it done. Clicking Post ≠ published.
- The relay writes helper `.js` files into the repo root — move them to `_catalog_work/linkedin-relay-scripts/` afterwards.

---

## 5. Run output structure

```
_catalog_work/
├── semrush-3ue-YYYY-MM-DD.md          Phase 1 — research data + baseline
├── shortlist-YYYY-MM-DD.md            Phase 2 — 5 keywords + rationale
├── linkedin-YYYY-MM-DD.md             Phase 4 — drafted posts (pre-approval)
├── linkedin-posted-YYYY-MM-DD.md      Phase 4 — published manifest + evidence
├── images/
│   ├── {keyword-slug}-hero.png
│   └── {keyword-slug}-linkedin-4x5.png
└── linkedin-relay-scripts/            relay helper files, moved out of repo root
```

The manifest is the audit trail: keyword → model → product-page URL → source image → generated image → post status + feed evidence.

---

## 6. Hard stops

Stop and ask rather than proceeding if:

- 3UE shows a login wall → report, never attempt credentials
- A shortlisted keyword has no matching real product → drop it, never invent a product
- A product page lacks a spec you want to show → leave the spec off
- A model wants to draw the YOMIN logo → composite the real asset instead
- Semrush returns no volume in any database → keyword unvalidated, do not proceed
- Anything would require a certification, award or statistic not in §0 → omit it

---

## 7. Cadence

Run the full playbook per content cycle. Log the Phase 1 domain baseline every single time — Authority Score, organic keywords, organic traffic and AI mentions across successive runs are the actual proof of return. A run that ships images and posts but records no baseline has no way to demonstrate it worked.
