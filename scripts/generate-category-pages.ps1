# Generate SEO category landing pages from products.html template
$ErrorActionPreference = "Stop"
$template = Get-Content "products.html" -Raw

$categories = @(
  @{
    slug = "energy-meter"
    filter = "Energy Meter"
    title = "Energy Meters - Single & Three Phase | Yomin Electric"
    desc = "Factory-direct energy meters: single phase, three phase, prepaid STS keypad meters. DIN rail, LCD backlit, RS485 MODBUS. CE certified, ISO9001. Low MOQ from 100 units."
    canonical = "https://www.yominelectric.com/products?category=energy-meter"
    ldName = "Energy Meters"
    ldDesc = "Yomin Electric energy meter product category: single phase, three phase, prepaid STS, and smart energy meters for residential, commercial and industrial metering."
  },
  @{
    slug = "voltage-stabilizer-regulator"
    filter = "Voltage Stabilizer/Regulator"
    title = "Voltage Stabilizers & Regulators | Yomin Electric"
    desc = "Factory-direct voltage stabilizers and automatic voltage regulators (AVR). Single & three phase, servo motor control, LED display, 50/60Hz. Home and industrial use. Low MOQ from China."
    canonical = "https://www.yominelectric.com/products?category=voltage-stabilizer-regulator"
    ldName = "Voltage Stabilizers & Regulators"
    ldDesc = "Yomin Electric voltage stabilizer product category: automatic AC voltage regulators, servo motor stabilizers, single and three phase AVR for home, medical, CNC and industrial protection."
  },
  @{
    slug = "current-transformer"
    filter = "Current Transformer"
    title = "Current Transformers - Split Core & Solid Core CT | Yomin Electric"
    desc = "Precision current transformers for metering and protection. Class 0.2s to 1, 5A/1A secondary, split core and molded case. IEC 61869-2. Factory direct, low MOQ from China."
    canonical = "https://www.yominelectric.com/products?category=current-transformer"
    ldName = "Current Transformers"
    ldDesc = "Yomin Electric current transformer product category: low voltage CTs for metering, protection, energy monitoring, split core CTs for retrofit, and panel-mounted CTs."
  },
  @{
    slug = "variac-transformer"
    filter = "Variac/Transformer"
    title = "Variac Transformers - Variable AC Voltage | Yomin Electric"
    desc = "Variable voltage transformers for lab testing, R&D, and industrial voltage adjustment. Single & three phase, 500VA to 30kVA, copper windings. OEM/ODM available. Low MOQ 10 units."
    canonical = "https://www.yominelectric.com/products?category=variac-transformer"
    ldName = "Variac Transformers"
    ldDesc = "Yomin Electric variac transformer product category: variable AC voltage transformers, auto transformers for laboratory, industrial testing and voltage control applications."
  },
  @{
    slug = "screw-machine"
    filter = "Screw Machine"
    title = "Automatic Screw Assembly Machines | Yomin Electric"
    desc = "Automatic screw driving and assembly machines for brass/aluminum busbar processing, terminal block production. OEM customization, 2-year warranty. Factory direct from Zhejiang, China."
    canonical = "https://www.yominelectric.com/products?category=screw-machine"
    ldName = "Screw Assembly Machines"
    ldDesc = "Yomin Electric screw machine product category: automatic drilling, tapping, screw assembly machines for busbar and terminal block production. CE certified, ISO9001."
  },
  @{
    slug = "fuse-protection"
    filter = "Fuse & Protection"
    title = "Fuses & Protection Devices | Yomin Electric"
    desc = "Overcurrent protection fuses and circuit safety devices for solar PV systems, LV distribution boards, and industrial panels. CE certified. Factory direct from China, low MOQ."
    canonical = "https://www.yominelectric.com/products?category=fuse-protection"
    ldName = "Fuses & Protection"
    ldDesc = "Yomin Electric fuse and protection product category: overcurrent fuses, circuit protection devices for solar, industrial, and LV distribution applications."
  },
  @{
    slug = "voltage-protector"
    filter = "Voltage Protector"
    title = "Voltage Protectors | Yomin Electric"
    desc = "Voltage and surge protectors for household appliances, refrigerators, AC units, motors. Phase protection, over/under voltage cutoff. Factory direct from China, competitive pricing."
    canonical = "https://www.yominelectric.com/products?category=voltage-protector"
    ldName = "Voltage Protectors"
    ldDesc = "Yomin Electric voltage protector product category: surge protectors, phase protection, over/under voltage cutoff devices for household and commercial appliances."
  },
  @{
    slug = "socket-wiring"
    filter = "Socket & Wiring"
    title = "Smart Sockets & Wiring | Yomin Electric"
    desc = "Smart WiFi sockets, switches, and wiring accessories for home automation and office use. App-controlled, CE certified. Factory direct from China with low MOQ for distributors."
    canonical = "https://www.yominelectric.com/products?category=socket-wiring"
    ldName = "Sockets & Wiring"
    ldDesc = "Yomin Electric socket and wiring product category: smart sockets, switches, wiring accessories for home automation, office, and EV charging applications."
  },
  @{
    slug = "terminal-connector"
    filter = "Terminal & Connector"
    title = "Terminals & Connectors | Yomin Electric"
    desc = "DIN rail terminals, connectors, and wiring accessories for control cabinets, switchboards, and industrial panel wiring. CE certified. Factory direct from Zhejiang, China. Low MOQ."
    canonical = "https://www.yominelectric.com/products?category=terminal-connector"
    ldName = "Terminals & Connectors"
    ldDesc = "Yomin Electric terminal and connector product category: DIN rail terminals, cable connectors, wiring accessories for control cabinets and industrial installations."
  },
  @{
    slug = "solar-pv-products"
    filter = "Solar/PV Products"
    title = "Solar & PV Products | Yomin Electric"
    desc = "Solar power products for grid-tie, off-grid, and PV combiner box applications. PV connectors, DC isolators, and solar accessories. CE certified. Factory direct from China."
    canonical = "https://www.yominelectric.com/products?category=solar-pv-products"
    ldName = "Solar & PV Products"
    ldDesc = "Yomin Electric solar and PV product category: solar connectors, combiner boxes, DC isolators, and accessories for residential and commercial solar installations."
  },
  @{
    slug = "tools-hardware"
    filter = "Tools & Hardware"
    title = "Industrial Tools & Hardware | Yomin Electric"
    desc = "Industrial control tools, isolation transformers, machine tool accessories, and factory equipment. ISO9001 certified. Export-quality hardware from China, factory-direct pricing."
    canonical = "https://www.yominelectric.com/products?category=tools-hardware"
    ldName = "Tools & Hardware"
    ldDesc = "Yomin Electric tools and hardware product category: industrial control products, machine tools, isolation transformers for factory automation and OEM projects."
  },
  @{
    slug = "security-seal"
    filter = "Security Seal"
    title = "Security Seals - Anti-Tamper Meter Seals | Yomin Electric"
    desc = "Anti-tamper security seals for utility metering, revenue protection, and smart grid compliance. CE certified. Factory direct from China with low MOQ for utility companies."
    canonical = "https://www.yominelectric.com/products?category=security-seal"
    ldName = "Security Seals"
    ldDesc = "Yomin Electric security seal product category: anti-tamper meter seals, revenue protection seals for utility metering and smart grid applications."
  },
  @{
    slug = "other"
    filter = "Other"
    title = "Other Electrical Products | Yomin Electric"
    desc = "Additional electrical products and accessories for industrial and commercial use. CE certified, ISO9001. Export-ready, factory-direct from Zhejiang, China."
    canonical = "https://www.yominelectric.com/products?category=other"
    ldName = "Other Products"
    ldDesc = "Yomin Electric additional electrical products: industrial components, accessories, and specialized electrical equipment for export markets worldwide."
  },
  @{
    slug = "aluminum-busbar"
    filter = "Aluminum Busbar"
    title = "Aluminum Busbars for Power Distribution | Yomin Electric"
    desc = "High-conductivity aluminum busbars for switchgear, panel boards, and power distribution. Custom sizes available. Factory direct from China with competitive pricing."
    canonical = "https://www.yominelectric.com/products?category=aluminum-busbar"
    ldName = "Aluminum Busbars"
    ldDesc = "Yomin Electric aluminum busbar product category: high-conductivity aluminum busbars for LV and MV switchgear, power distribution panels, and electrical enclosures."
  },
  @{
    slug = "flexible-busbar"
    filter = "Flexible Busbar"
    title = "Flexible Busbars for Battery & EV | Yomin Electric"
    desc = "Flexible laminated copper and aluminum busbars for battery packs, EV power distribution, and energy storage. ISO9001 certified, custom designs."
    canonical = "https://www.yominelectric.com/products?category=flexible-busbar"
    ldName = "Flexible Busbars"
    ldDesc = "Yomin Electric flexible busbar product category: laminated flexible busbars for EV battery packs, energy storage systems, and power electronics."
  },
  @{
    slug = "rigid-busbar"
    filter = "Rigid Busbar"
    title = "Rigid Busbars for Panel Boards | Yomin Electric"
    desc = "Rigid copper and aluminum busbars for LV panel boards, switchgear, and distribution cabinets. Insulated and bare options. Factory direct pricing."
    canonical = "https://www.yominelectric.com/products?category=rigid-busbar"
    ldName = "Rigid Busbars"
    ldDesc = "Yomin Electric rigid busbar product category: rigid copper and aluminum busbars for switchgear, panel boards, and industrial power distribution."
  },
  @{
    slug = "energy-storage-busbar"
    filter = "Energy Storage Busbar"
    title = "Energy Storage Busbars for BESS | Yomin Electric"
    desc = "High-current busbars for battery energy storage systems (BESS). Custom configurations for Li-ion battery racks and containerized storage. OEM/ODM available."
    canonical = "https://www.yominelectric.com/products?category=energy-storage-busbar"
    ldName = "Energy Storage Busbars"
    ldDesc = "Yomin Electric energy storage busbar product category: high-current busbars for battery energy storage systems, Li-ion racks, and grid-scale storage solutions."
  },
  @{
    slug = "busbar-protection"
    filter = "Busbar Protection"
    title = "Busbar Protection Systems | Yomin Electric"
    desc = "Busbar differential protection relays, arc flash detection, and insulation monitoring for LV and MV busbar systems. IEC 61850 compliant, factory direct."
    canonical = "https://www.yominelectric.com/products?category=busbar-protection"
    ldName = "Busbar Protection"
    ldDesc = "Yomin Electric busbar protection product category: differential protection relays, arc flash detection, insulation monitoring for power distribution busbar systems."
  },
  @{
    slug = "composite-laminated-busbar"
    filter = "Composite Laminated Busbar"
    title = "Composite Laminated Busbars | Yomin Electric"
    desc = "Composite laminated busbars for compact power distribution. Lightweight, high insulation, low inductance design. Custom engineering available."
    canonical = "https://www.yominelectric.com/products?category=composite-laminated-busbar"
    ldName = "Composite Laminated Busbars"
    ldDesc = "Yomin Electric composite laminated busbar product category: lightweight laminated busbars for compact power electronics, converters, and inverters."
  },
  @{
    slug = "ccs-integrated-busbar"
    filter = "CCS Integrated Busbar"
    title = "CCS Integrated Busbars | Yomin Electric"
    desc = "Cell Contacting System (CCS) integrated busbars for battery modules. Precision welding, FPC/FFC integration. Designed for EV and ESS battery pack assembly."
    canonical = "https://www.yominelectric.com/products?category=ccs-integrated-busbar"
    ldName = "CCS Integrated Busbars"
    ldDesc = "Yomin Electric CCS integrated busbar product category: cell contacting system busbars for EV battery modules and energy storage pack assembly."
  },
  @{
    slug = "heavy-duty-busbar"
    filter = "Heavy Duty Busbar"
    title = "Heavy Duty Busbars for High Current | Yomin Electric"
    desc = "Heavy duty copper busbars rated for high current applications up to 6300A. Fabricated to IEC 61439 standards. Custom bending, drilling, and plating."
    canonical = "https://www.yominelectric.com/products?category=heavy-duty-busbar"
    ldName = "Heavy Duty Busbars"
    ldDesc = "Yomin Electric heavy duty busbar product category: high-current copper busbars for main distribution boards, generator connections, and industrial power systems."
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

  # 4) Structured data
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
  $content = $content -replace '<script type="application/ld\+json">[\s\S]*?</script>', $ldJson

  # 5) Add global category preset
  $preset = "<script>window.YOMIN_ACTIVE_CATEGORY = '$($cat.filter)';</script>"
  $content = $content -replace '(<meta charset="UTF-8">)', "`$1`n  $preset"

  # 6) Update inline canonical redirect fixup
  $content = $content -replace "canon.href = 'https://www\.yominelectric\.com/products\?category=' \+ slug;", "canon.href = '$($cat.canonical)';"

  # Write file
  $rootDir = Split-Path -Parent $PSScriptRoot
  if (-not $rootDir) { $rootDir = Get-Location }
  $outPath = Join-Path $rootDir "$($cat.slug).html"
  [System.IO.File]::WriteAllText($outPath, $content, [System.Text.UTF8Encoding]::new($false))
  Write-Host "Created: $($cat.slug).html"
}

Write-Host "`nDone! Generated $($categories.Count) category pages."
