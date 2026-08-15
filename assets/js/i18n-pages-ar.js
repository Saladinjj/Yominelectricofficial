'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['ar'] = {
    'browse_cat': 'تصفح حسب الفئة',
    'view_all': 'عرض الكل',
    'all_products': 'جميع المنتجات',
    'products': 'المنتجات',
    'home': 'الرئيسية',
    'prev': 'السابق ←',
    'next': '→ التالي',
    'page': 'صفحة',
    'inquiry_price': 'استفسر عن السعر',
    'min_order': 'الحد الأدنى للطلب:',
    'products_count': 'منتجات',
    'request_quote': 'طلب عرض سعر',
    'whatsapp': 'واتساب',
    'more_in_cat': 'المزيد في هذه الفئة',
    'tech_specs': 'المواصفات الفنية',
    'key_features': 'الميزات الرئيسية',
    'applications': 'التطبيقات',
    'why_yomin': 'لماذا تختار Yomin Electric',
    'worldwide_ship': '🌍 شحن عالمي',
    'ship_time': '١٥–٢٥ يوم عمل',
    'ship_countries': 'خدمة أكثر من 95 دولة',
    'ship_packaging': 'تغليف تصدير آمن',
    'ship_returns': 'سياسة إرجاع 30 يوماً',
    'ship_free_consult': 'استشارة شحن مجانية',
    'ship_incoterms': 'DDP / FOB / CIF متاح',
    'certified': 'معتمد ISO 9001 & CE',
    'factory_direct': 'مباشر من المصنع',
    'oem_odm': 'OEM / ODM متاح',
    'since_1996': 'منذ 1996',
    '95_countries': '٩٥+ دولة',
    'yomin_tagline': 'منتجات كهربائية مباشرة من المصنع — موثوق بها في أكثر من 95 دولة',
    'why_body': 'تصنع شركة Zhejiang Yomin Electric Co., Ltd. منتجات كهربائية دقيقة منذ عام 1996، وتحظى بثقة المشترين في أكثر من 95 دولة. يتم اختبار كل وحدة قبل الشحن.',
    'cat_screw-machine': 'ماكينات البراغي',
    'cat_energy-meter': 'عدادات الطاقة',
    'cat_current-transformer': 'محولات التيار',
    'cat_voltage-stabilizer-regulator': 'منظمات الجهد',
    'cat_variac-transformer': 'محولات فاريك',
    'cat_terminal-connector': 'طرفيات وموصلات',
    'cat_fuse-protection': 'المنصهرات والحماية',
    'cat_socket-wiring': 'مقابس وأسلاك',
    'cat_solar-pv-products': 'منتجات الطاقة الشمسية',
    'cat_tools-hardware': 'أدوات ومعدات',
    'cat_aluminum-busbar': 'قضبان الألومنيوم',
    'cat_flexible-busbar': 'قضبان مرنة',
    'cat_security-seal': 'أختام الأمان',
    'cat_other': 'منتجات أخرى'
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
    /* Product titles in cards (data-pid attribute) */
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
  var stored = localStorage.getItem('ym_lang');
  if (stored && stored !== 'en') applyLang(stored);
  /* Re-apply whenever user switches language */
  document.addEventListener('langChanged', function(e) { applyLang(e.detail); });
  /* Also watch storage changes (multi-tab) */
  window.addEventListener('storage', function(e) {
    if (e.key === 'ym_lang' && e.newValue && e.newValue !== 'en') applyLang(e.newValue);
  });
})();
