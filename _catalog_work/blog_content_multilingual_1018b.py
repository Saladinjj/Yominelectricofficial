# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-18 (Batch 2):
1. Medium-Voltage Load Break Switches (LBS) for Distribution Feeder Automation (EN, FR, ES, AR)
2. Radiation Cross-Linked Polyolefin Busbar Heat Shrink Tubing for Switchgear Arc-Flash Protection (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. LOAD BREAK SWITCH (EN, FR, ES, AR)
# ==============================================================================

LBS_EN = dict(
    lang='en',
    dir='ltr',
    slug='distribution-grid-what-is-a-load-break-switch',
    title='Distribution Grid Switching: What Is a Load Break Switch?',
    breadcrumb='Medium-Voltage Distribution &amp; Load Break Switches',
    read='10 min read',
    alt='Medium-voltage 24kV Load Break Switch (Model FKN12/FLN36 series) mounted inside a switchgear cubicle with spring mechanism and earth switch',
    desc=('Medium-voltage distribution automation, ring main units (RMU), and compact transformer substations: What is a load break switch (LBS)? '
          'How spring-operated contacts, SF6 gas or vacuum arc quenching, integrated earthing switches, and high-voltage current-limiting fuse combinations provide safe feeder switching under full load current.'),
    model='Model FN18 / FLN36 / FKN12 / YM-LBS Series 12kV, 24kV, 36kV Indoor & Outdoor Pole-Mounted Medium-Voltage Load Break Switches (630A Rated Current, 25kA Making Capacity, Integrated Earth Switch, IEC 62271-102 / 105)',
    category='Medium-Voltage Distribution & Load Break Switches / Medium-Voltage Switchgear',
    kw='what is a load break switch &middot; load break switch &middot; sf6 load break switch &middot; pole mounted load break switch &middot; lbs switch &middot; load break switch with fuse',
    specs=[
        ('Rated Service Voltage & System Frequency', 'Nominal system voltages: 12 kV, 24 kV, and 36 kV AC (Rated power frequency: 50 Hz / 60 Hz)'),
        ('Rated Continuous Operational Current', 'Standard continuous current rating: 630 A (Optional heavy-duty feeder rating: up to 1250 A)'),
        ('Rated Short-Time Withstand Current ($I_k$)', '20 kA / 25 kA for 3 seconds / 4 seconds; Rated peak withstand current ($I_p$): up to 63 kA peak'),
        ('Rated Short-Circuit Making Capacity', 'Rated making capacity: 50 kA to 63 kA peak (Tested safe closure onto existing short-circuit faults without contact damage)'),
        ('Arc Quenching Media & Mechanism Design', 'Dual-break rotary puffing contact design: SF6 gas-insulated puffer chamber or hermetic vacuum interrupters with zero external emission'),
        ('Integrated Earth Switch Interlocking', 'Mechanically interlocked high-speed earthing switch with visible blade position indicator for maintenance grounding safety'),
        ('Operating Mechanism & Motorization Option', 'Manual spring-charge stored energy mechanism with snap-action trip coil; optional 24V/220V DC motor actuator for SCADA remote automation'),
        ('International Manufacturing Safety Standards', 'Fully tested and compliant with IEC 62271-1, IEC 62271-102 (Disconnectors & Earth Switches), and IEC 62271-105 (Switch-Fuse Combinations)')
    ],
    faqs=[
        ('What is a Load Break Switch (LBS) and how does it differ from a Circuit Breaker and an Isolator?',
         'A Load Break Switch (LBS)—frequently designated in utility distribution engineering as an interrupter switch, switch-disconnector, or sectionalizer switch—is '
         'a medium-voltage mechanical switching device designed to <strong>safely make, carry, and interrupt normal operational load currents</strong> '
         '(typically 630A at 12kV, 24kV, or 36kV), as well as closed-loop feeder loop currents and transformer magnetizing currents. '
         'In modern electrical distribution networks: '
         '<ul>'
         '<li><strong>Difference from an Isolator (Disconnector):</strong> An isolator has zero arc-extinguishing capability and can ONLY be opened '
         'when the circuit is completely de-energized under zero load. Opening an isolator under live load draws a continuous plasma arc exceeding 3000°C, '
         'resulting in explosive phase-to-phase flashover. An LBS incorporates high-speed spring mechanisms and an arc-quenching chamber that quenches full load arcs in milliseconds.</li>'
         '<li><strong>Difference from a Circuit Breaker (VCB/SF6):</strong> A circuit breaker is engineered to interrupt massive, symmetrical short-circuit fault currents '
         '(25kA to 40kA) via complex protective relay trip units. A circuit breaker costs 3× to 5× more than a load break switch. An LBS handles daily switching '
         'and sectionalizing, relying on downstream current-limiting fuses to clear short-circuits.</li>'
         '</ul>'),
        ('How does a Load Break Switch and High-Voltage Fuse Combination protect distribution transformers?',
         'Under standard IEC 62271-105 specifications, a Load Break Switch is frequently paired directly with three high-voltage current-limiting fuse-links: '
         '<ul>'
         '<li><strong>Operational Switching:</strong> The LBS handles routine operational switching: connecting, disconnecting, and sectionalizing the transformer '
         'under full rated load (e.g. 500kVA to 2500kVA distribution transformers).</li>'
         '<li><strong>Short-Circuit Clearance:</strong> If an internal transformer short-circuit or phase-to-phase cable fault occurs, the high-voltage current-limiting fuses '
         'melt and clear the fault current in under 5 to 10 milliseconds, cutting off peak short-circuit currents long before they reach destructive levels. '
         'When any single fuse blows, an integrated spring-loaded striker pin triggers the LBS mechanical trip latch, automatically opening all three phases simultaneously to prevent single-phasing damage.</li>'
         '</ul>'),
        ('What is the function of the Integrated Earth Switch in an LBS cubicle?',
         'Safety interlocking is mandatory in medium-voltage switchgear. YOMIN LBS units incorporate an integrated, mechanically interlocked earth switch: '
         '<ul>'
         '<li><strong>Fail-Safe Mechanical Interlock:</strong> The main switch contacts and the earth switch contacts share a mechanical key or lever interlock '
         'that makes it physically impossible to close the earth switch while the main load break switch is closed.</li>'
         '<li><strong>Personnel Maintenance Safety:</strong> Before utility technicians open the cable compartment for cable testing or maintenance, '
         'the main switch is opened, and the earth switch is closed, safely discharging all capacitive residual charges from underground cables directly to the station earth grid.</li>'
         '</ul>')
    ],
    cta='Designing medium-voltage distribution automation networks, ring main units (RMU), compact transformer substations, or overhead distribution feeder sectionalizing points requiring certified IEC 62271-102 / 105 indoor or pole-mounted load break switches (12kV–36kV, 630A, integrated earth switch, fuse combination)? YOMIN manufactures precision FN18/FLN36 series load break switches.',
    body='''
<h2>The Critical Sectionalizing and Switching Foundation for Modern Medium-Voltage Grids</h2>
<p>Inside electrical distribution networks, compact secondary substations, renewable solar/wind gathering stations, and industrial manufacturing plants operating at <strong>11kV, 24kV, or 33kV/36kV</strong>, electrical engineers face continuous operational switching requirements.</p>
<p>Feeder lines must be sectionalized for routine maintenance, transformer branches must be isolated without interrupting upstream substations, and ring distribution topologies must be reconfigured to maintain power continuity during local grid disturbances.</p>
<p>However, installing full-scale vacuum or SF6 circuit breakers at every switching point is economically prohibitive, while standard disconnectors (isolators) cannot be operated under load without triggering catastrophic electrical explosions.</p>
<p>The <strong>Medium-Voltage Load Break Switch (Model FN18 / FLN36 / FKN12 Series)</strong> provides the optimal technical and economic balance: a rugged, high-speed switching apparatus capable of safely interrupting full rated load currents (630A) and making onto short circuits, complete with integrated earthing safety and modular high-voltage current-limiting fuse protection.</p>

<h2>Engineering Anatomy: Inside a Model FLN36 / FKN12 Medium-Voltage Load Break Switch</h2>
<ol>
  <li><strong>Rotary Puffing Arc-Quenching Chamber:</strong> Utilizes SF6 gas insulation or vacuum interruption chambers. As contacts separate, an integrated piston compresses gas into a high-velocity blast directed across the contact gap, cooling and de-ionizing the AC plasma arc at the first natural zero-crossing.</li>
  <li><strong>Stored Energy Spring-Operating Mechanism:</strong> Operates independently of the operator\'s handle speed. A charged spring snaps the contacts open or closed in milliseconds, ensuring consistent arc interruption and preventing contact burning.</li>
  <li><strong>Mechanically Interlocked Earth Switch:</strong> Integrates high-conductivity earthing blades capable of withstanding short-circuit making currents (50kA peak), mechanically interlocked with the main contacts to ensure 100% fail-safe maintenance grounding.</li>
  <li><strong>Modular High-Voltage Fuse-Combination Base:</strong> Heavy-duty silver-plated spring clips accommodate high-rupturing-capacity (HRC) current-limiting fuses. Features a mechanical trip linkage that automatically trips the LBS open if any phase fuse blows.</li>
  <li><strong>Robust Epoxy Resin Insulating Enclosure:</strong> Cast from high-grade cycloaliphatic epoxy resin, providing superior mechanical rigidity, high dielectric strength, and high creepage distances that resist tracking in humid and contaminated substation environments.</li>
</ol>

<h2>Comparison: Load Break Switch (LBS) vs. Disconnector (Isolator) vs. Vacuum Circuit Breaker (VCB)</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Performance Metric</th>
      <th>Standard Disconnector (Isolator)</th>
      <th>YOMIN Medium-Voltage Load Break Switch (LBS)</th>
      <th>Vacuum Circuit Breaker (VCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Normal Rated Load Current Switching</strong></td>
      <td>Prohibited: Cannot interrupt load current (No-load operation only).</td>
      <td><strong>Full Capability: Safely makes and breaks full rated load (630A).</strong></td>
      <td>Full Capability: Makes and breaks rated operational load currents.</td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Fault Breaking Current</strong></td>
      <td>None: Zero fault interruption capability.</td>
      <td><strong>Via Fuses: Clears up to 50kA short-circuit faults with HRC fuses.</strong></td>
      <td>Full Autonomous: Trips and clears 25kA–40kA short-circuits via relays.</td>
    </tr>
    <tr>
      <td><strong>Equipment Cost &amp; Panel Space</strong></td>
      <td>Lowest cost; compact dimensions.</td>
      <td><strong>Optimal Economics: Approx. 25%–35% the cost of a full VCB panel.</strong></td>
      <td>Highest cost; requires CTs, protection relays, and auxiliary supply.</td>
    </tr>
    <tr>
      <td><strong>Maintenance Earthing Integration</strong></td>
      <td>Separate external earth switch required.</td>
      <td><strong>Built-in: Integrated mechanically interlocked earth switch standard.</strong></td>
      <td>Requires separate dedicated earthing switch assembly.</td>
    </tr>
    <tr>
      <td><strong>Primary Application in Distribution Grids</strong></td>
      <td>Visual safety isolation after breaker trip.</td>
      <td><strong>Ring Main Units (RMU), feeder sectionalizing, transformer bays.</strong></td>
      <td>Main substation incomers and critical transmission feeders.</td>
    </tr>
  </tbody>
</table>
'''
)

LBS_FR = dict(
    lang='fr',
    dir='ltr',
    slug='distribution-grid-what-is-a-load-break-switch-fr',
    title='Réseaux de Distribution Moyenne Tension : Qu\'est-ce qu\'un Interrupteur-Sectionneur (LBS) ?',
    breadcrumb='Distribution Moyenne Tension &amp; Interrupteurs-Sectionneurs',
    read='10 min de lecture',
    alt='Interrupteur-sectionneur moyenne tension 24kV (Série FLN36/FKN12) monté en cellule HTA avec mécanisme à ressort et sectionneur de terre',
    desc=('Réseaux de distribution HTA, cellules Ring Main Unit (RMU) et postes de transformation compacts : Qu\'est-ce qu\'un interrupteur-sectionneur moyenne tension (LBS) ? '
          'Coupure sous courant nominal de charge, extinction d\'arc au gaz SF6 ou sous vide, sectionneur de terre intégré et combiné fusibles HTA.'),
    model='Série FN18 / FLN36 / FKN12 : Interrupteurs-Sectionneurs Moyenne Tension 12kV, 24kV, 36kV pour Intérieur et Extérieur (630A, Pouvoir de Fermeture 25kA, Terre Intégrée, CEI 62271-102 / 105)',
    category='Distribution Moyenne Tension & Interrupteurs-Sectionneurs / Cellules HTA',
    kw='interrupteur sectionneur moyenne tension &middot; load break switch &middot; interrupteur hta sf6 &middot; combiné interrupteur fusible &middot; interrupteur sectionneur rmu &middot; lbs 24kv',
    specs=[
        ('Tension Assignée de Service et Fréquence', 'Tensions nominales de réseau : 12 kV, 24 kV et 36 kV AC (Fréquence industrielle : 50 Hz / 60 Hz)'),
        ('Courant Assigné Permanent Admissible ($I_n$)', 'Courant nominal permanent standard : 630 A (Option forte puissance : jusqu\'à 1250 A)'),
        ('Courant de Courte Durée Admissible ($I_k$)', '20 kA / 25 kA pendant 3 secondes / 4 secondes ; Valeur de crête admissible ($I_p$) : jusqu\'à 63 kA crête'),
        ('Pouvoir Assigné de Fermeture en Court-Circuit', 'Pouvoir de fermeture sur court-circuit : 50 kA à 63 kA crête (Fermeture sécurisée sans soudure de contacts)'),
        ('Principe et Milieu d\'Extinction d\'Arc', 'Contacts rotatifs à soufflage : Chambre étanche au gaz SF6 ou ampoules à vide à zéro émission externe'),
        ('Sectionneur de Terre Intégré et Verrouillage', 'Sectionneur de mise à la terre rapide à commande dépendante avec verrouillage mécanique anti-fausse manœuvre'),
        ('Mécanisme de Commande et Motorisation', 'Mécanisme à accumulation d\'énergie par ressorts à déclenchement brusque ; Motorisation 24V/220V DC pour téléconduite SCADA'),
        ('Conformité aux Normes Internationales', 'Certifié et conforme aux normes CEI 62271-1, CEI 62271-102 (Sectionneurs et Terre) et CEI 62271-105 (Combinés Fusibles)')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Interrupteur-Sectionneur (LBS) et comment se distingue-t-il d\'un Disjoncteur et d\'un Sectionneur ?',
         'Un Interrupteur-Sectionneur moyenne tension (Load Break Switch)—communément désigné sous l\'acronyme LBS ou interrupteur HTA—est '
         'un appareil électromécanique de coupure capable <strong>d\'établir, de supporter et d\'interrompre des courants dans les conditions normales de charge</strong> '
         '(généralement 630 A sous 12 kV ou 24 kV), ainsi que de fermer en toute sécurité sur un court-circuit accidentel. '
         'Dans les postes de distribution électrique : '
         '<ul>'
         '<li><strong>Différence avec le Sectionneur simple :</strong> Le sectionneur n\'a aucun pouvoir de coupure ; il ne peut être manœuvré '
         'qu\'à vide absolu. L\'ouvrir en charge provoquerait un arc électrique explosif dévastateur. L\'interrupteur-sectionneur coupe le courant nominal instantanément.</li>'
         '<li><strong>Différence avec le Disjoncteur HTA :</strong> Le disjoncteur est conçu pour couper des courants de court-circuit massifs (25 à 40 kA) '
         'via des relais de protection numériques, à un coût 3 à 4 fois plus élevé. L\'interrupteur-sectionneur assure l\'exploitation quotidienne, '
         'la protection contre les courts-circuits étant déléguée à des fusibles limiteurs HTA associés.</li>'
         '</ul>'),
        ('Comment fonctionne l\'association Interrupteur-Sectionneur et Fusibles HTA (Combiné Inter-Fusibles) ?',
         'Selon la norme CEI 62271-105, l\'interrupteur-sectionneur est très fréquemment associé en série avec trois fusibles limiteurs à haut pouvoir de coupure : '
         '<ul>'
         '<li><strong>Exploitation Normale :</strong> L\'interrupteur-sectionneur assure l\'enclenchement et le déclenchement en charge du transformateur.</li>'
         '<li><strong>Protection Court-Circuit :</strong> En cas de défaut interne sur le transformateur, les fusibles fondent en quelques millisecondes, '
         'limitant l\'onde de courant. Dès la fusion d\'un fusible, un percuteur mécanique libère instantanément le ressort de l\'interrupteur, '
         'provoquant l\'ouverture simultanée des trois phases pour éviter tout fonctionnement dangereux en biphasé.</li>'
         '</ul>'),
        ('Quel est le rôle du Sectionneur de Terre intégré dans une cellule HTA ?',
         'Le sectionneur de mise à la terre intégré à l\'interrupteur-sectionneur YOMIN garantit la sécurité absolue des opérateurs : '
         'un verrouillage mécanique interdit formellement de fermer la terre lorsque l\'interrupteur principal est enclenché, '
         'et permet de décharger l\'énergie résiduelle capacitive des câbles souterrains avant toute intervention humaine.')
    ],
    cta='Vous concevez des cellules de distribution HTA en boucle fermée (Ring Main Units), des postes de transformation compacts ou des départs aériens nécessitant des interrupteurs-sectionneurs certifiés CEI 62271-102 / 105 (12kV–36kV, 630A, terre intégrée, combiné fusibles) ? YOMIN fabrique des appareils séries FN18/FLN36 de haute fiabilité.',
    body='''
<h2>L\'Appareil de Manœuvre et de Sectionnement Incontournable des Réseaux Moyenne Tension</h2>
<p>Sur les réseaux de distribution d\'électricité moyenne tension, dans les postes de livraison abonnés et les postes de transformation urbains et industriels fonctionnant sous <strong>11kV, 24kV ou 33kV</strong>, la gestion des flux d\'énergie exige des organes de coupure performants.</p>
<p>Il est indispensable de pouvoir commuter les départs en charge, isoler un tronçon de câble souterrain en maintenance et réalimenter les boucles sans provoquer d\'interruption générale sur le réseau amont.</p>
<p>L\'installation systématique de disjoncteurs sous vide est économiquement trop lourde pour les départs secondaires, tandis que les simples sectionneurs ne peuvent pas être ouverts en charge sous peine d\'explosion.</p>
<p>L\'<strong>Interrupteur-Sectionneur Moyenne Tension (Séries FN18 / FLN36 / FKN12)</strong> offre le compromis technico-économique idéal : un appareil compact, robuste et endurant, capable d\'interrompre les courants de charge nominaux (630A) et d\'assurer la sécurité du personnel grâce à son sectionneur de terre intégré et son combiné fusibles HTA.</p>

<h2>Caractéristiques et Avantages Technologiques des Séries FLN36 / FKN12</h2>
<ol>
  <li><strong>Chambre de Coupure à Soufflage au Gaz SF6 ou sous Vide :</strong> Soufflage automatique de gaz lors de la séparation des contacts, refroidissant et déionisant l\'arc électrique dès le premier passage à zéro du courant alternatif.</li>
  <li><strong>Commande Mécanique à Accumulation d\'Énergie par Ressorts :</strong> Vitesse d\'ouverture et de fermeture indépendante de l\'opérateur, garantissant une rupture franche et empêchant l\'usure prématurée des contacts d\'arc.</li>
  <li><strong>Sectionneur de Terre à Fermeture Rapide Intégré :</strong> Couteaux de mise à la terre dimensionnés pour fermer sur court-circuit (50 kA crête) avec verrouillage mécanique positif anti-erreur.</li>
  <li><strong>Combiné Fusibles Haute Tension avec Déclenchement Automatique :</strong> Système de tringlerie déclenchant l\'ouverture tripolaire instantanée dès la fusion du percuteur d\'un des trois fusibles HTA.</li>
  <li><strong>Enveloppe Isolante en Résine Époxyde Moule :</strong> Rigidité diélectrique exceptionnelle et tenue parfaite contre la condensation et la pollution industrielle en cellule fermée.</li>
</ol>
'''
)

LBS_ES = dict(
    lang='es',
    dir='ltr',
    slug='distribution-grid-what-is-a-load-break-switch-es',
    title='Redes de Distribución de Media Tensión: ¿Qué es un Interruptor de Carga (Load Break Switch)?',
    breadcrumb='Distribución de Media Tensión e Interruptores de Carga',
    read='10 min de lectura',
    alt='Interruptor de carga de media tensión de 24kV (Serie FLN36/FKN12) instalado en celda de distribución con mecanismo de resortes y seccionador de puesta a tierra',
    desc=('Automatización de distribución eléctrica, celdas tipo Ring Main Unit (RMU) y subestaciones compactas: ¿Qué es un interruptor de carga (Load Break Switch - LBS)? '
          'Corte de corriente nominal bajo carga, extinción de arco en gas SF6 o vacío, seccionador de tierra integrado y combinación con fusibles de media tensión.'),
    model='Serie FN18 / FLN36 / FKN12: Interruptores Seccionadores de Carga de Media Tensión 12kV, 24kV, 36kV para Interior e Intemperie (630A, Poder de Cierre 25kA, Puesta a Tierra Integrada, IEC 62271-102 / 105)',
    category='Distribución de Media Tensión e Interruptores de Carga / Celdas de Media Tensión',
    kw='interruptor de carga &middot; load break switch &middot; interruptor seccionador media tension &middot; interruptor sf6 rmu &middot; combinacion interruptor fusible &middot; lbs 24kv',
    specs=[
        ('Tensión Nominal de Servicio y Frecuencia', 'Tensiones nominales del sistema: 12 kV, 24 kV y 36 kV AC (Frecuencia de red: 50 Hz / 60 Hz)'),
        ('Corriente Nominal Continua de Operación ($I_n$)', 'Corriente nominal continua estándar: 630 A (Opción para alimentadores pesados: hasta 1250 A)'),
        ('Corriente de Corta Duración Admisible ($I_k$)', '20 kA / 25 kA durante 3 segundos / 4 segundos ; Corriente pico admisible ($I_p$): hasta 63 kA pico'),
        ('Capacidad de Cierre en Cortocircuito Asignada', 'Poder de cierre sobre cortocircuito: 50 kA a 63 kA pico (Cierre seguro sin daño en los contactos de potencia)'),
        ('Medio y Principio de Extinción del Arco', 'Diseño rotativo autocompresor: Cámara aislada en gas SF6 o botellas de vacío herméticas con cero emisión externa'),
        ('Seccionador de Puesta a Tierra con Enclavamiento', 'Cuchillas de puesta a tierra rápida integradas con bloqueo mecánico positivo que impide maniobras erróneas'),
        ('Mecanismo de Operación y Motorización', 'Mecanismo de resortes con acumulación de energía de disparo rápido ; Motorización 24V/220V DC para telemando SCADA'),
        ('Conformidad con Normativas Internacionales', 'Probado y certificado bajo normas internacionales IEC 62271-1, IEC 62271-102 (Seccionadores y Tierra) e IEC 62271-105 (Interruptor-Fusible)')
    ],
    faqs=[
        ('¿Qué es un Interruptor de Carga (Load Break Switch) y en qué se diferencia de un Interruptor de Potencia y un Seccionador?',
         'Un Interruptor de Carga (Load Break Switch - LBS)—denominado en ingeniería eléctrica como interruptor seccionador bajo carga—es '
         'un equipo de maniobra de media tensión diseñado para <strong>conectar, conducir e interrumpir corrientes nominales en condiciones normales de carga</strong> '
         '(típicamente 630 A a 12 kV, 24 kV o 36 kV), así como cerrar con total seguridad sobre un cortocircuito. '
         'En redes de distribución eléctrica : '
         '<ul>'
         '<li><strong>Diferencia con el Seccionador simple:</strong> Un seccionador ordinario carece de capacidad de extinción de arco; solo puede abrirse '
         'sin carga (desconectado). Abrirlo bajo carga provocaría un arco violento destructivo. El LBS extingue el arco de carga en milisegundos.</li>'
         '<li><strong>Diferencia con el Interruptor de Potencia (Disyuntor):</strong> El disyuntor interrumpe enormes corrientes de cortocircuito (25 a 40 kA) '
         'mediante relés de protección numéricos, a un costo 3 a 4 veces superior. El interruptor de carga realiza las maniobras diarias de servicio '
         'y deriva la protección contra cortocircuitos a fusibles limitadores de alta capacidad de ruptura.</li>'
         '</ul>'),
        ('¿Cómo protege a un transformador la combinación de Interruptor de Carga con Fusibles de Media Tensión?',
         'Bajo la norma IEC 62271-105, el interruptor de carga se combina directamente con tres fusibles limitadores de corriente de alta tensión: '
         '<ul>'
         '<li><strong>Maniobra de Servicio:</strong> El interruptor de carga realiza las aperturas y cierres de operación normal del transformador.</li>'
         '<li><strong>Desconexión en Falla:</strong> Si ocurre un cortocircuito interno en el transformador, los fusibles se funden en menos de 10 milisegundos. '
         'Al fundirse cualquiera de ellos, un percutor mecánico acciona instantáneamente el trinquete del interruptor de carga, abriendo las tres fases '
         'de manera simultánea para evitar sobrecalentamientos por operación bifásica.</li>'
         '</ul>'),
        ('¿Qué función cumple el Seccionador de Puesta a Tierra integrado?',
         'El seccionador de tierra integrado en el LBS de YOMIN garantiza la seguridad del personal : '
         'un enclavamiento mecánico hace imposible cerrar la tierra si el interruptor principal está conectado, '
         'y permite descargar la tensión residual capacitiva de los cables subterráneos antes de que los técnicos accedan a la celda.')
    ],
    cta='¿Diseña celdas de media tensión en anillo (Ring Main Units), subestaciones compactas de distribución o líneas aéreas que requieren interruptores seccionadores bajo carga certificados IEC 62271-102 / 105 (12kV–36kV, 630A, puesta a tierra integrada, combinación con fusibles)? YOMIN suministra interruptores series FN18/FLN36 de alta confiabilidad.',
    body='''
<h2>El Dispositivo de Maniobra y Seccionamiento Clave para Redes Eléctricas de Media Tensión</h2>
<p>En redes de distribución de energía eléctrica, subestaciones secundarias compactas y plantas industriales que operan en <strong>11kV, 24kV o 36kV</strong>, los ingenieros de operación requieren equipos de corte confiables y versátiles.</p>
<p>Es indispensable maniobrar circuitos alimentadores en servicio continuo, aislar tramos de cable subterráneo para mantenimiento y reconfigurar la red en anillo sin provocar cortes generales en las subestaciones principales.</p>
<p>Instalar interruptores automáticos (disyuntores) en cada punto de derivación resulta económicamente inviable, mientras que los simples seccionadores no pueden abrirse bajo carga.</p>
<p>El <strong>Interruptor de Carga de Media Tensión (Series FN18 / FLN36 / FKN12)</strong> ofrece la solución técnica y económica ideal : un equipo robusto y compacto capaz de interrumpir corrientes de carga completas (630A) con máxima seguridad gracias a su seccionador de tierra integrado y su conjunto de fusibles de alta tensión.</p>

<h2>Componentes Constructivos y Ventajas de Ingeniería de las Series FLN36 / FKN12</h2>
<ol>
  <li><strong>Cámara de Extinción de Arco con Gas SF6 o Vacío:</strong> Sistema rotativo que comprime el gas hacia los contactos de corte, extinguiendo el arco eléctrico en el primer cruce por cero de la corriente alterna.</li>
  <li><strong>Mando Mecánico de Resortes con Acumulación de Energía:</strong> Velocidad de maniobra independiente del operador, garantizando una desconexión instantánea sin desgaste en los contactos principales.</li>
  <li><strong>Cuchillas de Puesta a Tierra Rápida Integradas:</strong> Capaces de cerrar sobre cortocircuito (50 kA pico) con enclavamiento mecánico positivo que elimina riesgos humanos.</li>
  <li><strong>Conjunto Combinado con Fusibles de Media Tensión:</strong> Sistema de disparo tripolar automático accionado por el percutor del fusible ante cualquier cortocircuito severo.</li>
  <li><strong>Aislamiento en Resina Epoxi de Alta Rigidez:</strong> Envolvente de resina cicloalifática resistente a la tracción mecánica, arborescencias eléctricas y condensación ambiental severa.</li>
</ol>
'''
)

LBS_AR = dict(
    lang='ar',
    dir='rtl',
    slug='distribution-grid-what-is-a-load-break-switch-ar',
    title='شبكات توزيع الجهد المتوسط: ما هو قاطع كسر الحمل (Load Break Switch - LBS)؟',
    breadcrumb='توزيع الجهد المتوسط وقواطع كسر الحمل',
    read='10 دقائق قراءة',
    alt='قاطع كسر الحمل للجهد المتوسط 24kV (موديل FLN36/FKN12) مثبت داخل خلية مفاتيح بآلية زنبركية وسكين تأريض مدمج',
    desc=('أتمتة شبكات توزيع الجهد المتوسط، وحلقات التغذية الحلقية (RMU)، ومحطات المحولات المدمجة: ما هو قاطع كسر الحمل (Load Break Switch - LBS)؟ '
          'قطع تيار الحمل الاسمي، وإخماد الشرر بغاز SF6 أو غرف التفريغ، وسكين التأريض الميكانيكي المدمج، ومجموعة المصهرات ذات سعة القطع العالية.'),
    model='سلسلة FN18 / FLN36 / FKN12: قواطع كسر الحمل للجهد المتوسط 12kV و 24kV و 36kV للاستخدام الداخلي والخارجي (تيار 630A، قدرة توصيل قصر 25kA، تأريض مدمج، معتمدة IEC 62271-102 / 105)',
    category='توزيع الجهد المتوسط وقواطع كسر الحمل / خلايا الجهد المتوسط HTA',
    kw='قاطع كسر الحمل &middot; load break switch &middot; مفتاح فصل تحت الحمل &middot; قاطع lbs &middot; مفتاح غاز sf6 &middot; قاطع احمال الجهد المتوسط',
    specs=[
        ('الجهد الاسمي المقنن وتردد الشبكة', 'جهود التشغيل الاسمية: 12 كيلو فولت، 24 كيلو فولت، و 36 كيلو فولت AC (التردد المقنن: 50/60 هرتز)'),
        ('التيار المستمر الاسمي المقنن للتشغيل ($I_n$)', 'تيار الحمل المستمر القياسي: 630 أمبير (خيار التيارات العالية: حتى 1250 أمبير)'),
        ('تيار الصمود الحراري لفترة قصيرة ($I_k$)', '20 kA / 25 kA لمدة 3 ثوانٍ / 4 ثوانٍ؛ تيار القمة الأقصى الصامد ($I_p$): حتى 63 kA قمة'),
        ('قدرة التوصيل على تيار القصر المقننة', 'قدرة إغلاق مؤكدة على تيار القصر: 50 kA إلى 63 kA قمة (إغلاق آمن دون التحام نقاط التلامس)'),
        ('وسط إخماد القوس الكهربائي والآلية', 'تصميم نفث الغاز الذاتي المزدوج: غرف معزولة بغاز سداسي فلوريد الكبريت SF6 أو غرف تفريغ محكمة Vacuum'),
        ('سكين التأريض المدمج ونظام القفل التبادلي', 'سكين تأريض سريع متكامل مع قفل ميكانيكي ترادفي إيجابي لمنع مناورات التأريض الخاطئة'),
        ('آلية التشغيل الميكانيكية وإمكانية الأتمتة', 'آلية زنبركية لتخزين الطاقة بفتح وإغلاق فوري مستقل؛ محرك كهربائي 24V/220V DC اختياري للربط مع SCADA'),
        ('المطابقة للمواصفات والاعتمادات الدولية', 'مختبر ومعتمد بالكامل وفقاً للمعايير الدولية IEC 62271-1 و IEC 62271-102 (الفواصـل والتأريض) و IEC 62271-105 (المصهرات)')
    ],
    faqs=[
        ('ما هو قاطع كسر الحمل (Load Break Switch - LBS) وكيف يختلف عن القاطع الآلي وفاصل العزل؟',
         'قاطع كسر الحمل للجهد المتوسط—والمعروف هندسياً باسم مفتاح الفصل تحت الحمل (LBS) أو قاطع المناورة—هو '
         'جهاز ميكانيكي متطور في شبكات الجهد المتوسط مصمم <strong>لتوصيل وتحمل وفصل تيارات الحمل العادية بالكامل في ظروف التشغيل الحية</strong> '
         '(عادة 630 أمبير بجهد 12kV أو 24kV أو 36kV)، فضلاً عن قدرته على التوصيل الآمن أثناء حدوث تيار قصر عرضي. '
         'وفي منظومة شبكات التوزيع : '
         '<ul>'
         '<li><strong>الفارق مع فاصل العزل (Disconnector/Isolator):</strong> فاصل العزل العادي لا يمتلك أي وسيلة لإخماد القوس الكهربائي، '
         'ولا يجوز فتحه إلا عندما تكون الدائرة مفصولة تماماً وبلا حمل. فتحه تحت الحمل يولد شرارة انفجارية مدمرة. بينما يطفئ قاطع LBS شرارة تيار الحمل في أجزاء من الثانية.</li>'
         '<li><strong>الفارق مع القاطع الآلي (Circuit Breaker):</strong> صُمم القاطع الآلي لقطع تيارات القصر الهائلة (25 إلى 40 ألف أمبير) '
         'عبر مرحلات حماية معقدة وبكلفة تعادل 3 إلى 4 أضعاف. يقوم قاطع كسر الحمل بمناورات الفصل والتشغيل اليومية، وتُوكل مهمة حماية القصر إلى مصهرات الجهد العالي.</li>'
         '</ul>'),
        ('كيف تحمي منظومة قاطع كسر الحمل المدمج مع المصهرات (LBS + Fuses) محولات التوزيع؟',
         'وفقاً للمواصفة الدولية IEC 62271-105، يتم دمج قاطع كسر الحمل في نسق ترادفي مع ثلاث مصهرات حماية عالية سعة القطع (HRC) : '
         '<ul>'
         '<li><strong>التشغيل الاعتيادي:</strong> يقوم قاطع LBS بمناورات التغذية وفصل المحول تحت كامل الحمل الاسمي بأمان تام.</li>'
         '<li><strong>الحماية عند القصر:</strong> عند حدوث عطل قصر داخلي في المحول، تنصهر المصهرات في أقل من 10 أجزاء من الألف من الثانية، '
         'محددة قمة تيار العطل. وبمجرد انصهار أي مصهر، يندفع مسمار طارق ميكانيكي (Striker Pin) ليفصل آلية القاطع الرئيسي فورياً، '
         'مما يؤدي لفتح الأوجه الثلاثة في آن واحد لمنع احتراق المحول بسبب تغذية وجهين فقط.</li>'
         '</ul>'),
        ('ما هي وظيفة سكين التأريض المدمج داخل خلية القاطع؟',
         'يمثل سكين التأريض المدمج ركيزة الأمان الحيوية لفنيي الصيانة : '
         'حيث يمنع نظام القفل الميكانيكي الداخلي إمكانية إغلاق سكين التأريض نهائياً إذا كان القاطع الرئيسي في وضع التوصيل، '
         'ويتيح تفريغ الشحنات الكهربائية السعوية المتبقية في الكابلات المدفونة مباشرة نحو الأرض قبل فتح باب الخلية لبدء الصيانة.')
    ],
    cta='هل تعمل على تصميم محطات شبكات التوزيع الحلقية (RMU)، أو محطات المحولات المدمجة، أو خطوط التوزيع الهوائية التي تتطلب قواطع كسر الحمل المعتمدة IEC 62271-102 / 105 (جهد 12kV–36kV، تيار 630A، تأريض مدمج، وتوافق المصهرات)؟ تصنع يمين (YOMIN) قواطع سلسلة FN18/FLN36 بأعلى معايير الموثوقية.',
    body='''
<h2>الركيزة الهندسية لمناورات التشغيل والعزل الآمن في شبكات توزيع الجهد المتوسط</h2>
<p>في شبكات توزيع الطاقة الكهربائية، ومحطات التوزيع الحلقية الثانوية، ومحطات محولات التغذية الصناعية التي تعمل بجهود <strong>11 كيلو فولت، 24 كيلو فولت، أو 33/36 كيلو فولت</strong>، يواجه مهندسو التشغيل متطلبات مناورة وتحويل مستمرة لتغذية الأحمال.</p>
<p>يتعين فصل وتجزئة الخطوط لإجراء الصيانة المجدولة، وتغذية المحولات الفرعية، وإعادة تشكيل مسارات الحلقات دون التسبب في انقطاعات عامة للكهرباء عبر الشبكة الرئيسية.</p>
<p>إن تركيب قواطع آلية تفريغية باهظة الثمن عند كل نقطة تفريع يمثل عبئاً مالياً كبيراً، في حين أن الفواصـل العادية لا تملك أي قدرة على قطع تيار الحمل المار.</p>
<p>يقدم <strong>قاطع كسر الحمل للجهد المتوسط (سلسلة FN18 / FLN36 / FKN12)</strong> التوازن الهندسي والاقتصادي الأمثل: جهاز مناورة ميكانيكي قوي وسريع قادر على إخماد تيارات الحمل الكاملة (630 أمبير) بأمان تام، ومزود بسكين تأريض مدمج ومصهرات جهد عالٍ حاسمة للحماية من أخطار القصر.</p>

<h2>المكونات الهندسية وميزات التصميم لسلسلة قواطع FLN36 / FKN12</h2>
<ol>
  <li><strong>غرفة إخماد الشرر بنفث غاز SF6 أو التفريغ:</strong> مكبس ذاتي يضغط الغاز باتجاه نقاط التلامس عند انفصالها، مما يبرد القوس الكهربائي ويزيل تأينه عند أول نقطة عبور لصفر التيار المتردد.</li>
  <li><strong>آلية تشغيل زنبركية سريعة لتخزين الطاقة:</strong> سرعة فتح وإغلاق ثابتة ومستقلة تماماً عن حركة يد المشغل، مما يضمن سرعة قطع فائقة تمنع تآكل نقاط التلامس.</li>
  <li><strong>سكين تأريض سريع مدمج عالي الكفاءة:</strong> قادر على التوصيل على تيار القصر (50 kA قمة) مع قفل ميكانيكي إيجابي يمنع أي خطأ بشري أثناء عمليات الصيانة.</li>
  <li><strong>قاعدة مصهرات الجهد العالي المزودة بآلية الفصل التلقائي:</strong> نظام ميكانيكي ترادفي يفصل الأوجه الثلاثة فورياً عند انصهار مسمار أي مصهر لحماية المحولات.</li>
  <li><strong>هيكل عازل من راتنج الإيبوكسي المصبوب:</strong> عزل ديإلكتريكي فائق يتحمل التلوث والرطوبة المرتفعة والإجهادات الديناميكية العنيفة داخل خلايا التوزيع المدمجة.</li>
</ol>
'''
)

# ==============================================================================
# 2. BUSBAR HEAT SHRINK TUBE (EN, FR, ES, AR)
# ==============================================================================

BST_EN = dict(
    lang='en',
    dir='ltr',
    slug='switchgear-insulation-what-is-a-busbar-heat-shrink-tube',
    title='Switchgear Insulation: What Is a Busbar Heat Shrink Tube?',
    breadcrumb='Switchgear Busbars &amp; Insulation Sleeves',
    read='10 min read',
    alt='Medium-voltage copper distribution busbars insulated with radiation cross-linked polyolefin Busbar Heat Shrink Tubing (Model MPBS series) inside electrical switchgear',
    desc=('Medium-voltage switchgear cubicles, compact substations, motor control centers (MCC), and busbar trunking systems: What is a busbar heat shrink tube? '
          'How radiation cross-linked polyolefin, 2:1 shrink ratios, high dielectric strength (> 25 kV/mm), and flame-retardant formulation allow up to 50% reduction in switchgear busbar air clearances while eliminating arc-flash risks.'),
    model='Model MPBS / WRSBG Series 1kV, 10kV, 24kV, 36kV Radiation Cross-Linked Polyolefin Heat-Shrinkable Busbar Insulation Tubing (Shrink Ratio 2:1 / 2.5:1, Dielectric Strength > 25 kV/mm, UL 224 / IEC 60068)',
    category='Switchgear Busbars & Insulation Sleeves / Heat-Shrinkable Busbar Tubing',
    kw='what is a busbar heat shrink tube &middot; busbar heat shrink tube &middot; busbar heat shrink tubing &middot; medium voltage busbar insulation sleeve &middot; 10kv busbar heat shrink &middot; 36kv busbar sleeve',
    specs=[
        ('Base Polymer Formulation & Cross-Linking', 'Specially formulated radiation cross-linked thermally stabilized flame-retardant polyolefin (Zero halogens, low smoke emission)'),
        ('Operating Voltage Insulation Class Ratings', 'Standard ratings: 1 kV (LV control busbars), 10 kV / 12 kV, 24 kV, and 36 kV / 40.5 kV (MV substation busbars)'),
        ('Radial Heat Shrink Expansion Ratio', 'Standard shrink ratio: 2:1 and 2.5:1 (Conforms smoothly over rectangular, square, round, and bend copper/aluminum busbars)'),
        ('Minimum Shrink & Full Recovery Temperatures', 'Initial shrink temperature: $\ge 85^\circ\text{C}$; Full complete elastic recovery temperature: $\ge 120^\circ\text{C}$ (Fast installation with hot air gun)'),
        ('Dielectric Breakdown Strength & Withstand', 'Tested dielectric breakdown strength: $\ge 25\,\text{kV/mm}$ (Withstands $1\,\text{min}$ power-frequency withstand up to $80\,\text{kV}$)'),
        ('Continuous Operating Thermal Endurance', 'Continuous operating temperature range: $-55^\circ\text{C}$ to $+125^\circ\text{C}$ (Thermal aging tested at $150^\circ\text{C}$ for 168 hours)'),
        ('Flame Retardancy & Self-Extinguishing Grade', 'Meets UL 224 VW-1 flame retardancy; oxygen index $\ge 30\%$; self-extinguishing within $< 15$ seconds without dripping'),
        ('International Manufacturing Safety Standards', 'Fully tested and compliant with IEC 60068 (Environmental Testing), UL 224, ASTM D2671, and GB/T 1059')
    ],
    faqs=[
        ('What is a Busbar Heat Shrink Tube and why is it essential in modern electrical switchgear?',
         'A Busbar Heat Shrink Tube—frequently designated as a medium-voltage busbar insulation sleeve, busbar heat shrinkable tubing, or cross-linked polyolefin busbar wrap—is '
         'a specialized heavy-wall, heat-shrinkable insulating sleeve extruded from radiation cross-linked polyolefin polymers. '
         'In electrical power distribution switchboards and transformer cubicles: '
         '<ul>'
         '<li><strong>Arc-Flash Fault Prevention:</strong> Uninsulated bare copper busbars inside switchgear cabinets are vulnerable to accidental short-circuits. '
         'Intruding vermin (rats, geckos, snakes), condensation dripping from cabinet ceilings, or accidental dropped tools bridge the air gap between adjacent bare phases, '
         'instantly triggering catastrophic multi-megawatt arc-flash explosions. Busbar heat shrink tubing forms a seamless, impenetrable dielectric skin '
         'that prevents phase-to-phase and phase-to-ground flashovers even under direct vermin contact.</li>'
         '<li><strong>Switchgear Clearance Reduction (Up to 50%):</strong> Standard electrical safety codes require substantial air clearances between bare busbars '
         '(e.g. at 24kV, bare conductors require over 180mm to 220mm of air clearance). Insulating the busbars with YOMIN MPBS tubing allows electrical panel builders '
         'to <strong>reduce phase-to-phase and phase-to-ground clearances by up to 50%</strong>, shrinking overall switchgear enclosure dimensions, saving floor space, and reducing enclosure manufacturing costs.</li>'
         '</ul>'),
        ('How does Radiation Cross-Linking enhance the thermal and mechanical endurance of Busbar Tubing?',
         'Standard thermoplastic polymers soften, melt, and flow when subjected to temperatures exceeding 80°C to 100°C. '
         'YOMIN busbar tubing undergoes high-energy <strong>electron beam radiation cross-linking</strong>: '
         '<ul>'
         '<li><strong>Molecular Matrix:</strong> The electron beam breaks linear polymer chains, creating strong permanent covalent carbon-carbon bonds '
         'between adjacent molecular chains, transforming the material into a three-dimensional elastomeric network.</li>'
         '<li><strong>Thermal Memory &amp; Resistance:</strong> Cross-linked polyolefin does NOT melt at high temperatures. Under continuous full-load busbar '
         'operating temperatures ($105^\circ\text{C}$) and momentary short-circuit fault spikes ($250^\circ\text{C}$ for 1 to 3 seconds), '
         'the tubing maintains complete mechanical elasticity, zero dripping, and 100% dielectric integrity without thermal degradation.</li>'
         '</ul>'),
        ('What is the difference between Busbar Heat Shrink Tubing and standard Thin-Wall Heat Shrink Tubing?',
         'Thin-wall heat shrink tubing is designed for low-voltage (600V) wire harnessing, electronic splices, and cosmetic color-coding, featuring thin walls (0.3mm to 0.5mm) '
         'with low dielectric breakdown and minimal tear resistance. '
         '<strong>Busbar Heat Shrink Tubing (YOMIN MPBS series)</strong> features a heavy, uniform wall thickness (2.0mm to 4.5mm after recovery), '
         'formulated specifically to withstand 10kV, 24kV, and 36kV continuous dielectric stresses, with high tensile strength ($\ge 14\,\text{MPa}$), '
         'superior tracking resistance, and puncture resistance against sharp copper busbar punched edges.')
    ],
    cta='Designing compact medium-voltage switchgear cubicles, motor control centers (MCC), transformer terminal links, or busbar trunking systems requiring certified IEC 60068 / UL 224 heat-shrinkable busbar insulation tubing (1kV to 36kV, 2:1 shrink ratio, > 25kV/mm dielectric, up to 50% clearance reduction)? YOMIN manufactures precision MPBS series busbar sleeves.',
    body='''
<h2>The Dielectric Armor for Compact Switchgear and Arc-Flash Risk Mitigation</h2>
<p>Inside modern electrical utility substations, commercial power distribution switchboards, compact ring main units (RMU), and industrial motor control centers, high-conductivity copper and aluminum busbars carry heavy electric currents at voltages from <strong>1kV up to 36kV</strong>.</p>
<p>To reduce real estate footprint and equipment manufacturing costs, electrical panel builders engineer switchgear enclosures to be as compact and slim as possible.</p>
<p>However, compact switchgear cabinets force adjacent phase busbars into extremely tight proximity. If bare copper busbars are left exposed, minor airborne dust accumulation, high humidity condensation, or an intruding rodent bridging two phases triggers an explosive, multi-megawatt arc-flash fault that destroys the entire switchgear line.</p>
<p>The <strong>Medium-Voltage Heat-Shrinkable Busbar Insulation Tubing (Model MPBS / WRSBG Series)</strong> provides the definitive engineering solution: a rugged, radiation cross-linked polyolefin sleeve that shrinks seamlessly over straight, curved, and complex rectangular copper busbars, doubling dielectric withstand, eliminating flashovers, and enabling up to 50% reduction in switchgear air clearances.</p>

<h2>Engineering Anatomy: Inside Model MPBS Medium-Voltage Busbar Heat Shrink Tubing</h2>
<ol>
  <li><strong>Radiation Cross-Linked Polyolefin Matrix:</strong> Formulated from premium polyolefin polymers subjected to high-energy electron beam irradiation, creating a cross-linked molecular network that prevents melting, dripping, or cracking under thermal overloads up to $200^\circ\text{C}$.</li>
  <li><strong>Engineered Radial Shrink Ratio (2:1 to 2.5:1):</strong> Expands easily over rectangular busbars of varying widths and thicknesses, recovering with uniform wall thickness (2.0mm to 4.5mm) tightly conforming around sharp 90-degree bends without creasing or thinning.</li>
  <li><strong>Superior Dielectric Withstand Voltage (&ge; 25 kV/mm):</strong> High dielectric strength ensures that a single layer of YOMIN 24kV/36kV busbar tubing provides complete insulation integrity against phase-to-phase and phase-to-ground flashover voltages.</li>
  <li><strong>Flame-Retardant &amp; Halogen-Free Formulation:</strong> Self-extinguishing material compliant with UL 224 VW-1 that extinguishes flame within seconds without dripping flaming polymers or emitting corrosive halogen acid gases during accidental cabinet fires.</li>
  <li><strong>Environmental Tracking &amp; UV Resistance:</strong> Specially stabilized against ozone, solar ultraviolet radiation, and harsh industrial chemical vapors, preventing surface tracking in contaminated and humid industrial environments.</li>
</ol>

<h2>Comparison: YOMIN Busbar Heat Shrink Tubing vs. Standard Thin-Wall Tubing vs. Liquid PVC Dip Coating</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Performance Metric</th>
      <th>Standard Thin-Wall Tubing</th>
      <th>Liquid PVC Dip Coating</th>
      <th>YOMIN Busbar Heat Shrink Tubing (MPBS Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Voltage Rating &amp; Dielectric Strength</strong></td>
      <td>Low Voltage Only (600V); Dielectric &lt; 10 kV/mm.</td>
      <td>Unpredictable: Non-uniform thickness causes weak dielectric spots.</td>
      <td><strong>Medium Voltage Certified: 10kV to 36kV; Uniform &gt; 25 kV/mm.</strong></td>
    </tr>
    <tr>
      <td><strong>Wall Thickness After Recovery</strong></td>
      <td>Thin (0.3mm to 0.5mm); easily punctured by sharp busbar edges.</td>
      <td>Varies drastically on corners; prone to sagging and bubbles.</td>
      <td><strong>Heavy-Duty (2.0mm to 4.5mm): High mechanical tear and cut resistance.</strong></td>
    </tr>
    <tr>
      <td><strong>Switchgear Clearance Reduction</strong></td>
      <td>Zero: Cannot be used to reduce electrical air clearances.</td>
      <td>Minimal: Lack of consistent dielectric certification limits design.</td>
      <td><strong>Up to 50% Reduction: Tested to permit compact phase spacing.</strong></td>
    </tr>
    <tr>
      <td><strong>Thermal Overload &amp; Melting Resistance</strong></td>
      <td>Poor: Melts and drips at temperatures above 105°C.</td>
      <td>Moderate: Softens under busbar continuous operating heat.</td>
      <td><strong>Cross-Linked Matrix: Non-melting; withstands 250°C short-circuit peaks.</strong></td>
    </tr>
    <tr>
      <td><strong>Installation Versatility in the Field</strong></td>
      <td>Requires pre-assembly; difficult over wide rectangular bars.</td>
      <td>Requires factory chemical dipping tanks; impossible on-site.</td>
      <td><strong>Fast Field Installation: Slips over busbars; shrinks in minutes with hot air gun.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

BST_FR = dict(
    lang='fr',
    dir='ltr',
    slug='switchgear-insulation-what-is-a-busbar-heat-shrink-tube-fr',
    title='Isolation des Jeux de Barres : Qu\'est-ce qu\'une Gaine Thermorétractable pour Barres en Cuivre ?',
    breadcrumb='Jeux de Barres &amp; Gaines d\'Isolation Thermorétractables',
    read='10 min de lecture',
    alt='Gaines thermorétractables d\'isolation en polyoléfine réticulée (Série MPBS) rétractées sur des barres de cuivre moyenne tension dans un tableau électrique',
    desc=('Cellules HTA, tableaux de distribution compacts, centres de contrôle de moteurs (MCC) et gaines à barres : Qu\'est-ce qu\'une gaine thermorétractable pour jeux de barres ? '
          'Polyoléfine réticulée sous rayonnement, coefficient de rétreint 2:1, rigidité diélectrique (> 25 kV/mm) et réduction jusqu\'à 50% des distances d\'isolement dans l\'air.'),
    model='Série MPBS / WRSBG : Gaines Thermorétractables Moyenne Tension pour Jeux de Barres 1kV, 10kV, 24kV, 36kV (Rétreint 2:1 / 2.5:1, Rigidité > 25 kV/mm, UL 224 / CEI 60068)',
    category='Jeux de Barres & Gaines d\'Isolation Thermorétractables / Gaines Thermorétractables HTA',
    kw='gaine thermoretractable pour barre de cuivre &middot; busbar heat shrink tube &middot; gaine isolation jeu de barres &middot; gaine thermoretractable 24kv &middot; gaine hta 36kv &middot; gaine mpbs',
    specs=[
        ('Polymère de Base et Réticulation', 'Polyoléfine ignifugée haute performance réticulée sous faisceau d\'électrons (Sans halogène, faible émission de fumée)'),
        ('Classes de Tension Assignée d\'Isolement', 'Gamme normalisée : 1 kV (BT), 10 kV / 12 kV, 24 kV et 36 kV / 40.5 kV (Jeux de barres HTA en cellules fermées)'),
        ('Coefficient de Rétreint Radial d\'Origine', 'Rapport de rétreint standard : 2:1 et 2.5:1 (Épouse parfaitement les barres rectangulaires, coudes et sections rondes)'),
        ('Températures de Rétreint et de Récupération', 'Début de rétreint : $\ge 85^\circ\text{C}$ ; Rétraction complète élastique : $\ge 120^\circ\text{C}$ (Pose rapide au pistolet thermique)'),
        ('Rigidité Diélectrique et Tenue en Tension', 'Rigidité diélectrique certifiée : $\ge 25\,\text{kV/mm}$ (Tenue à fréquence industrielle $1\,\text{min}$ jusqu\'à $80\,\text{kV}$)'),
        ('Endurance Thermique Continue en Service', 'Plage de température de fonctionnement : $-55^\circ\text{C}$ à $+125^\circ\text{C}$ (Essai de vieillissement 168h à $150^\circ\text{C}$)'),
        ('Comportement au Feu et Auto-Extinguibilité', 'Conforme à UL 224 VW-1 ; Indice d\'oxygène $\ge 30\%$ ; Auto-extinguible en moins de 15 secondes sans égouttement'),
        ('Conformité aux Normes Internationales', 'Certifié et conforme aux normes CEI 60068, UL 224, ASTM D2671 et spécifications de tenue diélectrique en armoires')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Gaine Thermorétractable pour Jeux de Barres et pourquoi est-elle indispensable ?',
         'Une Gaine Thermorétractable pour Jeux de Barres—également appelée gaine d\'isolation pour barres en cuivre HTA ou manchon thermorétractable polyoléfine—est '
         'une gaine isolante épaisse extrudée à partir de polyoléfine réticulée sous rayonnement d\'électrons. '
         'Dans les tableaux de distribution électrique et cellules de transformateurs : '
         '<ul>'
         '<li><strong>Prévention des Déflagrations d\'Arc Électrique (Arc-Flash) :</strong> Les barres en cuivre nu non isolées sont exposées aux risques '
         'de courts-circuits accidentels. L\'intrusion de rongeurs, la condensation ou la chute d\'outils peuvent ponter l\'espace d\'air entre deux phases, '
         'provoquant instantanément une explosion par arc électrique de plusieurs mégawatts. La gaine forme une armure diélectrique hermétique empêchant tout amorçage.</li>'
         '<li><strong>Réduction des Distances d\'Isolement (Jusqu\'à 50%) :</strong> Les normes de sécurité exigent d\'importantes distances d\'air entre barres nues '
         '(plus de 200 mm sous 24 kV). L\'isolation par gaine YOMIN MPBS permet de <strong>réduire de moitié les distances entre phases et par rapport à la masse</strong>, '
         'ce qui permet aux tableautiers de construire des armoires électriques ultra-compactes, d\'économiser de l\'espace au sol et d\'abaisser les coûts d\'enveloppe.</li>'
         '</ul>'),
        ('Quels sont les avantages de la réticulation sous faisceau d\'électrons ?',
         'Les polymères thermoplastiques ordinaires fondent dès que la température dépasse 90°C. '
         'La réticulation sous rayonnement d\'électrons crée des liaisons covalentes transversales entre les chaînes moléculaires de la polyoléfine, '
         'la transformant en un élastomère indéformable. Même en cas de surcharge thermique continue des barres ($105^\circ\text{C}$) '
         'ou de pic de court-circuit ($250^\circ\text{C}$), la gaine YOMIN ne fond pas, ne s\'égoutte pas et conserve 100% de sa rigidité diélectrique.'),
        ('Quelle est la différence entre une gaine pour barres et une gaine thermorétractable mince classique ?',
         'La gaine mince classique (0,3 à 0,5 mm) est conçue pour le repérage de câbles basse tension et se déchire sur les arêtes vives du cuivre. '
         'La <strong>gaine pour jeux de barres YOMIN MPBS</strong> présente une épaisseur robuste (2,0 à 4,5 mm après rétraction), '
         'spécialement formulée pour résister à des contraintes diélectriques de 10kV, 24kV et 36kV et certifiée pour réduire les distances dans l\'air.')
    ],
    cta='Vous concevez des cellules HTA compactes, des tableaux de distribution industrielle, des liaisons de transformateurs ou des gaines à barres nécessitant des gaines thermorétractables certifiées CEI 60068 / UL 224 (1kV à 36kV, tenue > 25kV/mm, réduction des distances jusqu\'à 50%) ? YOMIN fabrique des gaines série MPBS de haute précision.',
    body='''
<h2>Le Blindage Diélectrique pour Cellules Électriques Compactes et Prévention des Arcs</h2>
<p>Dans les postes de distribution d\'énergie électrique, les cellules HTA de moyenne tension, les tableaux généraux basse tension et les centres de commande de moteurs, les barres en cuivre et en aluminium transportent de fortes puissances sous des tensions de <strong>1kV jusqu\'à 36kV</strong>.</p>
<p>Pour réduire l\'encombrement au sol des postes et abaisser le coût de fabrication des enveloppes métalliques, les tableautiers conçoivent des cellules de plus en plus étroites.</p>
<p>Cependant, le resserrement des barres nues crée un risque critique d\'amorçage diélectrique : la moindre poussière conductrice, une humidité de condensation ou un animal nuisible franchissant la distance d\'air déclenche un arc électrique dévastateur qui détruit l\'armoire.</p>
<p>La <strong>Gaine Thermorétractable Moyenne Tension pour Jeux de Barres (Séries MPBS / WRSBG)</strong> apporte la solution technique absolue : un manchon en polyoléfine réticulée qui se moule parfaitement sur les barres droites ou coudées, doublant la tenue diélectrique et permettant de réduire de 50% les distances d\'isolement dans l\'air.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série MPBS</h2>
<ol>
  <li><strong>Polyoléfine Réticulée sous Rayonnement Électronique :</strong> Structure moléculaire tridimensionnelle empêchant toute fusion, écoulement ou fissuration sous contrainte thermique intense jusqu\'à $200^\circ\text{C}$.</li>
  <li><strong>Coefficient de Rétreint Élargi (2:1 à 2,5:1) :</strong> Rétraction uniforme épousant les barres rectangulaires et les coudes à 90 degrés sans pliure ni amincissement des arêtes.</li>
  <li><strong>Rigidité Diélectrique Exceptionnelle (&ge; 25 kV/mm) :</strong> Protection diélectrique sans faille assurant l\'isolation complète entre phases et par rapport à la masse métallique des cellules.</li>
  <li><strong>Ignifugation et Écologie Sans Halogène (UL 224 VW-1) :</strong> Matériau auto-extinguible s\'éteignant en quelques secondes sans dégagement de gaz acides corrosifs ni gouttes incandescentes.</li>
  <li><strong>Pose Facile et Immédiate sur Chantier :</strong> S\'enfile simplement sur la barre de cuivre et se rétracte en quelques minutes à l\'aide d\'un décapeur thermique standard.</li>
</ol>
'''
)

BST_ES = dict(
    lang='es',
    dir='ltr',
    slug='switchgear-insulation-what-is-a-busbar-heat-shrink-tube-es',
    title='Aislamiento de Barras Colectoras: ¿Qué es un Tubo Termorretráctil para Barras (Busbar Heat Shrink)?',
    breadcrumb='Barras Colectoras y Aislamientos Termorretráctiles',
    read='10 min de lectura',
    alt='Tubos termorretráctiles de poliolefina reticulada (Serie MPBS) termoencogidos sobre barras colectoras de cobre de media tensión en un tablero eléctrico',
    desc=('Celdas de media tensión, tableros compactos de distribución, centros de control de motores (MCC) y electroductos: ¿Qué es un tubo termorretráctil para barras colectoras? '
          'Poliolefina reticulada por radiación, relación de encogimiento 2:1, rigidez dieléctrica (> 25 kV/mm) y reducción de hasta un 50% en las distancias de aislamiento en aire.'),
    model='Serie MPBS / WRSBG: Tubos Termorretráctiles de Media Tensión para Barras Colectoras 1kV, 10kV, 24kV, 36kV (Encogimiento 2:1 / 2.5:1, Rigidez > 25 kV/mm, UL 224 / IEC 60068)',
    category='Barras Colectoras y Aislamientos Termorretráctiles / Tubos Termorretráctiles para Barras',
    kw='tubo termorretractil para barra de cobre &middot; busbar heat shrink tube &middot; funda termorretractil barras &middot; tubo termorretractil 24kv &middot; funda media tension 36kv &middot; tubo mpbs',
    specs=[
        ('Polímero Base y Reticulación por Radiación', 'Poliolefina retardante a la llama estabilizada térmicamente reticulada por haz de electrones (Libre de halógenos, baja emisión de humos)'),
        ('Clases de Tensión Nominal de Aislamiento', 'Gama disponible: 1 kV (BT), 10 kV / 12 kV, 24 kV y 36 kV / 40.5 kV (Barras colectoras de subestaciones y celdas HTA)'),
        ('Relación de Encogimiento Radial Nominal', 'Relación estándar: 2:1 y 2.5:1 (Se adapta perfectamente sobre barras rectangulares, curvas en 90° y barras redondas)'),
        ('Temperaturas de Inicio y Contracción Total', 'Inicio de encogimiento: $\ge 85^\circ\text{C}$ ; Recuperación elástica completa: $\ge 120^\circ\text{C}$ (Instalación rápida con pistola de calor)'),
        ('Rigidez Dieléctrica y Tensión de Ruptura', 'Rigidez dieléctrica ensayada: $\ge 25\,\text{kV/mm}$ (Soporta ensayo a frecuencia industrial $1\,\text{min}$ hasta $80\,\text{kV}$)'),
        ('Resistencia Térmica Continua de Operación', 'Rango térmico de servicio continuo: $-55^\circ\text{C}$ a $+125^\circ\text{C}$ (Ensayado por envejecimiento a $150^\circ\text{C}$ durante 168h)'),
        ('Retardancia a la Llama y Autoextinguibilidad', 'Cumple norma UL 224 VW-1 ; Índice de oxígeno $\ge 30\%$ ; Autoextinguible en menos de 15 segundos sin goteo de partículas'),
        ('Conformidad con Normativas Internacionales', 'Probado y certificado bajo normas internacionales IEC 60068, UL 224, ASTM D2671 y estándares de aislamiento de tableros')
    ],
    faqs=[
        ('¿Qué es un Tubo Termorretráctil para Barras Colectoras y por qué es esencial en celdas de media tensión?',
         'Un Tubo Termorretráctil para Barras (Busbar Heat Shrink Tubing)—conocido también como funda termorretráctil para barras de cobre o manga aislante de media tensión—es '
         'un tubo aislante de pared gruesa extruido a partir de poliolefina reticulada mediante haz de electrones de alta energía. '
         'En subestaciones de distribución y tableros eléctricos : '
         '<ul>'
         '<li><strong>Prevención de Explosiones por Arco Eléctrico (Arc-Flash):</strong> Las barras de cobre desnudas dentro de un tablero son vulnerables '
         'a cortocircuitos accidentales provocados por roedores, condensación de humedad o herramientas caídas que puentean el aire entre fases. '
         'El tubo termorretráctil forma una envoltura dieléctrica impenetrable que elimina totalmente el riesgo de flameo o chispa accidental.</li>'
         '<li><strong>Reducción de Distancias de Aislamiento (Hasta 50%):</strong> Las normas eléctricas exigen grandes espacios libres en aire entre barras desnudas '
         '(más de 200 mm a 24 kV). Aislar las barras con tubo YOMIN MPBS permite <strong>reducir hasta en un 50% las distancias entre fases y con respecto a tierra</strong>, '
         'permitiendo a los fabricantes diseñar celdas ultracompactas, ahorrar espacio en sala eléctrica y abaratar costos de fabricación.</li>'
         '</ul>'),
        ('¿Por qué la reticulación por radiación supera a los plásticos convencionales?',
         'Los plásticos termoplásticos comunes se derriten cuando la temperatura de las barras supera los 90°C. '
         'La reticulación por haz de electrones enlaza transversalmente las moléculas del polímero convirtiéndolo en un material termoestable elastomérico. '
         'Bajo calentamiento continuo a plena carga ($105^\circ\text{C}$) o sobrecorrientes momentáneas de cortocircuito ($250^\circ\text{C}$), '
         'el tubo YOMIN no se funde, no gotea y conserva el 100% de su capacidad aislante.'),
        ('¿Cuál es la diferencia entre un tubo termorretráctil para barras y un termocontraíble común?',
         'El termocontraíble común de pared delgada (0.3 a 0.5 mm) se emplea para cables de baja tensión (600V) y se rasga con los bordes filosos de las barras. '
         'El <strong>tubo para barras colectoras YOMIN MPBS</strong> posee un espesor grueso (2.0 a 4.5 mm recuperado), '
         'diseñado específicamente para soportar esfuerzos dieléctricos continuos de 10kV, 24kV y 36kV y reducir distancias en aire.')
    ],
    cta='¿Diseña celdas compactas de media tensión, tableros de distribución industrial, conexiones de transformadores o electroductos que requieren tubos termorretráctiles para barras certificados IEC 60068 / UL 224 (1kV a 36kV, rigidez > 25kV/mm, reducción de espacios de hasta el 50%)? YOMIN suministra tubos serie MPBS de máxima calidad.',
    body='''
<h2>La Armadura Dieléctrica para Celdas Compactas y Mitigación del Riesgo de Arc-Flash</h2>
<p>En el interior de subestaciones eléctricas de distribución, celdas compactas de media tensión, tableros generales y centros de control de motores, las barras colectoras de cobre y aluminio transportan elevadas corrientes en tensiones de <strong>1kV hasta 36kV</strong>.</p>
<p>Con el fin de optimizar el espacio físico en las salas eléctricas y reducir el costo de los gabinetes metálicos, los fabricantes de tableros buscan dimensiones cada vez más reducidas.</p>
<p>Sin embargo, acercar barras de cobre desnudas incrementa drásticamente el riesgo de descargas disruptivas : cualquier acumulación de polvo, condensación de humedad ambiental o ingreso de un animal crea un arco eléctrico violento que destruye el tablero por completo.</p>
<p>El <strong>Tubo Termorretráctil de Media Tensión para Barras Colectoras (Series MPBS / WRSBG)</strong> proporciona la solución técnica definitiva : una funda de poliolefina reticulada que se contrae de forma homogénea sobre barras rectas y curvas, duplicando el aislamiento dieléctrico y permitiendo reducir hasta un 50% las distancias de separación en aire.</p>

<h2>Elementos Constructivos y Ventajas de Ingeniería de la Serie MPBS</h2>
<ol>
  <li><strong>Poliolefina Reticulada por Radiación Electrónica:</strong> Estructura molecular tridimensional que evita la fusión, deformación o goteo del material ante sobrecargas térmicas extremas de hasta $200^\circ\text{C}$.</li>
  <li><strong>Relación de Encogimiento Ampliada (2:1 a 2.5:1):</strong> Se ajusta con perfecta uniformidad sobre barras rectangulares y curvas pronunciadas de 90 grados sin fisuras ni adelgazamiento en los vértices.</li>
  <li><strong>Rigidez Dieléctrica Excepcional (&ge; 25 kV/mm):</strong> Máxima seguridad que garantiza el aislamiento continuo entre fases y hacia la estructura metálica del tablero.</li>
  <li><strong>Retardante a la Llama Libre de Halógenos (UL 224 VW-1):</strong> Material autoextinguible que apaga el fuego en segundos sin liberar gases ácidos corrosivos ni humo denso.</li>
  <li><strong>Montaje Práctico y Rápido en Obra:</strong> Se desliza fácilmente sobre la barra de cobre y se encoge en pocos minutos mediante una pistola de aire caliente convencional.</li>
</ol>
'''
)

BST_AR = dict(
    lang='ar',
    dir='rtl',
    slug='switchgear-insulation-what-is-a-busbar-heat-shrink-tube-ar',
    title='عزل قضبان التوزيع الكهربائية: ما هو أنبوب الانكماش الحراري لقضبان البارات (Busbar Heat Shrink Tube)؟',
    breadcrumb='قضبان التوزيع وأنابيب العزل الحراري',
    read='10 دقائق قراءة',
    alt='أنابيب انكماش حراري من البولي أوليفين المعالج إشعاعياً (موديل MPBS) منكمشة على قضبان نحاسية للجهد المتوسط في لوحة كهربائية',
    desc=('خلايا الجهد المتوسط HTA، ولوحات التوزيع المدمجة، ومراكز التحكم في المحركات (MCC)، ومجاري البارات: ما هو أنبوب الانكماش الحراري لقضبان التوزيع (Busbar Heat Shrink Tube)؟ '
          'البولي أوليفين المتشابك إشعاعياً، ونسبة انكماش 2:1، وصمود ديإلكتريكي فائق (> 25 kV/mm)، وتقليص المسافات الهوائية بين الأوجه بنسبة تصل إلى 50% لمنع حوادث القوس الكهربائي.'),
    model='سلسلة MPBS / WRSBG: أنابيب الانكماش الحراري لعزل قضبان البارات للجهود 1kV و 10kV و 24kV و 36kV (نسبة انكماش 2:1 / 2.5:1، صمود > 25 kV/mm، معتمدة UL 224 / IEC 60068)',
    category='قضبان التوزيع وأنابيب العزل الحراري / أنابيب الانكماش الحراري للبارات',
    kw='انبوب انكماش حراري لقضبان التوزيع &middot; busbar heat shrink tube &middot; عزل بارات النحاس &middot; شيرينك بارات 24kv &middot; انبوب عازل 36kv &middot; شيرينك mpbs',
    specs=[
        ('البوليمر الأساسي والتشبيك الإشعاعي', 'بولي أوليفين مثبط للهب عالي الأداء معالج إشعاعياً بحزم الإلكترونات (خالٍ من الهالوجينات ومنخفض انبعاث الدخان)'),
        ('فئات جهود العزل الاسمي المقننة', 'الفئات القياسية: 1 كيلو فولت (جهد منخفض)، 10/12 كيلو فولت، 24 كيلو فولت، و 36/40.5 كيلو فولت (لقضبان الجهد المتوسط)'),
        ('نسبة الانكماش القطري الاسمي المعتمدة', 'نسبة انكماش قياسية: 2:1 و 2.5:1 (تنكمش بانسيابية تامة فوق البارات المستطيلة والمستديرة والانحناءات الزاوية 90°)'),
        ('درجات حرارة بدء الانكماش والتعافي التام', 'بدء الانكماش: $\ge 85^\circ\text{C}$؛ الانكماش المرن التام: $\ge 120^\circ\text{C}$ (تركيب سريع باستخدام مسدس الهواء الساخن)'),
        ('قوة ومتانة الصمود العازل الديزلكتريكي', 'صمود ديإلكتريكي فائق مختبر: $\ge 25\,\text{kV/mm}$ (تحمل جهد تردد الشبكة لمدة دقيقة كاملة حتى $80\,\text{kV}$)'),
        ('التحمل الحراري المستمر أثناء التشغيل', 'نطاق درجات حرارة الخدمة المستمرة: من $-55^\circ\text{C}$ حتى $+125^\circ\text{C}$ (اختبار التقادم الحراري عند $150^\circ\text{C}$ لمدة 168 ساعة)'),
        ('مقاومة اللهب وخاصية الإطفاء الذاتي', 'مطابق للمواصفة UL 224 VW-1؛ معامل الأكسجين $\ge 30\%$؛ إطفاء ذاتي تام في أقل من 15 ثانية دون أي تساقط لقطرات مشتعلة'),
        ('المطابقة للمواصفات والاعتمادات الدولية', 'مختبر ومعتمد بالكامل وفقاً للمعايير الدولية IEC 60068 و UL 224 و ASTM D2671 واشتراطات عزل اللوحات الكهربائية')
    ],
    faqs=[
        ('ما هو أنبوب الانكماش الحراري لقضبان البارات (Busbar Heat Shrink Tube) ولماذا يعتبر حاسماً في اللوحات الكهربائية؟',
         'أنبوب الانكماش الحراري لقضبان البارات—والمعروف في هندسة تصنيع اللوحات باسم شيرينك بارات النحاس أو عازل البارات الحراري—هو '
         'أنبوب عازل سميك الجدار مُصنع من بوليمر البولي أوليفين المعالج بتقنية التشبيك الإشعاعي الإلكتروني. '
         'وفي لوحات التوزيع ومحطات التحويل الكهربائية : '
         '<ul>'
         '<li><strong>منع حوادث القوس الكهربائي المتفجر (Arc-Flash):</strong> قضبان النحاس العارية داخل اللوحات تكون معرضة لأعطال قصر فتاكة '
         'بسبب دخول القوارض (الفئران، الزواحف) أو تساقط قطرات الرطوبة والتكثيف التي تصل بين الأوجه الحية، مما يطلق انفجاراً نارياً هائلاً. '
         'يوفر أنبوب الشيرينك درعاً عازلاً متصلاً يمنع أي تلامس أو شرارة حتى عند ملامسة جسم غريب للبارة مباشرة.</li>'
         '<li><strong>تقليص المسافات الهوائية بين الأوجه بنسبة 50%:</strong> تفرض معايير السلامة مسافات هوائية واسعة بين البارات العارية '
         '(أكثر من 200 مم عند جهد 24kV). ويتيح عزل البارات بأنابيب يمين MPBS <strong>تقليل المسافات المطلوبة بنسبة تصل إلى 50%</strong>، '
         'مما يتيح لمصنعي اللوحات تصنيع خلايا توزيع مدمجة الحجم توفر مساحات المباني وتخفض تكاليف الحديد والأغلفة المعدنية.</li>'
         '</ul>'),
        ('ما هي المزايا الفنية للتشبيك الإشعاعي بحزم الإلكترونات؟',
         'تذوب اللدائن البلاستيكية العادية وتتحول إلى سائل بمجرد تجاوز الحرارة 90 درجة مئوية. '
         'بينما يقوم التشبيك الإشعاعي بربط السلاسل الجزيئية للبولي أوليفين بروابط تساهمية قوية تجعله مادة مطاطية لا تذوب مطلقاً. '
         'وتحت حرارة التشغيل المستمرة ($105^\circ\text{C}$) أو تيارات القصر اللحظية العنيفة ($250^\circ\text{C}$)، '
         'يحتفظ أنبوب يمين بمرونته الكاملة وصموده الديزلكتريكي دون أي انصهار أو تساقط للقطرات.'),
        ('ما هو الفارق بين أنبوب عزل البارات وأنبوب الشيرينك العادي الرقيق؟',
         'صُمم الشيرينك العادي ذو الجدار الرقيق (0.3 إلى 0.5 مم) لعزل أسلاك الجهد المنخفض (600V) ويتمزق بسهولة عند حواف النحاس الحادة. '
         'بينما يتميز <strong>أنبوب يمين MPBS لعزل البارات</strong> بجدار سميك ومتين (من 2.0 إلى 4.5 مم بعد الانكماش)، '
         'مُصمم خصيصاً ليتحمل إجهادات جهود 10kV و 24kV و 36kV المستمرة ومعتمد لتقليص المسافات الهوائية بين الأوجه.')
    ],
    cta='هل تعمل على تصنيع خلايا الجهد المتوسط المدمجة، أو لوحات التوزيع الصناعية، أو وصلات محولات التغذية التي تتطلب أنابيب انكماش حراري لعزل البارات معتمدة IEC 60068 / UL 224 (جهود 1kV إلى 36kV، صمود عزل > 25kV/mm، تقليص مسافات بنسبة 50%)؟ تصنع يمين (YOMIN) أنابيب سلسلة MPBS بأعلى معايير الجودة.',
    body='''
<h2>الدرع الديزلكتريكي المنيع للوحات الكهربائية المدمجة والوقاية من أخطار القوس الكهربائي</h2>
<p>في محطات توزيع الطاقة الكهربائية، وخلايا الجهد المتوسط، ولوحات التوزيع الصناعية الرئيسية، ومراكز التحكم في المحركات، تنقل قضبان النحاس والألمنيوم تيارات هائلة بجهود تتراوح بين <strong>1 كيلو فولت وتصل إلى 36 كيلو فولت</strong>.</p>
<p>ومن أجل تقليص المساحات المشغولة وتخفيض تكاليف تصنيع الهياكل المعدنية، يتجه مهندسو تصنيع اللوحات إلى تصميم خلايا مدمجة ونحيفة للغاية.</p>
<p>ومع ذلك، فإن تقارب البارات النحاسية العارية يخلق خطراً داهماً: فأي تجمع للغبار أو تكثف لقطرات الرطوبة أو دخول كائن حي عابر يقفز عبر الفجوة الهوائية، مشعلاً قوساً كهربائياً انفجارياً مدمراً يدمر اللوحة برمتها.</p>
<p>يوفر <strong>أنبوب الانكماش الحراري لعزل قضبان البارات للجهد المتوسط (سلسلة MPBS / WRSBG)</strong> الحل الهندسي الجذري الحاسم: غلاف بولي أوليفين متطور معالج إشعاعياً ينكمش بإحكام تام فوق البارات المستقيمة والمنحنية، مضاعفاً العزل الكهربائي ومتيحاً تقليص المسافات الهوائية بين الأوجه بنسبة 50% بأمان تام.</p>

<h2>المكونات الهندسية وميزات التصميم لسلسلة أنابيب MPBS</h2>
<ol>
  <li><strong>بولي أوليفين متشابك إشعاعياً بحزم الإلكترونات:</strong> بنية جزيئية ثلاثية الأبعاد تمنع أي ذوبان أو تشوه تحت درجات الحرارة العالية التي تتجاوز $200^\circ\text{C}$.</li>
  <li><strong>نسبة انكماش قطري مرنة ومتسعة (2:1 إلى 2.5:1):</strong> تنكمش بنعومة وتماسك فوق البارات المستطيلة والانحناءات الزاوية 90 درجة دون أي تشققات في الحواف.</li>
  <li><strong>صمود ديإلكتريكي فائق (&ge; 25 kV/mm):</strong> حماية ديإلكتريكية استثنائية تضمن العزل الكامل بين الأوجه الحية وعن الهياكل المعدنية المؤرضة.</li>
  <li><strong>مقاومة تامة للاشتعال وخلو من الهالوجين (UL 224 VW-1):</strong> مادة ذاتية الإطفاء تنطفئ فورياً دون إصدار غازات حمضية سامة أو قطرات مشتعلة.</li>
  <li><strong>تركيب فوري وسهل في الموقع:</strong> تنزلق الأنبوبة بسهولة فوق بارات النحاس وتنكمش في دقائق معدودة باستخدام مسدس الهواء الساخن القياسي.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1018B = [
    LBS_EN, LBS_FR, LBS_ES, LBS_AR,
    BST_EN, BST_FR, BST_ES, BST_AR
]
