'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['es'] = {
    'browse_cat': 'Por Categoría',
    'view_all': 'Ver todo',
    'inquiry_price': 'Consultar Precio',
    'request_quote': 'Solicitar Cotización',
    'whatsapp': 'WhatsApp',
    'more_in': 'Más en',
    'applications': 'Aplicaciones',
    'why_yomin': 'Por Qué Elegir Yomin Electric',
    'tech_specs': 'Especificaciones Técnicas',
    'key_features': 'Características Clave',
    'worldwide_ship': 'Envío Mundial',
    'ship_time': '15–25 días hábiles',
    'ship_countries': '95+ países atendidos',
    'ship_free_consult': 'Consulta gratuita de envío',
    'ship_returns': 'Política de 30 días',
    'min_order': 'Pedido Mín.:',
    'products': 'Productos',
    'all_products': 'Todos los Productos',
    'yomin_tagline': 'Productos eléctricos de fábrica — en más de 95 países',
    'certified': 'Certificado ISO 9001 &amp; CE',
    'oem_odm': 'OEM / ODM Disponible',
    'factory_direct': 'Directo de Fábrica',
    'prev': 'Ant',
    'next': 'Sig',
    'cat_screw-machine': 'Screw Machines',
    'cat_energy-meter': 'Energy Meters',
    'cat_current-transformer': 'Current Transformers',
    'cat_voltage-stabilizer-regulator': 'Voltage Stabilizers',
    'cat_variac-transformer': 'Variac Transformers',
    'cat_terminal-connector': 'Terminals &amp; Connectors',
    'cat_fuse-protection': 'Fuses &amp; Protection',
    'cat_socket-wiring': 'Sockets &amp; Wiring',
    'cat_solar-pv-products': 'Solar &amp; PV Products',
    'cat_tools-hardware': 'Tools &amp; Hardware',
    'cat_aluminum-busbar': 'Aluminum Busbars',
    'cat_flexible-busbar': 'Flexible Busbars',
    'cat_security-seal': 'Security Seals',
    'cat_other': 'Other Products'
};
// Apply translations on DOMContentLoaded
(function(){
  function applyLang(l){
    var d=window.__ymPagesI18n&&window.__ymPagesI18n[l];
    if(!d)return;
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k=el.getAttribute('data-i18n');
      if(d[k])el.textContent=d[k];
    });
    // RTL
    if(l==='ar'){document.documentElement.setAttribute('dir','rtl');}
    else{document.documentElement.removeAttribute('dir');}
  }
  var stored=localStorage.getItem('ym_lang');
  if(stored&&stored!=='en'){
    if(typeof T!=='undefined'&&T[stored]){
      // product titles handled by main i18n
    }
    applyLang(stored);
  }
  document.addEventListener('langChanged',function(e){applyLang(e.detail);});
})();
