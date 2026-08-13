# Generate static HTML product pages: products/<catSlug>/<productSlug>.html
# Usage: powershell -File tools\generate-product-pages.ps1
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$data = Get-Content (Join-Path $root 'data\products.json') -Raw -Encoding UTF8 | ConvertFrom-Json

$CAT_SLUG = @{
  'Energy Meter' = 'energy-meter'; 'Voltage Stabilizer/Regulator' = 'voltage-stabilizer-regulator'
  'Current Transformer' = 'current-transformer'; 'Screw Machine' = 'screw-machine'
  'Flexible Busbar' = 'flexible-busbar'; 'Rigid Busbar' = 'rigid-busbar'
  'Aluminum Busbar' = 'aluminum-busbar'; 'Composite Laminated Busbar' = 'composite-laminated-busbar'
  'CCS Integrated Busbar' = 'ccs-integrated-busbar'; 'Heavy Duty Busbar' = 'heavy-duty-busbar'
  'Energy Storage Busbar' = 'energy-storage-busbar'; 'Busbar Protection' = 'busbar-protection'
  'Variac/Transformer' = 'variac-transformer'; 'Terminal & Connector' = 'terminal-connector'
  'Solar/PV Products' = 'solar-pv-products'; 'Fuse & Protection' = 'fuse-protection'
  'Voltage Protector' = 'voltage-protector'; 'Socket & Wiring' = 'socket-wiring'
  'Tools & Hardware' = 'tools-hardware'; 'Security Seal' = 'security-seal'
  'Emergency Lighting' = 'emergency-lighting'; 'Other' = 'other'
}

function Get-Slug([string]$s) {
  $s = $s.ToLowerInvariant()
  $s = $s -replace '[^a-z0-9]+', '-'
  return $s.Trim('-')
}
function Esc([string]$s) {
  if ($null -eq $s) { return '' }
  return $s.Replace('&', '&amp;').Replace('<', '&lt;').Replace('>', '&gt;').Replace('"', '&quot;').Replace("'", '&#39;')
}
function UrlEnc([string]$s) { return [uri]::EscapeDataString($s) }
function SpecVal($v) {
  if ($null -eq $v) { return '' }
  if ($v -is [System.Array]) { return (($v | ForEach-Object { $_.ToString() }) -join '; ') }
  if ($v -is [System.Management.Automation.PSCustomObject]) {
    $parts = @(); foreach ($pp in $v.PSObject.Properties) { $parts += ($pp.Name + ': ' + $pp.Value) }
    return ($parts -join '; ')
  }
  return $v.ToString()
}

# --- slug assignment (same algorithm as products.js: dedupe with id suffix) ---
$used = @{}
foreach ($p in $data) {
  $slug = Get-Slug $p.title
  if ($used.ContainsKey($slug)) { $slug = $slug + '-' + $p.id }
  $used[$slug] = $true
  $p | Add-Member -NotePropertyName slug -NotePropertyValue $slug -Force
}

$head = @'
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T0HYWYQ6NF"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-T0HYWYQ6NF');</script>
<meta charset="UTF-8">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/logo_transparent.png">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@TITLE@ | Yomin Electric</title>
<meta name="description" content="@DESC@">
<link rel="canonical" href="@CANON@">
<meta property="og:title" content="@TITLE@">
<meta property="og:description" content="@DESC@">
<meta property="og:url" content="@CANON@">
<meta property="og:type" content="product">
<meta property="og:image" content="@OGIMG@">
<meta property="og:site_name" content="Yomin Electric">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="@TITLE@">
<meta name="twitter:description" content="@DESC@">
<meta name="twitter:image" content="@OGIMG@">
<meta name="robots" content="index, follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet"></noscript>
<link rel="stylesheet" href="/assets/css/product-page.css">
@JSONLD@
</head>
<body>

<nav id="nav">
  <a href="/" class="n-logo"><img src="/logo_transparent.png" alt="Yomin Electric" width="44" height="44"></a>
  <ul class="n-ctr">
    <li><a href="/">Home</a></li>
    <li><a href="/products" class="active">Products</a></li>
    <li><a href="/solutions">Solutions</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/process">Process</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
  <div class="n-rt">
    <div class="theme-pair">
      <button class="theme-btn-s" id="btnDark" aria-label="Dark mode"><span class="t-ic">&#9790;</span></button>
      <button class="theme-btn-s active" id="btnLight" aria-label="Light mode"><span class="t-ic">&#9728;</span></button>
    </div>
    <a href="/contact" class="ncta">Get Quote</a>
    <button class="ham" id="ham"><span></span><span></span><span></span></button>
  </div>
</nav>

<div class="mob" id="mob">
  <button class="mob-x" id="mob-x">&#10005;</button>
  <a href="/">Home</a>
  <a href="/products">Products</a>
  <a href="/solutions">Solutions</a>
  <a href="/blog">Blog</a>
  <a href="/process">Process</a>
  <a href="/about">About</a>
  <a href="/contact">Contact</a>
</div>

<main>
  <div class="container">
    <div class="crumbs">
      <a href="/">Home</a><span class="sep">&#183;</span><a href="/products">Products</a><span class="sep">&#183;</span><a href="@CATLINK@">@CATNAME@</a><span class="sep">&#183;</span><span class="cur">@TITLE@</span>
    </div>

    <div class="product-layout">
      <div class="gallery">
        <div class="g-main"><img id="mainImg" src="@IMG0@" alt="@ALTDESC@" loading="eager"></div>
        @THUMBS@
      </div>
      <div class="p-info">
        <h1>@TITLE@</h1>
        <a href="@CATLINK@" class="p-cat">@CATNAME@</a>
        <div class="p-price">Request Quote</div>
        <p class="p-desc">@DESCHTML@</p>
        <div class="p-actions">
          <a class="btn btn-main" href="/contact?product=@QUOTEPARAM@">Request a Quote</a>
          <a class="btn btn-wa" href="@WALINK@" target="_blank" rel="noopener">WhatsApp</a>
          <a class="btn btn-ghost" href="@CATLINK@">More in @CATNAME@</a>
        </div>
        @KEYWORDS@
        @DATASHEET@
      </div>
    </div>

    @DETAILS@
  </div>
</main>

<footer>
  <div>
    <div class="ft-brand-n">Yomin Electric</div>
    <div class="ft-sub">Zhejiang Yomin Electric Co., Ltd. &#8212; Precision energy metering solutions since 1996.</div>
  </div>
  <div class="ft-links">
    <a href="/">Home</a><a href="/products">Products</a><a href="/blog">Blog</a><a href="/about">About</a><a href="/contact">Contact</a>
  </div>
</footer>

<div class="float-btns">
  <button class="float-btn float-btn-wc" id="wc-btn">
    <svg viewBox="0 0 24 24" fill="white" width="26" height="26"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 3.882-1.98 5.853-1.838-.576-3.583-3.895-6.348-7.596-6.348zM5.785 5.991c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178A1.17 1.17 0 0 1 4.623 7.17c0-.651.52-1.18 1.162-1.18zm4.315 0c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178 1.17 1.17 0 0 1-1.162-1.178c0-.651.52-1.18 1.162-1.18z"/></svg>
  </button>
  <a class="float-btn float-btn-wa" href="https://wa.me/8619016543301" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24" fill="white" width="26" height="26"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
  </a>
</div>

<div class="wc-modal-overlay" id="wc-overlay">
  <div class="wc-modal">
    <div class="wc-modal-icon">&#128172;</div>
    <div class="wc-modal-title">Connect on WeChat</div>
    <div class="wc-modal-sub">Scan the QR code with WeChat to reach our sales team directly.</div>
    <div class="wc-qr-wrap"><img src="/assets/images/qr-wechat.jpg" alt="WeChat QR"></div>
    <button class="wc-modal-close" id="wc-close">&#10005; Close</button>
  </div>
</div>

<script src="/assets/js/product-page.js"></script>
</body>
</html>
'@

$outBase = Join-Path $root 'products'
$count = 0
foreach ($p in $data) {
  $catSlug = $CAT_SLUG[$p.category]
  if (-not $catSlug) { $catSlug = 'other' }
  $slug = $p.slug
  $canon = "https://www.yominelectric.com/products/$catSlug/$slug"
  $title = Esc $p.title
  $desc = Esc $p.description
  $descMeta = $p.description
  if ($descMeta.Length -gt 155) { $descMeta = $descMeta.Substring(0, 152).TrimEnd() + '...' }
  $descMeta = Esc $descMeta

  $imgList = @($p.images)
  if ($imgList.Count -eq 0 -and $p.image) { $imgList = @($p.image) }
  $img0 = if ($imgList.Count -gt 0) { $imgList[0] } else { '/assets/images/placeholder.png' }
  $ogimg = 'https://www.yominelectric.com' + $img0
  $alts = Esc $p.title

  # thumbnails
  $thumbs = ''
  if ($imgList.Count -gt 1) {
    $thumbs = '<div class="g-thumbs">'
    for ($i = 0; $i -lt $imgList.Count; $i++) {
      $cls = if ($i -eq 0) { ' active' } else { '' }
      $thumbs += "<img class=`"$cls`" src=`"$($imgList[$i])`" data-full=`"$($imgList[$i])`" alt=`"$alts $($i+1)`">"
    }
    $thumbs += '</div>'
  }

  # description html
  $descHtml = (Esc $p.description) -replace "`n", '<br>'

  # keywords chips
  $kw = ''
  $kwLines = @($p.keywords -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ })
  if ($kwLines.Count -gt 0) {
    $kw = '<div class="p-meta">'
    foreach ($k in $kwLines) { $kw += "<span class=`"chip`">$(Esc $k)</span>" }
    $kw += '</div>'
  }

  # datasheet
  $ds = ''
  if ($p.datasheet) { $ds = '<a class="dsheet" href="' + (Esc $p.datasheet) + '" target="_blank" rel="noopener">&#128196; Download Datasheet (PDF)</a>' }

  # specs table
  $specsHtml = ''
  if ($p.specs -and ($p.specs.PSObject.Properties.Count -gt 0)) {
    $rows = ''
    foreach ($prop in $p.specs.PSObject.Properties) {
      $val = SpecVal $prop.Value
      if ($val) { $rows += "<tr><th>$(Esc $prop.Name)</th><td>$(Esc $val)</td></tr>" }
    }
    if ($rows) { $specsHtml = "<table class=`"specs`"><tbody>$rows</tbody></table>" }
  }

  # processes
  $procHtml = ''
  if ($p.processes -and @($p.processes).Count -gt 0) {
    $steps = ''
    foreach ($st in @($p.processes)) {
      $extra = ($st.PSObject.Properties | Where-Object { $_.Name -notin @('step', 'title') } | ForEach-Object { (SpecVal $_.Value) } | Where-Object { $_ }) -join ' '
      $extraHtml = ''
      if ($extra) { $extraHtml = "<p>$(Esc $extra)</p>" }
      $steps += "<div class=`"pstep`"><div class=`"num`">$(Esc $st.step)</div><div class=`"txt`"><strong>$(Esc $st.title)</strong>$extraHtml</div></div>"
    }
    if ($steps) { $procHtml = "<div class=`"process-steps`"><h3>Production Process</h3>$steps</div>" }
  }

  # details section
  $details = ''
  if ($specsHtml -or $procHtml) {
    $details = '<section class="p-details"><h2>Technical Specifications</h2>' + $specsHtml + $procHtml + '</section>'
  }

  # JSON-LD
  $imagesJson = @($imgList | ForEach-Object { 'https://www.yominelectric.com' + $_ })
  $jsonld = @{
    '@context' = 'https://schema.org'
    '@type' = 'Product'
    name = $p.title
    sku = $p.id
    mpn = $p.id
    brand = @{ '@type' = 'Brand'; name = 'Yomin Electric' }
    category = $p.category
    description = $p.description
    image = $imagesJson
    url = $canon
    hasMerchantReturnPolicy = @{
      '@type' = 'MerchantReturnPolicy'
      applicableCountry = '*'
      returnPolicyCategory = 'https://schema.org/MerchantReturnFiniteReturnWindow'
      merchantReturnDays = 30
      returnMethod = 'https://schema.org/ReturnByMail'
      returnFees = 'https://schema.org/FreeReturn'
    }
    shippingDetails = @{
      '@type' = 'OfferShippingDetails'
      shippingRate = @{ '@type' = 'MonetaryAmount'; value = 0; currency = 'USD' }
      shippingDestination = @{ '@type' = 'DefinedRegion'; addressCountry = '*' }
      deliveryTime = @{
        '@type' = 'ShippingDeliveryTime'
        handlingTime = @{ '@type' = 'QuantitativeValue'; minValue = 1; maxValue = 3; unitCode = 'DAY' }
        transitTime = @{ '@type' = 'QuantitativeValue'; minValue = 15; maxValue = 25; unitCode = 'DAY' }
      }
    }
  } | ConvertTo-Json -Depth 8 -Compress
  $bread = @{
    '@context' = 'https://schema.org'
    '@type' = 'BreadcrumbList'
    itemListElement = @(
      @{ '@type' = 'ListItem'; position = 1; name = 'Home'; item = 'https://www.yominelectric.com/' }
      @{ '@type' = 'ListItem'; position = 2; name = 'Products'; item = 'https://www.yominelectric.com/products' }
      @{ '@type' = 'ListItem'; position = 3; name = $p.category; item = 'https://www.yominelectric.com/products?category=' + $catSlug }
      @{ '@type' = 'ListItem'; position = 4; name = $p.title; item = $canon }
    )
  } | ConvertTo-Json -Depth 6 -Compress
  $jsonldHtml = '<script type="application/ld+json">' + $jsonld + '</script>' + "`n" + '<script type="application/ld+json">' + $bread + '</script>'

  $quoteParam = UrlEnc $p.title
  $waText = UrlEnc ("Hello, I am interested in " + $p.title)
  $waLink = 'https://wa.me/8619016543301?text=' + $waText
  $catLink = '/products?category=' + $catSlug

  $html = $head
  $html = $html.Replace('@TITLE@', $title)
  $html = $html.Replace('@DESC@', $descMeta)
  $html = $html.Replace('@CANON@', $canon)
  $html = $html.Replace('@OGIMG@', $ogimg)
  $html = $html.Replace('@JSONLD@', $jsonldHtml)
  $html = $html.Replace('@CATNAME@', (Esc $p.category))
  $html = $html.Replace('@CATLINK@', $catLink)
  $html = $html.Replace('@IMG0@', (Esc $img0))
  $html = $html.Replace('@ALTDESC@', $alts)
  $html = $html.Replace('@THUMBS@', $thumbs)
  $html = $html.Replace('@DESCHTML@', $descHtml)
  $html = $html.Replace('@QUOTEPARAM@', $quoteParam)
  $html = $html.Replace('@WALINK@', $waLink)
  $html = $html.Replace('@KEYWORDS@', $kw)
  $html = $html.Replace('@DATASHEET@', $ds)
  $html = $html.Replace('@DETAILS@', $details)

  $dir = Join-Path $outBase $catSlug
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  [System.IO.File]::WriteAllText((Join-Path $dir ($slug + '.html')), $html, (New-Object System.Text.UTF8Encoding $false))
  $count++
}
Write-Output "Generated $count product pages"
