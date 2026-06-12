# Generate SEO category landing pages from products.html template
$ErrorActionPreference = "Stop"
$template = Get-Content "products.html" -Raw

$categories = @(
  @{
    slug = "energy-meter"
    filter = "Energy Meter"
    title = "Energy Meters - Single & Three Phase | Yomin Electric"
    desc = "Factory-direct energy meters: single phase, three phase, prepaid STS keypad meters. DIN rail, LCD backlit, RS485 MODBUS. CE certified, ISO9001. Low MOQ from 100 units."
    canonical = "https://www.yominelectric.com/products/energy-meter"
    ldName = "Energy Meters"
    ldDesc = "Yomin Electric energy meter product category: single phase, three phase, prepaid STS, and smart energy meters for residential, commercial and industrial metering."
  },
  @{
    slug = "voltage-stabilizer-regulator"
    filter = "Voltage Stabilizer/Regulator"
    title = "Voltage Stabilizers & Regulators - Automatic AVR | Yomin Electric"
    desc = "Factory-direct voltage stabilizers and automatic voltage regulators (AVR). Single & three phase, servo motor control, LED display, 50/60Hz. Home and industrial use. Low MOQ from China."
    canonical = "https://www.yominelectric.com/products/voltage-stabilizer-regulator"
    ldName = "Voltage Stabilizers & Regulators"
    ldDesc = "Yomin Electric voltage stabilizer product category: automatic AC voltage regulators, servo motor stabilizers, single and three phase AVR for home, medical, CNC and industrial protection."
  },
  @{
    slug = "current-transformer"
    filter = "Current Transformer"
    title = "Current Transformers - Split Core & Solid Core CT | Yomin Electric"
    desc = "Precision current transformers for metering and protection. Class 0.2s to 1, 5A/1A secondary, split core and molded case. IEC 61869-2. Factory direct, low MOQ from China."
    canonical = "https://www.yominelectric.com/products/current-transformer"
    ldName = "Current Transformers"
    ldDesc = "Yomin Electric current transformer product category: low voltage CTs for metering, protection, energy monitoring, split core CTs for retrofit, and panel-mounted CTs."
  },
  @{
    slug = "variac-transformer"
    filter = "Variac/Transformer"
    title = "Variac Transformers - Variable AC Voltage | Yomin Electric"
    desc = "Variable voltage transformers for lab testing, R&D, and industrial voltage adjustment. Single & three phase, 500VA to 30kVA, copper windings. OEM/ODM available. Low MOQ 10 units."
    canonical = "https://www.yominelectric.com/products/variac-transformer"
    ldName = "Variac Transformers"
    ldDesc = "Yomin Electric variac transformer product category: variable AC voltage transformers, auto transformers for laboratory, industrial testing and voltage control applications."
  },
  @{
    slug = "screw-machine"
    filter = "Screw Machine"
    title = "Automatic Screw Assembly Machines | Yomin Electric"
    desc = "Automatic screw driving and assembly machines for brass/aluminum busbar processing, terminal block production. OEM customization, 2-year warranty. Factory direct from Zhejiang, China."
    canonical = "https://www.yominelectric.com/products/screw-machine"
    ldName = "Screw Assembly Machines"
    ldDesc = "Yomin Electric screw machine product category: automatic drilling, tapping, screw assembly machines for busbar and terminal block production. CE certified, ISO9001."
  },
  @{
    slug = "fuse-protection"
    filter = "Fuse & Protection"
    title = "Fuses & Protection Devices - Overcurrent Safety | Yomin Electric"
    desc = "Overcurrent protection fuses and circuit safety devices for solar PV systems, LV distribution boards, and industrial panels. CE certified. Factory direct from China, low MOQ."
    canonical = "https://www.yominelectric.com/products/fuse-protection"
    ldName = "Fuses & Protection"
    ldDesc = "Yomin Electric fuse and protection product category: overcurrent fuses, circuit protection devices for solar, industrial, and LV distribution applications."
  },
  @{
    slug = "voltage-protector"
    filter = "Voltage Protector"
    title = "Voltage Protectors - Surge & Phase Protection | Yomin Electric"
    desc = "Voltage and surge protectors for household appliances, refrigerators, AC units, motors. Phase protection, over/under voltage cutoff. Factory direct from China, competitive pricing."
    canonical = "https://www.yominelectric.com/products/voltage-protector"
    ldName = "Voltage Protectors"
    ldDesc = "Yomin Electric voltage protector product category: surge protectors, phase protection, over/under voltage cutoff devices for household and commercial appliances."
  },
  @{
    slug = "socket-wiring"
    filter = "Socket & Wiring"
    title = "Smart Sockets & Wiring Accessories | Yomin Electric"
    desc = "Smart WiFi sockets, switches, and wiring accessories for home automation and office use. App-controlled, CE certified. Factory direct from China with low MOQ for distributors."
    canonical = "https://www.yominelectric.com/products/socket-wiring"
    ldName = "Sockets & Wiring"
    ldDesc = "Yomin Electric socket and wiring product category: smart sockets, switches, wiring accessories for home automation, office, and EV charging applications."
  },
  @{
    slug = "terminal-connector"
    filter = "Terminal & Connector"
    title = "Terminals & Connectors - DIN Rail Panel Wiring | Yomin Electric"
    desc = "DIN rail terminals, connectors, and wiring accessories for control cabinets, switchboards, and industrial panel wiring. CE certified. Factory direct from Zhejiang, China. Low MOQ."
    canonical = "https://www.yominelectric.com/products/terminal-connector"
    ldName = "Terminals & Connectors"
    ldDesc = "Yomin Electric terminal and connector product category: DIN rail terminals, cable connectors, wiring accessories for control cabinets and industrial installations."
  },
  @{
    slug = "solar-pv-products"
    filter = "Solar/PV Products"
    title = "Solar & PV Products - Grid-Tie & Off-Grid | Yomin Electric"
    desc = "Solar power products for grid-tie, off-grid, and PV combiner box applications. PV connectors, DC isolators, and solar accessories. CE certified. Factory direct from China."
    canonical = "https://www.yominelectric.com/products/solar-pv-products"
    ldName = "Solar & PV Products"
    ldDesc = "Yomin Electric solar and PV product category: solar connectors, combiner boxes, DC isolators, and accessories for residential and commercial solar installations."
  },
  @{
    slug = "tools-hardware"
    filter = "Tools & Hardware"
    title = "Industrial Tools & Hardware | Yomin Electric"
    desc = "Industrial control tools, isolation transformers, machine tool accessories, and factory equipment. ISO9001 certified. Export-quality hardware from China, factory-direct pricing."
    canonical = "https://www.yominelectric.com/products/tools-hardware"
    ldName = "Tools & Hardware"
    ldDesc = "Yomin Electric tools and hardware product category: industrial control products, machine tools, isolation transformers for factory automation and OEM projects."
  },
  @{
    slug = "security-seal"
    filter = "Security Seal"
    title = "Security Seals - Meter Anti-Tamper | Yomin Electric"
    desc = "Anti-tamper security seals for utility metering, revenue protection, and smart grid compliance. CE certified. Factory direct from China with low MOQ for utility companies."
    canonical = "https://www.yominelectric.com/products/security-seal"
    ldName = "Security Seals"
    ldDesc = "Yomin Electric security seal product category: anti-tamper meter seals, revenue protection seals for utility metering and smart grid applications."
  },
  @{
    slug = "other"
    filter = "Other"
    title = "Other Electrical Products | Yomin Electric"
    desc = "Additional electrical products and accessories for industrial and commercial use. CE certified, ISO9001. Export-ready, factory-direct from Zhejiang, China."
    canonical = "https://www.yominelectric.com/products/other"
    ldName = "Other Products"
    ldDesc = "Yomin Electric additional electrical products: industrial components, accessories, and specialized electrical equipment for export markets worldwide."
  },
  @{
    slug = "busbar"
    filter = "__busbar__"
    title = "Busbars - Flexible, Rigid, Aluminum | Yomin Electric"
    desc = "Flexible, rigid, aluminum, composite laminated, and CCS integrated busbars for EV battery packs, energy storage, and power distribution. Quote-based pricing. Factory direct from China."
    canonical = "https://www.yominelectric.com/products/busbar"
    ldName = "Busbars"
    ldDesc = "Yomin Electric busbar product category: flexible busbars, rigid busbars, aluminum busbars, composite laminated busbars for EV, energy storage and power distribution."
  }
)

foreach ($cat in $categories) {
  $content = $template

  # 1) Title
  $content = $content -replace '<title>Energy Meters, CTs & Voltage Regulators \| Yomin Electric</title>', "<title>$($cat.title)</title>"

  # 2) Meta description
  $content = $content -replace '<meta name="description" content="Browse[^"]*">', "<meta name=`"description`" content=`"$($cat.desc)`">"

  # 3) Canonical
  $content = $content -replace '<link rel="canonical" href="https://www\.yominelectric\.com/products[^"]*" />', "<link rel=`"canonical`" href=`"$($cat.canonical)`" />"

  # 4) Structured data (replace whole ItemList block)
  $ldJson = @"
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "$($cat.ldName)",
  "description": "$($cat.ldDesc)",
  "url": "$($cat.canonical)",
  "mainEntity": {
    "@type": "ItemList",
    "url": "$($cat.canonical)"
  }
}
</script>
"@
  # Escape for regex
  $ldEscaped = [regex]::Escape($ldJson)
  $content = $content -replace '<script type="application/ld\+json">[\s\S]*?</script>', $ldJson

  # 5) Add global category preset
  $preset = "<script>window.YOMIN_ACTIVE_CATEGORY = '$($cat.filter)';</script>"
  # Insert after charset meta tag
  $content = $content -replace '(<meta charset="UTF-8">)', "`$1`n  $preset"

  # 6) Update the slug redirect script canonical URL (optional but good)
  $content = $content -replace "canon.href = 'https://www\.yominelectric\.com/products\?category=' \+ slug;", "canon.href = '$($cat.canonical)';"

  # Write file
  $rootDir = Split-Path -Parent $PSScriptRoot
  if (-not $rootDir) { $rootDir = Get-Location }
  $outPath = Join-Path $rootDir "$($cat.slug).html"
  [System.IO.File]::WriteAllText($outPath, $content, [System.Text.UTF8Encoding]::new($false))
  Write-Host "Created: $outPath"
}

Write-Host "`nDone! Generated $($categories.Count) category pages."
