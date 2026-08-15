'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['fr'] = {
    'browse_cat': 'Par Catégorie',
    'view_all': 'Voir tout',
    'inquiry_price': 'Demander un Prix',
    'request_quote': 'Demander un Devis',
    'whatsapp': 'WhatsApp',
    'more_in': 'Plus dans',
    'applications': 'Applications',
    'why_yomin': 'Pourquoi Choisir Yomin Electric',
    'tech_specs': 'Caractéristiques Techniques',
    'key_features': 'Caractéristiques Clés',
    'worldwide_ship': 'Livraison Mondiale',
    'ship_time': '15–25 jours ouvrés',
    'ship_countries': '95+ pays desservis',
    'ship_free_consult': 'Consultation gratuite',
    'ship_returns': 'Retour sous 30 jours',
    'min_order': 'Commande Min.:',
    'products': 'Produits',
    'all_products': 'Tous les Produits',
    'yomin_tagline': 'Produits électriques d&#x27;usine — approuvés dans 95+ pays',
    'certified': 'Certifié ISO 9001 &amp; CE',
    'oem_odm': 'OEM / ODM Disponible',
    'factory_direct': 'Direct Usine',
    'prev': 'Préc',
    'next': 'Suiv',
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
