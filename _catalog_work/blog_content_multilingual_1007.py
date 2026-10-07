# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-07:
1. Manual Service Disconnect (MSD) for BESS Battery Packs (EN, FR, ES, AR)
2. J-Type Fuse Cutout for Utility Feeder Pillars (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. MANUAL SERVICE DISCONNECT (MSD) (EN, FR, ES, AR)
# ==============================================================================

MSD_EN = dict(
    lang='en',
    dir='ltr',
    slug='bess-battery-safety-what-is-a-manual-service-disconnect',
    title='Battery Energy Storage Systems (BESS): What Is a Manual Service Disconnect (MSD)?',
    breadcrumb='Flexible Busbars &amp; Energy Storage',
    read='10 min read',
    alt='Heavy-duty high-voltage Manual Service Disconnect (Model MSD series) with integrated DC fuse and HVIL installed on a BESS lithium battery pack enclosure',
    desc=('Commercial and utility-scale Battery Energy Storage Systems (BESS) and EV battery pack safety: What is a manual service disconnect (MSD)? '
          'How two-stage extraction handles, integrated 1000V DC fuses, and High Voltage Interlock Loops (HVIL) eliminate arc flash hazards during maintenance.'),
    model='Model MSD Series High-Voltage Manual Service Disconnect with Integrated DC Fuse and HVIL (up to 1000V DC, 630A, IP67/IP6K9K)',
    category='Flexible Busbars & Energy Storage / Manual Service Disconnects (MSD)',
    kw='what is a manual service disconnect &middot; manual service disconnect &middot; msd connector &middot; high voltage msd &middot; bess manual service disconnect &middot; hvil msd plug',
    specs=[
        ('Rated System Operational Voltage', 'Rated continuous operating voltage up to 1000V DC / 1500V DC; insulation dielectric test voltage &ge; 5000V AC / 1 minute'),
        ('Continuous Current & Integrated Fuse Ratings', 'Modular continuous current ratings from 150A, 250A, 350A, 400A, up to 630A DC (accommodating high-speed aR/gR DC fuse links)'),
        ('Integrated High Voltage Interlock Loop (HVIL)', 'Dual-pin integrated signal circuit that physically disconnects 10 to 30 milliseconds *before* high-voltage power contacts separate'),
        ('Two-Stage Mechanical Lever Extraction', 'Tool-free two-step extraction handle: Stage 1 breaks HVIL and opens signal circuit; Stage 2 unlocks and extracts the main fuse plug'),
        ('Ingress Protection & Environmental Sealing', 'Certified IP67 and IP6K9K high-pressure waterproof/dustproof in mated condition with silicone compression seals; IP2X touch-proof unmated'),
        ('Contact Terminal Material & Plating', 'High-purity forged tellurium copper contacts with thick silver plating (&ge; 5 &mu;m) for sub-milliohm contact resistance (&le; 0.2 m&Omega;)'),
        ('Mechanical Durability & Endurance Life', 'Rated mechanical life &ge; 500 mating/unmating cycles without degradation; flame-retardant thermoplastic housing (UL 94 V-0)'),
        ('International Safety Standards Compliance', 'Certified to UL 4128, USCAR-2, USCAR-37, IEC 60664-1, ISO 6469, and UN 38.3 transport safety requirements')
    ],
    faqs=[
        ('What is a Manual Service Disconnect (MSD) and why is it mandatory in high-voltage BESS and EV battery packs?',
         'A Manual Service Disconnect—universally abbreviated as an MSD—is '
         'a specialized high-voltage mechanical safety disconnect plug featuring an integrated DC fuse and a two-stage manual extraction lever. '
         'It is mounted directly on the exterior casing of high-voltage battery enclosures (ranging from 400V to 1000V+ DC) in utility-scale Battery Energy Storage Systems (BESS), '
         'commercial solar microgrids, and electric commercial vehicles. '
         'An MSD fulfills three non-negotiable life-safety functions: '
         '<ul>'
         '<li><strong>1. Physical Circuit Interruption for Technicians:</strong> When servicing, transporting, or repairing high-voltage battery racks, '
         'technicians cannot rely solely on software or electronic contactors (which can fail closed or suffer welded contacts). '
         'Pulling the MSD physically splits the series battery string in half, dropping the rack voltage to harmless, non-lethal potential levels.</li>'
         '<li><strong>2. Integrated High-Breaking DC Short-Circuit Protection:</strong> Inside the plug handle, the MSD houses a fast-acting ceramic DC fuse '
         '(rated up to 630A at 1000V DC with 50kA interrupting capacity). If an external short circuit occurs, the fuse blows in milliseconds, protecting battery cells from catastrophic thermal runaway.</li>'
         '<li><strong>3. Arc Flash Elimination via Two-Stage Lever:</strong> DC power has no zero-crossing voltage point, making DC arcs explosive and persistent. '
         'The two-stage lever design guarantees that the High Voltage Interlock Loop (HVIL) drops system power *before* physical contacts disengage, preventing deadly arc flashes.</li>'
         '</ul>'),
        ('How does the two-stage extraction lever and HVIL physically eliminate DC arc flash during manual disconnection?',
         'Pulling an MSD plug under high-current load without protection would create a blinding plasma explosion. The MSD prevents this through an exact mechanical interlock sequence: '
         '<ul>'
         '<li><strong>Stage 1 (HVIL Interruption & Pause):</strong> The technician flips the primary orange release latch and lifts the lever to the intermediate position (~45 degrees). '
         'This action separates the internal High Voltage Interlock Loop (HVIL) signal pins while the heavy high-voltage power fuse contacts remain fully engaged. '
         'The Battery Management System (BMS) instantly senses the broken HVIL circuit and opens the main DC vacuum/air contactors, de-energizing the battery loop in under 20 milliseconds. '
         'A mechanical stop physically blocks the lever, forcing the technician to pause.</li>'
         '<li><strong>Stage 2 (Dead-Circuit Pin Separation):</strong> The technician presses a secondary red safety release button, unlocking the remaining lever stroke. '
         'The handle pulls the high-voltage power fuse contacts out of the female socket jaws. '
         'Because the circuit was already de-energized by the BMS in Stage 1, the physical separation occurs under zero current (dead circuit), completely eliminating electric arcs and contact erosion.</li>'
         '</ul>'),
        ('What is the difference between an MSD and an Energy Storage Quick Connector?',
         'While both components serve high-voltage battery energy storage installations, their mechanical and electrical purposes are distinct: '
         '<ul>'
         '<li><strong>Manual Service Disconnect (MSD):</strong> A safety maintenance disconnect and overcurrent device. '
         'It features a two-stage extraction handle, houses an internal replaceable high-speed DC fuse link inside the plug body, and is permanently bolted '
         'to the battery pack bulkhead to split series strings during servicing.</li>'
         '<li><strong>Energy Storage Quick Connector:</strong> A high-current power transfer cable fitting (cable-to-bus or cable-to-rack). '
         'It does not contain an internal fuse, features a 360-degree rotating cable head, and is used to interconnect battery module terminals '
         'to external DC combiner busbars or inverter inputs.</li>'
         '</ul>')
    ],
    cta='Designing containerized battery energy storage systems (BESS), commercial solar-plus-storage racks, or electric vehicle battery enclosures requiring certified 1000V DC Manual Service Disconnects (MSD) with integrated fuses? YOMIN manufactures industrial-grade MSD units.',
    body='''
<h2>The Critical Safety Barrier in High-Voltage Energy Storage Racks</h2>
<p>Modern commercial and utility-scale <strong>Battery Energy Storage Systems (BESS)</strong> pack thousands of kilowatt-hours into containerized enclosures operating at high voltages from <strong>600V to 1000V+ DC</strong>. These immense battery banks provide grid-scale frequency response, solar peak shifting, and microgrid backup power.</p>
<p>However, working on live DC battery packs represents an extreme hazard for electrical technicians, utility operators, and emergency first responders. Unlike AC networks where current passes through zero 100 to 120 times per second, direct current (DC) sustains intense, non-extinguishing electric arcs that can instantly vaporize metal and trigger explosive battery fires.</p>
<p>International safety standards—including <strong>NFPA 855, UL 9540, and ISO 6469</strong>—mandate a dedicated, tool-free mechanical device to isolate high-voltage strings before any human intervention.</p>
<p>The <strong>Manual Service Disconnect (Model MSD Series)</strong> is the standardized solution: a high-voltage safety plug combining an internal high-speed DC fuse, a two-stage arc-prevention lever, and an integrated High Voltage Interlock Loop (HVIL).</p>

<h2>Engineering Anatomy: Inside a Certified 1000V DC Manual Service Disconnect</h2>
<ol>
  <li><strong>Ergonomic Two-Stage Extraction Handle:</strong> Engineered with a mechanical interlock that enforces a mandatory physical delay between breaking the low-voltage HVIL circuit (Stage 1) and separating the high-voltage power pins (Stage 2).</li>
  <li><strong>Integrated High-Rupturing-Capacity Ceramic DC Fuse:</strong> Protects the battery pack against catastrophic external short-circuit faults (up to 50kA breaking capacity), mounted securely inside the insulated plug body.</li>
  <li><strong>Dual-Pin High Voltage Interlock Loop (HVIL):</strong> Shorter auxiliary micro-switch pins disconnect 10–30 ms before the power circuit breaks, signaling the BMS to drop the main contactors under zero load.</li>
  <li><strong>Silver-Plated Crown Spring Contact Terminals:</strong> Machined from tellurium copper with multi-contact louvered springs and &ge; 5 &mu;m silver plating, maintaining sub-milliohm contact resistance under 400A–630A continuous load.</li>
  <li><strong>IP67 / IP6K9K Dual-O-Ring Compression Sealing:</strong> High-grade fluorosilicone gaskets prevent ingress of water, salt fog, and dust inside outdoor containerized BESS enclosures.</li>
  <li><strong>IP2X Touch-Proof Receptacle Shrouds:</strong> Deeply recessed female contacts prevent human fingers from touching live busbars even when the MSD plug is completely removed.</li>
</ol>

<h2>Comparison: Manual Service Disconnect (MSD) vs. DC Molded Case Circuit Breaker (MCCB)</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>DC Molded Case Circuit Breaker (MCCB)</th>
      <th>YOMIN High-Voltage Manual Service Disconnect (MSD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Physical Contact Air-Gap Visibility</strong></td>
      <td>Hidden: Contacts sealed inside breaker casing; cannot visually confirm separation.</td>
      <td><strong>Visible Air Gap: Complete physical removal of plug creates 100% visible, foolproof isolation gap.</strong></td>
    </tr>
    <tr>
      <td><strong>Contact Welding Failure Risk</strong></td>
      <td>High: Electronic contacts can weld closed during high-current short-circuit events.</td>
      <td><strong>Zero Risk: Plug removal physically breaks the circuit mechanically, regardless of electrical state.</strong></td>
    </tr>
    <tr>
      <td><strong>Integrated Fast-Acting Fuse Protection</strong></td>
      <td>Thermal-magnetic or electronic trip unit with 20–50 ms mechanical delay.</td>
      <td><strong>Integrated ultra-fast silver-element ceramic DC fuse clears massive faults in &le; 5 ms.</strong></td>
    </tr>
    <tr>
      <td><strong>Tool-Free Operation &amp; Touch Safety</strong></td>
      <td>Requires operating lever; live busbar terminals exposed under maintenance panels.</td>
      <td><strong>100% Tool-free two-stage handle; IP2X touch-proof female sockets prevent accidental shock.</strong></td>
    </tr>
    <tr>
      <td><strong>Enclosure Space &amp; Weight Footprint</strong></td>
      <td>Heavy, bulky unit requiring dedicated chassis and mounting brackets.</td>
      <td><strong>Compact, panel-mounted plug-and-socket design optimized for dense battery module faces.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MSD_FR = dict(
    lang='fr',
    dir='ltr',
    slug='bess-battery-safety-what-is-a-manual-service-disconnect-fr',
    title="Systèmes de Stockage d'Énergie BESS : Qu'est-ce qu'un Sectionneur Manuel de Service (MSD) ?",
    breadcrumb='Barres Souples &amp; Stockage d\'Énergie',
    read='10 min de lecture',
    alt='Sectionneur manuel de service haute tension (Série MSD) avec fusible DC intégré et boucle HVIL installé sur un rack de batteries BESS',
    desc=('Sécurité des systèmes de stockage d\'énergie par batterie (BESS) et packs de batteries haute tension : Qu\'est-ce qu\'un sectionneur manuel de service (MSD) ? '
          'Levier d\'extraction à deux étages, cartouche fusible DC 1000V intégrée et boucle HVIL pour éliminer les risques d\'arc électrique.'),
    model='Série MSD : Sectionneurs Manuels de Service Haute Tension avec Fusible DC Intégré et Boucle HVIL (jusqu\'à 1000V DC, 630A, IP67/IP6K9K)',
    category='Barres Souples & Stockage d\'Énergie / Sectionneurs de Service (MSD)',
    kw='sectionneur manuel de service &middot; prise msd &middot; connecteur msd &middot; fusible dc bess &middot; boucle hvil msd &middot; coupure batterie haute tension',
    specs=[
        ('Tension Nominale de Service et Isolement', 'Tension assignée continue jusqu\'à 1000V DC / 1500V DC ; tension d\'essai diélectrique &ge; 5000V AC pendant 1 minute'),
        ('Courant Permanent et Calibre des Fusibles', 'Calibres modulaires de 150A, 250A, 350A, 400A jusqu\'à 630A DC (logeant des cartouches fusibles céramiques ultra-rapides aR/gR)'),
        ('Boucle de Verrouillage Haute Tension (HVIL)', 'Circuit pilote à deux broches s\'ouvrant mécaniquement 10 à 30 ms *avant* la séparation des contacts de puissance'),
        ('Poignée d\'Extraction Mécanique à Deux Étages', 'Levier ergonomique sans outil : l\'étage 1 coupe le signal HVIL ; l\'étage 2 déverrouille et extrait le bloc fusible'),
        ('Degré de Protection et Étanchéité IP', 'Certifié IP67 et IP6K9K à l\'état verrouillé avec joints toriques en silicone ; sécurité tactile IP2X à l\'état ouvert'),
        ('Matériau des Pôles et Traitement de Surface', 'Contacts en cuivre tellure forgé à ressorts multiples avec argenture électrolytique épaisse (&ge; 5 &mu;m)'),
        ('Endurance Mécanique et Durabilité', 'Endurance mécanique &ge; 500 cycles de manœuvre ; boîtier en polymère thermoplastique ignifugé UL 94 V-0'),
        ('Normes Internationales de Sécurité', 'Conforme aux normes UL 4128, USCAR-2, USCAR-37, CEI 60664-1, ISO 6469 et prescriptions de transport UN 38.3')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Sectionneur Manuel de Service (MSD) et pourquoi est-il obligatoire sur les racks de batteries BESS ?',
         'Un Sectionneur Manuel de Service—universellement appelé prise MSD (Manual Service Disconnect)—est '
         'un organe de coupure et de sécurité mécanique haute tension intégrant un fusible DC haute performance et un levier d\'extraction à deux temps. '
         'Il est fixé directement sur la face avant des bacs de batteries (fonctionnant de 400V à plus de 1000V DC) dans les conteneurs BESS et véhicules électriques. '
         'Le MSD remplit trois missions vitales : '
         '<ul>'
         '<li><strong>1. Coupure Physique Visible pour la Maintenance :</strong> Les techniciens ne peuvent se fier uniquement à des relais électroniques. '
         'L\'extraction manuelle du MSD sépare physiquement la chaîne de cellules en série, divisant la tension totale en deux demi-tensions inoffensives.</li>'
         '<li><strong>2. Protection par Fusible Ultra-Rapide Intégré :</strong> Le corps de la prise abrite un fusible céramique DC (jusqu\'à 630A sous 1000V DC '
         'avec un pouvoir de coupure de 50kA) qui élimine les courts-circuits en quelques millisecondes, empêchant tout emballement thermique.</li>'
         '<li><strong>3. Éradication de l\'Arc Électrique grâce au Levier en 2 Temps :</strong> Le courant continu ne s\'éteignant pas naturellement, '
         'la cinématique du levier garantit que la boucle HVIL coupe l\'alimentation générale *avant* que les broches de puissance ne se séparent.</li>'
         '</ul>'),
        ('Comment la poignée à deux étages et le circuit HVIL éliminent-ils l\'arc électrique ?',
         'La déconnexion s\'effectue selon une séquence chronologique mécanique infaillible : '
         '<ul>'
         '<li><strong>Étage 1 (Coupure HVIL et pause mécanique) :</strong> Le technicien soulève le levier à 45°. '
         'Ce premier mouvement déconnecte les broches auxiliaires de la boucle HVIL alors que les contacts de puissance restent fermés. '
         'Le contrôleur BMS détecte l\'ouverture et ordonne aux contacteurs principaux d\'ouvrir le circuit en moins de 20 ms. Une butée mécanique bloque le levier.</li>'
         '<li><strong>Étage 2 (Séparation hors tension) :</strong> Le technicien appuie sur le bouton rouge de déverrouillage pour achever la course du levier. '
         'Les broches de puissance se séparent alors dans un circuit totalement désexcité (zéro ampère), sans aucune étincelle ni détérioration.</li>'
         '</ul>'),
        ('Quelle est la différence entre un MSD et un Connecteur Rapide de Stockage ?',
         'Bien qu\'ils équipent tous deux les conteneurs BESS, leurs fonctions sont distinctes : '
         '<ul>'
         '<li><strong>Sectionneur Manuel de Service (MSD) :</strong> Organe de sécurité et de coupure d\'urgence intégrant un fusible DC amovible. '
         'Il est fixé sur la façade pour ouvrir physiquement le circuit lors des interventions de maintenance.</li>'
         '<li><strong>Connecteur Rapide de Stockage d\'Énergie :</strong> Raccord de puissance sur câble servant à interconnecter les modules de batterie '
         'au jeu de barres principal, sans fusible interne.</li>'
         '</ul>')
    ],
    cta='Vous concevez des conteneurs de stockage d\'énergie par batterie (BESS), des armoires photovoltaïques hybrides ou des packs de batteries haute tension nécessitant des sectionneurs manuels de service (MSD) certifiés UL 4128 ? YOMIN fabrique des prises MSD haute sécurité.',
    body='''
<h2>Le Dispositif de Sécurité Ultime des Systèmes BESS Haute Tension</h2>
<p>Les <strong>systèmes de stockage d\'énergie par batterie à grande échelle (BESS)</strong> concentrent des milliers de kilowattheures dans des conteneurs sous des tensions continues atteignant <strong>600V à plus de 1000V DC</strong>.</p>
<p>Cependant, intervenir sur des batteries en courant continu sous haute tension expose les techniciens au danger mortel de l\'arc électrique continu (Arc Flash), capable de vaporiser le cuivre instantanément en l\'absence de passage à zéro naturel.</p>
<p>Les normes internationales de sécurité (notamment <strong>NFPA 855 et UL 9540</strong>) imposent la présence d\'un organe de coupure manuelle visible et manœuvrable sans outil.</p>
<p>Le <strong>Sectionneur Manuel de Service (Série MSD)</strong> apporte la solution technique standardisée : une prise de coupure étanche IP67 associant un fusible DC ultra-rapide, une boucle de verrouillage électrique HVIL et un levier d\'extraction à temporisation mécanique.</p>

<h2>Conception Mécanique et Éléments de Fiabilité</h2>
<ol>
  <li><strong>Poignée d\'Extraction à Deux Temps :</strong> Impose un délai mécanique forcé entre l\'ouverture du circuit de pilotage HVIL (Étage 1) et l\'ouverture des contacts de puissance (Étage 2).</li>
  <li><strong>Fusible Céramique Haute Tension Intégré :</strong> Protège les cellules contre les courts-circuits violents (pouvoir de coupure 50kA sous 1000V DC).</li>
  <li><strong>Broches de Sécurité HVIL :</strong> Plus courtes que les contacts principaux pour commander la coupure des contacteurs généraux avant séparation physique.</li>
  <li><strong>Contacts en Cuivre Argenté à Bagues de Ressort :</strong> Garantissent une résistance de contact &le; 0,2 m&Omega; pour éviter tout échauffement sous 630A continus.</li>
</ol>
'''
)

MSD_ES = dict(
    lang='es',
    dir='ltr',
    slug='bess-battery-safety-what-is-a-manual-service-disconnect-es',
    title='Sistemas de Almacenamiento BESS: ¿Qué es un Desconectador Manual de Servicio (MSD)?',
    breadcrumb='Barras Flexibles y Almacenamiento',
    read='10 min de lectura',
    alt='Desconectador manual de servicio de alta tensión (Serie MSD) con fusible DC integrado y lazo HVIL instalado en gabinete de baterías de litio BESS',
    desc=('Sistemas de almacenamiento de energía con baterías (BESS) y seguridad en paquetes de baterías de alta tensión: ¿Qué es un desconectador manual de servicio (MSD)? '
          'Palanca de extracción en dos etapas, fusible DC integrado de 1000V y lazo HVIL para erradicar arcos eléctricos en mantenimiento.'),
    model='Serie MSD: Desconectadores Manuales de Servicio de Alta Tensión con Fusible DC y Lazo HVIL (hasta 1000V DC, 630A, IP67/IP6K9K)',
    category='Barras Flexibles y Almacenamiento / Desconectadores Manuales (MSD)',
    kw='desconectador manual de servicio &middot; enchufe msd &middot; conector msd &middot; fusible dc bess &middot; lazo hvil msd &middot; corte bateria alta tension',
    specs=[
        ('Tensión Nominal de Operación y Ensayo', 'Tensión nominal continua de servicio hasta 1000V DC / 1500V DC; tensión de ensayo dieléctrico &ge; 5000V AC durante 1 minuto'),
        ('Capacidad de Corriente y Calibre de Fusible', 'Capacidades continuas de 150A, 250A, 350A, 400A hasta 630A DC (alojando fusibles cerámicos ultrarrápidos aR/gR)'),
        ('Lazo de Enclavamiento de Alta Tensión (HVIL)', 'Circuito de control integrado que se desconecta mecánicamente 10 a 30 ms *antes* que los contactos de potencia'),
        ('Palanca de Extracción de Dos Etapas', 'Mecanismo ergonómico sin herramientas: Etapa 1 abre la señal HVIL; Etapa 2 destraba y extrae el cuerpo del fusible'),
        ('Grado de Estanqueidad y Protección IP', 'Certificado IP67 e IP6K9K en estado acoplado con sellos de silicona; protección táctil IP2X al retirar el conector'),
        ('Material y Tratamiento de los Bornes', 'Contactos de cobre al telurio forjado con resortes laminares y recubrimiento grueso de plata pura (&ge; 5 &mu;m)'),
        ('Vida Útil Mecánica y Resistencia al Fuego', 'Vida mecánica &ge; 500 ciclos de maniobra; carcasa de polímero termoplástico autoextinguible (UL 94 V-0)'),
        ('Normativas Internacionales de Seguridad', 'Conforme con normas UL 4128, USCAR-2, USCAR-37, IEC 60664-1, ISO 6469 y exigencias de transporte UN 38.3')
    ],
    faqs=[
        ('¿Qué es un Desconectador Manual de Servicio (MSD) y por qué es obligatorio en racks BESS y vehículos eléctricos?',
         'Un Desconectador Manual de Servicio—conocido por sus siglas en inglés MSD (Manual Service Disconnect)—es '
         'un dispositivo mecánico de corte y seguridad de alta tensión que incorpora un fusible DC de alta velocidad y una palanca de extracción en dos tiempos. '
         'Se instala en la envolvente exterior de los módulos de baterías (que operan de 400V a más de 1000V DC) en sistemas BESS y plantas solares. '
         'El MSD cumple tres objetivos vitales de seguridad: '
         '<ul>'
         '<li><strong>1. Corte Físico Visible para Mantenimiento:</strong> No se puede depender exclusivamente de contactores electrónicos. '
         'La extracción del MSD divide físicamente la cadena de baterías en dos mitades con tensiones no letales, garantizando la seguridad del operario.</li>'
         '<li><strong>2. Protección ante Cortocircuitos con Fusible DC Integrado:</strong> Aloja un fusible cerámico de acción rápida (hasta 630A a 1000V DC '
         'con 50kA de poder de corte) que despeja fallas severas en milisegundos, previniendo el embalamiento térmico del banco.</li>'
         '<li><strong>3. Eliminación del Arco Eléctrico con Palanca en 2 Fases:</strong> La corriente continua carece de cruce por cero. '
         'El diseño cinemático de la palanca asegura que el circuito de control HVIL ordene el corte de energía *antes* de que los contactos de potencia se separen.</li>'
         '</ul>'),
        ('¿Cómo erradica el arco eléctrico el mecanismo de extracción en dos etapas con lazo HVIL?',
         'La desconexión sigue una secuencia mecánica obligatoria: '
         '<ul>'
         '<li><strong>Etapa 1 (Apertura de HVIL y pausa obligada):</strong> El operario levanta la palanca hasta 45°. '
         'Este movimiento desconecta los pines auxiliares del lazo HVIL mientras los contactos principales de potencia siguen cerrados. '
         'El BMS detecta la apertura y abre los contactores generales en menos de 20 ms. Un tope mecánico detiene la palanca.</li>'
         '<li><strong>Etapa 2 (Separación sin carga eléctrica):</strong> El operario presiona el botón rojo de seguridad para completar la extracción. '
         'Los contactos principales de potencia se separan en un circuito completamente desenergizado (cero corriente), sin chispas ni desgaste.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre un MSD y un Conector Rápido de Baterías?',
         'Aunque ambos conviven en un contenedor BESS, tienen propósitos diferentes: '
         '<ul>'
         '<li><strong>Desconectador Manual de Servicio (MSD):</strong> Dispositivo de seguridad y mantenimiento con fusible DC integrado que se monta en el panel '
         'para abrir físicamente el circuito en serie de las baterías.</li>'
         '<li><strong>Conector Rápido de Almacenamiento:</strong> Enchufe de potencia sobre cable que conecta eléctricamente los módulos con las barras colectoras, '
         'sin fusible interno.</li>'
         '</ul>')
    ],
    cta='¿Diseña contenedores de almacenamiento de energía con baterías (BESS), microrredes solares o sistemas de baterías de alta tensión que requieren desconectadores manuales de servicio (MSD) bajo norma UL 4128? YOMIN fabrica desconectadores MSD industriales de máxima seguridad.',
    body='''
<h2>El Dispositivo de Seguridad Indispensable en Almacenamiento BESS</h2>
<p>Los <strong>sistemas de almacenamiento de energía por batería a escala comercial y de red (BESS)</strong> albergan megawatts de potencia bajo tensiones continuas que alcanzan <strong>600V a más de 1000V DC</strong>.</p>
<p>Sin embargo, realizar tareas de mantenimiento en cadenas de baterías DC vivas presenta riesgos mortales de arco eléctrico sostenido, capaz de vaporizar conductores de cobre en fracciones de segundo.</p>
<p>Normas de seguridad como <strong>NFPA 855 y UL 9540</strong> exigen un mecanismo manual, visible y operable sin herramientas para aislar los paquetes de baterías antes de cualquier intervención técnica.</p>
<p>El <strong>Desconectador Manual de Servicio (Serie MSD)</strong> constituye el estándar internacional: un dispositivo con grado de protección IP67 que combina un fusible DC ultrarrápido, un lazo de enclavamiento HVIL y una palanca con retardo mecánico incorporado.</p>

<h2>Elementos de Diseño y Seguridad</h2>
<ol>
  <li><strong>Palanca de Extracción de Dos Etapas:</strong> Impone una pausa física obligatoria entre la apertura de la señal HVIL (Fase 1) y la separación de potencia (Fase 2).</li>
  <li><strong>Fusible Cerámico DC de Gran Poder de Corte:</strong> Protege las celdas ante cortocircuitos masivos con 50kA de poder de ruptura a 1000V DC.</li>
  <li><strong>Pines de Control HVIL Adelantados:</strong> Desconectan la señal de control milisegundos antes para asegurar una desconexión de potencia con corriente cero.</li>
  <li><strong>Bornes de Cobre Plateado con Resortes de Corona:</strong> Mantienen una resistencia de contacto inferior a 0,2 m&Omega; evitando calentamientos bajo 630A continuos.</li>
</ol>
'''
)

MSD_AR = dict(
    lang='ar',
    dir='rtl',
    slug='bess-battery-safety-what-is-a-manual-service-disconnect-ar',
    title='منظومات تخزين طاقة البطاريات (BESS): ما هو قاطع الصيانة اليدوي عالي الجهد (MSD)؟',
    breadcrumb='القضبان المرنة وتخزين الطاقة',
    read='10 دقائق قراءة',
    alt='قاطع صيانة يدوي عالي الجهد للبطاريات (موديل MSD) مع فيوز تيار مستمر مدمج وحلقة HVIL مثبت على حاوية بطاريات BESS',
    desc=('منظومات تخزين الطاقة بالبطاريات (BESS) وحزم بطاريات الجهد العالي: ما هو قاطع الصيانة اليدوي (MSD)؟ '
          'ذراع سحب بمرحلتين ميكانيكيتين، وفيوز تيار مستمر مدمج بجهد 1000V، وحلقة HVIL لإلغاء مخاطر القوس الكهربائي أثناء الصيانة.'),
    model='سلسلة MSD: قواطع الصيانة اليدوية عالية الجهد المدمجة بفيوز DC وحلقة HVIL (جهد حتى 1000V DC، وسعات حتى 630A، بحماية IP67/IP6K9K)',
    category='القضبان المرنة وتخزين الطاقة / قواطع الصيانة اليدوية MSD',
    kw='قاطع صيانة يدوي &middot; مقبس msd &middot; قاطع msd &middot; فيوز بطاريات bess &middot; حلقة hvil msd &middot; فصل بطاريات الجهد العالي',
    specs=[
        ('جهد التشغيل الاسمي ومستوى العزل', 'جهد تشغيل مستمر مقنن حتى 1000V DC / 1500V DC؛ جهد صمود العزل الاختباري &ge; 5000V AC لمدة دقيقة كاملة'),
        ('التيار المستمر وسعة الفيوز المدمج', 'سعات تيار معيارية: 150A، 250A، 350A، 400A، وحتى 630A DC (تستوعب فيوزات سيراميكية فائقة السرعة aR/gR)'),
        ('حلقة القفل الداخلي عالي الجهد (HVIL)', 'دائرة تحكم إشارية مدمجة تفصل ميكانيكياً بفارق 10 إلى 30 مليثانية *قبل* انفصال أقطاب القدرة الرئيسية'),
        ('ذراع السحب الميكانيكي على مرحلتين', 'مقبض سحب يدوي دون أدوات: المرحلة الأولى تقطع مسار HVIL؛ والمرحلة الثانية تحرر وتسحب قابس الفيوز بالكامل'),
        ('درجة الحماية البيئية ومقاومة الماء', 'معتمد بدرجة عزل IP67 و IP6K9K في حالة القفل؛ ومزود بعوازل IP2X تمنع لمس الأجزاء الحية بالأصابع عند الفتح'),
        ('مادة تصنيع الأقطاب وسماكة الفضة', 'نحاس تيلوريوم مطروق عالي النقاوة بنوابض تاجية مرنة وطلاء فضة سميك (&ge; 5 &mu;m) لأدنى مقاومة تلامس (&le; 0.2 m&Omega;)'),
        ('العمر الميكانيكي والتحمل الحراري', 'عمر تشغيلي ميكانيكي &ge; 500 دورة تعشيق وفصل؛ وهيكل خارجي من اللدائن الحرارية المقاومة للهب (UL 94 V-0)'),
        ('مطابقة المواصفات القياسية الدولية', 'معتمد كلياً طبقاً لمواصفات UL 4128 و USCAR-2 و USCAR-37 و IEC 60664-1 و ISO 6469 ومتطلبات نقل البطاريات UN 38.3')
    ],
    faqs=[
        ('ما هو قاطع الصيانة اليدوي (MSD) ولماذا هو إلزامي في بنوك بطاريات BESS والسيارات الكهربائية؟',
         'قاطع الصيانة اليدوي—والمعروف في صناعة تخزين الطاقة باسم MSD (Manual Service Disconnect)—هو '
         'قابس أمان ميكانيكي عالي الجهد مدمج به فيوز تيار مستمر فائق السرعة ومقبض سحب ميكانيكي ذو مرحلتين. '
         'يُثبت القاطع على الواجهة الخارجية لحاويات البطاريات (التي تعمل بجهود من 400V إلى أكثر من 1000V DC) في محطات BESS الكبرى. '
         'يحقق هذا القاطع ثلاث غايات أمان حتمية: '
         '<ul>'
         '<li><strong>1. فصل فيزيائي مرئي للصيانة:</strong> لا يمكن للمهندسين الاعتماد كلياً على القواطع الإلكترونية والبرمجيات التي قد تعلق مغلقة. '
         'إن سحب قاطع MSD يقطع السلسلة المتوالية للبطاريات فيزيائياً إلى نصفين غير ضارين بجهد آمن لحماية الفنيين.</li>'
         '<li><strong>2. حماية فائقة بفيوز DC سيراميكي مدمج:</strong> يحتوي القابس على فيوز سيراميكي (سعة حتى 630A عند 1000V DC وبقدرة قطع 50kA) '
         'يخمد تيارات القصر الهائلة في أجزاء من المليثانية، مانعاً الانفجار الحراري لخلايا الليثيوم.</li>'
         '<li><strong>3. إلغاء خطر القوس الكهربائي (Arc Flash):</strong> لا يمر التيار المستمر بنقطة الصفر، مما يجعل شرارته مستمرة ونارية. '
         'تضمن آلية الذراع المرحلية قطع دائرة HVIL وتفريغ الشحنة بالكامل *قبل* تباعد نقاط التلامس الفيزيائية.</li>'
         '</ul>'),
        ('كيف تلغي آلية السحب ذات المرحلتين وحلقة HVIL خطر تفريغ الشحنة والقوس الكهربائي؟',
         'تتم عملية السحب بتسلسل ميكانيكي هندسي محكم: '
         '<ul>'
         '<li><strong>المرحلة الأولى (قطع مسار HVIL ووقفة إلزامية):</strong> يرفع الفني الذراع بزاوية 45 درجة. '
         'يفصل هذا الحركة دبابيس حلقة HVIL بينما تظل أقطاب القدرة الرئيسية ملامسة تماماً. '
         'يرصد نظام إدارة البطارية (BMS) فتح الدائرة ويأمر القواطع الرئيسية بفصل التيار في أقل من 20 مليثانية. ويصطدم الذراع بحاجز يمنع مواصلة السحب.</li>'
         '<li><strong>المرحلة الثانية (الفصل التام دون تيار):</strong> يضغط الفني على زر الأمان الأحمر لتحرير الحاجز وإتمام سحب المقبس. '
         'تنفصل أقطاب القدرة الرئيسية في دائرة خاملة تماماً ومعدومة التيار (صفر أمبير)، مما يمنع حدوث أي شرارة كهربائية كلياً.</li>'
         '</ul>'),
        ('ما هو الفرق الجوهري بين قاطع الصيانة MSD وموصلات تخزين الطاقة السريعة؟',
         'رغم تواجدهما معاً في محطات BESS، إلا أن لكل منهما وظيفة محددة: '
         '<ul>'
         '<li><strong>قاطع الصيانة اليدوي (MSD):</strong> جهاز أمان وفصل ميكانيكي يحتوي على فيوز DC داخلي، يُثبت على الغلاف لقطع دائرة البطاريات وقت الصيانة.</li>'
         '<li><strong>موصلات تخزين الطاقة السريعة (Connectors):</strong> وصلات كابلات قدرة مرنة تُستخدم لتوصيل أطراف البطارية بقضبان التوزيع، ولا تحتوي على فيوز.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تطوير محطات تخزين الطاقة بالبطاريات (BESS)، أو بطاريات المنظومات الشمسية، أو حزم بطاريات الجهد العالي بجهد 1000V المعتمدة لمعايير UL 4128؟ تصنع يمين (YOMIN) قواطع صيانة يدوية MSD متطورة بأعلى معايير الأمان.',
    body='''
<h2>صمام الأمان الحاسم في رفوف بطاريات تخزين الطاقة عالية الجهد</h2>
<p>تعمل <strong>منظومات تخزين طاقة البطاريات على نطاق الشبكة (BESS)</strong> الحديثة عند جهود مستمرة مرتفعة تتراوح بين <strong>600V و 1000V+ DC</strong>، حيث تُخزن آلاف الميغاوات/ساعة في حاويات معيارية متطورة.</p>
<p>ومع ذلك، فإن صيانة حزم البطاريات الحية في بيئة التيار المستمر تمثل خطراً فادحاً يهدد حياة الفنيين بسبب ظاهرة القوس الكهربائي المستمر (DC Arc Flash) التي تصهر المعادن فورياً لعدم وجود نقطة الصفر الطبيعية.</p>
<p>تفرض معايير السلامة الدولية الحازمة (مثل <strong>NFPA 855 و UL 9540</strong>) تزويد كل سلسلة بطاريات بجهاز فصل يدوي ميكانيكي مرئي وقابل للتشغيل دون أدوات.</p>
<p>يمثل <strong>قاطع الصيانة اليدوي عالي الجهد (سلسلة MSD)</strong> الحل الهندسي القياسي الحاسم: قابس أمان محكم العزل (IP67) يجمع بين فيوز تيار مستمر فائق السرعة، وحلقة أمان ذكية HVIL، وذراع ميكانيكي مانع للشرر الكهربائي.</p>

<h2>المكونات الهندسية وميزات الحماية الفائقة</h2>
<ol>
  <li><strong>مقبض سحب ميكانيكي على مرحلتين:</strong> يفرض فاصلاً زمنياً ميكانيكياً إجبارياً بين قطع إشارة التحكم HVIL (المرحلة 1) وفصل أقطاب القدرة (المرحلة 2).</li>
  <li><strong>فيوز سيراميكي مدمج عالي قدرة القطع:</strong> يقطع تيارات القصر الضخمة (قدرة قطع 50kA عند 1000V DC) لحماية خلايا الليثيوم من الانفجار.</li>
  <li><strong>دبابيس حلقة الأمان الكهربائي HVIL:</strong> تفصل مسبقاً لإصدار أمر فتح القواطع الرئيسية للبطارية قبل انفصال الأقطاب الفيزيائية.</li>
  <li><strong>أقطاب نحاسية مطلية بالفضة بنوابض تاجية:</strong> تحقق مقاومة تلامس ضئيلة (&le; 0.2 m&Omega;) تضمن برودة التوصيل تحت تيار دائم حتى 630 أمبير.</li>
</ol>
'''
)

# ==============================================================================
# 2. J-TYPE FUSE CUTOUT (EN, FR, ES, AR)
# ==============================================================================

JFC_EN = dict(
    lang='en',
    dir='ltr',
    slug='feeder-pillars-what-is-a-j-type-fuse-cutout',
    title='Utility Feeder Pillars & Substation Protection: What Is a J-Type Fuse Cutout?',
    breadcrumb='Fuses &amp; Protection',
    read='10 min read',
    alt='Bank of heavy-duty three-phase J-Type Fuse Cutouts (Model J-Type 300A/400A) installed inside an outdoor utility distribution feeder pillar cabinet',
    desc=('Municipal power distribution, feeder pillars, and transformer low-voltage protection: What is a J-type fuse cutout? '
          'How wedge-tightened fuse carriers, BS 88 slotted-tag fuse links, DMC polyester bases, and 80kA breaking capacity protect urban utility networks.'),
    model='Model J-Type 300A / 400A Heavy-Duty Distribution Fuse Cutout Base & Wedge Carrier (BS 88 / BS 1361, 82mm / 92mm Centers, 80kA)',
    category='Fuses & Protection / J-Type Fuse Cutouts',
    kw='what is a j type fuse cutout &middot; j type fuse cutout &middot; j-type fuse cut out &middot; feeder pillar fuse &middot; wedge type fuse carrier &middot; bs88 j type fuse',
    specs=[
        ('Rated Operational Voltage & Frequency', 'Rated operational voltage: 415V / 500V AC at 50/60 Hz; rated insulation voltage: 690V / 1000V AC'),
        ('Continuous Current Carrying Ratings', 'Available in heavy-duty ratings: 315A, 400A, and up to 630A continuous current capacity'),
        ('Short-Circuit Breaking Capacity (Icu)', 'Certified high breaking capacity (HBC) up to 80kA symmetrical RMS fault current at 415V AC'),
        ('Fuse Link Mounting Fixing Centers', 'Standardized slotted-tag fixing centers: 82mm (standard distribution) and 92mm (heavy industrial / network)'),
        ('Base Molding Material & Flame Rating', 'High-strength, non-tracking Dough Molding Compound (DMC) glass-reinforced thermoset polyester (UL 94 V-0, heat-resistant)'),
        ('Wedge Tightening Clamping Mechanism', 'Insulated thumb-screw or bolted high-tensile brass wedge block clamping slotted fuse tags directly against silver-plated copper busbar pads'),
        ('Incoming & Outgoing Terminal Types', 'Direct mechanical shear-bolt cable lugs or compression lugs accommodating underground cables from 70 mm&sup2; up to 300 mm&sup2;'),
        ('Applicable International Utility Standards', 'Fully compliant with BS 88-1, BS 88-5, BS 1361, IEC 60269-1, IEC 60269-2, and major utility specifications (SEC, DEWA, UK DNOs)')
    ],
    faqs=[
        ('What is a J-Type Fuse Cutout and where is it used in utility power distribution networks?',
         'A J-Type Fuse Cutout—commonly termed a feeder pillar fuse cutout, wedge-type cutout, or BS 88 distribution fuse base—is '
         'a heavy-duty electrical distribution protective assembly comprising an insulating glass-reinforced polyester base and a wedge-tightened fuse carrier. '
         'It is specifically engineered to hold high-breaking-capacity slotted-tag fuse links (BS 88 Part 5). '
         'J-Type cutouts are the standard low-voltage overcurrent protection equipment across municipal and utility networks for three primary applications: '
         '<ul>'
         '<li><strong>1. Outdoor Distribution Feeder Pillars:</strong> Mounted vertically along copper busbars inside street-level feeder pillars '
         'to protect individual underground municipal distributor cables branching out to residential neighborhoods and commercial buildings.</li>'
         '<li><strong>2. Pole-Mounted Distribution Transformer Cutouts:</strong> Installed at overhead-to-underground transition poles (terminal poles) '
         'to protect low-voltage cables dropping down from overhead distribution transformers.</li>'
         '<li><strong>3. Substation LV Switchboards:</strong> Serving as incoming and outgoing circuit protection links in compact urban package substations.</li>'
         '</ul>'),
        ('Why do distribution network utilities insist on Wedge-Type J Cutouts instead of standard DIN knife-blade fuses?',
         'While DIN knife-blade fuses (NH type) rely on spring-tensioned copper clips, heavy municipal distribution utilities '
         '(across the UK, Middle East, and Commonwealth) mandate bolted or thumb-screw wedge-type J cutouts for critical technical reasons: '
         '<ul>'
         '<li><strong>1. Permanent High Contact Pressure:</strong> Knife-blade clips lose spring tension over years of thermal cycling, causing high contact resistance '
         'and catastrophic overheating. The wedge mechanism on a J-type cutout uses an insulated thumb-screw to wedge the slotted fuse tag directly against solid silver-plated copper pads, '
         'guaranteeing hundreds of kilograms of constant clamping force that cannot loosen with age.</li>'
         '<li><strong>2. Elimination of Insertion Arc Flash:</strong> When replacing a fuse in a live feeder pillar, inserting a DIN knife blade under load '
         'can cause dangerous arcing. The wedge carrier on a J-type cutout allows the technician to insert the fuse smoothly without contact, and then clamp the wedge tight using the insulated knob, '
         'preventing arc flashes and ensuring lineman safety.</li>'
         '<li><strong>3. Unmatched Short-Circuit Withstand (80kA):</strong> Under severe underground cable faults, massive electromagnetic forces attempt to blow fuse blades out of their jaws. '
         'The mechanical wedge physically locks the fuse tags in place, easily containing symmetrical short circuits up to 80,000 amperes.</li>'
         '</ul>'),
        ('What is the difference between 82mm and 92mm fixing centers in J-type fuse links?',
         'The dimension refers to the center-to-center distance between the two slotted mounting tags of the cylindrical ceramic fuse link: '
         '<ul>'
         '<li><strong>82mm Fixing Center:</strong> The most widely deployed utility standard across the Middle East (Saudi Electricity Company, DEWA) and the UK. '
         'Typically utilized for fuse ratings from 20A up to 400A in standard municipal feeder pillars and transformer service cutouts.</li>'
         '<li><strong>92mm Fixing Center:</strong> Utilized primarily for heavy industrial distribution feeders and higher current ratings (up to 630A). '
         'YOMIN J-type cutout bases are engineered with dual-position terminal studs or dedicated base models to accommodate both 82mm and 92mm utility standards.</li>'
         '</ul>')
    ],
    cta='Procuring utility-grade low-voltage distribution equipment, feeder pillar fuse bases, or heavy-duty J-type wedge fuse cutouts compliant with BS 88 and IEC 60269? YOMIN manufactures high-breaking-capacity distribution fuse gear.',
    body='''
<h2>The Robust Vanguard of Urban Low-Voltage Power Distribution</h2>
<p>In municipal electrical distribution grids across the Middle East, the United Kingdom, and Commonwealth markets, electrical energy travels from primary distribution substations through underground cables into outdoor street-level <strong>distribution feeder pillars</strong> and compact kiosk substations.</p>
<p>These feeder pillars distribute low-voltage electrical power (415V/500V AC) to residential blocks, street lighting networks, and commercial complexes. Under continuous tropical ambient heat, desert dust storms, and heavy cyclic electrical loads, low-voltage distribution gear must operate reliably for 30 to 40 years without failure.</p>
<p>If an underground municipal cable is damaged by excavation or cable degradation, prospective fault currents can exceed <strong>50,000 to 80,000 amperes</strong>. Standard commercial circuit breakers or spring-clip fuses cannot withstand these extreme mechanical forces and thermal stresses.</p>
<p>The <strong>J-Type Fuse Cutout (Model J-Type 300A/400A Series)</strong> represents the field-proven utility standard: a rugged, non-tracking glass-reinforced polyester base housing a heavy wedge-tightened fuse carrier that securely locks BS 88 slotted fuse links under massive contact pressure.</p>

<h2>Engineering Anatomy: Inside a Utility-Grade J-Type Wedge Fuse Cutout</h2>
<ol>
  <li><strong>DMC Glass-Reinforced Thermoset Polyester Base:</strong> Molded from heavy-duty Dough Molding Compound (DMC) with high dielectric strength and superior resistance to electrical tracking under humid or polluted environments.</li>
  <li><strong>Thumb-Screw Wedge Tightening Carrier:</strong> Features an insulated, flame-retardant thermoplastic knob that tightens an internal brass wedge, clamping the slotted fuse tags directly against the silver-plated copper busbar terminal pads.</li>
  <li><strong>Solid Silver-Plated Copper Busbar Terminals:</strong> High-conductivity electrolytic copper contact jaws plated with &ge; 5 &mu;m silver, delivering minimal contact resistance and zero thermal runaway under 400A continuous load.</li>
  <li><strong>Standardized 82mm / 92mm Slotted Fixing Geometry:</strong> Compatible with all standard utility-approved BS 88 Part 5 high-breaking-capacity (80kA) fuse links.</li>
  <li><strong>Direct Mechanical Cable Clamping:</strong> Heavy-duty mechanical shear-bolt or compression lugs accommodate large municipal aluminium and copper underground cables from 70 mm&sup2; up to 300 mm&sup2;.</li>
</ol>

<h2>Comparison: J-Type Wedge Fuse Cutout vs. DIN NH Blade Fuse Base vs. Molded Case Circuit Breaker (MCCB)</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>DIN NH Blade Fuse Base</th>
      <th>YOMIN J-Type Wedge Fuse Cutout (BS 88)</th>
      <th>Molded Case Circuit Breaker (MCCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Contact Clamping Mechanism</strong></td>
      <td>Spring-tensioned clips (susceptible to fatigue and loosening).</td>
      <td><strong>Insulated mechanical screw wedge (permanent high-pressure clamp).</strong></td>
      <td>Internal spring-loaded breaker contact fingers.</td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Breaking Capacity (Icu)</strong></td>
      <td>Typically 50kA–100kA.</td>
      <td><strong>High Certified Breaking Capacity: 80kA symmetrical RMS at 415V AC.</strong></td>
      <td>Typically 25kA–50kA in compact frame sizes.</td>
    </tr>
    <tr>
      <td><strong>Environmental Resilience in Feeder Pillars</strong></td>
      <td>Moderate: Open clips collect dust, sand, and moisture.</td>
      <td><strong>Superior: DMC thermoset base immune to tracking; wedge cuts through oxide film.</strong></td>
      <td>Sensitive to desert heat, sand ingress, and internal mechanism jamming.</td>
    </tr>
    <tr>
      <td><strong>Insertion &amp; Removal Safety Under Load</strong></td>
      <td>Requires external glove handle; danger of clip arcing.</td>
      <td><strong>Built-in insulated knob allows safe insertion and positive wedge locking.</strong></td>
      <td>Toggle switch operation (electronic trip unit requires auxiliary power).</td>
    </tr>
    <tr>
      <td><strong>Utility Network Track Record</strong></td>
      <td>Predominant in Continental Europe.</td>
      <td><strong>Mandatory specification across Middle East (SEC, DEWA) &amp; British Commonwealth.</strong></td>
      <td>Common in private buildings; less common in municipal distributor cables.</td>
    </tr>
  </tbody>
</table>
'''
)

JFC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='feeder-pillars-what-is-a-j-type-fuse-cutout-fr',
    title="Armoires de Distribution Publique & Postes : Qu'est-ce qu'un Coupe-Circuit Fusible Type J ?",
    breadcrumb='Fusibles &amp; Protection',
    read='10 min de lecture',
    alt='Ensemble de coupe-circuits fusibles industriels type J (Modèle J-Type 300A/400A) montés dans une armoire de distribution publique',
    desc=('Distribution électrique publique, armoires de coupure urbaines et protection des postes de transformation : Qu\'est-ce qu\'un coupe-circuit type J ? '
          'Porte-fusible à serrage par coin (wedge), cartouches à pattes fendues BS 88, socle en polyester armé DMC et pouvoir de coupure de 80kA.'),
    model='Série J-Type 300A / 400A : Socles et Porte-Fusibles de Distribution à Serrage par Coin (BS 88 / BS 1361, Entraxe 82mm / 92mm, 80kA)',
    category='Fusibles & Protection / Coupe-Circuits Type J',
    kw='coupe-circuit type j &middot; fusible type j &middot; socle fusible wedge &middot; armoire de distribution feeder pillar &middot; fusible bs88 &middot; coupe-circuit réseau',
    specs=[
        ('Tension Assignée d\'Emploi et Fréquence', 'Tension assignée d\'emploi : 415V / 500V AC à 50/60 Hz ; tension d\'isolement : 690V / 1000V AC'),
        ('Courant Permanent Admissible du Socle', 'Disponible en calibres industriels lourds : 315A, 400A et jusqu\'à 630A en service continu'),
        ('Pouvoir de Coupure en Court-Circuit (Icu)', 'Pouvoir de coupure élevé certifié (HBC) jusqu\'à 80kA sous 415V AC en courant alternatif symétrique'),
        ('Entraxe de Fixation des Cartouches à Pattes', 'Entraxes normalisés pour cartouches à pattes fendues : 82mm (standard réseau) et 92mm (forte puissance)'),
        ('Matériau du Socle et Résistance Électrique', 'Polyester thermodurcissable armé de fibres de verre (DMC) autoextinguible (UL 94 V-0) haute résistance au cheminement'),
        ('Mécanisme de Serrage par Coin (Wedge)', 'Molette isolante manœuvrant un coin en laiton massif qui plaque fermement les pattes du fusible contre les barres de cuivre'),
        ('Raccordement des Câbles Souterrains', 'Bornes à serrage mécanique à vis fusibles ou bornes pour cosses à sertir de 70 mm&sup2; jusqu\'à 300 mm&sup2;'),
        ('Conformité aux Normes Internationales', 'Parfaitement conforme aux normes BS 88-1, BS 88-5, BS 1361, CEI 60269-1, CEI 60269-2 et cahiers des charges de distribution publique')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Coupe-Circuit Fusible Type J et où est-il déployé sur les réseaux électriques ?',
         'Un Coupe-Circuit Fusible Type J—souvent désigné sous le terme de coupe-circuit pour armoire urbaine (feeder pillar) ou socle à coin (wedge type)—est '
         'un ensemble électromécanique de protection basse tension comprenant un socle en polyester renforcé et un porte-fusible à serrage par coin. '
         'Il est spécialement conçu pour accueillir les cartouches fusibles industrielles à pattes fendues selon la norme britannique BS 88 Part 5. '
         'On le retrouve principalement dans trois applications de distribution publique : '
         '<ul>'
         '<li><strong>1. Armoires de Distribution Publique (Feeder Pillars) :</strong> Monté sur les jeux de barres verticaux des armoires urbaines '
         'pour protéger les câbles souterrains alimentant les quartiers résidentiels et zones d\'activités.</li>'
         '<li><strong>2. Coffrets de Pied de Poteau pour Transformateurs :</strong> Installé au bas des poteaux de transition aéro-souterraine '
         'pour protéger la descente BT des transformateurs aériens.</li>'
         '<li><strong>3. Tableaux Basse Tension des Postes de Transformation :</strong> Utilisé comme organe de départ dans les postes urbains compacts.</li>'
         '</ul>'),
        ('Pourquoi les distributeurs d\'énergie exigent-ils le serrage par coin (Wedge) au lieu des fusibles à couteaux DIN ?',
         'Sur les réseaux de distribution publique lourds, les distributeurs imposent le coupe-circuit type J pour trois raisons techniques majeures : '
         '<ul>'
         '<li><strong>1. Pression de Contact Permanente et Indévissable :</strong> Les pinces des fusibles à couteaux DIN perdent leur élasticité avec les années '
         'et les cycles thermiques, provoquant des échauffements destructeurs. Le système à coin du type J utilise une vis isolante qui plaque la patte du fusible '
         'avec une force mécanique colossale sur le cuivre massif argenté, garantissant une résistance de contact nulle pendant 40 ans.</li>'
         '<li><strong>2. Sécurité Totale à l\'Insertion :</strong> La mise en place d\'un fusible à couteaux sous charge peut provoquer un arc violent. '
         'Le porte-fusible type J permet d\'engager la cartouche sans effort mécanique, puis de bloquer le coin grâce à la molette isolée en toute sécurité.</li>'
         '<li><strong>3. Tenue Exceptionnelle aux Courts-Circuits (80kA) :</strong> Sous un défaut souterrain violent, les forces électrodynamiques '
         'ont tendance à éjecter les fusibles à couteaux. Le coin mécanique verrouille physiquement la cartouche, contenant sans faillir 80 000 ampères.</li>'
         '</ul>'),
        ('Quelle est la différence entre les entraxes de 82mm et 92mm ?',
         'Cette dimension désigne la distance entre les centres des deux fentes de fixation de la cartouche céramique : '
         '<ul>'
         '<li><strong>Entraxe 82mm :</strong> C\'est le standard le plus répandu au Moyen-Orient et au Royaume-Uni pour les calibres de 20A à 400A.</li>'
         '<li><strong>Entraxe 92mm :</strong> Utilisé pour les départs industriels de très forte intensité atteignant 630A. '
         'Les socles YOMIN sont étudiés pour s\'adapter avec précision à ces deux géométries réglementaires.</li>'
         '</ul>')
    ],
    cta='Vous fabriquez des armoires de distribution publique (feeder pillars), des postes de transformation urbains ou recherchez des coupe-circuits fusibles type J conformes BS 88 ? YOMIN produit des équipements de protection basse tension haute performance.',
    body='''
<h2>Le Rempart Indispensable des Réseaux de Distribution Publique Basse Tension</h2>
<p>Sur les réseaux de distribution d\'électricité municipaux au Moyen-Orient et dans les pays du Commonwealth, l\'énergie issue des postes de transformation chemine par câbles souterrains vers des <strong>armoires de coupure urbaines (Feeder Pillars)</strong> installées sur la voie publique.</p>
<p>Ces armoires alimentent en basse tension (415V/500V) des quartiers entiers, des réseaux d\'éclairage public et des complexes tertiaires. Face aux chaleurs extrêmes, à la poussière et aux surcharges cycliques, ce matériel doit fonctionner sans faille pendant plusieurs décennies.</p>
<p>En cas de court-circuit sur un câble souterrain, les courants de défaut peuvent dépasser <strong>50 000 à 80 000 ampères</strong>. Les disjoncteurs ordinaires ou les pinces à ressorts simples ne peuvent contenir de telles contraintes mécaniques.</p>
<p>Le <strong>Coupe-Circuit Fusible Type J (Série J-Type 300A/400A)</strong> constitue la référence éprouvée : un socle robuste en polyester thermodurcissable armé de fibres de verre (DMC) associé à un chariot de serrage par coin qui verrouille les cartouches BS 88 sous une pression mécanique inégalée.</p>

<h2>Conception et Éléments de Robustesse</h2>
<ol>
  <li><strong>Socle Moulé en Polyester Armé DMC :</strong> Offre une rigidité diélectrique maximale et une immunité totale contre le cheminement électrique sous atmosphère humide et polluée.</li>
  <li><strong>Porte-Fusible à Molette de Serrage par Coin :</strong> Permet de plaquer mécaniquement les pattes fendues du fusible contre les barres de cuivre massif argenté.</li>
  <li><strong>Plages de Raccordement en Cuivre Pur Électrolytique Argenté :</strong> Éliminent tout échauffement sous un régime permanent sévère de 400A continu.</li>
  <li><strong>Pouvoir de Coupure Certifié 80kA :</strong> Garantit une interruption sûre et instantanée des courts-circuits les plus dévastateurs selon la norme BS 88.</li>
</ol>
'''
)

JFC_ES = dict(
    lang='es',
    dir='ltr',
    slug='feeder-pillars-what-is-a-j-type-fuse-cutout-es',
    title='Cajas de Distribución Urbana y Subestaciones: ¿Qué es un Cortacircuito Fusible Tipo J?',
    breadcrumb='Fusibles y Protección',
    read='10 min de lectura',
    alt='Conjunto de cortacircuitos fusibles de distribución tipo J (Modelo J-Type 300A/400A) montados en armario de distribución urbana feeder pillar',
    desc=('Distribución eléctrica urbana, armarios feeder pillars y protección de subestaciones: ¿Qué es un cortacircuito fusible tipo J? '
          'Portafusibles con apriete por cuña (wedge), fusibles de ranura BS 88, base de poliéster reforzado DMC y poder de corte de 80kA.'),
    model='Serie J-Type 300A / 400A: Bases y Portafusibles de Distribución con Apriete por Cuña (BS 88 / BS 1361, Distancia entre Centros 82mm / 92mm, 80kA)',
    category='Fusibles y Protección / Cortacircuitos Tipo J',
    kw='cortacircuito tipo j &middot; fusible tipo j &middot; base fusible wedge &middot; armario feeder pillar &middot; fusible bs88 &middot; fusible distribucion urbana',
    specs=[
        ('Tensión Nominal de Servicio y Frecuencia', 'Tensión nominal de servicio: 415V / 500V AC a 50/60 Hz; tensión de aislamiento: 690V / 1000V AC'),
        ('Capacidad de Corriente Continua Admisible', 'Disponible en calibres de servicio pesado: 315A, 400A y hasta 630A en régimen continuo'),
        ('Poder de Corte ante Cortocircuito (Icu)', 'Alto poder de corte certificado (HBC) de hasta 80kA simétricos a 415V AC'),
        ('Distancia entre Centros de Fijación', 'Distancia normalizada para fusibles con orejetas ranuradas: 82mm (estándar de distribución) y 92mm (servicio pesado)'),
        ('Material de la Base y Resistencia Térmica', 'Poliéster termoendurecible reforzado con fibra de vidrio (DMC) autoextinguible (UL 94 V-0) de alta resistencia al arco'),
        ('Mecanismo de Apriete por Cuña (Wedge)', 'Perilla aislante que acciona una cuña de latón macizo para apretar las orejetas del fusible directamente sobre las barras de cobre'),
        ('Terminales de Conexión de Cables', 'Terminales mecánicos de perno fusible o terminales de compresión aptos para cables subterráneos de 70 mm&sup2; a 300 mm&sup2;'),
        ('Normativas Internacionales Aplicables', 'Totalmente conforme con normas BS 88-1, BS 88-5, BS 1361, IEC 60269-1, IEC 60269-2 y pliegos de compañías eléctricas')
    ],
    faqs=[
        ('¿Qué es un Cortacircuito Fusible Tipo J y en qué aplicaciones de la red de distribución se instala?',
         'Un Cortacircuito Fusible Tipo J—conocido internacionalmente como cortacircuito para feeder pillar o base fusible de cuña (wedge-type)—es '
         'un equipo electromecánico de protección en baja tensión compuesto por una base de poliéster reforzado y un portafusible de ajuste por cuña. '
         'Está diseñado exclusivamente para alojar fusibles cilíndricos con orejetas ranuradas según norma británica BS 88 Part 5. '
         'Se utiliza en tres aplicaciones fundamentales de las compañías eléctricas: '
         '<ul>'
         '<li><strong>1. Armarios de Distribución Urbana (Feeder Pillars):</strong> Montado sobre barras colectoras verticales en cajas de intemperie '
         'para proteger cables subterráneos que alimentan manzanas residenciales o centros comerciales.</li>'
         '<li><strong>2. Puntos de Transformación en Poste:</strong> Instalado al pie de postes de transición aéreo-subterránea para proteger la salida '
         'en baja tensión de transformadores de distribución.</li>'
         '<li><strong>3. Cuadros de Salida en Subestaciones:</strong> Como elemento de seccionamiento y protección en centros de transformación compactos.</li>'
         '</ul>'),
        ('¿Por qué las compañías eléctricas prefieren el sistema de Cuña (Wedge) en lugar de fusibles de cuchilla tipo DIN?',
         'Las distribuidoras eléctricas exigen el sistema tipo J por tres razones de ingeniería insustituibles: '
         '<ul>'
         '<li><strong>1. Presión de Contacto Constante e Inalterable:</strong> Las pinzas de los fusibles de cuchilla tipo DIN pierden elasticidad con el calor '
         'y los años, generando falsos contactos y sobrecalentamientos destructivos. El apriete por cuña del tipo J utiliza un tornillo con perilla aislante '
         'que presiona mecánicamente la orejeta con cientos de kilos de fuerza sobre el cobre plateado macizo, eliminando la resistencia de contacto por décadas.</li>'
         '<li><strong>2. Seguridad al Insertar bajo Tensión:</strong> Insertar una cuchilla DIN bajo carga puede provocar arcos peligrosos. '
         'El portafusible tipo J permite introducir el fusible sin fricción y luego apretar la cuña con total aislamiento y seguridad para el liniero.</li>'
         '<li><strong>3. Inmunidad ante Fuerzas de Cortocircuito (80kA):</strong> Durante una falla masiva en un cable subterráneo, las fuerzas electrodinámicas '
         'tienden a expulsar las cuchillas DIN de sus zapatas. La cuña mecánica bloquea físicamente el fusible impidiendo su expulsión.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre los centros de fijación de 82mm y 92mm?',
         'La medida se refiere a la separación exacta entre las ranuras de montaje de la cartucho cerámico: '
         '<ul>'
         '<li><strong>82mm:</strong> El estándar mayoritario en empresas de distribución pública (como Saudi Electricity Company, DEWA y Reino Unido) para calibres de 20A a 400A.</li>'
         '<li><strong>92mm:</strong> Destinado a alimentadores industriales de alta corriente (hasta 630A). '
         'Las bases YOMIN cuentan con opciones para acoplar con precisión ambas distancias reglamentarias.</li>'
         '</ul>')
    ],
    cta='¿Fabrica armarios de distribución urbana (feeder pillars), centros de transformación o requiere cortacircuitos fusibles tipo J bajo norma BS 88? YOMIN fabrica equipos de corte y protección para distribución pública de alta resistencia.',
    body='''
<h2>La Máxima Protección para Redes de Distribución Eléctrica Urbana</h2>
<p>En redes de distribución eléctrica de baja tensión en Oriente Medio y países de normativa británica, la energía se distribuye desde subestaciones a través de cables subterráneos hacia <strong>armarios de distribución a nivel de acera (Feeder Pillars)</strong>.</p>
<p>Estos armarios abastecen de energía a barrios enteros y alumbrado público. Sometidos al calor solar extremo del desierto, polución y sobrecargas cíclicas, los equipos de seccionamiento deben operar durante décadas sin mantenimiento.</p>
<p>Ante una falla subterránea, las corrientes de cortocircuito pueden alcanzar entre <strong>50.000 y 80.000 amperios</strong>, requiriendo componentes robustos que no se destruyan mecánicamente.</p>
<p>El <strong>Cortacircuito Fusible Tipo J (Serie J-Type 300A/400A)</strong> es la solución consolidada en el sector utility: una base robusta de poliéster termoendurecido (DMC) y un portafusibles de apriete por cuña mecánica que inmoviliza los fusibles BS 88 bajo una presión de contacto imbatible.</p>

<h2>Elementos de Diseño y Calidad Constructiva</h2>
<ol>
  <li><strong>Base de Poliéster Reforzado DMC:</strong> Brinda máxima resistencia mecánica y rigidez dieléctrica inmune a corrientes de fuga en climas húmedos o polvorientos.</li>
  <li><strong>Portafusibles con Perilla de Bloqueo por Cuña:</strong> Prensa sólidamente las orejetas ranuradas contra los bornes de cobre electrolítico plateado.</li>
  <li><strong>Bornes de Cobre Macizo con Baño de Plata:</strong> Garantizan resistencia eléctrica nula y evitan el calentamiento bajo 400A continuos.</li>
  <li><strong>Poder de Corte Certificado de 80kA a 415V AC:</strong> Asegura la extinción limpia e instantánea de las fallas más violentas según norma BS 88.</li>
</ol>
'''
)

JFC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='feeder-pillars-what-is-a-j-type-fuse-cutout-ar',
    title='لوحات توزيع الأعمدة والمحطات الفرعية: ما هي قاعدة وفيوز التوزيع من النوع J (J-Type Cutout)؟',
    breadcrumb='الفيوزات والقواطع الحامية',
    read='10 دقائق قراءة',
    alt='مجموعة قواعد وفيوزات التوزيع من النوع J (موديل J-Type 300A/400A) مثبتة داخل كابينة توزيع خارجية (Feeder Pillar)',
    desc=('شبكات توزيع الكهرباء البلدية، وكبائن التغذية الخارجية (Feeder Pillars)، وحماية المحطات الفرعية: ما هي قاعدة وفيوز النوع J؟ '
          'حوامل الفيوزات ذات الربط بالخابور الإسفيني (Wedge)، وفيوزات BS 88 المشقوقة، وقواعد البوليستر المقوى DMC وسعة قطع 80kA.'),
    model='سلسلة J-Type 300A / 400A: قواعد وحوامل فيوزات شبكات التوزيع بنظام الخابور الإسفيني (BS 88 / BS 1361، أبعاد 82 مم / 92 مم، 80kA)',
    category='الفيوزات والحماية / قواعد وفيوزات النوع J (J-Type Cutouts)',
    kw='فيوز نوع j &middot; قاعدة فيوز j &middot; j type fuse cutout &middot; كابينة feeder pillar &middot; فيوز bs88 &middot; فيوز خابور اسفيني wedge',
    specs=[
        ('جهد التشغيل المقنن والتردد المعتمد', 'جهد تشغيل اسمي: 415V / 500V AC بتردد 50/60 هرتز؛ جهد العزل المقنن: 690V / 1000V AC'),
        ('سعات التيار المستمر الاسمية للقاعدة', 'متوفر بسعات الخدمة الشاقة لشبكات التوزيع: 315A، 400A، وحتى 630A تيار تشغيلي مستمر'),
        ('سعة قطع تيار القصر المعتمدة (Icu)', 'سعة قطع فائقة (HBC) معتمدة تصل إلى 80kA تيار قصر متماثل عند جهد 415V AC'),
        ('المسافة بين مراكز فتحات تثبيت الفيوز', 'أبعاد المسافات بين فتحات تثبيت زعانف الفيوز المشقوقة: 82 مم (قياسي للبلديات) و 92 مم (للصناعات الثقيلة)'),
        ('مادة تصنيع القاعدة ومقاومة الشرر', 'مركب بوليستر مقوى بالألياف الزجاجية المصبوب حرارياً (DMC) غير قابل للتتبع الكهربائي ومقاوم للهب (UL 94 V-0)'),
        ('آلية التثبيت بالخابور الإسفيني (Wedge)', 'مقبض لولبي معزول يحرك خابوراً نحاسياً مائلاً ليضغط زعانف الفيوز بقوة ميكانيكية هائلة على قضبان النحاس الفضية'),
        ('مخارج توصيل الكابلات الأرضية الرئيسية', 'مرابط ميكانيكية بمسامير قابلة للقص أو مرابط ضغط تستوعب كابلات شبكات التوزيع من 70 مم&sup2; حتى 300 مم&sup2;'),
        ('المواصفات القياسية واعتمادات شركات الكهرباء', 'مطابق كلياً لمواصفات BS 88-1 و BS 88-5 و BS 1361 و IEC 60269 واعتمادات شركات الكهرباء الكبرى (SEC، DEWA)')
    ],
    faqs=[
        ('ما هي قاعدة وفيوز التوزيع من النوع J (J-Type Fuse Cutout) وأين تُستخدم في شبكات الكهرباء؟',
         'قاعدة وفيوز التوزيع من النوع J—والمعروفة في مشاريع الكهرباء باسم فيوز كبائن التغذية (Feeder Pillar Cutout) أو قاعدة الفيوز الإسفينية (Wedge Cutout)—هي '
         'منظومة حماية كهروميكانيكية متينة لشبكات الجهد المنخفض تتألف من قاعدة عازلة من البوليستر المقوى وحامل فيوز مزود بمقبض خابور إسفيني. '
         'صُممت خصيصاً لاحتضان فيوزات السيراميك ذات الزعانف المشقوقة طبقاً للمواصفة البريطانية BS 88 Part 5. '
         'تُعد هذه القواعد العمود الفقري لحماية شبكات التوزيع في ثلاثة مواقع رئيسية: '
         '<ul>'
         '<li><strong>1. كبائن التوزيع الخارجية في الشوارع (Feeder Pillars):</strong> تُثبت عمودياً على قضبان النحاس داخل الكبائن الحديدية في الطرقات '
         'لحماية الكابلات الأرضية المغذية للأحياء السكنية والمراكز التجارية.</li>'
         '<li><strong>2. صناديق التوزيع عند أسفل أعمدة المحولات:</strong> تُركب لحماية الكابلات الهابطة من محولات التوزيع الهوائية إلى الشبكة الأرضية.</li>'
         '<li><strong>3. لوحات التوزيع الرئيسية في محطات التحويل الفرعية:</strong> كعنصر حماية رئيسي لخطوط التغذية الخارجة من المحطة.</li>'
         '</ul>'),
        ('لماذا تصر شركات الكهرباء وهيئات التوزيع على نظام الخابور (Wedge) بدلاً من فيوزات السكاكين العادية (DIN)؟',
         'تفرض شركات الكهرباء (في الشرق الأوسط كالسعودية والإمارات وبريطانيا) قواعد النوع J لأسباب فنية قاطعة: '
         '<ul>'
         '<li><strong>1. ضغط تلامس دائم لا يرتخي بالحرارة:</strong> ترتخي ملاقط فيوزات السكاكين العادية مع السنين وتقلب الفصول مسببة سخونة واحتراقاً كارثياً. '
         'بينما يعتمد نظام النوع J على خابور نحاسي يُحكم بمقبض لولبي يضغط زعنفة الفيوز بمئات الكيلوغرامات على النحاس المطلي بالفضة، مانعاً أي مقاومة تلامس لـ 40 عاماً.</li>'
         '<li><strong>2. الأمان التام عند التركيب تحت الجهد:</strong> إن دفع سكين فيوز عادي تحت الحمل قد يولد قوساً كهربائياً خطيراً في وجه الفني. '
         'أما حامل النوع J فيدخل بحرية تامة دون احتكاك، ثم يُربط الخابور بإحكام عبر المقبض المعزول بأمان مطلق.</li>'
         '<li><strong>3. صمود أسطوري أمام تيارات القصر (80kA):</strong> عند حدوث قصر أرضي عنيف، تدفع القوى الكهروديناميكية الفيوزات العادية للخروج من مكانها. '
         'أما الخابور الميكانيكي فيقفل الفيوز في مكانه بقوة، متحكماً بأعتى تيارات القصر حتى 80,000 أمبير دون أي تزحزح.</li>'
         '</ul>'),
        ('ما هو الفرق بين أبعاد التثبيت 82 مم و 92 مم في فيوزات النوع J؟',
         'يشير هذا البعد إلى المسافة المقاسة بين منتصفي فتحتي التثبيت في زعانف الفيوز السيراميكي: '
         '<ul>'
         '<li><strong>مسافة 82 مم:</strong> المعيار الأكثر انتشاراً لدى شركات الكهرباء (مثل الشركة السعودية للكهرباء SEC وهيئة كهرباء ومياه دبي DEWA) للسعات من 20A حتى 400A.</li>'
         '<li><strong>مسافة 92 مم:</strong> مخصصة لخطوط التغذية الصناعية الثقيلة ذات التيارات المرتفعة التي تصل إلى 630A. '
         'تصمم يمين (YOMIN) قواعد فيوزات J لتلائم كلا البعدين المعتمدين بدقة متناهية.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع كبائن التغذية الخارجية (Feeder Pillars)، أو محطات المحولات الفرعية، أو توريد قواعد وفيوزات التوزيع من النوع J المعتمدة لمواصفات BS 88؟ تصنع يمين (YOMIN) معدات وقواعد فيوزات توزيع الجهد المنخفض عالية الجودة والتحمل.',
    body='''
<h2>صمام الأمان القوي لشبكات توزيع الكهرباء الأرضية في المدن</h2>
<p>في شبكات توزيع الكهرباء البلدية في الشرق الأوسط والدول المعتمدة للمواصفات البريطانية، تخرج الطاقة من محطات التحويل الرئيسية عبر كابلات أرضية ضخمة تصب في <strong>كبائن التغذية الميدانية في الشوارع (Feeder Pillars)</strong>.</p>
<p>تقوم هذه الكبائن بتوزيع الكهرباء منخفضة الجهد (415V/500V AC) على المباني وإنارة الطرقات. وتحت حرارة الصيف الشديدة والعواصف الترابية والأحمال المتزايدة، يجب أن تصمد هذه المعدات لعشرات السنين دون أي انقطاع.</p>
<p>وفي حال تعرض كابل أرضي للتلف أو الحفر الخاطئ، يمكن أن يقفز تيار العطل والقصر إلى ما بين <strong>50,000 و 80,000 أمبير</strong>. وهنا تعجز القواطع العادية وملاقط الفيوزات الضعيفة عن الصمود ميكانيكياً وحرارياً.</p>
<p>تمثل <strong>قواعد وفيوزات التوزيع من النوع J (سلسلة J-Type 300A/400A)</strong> المعيار الهندسي الأبرز والأكثر موثوقية: قاعدة عازلة فائقة المتانة من البوليستر المقوى DMC مع حامل فيوز ذي خابور ميكانيكي إسفيني يغلق الفيوز تحت ضغط تلامس استثنائي.</p>

<h2>المكونات الهندسية وميزات المتانة لشبكات البلديات</h2>
<ol>
  <li><strong>قاعدة مصبوبة من البوليستر المقوى بالألياف الزجاجية (DMC):</strong> تمنع كلياً ظاهرة التتبع والانهيار الكهربائي وتتحمل أقصى درجات الحرارة والرطوبة والملوحة.</li>
  <li><strong>حامل فيوز بمقبض خابور إسفيني لولبي:</strong> يضغط زعانف الفيوز المشقوقة مباشرة وبقوة هائلة على ألواح النحاس الإلكتروليتي المطلي بالفضة.</li>
  <li><strong>أطراف نحاسية صلبة مطلية بالفضة (&ge; 5 &mu;m):</strong> تضمن مقاومة تلامس معدومة وتمنع أي ارتفاع حراري تحت تيار دائم حتى 400 أمبير.</li>
  <li><strong>سعة قطع تيار قصر معتمدة تصل إلى 80kA عند 415V AC:</strong> تضمن إخماداً فورياً وآمناً لأعتى تيارات الأعطال الكهربائية طبقاً لمواصفة BS 88.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1007 = [
    MSD_EN, MSD_FR, MSD_ES, MSD_AR,
    JFC_EN, JFC_FR, JFC_ES, JFC_AR
]
