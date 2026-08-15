/* i18n-global.js — full translation system for all pages
 * Sets window.__ymT (nav + product page keys) and exposes window.sL alias.
 * Loaded on every product/category page.
 */
(function() {
  // Merge product-page specific keys into window.__ymT
  var PKG = {
  en: {
  "certified": "ISO 9001 & CE Certified",
  "factory_direct": "Factory Direct",
  "oem_odm": "OEM / ODM Available",
  "95_countries": "95+ Countries",
  "since_1996": "Since 1996",
  "home": "Home",
  "all_products": "All Products",
  "nav_quote": "Get a Quote",
  "request_quote": "Request a Quote",
  "whatsapp": "WhatsApp",
  "more_in_cat": "More in this category",
  "min_order": "Min. Order:",
  "worldwide_ship": "\ud83c\udf0d Worldwide Shipping",
  "tech_specs": "Technical Specifications",
  "key_features": "Key Features",
  "applications": "Applications",
  "why_yomin": "Why Choose Yomin Electric",
  "why_body": "Zhejiang Yomin Electric Co., Ltd. is a factory-direct manufacturer of precision electrical products since 1996, trusted by buyers in 95+ countries. Every unit is tested before shipping.",
  "ship_time": "15\u201325 business days",
  "ship_countries": "95+ countries served",
  "ship_packaging": "Secure export packaging",
  "ship_returns": "30-day return policy",
  "ship_free_consult": "Free shipping consultation",
  "ship_incoterms": "DDP / FOB / CIF available",
  "ship_freight": "Sea & Air freight",
  "ship_global": "Global distribution",
  "ship_cartons": "Export-grade cartons",
  "ship_guarantee": "Quality guarantee",
  "ship_contact": "Contact our team",
  "ship_incoterms_sub": "All Incoterms available",
  "app_residential": "Residential & commercial installations",
  "app_industrial": "Industrial power systems",
  "app_energy_mon": "Energy monitoring & management",
  "app_oem": "OEM / ODM production",
  "app_export": "Export & utility projects",
  "why_iso": "ISO 9001 & CE certified manufacturing",
  "why_pricing": "Factory-direct competitive pricing",
  "why_oem": "Full OEM / ODM customization support",
  "why_qc": "Strict QC \u2014 every unit tested before shipment",
  "why_logistics": "Fast export logistics to 95+ countries",
  "why_support": "Responsive technical support team",
  "cat_screw-machine": "Screw Machines",
  "cat_energy-meter": "Energy Meters",
  "cat_current-transformer": "Current Transformers",
  "cat_voltage-stabilizer-regulator": "Voltage Stabilizers",
  "cat_variac-transformer": "Variac Transformers",
  "cat_terminal-connector": "Terminals & Connectors",
  "cat_fuse-protection": "Fuses & Protection",
  "cat_socket-wiring": "Sockets & Wiring",
  "cat_solar-pv-products": "Solar & PV Products",
  "cat_tools-hardware": "Tools & Hardware",
  "cat_aluminum-busbar": "Aluminum Busbars",
  "cat_flexible-busbar": "Flexible Busbars",
  "cat_security-seal": "Security Seals",
  "cat_other": "Other Products",
  "browse_cat": "Browse by Category",
  "view_all": "View all",
  "inquiry_price": "Inquire for Price",
  "products_count": "products",
  "yomin_tagline": "Factory-direct electrical products \u2014 trusted in 95+ countries"
  },
  fr: {
  "certified": "Certifi\u00e9 ISO 9001 & CE",
  "factory_direct": "Direct Usine",
  "oem_odm": "OEM / ODM Disponible",
  "95_countries": "95+ Pays",
  "since_1996": "Depuis 1996",
  "home": "Accueil",
  "all_products": "Tous les Produits",
  "nav_quote": "Obtenir un Devis",
  "request_quote": "Demander un Devis",
  "whatsapp": "WhatsApp",
  "more_in_cat": "Plus dans cette cat\u00e9gorie",
  "min_order": "Commande min.:",
  "worldwide_ship": "\ud83c\udf0d Livraison Mondiale",
  "tech_specs": "Caract\u00e9ristiques Techniques",
  "key_features": "Caract\u00e9ristiques Principales",
  "applications": "Applications",
  "why_yomin": "Pourquoi Choisir Yomin Electric",
  "why_body": "Zhejiang Yomin Electric Co., Ltd. est un fabricant direct d'usine de produits \u00e9lectriques de pr\u00e9cision depuis 1996, reconnu par les acheteurs dans plus de 95 pays. Chaque unit\u00e9 est test\u00e9e avant exp\u00e9dition.",
  "ship_time": "15 \u00e0 25 jours ouvr\u00e9s",
  "ship_countries": "Livraison dans 95+ pays",
  "ship_packaging": "Emballage export s\u00e9curis\u00e9",
  "ship_returns": "Retour sous 30 jours",
  "ship_free_consult": "Conseil d'exp\u00e9dition gratuit",
  "ship_incoterms": "DDP / FOB / CIF disponibles",
  "ship_freight": "Fret maritime et a\u00e9rien",
  "ship_global": "Distribution mondiale",
  "ship_cartons": "Cartons d'exportation",
  "ship_guarantee": "Garantie de qualit\u00e9",
  "ship_contact": "Contactez notre \u00e9quipe",
  "ship_incoterms_sub": "Tous les Incoterms disponibles",
  "app_residential": "Installations r\u00e9sidentielles et commerciales",
  "app_industrial": "Syst\u00e8mes d'alimentation industriels",
  "app_energy_mon": "Surveillance et gestion de l'\u00e9nergie",
  "app_oem": "Production OEM / ODM",
  "app_export": "Projets d'exportation et d'utilit\u00e9",
  "why_iso": "Fabrication certifi\u00e9e ISO 9001 & CE",
  "why_pricing": "Prix comp\u00e9titifs directs usine",
  "why_oem": "Support complet OEM / ODM",
  "why_qc": "Contr\u00f4le qualit\u00e9 strict \u2014 chaque unit\u00e9 test\u00e9e avant exp\u00e9dition",
  "why_logistics": "Logistique d'exportation rapide vers 95+ pays",
  "why_support": "\u00c9quipe de support technique r\u00e9active",
  "cat_screw-machine": "Machines \u00e0 Vis",
  "cat_energy-meter": "Compteurs d'\u00c9nergie",
  "cat_current-transformer": "Transformateurs de Courant",
  "cat_voltage-stabilizer-regulator": "Stabilisateurs de Tension",
  "cat_variac-transformer": "Transformateurs Variac",
  "cat_terminal-connector": "Bornes & Connecteurs",
  "cat_fuse-protection": "Fusibles & Protection",
  "cat_socket-wiring": "Prises & C\u00e2blage",
  "cat_solar-pv-products": "Produits Solaires & PV",
  "cat_tools-hardware": "Outils & Quincaillerie",
  "cat_aluminum-busbar": "Barres de Bus en Aluminium",
  "cat_flexible-busbar": "Barres de Bus Flexibles",
  "cat_security-seal": "Joints de S\u00e9curit\u00e9",
  "cat_other": "Autres Produits",
  "browse_cat": "Parcourir par Cat\u00e9gorie",
  "view_all": "Voir tout",
  "inquiry_price": "Demander un Prix",
  "products_count": "produits",
  "yomin_tagline": "Produits \u00e9lectriques d'usine \u2014 approuv\u00e9s dans plus de 95 pays"
  },
  es: {
  "certified": "Certificado ISO 9001 & CE",
  "factory_direct": "Directo de F\u00e1brica",
  "oem_odm": "OEM / ODM Disponible",
  "95_countries": "95+ Pa\u00edses",
  "since_1996": "Desde 1996",
  "home": "Inicio",
  "all_products": "Todos los Productos",
  "nav_quote": "Obtener una Cotizaci\u00f3n",
  "request_quote": "Solicitar Cotizaci\u00f3n",
  "whatsapp": "WhatsApp",
  "more_in_cat": "M\u00e1s en esta categor\u00eda",
  "min_order": "Pedido m\u00edn.:",
  "worldwide_ship": "\ud83c\udf0d Env\u00edo Mundial",
  "tech_specs": "Especificaciones T\u00e9cnicas",
  "key_features": "Caracter\u00edsticas Principales",
  "applications": "Aplicaciones",
  "why_yomin": "Por Qu\u00e9 Elegir Yomin Electric",
  "why_body": "Zhejiang Yomin Electric Co., Ltd. es fabricante directo de f\u00e1brica de productos el\u00e9ctricos de precisi\u00f3n desde 1996, con la confianza de compradores en m\u00e1s de 95 pa\u00edses. Cada unidad se prueba antes del env\u00edo.",
  "ship_time": "15 a 25 d\u00edas h\u00e1biles",
  "ship_countries": "Env\u00edo a m\u00e1s de 95 pa\u00edses",
  "ship_packaging": "Embalaje de exportaci\u00f3n seguro",
  "ship_returns": "Devoluci\u00f3n en 30 d\u00edas",
  "ship_free_consult": "Consulta de env\u00edo gratuita",
  "ship_incoterms": "DDP / FOB / CIF disponibles",
  "ship_freight": "Flete mar\u00edtimo y a\u00e9reo",
  "ship_global": "Distribuci\u00f3n global",
  "ship_cartons": "Cajas de exportaci\u00f3n",
  "ship_guarantee": "Garant\u00eda de calidad",
  "ship_contact": "Contacte nuestro equipo",
  "ship_incoterms_sub": "Todos los Incoterms disponibles",
  "app_residential": "Instalaciones residenciales y comerciales",
  "app_industrial": "Sistemas de energ\u00eda industrial",
  "app_energy_mon": "Monitoreo y gesti\u00f3n de energ\u00eda",
  "app_oem": "Producci\u00f3n OEM / ODM",
  "app_export": "Proyectos de exportaci\u00f3n y servicios p\u00fablicos",
  "why_iso": "Fabricaci\u00f3n certificada ISO 9001 & CE",
  "why_pricing": "Precios competitivos directos de f\u00e1brica",
  "why_oem": "Soporte completo OEM / ODM",
  "why_qc": "Control de calidad estricto \u2014 cada unidad probada antes del env\u00edo",
  "why_logistics": "Log\u00edstica de exportaci\u00f3n r\u00e1pida a m\u00e1s de 95 pa\u00edses",
  "why_support": "Equipo de soporte t\u00e9cnico receptivo",
  "cat_screw-machine": "M\u00e1quinas de Tornillos",
  "cat_energy-meter": "Contadores de Energ\u00eda",
  "cat_current-transformer": "Transformadores de Corriente",
  "cat_voltage-stabilizer-regulator": "Estabilizadores de Tensi\u00f3n",
  "cat_variac-transformer": "Transformadores Variac",
  "cat_terminal-connector": "Terminales & Conectores",
  "cat_fuse-protection": "Fusibles & Protecci\u00f3n",
  "cat_socket-wiring": "Enchufes & Cableado",
  "cat_solar-pv-products": "Productos Solares y FV",
  "cat_tools-hardware": "Herramientas & Hardware",
  "cat_aluminum-busbar": "Barras de Bus de Aluminio",
  "cat_flexible-busbar": "Barras de Bus Flexibles",
  "cat_security-seal": "Sellos de Seguridad",
  "cat_other": "Otros Productos",
  "browse_cat": "Explorar por Categor\u00eda",
  "view_all": "Ver todo",
  "inquiry_price": "Consultar Precio",
  "products_count": "productos",
  "yomin_tagline": "Productos el\u00e9ctricos de f\u00e1brica \u2014 confiados en m\u00e1s de 95 pa\u00edses"
  },
  ar: {
  "certified": "\u0645\u0639\u062a\u0645\u062f ISO 9001 & CE",
  "factory_direct": "\u0645\u0628\u0627\u0634\u0631 \u0645\u0646 \u0627\u0644\u0645\u0635\u0646\u0639",
  "oem_odm": "OEM / ODM \u0645\u062a\u0627\u062d",
  "95_countries": "\u0669\u0665+ \u062f\u0648\u0644\u0629",
  "since_1996": "\u0645\u0646\u0630 1996",
  "home": "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",
  "all_products": "\u062c\u0645\u064a\u0639 \u0627\u0644\u0645\u0646\u062a\u062c\u0627\u062a",
  "nav_quote": "\u0627\u062d\u0635\u0644 \u0639\u0644\u0649 \u0639\u0631\u0636 \u0633\u0639\u0631",
  "request_quote": "\u0637\u0644\u0628 \u0639\u0631\u0636 \u0633\u0639\u0631",
  "whatsapp": "\u0648\u0627\u062a\u0633\u0627\u0628",
  "more_in_cat": "\u0627\u0644\u0645\u0632\u064a\u062f \u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0641\u0626\u0629",
  "min_order": "\u0627\u0644\u062d\u062f \u0627\u0644\u0623\u062f\u0646\u0649 \u0644\u0644\u0637\u0644\u0628:",
  "worldwide_ship": "\ud83c\udf0d \u0634\u062d\u0646 \u0639\u0627\u0644\u0645\u064a",
  "tech_specs": "\u0627\u0644\u0645\u0648\u0627\u0635\u0641\u0627\u062a \u0627\u0644\u0641\u0646\u064a\u0629",
  "key_features": "\u0627\u0644\u0645\u064a\u0632\u0627\u062a \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",
  "applications": "\u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a",
  "why_yomin": "\u0644\u0645\u0627\u0630\u0627 \u062a\u062e\u062a\u0627\u0631 Yomin Electric",
  "why_body": "\u062a\u0635\u0646\u0639 \u0634\u0631\u0643\u0629 Zhejiang Yomin Electric Co., Ltd. \u0645\u0646\u062a\u062c\u0627\u062a \u0643\u0647\u0631\u0628\u0627\u0626\u064a\u0629 \u062f\u0642\u064a\u0642\u0629 \u0645\u0646\u0630 \u0639\u0627\u0645 1996\u060c \u0648\u062a\u062d\u0638\u0649 \u0628\u062b\u0642\u0629 \u0627\u0644\u0645\u0634\u062a\u0631\u064a\u0646 \u0641\u064a \u0623\u0643\u062b\u0631 \u0645\u0646 95 \u062f\u0648\u0644\u0629. \u064a\u062a\u0645 \u0627\u062e\u062a\u0628\u0627\u0631 \u0643\u0644 \u0648\u062d\u062f\u0629 \u0642\u0628\u0644 \u0627\u0644\u0634\u062d\u0646.",
  "ship_time": "\u0661\u0665\u2013\u0662\u0665 \u064a\u0648\u0645 \u0639\u0645\u0644",
  "ship_countries": "\u062e\u062f\u0645\u0629 \u0623\u0643\u062b\u0631 \u0645\u0646 95 \u062f\u0648\u0644\u0629",
  "ship_packaging": "\u062a\u063a\u0644\u064a\u0641 \u062a\u0635\u062f\u064a\u0631 \u0622\u0645\u0646",
  "ship_returns": "\u0633\u064a\u0627\u0633\u0629 \u0625\u0631\u062c\u0627\u0639 30 \u064a\u0648\u0645\u0627\u064b",
  "ship_free_consult": "\u0627\u0633\u062a\u0634\u0627\u0631\u0629 \u0634\u062d\u0646 \u0645\u062c\u0627\u0646\u064a\u0629",
  "ship_incoterms": "DDP / FOB / CIF \u0645\u062a\u0627\u062d",
  "ship_freight": "\u0634\u062d\u0646 \u0628\u062d\u0631\u064a \u0648\u062c\u0648\u064a",
  "ship_global": "\u062a\u0648\u0632\u064a\u0639 \u0639\u0627\u0644\u0645\u064a",
  "ship_cartons": "\u0643\u0631\u0627\u062a\u064a\u0646 \u062a\u0635\u062f\u064a\u0631 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u062c\u0648\u062f\u0629",
  "ship_guarantee": "\u0636\u0645\u0627\u0646 \u0627\u0644\u062c\u0648\u062f\u0629",
  "ship_contact": "\u0627\u062a\u0635\u0644 \u0628\u0641\u0631\u064a\u0642\u0646\u0627",
  "ship_incoterms_sub": "\u062c\u0645\u064a\u0639 \u0634\u0631\u0648\u0637 Incoterms \u0645\u062a\u0627\u062d\u0629",
  "app_residential": "\u0627\u0644\u062a\u0631\u0643\u064a\u0628\u0627\u062a \u0627\u0644\u0633\u0643\u0646\u064a\u0629 \u0648\u0627\u0644\u062a\u062c\u0627\u0631\u064a\u0629",
  "app_industrial": "\u0623\u0646\u0638\u0645\u0629 \u0627\u0644\u0637\u0627\u0642\u0629 \u0627\u0644\u0635\u0646\u0627\u0639\u064a\u0629",
  "app_energy_mon": "\u0645\u0631\u0627\u0642\u0628\u0629 \u0648\u0625\u062f\u0627\u0631\u0629 \u0627\u0644\u0637\u0627\u0642\u0629",
  "app_oem": "\u0625\u0646\u062a\u0627\u062c OEM / ODM",
  "app_export": "\u0645\u0634\u0627\u0631\u064a\u0639 \u0627\u0644\u062a\u0635\u062f\u064a\u0631 \u0648\u0627\u0644\u0645\u0631\u0627\u0641\u0642",
  "why_iso": "\u062a\u0635\u0646\u064a\u0639 \u0645\u0639\u062a\u0645\u062f \u0628\u0640 ISO 9001 & CE",
  "why_pricing": "\u0623\u0633\u0639\u0627\u0631 \u062a\u0646\u0627\u0641\u0633\u064a\u0629 \u0645\u0628\u0627\u0634\u0631\u0629 \u0645\u0646 \u0627\u0644\u0645\u0635\u0646\u0639",
  "why_oem": "\u062f\u0639\u0645 \u062a\u062e\u0635\u064a\u0635 OEM/ODM \u0627\u0644\u0643\u0627\u0645\u0644",
  "why_qc": "\u0645\u0631\u0627\u0642\u0628\u0629 \u0627\u0644\u062c\u0648\u062f\u0629 \u0627\u0644\u0635\u0627\u0631\u0645\u0629 \u2014 \u0643\u0644 \u0648\u062d\u062f\u0629 \u062a\u064f\u062e\u062a\u0628\u0631 \u0642\u0628\u0644 \u0627\u0644\u0634\u062d\u0646",
  "why_logistics": "\u0644\u0648\u062c\u0633\u062a\u064a\u0627\u062a \u062a\u0635\u062f\u064a\u0631 \u0633\u0631\u064a\u0639\u0629 \u0625\u0644\u0649 \u0623\u0643\u062b\u0631 \u0645\u0646 95 \u062f\u0648\u0644\u0629",
  "why_support": "\u0641\u0631\u064a\u0642 \u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0641\u0646\u064a \u0627\u0644\u0645\u062a\u062c\u0627\u0648\u0628",
  "cat_screw-machine": "\u0645\u0627\u0643\u064a\u0646\u0627\u062a \u0627\u0644\u0628\u0631\u0627\u063a\u064a",
  "cat_energy-meter": "\u0639\u062f\u0627\u062f\u0627\u062a \u0627\u0644\u0637\u0627\u0642\u0629",
  "cat_current-transformer": "\u0645\u062d\u0648\u0644\u0627\u062a \u0627\u0644\u062a\u064a\u0627\u0631",
  "cat_voltage-stabilizer-regulator": "\u0645\u0646\u0638\u0645\u0627\u062a \u0627\u0644\u062c\u0647\u062f",
  "cat_variac-transformer": "\u0645\u062d\u0648\u0644\u0627\u062a \u0641\u0627\u0631\u064a\u0643",
  "cat_terminal-connector": "\u0637\u0631\u0641\u064a\u0627\u062a \u0648\u0645\u0648\u0635\u0644\u0627\u062a",
  "cat_fuse-protection": "\u0627\u0644\u0645\u0646\u0635\u0647\u0631\u0627\u062a \u0648\u0627\u0644\u062d\u0645\u0627\u064a\u0629",
  "cat_socket-wiring": "\u0645\u0642\u0627\u0628\u0633 \u0648\u0623\u0633\u0644\u0627\u0643",
  "cat_solar-pv-products": "\u0645\u0646\u062a\u062c\u0627\u062a \u0627\u0644\u0637\u0627\u0642\u0629 \u0627\u0644\u0634\u0645\u0633\u064a\u0629",
  "cat_tools-hardware": "\u0623\u062f\u0648\u0627\u062a \u0648\u0645\u0639\u062f\u0627\u062a",
  "cat_aluminum-busbar": "\u0642\u0636\u0628\u0627\u0646 \u0627\u0644\u0623\u0644\u0648\u0645\u0646\u064a\u0648\u0645",
  "cat_flexible-busbar": "\u0642\u0636\u0628\u0627\u0646 \u0645\u0631\u0646\u0629",
  "cat_security-seal": "\u0623\u062e\u062a\u0627\u0645 \u0627\u0644\u0623\u0645\u0627\u0646",
  "cat_other": "\u0645\u0646\u062a\u062c\u0627\u062a \u0623\u062e\u0631\u0649",
  "browse_cat": "\u062a\u0635\u0641\u062d \u062d\u0633\u0628 \u0627\u0644\u0641\u0626\u0629",
  "view_all": "\u0639\u0631\u0636 \u0627\u0644\u0643\u0644",
  "inquiry_price": "\u0627\u0633\u062a\u0641\u0633\u0631 \u0639\u0646 \u0627\u0644\u0633\u0639\u0631",
  "products_count": "\u0645\u0646\u062a\u062c\u0627\u062a",
  "yomin_tagline": "\u0645\u0646\u062a\u062c\u0627\u062a \u0643\u0647\u0631\u0628\u0627\u0626\u064a\u0629 \u0645\u0628\u0627\u0634\u0631\u0629 \u0645\u0646 \u0627\u0644\u0645\u0635\u0646\u0639 \u2014 \u0645\u0648\u062b\u0648\u0642 \u0628\u0647\u0627 \u0641\u064a \u0623\u0643\u062b\u0631 \u0645\u0646 95 \u062f\u0648\u0644\u0629"
  }
  };

  // Initialize __ymT if not already set (index.html sets it; product pages don't)
  if (!window.__ymT) window.__ymT = {};
  var T = window.__ymT;

  // Merge product keys (don't overwrite existing nav keys from index.html)
  ['en','fr','es','ar'].forEach(function(l) {
    T[l] = Object.assign({}, PKG[l], T[l] || {});
  });

  // Expose sL as alias for setLang (nav buttons call sL())
  window.sL = function(lang) {
    if (window.setLang) {
      window.setLang(lang);
    } else {
      // main.js not yet loaded — store and apply when ready
      localStorage.setItem('ym_lang', lang);
      window.ymLang = lang;
      applyPageTranslations(lang);
      document.addEventListener('DOMContentLoaded', function() {
        if (window.setLang) window.setLang(lang);
      });
    }
  };

  // Apply data-i18n translations to the current page
  function applyPageTranslations(l) {
    if (!l || l === 'en') {
      // Reset to English
      document.querySelectorAll('[data-i18n]').forEach(function(el) {
        var k = el.getAttribute('data-i18n');
        var val = (T['en'] || PKG['en'])[k];
        if (val) el.textContent = val;
      });
      document.documentElement.setAttribute('lang', 'en');
      document.documentElement.removeAttribute('dir');
      return;
    }
    var d = T[l] || PKG[l];
    if (!d) return;

    // Static UI strings via data-i18n
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var k = el.getAttribute('data-i18n');
      if (d[k] !== undefined) el.textContent = d[k];
    });

    // Product titles via data-pid (uses window.T from main.js)
    if (window.T && window.T[l]) {
      document.querySelectorAll('[data-pid]').forEach(function(el) {
        var pid = el.getAttribute('data-pid');
        if (window.T[l][pid]) el.textContent = window.T[l][pid];
      });
    }

    // Arabic RTL
    if (l === 'ar') {
      document.documentElement.setAttribute('dir', 'rtl');
      document.documentElement.setAttribute('lang', 'ar');
    } else {
      document.documentElement.removeAttribute('dir');
      document.documentElement.setAttribute('lang', l);
    }
  }

  // Expose for external use
  window.applyPageTranslations = applyPageTranslations;

  // Apply immediately on load if language stored
  function applyStored() {
    var stored = localStorage.getItem('ym_lang') || window.ymLang;
    if (stored && stored !== 'en') applyPageTranslations(stored);
  }

  // Apply now
  applyStored();
  // Apply after DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyStored);
  }
  // Apply when main.js fires langChanged
  document.addEventListener('langChanged', function(e) { applyPageTranslations(e.detail); });
  window.addEventListener('langChanged', function(e) { applyPageTranslations(e.detail); });
  // Apply after full load
  window.addEventListener('load', applyStored);

})();
