# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-15 (Batch 2):
1. Bolted Strain Clamps for Overhead Transmission Lines (EN, FR, ES, AR)
2. Medium-Voltage Current Transformers for Substation Switchgear (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. STRAIN CLAMP (EN, FR, ES, AR)
# ==============================================================================

SC_EN = dict(
    lang='en',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-strain-clamp',
    title='Overhead Transmission Lines: What Is a Strain Clamp?',
    breadcrumb='Transmission Line Hardware &amp; Clamps',
    read='10 min read',
    alt='Heavy-duty bolted aluminum alloy Strain Clamp (Model NLL series) anchored to a composite insulator string at a transmission line dead-end steel lattice tower',
    desc=('High-voltage overhead transmission lines (11kV to 220kV), dead-end tension towers, and conductor anchoring: What is a strain clamp? '
          'How bolted aluminum alloy bodies, 95% conductor rated tensile strength (RTS) holding grip, high-torque U-bolts, and IEC 61284 standards secure transmission conductors.'),
    model='Model NLL / NY Series High-Strength Bolted & Compression Aluminum Alloy Strain Clamps for Bare ACSR / AAAC Conductors (11kV to 220kV, Holding Grip >= 95% RTS, IEC 61284 / ANSI C119.4)',
    category='Transmission Line Hardware & Clamps / Strain Clamps',
    kw='what is a strain clamp &middot; strain clamp &middot; bolted strain clamp &middot; transmission strain clamp nll &middot; tension clamp acsr &middot; dead end strain clamp',
    specs=[
        ('Applicable Conductor Type & Construction', 'Engineered for bare stranded aluminum conductors: ACSR (Aluminum Conductor Steel Reinforced), AAAC, and AAC conductors'),
        ('Rated Mechanical Holding Grip Strength', 'Extreme tensile holding grip efficiency: &ge; 95% of Conductor Rated Tensile Strength (RTS) without strand slippage'),
        ('Clamp Body & Keeper Plate Material', 'High-strength corrosion-resistant gravity cast aluminum alloy (Grade A356 / ZL101A, T6 heat-treated)'),
        ('U-Bolt Hardware & Tensile Grade', 'Heavy-duty U-bolts forged from high-tensile steel (Grade 8.8) with hot-dip galvanized coating (ASTM A153 / ISO 1461)'),
        ('Conductor Cross-Sectional Range', 'Standard jaw groove selections: 16 mm&sup2; up to 800 mm&sup2; (Conductor overall outer diameter range: &phi;7.0 mm to &phi;38.0 mm)'),
        ('Electrical Conductivity & Resistance Ratio', 'Low electrical resistance: Contact resistance ratio $R_{clamp} / R_{conductor} < 1.0$ (prevents thermal hot-spot overheating)'),
        ('Cotter Pin & Security Locking Hardware', 'Marine-grade stainless steel (Grade 304/316) humped cotter pin prevents accidental clevis pin disengagement'),
        ('International Utility Testing Standards', 'Fully tested and compliant with IEC 61284, ANSI C119.4, and BS 3288-1 utility line hardware specifications')
    ],
    faqs=[
        ('What is a Strain Clamp and where is it installed along overhead transmission lines?',
         'A Strain Clamp—frequently designated as a dead-end strain clamp, bolted tension clamp, or transmission anchoring clamp—is '
         'a specialized heavy-duty mechanical line fitting designed to securely grip a bare overhead transmission conductor '
         'and anchor it to a tension insulator string, transferring the full continuous longitudinal tensile pull of the line to the tower structure. '
         'Along high-voltage transmission and distribution corridors (11kV to 220kV+): '
         '<ul>'
         '<li><strong>1. Dead-End &amp; Terminal Towers:</strong> Installed where an overhead transmission line terminates at a high-voltage substation switchyard gantry '
         'or transitions into underground high-voltage cables. The clamp anchors the entire mechanical line tension while a non-tensioned jumper loop '
         'carries the electrical current into the station busbar.</li>'
         '<li><strong>2. Angle &amp; Corner Towers:</strong> Positioned wherever a transmission line changes horizontal direction by more than 15 to 30 degrees. '
         'Suspension clamps cannot withstand massive lateral resultant vector forces; tension insulator strings with dual strain clamps must be installed '
         'on both sides of the tower crossarm.</li>'
         '<li><strong>3. Long-Span River &amp; Canyon Crossings:</strong> Secures conductors across extreme aerial spans (exceeding 500 to 1500 meters) '
         'where high wind speeds, heavy ice accumulation, and massive conductor sag generate tens of thousands of kilograms of mechanical tension.</li>'
         '</ul>'),
        ('How does a Bolted Strain Clamp achieve over 95% holding strength without crushing aluminum strands?',
         'Securing a bare ACSR conductor under tens of thousands of newtons of tension requires a delicate balance between mechanical grip friction and conductor preservation: '
         '<ul>'
         '<li><strong>Wave-Profile Curvature Groove:</strong> The internal clamping channel of YOMIN NLL series clamps features an engineered sinusoidal '
         'or wave-shaped contour. As the conductor passes through the curved bed, the normal force applied by the U-bolts generates massive frictional resistance '
         'along the conductor length via the capstan effect, rather than relying on point-crushing pressure.</li>'
         '<li><strong>Radiused Aluminum Keeper Plate:</strong> The keeper plate is cast with smooth, flared radius bell-mouth ends. '
         'When linemen torque the high-tensile U-bolts to specified torque values (e.g. 45–60 N&middot;m), the clamping force distributes evenly '
         'across the outer aluminum strands without pinching, galling, or shearing individual wires.</li>'
         '<li><strong>95% RTS Certification:</strong> Under formal IEC 61284 tensile testing, YOMIN strain clamps sustain mechanical holding loads exceeding 95% '
         'of the conductor\'s ultimate breaking strength without slippage for over 60 seconds.</li>'
         '</ul>'),
        ('Why are Bolted Aluminum Strain Clamps preferred over Hydraulic Compression Clamps in distribution networks?',
         'While hydraulic compression strain clamps (NY series) provide permanent crimped joints for ultra-high-voltage (400kV–765kV) lines, '
         '<strong>Bolted Aluminum Strain Clamps (NLL series)</strong> dominate distribution and sub-transmission networks (11kV to 110kV) due to major operational advantages: '
         '<ul>'
         '<li><strong>Tool-Free Simplicity in the Field:</strong> Bolted clamps require only a standard lineman socket wrench or torque wrench. '
         'They eliminate the need to haul heavy, multi-ton hydraulic compression pumps, gasoline generators, and specialized crimping dies up transmission poles.</li>'
         '<li><strong>Reusability &amp; Line Sag Adjustability:</strong> During line stringing and maintenance, linemen can loosen the U-bolts, adjust conductor sag, '
         're-tension the line, or re-route spans without cutting the conductor. Compression clamps are permanent and must be completely cut out if adjustments are needed.</li>'
         '<li><strong>Zero Conductor Core Damage:</strong> Unlike hydraulic crimping which requires stripping outer aluminum layers to crimp the inner steel core, '
         'bolted clamps grip the fully assembled conductor directly over aluminum armor tape.</li>'
         '</ul>')
    ],
    cta='Designing high-voltage transmission lines, dead-end tension towers, river crossing spans, or substation overhead gantries requiring certified IEC 61284 bolted aluminum strain clamps (11kV to 220kV, holding grip >= 95% RTS)? YOMIN manufactures precision NLL series transmission strain clamps.',
    body='''
<h2>The Mechanical Anchor Holding High-Voltage Transmission Lines in Mid-Air</h2>
<p>Across national high-voltage transmission grids and regional power distribution networks spanning deserts, mountain ranges, river valleys, and coastal corridors at <strong>11kV, 33kV, 66kV, and 110kV</strong>, overhead conductors hang suspended under staggering mechanical tension.</p>
<p>Each kilometer of heavy bare Aluminum Conductor Steel Reinforced (ACSR) or All-Aluminum Alloy Conductor (AAAC) weighs thousands of kilograms. Under severe winter windstorms and heavy radial ice accumulation, mechanical tensile forces pulling on terminal structures reach tens of thousands of newtons.</p>
<p>While standard suspension clamps hang vertically to cradle the conductor\'s downward weight along straight-line runs, they are physically incapable of resisting longitudinal line pull. If a dead-end conductor were supported by a suspension clamp, the conductor would violently rip free, collapsing adjacent towers like dominos.</p>
<p>The <strong>High-Voltage Transmission Bolted Strain Clamp (Model NLL Series)</strong> serves as the indispensable structural anchor: a heavy-duty, high-strength aluminum alloy tension clamp engineered to grip bare overhead conductors with unshakeable mechanical holding power (&ge; 95% RTS) while transferring tension safely into the tower crossarm.</p>

<h2>Engineering Anatomy: Inside a Model NLL Bolted Aluminum Strain Clamp</h2>
<ol>
  <li><strong>High-Strength Cast Aluminum Alloy Body:</strong> Gravity die-cast from electrical-grade A356 aluminum alloy with T6 heat treatment. Possesses exceptional tensile strength, zero magnetic hysteresis power loss, and natural corrosion immunity in salt-fog marine and industrial sulfur environments.</li>
  <li><strong>Wave-Contoured Clamping Bed:</strong> The internal conductor groove features an engineered gentle sinusoidal wave profile that maximizes frictional holding grip via capstan friction principles without localized stress concentration.</li>
  <li><strong>Heavy-Duty High-Tensile U-Bolts:</strong> Forged from Grade 8.8 structural steel with hot-dip galvanized protective coating exceeding 85 &mu;m thickness. Paired with heavy spring lock washers and double locking nuts to prevent vibration loosening under wind aeolian vibration.</li>
  <li><strong>Smooth Flared Bell-Mouth Keeper:</strong> Aluminum keeper plate designed with generously radiused bell-mouth entrances that eliminate sharp edge pinching, protecting conductor outer strands from fatigue cracking during wind swing.</li>
  <li><strong>Integrated Clevis Tongue &amp; Cotter Pin Assembly:</strong> Forged pulling eye connects directly to composite suspension insulator strings via standard clevis shackles, locked in place by a marine-grade stainless steel humped cotter pin.</li>
</ol>

<h2>Comparison: Bolted Aluminum Strain Clamp (NLL) vs. Hydraulic Compression Dead-End (NY) vs. Preformed Helical Dead-End</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Preformed Helical Dead-End</th>
      <th>Hydraulic Compression Dead-End (NY)</th>
      <th>YOMIN Bolted Aluminum Strain Clamp (NLL Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Installation Tooling Required</strong></td>
      <td>Manual wrap; requires skilled hand technique.</td>
      <td>Heavy motorized hydraulic compression press (100–200 tons) &amp; dies.</td>
      <td><strong>Standard torque wrench or lineman socket wrench only; zero heavy tooling.</strong></td>
    </tr>
    <tr>
      <td><strong>Reusability &amp; Sag Adjustment</strong></td>
      <td>Single-use: Cannot be unwrapped and re-tensioned safely.</td>
      <td>Non-reusable: Conductor is permanently crushed; must be cut away.</td>
      <td><strong>100% Reusable: U-bolts can be loosened to adjust line sag or re-route spans.</strong></td>
    </tr>
    <tr>
      <td><strong>Conductor Preparation in Field</strong></td>
      <td>Must match exact conductor diameter tolerances.</td>
      <td>Requires stripping aluminum strands to crimp inner steel core.</td>
      <td><strong>Zero Conductor Stripping: Grips complete ACSR conductor over aluminum armor tape.</strong></td>
    </tr>
    <tr>
      <td><strong>Tensile Holding Grip Efficiency</strong></td>
      <td>Approx. 85% to 90% of conductor RTS.</td>
      <td>&ge; 95% of conductor RTS (permanent cold weld).</td>
      <td><strong>Certified &ge; 95% of conductor RTS under IEC 61284 tension testing standards.</strong></td>
    </tr>
    <tr>
      <td><strong>Primary Application in Power Grids</strong></td>
      <td>Telecom cables, guy wires, and light distribution lines.</td>
      <td>Extra-High-Voltage transmission (400kV to 765kV+).</td>
      <td><strong>Sub-transmission &amp; distribution: 11kV, 33kV, 66kV, 110kV dead-end towers &amp; substations.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

SC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-strain-clamp-fr',
    title="Lignes Aériennes de Transport : Qu'est-ce qu'une Pince d'Ancrage (Strain Clamp) ?",
    breadcrumb='Armement de Ligne &amp; Pinces d\'Ancrage',
    read='10 min de lecture',
    alt='Pince d\'ancrage à étriers boulonnés en alliage d\'aluminium (Série NLL) fixée sur une chaîne d\'isolateurs composites à un pylône d\'arrêt de ligne haute tension',
    desc=('Lignes aériennes haute tension (11kV à 220kV), pylônes d\'arrêt et ancrage mécanique des câbles : Qu\'est-ce qu\'une pince d\'ancrage (strain clamp) ? '
          'Corps en alliage d\'aluminium, tenue mécanique à 95% de la charge de rupture du conducteur (RTS), étriers en U à haute résistance et norme CEI 61284.'),
    model='Série NLL / NY : Pinces d\'Ancrage à Boulons et à Compression en Alliage d\'Aluminium pour Conducteurs Nus Almelec / Al-Acier (11kV à 220kV, Tenue >= 95% RTS, CEI 61284)',
    category='Armement de Ligne & Pinces d\'Ancrage / Pinces d\'Ancrage à Boulons',
    kw='pince d ancrage &middot; strain clamp &middot; pince de tension &middot; pince nll &middot; ancrage conducteur acsr &middot; armement ligne aerienne',
    specs=[
        ('Types de Conducteurs Nus Compatibles', 'Conçu pour câbles nus aériens : Al-Acier (ACSR), Almelec (AAAC) et aluminium pur (AAC) de 11kV à 220kV'),
        ('Résistance Mécanique de Tenue au Glissement', 'Efficacité d\'ancrage certifiée : &ge; 95% de la Charge de Rupture Assignée (RTS) du câble sans glissement'),
        ('Matériau du Corps et de la Plaque de Serrage', 'Alliage d\'aluminium moulé sous pression haute résistance (Grade A356 / ZL101A traité thermiquement T6)'),
        ('Boulonnerie en U et Classe d\'Acier', 'Étriers filetés en U forgés en acier haute résistance (Classe 8.8) galvanisés à chaud (ISO 1461 / ASTM A153)'),
        ('Plage de Section Transversale du Câble', 'Gorges d\'amarrage disponibles : de 16 mm&sup2; jusqu\'à 800 mm&sup2; (diamètres extérieurs de &phi;7,0 mm à &phi;38,0 mm)'),
        ('Rapport de Résistance Électrique de Contact', 'Excellente conductivité : rapport de résistance $R_{pince} / R_{conducteur} < 1,0$ (évite tout échauffement ponctuel)'),
        ('Goupille de Sécurité et Axe de Chape', 'Axe en acier forgé galvanisé et goupille fendue en acier inoxydable marin (Grade 304/316) anti-décrochage'),
        ('Normes Internationales de Qualification', 'Conforme et certifié selon les normes CEI 61284, ANSI C119.4 et spécifications d\'armement BS 3288-1')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Pince d\'Ancrage (Strain Clamp) et où est-elle installée sur une ligne aérienne ?',
         'Une Pince d\'Ancrage—couramment désignée sous le nom de pince de tension, pince d\'arrêt ou étrier d\'ancrage—est '
         'une ferrure mécanique haute tension conçue pour enserrer fermement l\'extrémité d\'un conducteur nu '
         'et le relier à une chaîne d\'isolateurs d\'arrêt, reprenant l\'intégralité de la tension mécanique longitudinale de la portée. '
         'Sur les réseaux de transport et de distribution HT : '
         '<ul>'
         '<li><strong>1. Pylônes d\'Arrêt et Terminaux de Poste :</strong> Installée aux extrémités de ligne où le câble s\'ancre '
         'sur le portique du poste électrique. La pince reprend l\'effort de traction tandis qu\'une boucle souple (jumper) '
         'assure la continuité électrique vers le jeu de barres.</li>'
         '<li><strong>2. Pylônes d\'Angle :</strong> Indispensable dès que la ligne change de direction de plus de 15 degrés, '
         'car les pinces de suspension simples ne peuvent résister aux efforts transversaux résultants.</li>'
         '<li><strong>3. Grandes Portées et Traversées de Fleuves :</strong> Sécurise les franchissements exceptionnels de 500 à 1500 mètres '
         'où le poids, le vent et le givre engendrent des tractions de plusieurs tonnes.</li>'
         '</ul>'),
        ('Comment la Pince d\'Ancrage à Boulons garantit-elle 95% de tenue sans cisailler les brins d\'aluminium ?',
         'L\'ancrage d\'un conducteur sous plusieurs tonnes de traction sans détériorer les brins extérieurs en aluminium repose sur une conception sophistiquée : '
         '<ul>'
         '<li><strong>Gorge Ondulée à Profil Sinusoïdal :</strong> Le canal intérieur de serrage des pinces YOMIN NLL présente un profil ondulé continu. '
         'Ce tracé génère une adhérence par effet cabestan sur toute la longueur de la pince, répartissant la retenue mécanique sans écrasement ponctuel.</li>'
         '<li><strong>Crapaudine à Bords Évasés :</strong> La pièce de serrage supérieure présente des extrémités arrondies qui éliminent les arêtes vives. '
         'Au serrage des étriers au couple prescrit, la pression se répartit uniformément sur le ruban d\'armure protégeant le câble.</li>'
         '<li><strong>Tenue Certifiée &ge; 95% RTS :</strong> Lors des essais de traction selon la CEI 61284, la pince résiste à 95% de la rupture du câble '
         'pendant plus de 60 secondes sans aucun glissement des brins.</li>'
         '</ul>'),
        ('Pourquoi privilégier les pinces à boulons par rapport aux manchons rétreints à compression en distribution ?',
         'Si les pinces à compression hexagonale (série NY) sont réservées aux très hautes tensions (400kV), '
         'les <strong>pinces d\'ancrage à étriers boulonnés (série NLL)</strong> s\'imposent en moyenne et haute tension (11kV à 110kV) : '
         '<ul>'
         '<li><strong>Simplicité sans Outillage Lourd :</strong> Seule une clé dynamométrique standard est requise, éliminant les groupes hydrauliques de 100 tonnes en haut des pylônes.</li>'
         '<li><strong>Réglage et Réutilisation :</strong> Les boulons peuvent être desserrés pour ajuster la flèche du câble ou reprendre le tirage lors de la maintenance.</li>'
         '<li><strong>Intégrité du Câble :</strong> Ne nécessite aucun dénudage des brins extérieurs d\'aluminium pour atteindre l\'âme d\'acier.</li>'
         '</ul>')
    ],
    cta='Vous concevez des lignes aériennes haute tension, des pylônes d\'arrêt ou des portiques de sous-stations nécessitant des pinces d\'ancrage en aluminium boulonnées certifiées CEI 61284 (11kV à 220kV, tenue >= 95% RTS) ? YOMIN fabrique des pinces de tension série NLL de haute résistance.',
    body='''
<h2>L\'Ancrage Mécanique Vital des Conducteurs de Lignes Aériennes Haute Tension</h2>
<p>Sur les réseaux de transport et de grand transport d\'électricité franchissant déserts, chaînes de montagnes et vallées à des tensions de <strong>11kV, 33kV, 66kV et 110kV</strong>, les câbles conducteurs sont suspendus sous des tensions mécaniques colossales.</p>
<p>Chaque kilomètre de câble Almelec (AAAC) ou Al-Acier (ACSR) pèse plusieurs tonnes. Sous l\'effet combiné des vents violents et des surcharges de givre hivernal, la traction mécanique exercée sur les supports atteint des dizaines de milliers de newtons.</p>
<p>Si les pinces de suspension suffisent en alignement droit pour porter le poids vertical du câble, elles sont incapables de retenir la traction axiale de la ligne. En cas de pylône d\'arrêt ou de fin de portée, un ancrage mécanique absolu est indispensable pour éviter l\'effondrement en cascade des portées voisines.</p>
<p>La <strong>Pince d\'Ancrage à Boulons en Alliage d\'Aluminium (Série NLL)</strong> apporte la sécurité structurelle indispensable : une ferrure de ligne robuste conçue pour retenir fermement les conducteurs nus avec une efficacité supérieure à 95% de leur charge de rupture (RTS), tout en transférant les efforts sur les bras du pylône.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série NLL</h2>
<ol>
  <li><strong>Corps en Alliage d\'Aluminium Haute Résistance A356 :</strong> Moulage de précision traité T6 offrant une excellente limite élastique, une immunité totale à la corrosion saline et zéro perte par hystérésis magnétique.</li>
  <li><strong>Gorge Ondulée Anti-Glissement :</strong> Profil sinusoïdal assurant une adhérence mécanique par friction progressive sans détérioration des brins conducteurs.</li>
  <li><strong>Étriers en U en Acier Forgé Haute Résistance 8.8 :</strong> Galvanisation à chaud renforcée (> 85 &mu;m) avec rondelles élastiques et double écrou pour résister aux vibrations éoliennes.</li>
  <li><strong>Crapaudine Évasée Protège-Câble :</strong> Entrées et sorties de gorge adoucies pour prévenir toute amorce de rupture par fatigue des brins d\'aluminium.</li>
  <li><strong>Chape d\'Attache Normalisée avec Goupille Inox :</strong> Raccordement direct aux ferrures de chaînes d\'isolateurs d\'arrêt avec goupille fendue de sécurité en acier inox marin.</li>
</ol>
'''
)

SC_ES = dict(
    lang='es',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-strain-clamp-es',
    title='Líneas Aéreas de Transmisión: ¿Qué es una Grapa de Retención (Strain Clamp)?',
    breadcrumb='Herrajes de Línea y Grapas de Retención',
    read='10 min de lectura',
    alt='Grapa de retención apernada en aleación de aluminio (Serie NLL) anclada a una cadena de aisladores poliméricos en una torre de remate de transmisión eléctrica',
    desc=('Líneas aéreas de alta tensión (11kV a 220kV), torres de retención y anclaje mecánico de conductores: ¿Qué es una grapa de retención (strain clamp)? '
          'Cuerpo de aleación de aluminio, sujeción mecánica al 95% de la carga de rotura del conductor (RTS), pernos en U de alta resistencia y norma IEC 61284.'),
    model='Serie NLL / NY: Grapas de Retención Tipo Perno y Compresión en Aleación de Aluminio para Conductores Desnudos ACSR / AAAC (11kV a 220kV, Agarre >= 95% RTS, IEC 61284)',
    category='Herrajes de Línea y Grapas de Retención / Grapas Aperadas de Retención',
    kw='grapa de retencion &middot; strain clamp &middot; grapa de tension apernada &middot; grapa nll &middot; retencion conductor acsr &middot; herrajes de linea alta tension',
    specs=[
        ('Tipos de Conductor Desnudo Compatibles', 'Diseñado para conductores aéreos desnudos: ACSR (Aluminio-Acero), AAAC (Aleación de Aluminio) y AAC (11kV a 220kV)'),
        ('Capacidad Mecánica de Agarre Certificada', 'Eficiencia de retención mecánica: &ge; 95% de la Carga de Rotura Asignada (RTS) del conductor sin deslizamiento'),
        ('Material del Cuerpo y Placa Presora', 'Aleación de aluminio fundido de alta resistencia mecánica (Grado A356 / ZL101A con tratamiento térmico T6)'),
        ('Tornillería en U y Clase de Resistencia', 'Pernos en U forjados en acero de alta resistencia (Grado 8.8) galvanizados por inmersión en caliente (ISO 1461)'),
        ('Rango de Sección Transversal del Conductor', 'Capacidades de garganta de amarre: desde 16 mm&sup2; hasta 800 mm&sup2; (diámetros exteriores de &phi;7,0 mm a &phi;38,0 mm)'),
        ('Relación de Resistencia Eléctrica de Contacto', 'Excelente conductividad: relación de resistencia $R_{grapa} / R_{conductor} < 1,0$ (elimina sobrecalentamientos térmicos)'),
        ('Pasador de Seguridad y Perno de Horquilla', 'Perno de acero forjado galvanizado y pasador de seguridad tipo chaveta en acero inoxidable marino (Grado 304/316)'),
        ('Normas Internacionales de Ensayo en Redes', 'Ensayado y conforme bajo normas internacionales IEC 61284, ANSI C119.4 y especificaciones BS 3288-1')
    ],
    faqs=[
        ('¿Qué es una Grapa de Retención (Strain Clamp) y cuál es su función en líneas aéreas?',
         'Una Grapa de Retención—conocida también como grapa terminal, grapa de anclaje, grapa de tensión apernada o grapa pistola—es '
         'un herraje electromecánico de alta tensión diseñado para sujetar con extrema firmeza el extremo de un conductor aéreo desnudo '
         'y anclarlo a una cadena de aisladores de retención, transfiriendo la totalidad de la tensión longitudinal del vano a la torre. '
         'En redes de transmisión y distribución de alta tensión (11kV a 220kV) : '
         '<ul>'
         '<li><strong>1. Torres de Remate y Pórticos de Subestación:</strong> Donde la línea aérea finaliza e ingresa a una subestación. '
         'La grapa soporta toda la tensión del cable mientras un puente flojo (jumper) conduce la corriente hacia las barras.</li>'
         '<li><strong>2. Torres de Ángulo:</strong> Indispensable en desvíos de línea superiores a 15 grados, donde las grapas de suspensión '
         'no soportarían las enormes fuerzas vectoriales resultantes.</li>'
         '<li><strong>3. Cruces de Ríos y Valles Profundos:</strong> En vanos extraordinarios de 500 a 1500 metros donde el viento y el hielo '
         'generan tensiones mecánicas de decenas de miles de kilogramos.</li>'
         '</ul>'),
        ('¿Cómo logra una Grapa Apernada más del 95% de agarre sin dañar los hilos de aluminio?',
         'Retener un cable sometido a toneladas de tensión sin estrangular los hilos exteriores de aluminio requiere un diseño hidrodinámico de presiones : '
         '<ul>'
         '<li><strong>Garganta Ondulada Sinusoidal:</strong> El canal interior de las grapas YOMIN NLL cuenta con un perfil ondulado continuo. '
         'Este diseño genera fricción mecánica por efecto cabrestante en toda la longitud de contacto, distribuyendo la fuerza de retención sin cortes puntuales.</li>'
         '<li><strong>Mordaza con Bordes Abocinados:</strong> La placa superior presora tiene bordes redondeados que previenen concentraciones de esfuerzo cortante '
         'al apretar los pernos en U al torque recomendado.</li>'
         '<li><strong>Certificación &ge; 95% RTS:</strong> En ensayos destructivos bajo norma IEC 61284, la grapa soporta el 95% de la rotura del conductor '
         'durante más de un minuto sin registrar ningún deslizamiento de hebras.</li>'
         '</ul>'),
        ('¿Por qué elegir grapas apernadas en lugar de manguitos de compresión hidráulica en distribución?',
         'Mientras que las grapas a compresión hexagonal (serie NY) se usan en ultra alta tensión (400kV), '
         'las <strong>grapas apernadas de aleación de aluminio (serie NLL)</strong> dominan en media y alta tensión (11kV a 110kV) : '
         '<ul>'
         '<li><strong>Instalación Sencilla sin Equipos Pesados:</strong> Solo se necesita una llave de torque estándar, sin cargar pesadas bombas hidráulicas en la torre.</li>'
         '<li><strong>Reutilización y Ajuste de Flecha:</strong> Se pueden aflojar los pernos para regular la catenaria del cable o tensar vanos durante el mantenimiento.</li>'
         '<li><strong>Sin Daño al Conductor:</strong> Se instala directamente sobre el cable con cinta de armadura de aluminio sin cortar los hilos conductores.</li>'
         '</ul>')
    ],
    cta='¿Diseña líneas aéreas de alta tensión, torres de remate o pórticos de subestaciones que requieren grapas de retención apernadas de aluminio certificadas IEC 61284 (11kV a 220kV, agarre >= 95% RTS)? YOMIN suministra grapas de retención serie NLL de máxima confiabilidad.',
    body='''
<h2>El Anclaje Mecánico Vital para Conductores en Líneas Aéreas de Transmisión</h2>
<p>En redes de transmisión y distribución de energía eléctrica que cruzan valles, desiertos y montañas bajo tensiones de <strong>11kV, 33kV, 66kV y 110kV</strong>, los conductores aéreos penden suspendidos bajo tensiones mecánicas descomunales.</p>
<p>Cada kilómetro de cable de aluminio con alma de acero (ACSR) o aleación de aluminio (AAAC) pesa miles de kilogramos. En épocas de tormentas con vientos cruzados y acumulación de hielo, las fuerzas de tracción que tiran de las estructuras alcanzan decenas de miles de newtons.</p>
<p>Si bien las grapas de suspensión soportan el peso vertical del cable en alineaciones rectas, son incapaces de resistir la tracción axial de la línea. En torres de remate o cambios de ángulo, un anclaje mecánico seguro es imperativo para evitar que la caída de un tramo colapse las torres adyacentes en cadena.</p>
<p>La <strong>Grapa de Retención Apernada de Aleación de Aluminio (Serie NLL)</strong> constituye el elemento estructural de confianza: un herraje de alta resistencia diseñado para abrazar conductores desnudos con una fuerza superior al 95% de su carga de rotura (RTS), transfiriendo la tensión hacia la cruceta de la torre con total seguridad.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie NLL</h2>
<ol>
  <li><strong>Cuerpo Fundido en Aleación de Aluminio A356-T6:</strong> Fundición de precisión tratada térmicamente que ofrece alta resistencia mecánica, cero pérdidas por histéresis magnética e inmunidad total a la corrosión ambiental.</li>
  <li><strong>Garganta Ondulada Anti-Deslizamiento:</strong> Perfil curvo diseñado para maximizar la fricción de agarre por contacto sin aplastar los hilos externos del conductor.</li>
  <li><strong>Pernos en U de Acero Estructural Grado 8.8:</strong> Galvanizados por inmersión en caliente con espesores mayores a 85 &mu;m, equipados con arandelas de presión y doble tuerca contra vibraciones eólicas.</li>
  <li><strong>Mordaza Presora Abocinada:</strong> Bordes de entrada y salida pulidos y redondeados que protegen los hilos de aluminio contra la fatiga por oscilación.</li>
  <li><strong>Horquilla de Anclaje con Pasador Inoxidable:</strong> Conexión directa a las cadenas de aisladores con pasador de seguridad en acero inoxidable grado marino que previene desenganches accidentales.</li>
</ol>
'''
)

SC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='overhead-transmission-lines-what-is-a-strain-clamp-ar',
    title='خطوط النقل الهوائية وأبراج الشد: ما هو مشبك الشد الميكانيكي (Strain Clamp)؟',
    breadcrumb='مهمات خطوط النقل ومشابك الشد',
    read='10 دقائق قراءة',
    alt='مشبك شد ميكانيكي بمسامير من سبائك الألومنيوم (موديل NLL) مثبت في سلسلة عوازل مركبة على برج شد نهائي لخط نقل كهربائي للجهد العالي',
    desc=('خطوط نقل الكهرباء الهوائية للجهد العالي (11kV إلى 220kV)، وأبراج الشد النهائية، وتثبيت الموصلات العارية: ما هو مشبك الشد (Strain Clamp)؟ '
          'هيكل سبائك الألومنيوم، وقوة إمساك ميكانيكية تعادل 95% من قوة شد الموصل (RTS)، ومسامير U عالية المتانة ومعايير IEC 61284.'),
    model='سلسلة NLL / NY: مشابك الشد الميكانيكية المربوطة بمسامير والكبس الهيدروليكي للموصلات العارية ACSR / AAAC (11kV إلى 220kV، قوة إمساك >= 95% RTS، معتمدة IEC 61284)',
    category='مهمات خطوط النقل ومشابك الشد / مشابك الشد المربوطة بمسامير',
    kw='مشبك شد خطوط نقل &middot; strain clamp &middot; مشبك شد ميكانيكي &middot; مشبك nll &middot; شد موصل acsr &middot; مهمات شبكات هوائية',
    specs=[
        ('أنواع الموصلات العارية المتوافقة', 'مصمم للموصلات العارية الهوائية: موصلات الألومنيوم المقواة بالصلب (ACSR)، وسبائك الألومنيوم (AAAC)، والألومنيوم النقي (AAC)'),
        ('قوة الإمساك الميكانيكي المقننة ضد الانزلاق', 'كفاءة إمساك ميكانيكية فائقة: &ge; 95% من قوة الشد القصوى الاسمية للموصل (RTS) دون أي انزلاق للشعيرات'),
        ('مادة تصنيع جسم المشبك ولوح الضغط', 'سبائك ألومنيوم مسبوكة عالية الصلابة ومقاومة للتآكل (فئة A356 / ZL101A معالجة حرارياً بتقنية T6)'),
        ('مواصفات مسامير الربط على شكل حرف U', 'مسامير U مشكلة من صلب عالي الإجهاد (فئة 8.8) ومجلفنة بالغمس الساخن (مطابقة لـ ISO 1461 / ASTM A153)'),
        ('نطاق مقاطع الموصلات الهوائية المتاحة', 'مجاري تثبيت تناسب مقاطع الكابلات: من 16 مم&sup2; حتى 800 مم&sup2; (أقطار خارجية للكابل من &phi;7.0 مم إلى &phi;38.0 مم)'),
        ('نسبة المقاومة والتوصيل الكهربائي بالتلامس', 'توصيل كهربائي ممتاز: نسبة مقاومة التلامس $R_{clamp} / R_{conductor} < 1.0$ (تمنع السخونة ونقاط الاحتراق)'),
        ('مسمار الشكيمة وتيلة الأمان المقاومة للصدأ', 'محور شكيمة مجلفن مع تيلة أمان مقوسة من الفولاذ المقاوم للصدأ البحري (درجة 304/316) لمنع الانفلات'),
        ('المواصفات القياسية الدولية لشبكات الكهرباء', 'مختبر ومعتمد بالكامل وفقاً للمواصفات الدولية IEC 61284 و ANSI C119.4 و BS 3288-1')
    ],
    faqs=[
        ('ما هو مشبك الشد الميكانيكي (Strain Clamp) وما هي وظيفته في خطوط النقل الهوائية؟',
         'مشبك الشد الميكانيكي—والمعروف في قطاع شبكات الكهرباء باسم مشبك التثبيت النهائي (Dead-End Clamp) أو مشبك الشد بالمسامير المسدس—هو '
         'قطعة معدنية هندسية مخصصة للجهد العالي صُممت للإمساك المحكم بنهاية موصل النقل الهوائي العاري '
         'وتثبيته في سلسلة عوازل الشد، ناقلاً كامل قوى الشد الميكانيكية الطولية للموصل إلى ذراع البرج الحديدي بأمان تام. '
         'وعلى طول مسارات خطوط النقل والتوزيع (من 11kV إلى 220kV وأكثر): '
         '<ul>'
         '<li><strong>1. أبراج النهاية والربط بمحطات التحويل:</strong> حيث ينتهي الخط الهوائي ويرتبط بساحة المحطة؛ يتحمل المشبك '
         'كامل الشد الميكانيكي، بينما تقوم وصلة كوبري مرنة غير مشدودة (Jumper) بنقل التيار الكهربائي إلى قضبان التوزيع.</li>'
         '<li><strong>2. أبراج الزاوية والانعطاف:</strong> تستخدم عند تغير اتجاه مسار الخط بأكثر من 15 درجة، '
         'حيث تعجز مشابك التعليق العادية عن تحمل قوى محصلة المتجهات الجانبية العنيفة.</li>'
         '<li><strong>3. مسافات عبور الأنهار والوديان:</strong> لتثبيت الموصلات في البحور الهوائية الشاسعة (من 500 إلى 1500 متر) '
         'حيث تؤدي الرياح الشديدة وتراكم الثلوج إلى توليد قوى شد ميكانيكية تصل لعشرات الأطنان.</li>'
         '</ul>'),
        ('كيف يحقق مشبك الشد قوة إمساك تتجاوز 95% دون سحق شعيرات الألومنيوم الحساسة؟',
         'يتطلب تثبيت موصل ألومنيوم تحت أطنان من قوى الشد دون الإضرار بالشعيرات الخارجية تصميماً هندسياً دقيقاً لتوزيع الإجهادات : '
         '<ul>'
         '<li><strong>مجرى تثبيت متموج بانحناء جيبي:</strong> يحتوي المجرى الداخلي لمشابك يمين NLL على تعرجات جيبية انسيابية. '
         'تولد هذه التموجات قوى احتكاك ميكانيكية هائلة على طول الكابل بفعل ظاهرة الاحتكاك الالتفافي (Capstan Effect) دون الضغط الساحق على نقطة واحدة.</li>'
         '<li><strong>لوح ضغط علوي بحواف بوقية مقوسة:</strong> صُمم لوح الضغط بحواف مائلة ناعمة تمنع الحواف الحادة من حز أسلاك الألومنيوم عند شد مسامير U بالعزم المطلوب.</li>'
         '<li><strong>شهادة صمود &ge; 95% RTS:</strong> في الاختبارات الميكانيكية المعتمدة وفقاً لـ IEC 61284، يصمد المشبك لقوة شد تعادل 95% من أقصى قوة شد للموصل '
         'لأكثر من 60 ثانية دون أي انزلاق.</li>'
         '</ul>'),
        ('لماذا تفضل مشابك الشد بالمسامير على وصلات الكبس الهيدروليكي في خطوط التوزيع؟',
         'بينما تستخدم مشابك الكبس الهيدروليكي الدائمة (سلسلة NY) في خطوط الجهد الفائق (400kV)، '
         'فإن <strong>مشابك الشد بالمسامير المصنوعة من الألومنيوم (سلسلة NLL)</strong> تسيطر على شبكات الجهد المتوسط والعالي (11kV إلى 110kV) لمزايا حاسمة : '
         '<ul>'
         '<li><strong>سهولة التركيب دون معدات ثقيلة:</strong> تحتاج فقط لمفتاح عزم يدوي قياسي، ملغيةً الحاجة لرفع مكابس هيدروليكية تزن مئات الكيلوجرامات فوق الأبراج.</li>'
         '<li><strong>قابلية الفك وتعديل ترخيم الخط:</strong> يمكن فك المسامير لإعادة ضبط ترخيم الكابل (Sag) أو صيانة الخط دون الحاجة لقطع الموصل.</li>'
         '<li><strong>سلامة الموصل:</strong> يمسك المشبك بكامل مقطع الموصل مباشرة فوق شريط الحماية دون تقشير شعيرات الألومنيوم للوصول للقلب الصلب.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصميم خطوط النقل الهوائية للجهد العالي، أو أبراج الشد والنهايات، أو ساحات محطات التحويل التي تتطلب مشابك شد ميكانيكية بمسامير من الألومنيوم معتمدة IEC 61284 (جهد 11kV إلى 220kV، وقوة إمساك >= 95% RTS)؟ تصنع يمين (YOMIN) مشابك الشد سلسلة NLL بأعلى درجات المتانة.',
    body='''
<h2>المرساة الميكانيكية الصلبة المعلقة لخطوط النقل الكهربائي الهوائية</h2>
<p>عبر شبكات نقل وتوزيع الكهرباء الوطنية التي تقطع الصحاري والوديان وسلاسل الجبال بجهود <strong>11kV و 33kV و 66kV و 110kV</strong>، تظل الموصلات الهوائية معلقة في الهواء تحت إجهادات شد ميكانيكية بالغة القسوة.</p>
<p>يزن كل كيلومتر من موصلات الألومنيوم المقواة بقلب صلب (ACSR) أو سبائك الألومنيوم (AAAC) آلاف الكيلوجرامات. ومع هبوب العواصف الشتوية وتراكم الثلوج، تقفز قوى الشد الطولية المؤثرة على الأبراج إلى عشرات الآلاف من النيوتنات.</p>
<p>وفي حين تقوم مشابك التعليق العادية بحمل الوزن الرأسي للموصل فقط في المسارات المستقيمة، فإنها تعجز تماماً عن مقاومة الشد الطولي للمسار. وعند أبراج النهاية والزوايا، يصبح وجود تثبيت ميكانيكي حاسم أمراً لا غنى عنه لمنع انهيار أبراج الخط بصورة متسلسلة.</p>
<p>يقدم <strong>مشبك الشد الميكانيكي بالمسامير المصنوع من سبائك الألومنيوم (سلسلة NLL)</strong> المرساة الهيكلية المعتمدة هندسياً: قطعة خطوط فائقة الصلابة صُممت للإمساك المحكم بالموصلات العارية بقوة صمود تتجاوز 95% من قوة شد الموصل، ناقلةً هذه الأحمال بأمان تام إلى أذرع الأبراج الحديدية.</p>

<h2>المكونات الهندسية وميزات التصميم لسلسلة مشابك NLL</h2>
<ol>
  <li><strong>هيكل مسبوك من سبائك الألومنيوم A356-T6:</strong> سباكة عالية الكثافة معالجة حرارياً توفر متانة شد ميكانيكية خارقة، مع انعدام الفقد المغناطيسي ومقاومة تامة للتآكل في البيئات الرطبة والصحراوية.</li>
  <li><strong>مجرى تثبيت مموج مضاد للانزلاق:</strong> تصميم انسيابي يضاعف الاحتكاك الميكانيكي بالتماس دون التسبب في سحق أو تشويه الشعيرات الخارجية للموصل.</li>
  <li><strong>مسامير U من الصلب عالي الإجهاد فئة 8.8:</strong> مجلفنة بالغمس الساخن بسماكة تتجاوز 85 ميكرون، ومزودة بحلقات زنبركية وصواميل مزدوجة لمقاومة الاهتزازات الهوائية.</li>
  <li><strong>لوح ضغط علوي بحواف بوقية مقوسة:</strong> أطراف مشطوفة تمنع الإجهاد الحاد عند مداخل ومخارج المشبك لتحمي الكابل من شروخ الكلال الناتجة عن تمايل الرياح.</li>
  <li><strong>وصلة شكيمة معيارية وتيلة أمان ستانلس ستيل:</strong> تثبيت مباشر في حلقات سلاسل العوازل مع تيلة أمان بحرية تمنع أي انفلات عرضي تحت الاهتزازات.</li>
</ol>
'''
)

# ==============================================================================
# 2. MEDIUM VOLTAGE CURRENT TRANSFORMER (EN, FR, ES, AR)
# ==============================================================================

MVCT_EN = dict(
    lang='en',
    dir='ltr',
    slug='medium-voltage-substations-what-is-a-medium-voltage-current-transformer',
    title='Medium-Voltage Substations: What Is a Medium-Voltage Current Transformer?',
    breadcrumb='Medium-Voltage Switchgear &amp; Instrument CTs',
    read='10 min read',
    alt='Three medium-voltage cast epoxy resin Current Transformers (Model LZZBJ9 series, 12kV rating) installed upright with copper busbars inside an air-insulated switchgear cubicle',
    desc=('Medium-voltage electrical substations (10kV to 35kV), primary distribution switchgear, and ring main units (RMU): What is a medium-voltage current transformer? '
          'How vacuum-cast cycloaliphatic epoxy resin, dual-core metering (0.2S) and protection (5P10/10P10), 31.5kA short-time thermal ratings, and IEC 61869-2 standards isolate instrumentation.'),
    model='Model LZZBJ9 / LZBW Series 10kV–35kV Cast Epoxy Resin Medium-Voltage Instrument Current Transformers (Dual Cores 0.2S / 5P10, 5A to 3150A, Ith up to 31.5kA / 3s, IEC 61869-2)',
    category='Medium-Voltage Switchgear & Instrument CTs / Cast Resin Current Transformers',
    kw='what is a medium voltage current transformer &middot; medium voltage current transformer &middot; mv current transformer &middot; 10kv current transformer epoxy &middot; cast resin ct 33kv &middot; lzzbj9 ct',
    specs=[
        ('Rated System Operating Voltage Class ($U_m$)', 'Medium-voltage distribution ratings: 10kV / 12kV, 24kV, and 36kV / 40.5kV AC (50/60 Hz, 3-Phase AIS/GIS)'),
        ('Rated Primary Current Range ($I_{pn}$)', 'Standard primary ratings: 5A, 10A, 15A, 20A, 30A, 50A, 100A, 200A, 400A, 600A, 1000A, 1250A, up to 3150A'),
        ('Rated Secondary Output Currents ($I_{sn}$)', 'Standard switchgear secondary dual-output ratings: 5 A or 1 A (Core 1: 1S1-1S2; Core 2: 2S1-2S2)'),
        ('Dual Core Configuration & Accuracy Classes', 'Dual-core architecture: Core 1: Class 0.2S / 0.5 (Revenue Metering); Core 2: Class 5P10 / 10P10 (Protection Relaying)'),
        ('Short-Time Thermal Current Withstand ($I_{th}$)', 'Heavy short-circuit thermal withstand: up to 31.5 kA for 3.0 seconds (Dynamic peak current $I_{dyn} \ge 2.5 \times I_{th}$)'),
        ('Insulation Material & Casting Technology', 'Automatic Pressure Gelation (APG) vacuum-cast cycloaliphatic epoxy resin (Class E / Class B insulation rating)'),
        ('Partial Discharge (PD) Level Certification', 'Ultra-low partial discharge: $< 10$ pC at $1.2 U_m / \sqrt{3}$ (guarantees 30+ year insulation service life)'),
        ('Power-Frequency & Lightning Impulse (BIL)', 'Dry power frequency withstand: up to 95 kV (1 min); Lightning impulse withstand (BIL): up to 200 kV peak (1.2/50 &mu;s)')
    ],
    faqs=[
        ('What is a Medium-Voltage Current Transformer (MV CT) and why is cast epoxy resin insulation essential?',
         'A Medium-Voltage Current Transformer—frequently designated as an MV instrument transformer, cast resin CT, or 10kV–35kV measuring/protection transformer—is '
         'a specialized instrument transformer designed to operate in medium-voltage power distribution networks (10kV to 35kV) '
         'to safely scale down heavy primary phase currents to standardized secondary values (5A or 1A) for digital protection relays, '
         'tariff energy meters, and SCADA monitoring equipment. '
         'In medium-voltage switchgear and distribution substations: '
         '<ul>'
         '<li><strong>The Dielectric Isolation Barrier:</strong> Low-voltage 0.66kV CTs rely on simple plastic shells and cannot withstand '
         'kilovolts of operating potential or transient lightning impulses (reaching 75kV at 12kV, or 170kV at 36kV). '
         'YOMIN LZZBJ9 series MV CTs utilize vacuum-cast cycloaliphatic epoxy resin processed via Automatic Pressure Gelation (APG). '
         'The monolithic solid resin casting forms a void-free, moisture-proof hermetic encapsulation that withstands 42kV power frequency voltage '
         'and 95kV lightning impulses, completely isolating sensitive low-voltage digital relays from dangerous medium-voltage potential.</li>'
         '<li><strong>Zero Maintenance &amp; Non-Flammable Safety:</strong> Unlike legacy oil-filled transformers that leak oil, require maintenance, '
         'and pose severe fire/explosion hazards inside indoor switchgear rooms, dry-type cast resin CTs are self-extinguishing, maintenance-free, '
         'and environmentally benign.</li>'
         '</ul>'),
        ('Why do Medium-Voltage CTs feature Dual Cores: Class 0.2S Metering vs. Class 5P10 Protection?',
         'A single magnetic core cannot simultaneously satisfy the conflicting physics of tariff metering and short-circuit fault protection: '
         '<ul>'
         '<li><strong>Core 1 — High-Precision Revenue Metering (Class 0.2S, Instrument Security Factor FS5):</strong> '
         'Wound from high-permeability nanocrystalline or nickel-iron alloy with an extremely narrow hysteresis loop. '
         'It maintains &plusmn;0.2% measurement accuracy even at tiny load currents (from 1% to 120% of rated current). '
         'Crucially, its core is designed to <strong>saturate early (FS &le; 5)</strong> during short-circuit faults, capping secondary current '
         'and protecting delicate digital power meters from thermal burnout.</li>'
         '<li><strong>Core 2 — Protective Relaying (Class 5P10 / 10P10, Accuracy Limit Factor ALF10/ALF20):</strong> '
         'Wound from high-saturation cold-rolled grain-oriented silicon steel (CRGO). '
         'It is engineered <strong>NOT to saturate</strong> even when primary currents spike to 10 or 20 times nominal current ($10 \times I_n$) during severe short-circuit faults. '
         'This guarantees that protection relays receive linear secondary current signals to execute instantaneous trip commands in under 20 milliseconds.</li>'
         '</ul>'),
        ('What is Partial Discharge (PD) and why must it be certified below 10 pC under IEC 61869-2?',
         'Partial discharge refers to localized microscopic electrical sparks occurring inside tiny air bubbles, voids, or delamination cracks '
         'trapped within the solid epoxy resin casting during manufacturing. '
         'Under continuous 10kV to 35kV electrical stress, ongoing partial discharges emit ozone, ultraviolet radiation, and nitric acid, '
         'gradually eroding the solid epoxy from the inside out until a catastrophic flashover shatters the CT and burns out the switchgear panel. '
         'YOMIN LZZBJ9 series CTs are manufactured using advanced vacuum de-gassing and high-pressure APG injection molds, '
         'guaranteeing factory routine partial discharge levels certified <strong>below 10 pico-coulombs (< 10 pC at 1.2 Um)</strong>, '
         'ensuring a proven operational lifespan exceeding 30 years without dielectric degradation.')
    ],
    cta='Designing medium-voltage air-insulated switchgear (AIS), compact ring main units (RMU), renewable substation metering bays, or distribution feeder panels requiring certified IEC 61869-2 cast epoxy resin current transformers (10kV to 35kV, dual 0.2S / 5P10 cores, Ith up to 31.5kA)? YOMIN manufactures precision LZZBJ9 series MV CTs.',
    body='''
<h2>The Indispensable Dielectric Guardian for Medium-Voltage Power Distribution Switchgear</h2>
<p>Inside every medium-voltage electrical substation, industrial power distribution room, compact ring main unit (RMU), and renewable wind/solar grid interconnection bay operating at <strong>10kV, 12kV, 24kV, and 33kV/36kV</strong>, measuring current accurately while isolating high voltages is a critical safety imperative.</p>
<p>Medium-voltage switchgear busbars carry thousands of amperes under severe continuous operating voltages. If dangerous 10kV–35kV potentials were allowed to flash over into secondary control wiring, delicate digital protection relays and energy meters would vaporize instantly, endangering human substation operators.</p>
<p>Furthermore, when heavy short-circuit faults erupt downstream—such as underground cable punctures or transformer phase-to-phase flashovers—fault currents explode to 25,000 or 31,500 amperes within milliseconds.</p>
<p>The <strong>Cast Epoxy Resin Medium-Voltage Current Transformer (Model LZZBJ9 / LZBW Series)</strong> provides the universal engineering benchmark: a robust dry-type pillar instrument transformer vacuum-cast from high-grade cycloaliphatic epoxy resin, delivering multi-core Class 0.2S precision metering and Class 5P10 protection under full IEC 61869-2 certification.</p>

<h2>Engineering Anatomy: Inside a Model LZZBJ9 Medium-Voltage Cast Resin Current Transformer</h2>
<ol>
  <li><strong>Monolithic Vacuum-Cast Epoxy Resin Body:</strong> Manufactured using the Automatic Pressure Gelation (APG) process with electrical-grade cycloaliphatic epoxy resin and micro-fine silica filler. Provides impervious hermetic sealing, zero oil leakage hazard, high mechanical cantilever rigidity, and permanent track-resistant insulation.</li>
  <li><strong>High-Conductivity Primary Copper Terminals (P1, P2):</strong> Thick silver-plated electrolytic copper terminal pads engineered with standard dual-bolt hole patterns to accept direct bolting of medium-voltage copper busbars with minimal joint resistance.</li>
  <li><strong>Independent Dual Magnetic Cores:</strong> Houses two completely isolated secondary windings wound on separate magnetic cores: a high-permeability nanocrystalline core for Class 0.2S revenue billing, and a high-saturation CRGO silicon steel core for Class 5P10 / 10P10 protection relaying.</li>
  <li><strong>Enclosed Secondary Terminal Box with Lead-Sealing Cover:</strong> Flame-retardant clear terminal compartment at the base houses robust brass screw terminals (1S1-1S2, 2S1-2S2) and dedicated earth terminal, complete with wire sealing holes to prevent commercial energy theft.</li>
  <li><strong>Short-Circuit Thermal Rating ($I_{th} = 31.5$ kA / 3s):</strong> Engineered internal copper conductor geometry and mechanical resin bonding withstand violent electromagnetic repulsion forces ($I_{dyn} \ge 80$ kA peak) and thermal short-circuit energy without internal cracking.</li>
</ol>

<h2>Comparison: Vacuum Cast Resin MV CT (LZZBJ9) vs. Legacy Oil-Immersed MV CT vs. Low-Voltage CT with Cable Sleeve</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Metric</th>
      <th>Low-Voltage CT over Insulated Cable</th>
      <th>Legacy Oil-Immersed Medium-Voltage CT</th>
      <th>YOMIN Cast Epoxy Resin MV CT (LZZBJ9 Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Insulation Voltage &amp; Dielectric Safety</strong></td>
      <td>Unsafe: Relies entirely on cable outer sheath; zero BIL lightning protection.</td>
      <td>High: Insulating transformer mineral oil; but prone to moisture ingress.</td>
      <td><strong>Superior Solid Dielectric: Vacuum-cast resin withstands 95kV BIL &amp; 42kV power frequency.</strong></td>
    </tr>
    <tr>
      <td><strong>Fire &amp; Explosion Hazard in Switchgear</strong></td>
      <td>High risk of flashover if cable insulation degrades over time.</td>
      <td>Severe Hazard: Combustible oil can rupture violently during internal arc faults.</td>
      <td><strong>Zero Fire Hazard: Solid self-extinguishing epoxy resin eliminates oil explosion risks.</strong></td>
    </tr>
    <tr>
      <td><strong>Maintenance &amp; Oil Sampling Requirements</strong></td>
      <td>Frequent cable inspection required.</td>
      <td>High: Requires annual oil dielectric breakdown testing and gasket replacement.</td>
      <td><strong>100% Maintenance-Free: Hermetically sealed solid-state dry casting lasts 30+ years.</strong></td>
    </tr>
    <tr>
      <td><strong>Measurement Accuracy &amp; Dual Core Capability</strong></td>
      <td>Single core only; lower accuracy due to large cable air gap.</td>
      <td>Dual core available; but bulky oil expansion bellows increase footprint.</td>
      <td><strong>Certified Dual Cores: Class 0.2S Revenue Metering + Class 5P10 / 10P10 Protective Relaying.</strong></td>
    </tr>
    <tr>
      <td><strong>Switchgear Space &amp; Mounting Orientation</strong></td>
      <td>Requires extra cable compartment height.</td>
      <td>Must remain upright; cannot be tilted or mounted horizontally.</td>
      <td><strong>Compact Pillar Design: Mounts upright or horizontal inside standard 11kV/33kV switchgear cubicles.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MVCT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='medium-voltage-substations-what-is-a-medium-voltage-current-transformer-fr',
    title="Postes Moyenne Tension : Qu'est-ce qu'un Transformateur de Courant Moyenne Tension (MV CT) ?",
    breadcrumb='Appareillage Moyenne Tension &amp; Transformateurs de Mesure',
    read='10 min de lecture',
    alt='Trois transformateurs de courant moyenne tension en résine époxy moulée sous vide (Série LZZBJ9, 12kV) installés dans une cellule de tableau électrique MT',
    desc=('Postes de transformation moyenne tension (10kV à 35kV), cellules de distribution primaire et tableaux RMU : Qu\'est-ce qu\'un transformateur de courant moyenne tension (MV CT) ? '
          'Résine époxy cycloaliphatique moulée sous vide, double circuit mesure (0.2S) et protection (5P10/10P10), tenue thermique 31,5kA et norme CEI 61869-2.'),
    model='Série LZZBJ9 / LZBW : Transformateurs de Courant Moyenne Tension en Résine Moulée (10kV à 35kV, Double Noyau 0.2S / 5P10, 5A à 3150A, CEI 61869-2)',
    category='Appareillage Moyenne Tension & Transformateurs de Mesure / Transformateurs de Courant en Résine Moulée',
    kw='transformateur de courant moyenne tension &middot; tc moyenne tension &middot; transformateur de mesure 10kv &middot; tc resine 33kv &middot; lzzbj9 tc &middot; transformateur de courant cellule',
    specs=[
        ('Tension Assignée d\'Isolement de Service ($U_m$)', 'Réseaux de distribution moyenne tension : 10kV / 12kV, 24kV et 36kV / 40,5kV AC (50/60 Hz, cellules MT)'),
        ('Plage de Courant Primaire Assigné ($I_{pn}$)', 'Calibres primaires normalisés : 5A, 10A, 20A, 50A, 100A, 200A, 400A, 600A, 1000A, 1250A jusqu\'à 3150A'),
        ('Courants Secondaires Assignés de Sortie ($I_{sn}$)', 'Standard pour appareillage de contrôle-commande : 5 A ou 1 A (Noyau 1 : 1S1-1S2 ; Noyau 2 : 2S1-2S2)'),
        ('Architecture Double Noyau et Classes de Précision', 'Double circuit magnétique indépendant : Noyau 1 Classe 0.2S / 0.5 (Comptage) ; Noyau 2 Classe 5P10 / 10P10 (Protection)'),
        ('Courant Thermique de Court-Circuit ($I_{th}$)', 'Tenue thermique élevée en court-circuit : jusqu\'à 31,5 kA pendant 3,0 secondes ($I_{dyn} \ge 2,5 \times I_{th}$)'),
        ('Technologie de Moulage et Résine Diélectrique', 'Moulage sous vide par procédé APG en résine époxy cycloaliphatique (classe thermique d\'isolement E / B)'),
        ('Niveau de Décharges Partielles Garanti', 'Décharges partielles ultra-faibles certifiées : $< 10$ pC à $1,2 U_m / \sqrt{3}$ (durée de vie diélectrique $> 30$ ans)'),
        ('Tension de Tenue à Fréquence Industrielle & BIL', 'Tenue à fréquence industrielle : jusqu\'à 95 kV (1 min) ; onde de choc de foudre (BIL) : jusqu\'à 200 kV crête')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transformateur de Courant Moyenne Tension et pourquoi la résine moulée est-elle incontournable ?',
         'Un Transformateur de Courant Moyenne Tension (TC MT)—également appelé transformateur de mesure en résine moulée ou TC 10kV–35kV—est '
         'un appareil de mesure inductif conçu pour les réseaux de distribution moyenne tension (10kV à 35kV) '
         'afin d\'abaisser avec précision les courants de ligne élevés vers des valeurs secondaires normalisées (5A ou 1A) exploitables '
         'par les relais de protection numériques, compteurs d\'énergie de facturation et automates de téléconduite. '
         'Dans les postes et cellules MT : '
         '<ul>'
         '<li><strong>La Barrière d\'Isolement Diélectrique :</strong> Les TC basse tension (0,66kV) ne peuvent supporter les dizaines de kilovolts '
         'de tension de service ni les ondes de choc de foudre (atteignant 75kV à 95kV). Les TC YOMIN LZZBJ9 sont moulés d\'un seul bloc '
         'en résine époxy cycloaliphatique sous vide par procédé APG. Cet isolant solide et étanche assure une séparation diélectrique absolue '
         'entre les barres MT sous tension et les circuits de contrôle BT.</li>'
         '<li><strong>Sécurité Incendie et Zéro Maintenance :</strong> Contrairement aux anciens TC à bain d\'huile sujets aux fuites et aux explosions, '
         'les TC secs en résine sont auto-extinguibles, ininflammables et ne requièrent aucun entretien pendant 30 ans.</li>'
         '</ul>'),
        ('Pourquoi intégrer un Double Noyau : Noyau Mesure Classe 0.2S vs. Noyau Protection Classe 5P10 ?',
         'Un circuit magnétique unique ne peut concilier les exigences opposées du comptage de haute précision et de la protection en court-circuit : '
         '<ul>'
         '<li><strong>Noyau 1 — Comptage Transactionnel (Classe 0.2S, Facteur de Sécurité FS &le; 5) :</strong> '
         'Fabriqué en matériau nanocristallin à très haute perméabilité, il maintient une précision de &plusmn;0,2% de 1% à 120% de la charge. '
         'Il est conçu pour <strong>saturer rapidement en cas de court-circuit (FS &le; 5)</strong>, plafonnant le courant secondaire pour protéger '
         'les centrales de mesure numériques contre la destruction thermique.</li>'
         '<li><strong>Noyau 2 — Relais de Protection (Classe 5P10 / 10P10, Facteur Limite de Précision ALF &ge; 10) :</strong> '
         'Réalisé en tôle d\'acier au silicium CRGO à saturation élevée. Il est conçu pour <strong>ne pas saturer</strong> lorsque le courant primaire '
         'atteint 10 à 20 fois le nominal lors d\'un défaut franc. Cela garantit que les relais reçoivent un signal linéaire fidèle '
         'pour ordonner l\'ouverture instantanée du disjoncteur en moins de 20 millisecondes.</li>'
         '</ul>'),
        ('Qu\'est-ce que le niveau de décharges partielles et pourquoi doit-il être inférieur à 10 pC ?',
         'Les décharges partielles sont de micro-arcs électriques qui se produisent dans des bulles d\'air ou micro-fissures microscopiques '
         'emprisonnées dans la résine lors du moulage. '
         'Sous tension permanente de 10kV à 35kV, ces décharges génèrent de l\'ozone et dégradent chimiquement la résine de l\'intérieur, '
         'menant à un claquage diélectrique destructeur. Les TC YOMIN LZZBJ9 sont fabriqués sous dégazage sous vide poussé, '
         'garantissant des décharges partielles <strong>inférieures à 10 pico-coulombs (< 10 pC à 1,2 Um)</strong>, assurant plus de 30 ans de fiabilité.')
    ],
    cta='Vous concevez des cellules de distribution moyenne tension (AIS), des tableaux compacts RMU ou des postes de raccordement d\'énergie renouvelable nécessitant des transformateurs de courant en résine moulée certifiés CEI 61869-2 (10kV à 35kV, double noyau 0.2S / 5P10, Ith jusqu\'à 31,5kA) ? YOMIN fabrique des TC MT série LZZBJ9 de haute précision.',
    body='''
<h2>Le Gardien Diélectrique Indispensable pour Cellules et Tableaux Moyenne Tension</h2>
<p>Au cœur de chaque poste de transformation moyenne tension, usine industrielle, armoire de comptage d\'énergie renouvelable éolienne/solaire et tableau de distribution primaire fonctionnant sous des tensions de <strong>10kV, 12kV, 24kV et 33kV/36kV</strong>, mesurer le courant en toute sécurité est une exigence absolue.</p>
<p>Les barres de distribution moyenne tension transportent des puissances considérables. Si la haute tension venait à franchir la barrière d\'isolement vers les circuits de relayage basse tension, les centrales de mesure et les automates seraient instantanément pulvérisés, mettant en danger les exploitants.</p>
<p>De plus, lorsqu\'un court-circuit violent frappe le départ de ligne—suite au claquage d\'un câble souterrain ou à un défaut de transformateur—les courants de défaut bondissent à plus de 25 000 ou 31 500 ampères en quelques millisecondes.</p>
<p>Le <strong>Transformateur de Courant Moyenne Tension en Résine Moulée (Série LZZBJ9 / LZBW)</strong> s\'impose comme la référence technologique mondiale : un appareil sec de type support coulé sous vide en résine époxy cycloaliphatique, offrant une précision de Classe 0.2S en comptage et une réponse linéaire Classe 5P10 en protection selon la norme CEI 61869-2.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série LZZBJ9</h2>
<ol>
  <li><strong>Corps Massif en Résine Époxy Coulé sous Vide (APG) :</strong> Résine cycloaliphatique renforcée de silice offrant une rigidité mécanique exceptionnelle, une étanchéité absolue et zéro risque d\'incendie par rapport aux anciens TC à huile.</li>
  <li><strong>Bornes Primaires en Cuivre Argenté Électrolytique (P1, P2) :</strong> Plages de raccordement généreuses permettant le boulonnage direct des barres de cuivre du jeu de barres MT avec une résistance de contact minime.</li>
  <li><strong>Deux Circuits Magnétiques Rigoureusement Indépendants :</strong> Circuit nanocristallin saturant à FS5 pour protéger les wattmètres en Classe 0.2S, et circuit en acier au silicium CRGO linéaire jusqu\'à 10 ou 20 fois $I_n$ pour les relais de protection.</li>
  <li><strong>Boîtier Secondaire Étanche et Plombable :</strong> Compartiment inférieur abritant les bornes à vis en laiton (1S1-1S2, 2S1-2S2) et borne de terre, avec orifices de plombage pour prévenir les fraudes sur le comptage d\'énergie.</li>
  <li><strong>Tenue Électrodynamique et Thermique Élevée :</strong> Conçu pour encaisser des chocs thermiques jusqu\'à 31,5 kA pendant 3 secondes et des crêtes dynamiques de plus de 80 kA sans fissuration mécanique.</li>
</ol>
'''
)

MVCT_ES = dict(
    lang='es',
    dir='ltr',
    slug='medium-voltage-substations-what-is-a-medium-voltage-current-transformer-es',
    title='Subestaciones de Media Tensión: ¿Qué es un Transformador de Corriente de Media Tensión (MV CT)?',
    breadcrumb='Aparamenta de Media Tensión y Transformadores de Medida',
    read='10 min de lectura',
    alt='Tres transformadores de corriente de media tensión en resina epoxi fundida al vacío (Serie LZZBJ9, 12kV) instalados verticalmente con barras de cobre en celda MT',
    desc=('Subestaciones de media tensión (10kV a 35kV), celdas de distribución primaria y unidades principales de anillo (RMU): ¿Qué es un transformador de corriente de media tensión (MV CT)? '
          'Resina epoxi cicloalifática fundida al vacío, doble núcleo de medición (0.2S) y protección (5P10/10P10), resistencia térmica 31,5kA y norma IEC 61869-2.'),
    model='Serie LZZBJ9 / LZBW: Transformadores de Corriente de Media Tensión en Resina Fundida (10kV a 35kV, Doble Núcleo 0.2S / 5P10, 5A a 3150A, IEC 61869-2)',
    category='Aparamenta de Media Tensión y Transformadores de Medida / Transformadores de Corriente en Resina Fundida',
    kw='transformador de corriente media tension &middot; tc media tension &middot; transformador de medida 10kv &middot; tc resina 33kv &middot; lzzbj9 tc &middot; transformador celda mt',
    specs=[
        ('Clase de Tensión Asignada de Servicio ($U_m$)', 'Redes de distribución en media tensión: 10kV / 12kV, 24kV y 36kV / 40,5kV AC (50/60 Hz, celdas MT AIS/GIS)'),
        ('Rango de Corriente Primaria Nominal ($I_{pn}$)', 'Calibres primarios estándar: 5A, 10A, 20A, 50A, 100A, 200A, 400A, 600A, 1000A, 1250A hasta 3150A'),
        ('Corrientes Secundarias Nominales de Salida', 'Salidas secundarias estandarizadas: 5 A o 1 A (Núcleo 1: 1S1-1S2; Núcleo 2: 2S1-2S2)'),
        ('Configuración de Doble Núcleo y Exactitud', 'Arquitectura de doble circuito magnético: Núcleo 1 Clase 0.2S / 0.5 (Facturación); Núcleo 2 Clase 5P10 / 10P10 (Protección)'),
        ('Corriente Térmica de Cortocircuito ($I_{th}$)', 'Elevada capacidad térmica de cortocircuito: hasta 31,5 kA durante 3,0 segundos ($I_{dyn} \ge 2,5 \times I_{th}$)'),
        ('Material Aislante y Tecnología de Colada', 'Colada al vacío por proceso APG en resina epoxi cicloalifática sólida (clase de aislamiento térmico E / B)'),
        ('Nivel Certificado de Descargas Parciales', 'Descargas parciales ultra bajas certificadas: $< 10$ pC a $1,2 U_m / \sqrt{3}$ (vida útil dieléctrica garantizada $> 30$ años)'),
        ('Tensión de Prueba a Frecuencia Industrial y BIL', 'Tensión soportada a frecuencia industrial: hasta 95 kV (1 min); tensión de impulso tipo rayo (BIL): hasta 200 kV cresta')
    ],
    faqs=[
        ('¿Qué es un Transformador de Corriente de Media Tensión y por qué es indispensable el aislamiento en resina epoxi?',
         'Un Transformador de Corriente de Media Tensión (TC de Media Tensión)—también denominado transformador de medida en resina fundida o TC 10kV–35kV—es '
         'un transformador de instrumento diseñado para operar en redes de distribución eléctrica de 10kV a 35kV '
         'para reducir con total precisión las altas corrientes primarias a valores secundarios estándar (5A o 1A) que alimentan '
         'a relés de protección digitales, medidores de facturación fiscal y sistemas de telecontrol SCADA. '
         'En celdas de media tensión y subestaciones de distribución : '
         '<ul>'
         '<li><strong>Barrera de Aislamiento Dieléctrico Absoluto:</strong> Los transformadores de baja tensión (0,66kV) no pueden soportar '
         'las decenas de kilovoltios de operación ni las sobretensiones por rayo (de 75kV a 95kV). Los TCs YOMIN LZZBJ9 se fabrican '
         'en un bloque macizo de resina epoxi cicloalifática fundida al vacío mediante el proceso APG. Esta resina sólida e impermeable '
         'aísla por completo los circuitos de control de baja tensión de los peligrosos potenciales de media tensión.</li>'
         '<li><strong>Seguridad Antiexplosiva y Cero Mantenimiento:</strong> A diferencia de los antiguos transformadores en baño de aceite '
         'que sufrían fugas y riesgos de incendio, los transformadores secos en resina son autoextinguibles, no explotan y no requieren mantenimiento.</li>'
         '</ul>'),
        ('¿Por qué incorporan Doble Núcleo: Medición Clase 0.2S vs. Protección Clase 5P10?',
         'Un solo núcleo magnético no puede satisfacer los requerimientos opuestos de la medición de alta precisión y el despeje de fallas : '
         '<ul>'
         '<li><strong>Núcleo 1 — Medición de Facturación (Clase 0.2S, Factor de Seguridad FS &le; 5):</strong> '
         'Fabricado con aleación nanocristalina de alta permeabilidad, mantiene una exactitud de &plusmn;0,2% desde el 1% hasta el 120% de la carga. '
         'Está diseñado para <strong>saturarse rápidamente ante un cortocircuito (FS &le; 5)</strong>, limitando la corriente secundaria para proteger '
         'a los medidores digitales contra quemaduras térmicas.</li>'
         '<li><strong>Núcleo 2 — Relés de Protección (Clase 5P10 / 10P10, Factor Límite de Precisión ALF &ge; 10):</strong> '
         'Fabricado con acero al silicio de grano orientado (CRGO) de alta saturación. Está diseñado para <strong>no saturarse</strong> '
         'cuando la corriente primaria se multiplica por 10 o 20 veces la nominal durante una falla franca. Esto garantiza que los relés reciban '
         'una señal lineal para ordenar el disparo del disyuntor en menos de 20 milisegundos.</li>'
         '</ul>'),
        ('¿Qué son las descargas parciales y por qué deben certificarse por debajo de 10 pC?',
         'Las descargas parciales son microarcos eléctricos internos que se originan dentro de burbujas de aire microscópicas atrapadas en la resina durante el moldeo. '
         'Bajo tensiones continuas de 10kV a 35kV, estas microchispas erosionan químicamente el aislante desde su interior, provocando con el tiempo '
         'una perforación dieléctrica destructiva. Los TCs YOMIN LZZBJ9 se fabrican bajo desgasificación profunda al vacío, garantizando '
         'descargas parciales <strong>inferiores a 10 picoculombios (< 10 pC a 1,2 Um)</strong>, asegurando más de 30 años de vida útil.')
    ],
    cta='¿Fabrica celdas de distribución en media tensión (AIS), centros de seccionamiento RMU o subestaciones de energía solar/eólica que requieren transformadores de corriente en resina epoxi certificados bajo norma IEC 61869-2 (10kV a 35kV, doble núcleo 0.2S / 5P10, Ith hasta 31,5kA)? YOMIN suministra TCs de media tensión serie LZZBJ9 de alta precisión.',
    body='''
<h2>El Aislamiento Dieléctrico Fundamental para Celdas y Tableros de Media Tensión</h2>
<p>En el interior de cada subestación eléctrica de media tensión, sala de distribución industrial, centro de transformación de energía renovable solar y eólica, y celdas de distribución primaria que operan en <strong>10kV, 12kV, 24kV y 33kV/36kV</strong>, medir la corriente con seguridad es una exigencia primordial.</p>
<p>Las barras colectoras de media tensión conducen potencias enormes. Si la alta tensión saltara hacia los circuitos secundarios de control y protección, los medidores digitales y relés quedarían destruidos instantáneamente, poniendo en grave riesgo la vida del personal técnico.</p>
<p>Asimismo, cuando ocurre un cortocircuito severo en la red subterránea o en un transformador de potencia, las corrientes de falla se elevan violentamente hasta 25.000 o 31.500 amperios en cuestión de milisegundos.</p>
<p>El <strong>Transformador de Corriente de Media Tensión en Resina Fundida (Serie LZZBJ9 / LZBW)</strong> representa el estándar internacional definitivo: un transformador seco tipo soporte fundido al vacío en resina epoxi cicloalifática, que entrega medición Clase 0.2S y protección Clase 5P10 bajo estricta certificación IEC 61869-2.</p>

<h2>Elementos Constructivos y Excelencia de Ingeniería de la Serie LZZBJ9</h2>
<ol>
  <li><strong>Cuerpo Macizo en Resina Epoxi Cicloalifática (APG):</strong> Proceso de colada al vacío con sílice micronizada que otorga extrema rigidez mecánica, cero riesgo de fugas de aceite y resistencia al fuego autoextinguible.</li>
  <li><strong>Terminales Primarios de Cobre Electrolítico Plateado (P1, P2):</strong> Platinas de conexión dimensionadas para permitir el empernado directo de las barras de cobre del tablero MT con mínima resistencia de contacto.</li>
  <li><strong>Dos Circuitos Magnéticos Totalmente Independientes:</strong> Núcleo nanocristalino que satura a FS5 para proteger medidores en Clase 0.2S, y núcleo de acero al silicio CRGO lineal hasta 10 o 20 veces $I_n$ para relés de disparo.</li>
  <li><strong>Caja de Bornes Secundarios Precintable:</strong> Compartimiento inferior con bornes de latón (1S1-1S2, 2S1-2S2) y borne de puesta a tierra con perforaciones para alambre de precinto antifraude.</li>
  <li><strong>Elevada Capacidad Térmica y Dinámica de Cortocircuito:</strong> Diseñado para tolerar esfuerzos térmicos de hasta 31,5 kA durante 3 segundos y picos dinámicos superiores a 80 kA sin sufrir fisuras mecánicas internas.</li>
</ol>
'''
)

MVCT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='medium-voltage-substations-what-is-a-medium-voltage-current-transformer-ar',
    title='محطات الجهد المتوسط وشبكات التوزيع: ما هو محول تيار الجهد المتوسط (Medium-Voltage CT)؟',
    breadcrumb='مهمات الجهد المتوسط ومحولات القياس',
    read='10 دقائق قراءة',
    alt='ثلاثة محولات تيار للجهد المتوسط مصبوبة براتنج الإيبوكسي تحت التفريغ (موديل LZZBJ9، جهد 12kV) مثبتة رأسياً مع قضبان النحاس داخل خلية مفاتيح MT',
    desc=('محطات تحويل الجهد المتوسط (10kV إلى 35kV)، وخلايا التوزيع الحلقية RMU، ولوحات التوزيع الرئيسية: ما هو محول تيار الجهد المتوسط (MV CT)؟ '
          'عزل راتنج الإيبوكسي المصبوب بالتفريغ، والقلب المزدوج للقياس (0.2S) والوقاية (5P10/10P10)، وصمود القصر 31.5kA ومعايير IEC 61869-2.'),
    model='سلسلة LZZBJ9 / LZBW: محولات تيار الجهد المتوسط المصبوبة براتنج الإيبوكسي (10kV إلى 35kV، قلب مزدوج 0.2S / 5P10، تيار 5A إلى 3150A، معتمدة IEC 61869-2)',
    category='مهمات الجهد المتوسط ومحولات القياس / محولات التيار المصبوبة بالإيبوكسي',
    kw='محول تيار جهد متوسط &middot; mv current transformer &middot; محول تيار 10kv &middot; محول تيار ايبوكسي 33kv &middot; lzzbj9 ct &middot; محول خلية موزع جهد متوسط',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة ($U_m$)', 'شبكات توزيع الجهد المتوسط الصناعية: 10kV / 12kV و 24kV و 36kV / 40.5kV AC (تردد 50/60 هرتز، خلايا AIS/GIS)'),
        ('نطاق قياس التيار الابتدائي الاسمي ($I_{pn}$)', 'سعات تيار ابتدائي معيارية: 5A و 10A و 20A و 50A و 100A و 200A و 400A و 600A و 1000A و 1250A وحتى 3150A'),
        ('التيار الثانوي الاسمي لأجهزة القياس والوقاية', 'مخرجات ثانوية معيارية للوحات: 5 أمبير أو 1 أمبير (الملف 1: 1S1-1S2؛ الملف 2: 2S1-2S2)'),
        ('تكوين القلب المزدوج وفئات الدقة المترولوجية', 'قلبان مغناطيسيان مستقلان: القلب 1 فئة 0.2S / 0.5 (عدادات الفوترة)؛ القلب 2 فئة 5P10 / 10P10 (مرحلات الوقاية)'),
        ('قدرة الصمود الحراري لتيارات القصر ($I_{th}$)', 'صمود حراري هائل لتيار القصر: حتى 31.5 kA لمدة 3.0 ثوانٍ (تيار الذروة الديناميكي $I_{dyn} \ge 2.5 \times I_{th}$)'),
        ('مادة العزل وتقنية الصب المتقدمة', 'صب تحت التفريغ الكامل بتقنية APG باستخدام راتنج إيبوكسي سيكلوأليفاتي صلب (تصنيف عزل حراري فئة E / B)'),
        ('مستوى التفريغ الجزئي (PD) المعتمد للمحول', 'تفريغ جزئي فائق الانخفاض معتمد: $< 10$ pC عند جهد $1.2 U_m / \sqrt{3}$ (يضمن عمراً تشغيلياً يتجاوز 30 عاماً)'),
        ('جهد صمود التردد الصناعي وصدمات الصواعق (BIL)', 'جهد صمود التردد الصناعي الجاف: حتى 95 kV (دقيقة واحدة)؛ جهد صمود نبضات الصواعق (BIL): حتى 200 kV ذروة')
    ],
    faqs=[
        ('ما هو محول تيار الجهد المتوسط (MV CT) ولماذا يعتبر العزل براتنج الإيبوكسي المصبوب أمراً حاسماً؟',
         'محول تيار الجهد المتوسط—والمعروف في قطاع محطات الكهرباء باسم محول قياس الجهد المتوسط أو محول التيار الجاف المصبوب بالإيبوكسي أو محول خلايا 10kV–35kV—هو '
         'محول قياس عالي القدرة صُمم ليعمل في شبكات توزيع الكهرباء ذات الجهد المتوسط (من 10kV إلى 35kV) '
         'لتحويل تيارات الخط العالية بدقة تامة إلى قيم ثانوية معيارية آمنة (5 أمبير أو 1 أمبير) تغذي مرحلات الوقاية الرقمية '
         'وعدادات قياس الطاقة والفوترة وأجهزة التحكم والمراقبة SCADA. '
         'وفي خلايا الجهد المتوسط ومحطات التوزيع : '
         '<ul>'
         '<li><strong>حاجز العزل الديزلكتريكي الصارم:</strong> لا تستطيع محولات الجهد المنخفض (0.66kV) تحمل جهود التشغيل العالية '
         'التي تبلغ آلاف الفولتات أو نبضات الصواعق العاتية (التي تصل إلى 75kV وحتى 95kV). تصنع محولات يمين LZZBJ9 بصب كامل لكتلة صلبة '
         'من راتنج الإيبوكسي السيكلوأليفاتي تحت التفريغ بتقنية APG. ويوفر هذا العزل الصلب عزلاً تاماً وموثوقاً يمنع وصول الجهد المتوسط '
         'الخطير إلى دوائر التحكم والمرحلات منخفضة الجهد.</li>'
         '<li><strong>الأمان ومقاومة الانفجار وانعدام الصيانة:</strong> بخلاف المحولات الزيتية القديمة المعرضة للتسريب والانفجار عند الأعطال، '
         'فإن المحولات الجافة المصبوبة بالإيبوكسي ذاتية الإطفاء، ولا تنفجر، ولا تتطلب أي صيانة زيتية على الإطلاق على مدار 30 عاماً.</li>'
         '</ul>'),
        ('لماذا يحتوي محول الجهد المتوسط على قلبين منفصلين: قلب قياس 0.2S مقابل قلب وقاية 5P10؟',
         'لا يمكن لدائرة مغناطيسية واحدة أن تجمع بين متطلبات الدقة الفائقة عند الأحمال المنخفضة ومتطلبات عدم التشبع عند تيارات القصر الهائلة : '
         '<ul>'
         '<li><strong>القلب الأول — عدادات قياس الطاقة والفوترة (فئة 0.2S، معامل أمان الأجهزة FS &le; 5):</strong> '
         'يُصنع من سبائك نانوبلورية فائقة النفاذية المغناطيسية، ليحافظ على دقة متناهية (&plusmn;0.2%) من 1% إلى 120% من تيار الحمل. '
         'وهو مصمم لـ <strong>يتشبع سريعاً عند وقوع قصر كهربائي (FS &le; 5)</strong> ليحمي العدادات الرقمية الحساسة من الاحتراق بالتيار الثانوي العالي.</li>'
         '<li><strong>القلب الثاني — مرحلات الوقاية والحماية (فئة 5P10 / 10P10، معامل حد الدقة ALF &ge; 10):</strong> '
         'يُصنع من صلب السيليكون ذي الحبيبات الموجهة CRGO عالي التشبع. وهو مصمم <strong>ألا يتشبع إطلاقاً</strong> حتى لو قفز تيار العطل '
         'إلى 10 أو 20 ضعف التيار الاسمي. هذا يضمن إرسال إشارة خطية دقيقة لمرحل الوقاية ليصدر أمر فصل فوري للقاطع في أقل من 20 مللي ثانية.</li>'
         '</ul>'),
        ('ما هو التفريغ الجزئي (PD) ولماذا يجب ألا يتجاوز 10 بيكوكولوم طبقاً للمواصفة IEC 61869-2؟',
         'التفريغ الجزئي هو شرر كهربائي مجهري يحدث داخل فقاعات الهواء الدقيقة المحبوسة داخل كتلة الإيبوكسي الصلبة أثناء عملية الصب. '
         'ومع استمرار الجهد المتوسط (10kV إلى 35kV)، يؤدي هذا الشرر لتآكل العزل كيميائياً من الداخل حتى يحدث انهيار وانهيار مفاجئ لعزل المحول. '
         'تُصنع محولات يمين LZZBJ9 تحت تفريغ هوائي عميق للغاية يضمن خلو العزل من أي فجوات، محققةً تفريغاً جزئياً معتمداً '
         '<strong>أقل من 10 بيكوكولوم (< 10 pC عند 1.2 Um)</strong>، وهو ما يضمن عمراً تشغيلياً آمناً يتجاوز 30 عاماً دون تدهور.</li>')
    ],
    cta='هل تعمل على تصنيع خلايا الجهد المتوسط الهوائية (AIS)، أو محطات التوزيع الحلقية RMU، أو محطات ربط مشاريع الطاقة المتجددة التي تتطلب محولات تيار جافة مصبوبة براتنج الإيبوكسي معتمدة IEC 61869-2 (جهد 10kV إلى 35kV، قلب مزدوج 0.2S / 5P10، تيار قصر حتى 31.5kA)؟ تصنع يمين (YOMIN) محولات LZZBJ9 بأعلى درجات الدقة.',
    body='''
<h2>الحارس الديزلكتريكي الموثوق لخلايا وموزعات شبكات الجهد المتوسط</h2>
<p>في قلب كل محطة تحويل كهربائية للجهد المتوسط، وغرفة توزيع كهرباء صناعية، ووحدة توزيع حلقية مدمجة (RMU)، وساحة ربط لمحطات الطاقة الشمسية وطاقة الرياح تعمل بجهد <strong>10kV و 12kV و 24kV و 33kV/36kV</strong>، يمثل قياس التيار بأمان وعزل الجهود العالية مطلباً حيوياً لا يقبل المساومة.</p>
<p>تنقل قضبان توزيع الجهد المتوسط طاقات كهربائية هائلة. فإذا سمح لعزل المحول بالانهيار وانتقال هذا الجهد العالي نحو دوائر التحكم والحماية منخفضة الجهد، فستحترق مرحلات الوقاية والعدادات في لحظة، معرّضةً حياة فنيي التشغيل للخطر الداهم.</p>
<p>وعلاوة على ذلك، عند حدوث عطل قصر كهربائي عنيف في الكابلات الأرضية أو المحولات، تقفز تيارات العطل في أجزاء من الثانية إلى 25,000 أو 31,500 أمبير.</p>
<p>يمثل <strong>محول تيار الجهد المتوسط المصبوب براتنج الإيبوكسي (سلسلة LZZBJ9 / LZBW)</strong> المعيار الهندسي القياسي المعتمد عالمياً: محول قياس دعامي جاف صُب تحت التفريغ من راتنج الإيبوكسي السيكلوأليفاتي عالي الجودة، موفراً دقة متناهية فئة 0.2S للقياس وحماية خطية فئة 5P10 طبقاً لاعتماد المواصفة الدولية IEC 61869-2.</p>

<h2>المكونات الهندسية وميزات الأداء الفائق لسلسلة محولات LZZBJ9</h2>
<ol>
  <li><strong>هيكل صلب مصبوب بالإيبوكسي تحت التفريغ (APG):</strong> خليط متجانس من راتنج الإيبوكسي ومسحوق السيليكا الدقيق يوفر صلابة ميكانيكية فائقة، مع انعدام تام لأي تسرب زيتي أو مخاطر حرائق مقارنة بالمحولات الزيتية.</li>
  <li><strong>أطراف توصيل ابتدائية من النحاس المطلي بالفضة (P1, P2):</strong> ألواح تلامس عريضة بفتحات مسامير قياسية تسمح بالربط المباشر لقضبان النحاس الخاصة بخلية الجهد المتوسط بأقل مقاومة تلامس ممكنة.</li>
  <li><strong>قلبان مغناطيسيان مستقلان تماماً:</strong> قلب نانوبلوري يتشبع عند FS5 لحماية عدادات الطاقة بدقة فئة 0.2S، وقلب من صلب السيليكون CRGO لا يتشبع حتى 10 أو 20 ضعف التيار الاسمي لمرحلات الوقاية.</li>
  <li><strong>صندوق أطراف ثانوية محكم وقابل للترصيص:</strong> حجرة سفلية تضم أطراف الربط النحاسية (1S1-1S2 و 2S1-2S2) وطرف التأريض، مع ثقوب لتمرير سلك الترصيص لمنع أي سرقة أو تلاعب بعدادات الطاقة.</li>
  <li><strong>صمود حراري وديناميكي فائق لتيارات القصر:</strong> هندسة داخلية مصممة لتحمل التيارات الحرارية حتى 31.5 kA لمدة 3 ثوانٍ وتيارات الذروة الديناميكية التي تتجاوز 80 kA دون أي تشقق داخلي.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1015B = [
    SC_EN, SC_FR, SC_ES, SC_AR,
    MVCT_EN, MVCT_FR, MVCT_ES, MVCT_AR
]
