# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-20 (Google Search Console Query Optimization):
1. Substation Engineering: Current Transformer Sizing Calculation Guide (EN, FR, ES, AR)
2. Utility Metering: Difference Between Prepaid and Postpaid Electricity (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. CURRENT TRANSFORMER SIZING CALCULATION (EN, FR, ES, AR)
# ==============================================================================

CT_CALC_EN = dict(
    lang='en',
    dir='ltr',
    slug='substation-engineering-current-transformer-sizing-calculation',
    title='Substation Engineering: Current Transformer Sizing Calculation Guide',
    breadcrumb='Substation Engineering &amp; CT Sizing Calculations',
    read='11 min read',
    alt='Substation switchgear compartment with three 24kV epoxy cast current transformers during secondary injection testing with calculation clipboard',
    desc=('Electrical switchgear engineering, protection relay coordination, and utility revenue metering: How to perform a current transformer sizing calculation. '
          'Step-by-step mathematical formulas for primary full-load current ($I_p$), 5A vs 1A secondary selection, lead resistance burden (VA), and protection CT knee-point voltage ($V_k$) under IEC 61869-2 and IEEE C57.13.'),
    model='Model MSQ, RCT, AK, and BH-0.66 Series 0.66kV to 35kV Measuring and Protection Current Transformers (Class 0.2S, Class 0.5, 5P10, 5P20, Rated Secondary 1A/5A, IEC 61869-2 & IEEE C57.13 Compliant)',
    category='Substation Engineering & CT Sizing Calculations / Instrument Transformers',
    kw='current transformer sizing calculation &middot; how to calculate ct ratio &middot; ct burden calculation &middot; protection ct sizing &middot; knee point voltage calculation &middot; ct saturation calculation &middot; iec 61869-2',
    specs=[
        ('Primary Current Sizing Formula ($I_{pn}$)', 'Calculated via $I_{pn} \ge 1.25 \times I_{\text{FLC}}$, where $I_{\text{FLC}} = \frac{S}{\sqrt{3} \times V_{\text{LL}}}$, rounded to the next standard primary rating'),
        ('Secondary Rated Output Current ($I_{sn}$)', 'Standard $5\,\text{A}$ for short panelboard wiring ($< 10\,\text{m}$); Standard $1\,\text{A}$ for long runs ($> 30\,\text{m}$) to slash secondary lead burden by $96\%$ ($I^2R$)'),
        ('Total Connected Burden Calculation ($S_b$)', 'Total VA Burden $S_b = I_{sn}^2 \times (2 \times R_{\text{leads}} + R_{\text{meter}} + R_{\text{contact}})$, where $R_{\text{leads}} = \rho \times \frac{L}{A}$'),
        ('Protection Knee-Point Voltage Formula ($V_k$)', '$V_k \ge 2 \times I_{f(\text{max})} \times \frac{I_{sn}}{I_{pn}} \times (R_{ct} + R_b)$ to prevent magnetic saturation during maximum asymmetrical through-faults'),
        ('Metering Accuracy Class Standards', 'Class 0.2S and Class 0.5S for utility grid tariff metering; Class 0.5 and Class 1.0 for commercial panel meters under IEC 61869-2'),
        ('Protection Accuracy Class Standards', 'Class 5P10 and 5P20: Composite error $\le 5\%$ at $10\times$ or $20\times$ rated symmetrical primary fault current for overcurrent & differential relays'),
        ('Instrument Security Factor ($FS$)', '$FS \le 5$ or $FS \le 10$ for metering CTs: Guarantees magnetic core saturates during primary short-circuits to protect delicate digital meters'),
        ('Short-Time Thermal Current ($I_{th}$)', 'Rated symmetrical thermal withstand current $I_{th} \ge 80 \times I_{pn}$ to $100 \times I_{pn}$ for $1.0\,\text{s}$ or $3.0\,\text{s}$ duration under IEC 61869-1')
    ],
    faqs=[
        ('What is the step-by-step formula to calculate the primary current rating ($I_{pn}$) of a Current Transformer?',
         'To size the primary current rating ($I_{pn}$), follow these standard engineering steps: '
         '<ol>'
         '<li><strong>Calculate the Full Load Current ($I_{\text{FLC}}$):</strong> '
         'For a 3-phase system: $I_{\text{FLC}} = \frac{P_{\text{kVA}} \times 1000}{\sqrt{3} \times V_{\text{LL}}}$. For example, on an $11\,\text{kV}$ system with a $2000\,\text{kVA}$ transformer: '
         '$I_{\text{FLC}} = \frac{2000 \times 1000}{1.732 \times 11000} \approx 105\,\text{A}$.</li>'
         '<li><strong>Apply the Continuous Overload Sizing Factor ($1.25\times$):</strong> '
         '$I_{\text{target}} = 1.25 \times 105\,\text{A} = 131.2\,\text{A}$.</li>'
         '<li><strong>Select the Next Standard Commercial Primary Rating:</strong> '
         'Standard IEC ratings are 100A, 150A, 200A, 250A, 300A, 400A, 500A, 600A, 800A, 1000A. In this case, select a <strong>150/5A</strong> or <strong>150/1A</strong> CT. '
         'Selecting 150A ensures the CT operates in its linear, high-accuracy zone (between 50% and 100% of rating) during normal operation without saturating during peak overloads.</li>'
         '</ol>'),
        ('Why should you choose a 1A secondary instead of a 5A secondary for long cable runs?',
         'The secondary lead burden loss is proportional to the square of the current ($P = I^2 R$). '
         '<ul>'
         '<li><strong>With a 5A secondary:</strong> $I^2 = 5^2 = 25$. A $1\,\Omega$ lead resistance imposes a massive $25 \times 1 = 25\,\text{VA}$ burden on the CT secondary! '
         'This exceeds the rated burden of most standard CTs (5VA, 10VA, or 15VA), causing severe measurement ratio errors and core saturation.</li>'
         '<li><strong>With a 1A secondary:</strong> $I^2 = 1^2 = 1$. The identical $1\,\Omega$ lead resistance imposes only $1 \times 1 = 1\,\text{VA}$ burden!</li>'
         '</ul>'
         'Choosing a 1A secondary reduces secondary wiring losses by <strong>96%</strong>, allowing smaller cable cross-sections ($2.5\,\text{mm}^2$ vs $6\,\text{mm}^2$) '
         'and permitting CTs to be located hundreds of meters away in outdoor substation switchyards without overloading the secondary core.'),
        ('How do you calculate the Knee-Point Voltage ($V_k$) for a protection class Current Transformer?',
         'For protection CTs (such as differential and distance protection under Class PX / Class 5P), the knee-point voltage $V_k$ is the point on the excitation curve '
         'where a $10\%$ increase in secondary voltage increases the excitation current by $50\%$. The sizing formula is: '
         '<p style="font-family:monospace;font-weight:bold;margin:10px 0;">V_k \ge 2 \times I_{f(\text{max})} \times \frac{I_{sn}}{I_{pn}} \times (R_{ct} + 2R_{\text{lead}} + R_{\text{relay}})</p>'
         'Where: '
         '<ul>'
         '<li>$I_{f(\text{max})}$ = Maximum prospective symmetrical primary short-circuit fault current (e.g. 25,000A).</li>'
         '<li>$\frac{I_{sn}}{I_{pn}}$ = CT transformation turns ratio (e.g. 5/1000 = 1/200).</li>'
         '<li>$R_{ct}$ = Internal secondary winding DC resistance at $75^\circ\text{C}$ (e.g. $0.5\,\Omega$).</li>'
         '<li>$2R_{\text{lead}}$ = Loop resistance of the secondary cables out and back (e.g. $0.4\,\Omega$).</li>'
         '<li>$R_{\text{relay}}$ = Internal impedance of the protection relay (typically $< 0.1\,\Omega$ for digital microprocessors).</li>'
         '<li>The safety multiplier of 2 ensures that the CT core does not saturate during the initial fully asymmetrical DC offset component of the fault current.</li>'
         '</ul>')
    ],
    cta='Designing substation control systems, generator protection panels, or low/medium-voltage switchgear requiring certified Class 0.2S / Class 0.5 metering current transformers or Class 5P10 / 5P20 protection current transformers? YOMIN manufactures precision instrument transformers with custom turns ratios, verified knee-point curves, and certified burden ratings under IEC 61869-2.',
    body='''
<h2>The Critical Role of Precise Current Transformer Sizing in Electrical Engineering</h2>
<p>In electrical substations, industrial power plants, and utility switchgear, current transformers (CTs) serve as the sensory nervous system: stepping down thousands of amperes of primary line current into safe, standardized secondary currents (5A or 1A) for revenue meters and protection relays.</p>
<p>However, an improperly sized current transformer represents a catastrophic engineering hazard:</p>
<ul>
  <li><strong>Under-sizing the CT burden:</strong> Connecting a 15VA metering circuit to a 5VA CT drives the magnetic core into continuous saturation, introducing massive ratio and phase errors that cause tens of thousands of dollars in commercial unmetered billing losses.</li>
  <li><strong>Under-sizing protection CT knee-point voltage ($V_k$):</strong> During an external through-fault, an under-sized protection CT saturates within milliseconds, producing distorted, zeroed secondary currents that cause differential protection relays to trip falsely or overcurrent breakers to fail to operate, resulting in switchgear arc-flash destruction.</li>
</ul>
<p>This comprehensive engineering guide outlines the exact step-by-step mathematical calculations required to size primary ratings, secondary outputs, total circuit burdens, and knee-point voltages under international standards <strong>IEC 61869-2</strong> and <strong>IEEE C57.13</strong>.</p>

<h2>Step-by-Step Sizing Methodology</h2>
<ol>
  <li><strong>Step 1: Primary Current Calculation ($I_{pn}$):</strong> Calculate full-load current from maximum kVA rating, apply a continuous $1.25\times$ safety factor for future load expansion, and select the next standard commercial primary rating.</li>
  <li><strong>Step 2: Secondary Current Selection (5A vs. 1A):</strong> Evaluate the secondary wire loop distance from the switchgear to the control room. If the distance exceeds 30 meters, mandate a 1A secondary to reduce $I^2R$ lead burden by 96%.</li>
  <li><strong>Step 3: Total Secondary Burden Calculation ($S_b$ in VA):</strong> Sum the wire lead resistance ($R_{\text{lead}} = \rho \cdot \frac{2L}{A}$), digital meter impedance, and terminal contact resistances. Ensure total connected VA is between 25% and 100% of the CT\'s rated burden to maintain class accuracy.</li>
  <li><strong>Step 4: Verification of Accuracy Limit Factor (ALF) and Knee-Point Voltage ($V_k$):</strong> For protection CTs, ensure the core can develop sufficient secondary electromotive force ($V_k$) under maximum prospective fault current ($I_{\text{sc}}$) without entering magnetic saturation before the protection relay trips.</li>
</ol>

<h2>Comparison: Metering Current Transformers vs. Protection Current Transformers</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Metering Current Transformer (Class 0.2S / 0.5)</th>
      <th>Protection Current Transformer (Class 5P10 / 5P20)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Core Operating Range</strong></td>
      <td>High accuracy from 5% to 120% of rated nominal current ($I_n$).</td>
      <td>Linear accuracy extending up to $10\times$ or $20\times$ rated fault current ($10 I_n$ or $20 I_n$).</td>
    </tr>
    <tr>
      <td><strong>Magnetic Saturation Behavior</strong></td>
      <td><strong>Early Saturation Mandated ($FS \le 5$ or $10$):</strong> Core saturates quickly during short-circuits to protect meters from burning out.</td>
      <td><strong>Late Saturation Mandated:</strong> High knee-point voltage ensures zero saturation during multi-kiloampere fault surges.</td>
    </tr>
    <tr>
      <td><strong>Standard Accuracy Classes</strong></td>
      <td>Class 0.1, Class 0.2, Class 0.2S, Class 0.5, Class 0.5S, Class 1.0.</td>
      <td>Class 5P, Class 10P, Class PR, Class PX under IEC 61869-2 (Class C / T under IEEE C57.13).</td>
    </tr>
    <tr>
      <td><strong>Primary Application</strong></td>
      <td>Kilowatt-hour (kWh) tariff billing, tenant submetering, power quality logging.</td>
      <td>Overcurrent relays, earth fault relays, transformer differential protection.</td>
    </tr>
  </tbody>
</table>
'''
)

CT_CALC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='substation-engineering-current-transformer-sizing-calculation-fr',
    title='Ingénierie Électrique : Guide de Calcul et Dimensionnement des Transformateurs de Courant',
    breadcrumb='Ingénierie &amp; Calcul des Transformateurs de Courant',
    read='11 min de lecture',
    alt='Compartiment de tableau électrique haute tension avec trois transformateurs de courant 24kV en résine époxy lors d\'essais d\'injection secondaire',
    desc=('Ingénierie des postes électriques, coordination des protections et comptage d\'énergie : Comment dimensionner et calculer un transformateur de courant (TI). '
          'Formules pas à pas pour le courant primaire ($I_p$), choix du secondaire 5A ou 1A, calcul de la charge de filerie (VA) et tension de coude de saturation ($V_k$) selon CEI 61869-2.'),
    model='Séries MSQ, RCT, AK et BH-0.66 : Transformateurs de Courant de Mesure et de Protection 0,66kV à 35kV (Classe 0.2S, 0.5, 5P10, 5P20, Secondaire 1A/5A, Conforme CEI 61869-2)',
    category='Ingénierie & Calcul des Transformateurs de Courant / Transformateurs de Mesure',
    kw='calcul transformateur de courant &middot; dimensionnement ti &middot; calcul rapport de transformation ti &middot; charge secondaire va ti &middot; tension de coude ti vk &middot; saturation transformateur de courant',
    specs=[
        ('Formule de Calcul du Courant Primaire ($I_{pn}$)', 'Calculé selon $I_{pn} \ge 1,25 \times I_{\text{FLC}}$, avec $I_{\text{FLC}} = \frac{S}{\sqrt{3} \times U_{\text{LL}}}$, arrondi au calibre normalisé immédiatement supérieur'),
        ('Courant Secondaire Assigné ($I_{sn}$)', 'Standard $5\,\text{A}$ pour courtes liaisons en armoire ($< 10\,\text{m}$) ; Standard $1\,\text{A}$ pour liaisons longues ($> 30\,\text{m}$) réduisant les pertes filerie de $96\%$'),
        ('Calcul de la Charge Raccordée ($S_b$)', 'Charge totale en VA $S_b = I_{sn}^2 \times (2 \times R_{\text{fils}} + R_{\text{appareil}} + R_{\text{contact}})$, avec $R_{\text{fils}} = \rho \times \frac{L}{S}$'),
        ('Formule de Tension de Coude de Protection ($V_k$)', '$V_k \ge 2 \times I_{cc(\text{max})} \times \frac{I_{sn}}{I_{pn}} \times (R_{ct} + R_b)$ pour éviter toute saturation lors d\'un court-circuit asymétrique'),
        ('Classes de Précision de Mesure', 'Classe 0.2S et Classe 0.5S pour le comptage tarifaire officiel ; Classe 0.5 et 1.0 pour indicateurs de tableau selon CEI 61869-2'),
        ('Classes de Précision de Protection', 'Classe 5P10 et 5P20 : Erreur composée $\le 5\%$ à $10\times$ ou $20\times$ le courant nominal de court-circuit assigné'),
        ('Facteur de Sécurité d\'Appareil ($FS$)', '$FS \le 5$ ou $FS \le 10$ : Garantit la saturation du noyau magnétique en cas de court-circuit primaire pour protéger les compteurs électroniques'),
        ('Tenue Thermique de Court-Circuit ($I_{th}$)', 'Courant thermique assigné de court-circuit $I_{th} \ge 80 \times I_{pn}$ pendant $1,0\,\text{s}$ ou $3,0\,\text{s}$ selon la norme CEI 61869-1')
    ],
    faqs=[
        ('Comment calculer le calibre primaire d\'un transformateur de courant (TI) ?',
         'Pour dimensionner le courant primaire ($I_{pn}$) : '
         '<ol>'
         '<li><strong>Calculer le courant nominal de pleine charge ($I_{\text{FLC}}$) :</strong> '
         'En triphasé : $I_{\text{FLC}} = \frac{P_{\text{kVA}} \times 1000}{\sqrt{3} \times U_{\text{composée}}}$. Par exemple, pour un transformateur $2000\,\text{kVA}$ sous $11\,\text{kV}$ : '
         '$I_{\text{FLC}} \approx 105\,\text{A}$.</li>'
         '<li><strong>Appliquer le facteur de sécurité de $1,25\times$ :</strong> '
         '$I_{\text{cible}} = 1,25 \times 105\,\text{A} = 131,2\,\text{A}$.</li>'
         '<li><strong>Choisir le calibre normalisé :</strong> Choisir un TI de <strong>150/5A</strong> ou <strong>150/1A</strong>.</li>'
         '</ol>'),
        ('Pourquoi privilégier un secondaire 1A plutôt que 5A pour les liaisons distantes ?',
         'Les pertes en ligne de la filerie secondaire sont proportionnelles au carré du courant ($P = R \cdot I^2$). '
         'Avec un secondaire 5A, un câble de résistance $1\,\Omega$ consomme $25\,\text{VA}$, ce qui surcharge le TI. '
         'Avec un secondaire 1A, la même résistance ne consomme que $1\,\text{VA}$. Le choix du 1A réduit les pertes par 25 (soit 96% d\'économie) '
         'et permet d\'éloigner les relais de protection de plusieurs centaines de mètres.')
    ],
    cta='Vous concevez des postes de distribution électrique, des armoires de protection ou des tableaux MT/BT nécessitant des transformateurs de courant de mesure (Classe 0.2S / 0.5) ou de protection (Classe 5P10 / 5P20) certifiés CEI 61869-2 ? YOMIN fabrique la gamme complète de TI avec courbes de magnétisation et tensions de coude garanties.',
    body='''
<h2>La Méthodologie Indispensable pour le Dimensionnement des Transformateurs de Courant</h2>
<p>Dans les postes électriques de transformation et les armoires industrielles, les transformateurs de courant (TI) constituent les organes de détection fondamentaux : ils abaissent des courants de plusieurs milliers d\'ampères à des valeurs sécurisées de 5A ou 1A pour alimenter les centrales de mesure et relais de protection.</p>
<p>Un mauvais calcul de dimensionnement entraîne de lourdes conséquences :</p>
<ul>
  <li><strong>Sous-dimensionnement de la puissance (VA) :</strong> Provoque une saturation magnétique prématurée et d\'importantes erreurs de mesure d\'énergie.</li>
  <li><strong>Sous-dimensionnement de la tension de coude ($V_k$) en protection :</strong> Le noyau sature lors d\'un court-circuit, empêchant le relais de déclencher et provoquant la destruction thermique du jeu de barres.</li>
</ul>
<p>Ce guide technique détaille les étapes précises et formules mathématiques nécessaires au calcul du rapport, de la charge de boucle et de la tension de saturation sous la norme internationale <strong>CEI 61869-2</strong>.</p>
'''
)

CT_CALC_ES = dict(
    lang='es',
    dir='ltr',
    slug='substation-engineering-current-transformer-sizing-calculation-es',
    title='Ingeniería de Subestaciones: Guía de Cálculo y Dimensionamiento de Transformadores de Corriente',
    breadcrumb='Ingeniería &amp; Cálculo de Transformadores de Corriente',
    read='11 min de lectura',
    alt='Compartimento de celdas de media tensión con tres transformadores de corriente de 24kV en resina epoxi durante pruebas de inyección secundaria',
    desc=('Ingeniería de subestaciones eléctricas, coordinación de protecciones y medición tarifaria: Cómo realizar el cálculo de dimensionamiento de un transformador de corriente (TC). '
          'Fórmulas matemáticas para la corriente primaria ($I_p$), selección de secundario 5A vs 1A, cálculo de carga de cableado (VA) y tensión de codo de saturación ($V_k$) bajo norma IEC 61869-2.'),
    model='Series MSQ, RCT, AK y BH-0.66: Transformadores de Corriente de Medida y Protección de 0.66kV a 35kV (Clase 0.2S, 0.5, 5P10, 5P20, Secundario 1A/5A, Conforme a IEC 61869-2)',
    category='Ingeniería & Cálculo de Transformadores de Corriente / Transformadores de Medida',
    kw='calculo transformador de corriente &middot; dimensionamiento tc &middot; calculo relacion de transformacion tc &middot; carga secundaria va tc &middot; voltaje de codo tc vk &middot; saturacion transformador de corriente',
    specs=[
        ('Fórmula de Corriente Primaria Asignada ($I_{pn}$)', 'Calculada mediante $I_{pn} \ge 1.25 \times I_{\text{FLC}}$, con $I_{\text{FLC}} = \frac{S}{\sqrt{3} \times V_{\text{LL}}}$, redondeando al calibre estándar superior'),
        ('Corriente Secundaria Normalizada ($I_{sn}$)', 'Estándar $5\,\text{A}$ para cableado corto dentro de cuadro ($< 10\,\text{m}$) ; Estándar $1\,\text{A}$ para tiradas largas ($> 30\,\text{m}$) reduciendo pérdidas un $96\%$'),
        ('Cálculo de Carga Total Conectada ($S_b$)', 'Carga total en VA $S_b = I_{sn}^2 \times (2 \times R_{\text{cables}} + R_{\text{instrumento}} + R_{\text{contacto}})$, con $R_{\text{cables}} = \rho \times \frac{L}{S}$'),
        ('Fórmula de Tensión de Codo de Protección ($V_k$)', '$V_k \ge 2 \times I_{cc(\text{max})} \times \frac{I_{sn}}{I_{pn}} \times (R_{ct} + R_b)$ para prevenir saturación durante fallas asimétricas'),
        ('Clases de Precisión para Medición', 'Clase 0.2S y Clase 0.5S para medición comercial de frontera ; Clase 0.5 y 1.0 para amperímetros y analizadores bajo IEC 61869-2'),
        ('Clases de Precisión para Protección', 'Clase 5P10 y 5P20: Error compuesto $\le 5\%$ a $10\times$ o $20\times$ la corriente nominal de cortocircuito asignada'),
        ('Factor de Seguridad de Instrumentos ($FS$)', '$FS \le 5$ o $FS \le 10$: Asegura la saturación controlada del núcleo en cortocircuito para proteger medidores digitales'),
        ('Capacidad Térmica de Cortocircuito ($I_{th}$)', 'Corriente térmica de cortocircuito $I_{th} \ge 80 \times I_{pn}$ durante $1.0\,\text{s}$ o $3.0\,\text{s}$ según norma IEC 61869-1')
    ],
    faqs=[
        ('¿Cómo se calcula la corriente primaria nominal de un Transformador de Corriente (TC)?',
         'Para calcular el primario nominal ($I_{pn}$) : '
         '<ol>'
         '<li><strong>Calcular la corriente a plena carga ($I_{\text{FLC}}$) :</strong> '
         'En trifásico : $I_{\text{FLC}} = \frac{P_{\text{kVA}} \times 1000}{\sqrt{3} \times V_{\text{L-L}}}$. Para un transformador de $2000\,\text{kVA}$ en $11\,\text{kV}$ : $I_{\text{FLC}} \approx 105\,\text{A}$.</li>'
         '<li><strong>Aplicar factor de sobrecarga continua ($1.25\times$) :</strong> '
         '$I_{\text{objetivo}} = 1.25 \times 105\,\text{A} = 131.2\,\text{A}$.</li>'
         '<li><strong>Seleccionar el calibre comercial normalizado :</strong> Seleccionar un TC de <strong>150/5A</strong> o <strong>150/1A</strong>.</li>'
         '</ol>'),
        ('¿Por qué elegir un secundario de 1A en lugar de 5A para cables de gran longitud?',
         'La potencia disipada en los cables secundarios es proporcional al cuadrado de la corriente ($P = I^2 R$). '
         'Un secundario de 5A disipa 25 veces más potencia que uno de 1A en el mismo cable. '
         'Al seleccionar 1A se reducen las pérdidas en un 96%, evitando la saturación del TC en distancias superiores a 30 metros.')
    ],
    cta='¿Diseña subestaciones eléctricas, centros de transformación o cuadros de distribución que requieren transformadores de corriente de medida (Clase 0.2S / 0.5) o de protección (Clase 5P10 / 5P20) certificados bajo IEC 61869-2? YOMIN fabrica transformadores de instrumento con curvas de saturación y tensiones de codo garantizadas.',
    body='''
<h2>La Metodología Esencial para el Dimensionamiento de Transformadores de Corriente</h2>
<p>En subestaciones eléctricas y salas de celdas de media y baja tensión, los transformadores de corriente (TC) actúan como sensores indispensables, reduciendo corrientes de miles de amperios a magnitudes seguras de 5A o 1A para alimentar relés y analizadores de potencia.</p>
<p>Un dimensionamiento incorrecto provoca graves problemas :</p>
<ul>
  <li><strong>Carga secundaria (VA) insuficiente :</strong> Origina saturación y graves errores de facturación energética.</li>
  <li><strong>Tensión de codo ($V_k$) insuficiente en protección :</strong> El núcleo se satura en cortocircuitos, impidiendo el disparo de las protecciones y quemando las barras colectoras.</li>
</ul>
<p>Esta guía técnica desglosa paso a paso las fórmulas matemáticas requeridas para dimensionar la relación de transformación, la carga en VA y la tensión de codo bajo la norma <strong>IEC 61869-2</strong>.</p>
'''
)

CT_CALC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='substation-engineering-current-transformer-sizing-calculation-ar',
    title='هندسة المحطات الكهربائية: دليل حساب واختيار سعة محول التيار (Current Transformer Sizing Calculation)',
    breadcrumb='هندسة المحطات وحسابات محولات التيار',
    read='11 دقيقة قراءة',
    alt='مقصورة قواطع الجهد المتوسط في محطة كهربائية تحتوي على ثلاثة محولات تيار مصبوبة براتنج الإيبوكسي 24kV أثناء اختبارات الحقن الثانوي',
    desc=('هندسة لوحات التوزيع وقواطع الجهد المتوسط، وتنسيق مرحلات الحماية، ومنظومات القياس: كيفية إجراء حسابات واختيار محول التيار (CT Sizing Calculation). '
          'المعادلات الرياضية لحساب تيار الحمل الكامل ($I_p$)، والمقارنة بين خرج 5A و 1A، وحساب حمل الأسلاك (Burden VA)، وجهد نقطة الانقلاب للتشبع ($V_k$) وفقاً للمواصفة القياسية الدولية IEC 61869-2.'),
    model='سلاسل MSQ و RCT و AK و BH-0.66: محولات تيار القياس والحماية من 0.66kV إلى 35kV (دقة فئة 0.2S و 0.5 و 5P10 و 5P20، خرج ثانوي 1A/5A، معتمدة وفقاً لـ IEC 61869-2 و IEEE C57.13)',
    category='هندسة المحطات وحسابات محولات التيار / محولات القياس والحماية الكهربائية',
    kw='حسابات محول التيار &middot; ct sizing calculation &middot; حساب نسبة تحويل محول التيار &middot; ct burden calculation &middot; جهد ركبة التشبع vk &middot; تشبع محول التيار ct saturation &middot; iec 61869-2',
    specs=[
        ('معادلة تيار الابتدائي المقنن ($I_{pn}$)', 'تحسب وفق المعادلة $I_{pn} \ge 1.25 \times I_{\text{FLC}}$، حيث $I_{\text{FLC}} = \frac{S}{\sqrt{3} \times V_{\text{LL}}}$ مع التقريب للقيمة القياسية التالية'),
        ('التيار الثانوي المقنن للقياس ($I_{sn}$)', 'معياري $5\,\text{A}$ للمسافات القصيرة داخل اللوحة ($< 10\,\text{m}$)؛ ومعياري $1\,\text{A}$ للمسافات الطويلة ($> 30\,\text{m}$) لتقليل فواقد الأسلاك بنسبة $96\%$'),
        ('حساب الحمل الكلي الموصل ($S_b$)', 'الحمل الكلي بالفولت أمبير $S_b = I_{sn}^2 \times (2 \times R_{\text{leads}} + R_{\text{meter}} + R_{\text{contact}})، حيث $R_{\text{leads}} = \rho \times \frac{L}{A}$'),
        ('معادلة جهد ركبة التشبع للحماية ($V_k$)', '$V_k \ge 2 \times I_{f(\text{max})} \times \frac{I_{sn}}{I_{pn}} \times (R_{ct} + R_b)$ لمنع التشبع المغناطيسي أثناء تيار القصر الأقصى'),
        ('فئات دقة القياس المعتمدة', 'فئة 0.2S و 0.5S لقياس الطاقة الرسمي للشبكات؛ وفئة 0.5 و 1.0 لأجهزة قياس اللوحات وفقاً لمعيار IEC 61869-2'),
        ('فئات دقة الحماية والمرحلات', 'فئة 5P10 و 5P20: نسبة الخطأ المركب $\le 5\%$ عند مرور $10\times$ أو $20\times$ ضعف تيار القصر المقنن للمرحلات التفاضلية وزيادة التيار'),
        ('معامل أمان الأجهزة ($FS$)', '$FS \le 5$ أو $FS \le 10$: يضمن تشبع القلب المغناطيسي بسرعة عند حدوث قصر لحماية العدادات الرقمية الحساسة من الاحتراق'),
        ('تحمل تيار القصر الحراري ($I_{th}$)', 'تيار التحمل الحراري المقنن $I_{th} \ge 80 \times I_{pn}$ لمدة $1.0\,\text{s}$ أو $3.0\,\text{s}$ طبقاً للمواصفة IEC 61869-1')
    ],
    faqs=[
        ('ما هي المعادلة الرياضية لحساب تيار الابتدائي المقنن لمحول التيار؟',
         'لحساب تيار الابتدائي المقنن ($I_{pn}$) يتم اتباع الخطوات الهندسية التالية: '
         '<ol>'
         '<li><strong>حساب تيار الحمل الكامل ($I_{\text{FLC}}$):</strong> '
         'للأنظمة ثلاثية الأوجه: $I_{\text{FLC}} = \frac{P_{\text{kVA}} \times 1000}{\sqrt{3} \times V_{\text{LL}}}$. على سبيل المثال لمحطة $2000\,\text{kVA}$ بجهد $11\,\text{kV}$ يكون التيار حوالي $105\,\text{A}$.</li>'
         '<li><strong>تطبيق معامل الأمان للأحمال المستقبلية ($1.25\times$):</strong> '
         '$I_{\text{target}} = 1.25 \times 105\,\text{A} = 131.2\,\text{A}$.</li>'
         '<li><strong>اختيار السعة القياسية التجارية:</strong> اختيار محول تيار <strong>150/5A</strong> أو <strong>150/1A</strong>.</li>'
         '</ol>'),
        ('لماذا يفضل اختيار خرج ثانوي 1A بدلاً من 5A في الكابلات الطويلة؟',
         'تتناسب القدرة المفقودة في أسلاك التوصيل طردياً مع مربع التيار ($P = I^2 R$). '
         'عند استخدام خرج 5A تكون الفواقد $25 \times R$، بينما عند استخدام خرج 1A تكون الفواقد $1 \times R$ فقط. '
         'هذا يعني أن اختيار خرج 1A يقلل فواقد الأسلاك بنسبة 96%، مما يسمح بمد كابلات المحول لمسافات تتجاوز مئات الأمتار دون تحميل المحول فوق طاقته أو التسبب في تشبعه.')
    ],
    cta='هل تعمل على تصميم محطات التحويل الكهربائية، أو لوحات قواطع الجهد المتوسط والمنخفض التي تتطلب محولات تيار قياس بدقة فئة 0.2S / 0.5 أو محولات حماية فئة 5P10 / 5P20 معتمدة دولياً؟ تصنع يمين (YOMIN) محولات تيار متطورة بمطابقة كاملة للمواصفة القياسية IEC 61869-2.',
    body='''
<h2>المنهجية الهندسية الدقيقة لحساب واختيار سعات محولات التيار في الشبكات الكهربائية</h2>
<p>في المحطات الكهربائية ولوحات قواطع التوزيع الرئيسية، تشكل محولات التيار (محولات القياس والحماية) حجر الزاوية للمراقبة والحماية؛ حيث تقوم بتخفيض التيارات العالية التي تصل إلى آلاف الأمبيرات إلى قيم آمنة وموحدة (5 أمبير أو 1 أمبير) لتغذية العدادات ومرحلات الحماية الرقمية الحديثة.</p>
<p>ويؤدي الخطأ في حسابات محول التيار إلى مخاطر تشغيلية جسيمة في المنظومة الكهربائية:</p>
<ul>
  <li><strong>نقص حمل الفولت أمبير المقنن:</strong> يؤدي إلى تشبع مغناطيسي مستمر للقلب الحديدي وحدوث أخطاء فادحة في قراءة فواتير استهلاك الطاقة الكهربائية، مما يسبب خسائر مالية فادحة للمنشآت والمصانع.</li>
  <li><strong>نقص جهد ركبة التشبع في محولات الحماية:</strong> يؤدي إلى تشبع المحول أثناء مرور تيار القصر العالي، مما يمنع مرحلات الحماية من استشعار العطل وفصل القاطع، وهو ما قد ينتهي بانفجار لوحة التوزيع وتدمير المعدات.</li>
</ul>
<p>يوضح هذا الدليل الهندسي الشامل الخطوات المعتمدة والمعادلات الرياضية لحساب سعة وتيار الابتدائي، واختيار الخرج الثانوي المناسب، وحساب أحمال الأسلاك وجهد التشبع وفقاً للمواصفة القياسية الدولية المعتمدة.</p>

<h2>خطوات الحساب الهندسي لاختيار محول التيار المناسب</h2>
<ol>
  <li><strong>الخطوة الأولى - حساب تيار الابتدائي:</strong> يتم حساب تيار الحمل الكامل للمعدة أو المحول المغذى بالاعتماد على القدرة الاسمية والجهد، ثم يتم ضرب الناتج في معامل أمان قدره 1.25 لاستيعاب التوسعات المستقبلية والأحمال الزائدة المستمرة، ثم اختيار السعة القياسية التجارية الأعلى مباشرة.</li>
  <li><strong>الخطوة الثانية - المفاضلة بين خرج 5 أمبير و 1 أمبير:</strong> يتم قياس المسافة الفعلية لكابلات التوصيل بين محول التيار وغرفة التحكم؛ فإذا تجاوزت المسافة ثلاثين متراً، يجب اختيار خرج ثانوي مقداره 1 أمبير لتقليل فواقد القدرة في الأسلاك بنسبة 96% وتجنب زيادة الحمل على المحول.</li>
  <li><strong>الخطوة الثالثة - حساب الحمل الكلي الموصل بالفولت أمبير:</strong> يتم جمع مقاومة أسلاك التوصيل ذهاباً وإياباً مع المقاومة الداخلية لعداد القياس أو مرحل الحماية ومقاومة نقاط التلامس، مع التأكد من أن الحمل الكلي يقع دائماً بين 25% و 100% من السعة المقننة للمحول للحفاظ على دقة القياس.</li>
  <li><strong>الخطوة الرابعة - التحقق من جهد ركبة التشبع لمحولات الحماية:</strong> بالنسبة لمحولات الحماية، يجب التأكد من قدرة المحول على توليد قوة دافعة كهربائية كافية عند مرور أقصى تيار قصر متوقع دون الدخول في مرحلة التشبع المغناطيسي قبل إتمام فصل الدائرة بأمان تام.</li>
</ol>

<h2>مقارنة هندسية شاملة بين محولات القياس ومحولات الحماية</h2>
<p>تختلف محولات تيار القياس عن محولات تيار الحماية في الخصائص المغناطيسية وسلوك التشبع؛ حيث تصمم محولات القياس بدقة متناهية في نطاق التشغيل الطبيعي مع التشبع السريع عند الأعطال لحماية العدادات، بينما تصمم محولات الحماية للحفاظ على الخطية المغناطيسية حتى عند مرور تيارات قصر تعادل عشرين ضعف التيار الاسمي لضمان عمل أجهزة الوقاية بكفاءة مطلقة.</p>
'''
)

# ==============================================================================
# 2. PREPAID VS POSTPAID ELECTRICITY (EN, FR, ES, AR)
# ==============================================================================

PRE_POST_EN = dict(
    lang='en',
    dir='ltr',
    slug='utility-metering-difference-between-prepaid-and-postpaid-electricity',
    title='Utility Metering: Difference Between Prepaid and Postpaid Electricity',
    breadcrumb='Utility Metering &amp; Prepaid vs Postpaid Electricity',
    read='10 min read',
    alt='Apartment electrical room wall installation comparing an STS keypad prepaid smart electricity meter side by side with a legacy postpaid meter',
    desc=('Power utilities, commercial property managers, and municipal energy distribution: What is the exact difference between prepaid and postpaid electricity? '
          'How STS 20-digit token encryption, split Customer Interface Units (CIU), zero utility bad-debt collection, real-time energy budgeting, and anti-tamper hardware revolutionize revenue protection under IEC 62055-41.'),
    model='Model DDSY & DTSY Series STS Compliant Single-Phase and Three-Phase Keypad Prepaid Energy Meters (20-Digit Token Recharge, Split CIU Interface, Anti-Tamper Optical Detection, IEC 62055-41 & IEC 62053-21)',
    category='Utility Metering & Prepaid vs Postpaid Electricity / Smart Energy Meters',
    kw='difference between prepaid and postpaid electricity &middot; prepaid vs postpaid meter &middot; what is a prepaid meter &middot; postpaid meter &middot; prepaid electricity meter &middot; sts prepaid meter &middot; revenue protection',
    specs=[
        ('Revenue Collection & Payment Principle', 'Prepaid: Upfront payment before consumption (100% debt-free utility revenue) vs Postpaid: Delayed billing 30–60 days after consumption with collection risk'),
        ('STS 20-Digit Token Encryption Standard', 'Standard Transfer Specification (IEC 62055-41 / 51): Highly secure cryptographic 20-digit numerical tokens generated at utility vending stations'),
        ('Split Architecture & Anti-Tamper Security', 'Split unit: Measurement Control Unit (MCU) installed in secure pole-top/stairwell enclosure; Customer Interface Unit (CIU) placed inside home via PLC/RF'),
        ('Billing Dispute & Meter Reading Labor', 'Prepaid: Zero manual meter reading labor; zero estimated billing disputes vs Postpaid: Requires manual meter readers, estimated billing reconciliations, and debt collection teams'),
        ('Load Limiting & Disconnection Mechanism', 'Prepaid: High-reliability internal 60A/80A/100A bistable magnetic latching relay disconnects power instantly when credit reaches zero; auto-reconnects on recharge'),
        ('Consumer Budget Control & Monitoring', 'Prepaid: Real-time LCD display showing remaining kWh balance, monetary credit, current power draw (kW), and audible low-credit warning beepers'),
        ('Emergency Credit & Friendly Hours Mode', 'Software programmable friendly hours (e.g. weekends, holidays, nighttime non-disconnection) and emergency credit overdraft for enhanced consumer satisfaction'),
        ('International Manufacturing Safety Compliance', 'Fully tested and compliant with IEC 62055-41, IEC 62055-51, IEC 62053-21 Class 1.0, and utility revenue protection grid codes')
    ],
    faqs=[
        ('What is the fundamental operational difference between prepaid electricity and postpaid electricity?',
         'The core difference lies in the financial transaction sequence and risk ownership: '
         '<ul>'
         '<li><strong>Prepaid Electricity:</strong> The consumer pays for electricity in advance. When purchasing credit, the utility vending system '
         'generates a secure 20-digit Standard Transfer Specification (STS) token. The consumer enters this token into the meter\'s keypad. '
         'The meter credits the kilowatt-hours and continuously counts down as appliances consume power. If credit drops to zero, an internal '
         'magnetic latching relay automatically disconnects the supply. The utility receives <strong>100% upfront cash flow with zero bad debt</strong>.</li>'
         '<li><strong>Postpaid Electricity:</strong> The consumer consumes electricity freely for a billing cycle (usually 30 days). At month-end, '
         'a utility meter reader physically visits the premises to record the index, or data is captured remotely. The utility prints and mails an invoice. '
         'The consumer has 15 to 30 days to pay. The utility bears massive financial working-capital strain, unmetered non-technical losses, estimated billing disputes, and unpaid arrears.</li>'
         '</ul>'),
        ('Why are power utilities and landlords rapidly migrating to STS Prepaid Meters?',
         'Utilities and commercial property managers migrate to prepaid metering to solve three critical operational bottlenecks: '
         '<ul>'
         '<li><strong>Elimination of Bad Debts and Arrears:</strong> Upfront token purchasing guarantees zero non-payment. In multi-tenant shopping centers and residential apartments, '
         'landlords never have to pursue absconded tenants for unpaid utility bills.</li>'
         '<li><strong>Drastic Reduction in Operational Overhead:</strong> Eliminates armies of manual meter readers, billing print/mail costs, and contentious legal disconnection disputes.</li>'
         '<li><strong>Automated Energy Conservation:</strong> When consumers visibly see their credit countdown on their indoor Customer Interface Unit (CIU), '
         'they voluntarily reduce waste by turning off idle air conditioners and lights, lowering peak grid demand by 10% to 15%.</li>'
         '</ul>'),
        ('How does a Split Prepaid Meter (MCU + CIU) prevent electricity theft and tampering?',
         'In traditional integrated prepaid meters, the entire unit is inside the tenant\'s home, making it vulnerable to magnetic tampering, bypass jumpers, or neutral disconnection. '
         'A <strong>Split Prepaid Meter</strong> separates the system into two distinct units: '
         '<ul>'
         '<li><strong>Measurement Control Unit (MCU):</strong> The actual revenue meter and disconnect relay are locked inside a tamper-evident polycarbonate enclosure '
         'mounted high on an outdoor utility pole or in a locked basement electrical switch room. Consumers have zero physical access to the power conductors.</li>'
         '<li><strong>Customer Interface Unit (CIU):</strong> A convenient tactile keypad and display unit installed inside the consumer\'s living room. '
         'The CIU communicates with the outdoor MCU via existing mains power lines (Power Line Carrier - PLC) or wireless Radio Frequency (RF), allowing tenants to enter recharge tokens comfortably without touching live wires.</li>'
         '</ul>')
    ],
    cta='Managing power utility networks, municipal electrification projects, commercial shopping plazas, or multi-tenant residential communities seeking to eliminate unpaid electricity arrears and automate revenue collection? YOMIN manufactures certified STS prepayment single-phase and three-phase smart keypad meters and split CIU systems under IEC 62055-41.',
    body='''
<h2>The Global Shift: Transforming Power Distribution from Invoicing to Prepayment</h2>
<p>Across the global power industry, electricity distributors, municipal utilities, and commercial real estate landlords face a relentless challenge: non-technical losses, overdue billing arrears, meter tampering, and protracted payment disputes that cripple financial cash flow.</p>
<p>For over a century, traditional <strong>postpaid electricity metering</strong> was the standard: consume first, inspect meters later, bill monthly, and chase payments. However, in modern smart grid architectures, this lagging financial model is being rapidly superseded by <strong>STS prepaid electricity metering</strong>.</p>
<p>This technical comparison analyzes the structural, financial, operational, and anti-tamper differences between prepaid and postpaid electricity, detailing why utility grid operators worldwide are standardizing on <strong>Standard Transfer Specification (STS)</strong> prepayment systems under <strong>IEC 62055-41</strong>.</p>

<h2>Detailed Comparison: Prepaid Electricity vs. Postpaid Electricity</h2>
<table>
  <thead>
    <tr>
      <th>Operational Dimension</th>
      <th>Legacy Postpaid Electricity</th>
      <th>Smart STS Prepaid Electricity (YOMIN DDSY/DTSY)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Cash Flow Timing</strong></td>
      <td><strong>Lagging (30 to 90 Days):</strong> Utility provides energy on credit; revenue arrives months after generation costs.</td>
      <td><strong>Immediate Upfront Cash Flow:</strong> Utility receives 100% payment before electricity is generated and consumed.</td>
    </tr>
    <tr>
      <td><strong>Bad Debt &amp; Default Risk</strong></td>
      <td>High: Tenants abscond with unpaid utility bills; unpaid arrears require costly litigation and physical disconnection crews.</td>
      <td><strong>Zero Bad Debt:</strong> Meter automatically disconnects supply via internal latching relay when credit reaches zero.</td>
    </tr>
    <tr>
      <td><strong>Meter Reading Overhead</strong></td>
      <td>Labor-intensive: Requires physical inspection visits by meter readers; prone to human recording errors and estimated bills.</td>
      <td><strong>Zero Routine Labor:</strong> Consumers purchase numerical tokens online, via mobile banking, or at vending kiosks.</td>
    </tr>
    <tr>
      <td><strong>Anti-Tamper Architecture</strong></td>
      <td>Vulnerable: Meters mounted inside consumer premises can be bypassed with neutral jumpers or magnetic interference.</td>
      <td><strong>Split Anti-Tamper Security:</strong> Meter (MCU) locked in secure outdoor enclosure; tenant interacts via remote wireless CIU.</td>
    </tr>
    <tr>
      <td><strong>Consumer Engagement</strong></td>
      <td>Passive: Consumers only see total usage at month-end, leading to "bill shock" and complaints.</td>
      <td><strong>Active Awareness:</strong> Real-time display of remaining kWh balance encourages voluntary energy conservation.</td>
    </tr>
  </tbody>
</table>
'''
)

PRE_POST_FR = dict(
    lang='fr',
    dir='ltr',
    slug='utility-metering-difference-between-prepaid-and-postpaid-electricity-fr',
    title='Comptage d\'Énergie : Différence entre Électricité Prépayée et Postpayée',
    breadcrumb='Comptage Électrique &amp; Prépayé vs Postpayé',
    read='10 min de lecture',
    alt='Local technique électrique d\'immeuble comparant côte à côte un compteur d\'électricité prépayé communicant STS à clavier et un compteur postpayé traditionnel',
    desc=('Distributeurs d\'électricité, gestionnaires d\'immeubles tertiaires et régies municipales : Quelle est la différence exacte entre électricité prépayée et postpayée ? '
          'Cryptage des jetons STS à 20 chiffres, boîtiers déportés (CIU), élimination des impayés, suivi budgétaire en temps réel et sécurité anti-fraude selon CEI 62055-41.'),
    model='Séries DDSY & DTSY : Compteurs d\'Énergie Prépayés STS Monophasés et Triphasés à Clavier (Recharge par Jetons 20 Chiffres, Boîtier Client Déporté CIU, Anti-Fraude Optique, Conforme CEI 62055-41 et CEI 62053-21)',
    category='Comptage Électrique & Prépayé vs Postpayé / Compteurs d\'Énergie Intelligents',
    kw='difference electricite prepayee et postpayee &middot; compteur prepaye vs postpaye &middot; quest ce quun compteur prepaye &middot; compteur a jeton sts &middot; compteur a clavier &middot; anti-fraude electricite &middot; cei 62055-41',
    specs=[
        ('Principe de Facturation et Recouvrement', 'Prépayé : Paiement préalable avant consommation (zéro impayé pour le distributeur) vs Postpayé : Facturation mensuelle à terme échu avec risque de défaut'),
        ('Standard de Cryptage des Jetons STS', 'Standard Transfer Specification (CEI 62055-41 / 51) : Jetons numériques à 20 chiffres hautement sécurisés générés en station de vente'),
        ('Architecture Split Anti-Fraude', 'Système séparé : Unité de comptage (MCU) installée en coffret extérieur sécurisé ; Boîtier d\'interface client (CIU) placé dans le logement via CPL/RF'),
        ('Coûts de Relève et Litiges Factures', 'Prépayé : Aucune relève manuelle sur site ; zéro litige de facture estimée vs Postpayé : Nécessite des agents releveurs et des contentieux de recouvrement'),
        ('Mécanisme de Coupure Automatique', 'Prépayé : Relais bistable magnétique interne 60A/80A/100A coupant automatiquement l\'alimentation à solde nul et réarmant dès la recharge'),
        ('Contrôle Budgétaire Consommateur', 'Prépayé : Écran LCD affichant en temps réel le crédit restant en kWh et en monnaie, avec alarme sonore de fin de crédit'),
        ('Crédit d\'Urgence et Heures de Grâce', 'Fonctionnement paramétrable d\'heures de grâce (pas de coupure la nuit, week-ends ou jours fériés) et crédit d\'urgence de dépannage'),
        ('Normes Internationales et Conformité', 'Entièrement certifié et conforme aux normes CEI 62055-41, CEI 62055-51 et CEI 62053-21 Classe 1.0')
    ],
    faqs=[
        ('Quelle est la différence fondamentale entre électricité prépayée et postpayée ?',
         'La différence majeure réside dans l\'ordre du flux financier : '
         '<ul>'
         '<li><strong>Électricité Prépayée :</strong> Le client achète son énergie à l\'avance sous forme d\'un jeton sécurisé STS à 20 chiffres. '
         'Le compteur décompte les kilowattheures au fur et à mesure. Si le crédit atteint zéro, le courant est automatiquement interrompu. '
         'Le gestionnaire encaisse <strong>100% de ses recettes d\'avance sans aucun impayé</strong>.</li>'
         '<li><strong>Électricité Postpayée :</strong> Le client consomme librement pendant un mois. Le gestionnaire relève le compteur, '
         'envoie une facture, et accorde un délai de paiement. Le distributeur subit des retards d\'encaissement et des risques d\'impayés.</li>'
         '</ul>')
    ],
    cta='Vous êtes une compagnie d\'électricité, une régie municipale ou un gestionnaire immobilier cherchant à éradiquer les impayés et automatiser la facturation d\'énergie ? YOMIN fabrique des compteurs intelligents prépayés STS monophasés et triphasés conformes à la norme CEI 62055-41.',
    body='''
<h2>La Révolution du Comptage : Passer de la Facturation Tradive au Prépaiement Sécurisé</h2>
<p>Partout dans le monde, les compagnies d\'électricité et les gestionnaires de parcs immobiliers sont confrontés au fardeau des factures impayées, des fraudes sur compteurs et des contestations de facturation.</p>
<p>Le système <strong>postpayé traditionnel</strong> est aujourd\'hui supplanté par le <strong>comptage prépayé STS (Standard Transfer Specification)</strong>, qui garantit un recouvrement immédiat des recettes et une maîtrise totale de la consommation d\'énergie.</p>
<p>Ce dossier technique détaille les différences clés entre électricité prépayée et postpayée selon la norme internationale <strong>CEI 62055-41</strong>.</p>
'''
)

PRE_POST_ES = dict(
    lang='es',
    dir='ltr',
    slug='utility-metering-difference-between-prepaid-and-postpaid-electricity-es',
    title='Medición de Energía: Diferencia entre Electricidad Prepago y Pospago',
    breadcrumb='Medición de Energía &amp; Prepago vs Pospago',
    read='10 min de lectura',
    alt='Cuadro eléctrico de edificio comparando lado a lado un medidor inteligente prepago STS con teclado y un medidor pospago convencional',
    desc=('Empresas distribuidoras de energía, administradores de fincas y centros comerciales: ¿Cuál es la diferencia exacta entre electricidad prepago y pospago? '
          'Cifrado de tokens STS de 20 dígitos, interfaz de usuario remota (CIU), eliminación de morosidad, control de presupuesto en tiempo real y protección antifraude bajo IEC 62055-41.'),
    model='Series DDSY & DTSY: Medidores de Energía Prepago STS Monofásicos y Trifásicos con Teclado (Recarga por Token de 20 Dígitos, Interfaz Dividida CIU, Detección Antifraude, IEC 62055-41 e IEC 62053-21)',
    category='Medición de Energía & Prepago vs Pospago / Medidores de Energía Inteligentes',
    kw='diferencia entre electricidad prepago y pospago &middot; medidor prepago vs pospago &middot; que es un medidor prepago &middot; medidor con token sts &middot; medidor con teclado &middot; antifraude electrico &middot; iec 62055-41',
    specs=[
        ('Principio de Cobro y Flujo de Caja', 'Prepago: Pago por adelantado antes del consumo (flujo de caja garantizado sin morosidad) vs Pospago: Facturación mensual vencida con riesgo de impago'),
        ('Estándar de Encriptación de Tokens STS', 'Standard Transfer Specification (IEC 62055-41 / 51): Tokens numéricos de 20 dígitos de alta seguridad generados en terminales de venta'),
        ('Arquitectura Dividida Split Antifraude', 'Sistema modular: Unidad de medida y corte (MCU) en caja exterior sellada ; Unidad de interfaz de cliente (CIU) en el interior del inmueble vía PLC/RF'),
        ('Costes de Lectura y Conflictos de Factura', 'Prepago: Cero lectura manual en campo ; cero reclamos por consumo estimado vs Pospago: Requiere cuadrillas de lectura y gestión de cobranzas'),
        ('Mecanismo de Desconexión Automática', 'Prepago: Relé magnético biestable interno de 60A/80A/100A que corta el suministro al agotarse el saldo y reconecta al recargar'),
        ('Control de Consumo para el Usuario', 'Prepago: Pantalla LCD con saldo remanente en kWh e importe, con alarma sonora de bajo saldo para evitar cortes accidentales'),
        ('Crédito de Emergencia y Horas de Gracia', 'Funciones programables de horas amigables (sin corte nocturno o en festivos) y crédito de emergencia configurable'),
        ('Normativas Internacionales de Fabricación', 'Totalmente probado y certificado según normas IEC 62055-41, IEC 62055-51 e IEC 62053-21 Clase 1.0')
    ],
    faqs=[
        ('¿Cuál es la diferencia fundamental entre electricidad prepago y pospago?',
         'La diferencia radica en el momento del pago y la gestión del riesgo : '
         '<ul>'
         '<li><strong>Electricidad Prepago:</strong> El usuario abona el servicio antes de consumir mediante un código numérico STS de 20 dígitos. '
         'El medidor descuenta la energía consumida y corta el paso si el saldo llega a cero. La distribuidora asegura el <strong>100% del cobro sin morosidad</strong>.</li>'
         '<li><strong>Electricidad Pospago:</strong> El usuario consume libremente durante un mes y abona la factura posteriormente, asumiendo la distribuidora el riesgo de impago.</li>'
         '</ul>')
    ],
    cta='¿Administra redes eléctricas municipales, proyectos de electrificación o propiedades en alquiler y desea erradicar la morosidad automatizando la recaudación? YOMIN fabrica medidores prepago STS certificados bajo norma IEC 62055-41.',
    body='''
<h2>La Evolución del Suministro Eléctrico : Del Modelo Pospago Tradicional al Prepago Digital</h2>
<p>Para las compañías distribuidoras de electricidad y administradores de inmuebles, la gestión de cobro de facturas y los impagos representan un reto financiero constante.</p>
<p>El <strong>sistema prepago inteligente STS</strong> revoluciona el sector al exigir el pago anticipado de la energía, empoderando al usuario y asegurando el flujo de caja operativo.</p>
<p>Este informe compara en detalle ambos modelos bajo los estándares internacionales <strong>IEC 62055-41</strong>.</p>
'''
)

PRE_POST_AR = dict(
    lang='ar',
    dir='rtl',
    slug='utility-metering-difference-between-prepaid-and-postpaid-electricity-ar',
    title='قياس استهلاك الطاقة: الفرق بين الكهرباء مسبقة الدفع والكهرباء آجلة الدفع (Prepaid vs Postpaid)',
    breadcrumb='قياس الطاقة &amp; مسبق الدفع مقابل آجل الدفع',
    read='10 دقائق قراءة',
    alt='لوحة عدادات كهربائية داخل مبنى توضح مقارنة مباشرة بين عداد كهرباء ذكي مسبق الدفع طراز STS بلوحة مفاتيح وعداد آجل الدفع تقليدي',
    desc=('شركات توزيع الكهرباء، وإدارات المجمعات التجارية، والمباني السكنية: ما هو الفرق الحقيقي بين الكهرباء مسبقة الدفع وآجلة الدفع؟ '
          'تشفير أكواد STS المكونة من 20 رقماً، ووحدات واجهة المستهلك المنفصلة (CIU)، والقضاء التام على ديون وفواتير الكهرباء المعدومة، والرقابة الفورية على الاستهلاك وفقاً للمواصفة IEC 62055-41.'),
    model='سلاسل DDSY و DTSY: عدادات الطاقة الكهربائية الذكية مسبقة الدفع بنظام كود STS أحادية وثلاثية الأوجه (شحن بكود 20 رقماً، واجهة عميل منفصلة CIU، حماية ضد التلاعب، معتمدة IEC 62055-41 و IEC 62053-21)',
    category='قياس الطاقة & مسبق الدفع مقابل آجل الدفع / عدادات الكهرباء الذكية',
    kw='الفرق بين الكهرباء مسبقة الدفع واجلة الدفع &middot; عداد مسبق الدفع vs عداد فاتورة &middot; ما هو العداد مسبق الدفع &middot; عداد كارت كهرباء &middot; عداد كود sts &middot; منع سرقة الكهرباء &middot; iec 62055-41',
    specs=[
        ('مبدأ تحصيل الإيرادات ودورة السداد', 'مسبق الدفع: سداد مسبق قبل الاستهلاك (إيرادات مضمونة بنسبة 100% دون أي ديون معدومة) مقابل آجل الدفع: فواتير شهرية متأخرة مع مخاطر التعثر'),
        ('معيار تشفير أكواد الشحن STS القياسي', 'معيار نقل البيانات الموحد (IEC 62055-41 / 51): أكواد رقمية مشفرة عالية الأمان من 20 رقماً تصدر عبر محطات البيع الرسمية'),
        ('بنية النظام المنفصل (Split Unit) لمنع التلاعب', 'نظام مزدوج: وحدة القياس والتحكم (MCU) محكمة الإغلاق خارج المبنى؛ ووحدة واجهة العميل (CIU) داخل الشقة عبر خطوط الكهرباء PLC/RF'),
        ('تكاليف قراءة العدادات والنزاعات', 'مسبق الدفع: لا حاجة لزيارات قراءة العدادات اليدوية؛ انعدام نزاعات الفواتير التقديرية مقابل آجل الدفع: تكاليف قراء وتحصيل ونزاعات قضائية'),
        ('آلية الفصل وإعادة التوصيل التلقائية', 'مسبق الدفع: مرحل مغناطيسي داخلي معتمد 60A/80A/100A يفصل الكهرباء تلقائياً عند نفاد الرصيد ويعيدها فور شحن الكود'),
        ('مراقبة وإدارة ميزانية الاستهلاك للمستهلك', 'مسبق الدفع: شاشة LCD تعرض الرصيد المتبقي بالكيلوواط/ساعة والمبلغ المالي، مع تنبيه صوتي عند انخفاض الرصيد'),
        ('خاصية الرصيد الاحتياطي وساعات الأمان', 'برمجة ذكية لمنع فصل التيار خلال ساعات الليل أو العطلات الأسبوعية والرسمية (Friendly Hours) مع إمكانية استلاف رصيد طوارئ'),
        ('شهادات الاعتماد ومطابقة المواصفات الدولية', 'مختبر ومعتمد بالكامل وفق معايير IEC 62055-41 و IEC 62055-51 و IEC 62053-21 فئة الدقة Class 1.0')
    ],
    faqs=[
        ('ما هو الفرق الجوهري بين الكهرباء مسبقة الدفع والكهرباء آجلة الدفع (الفواتير)؟',
         'يكمن الفارق الأساسي في توقيت التدفق المالي وإدارة مخاطر التحصيل: '
         '<ul>'
         '<li><strong>الكهرباء مسبقة الدفع:</strong> يشتري المستهلك رصيد الطاقة مسبقاً في صورة كود رقمي مكون من 20 رقماً مشفر بنظام STS. '
         'يقوم العداد بخصم الكيلوواط/ساعة تدريجياً. عند وصول الرصيد إلى الصفر، يفصل العداد التيار تلقائياً. '
         'تحصل شركة الكهرباء أو مالك العقار على <strong>تدفق نقدي مسبق بنسبة 100% بدون أي ديون أو متأخرات</strong>.</li>'
         '<li><strong>الكهرباء آجلة الدفع:</strong> يستهلك العميل الكهرباء بحرية لمدة شهر، ثم ترسل الشركة فاتورة بقيمة الاستهلاك. '
         'تتحمل شركة الكهرباء مخاطر تراكم الفواتير وتعثر المستهلكين وصعوبات التحصيل.</li>'
         '</ul>')
    ],
    cta='هل تدير شبكات توزيع كهربائية، أو مشاريع إسكان مجمعة، أو مراكز تجارية وترغب في القضاء التام على ديون الكهرباء المتأخرة وأتمتة التحصيل؟ تصنع يمين (YOMIN) عدادات الكهرباء الذكية مسبقة الدفع بنظام STS أحادية وثلاثية الأوجه المطابقة لمعيار IEC 62055-41.',
    body='''
<h2>التحول العالمي: الانتقال من الفواتير الآجلة إلى منظومات الدفع المسبق الذكية</h2>
<p>تواجه شركات توزيع الكهرباء والهيئات البلدية ومالكو المجمعات العقارية حول العالم تحدياً مستمراً يتمثل في تراكم الفواتير غير المحصلة، وفواقد الطاقة غير الفنية، ونزاعات قراءة العدادات التي تستنزف التدفقات النقدية.</p>
<p>لقد أصبح نظام <strong>العدادات مسبقة الدفع بنظام كود STS</strong> البديل التكنولوجي الأفضل لمنظومات الفواتير التقليدية، حيث يحقق الانضباط المالي والعدالة في استهلاك الطاقة.</p>
<p>يستعرض هذا الدليل الفني الفروق الجوهرية وميزات منظومة الدفع المسبق وفقاً للمواصفة القياسية الدولية <strong>IEC 62055-41</strong>.</p>
'''
)

ALL_MULTILINGUAL_POSTS_1020_GSC = [
    CT_CALC_EN, CT_CALC_FR, CT_CALC_ES, CT_CALC_AR,
    PRE_POST_EN, PRE_POST_FR, PRE_POST_ES, PRE_POST_AR
]
