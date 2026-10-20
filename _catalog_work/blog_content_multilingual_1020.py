# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-20:
1. MSQ Series Low-Voltage Current Transformers for Switchgear Metering (EN, FR, ES, AR)
2. DL Series Aluminum Compression Cable Lugs for Power Cable Terminations (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. MSQ CURRENT TRANSFORMER (EN, FR, ES, AR)
# ==============================================================================

MSQ_EN = dict(
    lang='en',
    dir='ltr',
    slug='switchgear-metering-what-is-an-msq-current-transformer',
    title='Switchgear Metering: What Is an MSQ Current Transformer?',
    breadcrumb='Switchgear Metering &amp; MSQ Current Transformers',
    read='10 min read',
    alt='Low-voltage electrical switchboard with three MSQ-60 series current transformers (Class 0.5) clamped over copper busbars',
    desc=('Low-voltage switchgear cabinets, motor control centers (MCC), generator panels, and commercial tenant submetering: What is an MSQ current transformer? '
          'How toroidal silicon steel cores, flame-retardant ABS/PC housings, sealable terminal covers, dual DIN-rail/busbar clamps, and IEC 61869-2 Class 0.5 accuracy transform heavy primary currents into precision metering signals.'),
    model='Model MSQ Series (MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100, MSQ-125) 0.66kV / 720V Measuring Current Transformers (Class 0.5 & Class 1.0 Accuracy, 30A to 6000A / 5A Primary Rating, Toroidal Core, Dual Mounting under IEC 61869-2)',
    category='Switchgear Metering & MSQ Current Transformers / Electrical Current Transformers',
    kw='what is an msq current transformer &middot; msq current transformer &middot; msq series current transformer &middot; measuring current transformer &middot; low voltage ct &middot; msq-30 ct &middot; msq-60 ct',
    specs=[
        ('Primary Current Rating Range ($I_{pn}$)', 'Comprehensive range from $30\,\text{A}$ up to $6000\,\text{A AC}$ primary across MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100, and MSQ-125 frame sizes'),
        ('Secondary Output Current ($I_{sn}$)', 'Standard $5\,\text{A}$ secondary output (Optional $1\,\text{A}$ secondary available for long cable run telemetry)'),
        ('Rated System & Insulation Voltage ($U_m$)', 'Rated operating voltage: $0.66\,\text{kV} / 660\,\text{V AC}$; Maximum rated continuous insulation voltage: $720\,\text{V AC}$ at $50/60\,\text{Hz}$'),
        ('Accuracy Class & Metering Performance', 'Class 0.5 (Standard utility revenue metering & high-precision power analyzers) and Class 1.0 (Standard panelboard ammeters & submetering)'),
        ('Core Material & Magnetic Annealing', 'High-permeability, low-loss grain-oriented silicon steel (CRGO) toroidal wound core; vacuum impregnated to eliminate acoustic hum and core losses'),
        ('Enclosure Polymer & Safety Protection', 'Impact-resistant flame-retardant ABS or polycarbonate (PC); self-extinguishing compliant with UL 94V-0; IP20 touch-proof terminal shrouding'),
        ('Security & Anti-Tamper Features', 'Integral clear polycarbonate transparent terminal cover with lead-seal aperture to prevent unauthorized secondary access and energy theft'),
        ('Mounting Versatility & Installation Options', 'Dual-mode mounting: Snap-on installation for standard 35mm DIN rail (EN 50022) or direct busbar clamping via insulated brass/nylon pressure screws')
    ],
    faqs=[
        ('What is an MSQ Current Transformer and why is it the global standard for low-voltage switchboard metering?',
         'An MSQ Current Transformer—frequently designated in electrical panel manufacturing as a square-type measuring CT or low-voltage window CT—is '
         'a specialized instrument transformer housed in a compact square-profile flame-retardant casing designed to step down heavy primary AC currents '
         '(from 30A up to 6000A) to a standardized, safe 5A or 1A secondary measurement current. '
         'In electrical power distribution: '
         '<ul>'
         '<li><strong>Safe Galvanic Isolation:</strong> Powers digital energy meters, power quality analyzers, and panel ammeters while isolating '
         'sensitive electronic circuitry from high-energy distribution busbars and lethal fault transients.</li>'
         '<li><strong>Class 0.5 Precision Revenue Metering:</strong> Delivers strictly regulated ratio error ($\le \pm 0.5\%$) and phase displacement error '
         'across 100% to 120% of rated current under IEC 61869-2, ensuring exact commercial tenant submetering and utility billing accuracy.</li>'
         '<li><strong>Compact Window Architecture:</strong> Designed with rectangular busbar window openings tailored to standard copper busbar dimensions '
         '(e.g., $30 \times 10\,\text{mm}$ in MSQ-30, $60 \times 20\,\text{mm}$ in MSQ-60, up to $125 \times 50\,\text{mm}$ in MSQ-125), allowing seamless, '
         'direct sliding over live busbars without cutting or jointing conductors.</li>'
         '</ul>'),
        ('What do the model numbers MSQ-30, MSQ-40, MSQ-60, and MSQ-85 signify?',
         'The numeric suffix in the MSQ series designation directly indicates the maximum primary copper busbar width (in millimeters) '
         'that can pass through the central window aperture: '
         '<ul>'
         '<li><strong>MSQ-30:</strong> Designed for primary currents from 30A to 300A; accommodates copper busbars up to $30 \times 10\,\text{mm}$ or cable diameters up to 30mm.</li>'
         '<li><strong>MSQ-40:</strong> Designed for primary currents from 100A to 500A; accommodates busbars up to $40 \times 10\,\text{mm}$.</li>'
         '<li><strong>MSQ-60:</strong> Designed for primary currents from 250A to 1000A; accommodates busbars up to $60 \times 20\,\text{mm}$.</li>'
         '<li><strong>MSQ-85:</strong> Designed for primary currents from 400A to 1600A; accommodates busbars up to $85 \times 30\,\text{mm}$.</li>'
         '<li><strong>MSQ-100 &amp; MSQ-125:</strong> Heavy-duty models handling 600A up to 6000A with large rectangular apertures up to $125 \times 50\,\text{mm}$.</li>'
         '</ul>'),
        ('Why is secondary open-circuit dangerous and how do MSQ transformers prevent it?',
         'Under Lenz\'s Law, the secondary current in a CT creates a demagnetizing flux that opposes the primary flux. '
         'If the secondary circuit is accidentally opened while primary current flows, the opposing flux vanishes, and the entire primary ampere-turns '
         'drive the magnetic core into deep saturation. This induces lethal peak voltage spikes exceeding 2,000V to 5,000V across secondary terminals S1-S2, '
         'presenting fatal electrocution hazards to technicians and destroying transformer insulation. '
         'MSQ transformers feature shrouded secondary screw terminals with clear sealable protective covers, allowing test switches or shorting links '
         'to be safely installed before disconnecting any meter.')
    ],
    cta='Designing low-voltage power distribution switchboards, motor control centers (MCC), commercial submetering panels, or generator synchronization enclosures requiring certified Class 0.5 / Class 1.0 MSQ series measuring current transformers (30A to 6000A, dual DIN-rail/busbar mounting, transparent sealable covers)? YOMIN manufactures precision MSQ transformers compliant with IEC 61869-2.',
    body='''
<h2>The Measurement Cornerstone for Modern Power Distribution and Energy Monitoring</h2>
<p>Inside low-voltage main distribution boards (MDB), motor control centers (MCC), commercial tenant billing switchboards, and solar power feed-in panels, electric currents reaching thousands of amperes flow through heavy copper busbars.</p>
<p>To measure, monitor, and bill this electrical energy, digital multi-function power meters, smart energy analyzers, and overload protection devices require an accurate, scaled-down replica of the primary current.</p>
<p>Direct measurement is physically impossible: connecting a digital meter directly to a 1000A busbar would require massive internal shunts, generate extreme heat, and destroy delicate microprocessor electronics during minor system overloads.</p>
<p>The <strong>MSQ Series Low-Voltage Measuring Current Transformer (Model MSQ-30 to MSQ-125)</strong> represents the globally recognized engineering standard for low-voltage switchgear metering : an ultra-compact, precision-wound toroidal instrument transformer engineered to step down heavy primary currents to standardized 5A or 1A secondary signals with Class 0.5 revenue accuracy, complete galvanic isolation, and versatile dual mounting capabilities under IEC 61869-2.</p>

<h2>Engineering Anatomy: Inside Model MSQ Measuring Current Transformers</h2>
<ol>
  <li><strong>Grain-Oriented Silicon Steel (CRGO) Toroidal Core:</strong> Precision tape-wound magnetic core annealed in vacuum furnaces to achieve ultra-high magnetic permeability and negligible hysteresis loss, ensuring perfect linear measurement even at low load currents (5% to 20% of rated $I_n$).</li>
  <li><strong>Flame-Retardant Polycarbonate/ABS Enclosure:</strong> Molded in robust, self-extinguishing plastic rated UL 94V-0, providing 3kV AC dielectric withstand protection between primary busbar and secondary terminals.</li>
  <li><strong>Versatile Dual-Mode Mounting System:</strong> Equipped with built-in metal/plastic mounting feet for standard 35mm DIN rail mounting, alongside insulated brass tightening screws that lock the transformer securely directly onto the primary copper busbar.</li>
  <li><strong>Sealable Transparent Secondary Terminal Cover:</strong> High-clarity polycarbonate cover enclosing secondary terminals S1 and S2, equipped with lead-wire sealing holes to prevent electricity theft and unauthorized meter tampering in commercial tenant billing.</li>
  <li><strong>Standardized Metric Busbar Apertures:</strong> Rectangular window profiles precisely matched to international standard copper busbar dimensions ($30 \times 10\,\text{mm}$, $40 \times 10\,\text{mm}$, $60 \times 20\,\text{mm}$, $85 \times 30\,\text{mm}$, $100 \times 40\,\text{mm}$, $125 \times 50\,\text{mm}$) for clean, uncluttered cabinet aesthetics.</li>
</ol>

<h2>Comparison: MSQ Current Transformers vs. Split-Core CTs vs. Solid Cast Resin CTs</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Metric</th>
      <th>Split-Core Current Transformer</th>
      <th>Solid Epoxy Cast Resin CT</th>
      <th>YOMIN MSQ Measuring CT (MSQ Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Accuracy Class &amp; Linearity</strong></td>
      <td>Moderate (Class 1.0–3.0): Air gap reduces magnetic permeability.</td>
      <td>High (Class 0.2–0.5): Continuous magnetic core.</td>
      <td><strong>High (Class 0.5 &amp; 1.0): Seamless toroidal CRGO core delivers revenue-grade accuracy.</strong></td>
    </tr>
    <tr>
      <td><strong>Installation in New Switchboards</strong></td>
      <td>Bulky, higher cost per unit; ideal for retrofits without power cut.</td>
      <td>Heavy and rigid; requires complex mounting brackets.</td>
      <td><strong>Optimal: Slides cleanly over busbars; snaps directly onto 35mm DIN rails.</strong></td>
    </tr>
    <tr>
      <td><strong>Acoustic Vibration &amp; Humming</strong></td>
      <td>Prone to acoustic hum if split core mating faces become dirty.</td>
      <td>Zero acoustic noise; fully encapsulated.</td>
      <td><strong>Zero Hum: Vacuum-impregnated core eliminates magnetostrictive acoustic noise.</strong></td>
    </tr>
    <tr>
      <td><strong>Revenue Anti-Tamper Sealing</strong></td>
      <td>Rarely equipped with sealable terminal covers.</td>
      <td>Terminal covers often bulky or absent.</td>
      <td><strong>Built-In Security: Clear polycarbonate sealable terminal cover prevents energy theft.</strong></td>
    </tr>
    <tr>
      <td><strong>Economics &amp; Footprint</strong></td>
      <td>High unit cost; larger physical footprint.</td>
      <td>High unit cost; heavy weight adds structural load.</td>
      <td><strong>Best Value: Ultra-compact, lightweight, cost-effective for modern switchboards.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MSQ_FR = dict(
    lang='fr',
    dir='ltr',
    slug='switchgear-metering-what-is-an-msq-current-transformer-fr',
    title='Comptage en Tableau Électrique : Qu\'est-ce qu\'un Transformateur de Courant MSQ ?',
    breadcrumb='Comptage en Tableau &amp; Transformateurs MSQ',
    read='10 min de lecture',
    alt='Tableau électrique basse tension équipé de trois transformateurs de courant série MSQ-60 (Classe 0.5) montés sur barres de cuivre',
    desc=('Tableaux de distribution basse tension (TGBT), centres de contrôle moteurs (MCC) et sous-comptage divisionnaire : Qu\'est-ce qu\'un transformateur de courant MSQ ? '
          'Noyaux toroïdaux en tôle magnétique au silicium, boîtier ABS/PC auto-extinguible, capot plombable anti-fraude, double fixation rail DIN/barre et précision Classe 0.5 sous CEI 61869-2.'),
    model='Série MSQ (MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100, MSQ-125) : Transformateurs de Courant de Mesure Basse Tension 0,66kV / 720V (Classe 0.5 & 1.0, 30A à 6000A / 5A, Conforme CEI 61869-2)',
    category='Comptage en Tableau & Transformateurs MSQ / Transformateurs de Courant Électriques',
    kw='transformateur de courant msq &middot; ti msq &middot; transformateur msq &middot; transformateur de mesure basse tension &middot; tc msq 60 &middot; tore ouvrant vs msq &middot; classe 0.5 cei 61869',
    specs=[
        ('Gamme de Courants Primaires Assignés ($I_{pn}$)', 'Large plage de $30\,\text{A}$ à $6000\,\text{A AC}$ couvrant les calibres MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100 et MSQ-125'),
        ('Courant Secondaire Assigné ($I_{sn}$)', 'Standard $5\,\text{A}$ (Version $1\,\text{A}$ disponible pour les liaisons de télémesure à grande distance)'),
        ('Tension Assignée de Service et d\'Isolement', 'Tension de réseau : $0,66\,\text{kV} / 660\,\text{V AC}$ ; Tension maximale d\'isolement permanent : $720\,\text{V AC}$ à $50/60\,\text{Hz}$'),
        ('Classe de Précision et Performances', 'Classe 0.5 (Comptage divisionnaire officiel et centrales de mesure d\'énergie) et Classe 1.0 (Ampèremètres et indicateurs de tableau)'),
        ('Matériau du Noyau Magnétique', 'Tôle d\'acier au silicium à grains orientés (CRGO) à très faibles pertes magnétiques, recuit sous vide et imprégné sous vide anti-vibration'),
        ('Enveloppe Isolante et Sécurité', 'Boîtier en ABS ou Polycarbonate (PC) haute résistance aux chocs, auto-extinguible UL 94V-0, bornes protégées IP20'),
        ('Dispositif Plombable Anti-Fraude', 'Capot transparent en polycarbonate avec œilleton pour fil de plombage interdisant tout accès non autorisé au circuit de mesure'),
        ('Polyvalence et Modes de Fixation', 'Double mode de fixation : Encliquetage direct sur rail DIN 35 mm (EN 50022) ou serrage sur barre en cuivre par vis isolées')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transformateur de Courant MSQ et pourquoi est-il le standard en tableau TGBT ?',
         'Un Transformateur de Courant MSQ (couramment appelé TI de mesure profil carré ou transformateur toroïdal à fenêtre rectangulaire) est '
         'un appareil de mesure moyenne et basse tension conçu pour abaisser de forts courants alternatifs (de 30 A à 6000 A) '
         'en un courant secondaire normalisé de 5 A ou 1 A mesurable en toute sécurité par les centrales de mesure et compteurs d\'énergie. '
         'Dans la distribution électrique : '
         '<ul>'
         '<li><strong>Sécurité et Isolement Galvanique :</strong> Isole complètement les appareils électroniques sensibles de la puissance brute du jeu de barres.</li>'
         '<li><strong>Précision Certifiée Classe 0.5 :</strong> Garantit une erreur de rapport inférieure à ±0,5% pour une facturation d\'énergie exacte.</li>'
         '<li><strong>Fenêtre Rectangulaire Traversante :</strong> S\'adapte exactement aux dimensions normalisées des barres en cuivre sans devoir sectionner les conducteurs.</li>'
         '</ul>'),
        ('Que signifient les désignations MSQ-30, MSQ-40, MSQ-60 et MSQ-85 ?',
         'Le chiffre indique la largeur maximale (en millimètres) de la barre en cuivre qui peut traverser la fenêtre : '
         '<ul>'
         '<li><strong>MSQ-30 :</strong> Calibres de 30 A à 300 A pour barre jusqu\'à $30 \times 10\,\text{mm}$.</li>'
         '<li><strong>MSQ-60 :</strong> Calibres de 250 A à 1000 A pour barre jusqu\'à $60 \times 20\,\text{mm}$.</li>'
         '<li><strong>MSQ-100 :</strong> Calibres jusqu\'à 3200 A pour barre jusqu\'à $100 \times 40\,\text{mm}$.</li>'
         '</ul>')
    ],
    cta='Vous concevez des tableaux généraux basse tension (TGBT), des centres de contrôle moteurs (MCC) ou des armoires de sous-comptage d\'énergie nécessitant des transformateurs de courant de mesure série MSQ certifiés Classe 0.5 / Classe 1.0 (30A à 6000A, fixation rail DIN et barres, capot plombable) ? YOMIN fabrique la gamme complète MSQ selon la norme CEI 61869-2.',
    body='''
<h2>Le Standard Mondial Indispensable pour la Mesure et le Sous-Comptage d\'Énergie</h2>
<p>Dans les tableaux généraux basse tension (TGBT), les armoires d\'automatismes industriels et les tableaux de distribution d\'immeubles tertiaires, des courants de plusieurs milliers d\'ampères circulent dans les jeux de barres principaux.</p>
<p>Pour surveiller, gérer et facturer cette énergie, les centrales de mesure numériques, les compteurs divisionnaires et les relais de protection thermique ont besoin d\'un signal proportionnel et réduit du courant primaire.</p>
<p>Le <strong>Transformateur de Courant Basse Tension Série MSQ (Modèles MSQ-30 à MSQ-125)</strong> apporte la réponse technique parfaite : un transformateur toroïdal de précision à profil carré compact, abaissant le courant sous tension d\'isolement de 720V avec une précision certifiée Classe 0.5 et un double système de montage sur rail DIN 35 mm et barres de cuivre sous la norme internationale CEI 61869-2.</p>
'''
)

MSQ_ES = dict(
    lang='es',
    dir='ltr',
    slug='switchgear-metering-what-is-an-msq-current-transformer-es',
    title='Medición en Cuadros Eléctricos: ¿Qué es un Transformador de Corriente MSQ?',
    breadcrumb='Medición en Cuadros &amp; Transformadores MSQ',
    read='10 min de lectura',
    alt='Cuadro de distribución eléctrica de baja tensión con tres transformadores de corriente serie MSQ-60 (Clase 0.5) montados sobre barras colectoras de cobre',
    desc=('Cuadros generales de distribución en baja tensión (TGBT), centros de control de motores (MCC) y submedición comercial: ¿Qué es un transformador de corriente MSQ? '
          'Núcleos toroidales de acero al silicio de grano orientado, carcasa autoextinguible ABS/PC, tapa transparente precintable antifraude, montaje dual riel DIN y pletina, y precisión Clase 0.5 bajo IEC 61869-2.'),
    model='Serie MSQ (MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100, MSQ-125): Transformadores de Corriente de Medida para Baja Tensión 0.66kV / 720V (Clase 0.5 y 1.0, 30A a 6000A / 5A, Conforme a IEC 61869-2)',
    category='Medición en Cuadros & Transformadores MSQ / Transformadores de Corriente Eléctricos',
    kw='transformador de corriente msq &middot; tc msq &middot; transformador de medida baja tension &middot; tc msq 60 &middot; transformador de corriente clase 0.5 &middot; iec 61869-2 &middot; medicion de energia',
    specs=[
        ('Rango de Corriente Primaria Asignada ($I_{pn}$)', 'Ampla gama desde $30\,\text{A}$ hasta $6000\,\text{A AC}$ primaria cubriendo tamaños MSQ-30, MSQ-40, MSQ-60, MSQ-85, MSQ-100 y MSQ-125'),
        ('Corriente Secundaria Normalizada ($I_{sn}$)', 'Salida secundaria estándar de $5\,\text{A}$ (Opcional $1\,\text{A}$ para largas distancias de cableado)'),
        ('Tensión de Servicio y de Aislamiento', 'Tensión nominal de servicio: $0.66\,\text{kV} / 660\,\text{V AC}$ ; Tensión máxima de aislamiento permanente: $720\,\text{V AC}$ a $50/60\,\text{Hz}$'),
        ('Clase de Precisión y Metrología', 'Clase 0.5 (Submedición tarifaria y analizadores de redes de alta precisión) y Clase 1.0 (Amperímetros de cuadro e indicadores)'),
        ('Material del Núcleo Magnético', 'Chapa de acero al silicio de grano orientado (CRGO) de muy bajas pérdidas, recocida bajo vacío e impregnada para evitar zumbidos'),
        ('Envolvente Aislante y Protección', 'Carcasa de ABS o Policarbonato (PC) de alto impacto, autoextinguible UL 94V-0, bornes secundarios protegidos IP20'),
        ('Seguridad Antifraude y Precintado', 'Tapa transparente de policarbonato con orificio para precinto de seguridad que impide manipulaciones no autorizadas en el cableado secundario'),
        ('Versatilidad de Montaje e Instalación', 'Doble método de instalación: Enganche directo sobre riel DIN de 35 mm (EN 50022) o fijación sobre barra de cobre mediante tornillos aislados')
    ],
    faqs=[
        ('¿Qué es un Transformador de Corriente MSQ y por qué es el estándar en cuadros eléctricos?',
         'Un Transformador de Corriente MSQ (denominado comúnmente transformador de medida cuadrado o TC tipo ventana de baja tensión) es '
         'un transformador de medida diseñado para reducir grandes corrientes alternas (de 30 A a 6000 A) '
         'a una corriente secundaria segura y estandarizada de 5 A o 1 A, apta para ser leída por analizadores de energía y medidores de panel. '
         'En la distribución eléctrica : '
         '<ul>'
         '<li><strong>Aislamiento Galvánico y Seguridad:</strong> Protege los instrumentos de medición frente a sobretensiones y descargas del sistema de potencia.</li>'
         '<li><strong>Precisión Clase 0.5:</strong> Garantiza un error de relación inferior a ±0.5% para una facturación y control energético de máxima exactitud.</li>'
         '<li><strong>Ventana Rectangular Estandarizada:</strong> Se desliza directamente sobre las barras colectoras sin tener que desmontar conexiones.</li>'
         '</ul>')
    ],
    cta='¿Diseña cuadros generales de baja tensión (TGBT), centros de control de motores o sistemas de submedición eléctrica que requieren transformadores de corriente serie MSQ Clase 0.5 / 1.0 (30A a 6000A, montaje riel DIN y barras, tapa precintable)? YOMIN fabrica transformadores MSQ certificados bajo norma IEC 61869-2.',
    body='''
<h2>El Estándar Global de Medición y Submedición Eléctrica en Cuadros de Distribución</h2>
<p>En el interior de cuadros generales de distribución de baja tensión (TGBT), centros de control de motores y tableros de submedición de edificios comerciales e industriales, circulan corrientes de miles de amperios a través de barras colectoras de cobre.</p>
<p>Para medir, registrar y facturar esta energía, los analizadores de redes digitales y contadores electrónicos requieren una señal reducida y proporcional a la corriente real del circuito.</p>
<p>El <strong>Transformador de Corriente de Medida para Baja Tensión Serie MSQ (Modelos MSQ-30 a MSQ-125)</strong> ofrece la solución técnica idónea : un transformador toroidal de precisión con carcasa cuadrada compacta, aislamiento para 720V, precisión Clase 0.5 y doble sistema de fijación en riel DIN de 35 mm y pletinas de cobre bajo norma IEC 61869-2.</p>
'''
)

MSQ_AR = dict(
    lang='ar',
    dir='rtl',
    slug='switchgear-metering-what-is-an-msq-current-transformer-ar',
    title='قياس لوحات التوزيع الكهربائية: ما هو محول التيار من طراز MSQ؟',
    breadcrumb='قياس لوحات التوزيع ومحولات تيار MSQ',
    read='10 دقائق قراءة',
    alt='لوحة توزيع كهربائية للجهد المنخفض مزودة بثلاثة محولات تيار من سلسلة MSQ-60 بدقة فئة 0.5 مثبتة على قضبان نحاسية',
    desc=('لوحات التوزيع الكهربائية للجهد المنخفض، ومراكز التحكم في المحركات (MCC)، وخزائن المولدات، ومنظومات القياس الفرعي للطاقة: ما هو محول التيار من طراز MSQ؟ '
          'القلوب الحلقية المصنعة من صلب السيليكون عالي النفاذية، والأغلفة المقاومة للهب ABS/PC، والأغطية الشفافة القابلة للرصاص لمنع سرقة الكهرباء، والتثبيت المزدوج على قضبان DIN Rail والبارات النحاسية وفقاً للمواصفة IEC 61869-2.'),
    model='سلسلة MSQ (موديلات MSQ-30، MSQ-40، MSQ-60، MSQ-85، MSQ-100، MSQ-125): محولات تيار القياس للجهد المنخفض 0.66kV / 720V (دقة فئة 0.5 وفئة 1.0، تيارات من 30A إلى 6000A / 5A، معتمدة IEC 61869-2)',
    category='قياس لوحات التوزيع ومحولات تيار MSQ / محولات التيار الكهربائية للجهد المنخفض',
    kw='محول تيار msq &middot; msq current transformer &middot; محولات تيار لوحات التوزيع &middot; محول تيار قياس &middot; msq-60 ct &middot; محول تيار فئة 0.5 &middot; iec 61869-2',
    specs=[
        ('نطاق التيارات الابتدائية المقننة ($I_{pn}$)', 'نطاق شامل يبدأ من $30\,\text{A}$ وحتى $6000\,\text{A AC}$ يغطي أحجام النوافذ MSQ-30، MSQ-40، MSQ-60، MSQ-85، MSQ-100، و MSQ-125'),
        ('التيار الثانوي المقنن للقياس ($I_{sn}$)', 'الخرج القياسي المعتمد $5\,\text{A}$ (يتوفر خيار $1\,\text{A}$ لخطوط نقل الإشارات الطويلة)'),
        ('جهد التشغيل الاسمي وجهد العزل', 'جهد تشغيل الشبكة: $0.66\,\text{kV} / 660\,\text{V AC}$؛ أقصى جهد عزل مستمر: $720\,\text{V AC}$ بتردد $50/60\,\text{Hz}$'),
        ('فئة الدقة ومواصفات القياس المعتمدة', 'فئة 0.5 (Class 0.5 للقياس التجاري المعتمد وعدادات الطاقة الدقيقة) وفئة 1.0 (Class 1.0 لأجهزة قياس اللوحات)'),
        ('مادة القلب المغناطيسي والمعالجة', 'قلب حلقي ملفوف من صلب السيليكون الموجه الحبيبات (CRGO) فائق النفاذية ومنخفض الفواقد ومعالج حرارياً تحت تفريغ الهواء لمنع الاهتزاز'),
        ('مادة الغلاف الخارجي ومقاومة الحريق', 'غلاف مصنع من بلاستيك ABS أو بولي كربونات (PC) عالي المتانة ومقاوم للهب ذاتي الإطفاء مطابق لمعايير UL 94V-0، وحماية أطراف IP20'),
        ('ميزات الأمان ومنع التلاعب وسرقة الطاقة', 'غطاء شفاف من البولي كربونات فوق أطراف التوصيل الثانوية S1 و S2 مزود بفتحات للرصاص الأمني لمنع التلاعب وسرقة الكهرباء'),
        ('مرونة التثبيت والتركيب المزدوج', 'نظام تركيب مزدوج: تثبيت مباشر بالكبس على قضبان DIN Rail مقاس 35 مم (EN 50022) أو تثبيت مباشر فوق بارات النحاس بمسامير عازلة')
    ],
    faqs=[
        ('ما هو محول التيار من طراز MSQ ولماذا يعد المعيار العالمي في لوحات التوزيع؟',
         'محول التيار من طراز MSQ (والمعروف في سوق اللوحات بمحول التيار المربع أو محول التيار ذي النافذة المستطيلة للجهد المنخفض) هو '
         'محول قياس دقيق مصمم لتخفيض التيارات المترددة العالية (من 30 أمبير حتى 6000 أمبير) '
         'إلى تيار ثانوي قياسي آمن (5 أمبير أو 1 أمبير) يمكن قراءته بدقة تامة عبر عدادات الطاقة الرقمية وأجهزة القياس. '
         'وفي توزيع الطاقة الكهربائية : '
         '<ul>'
         '<li><strong>العزل الكهربائي والأمان:</strong> يوفر عزلاً تاماً بين دوائر القدرة العالية والأجهزة الإلكترونية الحساسة.</li>'
         '<li><strong>دقة معتمدة فئة 0.5:</strong> يضمن نسبة خطأ لا تتجاوز ±0.5% لحساب واستهلاك الطاقة بدقة تامة.</li>'
         '<li><strong>نافذة مستطيلة قياسية:</strong> ينزلق مباشرة فوق قضبان البارات النحاسية دون الحاجة لفك التوصيلات.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع لوحات التوزيع الكهربائية للجهد المنخفض، أو مراكز التحكم في المحركات، أو منظومات القياس الفرعي للطاقة التي تتطلب محولات تيار من سلسلة MSQ معتمدة بدقة فئة 0.5 / 1.0 (من 30A إلى 6000A، تثبيت على DIN Rail والبارات، غطاء شفاف قابل للرصاص)؟ تصنع يمين (YOMIN) محولات تيار MSQ القياسية وفقاً لمعيار IEC 61869-2.',
    body='''
<h2>المعيار الهندسي الأساسي لقياس ومراقبة الطاقة الكهربائية في لوحات التوزيع</h2>
<p>داخل لوحات التوزيع الكهربائية الرئيسية للجهد المنخفض، ومراكز تشغيل المحركات، وخزائن قياس استهلاك الطاقة في المجمعات التجارية والصناعية، تتدفق تيارات كهربائية تصل إلى آلاف الأمبيرات عبر قضبان البارات النحاسية.</p>
<p>ومن أجل قياس ومراقبة وإصدار فواتير استهلاك هذه الطاقة بدقة، تتطلب عدادات الطاقة الرقمية وأجهزة قياس معامل القدرة تياراً منخفضاً متناسباً تماماً مع تيار الحمل الحقيقي.</p>
<p>يقدم <strong>محول التيار من طراز MSQ للجهد المنخفض (موديلات MSQ-30 إلى MSQ-125)</strong> الحل التقني العالمي المعتمد: محول تيار حلقي دقيق بهيكل مربع مدمج، وعزل مقنن حتى 720V، ودقة قياس فئة 0.5، ونظام تثبيت مرن مزدوج على قضبان DIN Rail والبارات النحاسية وفقاً للمواصفة القياسية الدولية IEC 61869-2.</p>
'''
)

# ==============================================================================
# 2. DL ALUMINUM CABLE LUG (EN, FR, ES, AR)
# ==============================================================================

LUG_EN = dict(
    lang='en',
    dir='ltr',
    slug='power-cable-terminations-what-is-an-aluminum-cable-lug',
    title='Power Cable Terminations: What Is an Aluminum Cable Lug?',
    breadcrumb='Power Cable Terminations &amp; Aluminum Cable Lugs',
    read='10 min read',
    alt='Distribution transformer secondary terminals connected to heavy aluminum power cables with DL-240 compression aluminum cable lugs',
    desc=('Utility power distribution, overhead lines, solar/wind farms, and industrial feeder cables: What is an aluminum cable lug (DL series)? '
          'How pure electrolytic L99.6% aluminum barrels, pre-filled neutral antioxidant contact paste, hexagonal compression dies, and IEC 61238-1 Class A standards break the Al2O3 oxide film and prevent thermal creep and galvanic corrosion.'),
    model='Model DL Series Pure Aluminum L99.6% Compression Terminal Lugs (10mm² to 630mm² for AAC, AAAC, and ACSR Conductors, Pre-Filled with Antioxidant Grease, Friction-Forged Solid Palm, IEC 61238-1 Class A)',
    category='Power Cable Terminations & Aluminum Cable Lugs / Electrical Cable Connectors',
    kw='what is an aluminum cable lug &middot; aluminum cable lug &middot; aluminium cable lug &middot; dl cable lug &middot; dl series aluminum lug &middot; aluminum compression lug &middot; iec 61238-1',
    specs=[
        ('Conductor Metallurgy & Aluminum Purity', 'Pure electrical-grade aluminum (Al purity $\ge 99.6\%$, Grade L2 / 1060 alloy) delivering exceptional electrical conductivity and cold flow ductility'),
        ('Applicable Cable Cross-Sections & Range', 'Comprehensive cable range from $10\,\text{mm}^2$ up to $630\,\text{mm}^2$ (Covering all standard international metric and AWG aluminum conductors)'),
        ('Conductor Types & Cable Construction', 'Compatible with All Aluminum Conductors (AAC), All Aluminum Alloy Conductors (AAAC), Aluminum Conductor Steel Reinforced (ACSR), and XLPE/PVC underground cables'),
        ('Factory Internal Antioxidant Protection', 'Pre-filled at the factory with high-grade neutral antioxidant contact grease inside the barrel, sealed with a protective plastic plug to prevent oxide formation'),
        ('Palm Structure & Manufacturing Method', 'Solid forged seamless palm construction; friction-welded or solid-die stamped with precision metric stud mounting hole (M6, M8, M10, M12, M16, M20)'),
        ('Compression Crimping Tooling & Method', 'Hexagonal compression crimping using calibrated hydraulic crimping tools and matched hexagonal dies per DIN / IEC crimp tables'),
        ('Operating Temperature & Thermal Cycling', 'Tested under continuous electrical and thermal load cycling from $-40^\circ\text{C}$ to $+120^\circ\text{C}$ without thermal creep or connection loosening'),
        ('International Manufacturing Safety Standards', 'Fully tested and compliant with IEC 61238-1 Class A (Compression Connectors for Power Cables), GB/T 14315, and utility distribution specifications')
    ],
    faqs=[
        ('What is an Aluminum Cable Lug (DL Series) and why is it essential for terminating aluminum conductors?',
         'An Aluminum Cable Lug—specifically the universally recognized DL Series compression terminal—is '
         'a heavy-duty electrical connector manufactured from pure electrolytic aluminum (L99.6%) engineered '
         'to terminate multi-stranded all-aluminum power cables (AAC, AAAC, ACSR) onto electrical equipment studs, switchgear terminals, and transformer bushings. '
         'In power distribution and renewable energy: '
         '<ul>'
         '<li><strong>Overcomes Aluminum Oxide ($\text{Al}_2\text{O}_3$):</strong> When aluminum is exposed to air, an invisible, micro-thin aluminum oxide layer '
         'instantly forms. Aluminum oxide is a severe electrical insulator ($> 10^{14}\,\Omega\cdot\text{cm}$). Attempting to bolt bare aluminum without a proper terminal '
         'results in high contact resistance, arcing, and thermal failure. DL lugs are pre-filled with neutral antioxidant grease that breaks the oxide film during compression.</li>'
         '<li><strong>Matches Thermal Expansion:</strong> Aluminum expands and contracts at a rate of $23 \times 10^{-6}/\text{K}$ (substantially higher than copper). '
         'Using a pure aluminum DL lug with aluminum conductors ensures identical thermal expansion coefficients, eliminating thermal creep, loosening, and joint failure during peak load cycles.</li>'
         '<li><strong>High Mechanical Pull-Out Strength:</strong> Hydraulic hexagonal compression cold-welds the aluminum strands inside the barrel, '
         'exceeding IEC 61238-1 Class A mechanical tensile pull-out strength requirements.</li>'
         '</ul>'),
        ('Why is factory-filled antioxidant contact paste critical inside the barrel of an aluminum lug?',
         'The pre-filled neutral antioxidant grease inside the DL lug barrel fulfills three non-negotiable functions: '
         '<ul>'
         '<li><strong>Oxide Film Disruption:</strong> Under hydraulic compression pressure, the grease forces micro-abrasive mineral particles against the aluminum strands, '
         'mechanically rupturing the insulating aluminum oxide film and establishing thousands of metal-to-metal conducting micro-junctions.</li>'
         '<li><strong>Hermetic Atmospheric Sealing:</strong> The grease completely fills all interstitial voids between individual wire strands, '
         'forming an airtight, moisture-proof barrier that permanently prevents oxygen and moisture from entering and re-oxidizing the joint.</li>'
         '<li><strong>Corrosion Inhibition:</strong> Protects against galvanic degradation in humid, industrial, and coastal environments.</li>'
         '</ul>'),
        ('What precautions must be taken when connecting an Aluminum DL Lug to a Copper Busbar?',
         'Directly bolting pure aluminum to bare copper in the presence of atmospheric moisture creates a severe galvanic cell, '
         'rapidly corroding the aluminum. When connecting a DL aluminum lug to a copper busbar: '
         '<ul>'
         '<li><strong>Bimetallic Transition Washers (Al-Cu):</strong> Always install an explosive-bonded copper-aluminum bimetallic washer between the copper busbar and aluminum lug palm.</li>'
         '<li><strong>Belleville Spring Washers:</strong> Always install conical spring Belleville washers beneath the bolt head or nut to maintain constant mechanical contact pressure '
         'across thermal expansion and contraction cycles.</li>'
         '</ul>')
    ],
    cta='Procuring utility-grade electrical cable connectors for overhead power distribution, solar/wind farm collection circuits, or industrial transformer terminations requiring certified IEC 61238-1 Class A pure aluminum compression lugs (10mm² to 630mm², pre-filled with antioxidant grease, friction-forged solid palm)? YOMIN manufactures precision DL series aluminum cable lugs.',
    body='''
<h2>The Trusted Termination Solution for Utility Aluminum Power Distribution Cables</h2>
<p>In electrical utility transmission and distribution networks, solar photovoltaic collector arrays, wind turbine nacelles, and heavy industrial power substations, aluminum cables (AAC, AAAC, and ACSR) are the dominant conductor choice worldwide due to aluminum\'s light weight (one-third the density of copper) and superior raw material economics.</p>
<p>However, terminating heavy-gauge multi-stranded aluminum power cables requires specialized metallurgical engineering: aluminum forms an instantaneous, insulating aluminum oxide film ($\text{Al}_2\text{O}_3$), exhibits high thermal expansion, and can suffer galvanic corrosion if improperly connected.</p>
<p>The <strong>DL Series Pure Aluminum Compression Cable Lug</strong> provides the universally certified solution: precision-extruded from pure L99.6% electrical aluminum, pre-filled with neutral antioxidant contact paste, and engineered for hexagonal hydraulic compression to deliver permanent low contact resistance, high tensile strength, and complete thermal stability under IEC 61238-1 Class A.</p>

<h2>Engineering Anatomy: Inside Model DL Series Aluminum Compression Cable Lugs</h2>
<ol>
  <li><strong>Pure High-Conductivity Aluminum Alloy (Al &ge; 99.6%):</strong> Manufactured from high-grade electrical aluminum delivering superior electrical conductivity and maximum ductility during hydraulic compression crimping.</li>
  <li><strong>Factory Pre-Filled Antioxidant Neutral Contact Compound:</strong> The internal barrel is pre-loaded with high-temperature antioxidant grease and sealed with a bright plastic cap to prevent air exposure and instantly disrupt aluminum oxide during crimping.</li>
  <li><strong>Seamless Solid-Forged Mounting Palm:</strong> Forged into a solid, void-free flat contact surface with precision metric stud holes (M6 through M20) ensuring maximum surface-area contact on transformer bushings and switchgear pads.</li>
  <li><strong>Generous Chamfered Barrel Entry:</strong> Conical lead-in chamfer ensures smooth, zero-snag insertion of compacted and non-compacted stranded aluminum conductors without bending or damaging individual conductor wires.</li>
  <li><strong>Engineered Barrel Length for Double/Triple Compression:</strong> Lengthy barrel dimensions provide ample space for multiple hexagonal crimp bites, ensuring massive mechanical pull-out strength meeting IEC 61238-1 requirements.</li>
</ol>

<h2>Comparison: Pure Aluminum DL Lugs vs. Bimetallic DTL Lugs vs. Standard Copper Lugs</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Performance Metric</th>
      <th>Standard Copper Cable Lug (DT Series)</th>
      <th>Bimetallic Copper-Aluminum Lug (DTL Series)</th>
      <th>YOMIN Pure Aluminum Lug (DL Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Conductor Compatibility</strong></td>
      <td>Copper conductors only. (Direct crimping on aluminum causes galvanic failure).</td>
      <td>Aluminum cables to copper busbars.</td>
      <td><strong>Optimized for All-Aluminum Conductors (AAC, AAAC, ACSR, ABC).</strong></td>
    </tr>
    <tr>
      <td><strong>Thermal Expansion Match ($\alpha$)</strong></td>
      <td>Severe mismatch with aluminum cables ($\Delta\alpha \approx 7 \times 10^{-6}/\text{K}$).</td>
      <td>Matched at barrel (aluminum); matched at palm (copper).</td>
      <td><strong>Perfect 100% Match: Identical thermal expansion prevents joint loosening.</strong></td>
    </tr>
    <tr>
      <td><strong>Weight &amp; Overhead Line Strain</strong></td>
      <td>Heavy: 300% heavier than aluminum, increasing pole mechanical sag.</td>
      <td>Intermediate weight.</td>
      <td><strong>Ultra-Lightweight: Minimizes mechanical cantilever strain on bushings and poles.</strong></td>
    </tr>
    <tr>
      <td><strong>Internal Antioxidant Protection</strong></td>
      <td>Rarely pre-filled (copper does not require oxide paste).</td>
      <td>Pre-filled in aluminum barrel.</td>
      <td><strong>Factory Pre-Filled: High-grade antioxidant paste sealed with plastic cap.</strong></td>
    </tr>
    <tr>
      <td><strong>Cost Efficiency for Power Projects</strong></td>
      <td>High copper material cost.</td>
      <td>Higher manufacturing cost due to friction welding.</td>
      <td><strong>Highest Cost Efficiency: Ideal for massive utility and solar cable networks.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

LUG_FR = dict(
    lang='fr',
    dir='ltr',
    slug='power-cable-terminations-what-is-an-aluminum-cable-lug-fr',
    title='Raccordement des Câbles Électriques : Qu\'est-ce qu\'une Cosse en Aluminium (Série DL) ?',
    breadcrumb='Raccordement de Câbles &amp; Cosses Aluminium',
    read='10 min de lecture',
    alt='Bornes secondaires de transformateur de distribution raccordées à des câbles d\'énergie en aluminium avec des cosses à sertir série DL-240',
    desc=('Réseaux de distribution d\'électricité, lignes aériennes, centrales solaires/éoliennes et câbles industriels : Qu\'est-ce qu\'une cosse tubulaire en aluminium (série DL) ? '
          'Fût en aluminium pur électrolytique L99.6%, pâte antioxydante neutre pré-remplie en usine, sertissage hexagonal par rétreint et norme CEI 61238-1 Classe A.'),
    model='Série DL : Cosses Tubulaires en Aluminium Pur L99.6% à Rétreindre (10 mm² à 630 mm² pour Câbles AAC, AAAC et ACSR, Pré-Remplies de Graisse Antioxydante, Plage Forgée Massive, Conforme CEI 61238-1 Classe A)',
    category='Raccordement de Câbles & Cosses Aluminium / Connectique Électrique pour Câbles d\'Énergie',
    kw='cosse aluminium &middot; cosse dl &middot; cosse a sertir aluminium &middot; cosse tubulaire aluminium &middot; cable alu &middot; graisse antioxydante alu &middot; cei 61238-1',
    specs=[
        ('Métallurgie et Pureté de l\'Aluminium', 'Aluminium de pureté électrolytique $\ge 99,6\%$ (Nuance L2 / 1060) offrant une conductivité optimale et une excellente déformation plastique sous sertissage'),
        ('Plage de Sections de Câbles Admissibles', 'Large gamme de $10\,\text{mm}^2$ à $630\,\text{mm}^2$ (Compatible avec l\'ensemble des sections métriques et AWG normalisées)'),
        ('Types de Conducteurs Raccordables', 'Câbles aluminium tout aluminium (AAC), alliage d\'aluminium (AAAC), alu-acier (ACSR) et câbles isolés souterrains HTA/BT'),
        ('Protection Antioxydante en Usine', 'Fût pré-rempli en usine de pâte de contact antioxydante neutre obturé par un bouchon plastique hermétique étanche à l\'air'),
        ('Structure de la Plage de Raccordement', 'Plage massive matricée sans soudure, percée pour goujons métriques (M6, M8, M10, M12, M16, M20)'),
        ('Procédé et Outillage de Sertissage', 'Sertissage hexagonal par compression hydraulique avec matrices calibrées selon tableaux normalisés CEI / DIN'),
        ('Comportement aux Cycles Thermiques', 'Testé sous cycles thermiques et électriques continus de $-40^\circ\text{C}$ à $+120^\circ\text{C}$ sans fluage ni desserrage'),
        ('Conformité aux Normes Internationales', 'Certifié et conforme aux normes CEI 61238-1 Classe A (Raccords de compression pour câbles d\'énergie), NF C 33-090 et spécifications des distributeurs')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Cosse en Aluminium (Série DL) et pourquoi est-elle indispensable sur câble alu ?',
         'Une Cosse en Aluminium (particulièrement le modèle normalisé Série DL) est '
         'un raccord d\'extrémité en aluminium pur électrolytique (99,6%) conçu pour raccorder des câbles d\'énergie en aluminium '
         'sur les plages de bornes d\'équipements, transformateurs et disjoncteurs. '
         'Dans les réseaux électriques : '
         '<ul>'
         '<li><strong>Destruction de la Couche d\'Alumine ($\text{Al}_2\text{O}_3$) :</strong> À l\'air libre, l\'aluminium s\'oxyde instantanément en créant '
         'une pellicule isolante très dure. La cosse DL est pré-remplie d\'une pâte antioxydante qui brise cette couche lors du sertissage.</li>'
         '<li><strong>Compatibilité Dilatation Thermique :</strong> L\'aluminium et la cosse se dilatent au même coefficient thermique, évitant tout desserrage.</li>'
         '<li><strong>Résistance Mécanique Élevée :</strong> Le rétreint hexagonal crée une soudure à froid conforme à la norme CEI 61238-1 Classe A.</li>'
         '</ul>')
    ],
    cta='Vous déployez des réseaux de distribution électrique, des parcs photovoltaïques ou des lignes aériennes nécessitant des cosses en aluminium pur à sertir certifiées CEI 61238-1 Classe A (10 mm² à 630 mm², pré-remplies de graisse antioxydante) ? YOMIN fabrique la série DL selon les standards d\'ingénierie les plus stricts.',
    body='''
<h2>La Solution Technique Éprouvée pour le Raccordement Sécurisé des Câbles en Aluminium</h2>
<p>Sur les réseaux de transport et de distribution d\'électricité, dans les centrales solaires photovoltaïques et les parcs éoliens, les câbles en aluminium sont massivement privilégiés pour leur légèreté et leur excellent ratio technico-économique.</p>
<p>Cependant, le raccordement de ces câbles requiert une maîtrise métallurgique absolue en raison de l\'oxydation spontanée de l\'aluminium et de ses propriétés thermomécaniques.</p>
<p>La <strong>Cosse Tubulaire en Aluminium Série DL</strong> apporte la garantie d\'une liaison durable : tube en aluminium pur à 99,6%, pré-rempli en usine de pâte antioxydante neutre et certifié pour sertissage hexagonal sous la norme CEI 61238-1 Classe A.</p>
'''
)

LUG_ES = dict(
    lang='es',
    dir='ltr',
    slug='power-cable-terminations-what-is-an-aluminum-cable-lug-es',
    title='Terminaciones de Cables de Potencia: ¿Qué es un Terminal de Aluminio (Serie DL)?',
    breadcrumb='Terminaciones de Cables &amp; Terminales de Aluminio',
    read='10 min de lectura',
    alt='Bornes secundarios de transformador de distribución conectados a cables de potencia de aluminio mediante terminales de compresión serie DL-240',
    desc=('Redes de distribución eléctrica de media y baja tensión, líneas aéreas, parques solares/eólicos y alimentadores industriales: ¿Qué es un terminal de compresión de aluminio (serie DL)? '
          'Cuerpo de aluminio puro electrolítico L99.6%, pasta antioxidante neutra prellenada de fábrica, crimpado hexagonal por compresión hidráulica y norma IEC 61238-1 Clase A.'),
    model='Serie DL: Terminales Tubulares de Aluminio Puro L99.6% para Compresión (10 mm² a 630 mm² para Cables AAC, AAAC y ACSR, Prellenados con Grasa Antioxidante, Pala Forjada Maciza, Conforme a IEC 61238-1 Clase A)',
    category='Terminaciones de Cables & Terminales de Aluminio / Conectores Terminales de Potencia',
    kw='terminal de aluminio &middot; terminal dl &middot; terminal de compresion aluminio &middot; zapata de aluminio &middot; cable de aluminio &middot; pasta antioxidante aluminio &middot; iec 61238-1',
    specs=[
        ('Metalurgia y Pureza del Aluminio', 'Aluminio de pureza eléctrica $\ge 99.6\%$ (Grado L2 / 1060) que asegura una óptima conductividad y excelente ductilidad bajo compresión hidráulica'),
        ('Gama de Secciones de Cables Soportadas', 'Rango integral desde $10\,\text{mm}^2$ hasta $630\,\text{mm}^2$ (Compatible con cables métricos y calibres AWG normalizados)'),
        ('Tipos de Conductores Aplicables', 'Cables de aluminio puro (AAC), aleación de aluminio (AAAC), aluminio con alma de acero (ACSR) y cables aislados subterráneos'),
        ('Protección Antioxidante de Fábrica', 'Barril prellenado en fábrica con compuesto de contacto antioxidante neutro sellado con tapón de plástico hermético'),
        ('Pala de Conexión y Fabricación', 'Pala maciza forjada sin costura con orificio para perno métrico (M6, M8, M10, M12, M16, M20)'),
        ('Método y Herramienta de Crimpado', 'Compresión hexagonal mediante prensas hidráulicas y matrices calibradas bajo tablas de engaste IEC / DIN'),
        ('Comportamiento ante Ciclos Térmicos', 'Ensayado bajo ciclos de carga térmica continua de $-40^\circ\text{C}$ a $+120^\circ\text{C}$ sin aflojamiento ni deformación'),
        ('Conformidad con Normas Internacionales', 'Probado y certificado bajo norma IEC 61238-1 Clase A (Conectores de compresión para cables de potencia) y directivas de compañías eléctricas')
    ],
    faqs=[
        ('¿Qué es un Terminal de Aluminio (Serie DL) y por qué es indispensable en cables de aluminio?',
         'Un Terminal de Aluminio (particularmente la serie normalizada DL) es '
         'un conector tubular de aluminio puro electrolítico (99.6%) diseñado para terminar cables de potencia de aluminio '
         'en bornes de transformadores, seccionadores e interruptores de potencia. '
         'En la distribución eléctrica : '
         '<ul>'
         '<li><strong>Elimina la Capa Aislante de Óxido ($\text{Al}_2\text{O}_3$) :</strong> El aluminio al aire forma una película invisible de óxido altamente aislante. '
         'El terminal DL viene prellenado con grasa antioxidante que rompe mecánicamente esta película durante el prensado.</li>'
         '<li><strong>Mismo Coeficiente de Dilatación Térmica :</strong> El terminal y el cable se dilatan al unísono, evitando que la conexión se afloje con el tiempo.</li>'
         '<li><strong>Alta Resistencia a la Tracción :</strong> La compresión hexagonal genera una unión en frío maciza certificada bajo norma IEC 61238-1 Clase A.</li>'
         '</ul>')
    ],
    cta='¿Instala redes de distribución eléctrica, plantas solares fotovoltaicas o líneas de distribución que requieren terminales de compresión de aluminio puro certificados IEC 61238-1 Clase A (10 mm² a 630 mm², prellenados con pasta antioxidante)? YOMIN fabrica la serie DL bajo los más altos estándares.',
    body='''
<h2>La Solución Homologada para la Conexión Confiable de Cables de Potencia de Aluminio</h2>
<p>En redes de distribución eléctrica de media y baja tensión, huertos solares fotovoltaicos y parques eólicos, los conductores de aluminio representan la opción principal gracias a su ligereza y gran rendimiento económico.</p>
<p>No obstante, la terminación de estos cables requiere un diseño metalúrgico específico para combatir la oxidación natural del aluminio y asegurar una unión mecánicamente indestructible.</p>
<p>El <strong>Terminal Tubular de Aluminio para Compresión Serie DL</strong> ofrece la máxima garantía de servicio : cuerpo de aluminio puro al 99.6%, compuesto antioxidante neutro de fábrica y certificación bajo norma internacional IEC 61238-1 Clase A.</p>
'''
)

LUG_AR = dict(
    lang='ar',
    dir='rtl',
    slug='power-cable-terminations-what-is-an-aluminum-cable-lug-ar',
    title='نهايات كابلات الطاقة: ما هي كابل لوج الألمنيوم (Aluminum Cable Lug - طراز DL)؟',
    breadcrumb='نهايات كابلات الطاقة وكابل لوج الألمنيوم',
    read='10 دقائق قراءة',
    alt='أطراف محول توزيع كهربائي متصلة بكابلات طاقة ألمنيوم عبر كابل لوج ألمنيوم مضغوط هيدروليكياً طراز DL-240',
    desc=('شبكات توزيع الكهرباء، والخطوط الهوائية، ومحطات الطاقة الشمسية وطاقة الرياح، والكابلات الصناعية: ما هي كابل لوج الألمنيوم (كوسة ألمنيوم طراز DL)؟ '
          'أنابيب الألمنيوم الإلكتروليتي النقي L99.6%، ومعجون التلامس المضاد للأكسدة المعبأ مسبقاً بالمصنع، والكبس الهيدروليكي السداسي، ومطابقة معيار IEC 61238-1 Class A لمنع التقوس والتآكل الجلفاني.'),
    model='سلسلة DL: كابل لوج ألمنيوم نقي L99.6% للكبس بالضغط (من 10 مم² إلى 630 مم² لكابلات AAC و AAAC و ACSR، معبأة مسبقاً بمعجون مضاد للأكسدة، طرف توصيل مصمت مطروق، معتمدة IEC 61238-1 Class A)',
    category='نهايات كابلات الطاقة وكابل لوج الألمنيوم / نهايات وتوصيلات كابلات الطاقة الكهربائية',
    kw='كابل لوج المنيوم &middot; كابل شو المنيوم &middot; كوسة المنيوم &middot; dl cable lug &middot; كبس كابلات المنيوم &middot; معجون مضاد للاكسدة المنيوم &middot; iec 61238-1',
    specs=[
        ('نقاء وميتالورجيا معدن الألمنيوم', 'ألمنيوم إلكتروليتي نقي للأغراض الكهربائية بنقاء $\ge 99.6\%$ (سبيكة L2 / 1060) لتأمين أعلى موصلية كهربائية ومرونة فائقة أثناء الكبس الهيدروليكي'),
        ('نطاق مقاطع الكابلات المعتمدة', 'نطاق متكامل وشامل يغطي مقاطع من $10\,\text{mm}^2$ حتى $630\,\text{mm}^2$ (متوافق مع المقاييس المترية والمقاييس الأمريكية AWG)'),
        ('أنواع الموصلات والكابلات المدعومة', 'كابلات الألمنيوم الكامل (AAC)، وسبائك الألمنيوم (AAAC)، والألمنيوم المقوى بالفولاذ (ACSR)، والكابلات الأرضية المعزولة'),
        ('الحماية الداخلية المسبقة ضد الأكسدة', 'معبأة مسبقاً في المصنع بمعجون تلامس مضاد للأكسدة عالي الجودة ومحكمة الإغلاق بسدادة بلاستيكية لحجب الهواء والرطوبة'),
        ('هيكل طرف التوصيل والتصنيع', 'طرف تثبيت مصمت مطروق بدون لحامات ومثقوب بدقة لمسامير الربط المترية (M6, M8, M10, M12, M16, M20)'),
        ('طريقة وأدوات الكبس الهيدروليكي', 'كبس سداسي بالضغط الهيدروليكي باستخدام مكابس معتمدة ولقم كبس سداسية مطابقة لجداول المعايير الدولية IEC / DIN'),
        ('التحمل الحراري ودورات التشغيل', 'مختبر تحت دورات الحمل الكهربائي والحراري المستمر من $-40^\circ\text{C}$ حتى $+120^\circ\text{C}$ دون أي ارتخاء ميكانيكي'),
        ('المطابقة للمواصفات والاعتمادات الدولية', 'مختبر ومعتمد بالكامل وفق معيار IEC 61238-1 Class A (وصلات الضغط لكابلات الطاقة) ومواصفات شركات الكهرباء')
    ],
    faqs=[
        ('ما هي كابل لوج الألمنيوم (طراز DL) ولماذا تعتبر ضرورية لكابلات الألمنيوم؟',
         'كابل لوج الألمنيوم (والمعروفة في السوق باسم كابل شو ألمنيوم أو كوسة ألمنيوم طراز DL) هي '
         'وصلة نهاية كهربائية مصنعة من الألمنيوم الإلكتروليتي النقي بنسبة 99.6% مصممة لإنهاء وربط كابلات الطاقة المصنعة من الألمنيوم '
         'على أطراف المحولات والمفاتيح الكهربائية وقضبان التوزيع. '
         'وفي شبكات توزيع الطاقة : '
         '<ul>'
         '<li><strong>تكسير طبقة أكسيد الألمنيوم العازلة ($\text{Al}_2\text{O}_3$):</strong> يشكل الألمنيوم بمجرد تعرضه للهواء طبقة أكسيد صلبة جداً وعازلة كهربائياً. '
         'تأتي كابل لوج DL معبأة مسبقاً بمعجون تلامس خاص يقوم بكسر هذه الطبقة أثناء الكبس لتأمين تلامس معدني مباشر ممتاز.</li>'
         '<li><strong>توافق معامل التمدد الحراري:</strong> يتمدد الألمنيوم واللوج بنفس المعدل تماماً، مما يمنع ارتخاء المسمار وسخونة نقطة التوصيل أثناء الأحمال العالية.</li>'
         '<li><strong>قوة شد ميكانيكية فائقة:</strong> ينتج الكبس الهيدروليكي السداسي كتلة متراصة تقاوم قوى الشد الميكانيكي بكفاءة وفق معيار IEC 61238-1 Class A.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تنفيذ مشاريع شبكات توزيع الكهرباء، أو محطات الطاقة الشمسية، أو خطوط نقل القدرة التي تتطلب كابل لوج ألمنيوم نقي معتمد IEC 61238-1 Class A (مقاطع 10 مم² إلى 630 مم²، معبأة مسبقاً بمعجون مانع للأكسدة، طرف مصمت مطروق)؟ تصنع يمين (YOMIN) كابل لوج سلسلة DL بأعلى مواصفات الجودة.',
    body='''
<h2>الحل الهندسي المعتمد لربط وإنهاء كابلات الألمنيوم في شبكات الطاقة الكهربائية</h2>
<p>في شبكات نقل وتوزيع الطاقة الكهربائية ومحطات التوليد الكهروضوئية ومزارع الرياح، تعد كابلات الألمنيوم الخيار القياسي الأول عالمياً بفضل خفة وزنها وتكلفتها الاقتصادية الممتازة مقارنة بالنحاس.</p>
<p>ومع ذلك، يتطلب إنهاء هذه الكابلات دقة ميتالورجية وهندسية عالية للتعامل مع ظاهرة الأكسدة الطبيعية للألمنيوم واختلاف التمدد الحراري.</p>
<p>تقدم <strong>كابل لوج الألمنيوم للكبس الهيدروليكي سلسلة DL</strong> الحل الموثوق والمعتمد دولياً: تصنيع من الألمنيوم النقي بنسبة 99.6%، وتعبئة مسبقة في المصنع بمعجون مانع للأكسدة، وتوافق تام مع لقم الكبس السداسي وفق المواصفة القياسية الدولية IEC 61238-1 Class A.</p>
'''
)

ALL_MULTILINGUAL_POSTS_1020 = [
    MSQ_EN, MSQ_FR, MSQ_ES, MSQ_AR,
    LUG_EN, LUG_FR, LUG_ES, LUG_AR
]
