'use strict';
if (typeof window.__ymPagesI18n === 'undefined') window.__ymPagesI18n = {};
window.__ymPagesI18n['fr'] = {
    'browse_cat': 'Parcourir par Catégorie',
    'view_all': 'Voir tout',
    'all_products': 'Tous les Produits',
    'products': 'Produits',
    'home': 'Accueil',
    'prev': '← Précédent',
    'next': 'Suivant →',
    'page': 'Page',
    'inquiry_price': 'Demander un Prix',
    'min_order': 'Commande min. :',
    'products_count': 'produits',
    'request_quote': 'Demander un Devis',
    'whatsapp': 'WhatsApp',
    'more_in_cat': 'Plus dans cette catégorie',
    'tech_specs': 'Caractéristiques Techniques',
    'key_features': 'Caractéristiques Principales',
    'applications': 'Applications',
    'why_yomin': 'Pourquoi Choisir Yomin Electric',
    'worldwide_ship': '🌍 Livraison Mondiale',
    'ship_time': '15 à 25 jours ouvrés',
    'ship_countries': 'Livraison dans 95+ pays',
    'ship_packaging': 'Emballage export sécurisé',
    'ship_returns': 'Retour sous 30 jours',
    'ship_free_consult': 'Conseil d\'expédition gratuit',
    'ship_incoterms': 'DDP / FOB / CIF disponibles',
    'certified': 'Certifié ISO 9001 & CE',
    'factory_direct': 'Direct Usine',
    'oem_odm': 'OEM / ODM Disponible',
    'since_1996': 'Depuis 1996',
    '95_countries': '95+ Pays',
    'ship_freight': 'Fret maritime et aérien',
    'ship_global': 'Distribution mondiale',
    'ship_cartons': 'Cartons d\'exportation',
    'ship_guarantee': 'Garantie de qualité',
    'ship_contact': 'Contactez notre équipe',
    'ship_incoterms_sub': 'Tous les Incoterms disponibles',
    'app_residential': 'Installations résidentielles et commerciales',
    'app_industrial': 'Systèmes d\'alimentation industriels',
    'app_energy_mon': 'Surveillance et gestion de l\'énergie',
    'app_oem': 'Production OEM / ODM',
    'app_export': 'Projets d\'exportation et d\'utilité',
    'why_iso': 'Fabrication certifiée ISO 9001 & CE',
    'why_pricing': 'Tarification compétitive directe usine',
    'why_oem': 'Support complet de personnalisation OEM/ODM',
    'why_qc': 'Contrôle qualité strict — chaque unité testée avant expédition',
    'why_logistics': 'Logistique d\'exportation rapide vers 95+ pays',
    'why_support': 'Équipe de support technique réactive',
    'yomin_tagline': 'Produits électriques d\'usine — approuvés dans plus de 95 pays',
    'why_body': 'Zhejiang Yomin Electric Co., Ltd. fabrique des produits électriques de précision depuis 1996, reconnus par les acheteurs dans plus de 95 pays. Chaque unité est testée avant expédition.',
    'cat_screw-machine': 'Machines à Vis',
    'cat_energy-meter': 'Compteurs d\'Énergie',
    'cat_current-transformer': 'Transformateurs de Courant',
    'cat_voltage-stabilizer-regulator': 'Stabilisateurs de Tension',
    'cat_variac-transformer': 'Transformateurs Variac',
    'cat_terminal-connector': 'Bornes & Connecteurs',
    'cat_fuse-protection': 'Fusibles & Protection',
    'cat_socket-wiring': 'Prises & Câblage',
    'cat_solar-pv-products': 'Produits Solaires & PV',
    'cat_tools-hardware': 'Outils & Quincaillerie',
    'cat_aluminum-busbar': 'Barres de Bus en Aluminium',
    'cat_flexible-busbar': 'Barres de Bus Flexibles',
    'cat_security-seal': 'Joints de Sécurité',
    'cat_other': 'Autres Produits'
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
  var stored = localStorage.getItem('ym_lang');
  if (stored && stored !== 'en') applyLang(stored);
  /* Re-apply whenever user switches language */
  document.addEventListener('langChanged', function(e) { applyLang(e.detail); });
  /* Also watch storage changes (multi-tab) */
  window.addEventListener('storage', function(e) {
    if (e.key === 'ym_lang' && e.newValue && e.newValue !== 'en') applyLang(e.newValue);
  });
})();
