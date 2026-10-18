# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-18:
1. Dry-Type Galvanic Isolation Transformers for Power Quality and Medical Safety (EN, FR, ES, AR)
2. Heavy-Duty Long-Barrel Two-Hole Copper Compression Lugs for Switchgear and Telecom (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. ISOLATION TRANSFORMER (EN, FR, ES, AR)
# ==============================================================================

IT_EN = dict(
    lang='en',
    dir='ltr',
    slug='power-quality-what-is-an-isolation-transformer',
    title='Power Quality & Safety: What Is an Isolation Transformer?',
    breadcrumb='Power Quality &amp; Isolation Transformers',
    read='10 min read',
    alt='Three-phase industrial Dry-Type Galvanic Isolation Transformer (Model SG series) with copper coils and grounded electrostatic Faraday shield',
    desc=('Medical operating theaters, variable frequency drives (VFD), CNC machine tools, and commercial data centers: What is an isolation transformer? '
          'How physical galvanic decoupling, electrostatic Faraday shielding, common-mode noise attenuation (> 60 dB), and ungrounded IT electrical distribution prevent electric shock and equipment damage.'),
    model='Model SG / DG / JBK5 Series Three-Phase & Single-Phase Dry-Type Galvanic Isolation Transformers (100VA to 500kVA, 3kV Dielectric Withstand, Faraday Shield, IEC 61558-2-4 / UL 1561)',
    category='Power Quality & Isolation Transformers / Galvanic Isolation Transformers',
    kw='what is an isolation transformer &middot; isolation transformer &middot; dry type isolation transformer &middot; medical isolation transformer &middot; three phase isolation transformer &middot; galvanic isolation transformer',
    specs=[
        ('Primary-to-Secondary Electrical Decoupling', 'Complete 100% physical galvanic separation (Zero metallic electrical connection between primary input and secondary output coils)'),
        ('Electrostatic Noise Shielding (Faraday Screen)', 'Grounded electrolytic copper foil shield interleaved between primary and secondary windings (Common-mode noise attenuation &gt; 60 dB)'),
        ('Dielectric Hi-Pot Insulation Withstand Voltage', 'Tested dielectric strength: 3000 V AC / 1 min between windings, and between windings and grounded laminated steel core'),
        ('Magnetic Core Material & Lamination Grade', 'High-permeability cold-rolled grain-oriented (CRGO) silicon steel laminations with step-lap mitered joints for ultra-low no-load core losses'),
        ('Rated Power Capacity & Phase Configurations', 'Standard capacities: 100VA to 500kVA (Single-phase DG series: 100VA–50kVA; Three-phase SG series: 1kVA–500kVA, 50/60 Hz)'),
        ('Primary & Secondary Voltage Transformation', 'Standard inputs: 480V, 415V, 380V, 230V AC; Standard outputs: 400V, 380V, 220V, 208V, 120V AC (Step-up, step-down, or 1:1 ratio)'),
        ('Thermal Class & Insulation System Rating', 'Class F ($155^\circ\text{C}$) or Class H ($180^\circ\text{C}$) vacuum pressure impregnated (VPI) high-temperature Nomex / epoxy insulation'),
        ('International Manufacturing Safety Standards', 'Fully tested and compliant with IEC 61558-1, IEC 61558-2-4, UL 1561, CSA C22.2, and EN 61558-2-15 (Medical IT systems)')
    ],
    faqs=[
        ('What is an Isolation Transformer and how does Galvanic Isolation protect electrical equipment?',
         'An Isolation Transformer—frequently designated as a galvanic isolation transformer, dry-type safety isolating transformer, or medical IT transformer—is '
         'a specialized stationary transformer whose primary (input) and secondary (output) winding coils are completely physically and magnetically coupled '
         '<strong>without any direct electrical or metallic connection</strong> between them. '
         'In modern electrical distribution and automation engineering: '
         '<ul>'
         '<li><strong>Galvanic Decoupling &amp; Ground Loop Elimination:</strong> In standard utility electrical circuits, the neutral conductor is bonded to earth at the substation. '
         'When sensitive computer servers, CNC controllers, or medical laboratory instrumentation are connected to different ground rods across a facility, '
         'minute potential differences generate continuous circulating ground currents (ground loops), causing severe communication errors, measuring drift, and electronic component failure. '
         'An isolation transformer breaks the ground loop completely by creating a clean, ungrounded, freshly established secondary reference plane.</li>'
         '<li><strong>Electric Shock Mitigation (Ungrounded Floating Secondary):</strong> Touching a live phase conductor on a standard grounded utility system allows electric current '
         'to flow through the human body back to earth, causing lethal electrocution. '
         'With an ungrounded 1:1 isolation transformer, touching a single secondary phase conductor does not complete an electrical circuit to earth, '
         'preventing electric shock in hazardous or wet operating environments.</li>'
         '</ul>'),
        ('What is an Electrostatic Faraday Shield and why is it essential for VFDs and sensitive electronics?',
         'Standard transformers inherently possess inter-winding parasitic capacitance ($C_{ps}$) between adjacent primary and secondary coil layers. '
         'High-frequency voltage spikes, lightning impulses, and rapid switching transients ($dv/dt$) from Variable Frequency Drives (VFDs) easily bridge across this parasitic capacitance, '
         'passing directly through the transformer into delicate electronic microprocessors. '
         'YOMIN SG series transformers incorporate an <strong>Electrostatic Faraday Shield</strong>: '
         '<ul>'
         '<li><strong>Structure:</strong> A continuous sheet of insulated electrolytic copper foil placed physically between the primary and secondary windings, '
         'deliberately left with a non-shorting overlap and connected directly to the transformer\'s low-impedance earth ground.</li>'
         '<li><strong>Performance:</strong> It acts as an electrostatic barrier that diverts common-mode high-frequency noise currents straight into the ground '
         'before they can capacitively couple into the secondary winding, delivering over <strong>60 to 80 dB of common-mode noise attenuation</strong>.</li>'
         '</ul>'),
        ('What is the difference between an Autotransformer and an Isolation Transformer?',
         'While both devices adjust voltage levels, their internal architectures and safety capabilities are completely opposite: '
         '<ul>'
         '<li><strong>Autotransformer (Single Shared Winding):</strong> Utilizes a single continuous copper coil where the secondary voltage is tapped from the same winding as the primary. '
         'Because primary and secondary share a common metallic connection, autotransformers offer <strong>ZERO galvanic isolation</strong>, zero noise filtering, '
         'and pass grid surges, earth faults, and DC offsets straight through to downstream loads.</li>'
         '<li><strong>Isolation Transformer (Dual Independent Windings):</strong> Features two completely separate, physically isolated coils wound on opposite sections of the core. '
         'It delivers 100% dielectric isolation, protects human operators from ground faults, and filters harmonics, making it mandatory for medical operating rooms, '
         'data center PDU cabinets, and precision automated machinery.</li>'
         '</ul>')
    ],
    cta='Designing hospital healthcare medical IT facilities, industrial automation PLC control enclosures, variable frequency drive clean power feeds, or marine vessel switchboards requiring certified IEC 61558-2-4 / UL 1561 dry-type galvanic isolation transformers (100VA to 500kVA, Faraday electrostatic shield, 3kV isolation)? YOMIN manufactures precision SG/DG series isolation transformers.',
    body='''
<h2>The Galvanic Electrical Firewall for Modern Industrial and Medical Infrastructure</h2>
<p>Inside modern manufacturing plants, hospital surgical suites, commercial data centers, and advanced automation facilities, electronic power supplies, microprocessor PLCs, and medical monitors operate around the clock.</p>
<p>However, modern electrical distribution grids are flooded with high-frequency switching harmonics from solar inverters, massive voltage spikes from lightning strikes, and common-mode electrical noise generated by Variable Frequency Drives (VFDs).</p>
<p>Furthermore, in large commercial buildings, ground potential differences between distant utility grounding rods create continuous circulating ground loop currents that induce phantom voltages, distort instrumentation sensor readings, and destroy delicate silicon chips.</p>
<p>The <strong>Dry-Type Galvanic Isolation Transformer (Model SG / DG Series)</strong> provides the definitive engineering firewall: a precision power transformer that magnetically transfers energy across a high-dielectric physical air gap while completely isolating the input and output circuits, eliminating ground loops, filtering electrical transients, and protecting human operators from lethal electric shock.</p>

<h2>Engineering Anatomy: Inside a Model SG Three-Phase Dry-Type Isolation Transformer</h2>
<ol>
  <li><strong>Physically Separated Primary and Secondary Copper Coils:</strong> Precision-wound using high-purity electrolytic copper magnet wire (Cu-ETP 99.9%). Primary and secondary windings are separated by heavy-gauge high-temperature Nomex / mica barrier insulation tested to withstand 3000V AC.</li>
  <li><strong>Grounded Electrostatic Faraday Copper Shield:</strong> A full-coverage electrolytic copper screen inserted between the primary and secondary windings. Shunts common-mode noise, switching spikes, and high-frequency harmonics directly to ground, achieving over 60 dB noise attenuation.</li>
  <li><strong>High-Permeability Grain-Oriented Silicon Steel Core:</strong> Built from low-loss cold-rolled grain-oriented (CRGO) silicon steel laminations with precision mitered step-lap joints, minimizing eddy current losses, excitation current, and acoustic humming.</li>
  <li><strong>Vacuum Pressure Impregnation (VPI) Resin Coating:</strong> The complete core and coil assembly undergoes high-vacuum pressure impregnation with Class H ($180^\circ\text{C}$) solventless polymer resin, curing into a void-free, moisture-proof, and chemical-resistant monolithic block.</li>
  <li><strong>Heavy-Duty Tinned Copper Terminal Blocks &amp; Enclosure:</strong> High-conductivity terminal blocks supporting multi-conductor power cabling, housed within a ventilated NEMA 1 / IP20 to IP54 powder-coated steel cabinet equipped with lifting eyes and vibration-damping mounting pads.</li>
</ol>

<h2>Comparison: Galvanic Isolation Transformer vs. Autotransformer vs. Line Reactor</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Performance Metric</th>
      <th>Standard Line Reactor (Inductor)</th>
      <th>Step-Up / Step-Down Autotransformer</th>
      <th>YOMIN Galvanic Isolation Transformer (SG Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Galvanic Physical Isolation</strong></td>
      <td>None: Series inductive coil with direct metallic path.</td>
      <td>None: Single shared tapped coil with direct metallic path.</td>
      <td><strong>100% Galvanic Separation: Dual physically isolated independent windings.</strong></td>
    </tr>
    <tr>
      <td><strong>Ground Loop &amp; Noise Breaking</strong></td>
      <td>Zero: Ground loop currents pass unhindered through system.</td>
      <td>Zero: Ground currents and neutral offsets transmit directly.</td>
      <td><strong>Complete Decoupling: Breaks ground loops; eliminates circulating earth noise.</strong></td>
    </tr>
    <tr>
      <td><strong>Common-Mode Noise Attenuation</strong></td>
      <td>Poor: Limits peak current spikes; does not block noise.</td>
      <td>Zero: High-frequency noise couples directly to output.</td>
      <td><strong>Superior (&gt; 60 dB): Grounded Faraday screen shunts spikes to ground.</strong></td>
    </tr>
    <tr>
      <td><strong>Electric Shock Safety (Ungrounded Mode)</strong></td>
      <td>None: Direct line-to-ground shock hazard remains 100%.</td>
      <td>None: Touching a phase wire causes lethal ground shock.</td>
      <td><strong>High Safety: Secondary can float ungrounded; touching single line prevents shock.</strong></td>
    </tr>
    <tr>
      <td><strong>Voltage Ratio Flexibility</strong></td>
      <td>Zero: Operates at 1:1 voltage drop only.</td>
      <td>Flexible: Steps voltage up or down (e.g. 480V to 380V).</td>
      <td><strong>Universal: 1:1 isolation ratio or any custom step-up / step-down combination.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

IT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='power-quality-what-is-an-isolation-transformer-fr',
    title="Qualité de l'Énergie & Sécurité : Qu'est-ce qu'un Transformateur d'Isolement ?",
    breadcrumb='Qualité de l\'Énergie &amp; Transformateurs d\'Isolement',
    read='10 min de lecture',
    alt='Transformateur d\'isolement galvanique triphasé de type sec (Série SG) avec bobinages cuivre et écran électrostatique de Faraday relié à la terre',
    desc=('Blocs opératoires hospitaliers, variateurs de vitesse (VFD), machines-outils CNC et centres de données : Qu\'est-ce qu\'un transformateur d\'isolement ? '
          'Séparation galvanique totale, écran électrostatique de Faraday, atténuation des bruits de mode commun (> 60 dB) et régime de neutre IT sécurisé.'),
    model='Série SG / DG / JBK5 : Transformateurs d\'Isolement Galvanique Secs Triphasés et Monophasés (100VA à 500kVA, Tenue 3kV, Écran Faraday, CEI 61558-2-4 / UL 1561)',
    category='Qualité de l\'Énergie & Transformateurs d\'Isolement / Transformateurs d\'Isolement Galvanique',
    kw='transformateur d isolement &middot; transformateur d isolement galvanique &middot; transformateur sec triphase &middot; transformateur medical it &middot; ecran de faraday &middot; transformateur sg',
    specs=[
        ('Séparation Galvanique Primaire / Secondaire', 'Découplage physique total à 100% (Zéro liaison métallique conductrice entre les enroulements primaire et secondaire)'),
        ('Écran Électrostatique de Blindage (Faraday)', 'Feuille de cuivre électrolytique continue reliée à la terre entre enroulements (Atténuation du bruit de mode commun &gt; 60 dB)'),
        ('Rigidité Diélectrique et Tension d\'Épreuve', 'Essai diélectrique normalisé : 3000 V AC pendant 1 min entre enroulements, et entre enroulements et circuit magnétique'),
        ('Circuit Magnétique et Tôles Silicium', 'Tôles d\'acier au silicium à grains orientés laminées à froid (CRGO) à faibles pertes avec empilage de précision step-lap'),
        ('Plage de Puissance Nominale Disponible', 'Gamme de 100VA à 500kVA (Monophasé série DG : 100VA–50kVA ; Triphasé série SG : 1kVA–500kVA, 50/60 Hz)'),
        ('Tensions d\'Entrée et de Sortie Normalisées', 'Entrées standard : 480V, 415V, 380V, 230V AC ; Sorties standard : 400V, 380V, 220V, 208V, 120V AC (Rapport 1:1 ou élévateur/abaisseur)'),
        ('Classe Thermique et Système d\'Isolation', 'Classe F ($155^\circ\text{C}$) ou Classe H ($180^\circ\text{C}$) avec imprégnation sous vide et pression (VPI) de résine époxy / Nomex'),
        ('Conformité aux Normes Internationales', 'Certifié et conforme aux normes CEI 61558-1, CEI 61558-2-4, UL 1561, CSA C22.2 et EN 61558-2-15 (Usage médical IT)')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transformateur d\'Isolement et comment protège-t-il les installations sensibles ?',
         'Un Transformateur d\'Isolement—également appelé transformateur de séparation de circuits ou transformateur d\'isolement galvanique—est '
         'un transformateur dont les enroulements primaire et secondaire sont rigoureusement séparés physiquement et électriquement, '
         'le transfert d\'énergie s\'effectuant <strong>exclusivement par induction magnétique</strong> à travers le noyau de fer. '
         'Dans les installations industrielles et médicales : '
         '<ul>'
         '<li><strong>Rupture des Boucles de Masse :</strong> Dans un réseau classique, le neutre est mis à la terre au transformateur de quartier. '
         'Les différences de potentiel de terre entre différents points d\'une usine engendrent des courants de circulation (boucles de masse) '
         'qui perturbent les automates PLC et instruments de mesure. Le transformateur d\'isolement brise net ces boucles en créant un secondaire '
         'totalement flottant et indépendant.</li>'
         '<li><strong>Sécurité des Personnes Contre l\'Électrisation :</strong> Toucher un conducteur de phase sur un réseau classique relié à la terre '
         'entraîne un choc électrique mortel par retour à la terre. Avec un secondaire isolé non référencé à la terre, le contact accidentel '
         'avec une seule phase ne boucle aucun circuit électrique, empêchant toute électrisation.</li>'
         '</ul>'),
        ('Pourquoi l\'écran électrostatique de Faraday est-il indispensable pour les variateurs de vitesse ?',
         'Entre les bobinages primaire et secondaire d\'un transformateur classique existe une capacité parasite d\'enroulement ($C_{ps}$). '
         'Les pics de tension à front raide et les harmoniques haute fréquence générés par les variateurs de vitesse (VFD) ou les commutations de réseau '
         'traversent cette capacité et polluent les équipements informatiques. '
         'L\'<strong>Écran de Faraday</strong> inséré par YOMIN est une feuille de cuivre électrolytique interposée entre primaire et secondaire '
         'reliée à la terre, qui capte et dévie ces parasites haute fréquence vers le sol, offrant une atténuation remarquable de <strong>60 à 80 dB</strong>.'),
        ('Quelle est la différence fondamentale entre un Autotransformateur et un Transformateur d\'Isolement ?',
         'L\'autotransformateur ne possède qu\'un seul enroulement commun servant à la fois au primaire et au secondaire. '
         'Il existe donc une liaison métallique directe entre l\'entrée et la sortie : l\'autotransformateur n\'offre <strong>aucun isolement galvanique</strong> '
         'et transmet intégralement les défauts de terre et surtensions. '
         'Le transformateur d\'isolement possède deux bobinages distincts totalement isolés diélectriquement (3000 V), garantissant une sécurité absolue.')
    ],
    cta='Vous concevez des blocs opératoires hospitaliers en schéma IT médical, des armoires d\'automates PLC, des alimentations de variateurs de vitesse ou des tableaux de bord marins nécessitant des transformateurs d\'isolement galvanique certifiés CEI 61558-2-4 / UL 1561 ? YOMIN fabrique des transformateurs série SG/DG de haute précision.',
    body='''
<h2>Le Pare-Feu Électrique Galvanique pour les Équipements Industriels et Médicaux Sensibles</h2>
<p>Dans les usines modernes automatisées, les blocs opératoires hospitaliers, les centres de données et les salles de contrôle de procédés, les équipements électroniques de puissance et les automates programmables fonctionnent en continu sous haute exigence de fiabilité.</p>
<p>Pourtant, le réseau de distribution électrique subit en permanence des perturbations sévères : harmoniques de découpage des variateurs VFD, transitoires de foudre et bruits de mode commun.</p>
<p>De plus, les différences de potentiel entre les prises de terre disséminées dans un bâtiment industriel génèrent des courants vagabonds destructeurs (boucles de masse) qui perturbent les mesures analogiques et endommagent les cartes électroniques.</p>
<p>Le <strong>Transformateur d\'Isolement Galvanique Sec (Série SG / DG)</strong> apporte la solution technique absolue : un transformateur de puissance qui transfère l\'énergie sans aucun contact métallique entre l\'entrée et la sortie, supprimant les boucles de terre, filtrant les transitoires et protégeant les opérateurs contre les chocs électriques.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série SG</h2>
<ol>
  <li><strong>Bobinages Primaire et Secondaire Physiquement Séparés :</strong> Cuivre électrolytique pur Cu-ETP (99,9%) avec isolants Nomex / mica haute température résistant à une épreuve diélectrique de 3000 V AC.</li>
  <li><strong>Écran Électrostatique de Blindage de Faraday :</strong> Écran en feuille de cuivre interposé entre les couches d\'enroulements et relié à la terre, assurant une atténuation des bruits haute fréquence supérieure à 60 dB.</li>
  <li><strong>Circuit Magnétique en Tôles Silicium CRGO :</strong> Tôles à grains orientés à faibles pertes assemblées par imbrication step-lap, réduisant drastiquement les pertes à vide et le bruit acoustique.</li>
  <li><strong>Imprégnation Sous Vide et Pression (VPI) :</strong> Traitement complet sous vide avec résine polymère classe H ($180^\circ\text{C}$), garantissant une protection parfaite contre l\'humidité et la corrosion.</li>
  <li><strong>Raccordements Industriels Robustes :</strong> Borniers de puissance dimensionnés pour câbles de fortes sections sous capot de protection ventilé IP20 à IP54 avec plots antivibratoires.</li>
</ol>
'''
)

IT_ES = dict(
    lang='es',
    dir='ltr',
    slug='power-quality-what-is-an-isolation-transformer-es',
    title='Calidad de Energía y Seguridad: ¿Qué es un Transformador de Aislamiento?',
    breadcrumb='Calidad de Energía y Transformadores de Aislamiento',
    read='10 min de lectura',
    alt='Transformador de aislamiento galvánico trifásico tipo seco (Serie SG) con devanados de cobre y pantalla electrostática de Faraday conectada a tierra',
    desc=('Quirófanos hospitalarios, variadores de frecuencia (VFD), máquinas herramienta CNC y centros de cómputo: ¿Qué es un transformador de aislamiento? '
          'Separación galvánica total, apantallamiento electrostático de Faraday, atenuación de ruido de modo común (> 60 dB) y sistemas de neutro aislado IT seguros.'),
    model='Serie SG / DG / JBK5: Transformadores de Aislamiento Galvánico Secos Trifásicos y Monofásicos (100VA a 500kVA, Rigidez 3kV, Pantalla Faraday, IEC 61558-2-4 / UL 1561)',
    category='Calidad de Energía y Transformadores de Aislamiento / Transformadores de Aislamiento Galvánico',
    kw='transformador de aislamiento &middot; transformador de aislamiento galvanico &middot; transformador seco trifasico &middot; transformador medico it &middot; pantalla de faraday &middot; transformador sg',
    specs=[
        ('Separación Galvánica Primario / Secundario', 'Desacoplamiento físico completo al 100% (Cero conexión metálica o conductora entre las bobinas de entrada y salida)'),
        ('Blindaje Electrostático (Pantalla de Faraday)', 'Lámina de cobre electrolítico continua conectada a tierra entre devanados (Atenuación de ruido de modo común &gt; 60 dB)'),
        ('Rigidez Dieléctrica y Tensión de Ensayo', 'Tensión de ensayo de aislamiento: 3000 V AC durante 1 min entre bobinas, y entre bobinas y el núcleo laminado de acero'),
        ('Material del Núcleo y Grado Magnético', 'Láminas de acero al silicio de grano orientado laminado en frío (CRGO) con ensamblaje a inglete step-lap de mínimas pérdidas'),
        ('Rango de Potencias Nominales de Fabricación', 'Capacidades de 100VA a 500kVA (Monofásicos serie DG: 100VA–50kVA ; Trifásicos serie SG: 1kVA–500kVA, 50/60 Hz)'),
        ('Tensiones de Primario y Secundario Estándar', 'Entradas estándar: 480V, 415V, 380V, 230V AC ; Salidas estándar: 400V, 380V, 220V, 208V, 120V AC (Relación 1:1 o reductor/elevador)'),
        ('Clase Térmica y Sistema de Aislamiento', 'Clase F ($155^\circ\text{C}$) o Clase H ($180^\circ\text{C}$) con impregnación al vacío y presión (VPI) de resina epóxica y papel Nomex'),
        ('Conformidad con Normativas Internacionales', 'Probado y certificado bajo normas internacionales IEC 61558-1, IEC 61558-2-4, UL 1561, CSA C22.2 y EN 61558-2-15 (Uso médico IT)')
    ],
    faqs=[
        ('¿Qué es un Transformador de Aislamiento y cómo protege los equipos eléctricos sensibles?',
         'Un Transformador de Aislamiento—conocido también como transformador de separación de circuitos o transformador de aislamiento galvánico—es '
         'un equipo de potencia estático cuyos devanados primario (entrada) y secundario (salida) están completamente separados físicamente, '
         'transmitiendo la energía eléctrica <strong>únicamente por inducción magnética</strong> a través del núcleo. '
         'En tableros industriales y salas hospitalarias : '
         '<ul>'
         '<li><strong>Eliminación de Bucles de Tierra (Ground Loops):</strong> En una red normal, el neutro se conecta a tierra en la subestación. '
         'Las diferencias de voltaje entre distintas tomas de tierra de una fábrica generan corrientes parásitas circulantes que dañan PLCs y computadoras. '
         'El transformador de aislamiento rompe el bucle de tierra al crear un secundario flotante y completamente independiente.</li>'
         '<li><strong>Protección Antielectrocución (Secundario Flotante Aislado):</strong> Tocar un conductor de fase en una red conectada a tierra '
         'provoca una descarga mortal a través del cuerpo humano. En un transformador de aislamiento sin referencia a tierra, tocar una sola fase '
         'no cierra ningún circuito hacia tierra, impidiendo la electrocución accidental.</li>'
         '</ul>'),
        ('¿Qué es la Pantalla Electrostática de Faraday y por qué es vital frente a variadores de frecuencia?',
         'Entre el primario y el secundario de un transformador estándar existe una capacitancia parásita entre capas ($C_{ps}$). '
         'Los picos de voltaje rápidos y ruidos armónicos de alta frecuencia de los variadores de frecuencia (VFD) cruzan esta capacitancia y dañan los microprocesadores. '
         'La <strong>Pantalla de Faraday</strong> de YOMIN consiste en una lámina de cobre conectada a tierra colocada entre los bobinados, '
         'la cual absorbe y deriva los ruidos de alta frecuencia a tierra antes de que alcancen el secundario, logrando una atenuación de <strong>60 a 80 dB</strong>.'),
        ('¿Cuál es la diferencia entre un Autotransformador y un Transformador de Aislamiento?',
         'El autotransformador tiene un solo devanado continuo que comparten la entrada y la salida. '
         'Existe una conexión metálica directa, por lo que <strong>no proporciona aislamiento galvánico</strong> y transmite todas las perturbaciones y fallas de tierra. '
         'El transformador de aislamiento posee dos bobinas completamente separadas e independientes con aislamiento de 3000 V, garantizando máxima seguridad.')
    ],
    cta='¿Diseña quirófanos hospitalarios en esquema IT médico, tableros de control con PLC, alimentación limpia para variadores de frecuencia o cuadros navales que requieren transformadores de aislamiento galvánico certificados IEC 61558-2-4 / UL 1561? YOMIN suministra transformadores serie SG/DG de máxima calidad.',
    body='''
<h2>El Cortafuegos Eléctrico Galvanizado para Equipos Industriales y Hospitalarios Críticos</h2>
<p>En plantas de manufactura automatizada, salas quirúrgicas hospitalarias, centros de procesamiento de datos y cuartos de control de procesos, los equipos electrónicos operan bajo exigencias extremas de continuidad y precisión.</p>
<p>Sin embargo, la red de energía comercial transporta continuas perturbaciones: armónicos de conmutación de variadores VFD, transitorios de rayo y ruidos eléctricos de modo común.</p>
<p>Asimismo, las diferencias de potencial entre mallas de tierra distantes en un edificio generan bucles de tierra destructivos que falsean señales analógicas y queman microchips.</p>
<p>El <strong>Transformador de Aislamiento Galvánico Tipo Seco (Serie SG / DG)</strong> proporciona la respuesta técnica definitiva : un transformador que transfiere energía sin ningún contacto metálico entre la entrada y la salida, anulando bucles de tierra, filtrando transitorios y protegiendo al personal contra electrocución.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie SG</h2>
<ol>
  <li><strong>Bobinados Primario y Secundario Físicamente Separados:</strong> Cobre electrolítico de alta pureza Cu-ETP (99.9%) con barreras aislantes de papel Nomex / mica ensayadas a 3000 V AC.</li>
  <li><strong>Pantalla de Blindaje Electrostático de Faraday:</strong> Lámina de cobre electrolítico continua conectada a tierra que deriva ruidos parásitos de alta frecuencia con atenuación superior a 60 dB.</li>
  <li><strong>Núcleo Magnético de Acero al Silicio CRGO:</strong> Chapa de grano orientado de muy bajas pérdidas con cortes a inglete step-lap que reducen el calentamiento en vacío y el zumbido acústico.</li>
  <li><strong>Impregnación al Vacío y Presión (VPI):</strong> Proceso completo en resina polimérica Clase H ($180^\circ\text{C}$) que sella el conjunto contra la humedad, polvo y atmósferas corrosivas.</li>
  <li><strong>Gabinete Metálico Ventilado Robusto:</strong> Envolvente de acero galvanizado con pintura epoxi horneada (IP20 a IP54), cáncamos de elevación y soportes antivibratorios inferiores.</li>
</ol>
'''
)

IT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='power-quality-what-is-an-isolation-transformer-ar',
    title='جودة الطاقة والسلامة الكهربائية: ما هو محول العزل الكهربائي (Isolation Transformer)؟',
    breadcrumb='جودة الطاقة ومحولات العزل الجلفاني',
    read='10 دقائق قراءة',
    alt='محول عزل كهربائي جلفاني ثلاثي الأوجه من النوع الجاف (موديل SG) بملفات نحاسية وحاجز فاراداي الكهروستاتيكي المؤرض',
    desc=('غرف العمليات بالمستشفيات، ومغيرات السرعة (VFD)، وماكينات CNC الرقمية، ومراكز البيانات: ما هو محول العزل الكهربائي (Isolation Transformer)؟ '
          'الفصل الجلفاني الفيزيائي الكامل، وحاجز فاراداي الكهروستاتيكي، وتخميد الضوضاء المشتركة (> 60 dB)، وشبكات النظام المعزول IT لمنع الصعق الكهربائي.'),
    model='سلسلة SG / DG / JBK5: محولات العزل الجلفاني الجافة ثلاثية وأحادية الطور (من 100VA إلى 500kVA، صمود عزل 3kV، حاجز فاراداي، معتمدة IEC 61558-2-4 / UL 1561)',
    category='جودة الطاقة ومحولات العزل الجلفاني / محولات العزل الجلفاني الجافة',
    kw='محول عزل كهربائي &middot; isolation transformer &middot; محول عزل جلفاني &middot; محول جاف ثلاثي الاوجه &middot; محول غرف العمليات it &middot; محول عزل sg',
    specs=[
        ('الفصل الجلفاني الفيزيائي بين الدخل والخرج', 'فصل مادي حقيقي بنسبة 100% (انعدام تام لأي اتصال معدني أو توصيلي بين ملفات الابتدائي وملفات الثانوي)'),
        ('حاجز الحجب الكهروستاتيكي (شاشة فاراداي)', 'شريحة نحاس إلكتروليتي متصلة مؤرضة تفصل بين الملفات (تخميد الضوضاء ذات النمط المشترك &gt; 60 dB)'),
        ('جهد الصمود الديزلكتريكي المعتمد للعزل', 'صمود عزل فائق مختبر: 3000 V AC لمدة دقيقة كاملة بين الملفات، وبين الملفات والقلب الحديدي المؤرض'),
        ('مادة وجودة تصنيع القلب المغناطيسي', 'شرائح صلب سيليكوني مدرفلة على البارد ذات توجيه بلوري (CRGO) بتجميع متداخل دقيق step-lap لفواقد مغناطيسية متدنية'),
        ('نطاق السعات والقدرات الاسمية المتاحة', 'سعات قياسية من 100VA إلى 500kVA (أحادي الطور DG: 100VA–50kVA؛ ثلاثي الطور SG: 1kVA–500kVA، تردد 50/60 هرتز)'),
        ('خيارات جهود الدخل والخرج للمحول', 'جهود الدخل: 480V و 415V و 380V و 230V AC؛ جهود الخرج: 400V و 380V و 220V و 208V و 120V AC (نسبة 1:1 أو خافض/رافع)'),
        ('فئة العزل الحراري ونظام الراتنج', 'فئة حرارية Class F ($155^\circ\text{C}$) أو Class H ($180^\circ\text{C}$) بالتشريب بالراتنج البوليمري تحت التفريغ والضغط (VPI)'),
        ('شهادات المطابقة للمواصفات الدولية', 'مختبر ومعتمد وفقاً للمواصفات القياسية IEC 61558-1 و IEC 61558-2-4 و UL 1561 و CSA C22.2 و EN 61558-2-15 للمستشفيات')
    ],
    faqs=[
        ('ما هو محول العزل الكهربائي (Isolation Transformer) وكيف يوفر الحماية للمعدات الحساسة؟',
         'محول العزل الكهربائي—والمعروف في الهندسة الكهربائية باسم محول الفصل الجلفاني أو محول الأمان الطبي—هو '
         'محول كهربائي صُممت ملفاته الابتدائية (الدخل) والثانوية (الخرج) لتكون منفصلة فيزيائياً وميكانيكياً بصورة تامة، '
         'حيث تنتقل الطاقة الكهربائية بينهما <strong>عبر الحث الكهرومغناطيسي النقي فقط</strong> دون وجود أي سلك يربط بينهما. '
         'وفي البيئات الصناعية والطبية الحساسة : '
         '<ul>'
         '<li><strong>القضاء على الحلقات الأرضية (Ground Loops):</strong> في شبكات الكهرباء العادية، يربط خط التعادل (النيوترال) بالأرض في محطة التغذية. '
         'وعند توصيل أجهزة كمبيوتر أو وحدات PLC متفرقة بنقاط تأريض مختلفة داخل المصنع، تنشأ فروق جهد تولد تيارات أرضية دوارة تشوه قراءات الحساسات '
         'وتتلف الدوائر الإلكترونية. يكسر محول العزل هذه الحلقات نهائياً بتوفير نقطة مرجعية جديدة ونظيفة للخرج.</li>'
         '<li><strong>منع الصعق الكهربائي القاتل (الخرج المعزول العائم):</strong> لمس سلك الفاز الحي في شبكة عادية يؤدي لسريان التيار عبر جسم الإنسان '
         'نحو الأرض مسبباً الوفاة. أما في الخرج المعزول غير المرتبط بالأرض، فإن لمس خط واحد بالخطأ لا يكمل أي دائرة كهربائية، مما يمنع حدوث الصدمة.</li>'
         '</ul>'),
        ('ما هي شاشة فاراداي الكهروستاتيكية ولماذا تعتبر حاسمة مع مغيرات التردد والإنفرتر؟',
         'بين الملفات الابتدائية والثانوية في أي محول عادي توجد سعة سعوية طفيلية ($C_{ps}$). '
         'وتعبر النبضات الكهربائية العابرة والترددات العالية المشوشة المنبعثة من مغيرات السرعة (VFD) عبر هذه السعة لتصل إلى المعالجات الحساسة. '
         'تقوم <strong>شاشة فاراداي</strong> في محولات يمين—وهي رقاقة نحاسية ممتدة بين الملفات ومربوطة بالأرض—بامتصاص هذه التشوهات '
         'وتفريغها مباشرة نحو الأرض قبل عبورها للملف الثانوي، محققة تخميداً ممتازاً للضوضاء يتجاوز <strong>60 إلى 80 ديسيبل</strong>.'),
        ('ما هو الفارق الجوهري بين المحول الذاتي (Autotransformer) ومحول العزل؟',
         'يستخدم المحول الذاتي ملفاً نحاسياً واحداً مشتركاً بين الدخل والخرج، وبالتالي يوجد اتصال معدني كهربائي مباشر يمنع أي عزل جلفاني '
         'وينقل التوافقيات وصدمات الأرض مباشرة إلى الأحمال. '
         'بينما يحتوي محول العزل على ملفين منفصلين تماماً بعزل 3000 فولت، مما يجعله إلزامياً لغرف العمليات بالمستشفيات والماكينات الدقيقة.')
    ],
    cta='هل تعمل على تجهيز غرف العمليات الطبية بنظام IT المعزول، أو لوحات تحكم أتمتة المصانع PLC، أو تغذية مغيرات السرعة VFD بالطاقة النقية التي تتطلب محولات عزل جلفاني جافة معتمدة IEC 61558-2-4 / UL 1561؟ تصنع يمين (YOMIN) محولات سلسلة SG/DG بأعلى معايير الجودة.',
    body='''
<h2>الجدار الناري الكهرومغناطيسي الآمن للمهمات الصناعية والطبية الحساسة</h2>
<p>في المنشآت الصناعية المؤتمتة، وغرف العمليات الجراحية بالمستشفيات، ومراكز البيانات الكبرى، تعمل الأجهزة الإلكترونية الحساسة ووحدات التحكم المبرمج PLC على مدار الساعة دون انقطاع.</p>
<p>ومع ذلك، تعج شبكات الكهرباء العامة بتشوهات وتوافقيات عنيفة ناتجة عن مفاتيح الإنفرتر ومغيرات السرعة VFD، وصدمات الصواعق المفاجئة.</p>
<p>وفضلاً عن ذلك، فإن التفاوت في جهود التأريض بين المباني المختلفة يولد تيارات تسريب دوارة خطيرة في خطوط الأرضي (Ground Loops) تسبب أخطاء جسيمة في الإشارات وتدمر كروت التحكم الإلكترونية.</p>
<p>يقدم <strong>محول العزل الجلفاني من النوع الجاف (سلسلة SG / DG)</strong> الحل الهندسي القياسي الحاسم: محول قدرة متطور ينقل الطاقة عبر فجوة عزل مغناطيسية نقية تفصل دائرة الدخل عن الخرج، مما يقضي على الحلقات الأرضية، ويرشح النبضات المشوشة، ويحمي الأفراد من مخاطر الصعق الكهربائي.</p>

<h2>المكونات الهندسية وميزات التصميم لسلسلة محولات SG</h2>
<ol>
  <li><strong>ملفات ابتدائية وثانوية منفصلة فيزيائياً بالكامل:</strong> أسلاك نحاس إلكتروليتي نقي Cu-ETP (99.9%) مع فواصل عزل Nomex وميكا تتحمل اختبار صمود عزل يبلغ 3000 V AC.</li>
  <li><strong>شاشة حجب كهروستاتيكية من نحاس فاراداي:</strong> رقاقة نحاسية متصلة بين الملفات ومؤرضة مباشرة تبتلع النبضات السريعة وتوفر تخميداً للضوضاء يفوق 60 ديسيبل.</li>
  <li><strong>قلب مغناطيسي من شرائح الصلب السيليكوني CRGO:</strong> صلب مدرفل على البارد عالي النفاذية بتجميع mitered step-lap لخفض فواقد اللاحمل والضوضاء الصوتية.</li>
  <li><strong>تشريب حراري متطور بالراتنج تحت الضغط والتفريغ (VPI):</strong> معالجة كاملة براتنج بوليمري عالي الجودة يتحمل حرارة Class H ($180^\circ\text{C}$) ويمنع الرطوبة والأبخرة الكيميائية.</li>
  <li><strong>هيكل معدني قوي مع حماية IP20 إلى IP54:</strong> كابينة صلب مجلفن مطلية ببودرة إلكتروستاتيكية مع فتحات تهوية طبيعية، وحلقات رفع ووسائد مطاطية لامتصاص الاهتزازات.</li>
</ol>
'''
)

# ==============================================================================
# 2. TWO-HOLE CABLE LUG (EN, FR, ES, AR)
# ==============================================================================

THL_EN = dict(
    lang='en',
    dir='ltr',
    slug='heavy-duty-connections-what-is-a-two-hole-cable-lug',
    title='Heavy-Duty Connections: What Is a Two-Hole Cable Lug?',
    breadcrumb='Cable Terminals &amp; Heavy-Duty Lugs',
    read='10 min read',
    alt='Heavy-duty Two-Hole Tinned Copper Compression Cable Lugs (Model DT-2 series) bolted with dual bolts to vertical copper busbars inside electrical switchgear',
    desc=('Utility substation switchgear, telecom DC battery backup rooms, and high-vibration generator connections: What is a two-hole cable lug? '
          'How dual NEMA hole spacing, anti-rotation mechanical locking, long-barrel hydraulic compression, 99.9% electrolytic copper, and UL 486A-486B standards eliminate loose bolted connections and thermal runaway.'),
    model='Model DT-2 / YM-2HL Series Heavy-Duty Long-Barrel Two-Hole Tinned Copper Compression Lugs (35 mm² to 630 mm² / #6 AWG to 750 MCM, Dual NEMA Spacing, UL 486A-486B / IEC 61238-1)',
    category='Cable Terminals & Heavy-Duty Lugs / Two-Hole Compression Lugs',
    kw='what is a two hole cable lug &middot; two hole cable lug &middot; 2 hole copper lug &middot; long barrel two hole compression lug &middot; dual hole battery lug &middot; dt-2 lug',
    specs=[
        ('Conductor Raw Material & Copper Purity', 'Seamless heavy-wall electrolytic copper tube (Cu-ETP 99.9% purity; electrical conductivity &ge; 99.5% IACS)'),
        ('Surface Electro-Tin Plating Finish', 'Bright electro-tin electroplating (&ge; 8 &mu;m thickness; passes 96-hour salt spray ASTM B117 anti-corrosion test)'),
        ('Cable Wire Gauge Cross-Section Range', 'Full wire range: 35 mm&sup2; to 630 mm&sup2; (Imperial sizing: #6 AWG, 1/0, 2/0, 4/0 AWG, 250 MCM, 350 MCM, up to 750 MCM)'),
        ('Bolt Hole Configuration & NEMA Spacing', 'Precision-punched dual bolt holes: Standard NEMA spacing (1-inch or 1-3/4-inch center-to-center; bolt sizes M8, M10, M12, 1/2&quot;)'),
        ('Barrel Construction & Crimp Accommodations', 'Long-barrel heavy-duty design (Accommodates 2 to 3 hydraulic compression crimps for maximum tensile pull-out strength)'),
        ('Internal Inspection Window / Solid Palm', 'Solid-back blind-end palm design to prevent moisture ingress into stranded conductors in outdoor / telecom environments'),
        ('Rated Operating Voltage & Current Limits', 'Maximum operating voltage: 600V to 35 kV (UL rated for power distribution; rated to conductor ampacity up to 1000A+)'),
        ('International Manufacturing Safety Standards', 'Fully tested and certified compliant with UL 486A-486B (Wire Connectors), CSA C22.2, and IEC 61238-1 Class A')
    ],
    faqs=[
        ('What is a Two-Hole Cable Lug and why is it preferred over single-hole lugs in heavy-duty switchgear?',
         'A Two-Hole Cable Lug—frequently designated as a dual-hole compression lug, long-barrel 2-hole terminal, or NEMA-spaced battery lug—is '
         'a heavy-duty electrical connector fabricated from seamless electrolytic copper tube with an extended flat contact palm featuring '
         'two precision-drilled bolt holes aligned along the axis of the conductor. '
         'In high-current electrical infrastructure and telecommunication power systems: '
         '<ul>'
         '<li><strong>Anti-Rotation Mechanical Locking:</strong> When heavy, stiff power cables (such as 4/0 AWG, 250 MCM, or 500 MCM) are terminated '
         'with a single-bolt lug, any lateral cable movement, thermal expansion, or physical vibration exerts continuous rotational torque on the single bolt. '
         'Over time, this twists the lug, works the bolt loose, dramatically increases joint contact resistance, and triggers catastrophic thermal runaway. '
         'A two-hole lug secures the connection with two separate bolts, mechanically locking the palm flat against the busbar and completely preventing rotation.</li>'
         '<li><strong>Doubled Contact Surface Area:</strong> The extended palm provides more than double the metal-to-metal contact surface area '
         'against the switchboard busbar, cutting electrical joint resistance in half and lowering operating temperatures under continuous full-load currents.</li>'
         '</ul>'),
        ('Why do Telecommunications and Data Center standards (NEBS) mandate Two-Hole Lugs on battery buses?',
         'In telecommunication central offices, mobile cell sites, and hyperscale data centers running -48V DC power plants with multi-megawatt battery banks, '
         'Network Equipment-Building System (NEBS) standards strictly prohibit single-hole lugs on DC power buses: '
         '<ul>'
         '<li><strong>High DC Current Reliability:</strong> DC circuits carry massive continuous currents (thousands of amperes) at low voltages. '
         'A loose connection causing a mere 5 milliohm contact resistance drop produces immense localized heat ($P = I^2 \times R$) that ignites cable insulation.</li>'
         '<li><strong>Seismic &amp; Maintenance Immunity:</strong> Technicians pulling adjacent cables through battery racks can accidentally bump single-hole lugs, '
         'spinning them into adjacent live buses and causing explosive DC short-circuits. Two-hole lugs provide rigid structural immobility under seismic shocks and maintenance activities.</li>'
         '</ul>'),
        ('What is the difference between Long-Barrel and Standard-Barrel Two-Hole Compression Lugs?',
         'Standard-barrel lugs feature a short crimp zone intended for light-duty commercial wiring, accommodating only a single hydraulic crimp die press. '
         '<strong>Long-Barrel Two-Hole Lugs (YOMIN DT-2 series)</strong> feature an extended tubular copper barrel that accommodates two or three consecutive '
         'die crimps. This dramatically increases mechanical pull-out strength (withstanding over 500 to 1,500 lbs of cable tension without slipping), '
         'maximizes electrical contact area between stranded wire strands and copper tube, and provides superior resistance to thermal cycling fatigue.')
    ],
    cta='Designing utility substation switchgear, telecom central office DC battery backup rooms, industrial transformer ground buses, or heavy generator distribution panels requiring certified UL 486A-486B / IEC 61238-1 heavy-duty two-hole copper compression lugs (35mm² to 630mm² / #6 AWG to 750 MCM, NEMA dual bolt spacing)? YOMIN manufactures precision DT-2 series lugs.',
    body='''
<h2>The Anti-Rotation Electrical Foundation for High-Current Power Infrastructure</h2>
<p>Inside modern electrical utility substations, telecommunication DC power plants, industrial motor control centers, and high-vibration generator enclosures carrying currents from <strong>100A to over 1000A</strong>, electrical bolted terminations face severe mechanical and thermal stresses.</p>
<p>Terminating heavy-gauge power conductors (such as 4/0 AWG, 250 MCM, 350 MCM, or 500 MCM) using conventional single-hole cable lugs introduces a major mechanical vulnerability: cable stiffness and thermal expansion exert relentless rotational torque on the single mounting bolt.</p>
<p>Over months of operational heating cycles and transformer acoustic vibration, single bolts work loose. Micro-gaps form between the lug palm and the copper busbar, joint resistance spikes, and severe localized overheating triggers explosive arc-flash fires.</p>
<p>The <strong>Heavy-Duty Long-Barrel Two-Hole Copper Compression Lug (Model DT-2 / YM-2HL Series)</strong> provides the permanent engineering solution: a rugged seamless electrolytic copper connector featuring two precision NEMA-spaced bolt holes that mechanically lock the terminal against rotation, double the contact surface area, and guarantee vibration-proof electrical continuity.</p>

<h2>Engineering Anatomy: Inside a Model DT-2 Long-Barrel Two-Hole Copper Lug</h2>
<ol>
  <li><strong>Seamless Heavy-Wall Electrolytic Copper Tube (Cu-ETP 99.9%):</strong> Extruded from pure copper with thick, uniform sidewalls that resist cracking under high-tonnage hydraulic crimping forces, providing maximum electrical conductivity (&ge; 99.5% IACS).</li>
  <li><strong>Dual NEMA Standard Spaced Bolt Holes:</strong> Features two precision-punched holes with standard 1-inch or 1-3/4-inch center-to-center spacing, accommodating pairs of M8, M10, M12, or 1/2" high-tensile bolts for complete anti-rotation clamping.</li>
  <li><strong>Extended Long-Barrel Crimp Zone:</strong> Designed with extended barrel length allowing 2 to 3 consecutive hydraulic hex or indent crimps, maximizing mechanical pull-out tensile strength under severe cable tension.</li>
  <li><strong>Electro-Tin Protective Plating (&ge; 8 &mu;m):</strong> Heavy surface electro-tinning prevents atmospheric copper oxidation and inhibits galvanic corrosion when bolted directly to aluminum or tin-plated copper busbars.</li>
  <li><strong>Solid-Back Blind-End Palm Design:</strong> Solid seamless transition between barrel and palm with zero inspection hole, preventing rain, condensation, and environmental sulfur from entering the stranded cable core in outdoor and telecom installations.</li>
</ol>

<h2>Comparison: Heavy-Duty Two-Hole Lug vs. Standard Single-Hole Lug vs. Mechanical Set-Screw Lug</h2>
<table>
  <thead>
    <tr>
      <th>Operational Metric</th>
      <th>Mechanical Set-Screw Screw Lug</th>
      <th>Standard Single-Hole Compression Lug</th>
      <th>YOMIN Heavy-Duty Two-Hole Lug (DT-2 Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Anti-Rotation Joint Security</strong></td>
      <td>Poor: Single mounting bolt allows cable torque to twist lug.</td>
      <td>Poor: Prone to rotational loosening under thermal cycles.</td>
      <td><strong>100% Anti-Rotation: Dual NEMA bolts mechanically lock joint forever.</strong></td>
    </tr>
    <tr>
      <td><strong>Vibration &amp; Seismic Immunity</strong></td>
      <td>Low: Screws back out under continuous motor vibration.</td>
      <td>Moderate: Single bolt works loose under harmonic vibration.</td>
      <td><strong>Immune: Dual bolts with Belleville washers absorb 100% of vibration.</strong></td>
    </tr>
    <tr>
      <td><strong>Busbar Contact Surface Area</strong></td>
      <td>Small: Compact rectangular base with limited contact width.</td>
      <td>Standard: Single circular contact zone around mounting bolt.</td>
      <td><strong>Double Surface: Extended rectangular palm cuts joint resistance in half.</strong></td>
    </tr>
    <tr>
      <td><strong>Mechanical Pull-Out Tensile Strength</strong></td>
      <td>Moderate: Screw point clamps individual cable strands.</td>
      <td>Standard: Short barrel accommodates only 1 hydraulic crimp.</td>
      <td><strong>Maximum: Long barrel accommodates 2–3 hydraulic crimps for extreme pull-out.</strong></td>
    </tr>
    <tr>
      <td><strong>Telecom NEBS / Data Center Compliance</strong></td>
      <td>Prohibited on critical DC battery bus infrastructure.</td>
      <td>Strictly prohibited on high-current central office DC buses.</td>
      <td><strong>Mandatory: Fully meets NEBS and Telcordia telecommunication standards.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

THL_FR = dict(
    lang='fr',
    dir='ltr',
    slug='heavy-duty-connections-what-is-a-two-hole-cable-lug-fr',
    title="Raccordements Électriques Haute Puissance : Qu'est-ce qu'une Cosse à Deux Trous ?",
    breadcrumb='Cosses Électriques &amp; Raccordements Haute Puissance',
    read='10 min de lecture',
    alt='Cosses à sertir en cuivre étamé à deux trous de fixation (Série DT-2) fixées par double boulonnerie sur des barres de distribution dans un tableau électrique',
    desc=('Postes de transformation HTA/BT, bancs de batteries télécoms et raccordements haute puissance : Qu\'est-ce qu\'une cosse à deux trous de fixation ? '
          'Double perçage NEMA anti-rotation, fût long pour sertissages multiples, cuivre électrolytique 99,9% et conformité aux normes UL 486A-486B / CEI 61238-1.'),
    model='Série DT-2 / YM-2HL : Cosses à Sertir en Cuivre Électrolytique Étamé à Fût Long et Double Plage NEMA (35 mm² à 630 mm², Anti-Rotation, CEI 61238-1 / UL 486A-486B)',
    category='Cosses Électriques & Raccordements Haute Puissance / Cosses à Sertir à Deux Trous',
    kw='cosse a deux trous &middot; cosse deux trous cuivre &middot; cosse a sertir fut long &middot; cosse anti rotation &middot; cosse nema 2 trous &middot; cosse dt-2',
    specs=[
        ('Matière Première & Pureté du Cuivre', 'Tube de cuivre électrolytique massif sans soudure Cu-ETP (pureté 99,9% ; conductivité électrique &ge; 99,5% IACS)'),
        ('Traitement de Surface et Protection', 'Étamage électrolytique brillant continu (&ge; 8 &mu;m ; résistance éprouvée à 96h de brouillard salin selon ASTM B117)'),
        ('Plage des Sections de Câbles Raccordables', 'Gamme complète de 35 mm&sup2; à 630 mm&sup2; (calibres normalisés : 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500 et 630 mm&sup2;)'),
        ('Configuration et Entraxe des Deux Trous', 'Double perçage de précision aux entraxes NEMA normalisés (25,4 mm / 1 pouce ou 44,5 mm / 1-3/4 pouce ; vis M8, M10, M12)'),
        ('Conception du Fût et Longueur de Sertissage', 'Fût long renforcé permettant 2 à 3 sertissages hydrauliques consécutifs pour une résistance mécanique à l\'arrachement maximale'),
        ('Étanchéité du Raccordement et Plage Pleine', 'Plage massive sans trou de visite pour empêcher la pénétration d\'humidité et de poussières corrosives dans l\'âme du câble'),
        ('Tension et Intensité Admissibles de Service', 'Tension assignée : 600V à 35 kV (utilisable sur jeux de barres basse et moyenne tension ; intensités continues jusqu\'à 1000A+)'),
        ('Conformité aux Normes Internationales', 'Certifié et conforme aux normes CEI 61238-1 Classe A, UL 486A-486B, CSA C22.2 et exigences télécoms NEBS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Cosse à Deux Trous et pourquoi surpasse-t-elle la cosse à trou unique ?',
         'Une Cosse à Deux Trous de Fixation—souvent désignée sous le terme de cosse NEMA à double perçage ou cosse à fût long—est '
         'une cosse tubulaire robuste en cuivre électrolytique étamé dont la plage de raccordement plane comporte '
         'deux trous de perçage alignés selon l\'axe du câble. '
         'Dans les postes de distribution électrique et raccordements industriels : '
         '<ul>'
         '<li><strong>Sécurité Mécanique Anti-Rotation :</strong> Les câbles de forte section (de 95 à 400 mm²) sont très rigides. '
         'Avec une cosse ordinaire à un seul trou, toute vibration ou dilatation thermique exerce un couple de torsion qui finit par desserrer '
         'l\'unique boulon, créant un point chaud et un arc électrique destructeur. La cosse à deux trous est bloquée par deux boulons indépendants, '
         'rendant toute rotation physiquement impossible.</li>'
         '<li><strong>Surface de Contact Électrique Doublée :</strong> La plage allongée offre plus du double de surface de contact métallique '
         'avec le jeu de barres, divisant par deux la résistance de contact et garantissant un échauffement minimal sous fort courant.</li>'
         '</ul>'),
        ('Pourquoi les normes Télécoms et Data Centers (NEBS) imposent-elles les cosses à deux trous ?',
         'Dans les centrales téléphoniques et centres de données fonctionnant sous courant continu -48V avec de puissants bancs de batteries : '
         '<ul>'
         '<li><strong>Résistance aux Échauffements par Courant Continu :</strong> Les courants continus atteignent des milliers d\'ampères. '
         'Le moindre desserrage de boulon provoque un échauffement violent ($P = R \times I^2$) capable d\'enflammer les isolants de câbles.</li>'
         '<li><strong>Protection Contre les Courts-Circuits Accidentels :</strong> Lors des interventions d\'entretien, manipuler un câble voisin '
         'peut faire pivoter une cosse à un trou contre une barre adjacente sous tension, provoquant une explosion par court-circuit. '
         'La cosse à deux trous reste strictement immobile.</li>'
         '</ul>'),
        ('Quelle est la différence entre une cosse à fût standard et une cosse à fût long ?',
         'Le fût standard ne permet qu\'une seule passe de sertissage hydraulique. '
         'La <strong>cosse à fût long YOMIN DT-2</strong> permet deux à trois sertissages hydrauliques successifs, '
         'multipliant la résistance mécanique à la traction par deux et assurant une compacité moléculaire parfaite entre les brins de cuivre et le tube.')
    ],
    cta='Vous concevez des cellules de distribution HTA/BT, des bancs de batteries de secours télécoms ou des raccordements de générateurs exigeant des cosses à sertir en cuivre étamé à deux trous certifiées CEI 61238-1 / UL 486A-486B (35 à 630 mm², anti-rotation NEMA) ? YOMIN fabrique des cosses série DT-2 de haute qualité.',
    body='''
<h2>La Connexion Anti-Rotation Indispensable pour la Distribution Électrique Haute Puissance</h2>
<p>Dans les postes de transformation électrique, les armoires de distribution industrielle, les centrales de télécommunications et les raccordements de groupes électrogènes transportant des intensités de <strong>100A à plus de 1000A</strong>, les liaisons boulonnées subissent des contraintes mécaniques et thermiques extrêmes.</p>
<p>Raccorder des câbles de fortes sections (de 95 mm² à 400 mm²) avec des cosses à un seul trou présente une vulnérabilité mécanique majeure : la rigidité naturelle du câble et les dilatations thermiques exercent un couple de rotation continu sur l\'unique boulon de fixation.</p>
<p>Au fil des mois et des vibrations acoustiques des transformateurs, l\'écrou finit par se desserrer. La résistance de contact augmente brutalement, entraînant un échauffement en cascade jusqu\'à l\'apparition d\'arcs électriques destructeurs.</p>
<p>La <strong>Cosse à Sertir en Cuivre à Fût Long et Deux Trous de Fixation (Série DT-2 / YM-2HL)</strong> apporte la solution technique définitive : une cosse massive en cuivre étamé pourvue de deux perçages normalisés NEMA qui verrouillent mécaniquement la connexion contre toute rotation et doublent la surface de contact électrique.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série DT-2</h2>
<ol>
  <li><strong>Tube en Cuivre Électrolytique Pur Sans Soudure (Cu-ETP 99,9%) :</strong> Parois épaisses et homogènes garantissant une conductivité électrique maximale (&ge; 99,5% IACS) et une excellente tenue au sertissage hydraulique.</li>
  <li><strong>Double Perçage Normalisé NEMA :</strong> Deux trous poinçonnés de précision aux entraxes standards de 25,4 mm (1") ou 44,5 mm (1-3/4"), compatibles avec vis M8, M10 ou M12 pour un verrouillage anti-rotation absolu.</li>
  <li><strong>Fût Long pour Sertissage Renforcé :</strong> Longueur tubulaire accrue permettant 2 à 3 sertissages hydrauliques consécutifs, garantissant une résistance à l\'arrachement mécanique exceptionnelle.</li>
  <li><strong>Protection par Étamage Électrolytique Renforcé (&ge; 8 &mu;m) :</strong> Traitement d\'étamage brillant empêchant l\'oxydation du cuivre et évitant la corrosion galvanique sur les barres d\'aluminium ou de cuivre.</li>
  <li><strong>Plage Massive Étanche :</strong> Conception sans trou de visite empêchant la pénétration d\'humidité et d\'agents corrosifs dans l\'âme du câble en milieu extérieur ou tropical.</li>
</ol>
'''
)

THL_ES = dict(
    lang='es',
    dir='ltr',
    slug='heavy-duty-connections-what-is-a-two-hole-cable-lug-es',
    title='Conexiones de Alta Resistencia: ¿Qué es un Terminal de Dos Orificios (Two-Hole Lug)?',
    breadcrumb='Terminales Eléctricos y Conexiones de Potencia',
    read='10 min de lectura',
    alt='Terminales de compresión de cobre estañado de dos orificios (Serie DT-2) apernados firmemente con doble perno a barras colectoras de cobre en un tablero eléctrico',
    desc=('Subestaciones de distribución eléctrica, salas de baterías de telecomunicaciones y conexiones de generadores de alta vibración: ¿Qué es un terminal de dos orificios? '
          'Doble perforación NEMA antirotación, cañón largo para múltiples compresiones, cobre electrolítico 99.9% y normas UL 486A-486B / IEC 61238-1.'),
    model='Serie DT-2 / YM-2HL: Terminales de Compresión de Cobre Estañado de Cañón Largo con Dos Orificios NEMA (35 mm² a 630 mm² / #6 AWG a 750 MCM, IEC 61238-1 / UL 486A-486B)',
    category='Terminales Eléctricos y Conexiones de Potencia / Terminales de Compresión de Dos Orificios',
    kw='terminal de dos orificios &middot; terminal de cobre 2 huecos &middot; zapata de dos orificios &middot; terminal compresion cañon largo &middot; terminal antirotacion nema &middot; terminal dt-2',
    specs=[
        ('Materia Prima y Pureza del Cobre Conductor', 'Tubo de cobre electrolítico macizo sin costura Cu-ETP (pureza 99.9% ; conductividad eléctrica &ge; 99.5% IACS)'),
        ('Recubrimiento Protector de Estaño Electrolítico', 'Estañado electrolítico brillante continuo (&ge; 8 &mu;m ; ensayado a 96 horas de niebla salina bajo norma ASTM B117)'),
        ('Rango de Secciones y Calibres de Conductor', 'Gama completa de 35 mm&sup2; a 630 mm&sup2; (Calibres AWG/MCM: #6 AWG, 1/0, 2/0, 4/0 AWG, 250 MCM, 350 MCM hasta 750 MCM)'),
        ('Configuración de Doble Orificio y Distancia NEMA', 'Perforación doble precisa con separación estándar NEMA (25.4 mm / 1 pulgada o 44.5 mm / 1-3/4 pulgada ; pernos M8, M10, M12)'),
        ('Construcción del Cañón y Crimpado Múltiple', 'Diseño de cañón largo de alta resistencia (permite de 2 a 3 compresiones hidráulicas para máxima fuerza de tracción mecánica)'),
        ('Pala Maciza Sellada sin Orificio de Inspección', 'Diseño ciego sin mirilla para evitar el ingreso de humedad y polvo corrosivo hacia los hilos del conductor en intemperie'),
        ('Tensión y Capacidad de Corriente de Servicio', 'Tensión de trabajo nominal: 600V a 35 kV (utilizable en barras de baja y media tensión ; corrientes continuas de hasta 1000A+)'),
        ('Conformidad con Normativas Internacionales', 'Probado y certificado bajo normas internacionales UL 486A-486B, CSA C22.2, IEC 61238-1 Clase A y estándares NEBS')
    ],
    faqs=[
        ('¿Qué es un Terminal de Dos Orificios (Two-Hole Lug) y por qué supera al terminal tradicional de un solo perno?',
         'Un Terminal de Compresión de Dos Orificios—conocido también como terminal NEMA de doble agujero, zapata de dos huecos o terminal de cañón largo—es '
         'un conector eléctrico de alta resistencia forjado a partir de tubo de cobre electrolítico estañado cuya pala plana dispone de '
         'dos orificios de fijación alineados longitudinalmente con el eje del cable. '
         'En subestaciones eléctricas y tableros de potencia : '
         '<ul>'
         '<li><strong>Fijación Mecánica Antirotación:</strong> Los cables gruesos de potencia (de 4/0 AWG a 500 MCM) son muy rígidos. '
         'Con un terminal común de un solo perno, las vibraciones y la dilatación térmica transmiten un par de torsión constante que afloja la tuerca. '
         'El terminal de dos orificios se sujeta con dos pernos separados, bloqueando físicamente el terminal contra la barra e impidiendo cualquier giro.</li>'
         '<li><strong>Doble Superficie de Contacto Eléctrico:</strong> La pala alargada brinda más del doble de área de contacto metálico '
         'con la barra colectora, reduciendo a la mitad la resistencia de unión y garantizando una operación a menor temperatura bajo plena carga.</li>'
         '</ul>'),
        ('¿Por qué las normas de Telecomunicaciones y Data Centers (NEBS) exigen terminales de dos orificios?',
         'En salas de baterías de corriente continua -48V de telecomunicaciones y centros de cómputo : '
         '<ul>'
         '<li><strong>Seguridad Ante Altas Corrientes DC:</strong> Las corrientes en corriente continua son masivas (miles de amperios). '
         'Cualquier mínimo aflojamiento de perno eleva la resistencia de contacto disparando el calentamiento ($P = I^2 \times R$) e incendiando cables.</li>'
         '<li><strong>Prevención de Cortocircuitos por Mantenimiento:</strong> Al mover cables adyacentes, un terminal de un perno puede rotar '
         'y tocar una barra contigua energizada provocando una explosión. Los terminales de dos orificios garantizan una inmovilidad absoluta.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre un terminal de cañón estándar y uno de cañón largo?',
         'El cañón estándar solo permite una compresión hidráulica simple. '
         'El <strong>terminal de cañón largo YOMIN DT-2</strong> admite dos o tres compresiones consecutivas con prensa hidráulica, '
         'duplicando la resistencia mecánica a la tracción y logrando una fusión compacta entre los hilos del cable y el tubo de cobre.')
    ],
    cta='¿Diseña celdas de subestaciones eléctricas, salas de baterías de telecomunicaciones o conexiones de generadores que requieren terminales de compresión de cobre de dos orificios certificados UL 486A-486B / IEC 61238-1 (35 a 630 mm², antirotación NEMA)? YOMIN suministra terminales serie DT-2 de máxima fiabilidad.',
    body='''
<h2>La Conexión Antirotación Esencial para Sistemas Eléctricos de Alta Capacidad</h2>
<p>En el interior de subestaciones eléctricas de distribución, tableros generales de baja tensión, cuartos de baterías de telecomunicaciones y generadores que transportan intensidades de <strong>100A a más de 1000A</strong>, las uniones apernadas sufren continuas exigencias mecánicas y térmicas.</p>
<p>Conectar conductores de gran calibre (desde 4/0 AWG hasta 500 MCM) utilizando terminales convencionales de un solo orificio presenta un punto crítico de falla : la rigidez del cable y las oscilaciones térmicas ejercen un esfuerzo de palanca continuo sobre el único perno de fijación.</p>
<p>Con el paso del tiempo y las vibraciones mecánicas, la unión se afloja. Se generan microseparaciones entre la pala del terminal y la barra de cobre, disparando la resistencia de contacto y desatando sobrecalentamientos peligrosos.</p>
<p>El <strong>Terminal de Compresión de Cobre de Cañón Largo y Dos Orificios (Serie DT-2 / YM-2HL)</strong> representa la respuesta técnica definitiva : un conector de cobre electrolítico estañado con dos perforaciones NEMA que fijan mecánicamente la zapata contra el giro, duplicando la superficie de contacto eléctrico.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie DT-2</h2>
<ol>
  <li><strong>Tubo de Cobre Electrolítico Puro Sin Costura (Cu-ETP 99.9%):</strong> Espesor de pared uniforme que soporta elevadas presiones de crimpado hidráulico sin fisurarse, garantizando conductividad máxima (&ge; 99.5% IACS).</li>
  <li><strong>Perforación Doble Estándar NEMA:</strong> Dos orificios punzonados con separación estándar de 25.4 mm (1") o 44.5 mm (1-3/4"), para pernos M8, M10 o M12 asegurando fijación antirotación total.</li>
  <li><strong>Cañón Largo para Prensado Múltiple:</strong> Longitud extendida que admite de 2 a 3 compresiones hexagonales consecutivas, garantizando máxima resistencia mecánica a la tracción.</li>
  <li><strong>Estañado Electrolítico Protector (&ge; 8 &mu;m):</strong> Recubrimiento superficial de estaño que evita la oxidación del cobre e impide la corrosión galvánica al apernarse sobre barras de aluminio.</li>
  <li><strong>Pala Maciza Sellada sin Mirilla:</strong> Construcción cerrada que impide el ingreso de humedad ambiental y contaminantes hacia el interior del conductor en instalaciones exteriores.</li>
</ol>
'''
)

THL_AR = dict(
    lang='ar',
    dir='rtl',
    slug='heavy-duty-connections-what-is-a-two-hole-cable-lug-ar',
    title='التوصيلات الكهربائية للخدمة الشاقة: ما هي كابل شوكة ذات الثقبين (Two-Hole Cable Lug)؟',
    breadcrumb='كابلات ونهايات التوصيل للخدمة الشاقة',
    read='10 دقائق قراءة',
    alt='كابل شوكة نحاسية مضغوطة مطلية بالقصدير ذات ثقبين (موديل DT-2) مثبتة بمسامير مزدوجة على قضبان توزيع نحاسية في لوحة كهربائية',
    desc=('محطات المحولات وتوزيع الكهرباء، وغرف بطاريات الاتصالات DC، وتوصيلات المولدات عالية الاهتزاز: ما هي كابل شوكة ذات الثقبين (Two-Hole Lug)؟ '
          'التثبيت المزدوج المانع للدوران وفق معايير NEMA، والماسورة الطويلة للكبس المتعدد، والنحاس الإلكتروليتي 99.9%، ومعايير UL 486A-486B / IEC 61238-1.'),
    model='سلسلة DT-2 / YM-2HL: كابل شوكة نحاسية مضغوطة ذات ماسورة طويلة وثقبين بنظام NEMA (من 35 مم² إلى 630 مم²، مانعة للدوران، معتمدة IEC 61238-1 / UL 486A-486B)',
    category='كابلات ونهايات التوصيل للخدمة الشاقة / كابل شوكة بالكبس ذات الثقبين',
    kw='كابل شوكة ذات ثقبين &middot; two hole cable lug &middot; كابل شوكة نحاس ثقبين &middot; كابل شوكة مانعة للدوران &middot; كابل شوكة nema &middot; كابل شوكة dt-2',
    specs=[
        ('المادة الخام ونقاوة النحاس الموصل', 'أنبوب نحاس إلكتروليتي نقي غير ملحوم Cu-ETP (نقاوة 99.9%؛ توصيلية كهربائية &ge; 99.5% IACS)'),
        ('المعالجة السطحية ومقاومة التآكل', 'طلاء إلكتروليتي بالقصدير اللامع المتصل (&ge; 8 ميكرون؛ صمود باختبار الضباب الملحي 96 ساعة طبقاً لـ ASTM B117)'),
        ('نطاق مقاطع وأقطار الكابلات المتوافقة', 'تغطية كاملة من 35 مم&sup2; حتى 630 مم&sup2; (مقاسات AWG/MCM: من #6 AWG و 4/0 AWG و 250 MCM وحتى 750 MCM)'),
        ('هندسة الثقبين والتباعد المعياري NEMA', 'تثقيب دقيق بتباعد NEMA القياسي (مسافة بين المركزين 25.4 مم / 1 بوصة أو 44.5 مم / 1-3/4 بوصة؛ مسامير M8 إلى M12)'),
        ('تصميم الماسورة وقابلية الكبس المتعدد', 'ماسورة طويلة للخدمة الشاقة تستوعب من 2 إلى 3 كبسات هيدروليكية متتالية لأقصى قوة شد ميكانيكية مانعة للسحب'),
        ('تصميم الكف المصمت الخالي من الفتحات', 'تصميم مصمت بالكامل بدون فتحة معاينة لمنع تسرب الرطوبة والأبخرة إلى شعيرات الكابل في البيئات الخارجية'),
        ('الجهد الكهربائي والتيارات المقننة للخدمة', 'جهد تشغيل معتمد: من 600 فولت حتى 35 كيلو فولت (لقضبان الجهد المنخفض والمتوسط؛ تيارات مستمرة تتجاوز 1000A+)'),
        ('المطابقة للمواصفات والاعتمادات الدولية', 'مختبر ومعتمد بالكامل وفقاً للمعايير الدولية UL 486A-486B و CSA C22.2 و IEC 61238-1 فئة A واشتراطات NEBS للاتصالات')
    ],
    faqs=[
        ('ما هي كابل شوكة ذات الثقبين (Two-Hole Cable Lug) ولماذا تتفوق على كابل شوكة ذات الثقب الواحد؟',
         'كابل شوكة ذات الثقبين—والمعروفة في هندسة التركيبات الكهربائية باسم كابل شوكة NEMA ذات التثقيب المزدوج أو كابل شوكة ذات الماسورة الطويلة—هي '
         'نهاية طرفية نحاسية صلبة عالية المتانة مُصنعة من أنبوب نحاس إلكتروليتي غير ملحوم، يتميز كف التوصيل المنبسط فيها '
         'بوجود ثقبين متوازيين على طول محور الكابل. '
         'وفي محطات توزيع الكهرباء ولوحات الجهد المنخفض : '
         '<ul>'
         '<li><strong>التثبيت الميكانيكي المانع للدوران:</strong> كابلات القدرة السميكة (من 95 مم² إلى 400 مم²) تتميز بصلابة ميكانيكية عالية. '
         'ومع كابل شوكة ذات الثقب الواحد، فإن الاهتزازات والتمدد الحراري يولدان عزم دوران مستمر يؤدي لارتخاء المسمار وتآكل نقطة التوصيل واشتعالها. '
         'بينما يتم تثبيت كابل شوكة ذات الثقبين بمسمارين منفصلين، مما يقفل الكف بإحكام تام على البارة ويمنع أي دوران نهائياً.</li>'
         '<li><strong>مضاعفة مساحة التلامس الكهربائي:</strong> يوفر الكف الطويل أكثر من ضعف مساحة التلامس النحاسي مع قضيب التوزيع، '
         'مما يقلل مقاومة نقطة التوصيل إلى النصف ويضمن انخفاض درجات حرارة التشغيل تحت الأحمال الثقيلة.</li>'
         '</ul>'),
        ('لماذا تفرض معايير غرف الاتصالات ومراكز البيانات (NEBS) استخدام كابل شوكة ذات الثقبين؟',
         'في محطات الاتصالات ومراكز البيانات التي تعمل بجهد تيار مستمر -48V DC وبنوك بطاريات ضخمة : '
         '<ul>'
         '<li><strong>أمان الأحمال عند التيارات العالية:</strong> تسري تيارات هائلة تصل لآلاف الأمبيرات في دوائر التيار المستمر. '
         'وأي ارتخاء طفيف لمسمار يرفع المقاومة وينتج حرارة هائلة كفيلة بإشعال عوازل الكابلات.</li>'
         '<li><strong>منع القصر الكهربائي العرضي أثناء الصيانة:</strong> عند شد كابلات مجاورة أثناء الصيانة، قد تدور كابل شوكة ذات الثقب الواحد '
         'لتلامس بارة مجاورة حية وتحدث انفجاراً كهربائياً مدمراً. تضمن كابل شوكة ذات الثقبين ثباتاً صخرياً لا يتزحزح.</li>'
         '</ul>'),
        ('ما هو الفارق بين كابل شوكة ذات الماسورة العادية وذات الماسورة الطويلة؟',
         'تستوعب الماسورة العادية كبسة هيدروليكية واحدة فقط. '
         'بينما تتميز <strong>كابل شوكة يمين DT-2 ذات الماسورة الطويلة</strong> بتصميم يتيح كبس لقم الكبس الهيدروليكي مرتين أو ثلاث مرات متتالية، '
         'مما يضاعف قوة التماسك الميكانيكي ويمنع انسحاب الكابل تحت قوى الشد الميكانيكية العنيفة.')
    ],
    cta='هل تعمل على تصميم خلايا محطات التحويل الكهربائية، أو غرف بطاريات الاتصالات ومراكز البيانات، أو لوحات المولدات التي تتطلب كابل شوكة نحاسية ذات ثقبين معتمدة UL 486A-486B / IEC 61238-1 (من 35 إلى 630 مم²، مانعة للدوران بنظام NEMA)؟ تصنع يمين (YOMIN) نهايات سلسلة DT-2 بأعلى معايير المتانة.',
    body='''
<h2>الأساس الميكانيكي المانع للدوران لمنظومات التوزيع الكهربائي عالية القدرة</h2>
<p>في محطات تحويل الطاقة الكهربائية، ولوحات التوزيع الصناعية الرئيسية، ومحطات تغذية الاتصالات بالتيار المستمر، وغرف المولدات التي تنقل تيارات تتراوح بين <strong>100 أمبير وأكثر من 1000 أمبير</strong>، تتعرض نهايات الكابلات لإجهادات ميكانيكية وحرارية قاسية.</p>
<p>إن توصيل كابلات التغذية السميكة (من مقاس 95 مم² إلى 400 مم² وأكثر) باستخدام كابل شوكة تقليدية ذات ثقب واحد ينطوي على نقطة ضعف خطيرة: فصلابة الكابل القوية والتمدد الحراري يمارسان عزم دوران والتواء مستمر على مسمار التثبيت الوحيد.</p>
<p>ومع مرور شهور من دورات السخونة والبرودة واهتزازات المحولات، يرتخي المسمار تدريجياً، مما يرفع مقاومة التلامس ويتسبب في ارتفاع حراري متسارع ينتهي بشرر كهربائي مدمر.</p>
<p>تقدم <strong>كابل شوكة النحاسية ذات الماسورة الطويلة والثقبين (سلسلة DT-2 / YM-2HL)</strong> الحل الهندسي الجذري الدائم: نهاية طرفية متينة من النحاس الإلكتروليتي المطلي بالقصدير مزودة بثقبين قياسيين بنظام NEMA يثبتان الكابل بمسمارين يمنعان الدوران تماماً ويضاعفان مساحة التلامس الكهربائي.</p>

<h2>المكونات الهندسية وميزات التصميم لسلسلة كابل شوكة DT-2</h2>
<ol>
  <li><strong>أنبوب نحاس إلكتروليتي نقي غير ملحوم (Cu-ETP 99.9%):</strong> سماكة جدار أنبوبية متسقة تتحمل قوى الكبس الهيدروليكي العالية دون تشقق، مع توصيلية كهربائية ممتازة (&ge; 99.5% IACS).</li>
  <li><strong>تثقيب مزدوج بتباعد NEMA القياسي المعتمد:</strong> ثقبان بتباعد محوري دقيق 25.4 مم (1 بوصة) أو 44.5 مم (1-3/4 بوصة) متوافق مع مسامير M8 أو M10 أو M12 لمنع الدوران نهائياً.</li>
  <li><strong>ماسورة طويلة للكبس الهيدروليكي المزدوج والثلاثي:</strong> طول ماسورة ممتد يتيح كبس الكابل من مرتين إلى ثلاث مرات، مما يحقق قوة شد ميكانيكية فائقة ضد الانزلاق.</li>
  <li><strong>طلاء إلكتروليتي واقٍ بالقصدير اللامع (&ge; 8 ميكرون):</strong> يمنع تأكسد النحاس تماماً ويلغي التآكل الجلفاني عند الربط على بارات التوزيع المصنوعة من الألمنيوم أو النحاس.</li>
  <li><strong>كف مصمت ومحكم الإغلاق:</strong> خلو الكف من أي فتحات فحص يمنع تسرب الرطوبة والأبخرة الحمضية إلى داخل شعيرات الكابل في البيئات الخارجية والصناعية القاسية.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1018 = [
    IT_EN, IT_FR, IT_ES, IT_AR,
    THL_EN, THL_FR, THL_ES, THL_AR
]
