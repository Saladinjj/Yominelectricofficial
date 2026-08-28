'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['es'] = {
    'browse_cat': 'Explorar por Categoría',
    'view_all': 'Ver todo',
    'all_products': 'Todos los Productos',
    'products': 'Productos',
    'home': 'Inicio',
    'prev': '← Anterior',
    'next': 'Siguiente →',
    'page': 'Página',
    'inquiry_price': 'Consultar Precio',
    'min_order': 'Pedido mín.:',
    'products_count': 'productos',
    'request_quote': 'Solicitar Cotización',
    'whatsapp': 'WhatsApp',
    'more_in_cat': 'Más en esta categoría',
    'tech_specs': 'Especificaciones Técnicas',
    'key_features': 'Características Principales',
    'applications': 'Aplicaciones',
    'why_yomin': 'Por Qué Elegir Yomin Electric',
    'worldwide_ship': '🌍 Envío Mundial',
    'ship_time': '15 a 25 días hábiles',
    'ship_countries': 'Envío a más de 95 países',
    'ship_packaging': 'Embalaje de exportación seguro',
    'ship_returns': 'Devolución en 30 días',
    'ship_free_consult': 'Consulta de envío gratuita',
    'ship_incoterms': 'DDP / FOB / CIF disponibles',
    'certified': 'Certificado ISO 9001 & CE',
    'factory_direct': 'Directo de Fábrica',
    'oem_odm': 'OEM / ODM Disponible',
    'since_1996': 'Desde 1996',
    '95_countries': '95+ Países',
    'ship_freight': 'Flete marítimo y aéreo',
    'ship_global': 'Distribución global',
    'ship_cartons': 'Cajas de exportación',
    'ship_guarantee': 'Garantía de calidad',
    'ship_contact': 'Contacte nuestro equipo',
    'ship_incoterms_sub': 'Todos los Incoterms disponibles',
    'app_residential': 'Instalaciones residenciales y comerciales',
    'app_industrial': 'Sistemas de energía industrial',
    'app_energy_mon': 'Monitoreo y gestión de energía',
    'app_oem': 'Producción OEM / ODM',
    'app_export': 'Proyectos de exportación y servicios públicos',
    'why_iso': 'Fabricación certificada ISO 9001 & CE',
    'why_pricing': 'Precios competitivos directos de fábrica',
    'why_oem': 'Soporte completo de personalización OEM/ODM',
    'why_qc': 'Control de calidad estricto — cada unidad probada antes del envío',
    'why_logistics': 'Logística de exportación rápida a más de 95 países',
    'why_support': 'Equipo de soporte técnico receptivo',
    'yomin_tagline': 'Productos eléctricos de fábrica — confiados en más de 95 países',
    'why_body': 'Zhejiang Yomin Electric Co., Ltd. fabrica productos eléctricos de precisión desde 1996, con la confianza de compradores en más de 95 países. Cada unidad se prueba antes del envío.',
    'cat_screw-machine': 'Máquinas de Tornillos',
    'cat_energy-meter': 'Contadores de Energía',
    'cat_current-transformer': 'Transformadores de Corriente',
    'cat_voltage-stabilizer-regulator': 'Estabilizadores de Tensión',
    'cat_variac-transformer': 'Transformadores Variac',
    'cat_terminal-connector': 'Terminales & Conectores',
    'cat_fuse-protection': 'Fusibles & Protección',
    'cat_socket-wiring': 'Enchufes & Cableado',
    'cat_solar-pv-products': 'Productos Solares y FV',
    'cat_tools-hardware': 'Herramientas & Hardware',
    'cat_aluminum-busbar': 'Barras de Bus de Aluminio',
    'cat_flexible-busbar': 'Barras de Bus Flexibles',
    'cat_security-seal': 'Sellos de Seguridad',
    'cat_other': 'Otros Productos'
};
(function(){
  function applyLang(l){
    var d = window.__ymPagesI18n && window.__ymPagesI18n[l];
    if (!d) return;
    /* Static UI strings */
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k = el.getAttribute('data-i18n');
      if (d[k] !== undefined) el.textContent = d[k];
    });
    /* Product titles in cards, breadcrumbs, and h1 (data-pid attribute) */
    if (typeof T !== 'undefined' && T[l]) {
      document.querySelectorAll('[data-pid]').forEach(function(el){
        var pid = el.getAttribute('data-pid');
        if (T[l][pid]) el.textContent = T[l][pid];
      });
    }
    /* Category sidebar labels */
    document.querySelectorAll('[data-i18n^="cat_"]').forEach(function(el){
      var k = el.getAttribute('data-i18n');
      if (d[k]) el.textContent = d[k];
    });
    /* RTL for Arabic */
    if (l === 'ar') {
      document.documentElement.setAttribute('dir', 'rtl');
      document.documentElement.setAttribute('lang', 'ar');
    } else {
      document.documentElement.removeAttribute('dir');
      document.documentElement.setAttribute('lang', l === 'fr' ? 'fr' : l === 'es' ? 'es' : 'en');
    }
  }
  /* Apply on load if language already set */
  function applyStored() {
    var stored = localStorage.getItem('ym_lang') || window.ymLang;
    if (stored && stored !== 'en') applyLang(stored);
  }
  /* Apply immediately */
  applyStored();
  /* Apply after DOM fully loaded */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyStored);
  }
  /* Re-apply whenever user switches language */
  document.addEventListener('langChanged', function(e) { applyLang(e.detail); });
  window.addEventListener('langChanged', function(e) { applyLang(e.detail); });
  /* Also watch storage changes (multi-tab) */
  window.addEventListener('storage', function(e) {
    if (e.key === 'ym_lang' && e.newValue && e.newValue !== 'en') applyLang(e.newValue);
  });
  /* Retry after main.js sets window.ymLang */
  window.addEventListener('load', applyStored);
})();
