/** Canonical URL enforcement and legacy redirects for products page */

/* Stale category paths -> canonical (products moved categories during catalog rework) */
const PRODUCT_REDIRECTS = {
  "/products/current-transformer/factory-price-msq-85-type-single-phase-10kv-input-voltages-measuring-electricity-monitoring-autotransformer-cu": "/products/variac-transformer/factory-price-msq-85-type-single-phase-10kv-input-voltages-measuring-electricity-monitoring-autotransformer-cu",
  "/products/current-transformer/high-precision-mes-104-80-series-1250-5-single-phase-copper-electric-transformers-autotransformer-current-tran": "/products/variac-transformer/high-precision-mes-104-80-series-1250-5-single-phase-copper-electric-transformers-autotransformer-current-tran",
  "/products/current-transformer/mes-62-30-series-150-5-11kv-output-3kv-input-voltage-single-phase-low-voltage-toroidal-autotransformer-current": "/products/variac-transformer/mes-62-30-series-150-5-11kv-output-3kv-input-voltage-single-phase-low-voltage-toroidal-autotransformer-current",
  "/products/current-transformer/single-phase-ce-current-transformer-cp-62-30-toroidal-autotransformer-for-metering-50-5a-class-0-5-1-frequency": "/products/variac-transformer/single-phase-ce-current-transformer-cp-62-30-toroidal-autotransformer-for-metering-50-5a-class-0-5-1-frequency",
  "/products/current-transformer/tdgc2-5kva-single-phase-adjustable-manual-toroidal-variac-transformer-0-250ac-output-220v-avr-230v-nominal-vol": "/products/variac-transformer/tdgc2-5kva-single-phase-adjustable-manual-toroidal-variac-transformer-0-250ac-output-220v-avr-230v-nominal-vol",
  "/products/energy-meter/certified-new-energy-system-t2-2p-pv-1000v-rated-voltage-40ka-max-current-capacity-3p-solar-surge-protector": "/products/fuse-protection/certified-new-energy-system-t2-2p-pv-1000v-rated-voltage-40ka-max-current-capacity-3p-solar-surge-protector",
  "/products/energy-meter/high-quality-adjustable-over-under-voltage-protector-single-phase-electric-power-protector-made-of-pc-dc-curre": "/products/fuse-protection/high-quality-adjustable-over-under-voltage-protector-single-phase-electric-power-protector-made-of-pc-dc-curre",
  "/products/energy-meter/high-quality-dc-single-phase-voltage-protector-adjustable-over-under-electric-power-voltage-protector": "/products/fuse-protection/high-quality-dc-single-phase-voltage-protector-adjustable-over-under-electric-power-voltage-protector",
  "/products/energy-meter/single-phase-63a-voltage-protector-wifi-access-230v-dc-power-supply-220v-output-electric-digital-over-under-vo": "/products/fuse-protection/single-phase-63a-voltage-protector-wifi-access-230v-dc-power-supply-220v-output-electric-digital-over-under-vo",
  "/products/energy-meter/wifi-remote-control-switch-energy-meter-circuit-breaker-timer-digital-current-and-leakage-protection-voltage-p": "/products/fuse-protection/wifi-remote-control-switch-energy-meter-circuit-breaker-timer-digital-current-and-leakage-protection-voltage-p",
  "/products/other/1-5mm-3000pcs-spacer-clips-tile-leveling-clips-leveling-system-tiles": "/products/tools-hardware/1-5mm-3000pcs-spacer-clips-tile-leveling-clips-leveling-system-tiles",
  "/products/other/1-5mm-floor-wall-tile-leveling-system-tile-spacer-clips-wedges-tile-leveling-system-for-ceramic-tile-and-stone": "/products/tools-hardware/1-5mm-floor-wall-tile-leveling-system-tile-spacer-clips-wedges-tile-leveling-system-for-ceramic-tile-and-stone",
  "/products/other/1mm-1-5mm-2mm-2-5mm-3mm-modern-pvc-colored-and-perforated-tile-leveling-clips-and-wedges-system-accessory-tile": "/products/tools-hardware/1mm-1-5mm-2mm-2-5mm-3mm-modern-pvc-colored-and-perforated-tile-leveling-clips-and-wedges-system-accessory-tile",
  "/products/other/24-17mm-lippage-spacer-adjustment-tile-accessories-flat-floor-wall-tile-spacer-1-5mm-leveling-system-tile-leve": "/products/tools-hardware/24-17mm-lippage-spacer-adjustment-tile-accessories-flat-floor-wall-tile-spacer-1-5mm-leveling-system-tile-leve",
  "/products/other/china-supplier-modern-ceramic-tile-leveling-system-floor-tile-spacer-leveling-clips-for-apartment-use-with-pvc": "/products/tools-hardware/china-supplier-modern-ceramic-tile-leveling-system-floor-tile-spacer-leveling-clips-for-apartment-use-with-pvc",
  "/products/other/customizable-pvc-pe-tile-leveling-system-imperforate-floor-price-tiles-spacer-clips-and-wedges-for-porcelain": "/products/tools-hardware/customizable-pvc-pe-tile-leveling-system-imperforate-floor-price-tiles-spacer-clips-and-wedges-for-porcelain",
  "/products/other/factory-direct-supply-0-5-2mm-tile-leveling-system-clips-accessories-positioner-tile-spacer-base-plastic-level": "/products/tools-hardware/factory-direct-supply-0-5-2mm-tile-leveling-system-clips-accessories-positioner-tile-spacer-base-plastic-level",
  "/products/other/high-quality-modern-design-cross-tile-spacer-manufacturer-plastic-tilec-leveling-system-spacer-for-tiling-inst": "/products/tools-hardware/high-quality-modern-design-cross-tile-spacer-manufacturer-plastic-tilec-leveling-system-spacer-for-tiling-inst",
  "/products/other/high-quality-pvc-tile-leveling-system-modern-design-tile-spacer-clips-on-sale": "/products/tools-hardware/high-quality-pvc-tile-leveling-system-modern-design-tile-spacer-clips-on-sale",
  "/products/other/modern-design-automatic-clip-reusable-pvc-plastic-material-leveling-system-modern-design-ceramic-tiles-spacer-": "/products/tools-hardware/modern-design-automatic-clip-reusable-pvc-plastic-material-leveling-system-modern-design-ceramic-tiles-spacer-",
  "/products/other/modern-design-pvc-pe-tile-leveling-system-clips-thin-hollow-spacer-tiles-for-porcelain-floors-for-hotel-use-ti": "/products/tools-hardware/modern-design-pvc-pe-tile-leveling-system-clips-thin-hollow-spacer-tiles-for-porcelain-floors-for-hotel-use-ti",
  "/products/other/modern-design-thin-spacer-clips-high-quality-pe-pvc-and-ceramic-floor-tile-leveling-system-accessories": "/products/tools-hardware/modern-design-thin-spacer-clips-high-quality-pe-pvc-and-ceramic-floor-tile-leveling-system-accessories",
  "/products/other/modern-pvc-colored-and-perforated-tile-leveling-clips-spacer-tile-wedges-system-accessory-for-porcelain-floors": "/products/tools-hardware/modern-pvc-colored-and-perforated-tile-leveling-clips-spacer-tile-wedges-system-accessory-for-porcelain-floors",
  "/products/other/modern-pvc-tile-leveling-system-clips-and-wedges-tile-accessories": "/products/tools-hardware/modern-pvc-tile-leveling-system-clips-and-wedges-tile-accessories",
  "/products/other/modern-pvc-tile-leveling-system-clips-base-for-15-22mm-ceramic-thickness": "/products/tools-hardware/modern-pvc-tile-leveling-system-clips-base-for-15-22mm-ceramic-thickness",
  "/products/other/modern-pvc-tile-leveling-system-decking-spacer-leveler-for-ceramic-tiles-3mm-spacers": "/products/tools-hardware/modern-pvc-tile-leveling-system-decking-spacer-leveler-for-ceramic-tiles-3mm-spacers",
  "/products/other/modern-pvc-tile-leveling-system-imperforate-floor-price-tiles-spacer-clips-and-wedges": "/products/tools-hardware/modern-pvc-tile-leveling-system-imperforate-floor-price-tiles-spacer-clips-and-wedges",
  "/products/other/plastic-bases-level-wedges-spacers-pvc-tile-leveling-system-1mm-1-5mm-thickness-exterior-floor-tiles-ceramic-t": "/products/tools-hardware/plastic-bases-level-wedges-spacers-pvc-tile-leveling-system-1mm-1-5mm-thickness-exterior-floor-tiles-ceramic-t",
  "/products/other/professional-1-5mm-gap-tile-leveling-system-clips-and-wedges-ceramic-tile-spacers-leveling-system-wedges-tile-": "/products/tools-hardware/professional-1-5mm-gap-tile-leveling-system-clips-and-wedges-ceramic-tile-spacers-leveling-system-wedges-tile-",
  "/products/other/professional-plastic-pvc-pe-floor-wall-tile-level-clips-spacers-flat-leveling-system-spacer-accessories-tile-l": "/products/tools-hardware/professional-plastic-pvc-pe-floor-wall-tile-level-clips-spacers-flat-leveling-system-spacer-accessories-tile-l",
  "/products/other/tile-leveling-system-clips-and-wedges-modern-design-thin-spacer-clips-pe-pvc-and-ceramic-floor-accessories-til": "/products/tools-hardware/tile-leveling-system-clips-and-wedges-modern-design-thin-spacer-clips-pe-pvc-and-ceramic-floor-accessories-til",
  "/products/other/wholesale-plastic-tile-spacer-tile-leveling-system-clips-and-wedges-plier-tile-leveler-systems-spacers-accesso": "/products/tools-hardware/wholesale-plastic-tile-spacer-tile-leveling-system-clips-and-wedges-plier-tile-leveler-systems-spacers-accesso",
  "/products/solar-pv-products/t2-2p-pv-solar-surge-protector-1000v-rated-voltage-40ka-max-current-capacity-3p-solar-protector-tuv-certified-": "/products/fuse-protection/t2-2p-pv-solar-surge-protector-1000v-rated-voltage-40ka-max-current-capacity-3p-solar-protector-tuv-certified-",
  "/products/voltage-stabilizer-regulator/50-pieces-t-shape-tile-locator-height-regulator-spacers-porcelain-reusable-anti-lippage-tile-leveling-system": "/products/tools-hardware/50-pieces-t-shape-tile-locator-height-regulator-spacers-porcelain-reusable-anti-lippage-tile-leveling-system",
};

/* Empty placeholder categories removed from nav/sitemap until they have products */
const CATEGORY_REDIRECTS = {
  '/products/flexible-busbar': '/products',
  '/products/voltage-protector': '/products',
};

export default function middleware(request) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/$/, '') || '/';

  /* Legacy category-path redirects (stale duplicates -> canonical) */
  const redirectTarget = PRODUCT_REDIRECTS[path];
  if (redirectTarget) {
    return Response.redirect(new URL(redirectTarget, url.origin), 301);
  }

  /* Removed empty categories -> products index */
  const catTarget = CATEGORY_REDIRECTS[path];
  if (catTarget) {
    return Response.redirect(new URL(catTarget, url.origin), 301);
  }

  /* Redirect /products.html and /product.html to /products */
  if (path === '/products.html' || path === '/product.html') {
    const target = new URL('/products', url.origin);
    url.searchParams.forEach((v, k) => target.searchParams.set(k, v));
    if (target.search !== url.search || target.pathname !== path) {
      return Response.redirect(target.href, 301);
    }
  }

  /* Normalize trailing /products/ to /products */
  if (url.pathname === '/products/') {
    const target = new URL('/products', url.origin);
    url.searchParams.forEach((v, k) => target.searchParams.set(k, v));
    return Response.redirect(target.href, 301);
  }

  return;
}

export const config = {
  matcher: ['/products', '/products.html', '/product', '/product.html', '/products/', '/products/:path*'],
};
