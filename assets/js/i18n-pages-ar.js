'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['ar'] = {
    'browse_cat': 'تصفح حسب الفئة',
    'view_all': 'عرض الكل',
    'inquiry_price': 'استفسر عن السعر',
    'request_quote': 'طلب عرض سعر',
    'whatsapp': 'واتساب',
    'more_in': 'المزيد في',
    'applications': 'التطبيقات',
    'why_yomin': 'لماذا تختار Yomin Electric',
    'tech_specs': 'المواصفات الفنية',
    'key_features': 'الميزات الرئيسية',
    'worldwide_ship': 'شحن عالمي',
    'ship_time': '15-25 يوم عمل',
    'ship_countries': 'أكثر من 95 دولة',
    'ship_free_consult': 'استشارة شحن مجانية',
    'ship_returns': 'سياسة إرجاع 30 يومًا',
    'min_order': 'الحد الأدنى للطلب:',
    'products': 'منتجات',
    'all_products': 'جميع المنتجات',
    'yomin_tagline': 'منتجات كهربائية مباشرة من المصنع — موثوق في أكثر من 95 دولة',
    'certified': 'معتمد ISO 9001 &amp; CE',
    'oem_odm': 'OEM / ODM متاح',
    'factory_direct': 'مباشر من المصنع',
    'prev': 'السابق',
    'next': 'التالي',
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
