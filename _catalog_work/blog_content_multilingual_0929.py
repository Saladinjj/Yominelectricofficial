# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-09-29:
1. Moulded Case Circuit Breaker (MCCB) (EN, FR, ES, AR)
2. Motor Protection Circuit Breaker (MPCB) (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. MOULDED CASE CIRCUIT BREAKER (MCCB) (EN, FR, ES, AR)
# ==============================================================================

MCCB_EN = dict(
    lang='en',
    dir='ltr',
    slug='industrial-circuit-protection-what-is-a-moulded-case-circuit-breaker',
    title='Industrial Circuit Protection & Sizing: What Is a Moulded Case Circuit Breaker (MCCB)?',
    breadcrumb='Fuse &amp; Protection',
    read='10 min read',
    alt='Heavy-duty three-phase Moulded Case Circuit Breaker installed inside an industrial low-voltage main distribution panelboard',
    desc=('Industrial power distribution and feeder protection: What is a moulded case circuit breaker (MCCB)? '
          'How heavy-duty MCCBs provide adjustable thermal overload protection, high-breaking-capacity electromagnetic short-circuit trip up to 100kA, and electronic trip coordination.'),
    model='Model YMM1 / YMM2 Series Thermal-Magnetic & Electronic Moulded Case Circuit Breakers',
    category='Fuse & Protection / Moulded Case Circuit Breakers',
    kw='what is moulded case circuit breaker &middot; mccb &middot; moulded case circuit breaker &middot; what is an mccb &middot; mccb sizing &middot; circuit breaker trip unit',
    specs=[
        ('Rated Operational Current (In)', '16A, 25A, 32A, 40A, 50A, 63A, 80A, 100A, 125A, 160A, 200A, 250A, 315A, 400A, 500A, 630A, 800A, 1000A, 1250A, 1600A frame sizes'),
        ('Number of Poles', '3-Pole (3P for 3-phase 3-wire industrial motor/feeder circuits) and 4-Pole (4P with 100% or 50% neutral protection for 3-phase 4-wire commercial distribution)'),
        ('Rated Insulation & Operational Voltage', 'Ui 800V AC / 1000V AC; Ue 400V / 415V / 690V AC (50/60Hz); DC applications up to 1000V DC for battery storage and solar inverters'),
        ('Ultimate Short-Circuit Breaking Capacity (Icu)', 'Standard Economical (S: 25kA–35kA), High-Breaking (H: 50kA–70kA), and Ultra-High Current Limiting (R: 85kA–100kA at 400V AC)'),
        ('Trip Unit Technologies', 'Thermal-Magnetic Fixed (TMD), Thermal Adjustable / Magnetic Fixed (ATFM), and Intelligent Microprocessor Electronic Trip Unit (ETU / Micrologic)'),
        ('Protection Adjustments & Settings', 'Long-Time Overload Pick-up (Ir = 0.7 to 1.0 In), Short-Time Short-Circuit Delay (Isd = 1.5 to 10 Ir), and Instantaneous Short-Circuit (Ii = 10 to 12 In)'),
        ('Installation & Mounting Formats', 'Fixed front-connection mounting, plug-in base, and withdrawable (draw-out) cradle format with mechanical safety interlocks'),
        ('Applicable International Standards', 'IEC 60947-2 (Low-voltage switchgear and controlgear - Circuit-breakers), EN 60947-2, GB/T 14048.2, CE certified, RoHS compliant')
    ],
    faqs=[
        ('What is a Moulded Case Circuit Breaker (MCCB) and how does it differ from a standard Miniature Circuit Breaker (MCB)?',
         'A Moulded Case Circuit Breaker (MCCB) is an industrial-grade electrical protection device housed in an injection-molded, arc-resistant thermoset glass-reinforced '
         'polyester casing. While both MCBs and MCCBs protect against overloads and short circuits, they operate at fundamentally different tiers: '
         '1. **Current Rating:** MCBs typically top out at 63A or 125A with fixed thermal ratings, whereas MCCBs protect high-current feeders from 16A up to 1600A. '
         '2. **Short-Circuit Interrupting Capacity:** Standard MCBs interrupt 6kA to 10kA fault currents; industrial MCCBs feature massive de-ionizing arc chutes that safely '
         'interrupt violent prospective faults from 25kA up to 100kA. '
         '3. **Adjustability:** MCBs have non-adjustable, factory-fixed trip curves (B, C, D curves). MCCBs feature adjustable thermal dials (typically 0.7x to 1.0x In) '
         'or digital microprocessor trip units, allowing electrical engineers to dial in precise discrimination and selective coordination across upstream and downstream boards.'),
        ('What is the difference between thermal-magnetic and electronic trip units in an MCCB?',
         'An MCCB can be equipped with either of two core trip unit technologies: '
         '<ul>'
         '<li><strong>Thermal-Magnetic Trip Unit (TMD):</strong> Relies on mechanical physics. A bimetallic strip bends under resistive heat to trip overloads, '
         'and an electromagnetic coil pulls a mechanical plunger during high-current short circuits. It is cost-effective, robust, and impervious to electromagnetic interference (EMI).</li>'
         '<li><strong>Electronic Trip Unit (ETU):</strong> Utilizes internal current sensors (Rogowski coils or iron-core CTs) paired with a microprocessor logic controller. '
         'It measures true RMS current, provides precise digital dial or LCD adjustments for LSI/LSIG curves (Long-time, Short-time delay, Instantaneous, and Ground fault protection), '
         'and enables Modbus RS485 communication for smart switchboard telemetry.</li>'
         '</ul>'),
        ('What do the ratings Icu and Ics mean when specifying an industrial MCCB?',
         'Under standard IEC 60947-2, short-circuit interrupting ratings are specified by two critical parameters: '
         '1. **Icu (Ultimate Short-Circuit Breaking Capacity):** The absolute maximum short-circuit current that the MCCB can successfully interrupt at rated voltage. '
         'Following an Icu test sequence (Open - Time Delay - Close/Open: O-t-CO), the breaker is permitted to suffer internal contact erosion and may require replacement. '
         '2. **Ics (Service Short-Circuit Breaking Capacity):** The fault level that the breaker can clear repeatedly (O-t-CO-t-CO) without losing its ability to carry continuous '
         'rated current and provide ongoing overload protection. Premium industrial MCCBs feature an **Ics = 100% Icu** rating, guaranteeing full operational continuity '
         'after clearing major switchgear faults.')
    ],
    cta='Designing low-voltage main switchboards, motor control centers (MCC), or commercial facility distribution boards requiring certified 16A to 1600A moulded case circuit breakers? YOMIN manufactures heavy-duty thermal-magnetic and electronic MCCBs tested to IEC 60947-2.',
    body='''
<h2>The Backbone of Industrial Electrical Distribution</h2>
<p>In modern industrial manufacturing plants, commercial high-rise towers, and utility distribution substations, electrical faults carry catastrophic energy. A short circuit occurring directly downstream of a 1000 kVA or 2000 kVA distribution transformer can unleash prospective fault currents exceeding 35,000 to 65,000 amperes in less than three milliseconds.</p>
<p>Small domestic Miniature Circuit Breakers (MCBs) would vaporize instantly under such severe electromagnetic forces. Industrial facilities require robust, arc-quenching circuit protection engineered to withstand and isolate massive fault currents while carrying hundreds of amperes continuously without thermal drift.</p>
<p>The <strong>Moulded Case Circuit Breaker (MCCB)</strong> serves as the foundational protective device for incoming mains, motor branch feeders, and heavy commercial distribution switchgear worldwide.</p>

<h2>Inside an MCCB: Heavy-Duty Architecture and Current Limiting</h2>
<p>Unlike consumer-grade plastic modular breakers, an industrial MCCB is constructed within a heavy-duty thermoset molded case capable of withstanding intense internal mechanical pressures, scorching arc plasma temperatures exceeding 6,000&deg;C, and extreme dielectric stresses:</p>
<ul>
  <li><strong>Rotary Double-Break Contact Mechanism:</strong> Advanced MCCBs employ rotary contact arms that leverage electrodynamic repulsion forces. When a severe short circuit occurs, the opposing magnetic fields generated by the fault current violently blow the contacts apart before the mechanical operating latch has even unlatched. This "current-limiting" action extinguishes the arc in under 4 milliseconds, dramatically reducing the I&sup2;t thermal stress let-through to downstream cables.</li>
  <li><strong>De-Ionizing Arc Splitter Chutes:</strong> A stack of insulated steel splitter plates positioned adjacent to the contact gap draws the expanding plasma arc inward, stretching it and cooling it across multiple series arcs. The metallic plates absorb heat, recombining ionized gas particles into non-conductive air within milliseconds.</li>
  <li><strong>Adjustable Trip Calibration:</strong> Front-accessible dials allow plant electrical engineers to fine-tune the thermal overload threshold (Ir) to match exact cable ampacities, eliminating nuisance trips caused by ambient summer heat while providing tight overload protection.</li>
</ul>

<h2>Comparison: MCB vs. MCCB vs. ACB</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>MCB (Miniature Circuit Breaker)</th>
      <th>MCCB (Moulded Case Circuit Breaker)</th>
      <th>ACB (Air Circuit Breaker)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Current Rating Range</strong></td>
      <td>0.5A to 125A</td>
      <td><strong>16A to 1600A</strong></td>
      <td>630A to 6300A</td>
    </tr>
    <tr>
      <td><strong>Breaking Capacity (Icu)</strong></td>
      <td>6kA to 10kA (rarely 15kA)</td>
      <td><strong>25kA to 100kA</strong></td>
      <td>50kA to 150kA</td>
    </tr>
    <tr>
      <td><strong>Trip Unit Adjustability</strong></td>
      <td>Fixed; non-adjustable curves.</td>
      <td><strong>Adjustable thermal & magnetic (or ETU).</strong></td>
      <td>Fully programmable digital microprocessor.</td>
    </tr>
    <tr>
      <td><strong>Mounting Architecture</strong></td>
      <td>35mm DIN-rail snap-on.</td>
      <td><strong>Baseplate bolted, plug-in, or withdrawable.</strong></td>
      <td>Draw-out cassette chassis with racking handle.</td>
    </tr>
    <tr>
      <td><strong>Primary Application Tier</strong></td>
      <td>Final sub-circuits (lighting/plugs).</td>
      <td><strong>Main distribution panels, feeders, motors.</strong></td>
      <td>Main incoming substation switchgear.</td>
    </tr>
  </tbody>
</table>
'''
)

MCCB_FR = dict(
    lang='fr',
    dir='ltr',
    slug='industrial-circuit-protection-what-is-a-moulded-case-circuit-breaker-fr',
    title="Protection des Circuits Industriels & Dimensionnement : Qu'est-ce qu'un Disjoncteur Boîtier Moulé (MCCB) ?",
    breadcrumb='Fusibles &amp; Protection',
    read='10 min de lecture',
    alt='Disjoncteur boîtier moulé triphasé industriel installé à l\'intérieur d\'un tableau de distribution principale basse tension',
    desc=('Distribution électrique industrielle et protection des départs : Qu\'est-ce qu\'un disjoncteur boîtier moulé (MCCB) ? '
          'Comment les disjoncteurs industriels assurent une protection thermique réglable, un pouvoir de coupure jusqu\'à 100kA et une sélectivité électronique.'),
    model='Série YMM1 / YMM2 : Disjoncteurs Boîtier Moulé Magnéto-Thermiques et Électroniques',
    category='Fusibles & Protection / Disjoncteurs Boîtier Moulé',
    kw='disjoncteur boîtier moulé &middot; mccb &middot; qu\'est-ce qu\'un mccb &middot; pouvoir de coupure icu &middot; déclencheur électronique &middot; protection tableau électrique',
    specs=[
        ('Courant Assigné d\'Emploi (In)', 'Calibres de 16A, 25A, 32A, 40A, 50A, 63A, 80A, 100A, 125A, 160A, 200A, 250A, 315A, 400A, 500A, 630A, 800A, 1000A, 1250A, 1600A'),
        ('Nombre de Pôles', '3 Pôles (3P pour départs moteurs et distribution industrielle) et 4 Pôles (4P avec neutre protégé 100% ou 50% pour réseaux tertiaires)'),
        ('Tension Assignée d\'Isolement & d\'Emploi', 'Ui 800V / 1000V AC ; Ue 400V / 415V / 690V AC (50/60Hz) ; versions continues jusqu\'à 1000V DC pour stockage solaire'),
        ('Pouvoir de Coupure Ultime (Icu)', 'Standard Économique (S : 25kA–35kA), Haut Pouvoir (H : 50kA–70kA) et Très Haut Pouvoir Limiteur (R : 85kA–100kA à 400V)'),
        ('Technologies de Déclencheurs', 'Magnéto-thermique fixe (TMD), Thermique réglable / magnétique fixe (ATFM) et Déclencheur électronique à microprocesseur (ETU)'),
        ('Plages de Réglage des Déclencheurs', 'Surcharge long retard (Ir = 0,7 à 1,0 In), Court-circuit court retard (Isd = 1,5 à 10 Ir) et Instantané (Ii = 10 à 12 In)'),
        ('Modes d\'Installation & Raccordement', 'Appareil fixe à prises avant, débrochable sur socle ou extractible sur châssis avec verrouillages mécaniques de sécurité'),
        ('Normes Internationales Applicables', 'CEI 60947-2 (Appareillage à basse tension - Disjoncteurs), EN 60947-2, certifié CE et conforme RoHS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un disjoncteur boîtier moulé (MCCB) et en quoi diffère-t-il d\'un disjoncteur modulaire (MCB) ?',
         'Un disjoncteur boîtier moulé (MCCB - Moulded Case Circuit Breaker) est un appareil de coupure et de protection industrielle logé dans un boîtier '
         'en résine polyester thermodurcissable renforcée de fibres de verre, capable de résister aux fortes contraintes thermiques et électrodynamiques. '
         'Les principales différences avec un disjoncteur modulaire résident dans : '
         '1. **Le calibre de courant :** Les disjoncteurs modulaires s\'arrêtent à 63A ou 125A, alors que les MCCB protègent les départs de 16A jusqu\'à 1600A. '
         '2. **Le pouvoir de coupure :** Un modulaire classique coupe 6kA à 10kA, tandis qu\'un MCCB intègre des chambres de coupure soufflant des arcs de 25kA à 100kA. '
         '3. **Le réglage du seuil :** Les modulaires ont des courbes fixes (B, C, D) ; les MCCB permettent d\'ajuster le seuil thermique (0,7 à 1,0 In) pour une sélectivité totale.'),
        ('Quelle est la différence entre un déclencheur magnéto-thermique et un déclencheur électronique ?',
         'Deux technologies principales équipent les disjoncteurs boîtier moulé : '
         '<ul>'
         '<li><strong>Déclencheur Magnéto-Thermique :</strong> Fonctionnement électromécanique robuste. Un bilame chauffe et fléchit pour déclencher la surcharge, '
         'tandis qu\'une bobine magnétique attire un plongeur en cas de court-circuit franc. Insensible aux perturbations électromagnétiques (CEM).</li>'
         '<li><strong>Déclencheur Électronique (ETU) :</strong> Intègre des capteurs de courant (tores de mesure) et un microprocesseur. Il mesure le courant RMS vrai, '
         'offre des réglages numériques très fins (LSI : Long retard, Court retard, Instantané), et communique en Modbus RS485 pour les tableaux connectés.</li>'
         '</ul>'),
        ('Que signifient les valeurs Icu et Ics sur la plaque signalétique d\'un disjoncteur MCCB ?',
         'Selon la norme CEI 60947-2, le comportement d\'un disjoncteur sur court-circuit est défini par deux valeurs fondamentales : '
         '1. **Icu (Pouvoir de coupure ultime) :** Courant maximal présumé que le disjoncteur peut interrompre sous sa tension nominale. Après l\'essai, l\'appareil peut être endommagé. '
         '2. **Ics (Pouvoir de coupure de service) :** Courant de court-circuit que le disjoncteur peut couper plusieurs fois sans dégradation de ses performances. '
         'Les disjoncteurs industriels de premier rang affichent un ratio **Ics = 100% Icu**, garantissant la continuité de service après incident.')
    ],
    cta='Vous dimensionnez des tableaux généraux basse tension (TGBT), des armoires d\'alimentation d\'usine ou des centres de contrôle moteurs nécessitant des disjoncteurs boîtier moulé de 16A à 1600A ? YOMIN fabrique des MCCB certifiés CEI 60947-2.',
    body='''
<h2>La Clé de Voûte de la Distribution Électrique Industrielle</h2>
<p>Dans les usines de fabrication, les hôpitaux et les centres de données, les courts-circuits libèrent une énergie destructrice considérable. Un défaut survenant immédiatement en aval d'un transformateur de 1000 kVA ou 1600 kVA engendre des courants de court-circuit crêtes de 35 000 à 65 000 ampères en moins de trois millisecondes.</p>
<p>Les disjoncteurs modulaires domestiques exploseraient instantanément sous l'effet de ces forces électrodynamiques colossales. Les installations industrielles exigent des disjoncteurs dotés de chambres de coupure massives capables d'éteindre l'arc électrique en toute sécurité.</p>
<p>Le <strong>Disjoncteur Boîtier Moulé (MCCB)</strong> constitue la protection essentielle des départs généraux, des colonnes montantes et des machines industrielles lourdes.</p>

<h2>Architecture Interne et Technologie Limitatrice de Courant</h2>
<p>Un disjoncteur MCCB industriel est conçu pour résister à des températures d'arc plasma dépassant 6 000&deg;C grâce à des composants haute technologie :</p>
<ul>
  <li><strong>Contacts Rotatifs à Double Coupure :</strong> Les MCCB modernes utilisent des bras de contact rotatifs dont l'ouverture est accélérée par les forces d'induction magnétiques du court-circuit (répulsion électrodynamique). Cette action ultra-rapide limite l'onde de choc et étouffe l'arc en moins de 4 millisecondes, protégeant ainsi les câbles aval contre les contraintes thermiques (I&sup2;t).</li>
  <li><strong>Chambres de Coupure Désionisantes :</strong> Un empilage de tôles d'acier magnétiques attire et fractionne l'arc électrique en multiples arcs élémentaires, refroidissant et neutralisant les gaz ionisés en quelques millisecondes.</li>
  <li><strong>Calibrage Thermique Réglable :</strong> Des molettes en face avant permettent d'ajuster le courant de déclenchement thermique (Ir) entre 70% et 100% du calibre pour s'adapter rigoureusement à la section des câbles.</li>
</ul>

<h2>Comparatif : Modulaire (MCB) vs. Boîtier Moulé (MCCB) vs. Ouvert (ACB)</h2>
<table>
  <thead>
    <tr>
      <th>Caractéristique Technique</th>
      <th>Disjoncteur Modulaire (MCB)</th>
      <th>Disjoncteur Boîtier Moulé (MCCB)</th>
      <th>Disjoncteur Ouvert (ACB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Plage de Calibre</strong></td>
      <td>0,5A à 125A</td>
      <td><strong>16A à 1600A</strong></td>
      <td>630A à 6300A</td>
    </tr>
    <tr>
      <td><strong>Pouvoir de Coupure (Icu)</strong></td>
      <td>6kA à 10kA (rarement 15kA)</td>
      <td><strong>25kA à 100kA</strong></td>
      <td>50kA à 150kA</td>
    </tr>
    <tr>
      <td><strong>Réglage des Déclencheurs</strong></td>
      <td>Fixe (courbes B, C, D).</td>
      <td><strong>Réglable thermique & magnétique (ou ETU).</strong></td>
      <td>Microprocesseur numérique programmable.</td>
    </tr>
    <tr>
      <td><strong>Type de Montage</strong></td>
      <td>Encliquetable sur rail DIN 35mm.</td>
      <td><strong>Fixe sur platine, débrochable, extractible.</strong></td>
      <td>Châssis extractible avec manivelle.</td>
    </tr>
    <tr>
      <td><strong>Domaine d'Application</strong></td>
      <td>Circuits terminaux d'éclairage et prises.</td>
      <td><strong>TGBT, départs divisionnaires, moteurs.</strong></td>
      <td>Arrivée générale transformateur / poste HT/BT.</td>
    </tr>
  </tbody>
</table>
'''
)

MCCB_ES = dict(
    lang='es',
    dir='ltr',
    slug='industrial-circuit-protection-what-is-a-moulded-case-circuit-breaker-es',
    title='Protección de Circuitos Industriales y Dimensionamiento: ¿Qué es un Disyuntor de Caja Moldeada (MCCB)?',
    breadcrumb='Fusibles y Protección',
    read='10 min de lectura',
    alt='Disyuntor de caja moldeada trifásico industrial instalado dentro de un tablero de distribución principal de baja tensión',
    desc=('Distribución eléctrica industrial y protección de alimentadores: ¿Qué es un disyuntor de caja moldeada (MCCB)? '
          'Cómo los disyuntores industriales proporcionan protección térmica ajustable, capacidad de ruptura de hasta 100kA y coordinación selectiva electrónica.'),
    model='Serie YMM1 / YMM2: Interruptores Termomagnéticos y Electrónicos de Caja Moldeada',
    category='Fusibles y Protección / Interruptores de Caja Moldeada',
    kw='disyuntor de caja moldeada &middot; mccb &middot; qué es un mccb &middot; capacidad de ruptura icu &middot; disparador electrónico &middot; protección de tableros industriales',
    specs=[
        ('Corriente Nominal Operativa (In)', 'Calibres de 16A, 25A, 32A, 40A, 50A, 63A, 80A, 100A, 125A, 160A, 200A, 250A, 315A, 400A, 500A, 630A, 800A, 1000A, 1250A, 1600A'),
        ('Número de Polos', '3 Polos (3P para circuitos de motores y distribución industrial) y 4 Polos (4P con neutro protegido 100% o 50% para instalaciones comerciales)'),
        ('Tensión Nominal de Aislamiento y Operación', 'Ui 800V / 1000V AC; Ue 400V / 415V / 690V AC (50/60Hz); versiones en corriente continua hasta 1000V DC para energía solar'),
        ('Poder de Corte Último en Cortocircuito (Icu)', 'Estándar Económico (S: 25kA–35kA), Alto Poder (H: 50kA–70kA) y Ultra-Alto Limitador (R: 85kA–100kA a 400V AC)'),
        ('Tecnologías de Unidad de Disparo', 'Termomagnético fijo (TMD), Térmico ajustable / magnético fijo (ATFM) y Disparador electrónico por microprocesador (ETU)'),
        ('Ajustes y Parámetros de Disparo', 'Sobrecarga de largo retardo (Ir = 0,7 a 1,0 In), Cortocircuito de corto retardo (Isd = 1,5 a 10 Ir) e Instantáneo (Ii = 10 a 12 In)'),
        ('Formatos de Montaje e Instalación', 'Fijo de conexión frontal, enchufable en base (plug-in) y extraíble sobre cuna con enclavamientos mecánicos de seguridad'),
        ('Normas Internacionales Aplicables', 'IEC 60947-2 (Aparamenta de baja tensión - Interruptores automáticos), EN 60947-2, certificado CE y cumplimiento RoHS')
    ],
    faqs=[
        ('¿Qué es un disyuntor de caja moldeada (MCCB) y en qué se diferencia de un termomagnético modular (MCB)?',
         'Un disyuntor de caja moldeada (MCCB - Moulded Case Circuit Breaker) es un interruptor automático para aplicaciones industriales encerrado en una carcasa '
         'de resina de poliéster termoestable reforzada con fibra de vidrio. Sus diferencias fundamentales con un interruptor modular pequeño (MCB) son: '
         '1. **Capacidad de corriente:** Los MCB cubren hasta 63A o 125A, mientras que los MCCB protegen alimentadores de 16A hasta 1600A. '
         '2. **Poder de corte:** Los MCB interrumpen entre 6kA y 10kA; los MCCB industriales incorporan cámaras de extinción de arco para 25kA hasta 100kA. '
         '3. **Ajuste de disparo:** Los MCB tienen curvas fijas de fábrica (B, C, D); los MCCB disponen de diales para calibrar el umbral térmico (0,7 a 1,0 In) '
         'y disparadores electrónicos para lograr una selectividad precisa entre tableros.'),
        ('¿Cuál es la diferencia entre un disparador termomagnético y uno electrónico en un MCCB?',
         'Los MCCB pueden incorporar dos tecnologías de detección: '
         '<ul>'
         '<li><strong>Disparador Termomagnético (TMD):</strong> Basado en principios electromecánicos. Una lámina bimetálica se dobla por calor ante sobrecargas, '
         'y una bobina magnética acciona un percutor ante cortocircuitos. Es robusto, confiable e inmune a interferencias electromagnéticas.</li>'
         '<li><strong>Disparador Electrónico (ETU):</strong> Utiliza sensores de corriente y un procesador interno. Mide corriente RMS real, ofrece regulación digital '
         'milimétrica de curvas LSI (Largo retardo, Corto retardo e Instantáneo) y permite comunicación Modbus RS485 para tableros inteligentes.</li>'
         '</ul>'),
        ('¿Qué representan los valores Icu e Ics en la placa de características de un MCCB?',
         'La norma IEC 60947-2 clasifica la capacidad de corte ante cortocircuitos mediante dos parámetros: '
         '1. **Icu (Poder de corte último):** La máxima corriente de falla que el interruptor puede cortar a su tensión nominal. Tras la prueba, puede requerir cambio. '
         '2. **Ics (Poder de corte en servicio):** El nivel de cortocircuito que el interruptor puede interrumpir repetidamente sin perder su capacidad operativa normal. '
         'Los interruptores industriales de máxima calidad ofrecen un valor **Ics = 100% Icu**, garantizando la continuidad de servicio tras despejar fallas graves.')
    ],
    cta='¿Diseña tableros de distribución general (TGBT), centros de control de motores o subestaciones comerciales que requieren disyuntores de caja moldeada de 16A a 1600A? YOMIN fabrica interruptores automáticos probados bajo norma IEC 60947-2.',
    body='''
<h2>El Pilar de la Distribución Eléctrica Industrial</h2>
<p>En complejos manufactureros, edificios corporativos y subestaciones eléctricas, los cortocircuitos liberan una energía destructiva masiva. Una falla inmediatamente posterior a un transformador de 1000 kVA o 2000 kVA puede generar corrientes de cortocircuito superiores a 35.000 o 65.000 amperios en menos de tres milisegundos.</p>
<p>Los disyuntores modulares pequeños quedarían destruidos instantáneamente ante tales esfuerzos electrodinámicos. Las plantas industriales demandan interruptores automáticos con robustas cámaras de soplado de arco diseñados para soportar y despejar fallas intensas con total seguridad.</p>
<p>El <strong>Disyuntor de Caja Moldeada (MCCB)</strong> es el dispositivo de protección fundamental para las acometidas principales, alimentadores de fuerza y maquinaria pesada en todo el mundo.</p>

<h2>Arquitectura y Tecnología de Limitación de Corriente</h2>
<p>Un disyuntor MCCB industrial está fabricado para soportar temperaturas de plasma superiores a 6.000&deg;C mediante tecnologías avanzadas de extinción:</p>
<ul>
  <li><strong>Contactos Rotativos de Doble Ruptura:</strong> Los MCCB de última generación emplean brazos de contacto rotativos accionados por las propias fuerzas de repulsión electrodinámica generadas por el cortocircuito. Esta acción ultrarrápida apaga el arco en menos de 4 milisegundos, reduciendo drásticamente el estrés térmico (I&sup2;t) sobre los cables del circuito.</li>
  <li><strong>Cámaras Desionizadoras de Arco:</strong> Láminas de acero magnético apiladas absorben el calor, estiran el plasma y enfrían los gases ionizados en pocos milisegundos.</li>
  <li><strong>Ajuste Térmico Calibrado:</strong> Diales frontales permiten regular la corriente nominal térmica (Ir) entre el 70% y el 100% del calibre para ajustarse exactamente a la capacidad de los cables alimentadores.</li>
</ul>

<h2>Tabla Comparativa: MCB vs. MCCB vs. ACB</h2>
<table>
  <thead>
    <tr>
      <th>Parámetro Técnico</th>
      <th>Termomagnético Modular (MCB)</th>
      <th>Disyuntor de Caja Moldeada (MCCB)</th>
      <th>Disyuntor Abierto de Potencia (ACB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Rango de Corriente</strong></td>
      <td>0,5A a 125A</td>
      <td><strong>16A a 1600A</strong></td>
      <td>630A a 6300A</td>
    </tr>
    <tr>
      <td><strong>Poder de Corte (Icu)</strong></td>
      <td>6kA a 10kA (raramente 15kA)</td>
      <td><strong>25kA a 100kA</strong></td>
      <td>50kA a 150kA</td>
    </tr>
    <tr>
      <td><strong>Regulación de Disparo</strong></td>
      <td>Fija de fábrica (curvas B, C, D).</td>
      <td><strong>Ajustable térmica y magnética (o ETU).</strong></td>
      <td>Microprocesador digital programable.</td>
    </tr>
    <tr>
      <td><strong>Tipo de Montaje</strong></td>
      <td>Riel DIN 35mm.</td>
      <td><strong>Fijo en placa, enchufable o extraíble.</strong></td>
      <td>Chasis extraíble sobre rieles con manivela.</td>
    </tr>
    <tr>
      <td><strong>Nivel de Aplicación</strong></td>
      <td>Circuitos terminales de iluminación y tomas.</td>
      <td><strong>Tableros principales, alimentadores, motores.</strong></td>
      <td>Acometida general de transformador / subestación.</td>
    </tr>
  </tbody>
</table>
'''
)

MCCB_AR = dict(
    lang='ar',
    dir='rtl',
    slug='industrial-circuit-protection-what-is-a-moulded-case-circuit-breaker-ar',
    title='حماية الدوائر الصناعية وتحديد السعات: ما هو القاطع المصبوب (MCCB)؟',
    breadcrumb='المصهرات والحماية',
    read='10 دقائق قراءة',
    alt='قاطع تيار كهربائي مصبوب ثلاثي الأطوار عالي التحمل مثبت داخل لوحة التوزيع الرئيسية الصناعية منخفضة الجهد',
    desc=('توزيع الطاقة الكهربائية وحماية الدوائر الصناعية: ما هو القاطع المصبوب (MCCB)؟ '
          'كيف توفر القواطع المصبوبة حماية حرارية قابلة للضبط، وسعة قطع عالية لتيارات القصر تصل إلى 100 كيلو أمبير، وتنسيقاً إلكترونياً دقيقاً.'),
    model='سلسلة YMM1 / YMM2: قواطع الدوائر المصبوبة الحرارية-المغناطيسية والإلكترونية',
    category='المصهرات والحماية / قواطع الدوائر المصبوبة',
    kw='قاطع مصبوب &middot; mccb &middot; ما هو القاطع المصبوب &middot; سعة كسر القاطع icu &middot; وحدة الفصل الإلكترونية &middot; لوحات التوزيع الصناعية',
    specs=[
        ('التيار التشغيلي الاسمي (In)', 'سعات تبدأ من 16A، 25A، 32A، 40A، 50A، 63A، 80A، 100A، 125A، 160A، 200A، 250A، 315A، 400A، 500A، 630A، 800A، 1000A، 1250A، وحتى 1600A'),
        ('عدد الأقطاب', 'ثلاثي الأقطاب (3P لتغذية المحركات والدوائر الصناعية) ورباعي الأقطاب (4P مع حماية كاملة 100% أو 50% لخط المحايد في المنشآت التجارية)'),
        ('جهد العزل والتشغيل الاسمي', 'جهد العزل Ui حتى 800V / 1000V؛ جهد التشغيل Ue حتى 400V / 415V / 690V؛ إصدارات مخصصة للتيار المستمر حتى 1000V DC لأنظمة الطاقة الشمسية'),
        ('سعة كسر تيار القصر القصوى (Icu)', 'فئة اقتصادية قياسية (S: 25kA–35kA)، فئة عالية (H: 50kA–70kA)، وفئة فائقة محددة للتيار (R: 85kA–100kA عند 400V)'),
        ('تقنيات وحدات الفصل (Trip Units)', 'حرارية-مغناطيسية ثابتة (TMD)، حرارية قابلة للضبط / مغناطيسية ثابتة (ATFM)، ووحدة فصل إلكترونية رقمية بالمعالج الدقيق (ETU)'),
        ('نطاقات ضبط وتعيين منحنيات الفصل', 'ضبط تيار الحمل الزائد طويل المدى (Ir = 0.7 إلى 1.0 In)، ضبط تيار القصر قصير المدى (Isd = 1.5 إلى 10 Ir)، والفصل اللحظي (Ii = 10 إلى 12 In)'),
        ('أنماط التركيب والتثبيت', 'تثبيت ثابت بأطراف أمامية، قابل للتوصيل المباشر (Plug-in)، وقابل للسحب الكامل (Withdrawable) مع أقفال ميكانيكية لأمان الصيانة'),
        ('المعايير الدولية المعتمدة', 'IEC 60947-2 (المفاتيح وأجهزة التحكم منخفضة الجهد - قواطع الدوائر)، EN 60947-2، شهادة CE وتوافق كامل مع معايير RoHS')
    ],
    faqs=[
        ('ما هو القاطع المصبوب (MCCB) وما هو الفرق الجوهري بينه وبين القاطع المصغر (MCB)؟',
         'القاطع المصبوب (Moulded Case Circuit Breaker - MCCB) هو قاطع دائرة كهربائي صناعي متين محاط بغلاف عازل مصبوب من البوليستر الحراري المقوى بالألياف الزجاجية '
         'المقاومة للأقواس الكهربائية والحرارة العالية. وتتمثل الفروق الجوهرية بينه وبين القاطع المصغر (MCB) في: '
         '1. **سعة التيار:** يقتصر القاطع المصغر على سعات تصل إلى 63 أو 125 أمبير، بينما يحمي القاطع المصبوب الدوائر ذات التيارات العالية من 16 أمبير وحتى 1600 أمبير. '
         '2. **سعة كسر تيار القصر:** تقطع القواطع المصغرة تيارات قصر بين 6kA و 10kA، بينما تحتوي القواطع المصبوبة على غرف إخماد قوية تقطع بأمان تيارات تتراوح بين 25kA و 100kA. '
         '3. **قابلية الضبط:** تتميز القواطع المصغرة بمنحنيات فصل ثابتة من المصنع، بينما تتيح القواطع المصبوبة إمكانية ضبط تيار الحمل الزائد (0.7 إلى 1.0 In) بدقة تامة.'),
        ('ما الفرق بين وحدة الفصل الحرارية-المغناطيسية ووحدة الفصل الإلكترونية في القاطع المصبوب؟',
         'يمكن تزويد القاطع المصبوب بإحدى تقنيتي فصل رئيسيتين: '
         '<ul>'
         '<li><strong>وحدة الفصل الحرارية-المغناطيسية (TMD):</strong> تعتمد على الخواص الكهروميكانيكية الفيزيائية؛ حيث ينثني شريط ثنائي المعدن تحت تأثير الحرارة لفصل الحمل الزائد، '
         'بينما يجذب ملف مغناطيسي ذراع الفصل عند حدوث تيار قصر مفاجئ. تتميز بالمتانة العالية ومقاومة التشويش الكهرومغناطيسي.</li>'
         '<li><strong>وحدة الفصل الإلكترونية (ETU):</strong> تعتمد على حساسات تيار مدمجة ومعالج دقيق. تقيس القيمة الفعالة الحقيقية للتيار (True RMS)، '
         'وتوفر ضبطاً رقمياً دقيقاً لمنحنيات الفصل (LSI)، مع دعم بروتوكولات الاتصال Modbus RS485 لربط اللوحات الذكية.</li>'
         '</ul>'),
        ('ماذا تعني رموز Icu و Ics المدونة على لوحة بيانات القاطع المصبوب؟',
         'وفقاً للمعيار الدولي IEC 60947-2، تُحدد قدرة القاطع على تحمل تيارات القصر بمعيارين حاسمين: '
         '1. **Icu (سعة القطع القصوى لتيار القصر):** أقصى تيار قصر يمكن للقاطع أن يفصله بنجاح عند الجهد الاسمي لمرة واحدة، وقد يتطلب القاطع استبداله بعد هذا الاختبار. '
         '2. **Ics (سعة القطع التشغيلية لتيار القصر):** مقدار تيار القصر الذي يستطيع القاطع فصله عدة مرات متتالية دون أن يفقد قدرته على مواصلة الخدمة العادية. '
         'وتتميز قواطع يمين (YOMIN) الصناعية بنسبة **Ics = 100% Icu**، مما يضمن استمرارية التغذية الكهربائية وموثوقية اللوحة بعد إزالة العطل.')
    ],
    cta='هل تصمم لوحات التوزيع الرئيسية منخفضة الجهد (TGBT) أو غرف التحكم في المحركات والمحطات الفرعية التي تتطلب قواطع مصبوبة معتمدة بسعات من 16 إلى 1600 أمبير؟ تصنع يمين (YOMIN) قواطع تيار مصبوبة متينة ومختبرة وفق معايير IEC 60947-2 الدولية.',
    body='''
<h2>العمود الفقري لأنظمة توزيع الطاقة الكهربائية الصناعية</h2>
<p>في المجمعات الصناعية الكبرى والمباني التجارية الشاهقة ومحطات التوليد الفرعية، تحمل الأعطال الكهربائية طاقة تدميرية هائلة. إذ يمكن لتيار القصر الكهربائي الناشئ مباشرة بعد محول توزيع بسعة 1000 أو 2000 كيلو فولت أمبير أن يطلق تيارات خطيرة تتجاوز 35,000 إلى 65,000 أمبير في أقل من ثلاثة أجزاء من الألف من الثانية.</p>
<p>تتعرض القواطع المصغرة العادية للتلف والانفجار اللحظي تحت وطأة هذه القوى الكهروديناميكية العنيفة. لذلك تتطلب المنشآت الصناعية قواطع حماية متخصصة ومصممة لتحمل وإخماد هذه التيارات الفائقة بأمان تام مع استمرار نقل التيارات التشغيلية العالية دون تأثر بحرارة الجو.</p>
<p>يعد <strong>القاطع المصبوب (MCCB)</strong> جهاز الحماية الأساسي المعتمد عالمياً لخطوط التغذية الرئيسية، والمحركات الكبيرة، ولوحات التوزيع الصناعية الكبرى.</p>

<h2>البنية الهندسية الداخلية وتقنية الحد من تيار القصر</h2>
<p>يُصنع القاطع المصبوب الصناعي ليتحمل حرارة البلازما المنبعثة من القوس الكهربائي والتي قد تتجاوز 6,000 درجة مئوية عبر تقنيات متقدمة لإخماد الشرر:</p>
<ul>
  <li><strong>آلية نقاط التلامس الدوارة مزدوجة الكسر:</strong> تعتمد القواطع المصبوبة الحديثة على أذرع تلامس دوارة تستفيد من قوى التنافر الكهروديناميكية الناتجة عن تيار القصر نفسه لدفع نقاط التلامس للتباعد في أقل من 4 أجزاء من الألف من الثانية، مما يحد بشدة من الطاقة الحرارية المارة إلى الكابلات.</li>
  <li><strong>غرف إخماد وتقسيم القوس الكهربائي:</strong> شرائح فولاذية مغناطيسية متراصة تعمل على جذب القوس وتفتيته إلى أقواس صغيرة متتالية، مما يبرد الغازات المتأينة ويخمدها في أجزاء من الثانية.</li>
  <li><strong>مفاتيح المعايرة الحرارية القابلة للضبط:</strong> تتيح الأقراص الدوارة الأمامية لمهندسي الكهرباء إمكانية ضبط تيار الفصل الحراري (Ir) بدقة بين 70% و100% من السعة الاسمية ليتطابق مع سعة الكابل المغذى بالضبط.</li>
</ul>

<h2>جدول مقارنة هندسي: القاطع المصغر (MCB) مقابل القاطع المصبوب (MCCB) مقابل القاطع الهوائي (ACB)</h2>
<table>
  <thead>
    <tr>
      <th>المعلمة الهندسية</th>
      <th>القاطع المصغر (MCB)</th>
      <th>القاطع المصبوب (MCCB)</th>
      <th>القاطع الهوائي (ACB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>نطاق السعة الاسمية</strong></td>
      <td>من 0.5A إلى 125A</td>
      <td><strong>من 16A إلى 1600A</strong></td>
      <td>من 630A إلى 6300A</td>
    </tr>
    <tr>
      <td><strong>سعة كسر القصر (Icu)</strong></td>
      <td>من 6kA إلى 10kA (نادراً 15kA)</td>
      <td><strong>من 25kA إلى 100kA</strong></td>
      <td>من 50kA إلى 150kA</td>
    </tr>
    <tr>
      <td><strong>إمكانية ضبط منحنيات الفصل</strong></td>
      <td>ثابتة من المصنع (منحنيات B, C, D).</td>
      <td><strong>حرارية ومغناطيسية قابلة للضبط (أو إلكترونية).</strong></td>
      <td>معالج رقمي دقيق كامل البرمجة.</td>
    </tr>
    <tr>
      <td><strong>طريقة التركيب والتثبيت</strong></td>
      <td>تثبيت على سكة DIN بعرض 35 مم.</td>
      <td><strong>تثبيت بمسامير، قاعدة سريعة، أو سحب كامل.</strong></td>
      <td>شاسيه قابل للسحب بعجلات ومقبض يدوي.</td>
    </tr>
    <tr>
      <td><strong>مستوى التطبيق في اللوحة</strong></td>
      <td>الدوائر الفرعية النهائية (إنارة ومقابس).</td>
      <td><strong>لوحات التوزيع الرئيسية، المغذيات، والمحركات.</strong></td>
      <td>القاطع الرئيسي للمحول والمحطة الفرعية.</td>
    </tr>
  </tbody>
</table>
'''
)

# ==============================================================================
# 2. MOTOR PROTECTION CIRCUIT BREAKER (MPCB) (EN, FR, ES, AR)
# ==============================================================================

MPCB_EN = dict(
    lang='en',
    dir='ltr',
    slug='motor-overload-protection-what-is-a-motor-protection-circuit-breaker',
    title='Industrial Motor Overload & Phase Failure Protection: What Is a Motor Protection Circuit Breaker?',
    breadcrumb='Fuse &amp; Protection',
    read='10 min read',
    alt='Bank of modular DIN-rail Motor Protection Circuit Breakers actively operating inside an industrial Motor Control Center panel',
    desc=('Industrial three-phase motor protection and manual starter switching: What is a motor protection circuit breaker (MPCB)? '
          'How compact MPCBs integrate adjustable thermal motor overload protection, differential phase loss detection, and 13x In magnetic short-circuit clearing.'),
    model='Model YMV2 / GV2 Series Manual Motor Starter & Protection Circuit Breakers',
    category='Fuse & Protection / Motor Protection Circuit Breakers',
    kw='what is a motor protection circuit breaker &middot; mpcb &middot; motor protection circuit breaker &middot; manual motor starter &middot; phase loss protection &middot; motor overload protection',
    specs=[
        ('Thermal Current Setting Range (Ir)', 'Precision adjustable current dials spanning 0.1A to 80A across multiple frame sizes (0.1–0.16A up to 56–80A)'),
        ('Short-Circuit Magnetic Release (Irm)', 'Fixed instantaneous electromagnetic trip set to 13 to 15 times the maximum dial setting (13–15 In) for motor inrush ride-through'),
        ('Phase Failure / Unbalance Protection', 'Differential bimetallic trip mechanism detecting single-phasing and severe phase unbalance within &le; 3 seconds per IEC 60947-4-1'),
        ('Ambient Temperature Compensation', 'Built-in compensation bimetal ensuring precise overload trip calibration across &minus;20&deg;C to +60&deg;C operating ambient temperatures'),
        ('Rated Breaking Capacity (Icu)', 'High short-circuit interrupting capacity: 10kA to 100kA at 400V/415V AC; Type 2 coordination ready (eliminates upstream backup fuses)'),
        ('Operating Mechanisms', 'Ergonomic rotary handle or dual START/STOP pushbuttons with trip-free mechanism and padlockable handle in the OFF position'),
        ('Auxiliary Contacts & Accessories', 'Front/side-mounted instantaneous auxiliary contacts (1NO+1NC or 2NO), fault signaling trip alarm contacts, and undervoltage/shunt trip releases'),
        ('Applicable International Standards', 'IEC 60947-2, IEC 60947-4-1 (Motor starters - Electromechanical contactors and motor-starters), UL 508, CE certified, RoHS compliant')
    ],
    faqs=[
        ('What is a Motor Protection Circuit Breaker (MPCB) and why can\'t standard MCBs protect industrial electric motors?',
         'A Motor Protection Circuit Breaker (MPCB), also classified as a manual motor starter, is an electromechanical protection device specially tailored '
         'to the operating characteristics of three-phase electric induction motors. Standard Miniature Circuit Breakers (MCBs) cannot adequately protect motors for three reasons: '
         '1. **Motor Inrush Current:** An AC motor draws a starting surge of 6 to 8 times its full-load current (FLA). A standard MCB will either nuisance-trip during startup, '
         'or if oversized, fail to protect the motor from mild continuous running overloads. '
         '2. **Non-Adjustable Calibration:** MCBs have fixed factory ratings (e.g. 10A, 16A, 20A). An MPCB features a fine-tuning dial allowing engineers to match '
         'the trip threshold to the exact nameplate full-load current of the motor down to 0.1A increments. '
         '3. **Phase Failure Detection:** The leading cause of motor burnout is "single-phasing" (losing one phase due to a blown fuse or loose wire). An MCB is blind to single-phasing; '
         'an MPCB incorporates a differential mechanism that trips immediately when one phase drops, saving the motor from winding burnout.'),
        ('How does the differential mechanism in an MPCB detect phase failure (single-phasing)?',
         'The MPCB contains three calibrated bimetallic strips—one for each electrical phase—interconnected through two sliding differential trip bars. '
         'Under normal balanced running conditions, all three bimetallic strips bend equally, shifting both bars together without triggering the release latch. '
         'However, if one phase is lost while the motor is running, the current in the remaining two phases spikes by approximately 1.73 times normal load, '
         'causing their bimetals to heat and bend severely while the cold bimetal of the dead phase remains straight. '
         'This differential displacement causes the two sliding bars to pivot against each other, tripping the mechanical release latch in under 2 to 3 seconds, '
         'long before the motor stator windings can overheat and melt their dielectric enamel.'),
        ('What is the difference between an MPCB and a traditional Contactor + Thermal Overload Relay (TOR) combination?',
         'In conventional motor control, protection requires three separate devices: fuses/MCB (for short circuits) + magnetic contactor (for switching) + thermal overload relay (for overload). '
         'An MPCB merges the short-circuit protection and overload protection into a single compact 45mm DIN-rail unit. '
         'When paired with a contactor, it provides complete **Type 2 Coordination**, meaning after clearing a heavy short circuit, the MPCB and contactor suffer no damage '
         'and can be safely reset immediately without replacing burnt fuse links, minimizing industrial assembly downtime.')
    ],
    cta='Designing motor control centers (MCC), industrial pump stations, agricultural irrigation panels, or machinery automation starters requiring certified 0.1A to 80A motor protection circuit breakers? YOMIN manufactures heavy-duty MPCBs tested to IEC 60947-4-1.',
    body='''
<h2>Shielding Industrial Motors from Costly Catastrophic Burnout</h2>
<p>Three-phase induction electric motors are the primary workhorses of modern manufacturing, driving conveyor systems, centrifugal water pumps, refrigeration compressors, industrial fans, and hydraulic power units. However, electric motors are also among the most electrically vulnerable assets in any factory.</p>
<p>Continuous mechanical overloads, bearing friction, frequent high-inertia start cycles, low voltage brownouts, and supply phase loss generate excessive heat within copper stator windings. Because winding insulation life is halved for every 10&deg;C increase above rated operating temperature, an unprotected motor can suffer irreversible insulation breakdown in minutes.</p>
<p>The <strong>Motor Protection Circuit Breaker (MPCB)</strong> provides dedicated, comprehensive protection tailored specifically to the thermal and electromagnetic physics of industrial electric motors.</p>

<h2>Three Pillars of MPCB Motor Protection</h2>
<p>A certified MPCB integrates three complementary protective functions within a single modular 45mm DIN-rail housing:</p>
<ol>
  <li><strong>Adjustable Thermal Overload Protection:</strong> Equipped with an external dial calibrated in full-load amperes (FLA). Unlike fixed breakers, an engineer can adjust the trip setting precisely to the motor's nameplate rating (e.g. 14.5 Amperes). The internal bimetallic strips follow an inverse-time characteristic: they absorb the motor's 6x to 8x starting inrush surge without tripping, but react progressively faster as continuous overload magnitude increases.</li>
  <li><strong>High-Speed Electromagnetic Short-Circuit Clearing:</strong> Built-in magnetic solenoids detect instantaneous short circuits (such as a winding-to-ground or phase-to-phase dead short), tripping the contacts open in under 3 milliseconds. With breaking capacities reaching 50kA or 100kA at 400V, the MPCB eliminates the need for upstream backup fuses.</li>
  <li><strong>Differential Phase Loss (Single-Phasing) Sensitivity:</strong> An ingenious sliding differential bar mechanism detects when one phase conductor loses voltage. Under single-phasing, the remaining two operational phases carry excessive current that will rapidly overheat the stator. The MPCB detects the unequal deflection of the bimetallic strips and trips within seconds, completely preventing motor burnout.</li>
</ol>

<h2>Comparison: Standard MCB vs. Overload Relay (TOR) vs. MPCB</h2>
<table>
  <thead>
    <tr>
      <th>Protective Capability</th>
      <th>Standard MCB (Miniature Breaker)</th>
      <th>Thermal Overload Relay (TOR)</th>
      <th>Motor Protection Circuit Breaker (MPCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Overload Setting Precision</strong></td>
      <td><strong>Fixed:</strong> 10A, 16A, 20A step ratings.</td>
      <td>Adjustable dial (e.g. 9–14A).</td>
      <td><strong>Adjustable dial (precision 0.1A).</strong></td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Protection</strong></td>
      <td><strong>Yes:</strong> 6kA–10kA rating.</td>
      <td><strong>No:</strong> will explode without fuses.</td>
      <td><strong>Yes:</strong> heavy-duty 50kA–100kA Icu.</td>
    </tr>
    <tr>
      <td><strong>Phase Failure Sensitivity</strong></td>
      <td><strong>No:</strong> completely blind to single-phasing.</td>
      <td>Yes: differential trip bar.</td>
      <td><strong>Yes:</strong> integrated differential trip bar.</td>
    </tr>
    <tr>
      <td><strong>Manual Motor Isolation</strong></td>
      <td>Yes: toggle lever.</td>
      <td><strong>No:</strong> requires upstream isolator.</td>
      <td><strong>Yes:</strong> rotary handle with padlock lockout.</td>
    </tr>
    <tr>
      <td><strong>Panel Space Required</strong></td>
      <td>3 modules (54mm) + TOR (45mm).</td>
      <td>Mounted under contactor.</td>
      <td><strong>Compact single unit (45mm width).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MPCB_FR = dict(
    lang='fr',
    dir='ltr',
    slug='motor-overload-protection-what-is-a-motor-protection-circuit-breaker-fr',
    title="Protection contre les Surcharges & Manque de Phase : Qu'est-ce qu'un Disjoncteur Moteur ?",
    breadcrumb='Fusibles &amp; Protection',
    read='10 min de lecture',
    alt='Batterie de disjoncteurs moteurs modulaires sur rail DIN en fonctionnement dans un centre de contrôle de moteurs industriel',
    desc=('Protection des moteurs triphasés industriels et démarreur manuel : Qu\'est-ce qu\'un disjoncteur moteur (MPCB) ? '
          'Comment les disjoncteurs moteurs intègrent une protection thermique réglable, une détection différentielle de manque de phase et un déclencheur magnétique 13x In.'),
    model='Série YMV2 / GV2 : Disjoncteurs Démarreurs Moteurs Manuels et Protecteurs',
    category='Fusibles & Protection / Disjoncteurs Moteurs',
    kw='disjoncteur moteur &middot; mpcb &middot; qu\'est-ce qu\'un disjoncteur moteur &middot; protection manque de phase &middot; relais thermique moteur &middot; démarreur moteur manuel',
    specs=[
        ('Plage de Réglage Thermique (Ir)', 'Molettes de réglage micrométrique couvrant de 0,1A à 80A sur plusieurs tailles de boîtiers (de 0,1–0,16A jusqu\'à 56–80A)'),
        ('Déclencheur Magnétique Court-Circuit', 'Déclencheur électromagnétique instantané fixe calibré à 13 à 15 fois le courant maximal (13–15 In) pour absorber la pointe de démarrage'),
        ('Protection contre le Manque de Phase', 'Mécanisme différentiel à bilames détectant le déséquilibre sévère ou la perte d\'une phase en moins de 3 secondes selon la CEI 60947-4-1'),
        ('Compensation de Température Ambiante', 'Bilame de compensation intégré garantissant la fidélité du déclenchement entre &minus;20&deg;C et +60&deg;C de température ambiante'),
        ('Pouvoir de Coupure Assigné (Icu)', 'Haut pouvoir de coupure en court-circuit : 10kA à 100kA sous 400V/415V AC ; prêt pour la coordination de Type 2 (sans fusible amont)'),
        ('Mécanismes de Commande', 'Bouton rotatif ergonomique ou boutons-poussoirs Marche/Arrêt avec déclenchement libre et poignée cadenassable en position Arrêt (OFF)'),
        ('Contacts Auxiliaires et Accessoires', 'Contacts auxiliaires instantanés frontaux/latéraux (1NO+1NC ou 2NO), contacts de signalisation de défaut et bobines à émission/manque de tension'),
        ('Normes Internationales Applicables', 'CEI 60947-2, CEI 60947-4-1 (Contacteurs et démarreurs électromécaniques de moteurs), UL 508, certifié CE et conforme RoHS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un disjoncteur moteur (MPCB) et pourquoi les disjoncteurs modulaires standards ne peuvent-ils pas protéger les moteurs ?',
         'Un disjoncteur moteur (MPCB - Motor Protection Circuit Breaker), également appelé démarreur moteur manuel, est un appareil électromécanique spécialement '
         'conçu pour répondre aux caractéristiques physiques des moteurs électriques asynchrones triphasés. Un disjoncteur modulaire classique (MCB) ne convient pas pour trois raisons : '
         '1. **Le courant d\'appel au démarrage :** Un moteur absorbe 6 à 8 fois son courant nominal au démarrage. Un disjoncteur modulaire classique déclenchera de manière intempestive, '
         'ou s\'il est surdimensionné, il ne protégera plus le moteur contre les surcharges lentes. '
         '2. **La précision de réglage :** Les disjoncteurs modulaires ont des calibres fixes (10A, 16A, 20A). Un disjoncteur moteur dispose d\'une molette permettant '
         'd\'ajuster le seuil thermique exactement à l\'intensité nominale inscrite sur la plaque signalétique du moteur. '
         '3. **La sensibilité au manque de phase :** La cause principale de grillage des moteurs est la perte d\'une phase (marche en monophasé). Un modulaire ne détecte pas ce défaut ; '
         'le disjoncteur moteur intègre un mécanisme différentiel qui coupe le circuit en moins de 3 secondes dès qu\'une phase disparaît, sauvant le bobinage.'),
        ('Comment le mécanisme différentiel du disjoncteur moteur détecte-t-il la disparition d\'une phase ?',
         'Le disjoncteur moteur comporte trois bilames thermiques (un par phase) reliés par deux réglettes coulissantes différentielles. '
         'En fonctionnement équilibré normal, les trois bilames fléchissent de façon identique et déplacent les deux réglettes ensemble sans actionner le crochet de déclenchement. '
         'Si une phase vient à manquer, le moteur continue de tourner en absorbant un courant 1,73 fois plus élevé sur les deux phases restantes. '
         'Les deux bilames sous tension chauffent et fléchissent fortement, tandis que le bilame de la phase coupée reste froid et droit. '
         'Ce déplacement différentiel fait pivoter les réglettes l\'une par rapport à l\'autre, déclenchant l\'ouverture mécanique en 2 à 3 secondes avant que le vernis '
         'd\'isolation des bobines ne fonde.'),
        ('Quelle est la différence entre un disjoncteur moteur et un ensemble contacteur + relais thermique traditionnel ?',
         'Dans un schéma classique, le départ moteur nécessite trois appareils distincts : fusibles (pour les courts-circuits) + contacteur (pour la commande) + relais thermique (pour la surcharge). '
         'Le disjoncteur moteur réunit la protection contre les courts-circuits et les surcharges dans un boîtier compact de 45 mm de large monté sur rail DIN. '
         'Associé à un contacteur, il garantit une **Coordination de Type 2** : après coupure d\'un court-circuit franc, l\'appareil ne subit aucun dommage et peut être '
         'réarmé immédiatement sans nécessiter le remplacement de cartouches fusibles, éliminant les temps d\'arrêt en usine.')
    ],
    cta='Vous concevez des armoires de commande de moteurs, des stations de pompage industriel, des systèmes de ventilation ou des convoyeurs automatisés nécessitant des disjoncteurs moteurs certifiés de 0,1A à 80A ? YOMIN fabrique des démarreurs protecteurs conformes CEI 60947-4-1.',
    body='''
<h2>Préserver les Moteurs Industriels contre le Grillage des Bobinages</h2>
<p>Les moteurs électriques asynchrones triphasés constituent la force motrice de l'industrie moderne, entraînant pompes hydrauliques, compresseurs frigorifiques, ventilateurs d'extraction et convoyeurs de production. Ils sont cependant particulièrement sensibles aux perturbations du réseau électrique.</p>
<p>Les surcharges mécaniques prolongées, les blocages de rotor, les démarrages trop fréquents et la perte d'une phase provoquent un échauffement interne destructeur. La durée de vie des isolants des bobinages étant divisée par deux pour chaque élévation de 10&deg;C au-delà de la température limite, un moteur non protégé peut être détruit en quelques minutes.</p>
<p>Le <strong>Disjoncteur Moteur (MPCB)</strong> offre une protection complète, autonome et parfaitement adaptée aux caractéristiques électrothermiques des moteurs électriques.</p>

<h2>Les Trois Fonctions Fondamentales du Disjoncteur Moteur</h2>
<p>Un disjoncteur moteur certifié réunit trois protections vitales dans un encombrement modulaire compact de 45 mm :</p>
<ol>
  <li><strong>Protection Thermique Réglable contre les Surcharges :</strong> Doté d'une molette étalonnée en ampères réels, il permet d'ajuster le seuil thermique exactement sur le courant nominal du moteur. Ses bilames absorbent la surintensité normale de démarrage sans déclencher, mais réagissent rapidement en cas de surcharge anormale.</li>
  <li><strong>Protection Magnétique Instantanée contre les Courts-Circuits :</strong> Des bobines électromagnétiques déclenchent l'ouverture en moins de 3 millisecondes en cas de défaut franc phase-phase ou phase-terre, avec un pouvoir de coupure atteignant 50kA ou 100kA sous 400V, supprimant ainsi les fusibles de secours en amont.</li>
  <li><strong>Protection Différentielle contre le Manque de Phase :</strong> Un système mécanique à réglettes différentielles compare en permanence la flexion relative des trois bilames, déclenchant l'ouverture immédiate dès qu'une phase disparaît pour éviter la destruction thermique du stator.</li>
</ol>

<h2>Tableau Comparatif : Disjoncteur Modulaire vs. Relais Thermique vs. Disjoncteur Moteur</h2>
<table>
  <thead>
    <tr>
      <th>Critère de Performance</th>
      <th>Disjoncteur Modulaire (MCB)</th>
      <th>Relais Thermique (TOR)</th>
      <th>Disjoncteur Moteur (MPCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Réglage du Seuil Thermique</strong></td>
      <td><strong>Fixe :</strong> 10A, 16A, 20A.</td>
      <td>Réglable par molette (ex. 9–14A).</td>
      <td><strong>Réglable de précision (au dixième d'ampère).</strong></td>
    </tr>
    <tr>
      <td><strong>Protection Court-Circuit</strong></td>
      <td><strong>Oui :</strong> 6kA–10kA.</td>
      <td><strong>Non :</strong> détruit sans fusibles amont.</td>
      <td><strong>Oui :</strong> haut pouvoir de coupure 50kA–100kA.</td>
    </tr>
    <tr>
      <td><strong>Sensibilité au Manque de Phase</strong></td>
      <td><strong>Non :</strong> totalement aveugle.</td>
      <td>Oui : système différentiel.</td>
      <td><strong>Oui :</strong> mécanisme différentiel intégré.</td>
    </tr>
    <tr>
      <td><strong>Sectionnement Manuel Local</strong></td>
      <td>Oui : manette à bascule.</td>
      <td><strong>Non :</strong> nécessite un sectionneur amont.</td>
      <td><strong>Oui :</strong> bouton rotatif cadenassable.</td>
    </tr>
    <tr>
      <td><strong>Encombrement dans l'Armoire</strong></td>
      <td>3 modules (54mm) + Relais.</td>
      <td>Accroché sous le contacteur.</td>
      <td><strong>Appareil compact unique (largeur 45 mm).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MPCB_ES = dict(
    lang='es',
    dir='ltr',
    slug='motor-overload-protection-what-is-a-motor-protection-circuit-breaker-es',
    title='Protección contra Sobrecargas y Pérdida de Fase en Motores: ¿Qué es un Guardamotor?',
    breadcrumb='Fusibles y Protección',
    read='10 min de lectura',
    alt='Banco de disyuntores guardamotores modulares en riel DIN operando dentro de un tablero de centro de control de motores',
    desc=('Protección de motores eléctricos trifásicos y arrancador manual: ¿Qué es un guardamotor (MPCB)? '
          'Cómo los guardamotores integran protección térmica ajustable, detección diferencial de pérdida de fase y disparo magnético ante cortocircuitos de 13x In.'),
    model='Serie YMV2 / GV2: Interruptores Guardamotores y Arrancadores Manuales',
    category='Fusibles y Protección / Guardamotores',
    kw='guardamotor &middot; mpcb &middot; qué es un guardamotor &middot; protección pérdida de fase &middot; relé térmico guardamotor &middot; arrancador manual de motor',
    specs=[
        ('Rango de Ajuste Térmico (Ir)', 'Diales de regulación micrométrica de 0,1A a 80A a través de varios tamaños de carcasa (desde 0,1–0,16A hasta 56–80A)'),
        ('Disparo Magnético por Cortocircuito', 'Disparador electromagnético instantáneo fijo calibrado entre 13 y 15 veces la corriente máxima (13–15 In) para absorber el arranque'),
        ('Protección ante Pérdida de Fase', 'Mecanismo bimetálico diferencial que detecta desequilibrios graves o caída de una fase en &le; 3 segundos según IEC 60947-4-1'),
        ('Compensación de Temperatura Ambiente', 'Bimetal de compensación integrado que asegura la precisión del disparo térmico entre &minus;20&deg;C y +60&deg;C de temperatura ambiente'),
        ('Poder de Corte Nominal (Icu)', 'Alta capacidad de interrupción de cortocircuito: 10kA a 100kA a 400V/415V AC; listo para coordinación Tipo 2 (sin fusibles de respaldo)'),
        ('Mecanismos de Operación', 'Mando giratorio ergonómico o pulsadores Marcha/Paro con disparo libre y maneta bloqueable mediante candado en posición OFF'),
        ('Contactos Auxiliares y Accesorios', 'Bloques auxiliares frontales y laterales (1NA+1NC o 2NA), contactos de señalización de disparo por falla y bobinas de emisión/mínima tensión'),
        ('Normas Internacionales Aplicables', 'IEC 60947-2, IEC 60947-4-1 (Contactores y arrancadores electromecánicos de motor), UL 508, certificado CE y cumplimiento RoHS')
    ],
    faqs=[
        ('¿Qué es un guardamotor (MPCB) y por qué los termomagnéticos comunes no protegen adecuadamente a los motores eléctricos?',
         'Un guardamotor (MPCB - Motor Protection Circuit Breaker), también denominado arrancador manual de motor, es un dispositivo electromecánico especialmente '
         'diseñado para las curvas de funcionamiento de los motores de inducción trifásicos. Un interruptor termomagnético modular común (MCB) no es adecuado por tres razones: '
         '1. **Corriente de arranque inrush:** Un motor absorbe entre 6 y 8 veces su corriente nominal al arrancar. Un termomagnético común disparará innecesariamente, '
         'o si se sobredimensiona, dejará de proteger al motor frente a sobrecargas lentas de marcha. '
         '2. **Ajuste de corriente:** Los termomagnéticos comunes tienen valores fijos (10A, 16A, 20A). Un guardamotor cuenta con un dial que permite regular '
         'la corriente térmica exactamente al valor de placa del motor. '
         '3. **Sensibilidad a la pérdida de fase:** La principal causa de quema de motores es la falta de una fase. Un termomagnético común no detecta este fallo; '
         'el guardamotor incorpora un mecanismo diferencial que desconecta la alimentación en menos de 3 segundos, evitando que el bobinado se queme.'),
        ('¿Cómo detecta el mecanismo diferencial del guardamotor la pérdida de una fase?',
         'El guardamotor contiene tres láminas bimetálicas (una por fase) conectadas mediante dos barras deslizantes diferenciales. '
         'En condiciones normales equilibradas, los tres bimetales se flexionan por igual, desplazando ambas barras al unísono sin activar el pestillo de disparo. '
         'Si una fase se corta con el motor en marcha, la corriente en las dos fases restantes aumenta un 173%, calentando fuertemente sus bimetales mientras el bimetal '
         'de la fase sin corriente permanece frío y recto. '
         'Este desplazamiento diferencial hace pivotar las barras entre sí, liberando el pestillo mecánico en 2 a 3 segundos antes de que el esmalte aislante del bobinado se dañe.'),
        ('¿Cuál es la diferencia entre un guardamotor y la combinación tradicional de contactor + relé térmico?',
         'En tableros clásicos, proteger un motor requería tres aparatos: fusibles (cortocircuito) + contactor (maniobra) + relé térmico (sobrecarga). '
         'El guardamotor une la protección contra cortocircuitos y sobrecargas en un único módulo compacto de 45 mm montado sobre riel DIN. '
         'Al conectarse con un contactor, proporciona **Coordinación Tipo 2**: tras cortar un cortocircuito grave, el guardamotor no sufre daño y puede rearmarse '
         'de inmediato sin tener que cambiar fusibles quemados, eliminando tiempos muertos en la fábrica.')
    ],
    cta='¿Diseña centros de control de motores (CCM), sistemas de bombeo industrial, plantas de tratamiento de agua o tableros de maquinaria pesada que requieren guardamotores certificados de 0,1A a 80A? YOMIN fabrica arrancadores guardamotores conforme a norma IEC 60947-4-1.',
    body='''
<h2>Protegiendo los Motores Industriales contra Daños Catastróficos por Sobrecarga</h2>
<p>Los motores eléctricos trifásicos son el corazón de la producción industrial moderna, impulsando bombas centrífugas, compresores de aire, ventiladores de tiro forzado, cintas transportadoras y prensas hidráulicas. Sin embargo, también son los equipos más vulnerables frente a anomalías en la red eléctrica.</p>
<p>Sobrecargas mecánicas prolongadas, trabas en rodamientos, arranques continuos con alta inercia y la pérdida repentina de una fase elevan drásticamente la temperatura interna de los bobinados de cobre. Como la vida útil del aislamiento se reduce a la mitad por cada 10&deg;C de incremento térmico sobre el límite, un motor sin protección adecuada puede quemarse en minutos.</p>
<p>El <strong>Guardamotor (MPCB)</strong> brinda una protección dedicada y completa adaptada específicamente a las propiedades térmicas y magnéticas de los motores industriales.</p>

<h2>Las Tres Funciones Clave de Protección del Guardamotor</h2>
<p>Un guardamotor certificado integra tres protecciones vitales en una estructura modular de solo 45 mm de ancho para riel DIN:</p>
<ol>
  <li><strong>Protección Térmica Ajustable contra Sobrecargas:</strong> Cuenta con una perilla graduada en amperios reales de motor. Sus bimetales toleran la corriente de arranque de 6 a 8 veces la nominal sin disparar, pero reaccionan con rapidez proporcional ante sobrecargas continuas de trabajo.</li>
  <li><strong>Protección Magnética Instantánea contra Cortocircuitos:</strong> Bobinas electromagnéticas disparan los contactos en menos de 3 milisegundos ante cortocircuitos francos fase-fase o fase-tierra, con poderes de corte de 50kA o 100kA a 400V, prescindiendo de fusibles aguas arriba.</li>
  <li><strong>Protección Diferencial ante Pérdida de Fase:</strong> Un sistema de barras diferenciales compara constantemente la flexión relativa de los tres bimetales, provocando el disparo inmediato si una fase se interrumpe para impedir que el motor continúe operando en dos fases.</li>
</ol>

<h2>Comparativa: Termomagnético Común vs. Relé Térmico vs. Guardamotor</h2>
<table>
  <thead>
    <tr>
      <th>Función Operativa</th>
      <th>Termomagnético Común (MCB)</th>
      <th>Relé Térmico (TOR)</th>
      <th>Guardamotor (MPCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Ajuste de Corriente Térmica</strong></td>
      <td><strong>Fijo:</strong> 10A, 16A, 20A.</td>
      <td>Ajustable por dial (ej. 9–14A).</td>
      <td><strong>Ajustable micrométrico (precisión 0,1A).</strong></td>
    </tr>
    <tr>
      <td><strong>Protección de Cortocircuito</strong></td>
      <td><strong>Sí:</strong> 6kA–10kA.</td>
      <td><strong>No:</strong> se destruye sin fusibles.</td>
      <td><strong>Sí:</strong> alto poder de corte 50kA–100kA.</td>
    </tr>
    <tr>
      <td><strong>Sensibilidad a Falta de Fase</strong></td>
      <td><strong>No:</strong> no detecta el desbalance.</td>
      <td>Sí: mecanismo diferencial.</td>
      <td><strong>Sí:</strong> mecanismo diferencial integrado.</td>
    </tr>
    <tr>
      <td><strong>Mando y Seccionamiento Local</strong></td>
      <td>Sí: palanca basculante.</td>
      <td><strong>No:</strong> requiere seccionador previo.</td>
      <td><strong>Sí:</strong> mando giratorio bloqueable con candado.</td>
    </tr>
    <tr>
      <td><strong>Espacio Ocupado en Tablero</strong></td>
      <td>3 módulos (54mm) + Relé.</td>
      <td>Acoplado bajo el contactor.</td>
      <td><strong>Un solo aparato compacto (ancho 45 mm).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

MPCB_AR = dict(
    lang='ar',
    dir='rtl',
    slug='motor-overload-protection-what-is-a-motor-protection-circuit-breaker-ar',
    title='حماية المحركات الصناعية من الحمل الزائد وسقوط الأطوار: ما هو قاطع حماية المحرك؟',
    breadcrumb='المصهرات والحماية',
    read='10 دقائق قراءة',
    alt='مجموعة من قواطع حماية المحركات المعيارية على سكة DIN تعمل داخل لوحة مركز التحكم في المحركات الصناعية',
    desc=('حماية المحركات الحثية ثلاثية الأطوار والتشغيل اليدوي: ما هو قاطع حماية المحرك (MPCB)؟ '
          'كيف تجمع قواطع المحركات بين الحماية الحرارية القابلة للمعايرة الدقيقة، وحساسية كشف انقطاع الطور، وسعة قطع لتيارات القصر تصل إلى 13 ضعف التيار الاسمي.'),
    model='سلسلة YMV2 / GV2: قواطع الدوائر ومفاتيح التشغيل اليدوية لحماية المحركات',
    category='المصهرات والحماية / قواطع حماية المحركات',
    kw='قاطع حماية المحرك &middot; mpcb &middot; ما هو قاطع المحرك &middot; حماية سقوط الفاز &middot; حماية الحمل الزائد للمحرك &middot; بادئ تشغيل يدوي للمحرك',
    specs=[
        ('نطاق ضبط تيار الحمل الزائد (Ir)', 'أقراص معايرة دقيقة تغطي نطاقات واسعة من 0.1A وحتى 80A عبر أحجام هياكل مختلفة (من 0.1–0.16A حتى 56–80A)'),
        ('وحدة الفصل المغناطيسي لتيار القصر', 'فصل كهرومغناطيسي لحظي ثابت معاير على 13 إلى 15 ضعف أقصى قيمة للتيار (13–15 In) لتحمل تيار بدء الحركة'),
        ('الحماية ضد سقوط وانقطاع أحد الأطوار', 'آلية تفاضلية مزدوجة الشرائح ثنائية المعدن ترصد غياب أحد الأطوار وتفصل التغذية في أقل من 3 ثوانٍ وفق معيار IEC 60947-4-1'),
        ('التعويض الحراري لدرجة الحرارة المحيطة', 'شريحة تعويض حراري مدمجة تضمن ثبات معايرة الفصل بدقة عبر نطاق واسع من &minus;20&deg;C وحتى +60&deg;C'),
        ('سعة كسر تيار القصر الاسمية (Icu)', 'سعة قطع عالية لتيارات القصر: من 10kA إلى 100kA عند 400V/415V AC؛ جاهز للتنسيق من النوع الثاني (Type 2 Coordination)'),
        ('آليات التشغيل والتحكم اليدوي', 'مقبض دوار مريح أو أزرار ضغط تشغيل/إيقاف مع آلية فصل حر، ومقبض قابل للإغلاق بقفل أمان في وضع الإيقاف (OFF)'),
        ('نقاط التلامس المساعدة والملحقات', 'نقاط تلامس مساعدة لحظية أمامية وجانبية (1NO+1NC أو 2NO)، نقاط إشارة إلى حدوث عطل، وملفات فصل بالجهد المنخفض أو بإشارة خارجية'),
        ('المعايير الدولية المعتمدة', 'IEC 60947-2، IEC 60947-4-1 (المفاتيح وأجهزة التحكم - قواطع وبادئات تشغيل المحركات)، UL 508، شهادة CE وتوافق كامل مع معايير RoHS')
    ],
    faqs=[
        ('ما هو قاطع حماية المحرك (MPCB) ولماذا لا تصلح القواطع المصغرة العادية (MCB) لحماية المحركات الكهربائية؟',
         'قاطع حماية المحرك (Motor Protection Circuit Breaker - MPCB)، المعروف أيضاً باسم بادئ التشغيل اليدوي للمحرك، هو جهاز كهروميكانيكي مصمم خصيصاً '
         'ليتناسب مع الخصائص التشغيلية والحرارية للمحركات الحثية ثلاثية الأطوار. ولا تستطيع القواطع المصغرة العادية حماية المحركات لثلاثة أسباب رئيسية: '
         '1. **تيار بدء الحركة العالي (Inrush Current):** يسحب المحرك تيار بدء يبلغ 6 إلى 8 أضعاف تياره الاسمي. سيفصل القاطع المصغر العادي خاطئاً عند بدء التشغيل، '
         'أو إذا تم تكبير سعته، سيعجز تماماً عن حماية المحرك من تيارات الحمل الزائد البسيطة أثناء الدوران. '
         '2. **دقة معايرة التيار:** تحتوي القواطع المصغرة على سعات ثابتة من المصنع (10A, 16A, 20A)، بينما يمتلك قاطع المحرك قرص معايرة يتيح ضبط تيار الفصل '
         'بدقة متناهية ليطابق تيار الحمل الكامل للمحرك المسجل على لوحة بياناته. '
         '3. **كشف سقوط أحد الأطوار (Phase Loss):** السبب الأكبر لاحتراق المحركات هو انقطاع أحد الأطوار الثلاثة. لا يستشعر القاطع المصغر هذا العطل، '
         'بينما يمتلك قاطع المحرك آلية تفاضلية تفصل الدائرة فوراً في أقل من 3 ثوانٍ لحماية الملفات من الاحتراق.'),
        ('كيف ترصد الآلية التفاضلية في قاطع المحرك انقطاع أحد الأطوار (Single-Phasing)؟',
         'يحتوي قاطع المحرك على ثلاث شرائح ثنائية المعدن (شريحة لكل طور) مرتبطة معاً بواسطة مسطرتين تفاضليتين منزلقين. '
         'في ظروف التشغيل المتزنة العادية، تنثني الشرائح الثلاث بالتساوي، فتحرك المسطرتين معاً دون تحرير ذراع الفصل الميكانيكي. '
         'أما إذا انقطع أحد الأطوار أثناء عمل المحرك، يقفز التيار المار في الطورين المتبقيين إلى نحو 1.73 ضعف القيمة العادية لتأمين القدرة الميكانيكية. '
         'تسخن الشريحتان الحاملتان للتيار وتنثنيان بشدة، بينما تظل شريحة الطور المنقطع باردة ومستقيمة. '
         'يؤدي هذا التفاوت الحركي إلى تحريك المسطرتين باتجاهين متضادين، مما يحرر ذراع الفصل ويفصل التغذية عن المحرك في 2 إلى 3 ثوانٍ قبل أن يذوب عازل الملفات.'),
        ('ما الفرق بين قاطع حماية المحرك (MPCB) والتجميعة التقليدية المكونة من كونتاكتور + مرحل حمل حراري (Overload)؟',
         'في دوائر التحكم التقليدية، تتطلب حماية المحرك ثلاثة أجهزة منفصلة: مصهرات (لحماية القصر) + كونتاكتور (لتشغيل المحرك) + مرحل حراري (لحماية الحمل الزائد). '
         'يدمج قاطع المحرك (MPCB) كلاً من حماية تيار القصر وحماية الحمل الزائد في وحدة واحدة مدمجة بعرض 45 مم تثبت على سكة DIN. '
         'وعند دمجه مع كونتاكتور، يحقق الجهاز ما يُعرف باسم **التنسيق من النوع الثاني (Type 2 Coordination)**؛ حيث لا يتعرض القاطع أو الكونتاكتور لأي ضرر بعد فصل تيار قصر هائل، '
         'ويمكن إعادة تشغيله فوراً دون الحاجة لاستبدال مصهرات محترقة، مما يلغي فترات التوقف في المصانع.')
    ],
    cta='هل تصمم لوحات مراكز التحكم في المحركات (MCC)، أو محطات الضخ الصناعية، أو أنظمة الري الزراعي وخطوط الإنتاج المؤتمتة التي تتطلب قواطع حماية محركات معتمدة بسعات من 0.1 إلى 80 أمبير؟ تصنع يمين (YOMIN) قواطع حماية وبادئات تشغيل المحركات وفق معيار IEC 60947-4-1 الدولي.',
    body='''
<h2>حماية المحركات الصناعية من أخطار الاحتراق وتلف العوازل</h2>
<p>تشكل المحركات الحثية ثلاثية الأطوار القوة الدافعة الأساسية في خطوط الإنتاج والمنشآت الصناعية الكبرى؛ حيث تدير مضخات المياه وضواغط الهواء ومراوح التهوية الضخمة وخطوط السيور الناقلة ومحطات الرفع الهيدروليكية. ومع ذلك، تعد هذه المحركات من أكثر المعدات الكهربائية عرضة للأعطال.</p>
<p>تؤدي الأحمال الميكانيكية الزائدة المستمرة، وتآكل كراسي التحميل (البلي)، والبدء المتكرر للأحمال ذات القصور الذاتي العالي، وسقوط أحد الأطوار المغذية إلى ارتفاع مفرط في درجات حرارة ملفات النحاس داخل العضو الثابت. ولأن العمر الافتراضي لعوازل الملفات ينخفض إلى النصف مع كل ارتفاع قدره 10 درجات مئوية فوق الحد المسموح، فإن المحرك غير المحمي يتعرض للتلف والانهيار التام في دقائق معدودة.</p>
<p>يقدم <strong>قاطع حماية المحرك (MPCB)</strong> منظومة حماية هندسية مخصصة وشاملة صُممت خصيصاً لتواكب المتطلبات الحرارية والكهرومغناطيسية للمحركات الكهربائية.</p>

<h2>الوظائف الحمائية الثلاث المتكاملة في قاطع المحرك</h2>
<p>يدمج قاطع حماية المحرك المعتمد ثلاث وظائف حماية حيوية في وحدة معيارية مدمجة بعرض 45 مم تثبت على سكة DIN:</p>
<ol>
  <li><strong>حماية الحمل الزائد الحرارية القابلة للضبط:</strong> مزود بقرص معايرة خارجي مدرج بالأمبير الفعلي، يتيح للمهندس ضبط تيار الفصل بدقة تامة ليطابق التيار المقنن للمحرك. تمتص الشرائح ثنائية المعدن تيار البدء العالي دون أن تفصل، لكنها تفصل الدائرة بسرعة متناسبة طردياً مع شدة الحمل الزائد المستمر.</li>
  <li><strong>حماية كهرومغناطيسية فائقة السرعة من تيارات القصر:</strong> وحدات فصل كهرومغناطيسية مدمجة تستشعر تيار القصر الكهربائي العنيف وتفصل نقاط التلامس في أقل من 3 أجزاء من الألف من الثانية، بسعات قطع تصل إلى 50 أو 100 كيلو أمبير عند 400 فولت، مما يلغي الحاجة للمصهرات الاحتياطية.</li>
  <li><strong>حساسية فائقة لرصد انقطاع الأطوار:</strong> آلية تفاضلية ميكانيكية تستشعر غياب أحد خطوط التغذية على الفور، وتفصل التغذية الكهربائية في ثوانٍ معدودة قبل أن ترتفع حرارة العضو الثابت ويتعرض المحرك للاحتراق.</li>
</ol>

<h2>جدول مقارنة هندسي: القاطع المصغر (MCB) مقابل مرحل الحمل الزائد (TOR) مقابل قاطع حماية المحرك (MPCB)</h2>
<table>
  <thead>
    <tr>
      <th>المعيار الفني</th>
      <th>القاطع المصغر العادي (MCB)</th>
      <th>مرحل الحمل الزائد الحراري (TOR)</th>
      <th>قاطع حماية المحرك (MPCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>دقة ضبط تيار الحمل الزائد</strong></td>
      <td><strong>ثابت:</strong> سعات محددة 10A, 16A, 20A.</td>
      <td>قابل للضبط بقرص (مثل 9–14A).</td>
      <td><strong>ضبط معايرة دقيق (بأجزاء الأمبير 0.1A).</strong></td>
    </tr>
    <tr>
      <td><strong>حماية تيار القصر (Short Circuit)</strong></td>
      <td><strong>نعم:</strong> سعة قطع 6kA–10kA.</td>
      <td><strong>لا:</strong> يتلف ويحترق بدون مصهرات.</td>
      <td><strong>نعم:</strong> سعة قطع عالية 50kA–100kA Icu.</td>
    </tr>
    <tr>
      <td><strong>حساسية كشف انقطاع أحد الأطوار</strong></td>
      <td><strong>لا:</strong> لا يستشعر سقوط الطور.</td>
      <td>نعم: عبر مسطرة تفاضلية.</td>
      <td><strong>نعم:</strong> آلية تفاضلية ميكانيكية مدمجة.</td>
    </tr>
    <tr>
      <td><strong>العزل والتشغيل اليدوي الموضعي</strong></td>
      <td>نعم: ذراع فصل وتبديل.</td>
      <td><strong>لا:</strong> يتطلب قاطع عزل منفصل.</td>
      <td><strong>نعم:</strong> مقبض دوار قابل للقفل بقفل أمان.</td>
    </tr>
    <tr>
      <td><strong>المساحة المطلوبة داخل اللوحة</strong></td>
      <td>3 وحدات (54 مم) + المرحل.</td>
      <td>يركب أسفل الكونتاكتور.</td>
      <td><strong>جهاز مدمج واحد (عرض 45 مم فقط).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

ALL_MULTILINGUAL_POSTS_0929 = [
    MCCB_EN, MCCB_FR, MCCB_ES, MCCB_AR,
    MPCB_EN, MPCB_FR, MPCB_ES, MPCB_AR
]
