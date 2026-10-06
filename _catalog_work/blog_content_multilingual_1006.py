# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-06:
1. Energy Storage Connector for BESS Battery Racks (EN, FR, ES, AR)
2. Neutral Link and Earth Terminal Bars for Switchboards (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. ENERGY STORAGE CONNECTOR (EN, FR, ES, AR)
# ==============================================================================

ESC_EN = dict(
    lang='en',
    dir='ltr',
    slug='bess-battery-packs-what-is-an-energy-storage-connector',
    title='Battery Energy Storage Systems (BESS): What Is an Energy Storage Connector?',
    breadcrumb='Flexible Busbars &amp; Energy Storage',
    read='10 min read',
    alt='Heavy-duty 1500V DC single-pole quick-lock energy storage connectors (Model YM-ES series) installed on a utility-scale BESS lithium battery rack',
    desc=('Utility-scale Battery Energy Storage Systems (BESS) and commercial solar-plus-storage rack connections: What is an energy storage connector? '
          'How 1500V DC ratings, integrated High Voltage Interlock Loops (HVIL), IP67 sealing, and 360-degree rotating heads eliminate arc flash hazards in lithium battery packs.'),
    model='Model YM-ES / Rhino Series Single-Pole Quick-Lock Energy Storage Power Connectors (120A, 200A, 350A, 500A up to 1500V DC)',
    category='Flexible Busbars & Energy Storage / Energy Storage Connectors',
    kw='what is an energy storage connector &middot; energy storage connector &middot; bess connector &middot; battery energy storage connector &middot; 1500v energy storage connector &middot; hvil connector',
    specs=[
        ('Rated Operating Voltage & Dielectric Proof', 'Rated continuous operating voltage up to 1500V DC; withstand dielectric test voltage &ge; 5000V AC / 1 minute'),
        ('Current Carrying Capacity Options', 'Standard modular continuous current ratings: 120A, 200A, 250A, 350A, and 500A (accommodating 16 mm&sup2; to 120 mm&sup2; high-voltage shielded cables)'),
        ('Integrated High Voltage Interlock Loop (HVIL)', 'Integrated two-pin signal circuit that disconnects 10 to 30 milliseconds *before* high-voltage power pins to trigger inverter/BMS de-energization'),
        ('Contact Pin Material & Surface Plating', 'High-conductivity tellurium copper or beryllium copper crown spring contacts with thick micro-silver plating (&ge; 3 &mu;m) for minimal contact resistance'),
        ('Environmental Protection & Ingress Sealing', 'Certified IP67 waterproof and dustproof in mated condition with dual fluorosilicone O-rings; IP2X finger-safe touch protection unmated'),
        ('Mechanical Anti-Mismating Keying & Colors', 'Mechanical physical keyway indexing and visual color coding: Safety Orange for positive (+), Jet Black for negative (-)'),
        ('Flexible Cable Orientation & Locking Mechanism', '360-degree freely rotating right-angle plug head; dual-action push-pull self-locking latch with audible click and secondary security slide'),
        ('Applicable International Safety Standards', 'Fully compliant with UL 4128 (standard for connectors in electrochemical battery systems), IEC 61984, and RoHS/REACH')
    ],
    faqs=[
        ('What is an Energy Storage Connector and why can standard industrial plugs NOT be used for 1500V BESS racks?',
         'An Energy Storage Connector—frequently referred to by battery engineers as a BESS power connector or quick-lock battery plug—is '
         'a specialized single-pole, touch-proof electrical quick-disconnect fitting engineered specifically to carry high continuous DC current '
         'between rack-mounted lithium-ion battery modules (LiFePO4/NMC) and the central DC busbar in energy storage containers. '
         'Standard multi-pin industrial plugs or conventional screw terminals fail catastrophically in 1500V DC battery environments for three critical reasons: '
         '<ul>'
         '<li><strong>1. Lethal DC Arc Flash:</strong> Direct current (DC) does not have a natural zero-crossing point like AC power. '
         'If a connection carrying 300A at 1500V DC is accidentally unplugged under load, an uncontained, continuous plasma arc will form across the gap, '
         'instantly vaporizing copper, creating an explosive arc flash, and incinerating the battery rack.</li>'
         '<li><strong>2. Reverse Polarity Explosion:</strong> In series-connected battery strings, connecting positive to negative creates a dead short-circuit '
         'with prospective fault currents exceeding 50,000 amperes, triggering immediate thermal runaway. Energy storage connectors utilize mechanical keying '
         'and distinct color coding (orange/black) that makes cross-polarity insertion physically impossible.</li>'
         '<li><strong>3. Extreme Thermal Stresses in Sealed Racks:</strong> High continuous charging/discharging cycles demand sub-milliohm contact resistance. '
         'Energy storage connectors utilize silver-plated multi-contact crown springs that maintain low operating temperature and resist vibration loosening.</li>'
         '</ul>'),
        ('How does the High Voltage Interlock Loop (HVIL) physically prevent electrical accidents during maintenance?',
         'The High Voltage Interlock Loop (HVIL) is a life-critical safety circuit integrated directly into the connector geometry. '
         'Inside the plug, two small auxiliary signal pins sit alongside the primary high-current power contact. '
         'Critically, these HVIL signal pins are physically shorter than the main power pins: '
         '<ul>'
         '<li><strong>During Disconnection (Unplugging):</strong> As a technician presses the release button and pulls the plug, '
         'the shorter HVIL pins separate first—approximately 10 to 30 milliseconds <em>before</em> the high-voltage power contact breaks. '
         'The Battery Management System (BMS) and power conversion system (PCS) instantly detect the broken circuit and open the main DC contactors, '
         'de-energizing the battery rack before physical pin separation. This completely eliminates the possibility of an open-air DC arc flash.</li>'
         '<li><strong>During Connection (Plugging In):</strong> The main power pins make contact and seat fully inside the socket <em>before</em> '
         'the HVIL circuit closes, ensuring the system cannot be energized while contacts are only partially engaged.</li>'
         '</ul>'),
        ('Why is a 360-degree rotating plug head essential for containerized BESS battery enclosures?',
         'Containerized energy storage enclosures pack hundreds of megawatt-hours of battery cells into cramped 20-foot or 40-foot shipping containers. '
         'Space between battery module trays and rack doors is typically less than 10 to 15 centimeters. '
         'High-current cables (e.g., 50 mm&sup2; to 120 mm&sup2;) are extremely stiff with large bending radii. '
         'A fixed-angle connector forces cables into awkward bends that stress internal PCB terminals and cause micro-cracks over thermal cycles. '
         'The 360-degree freely rotating plug head of the YOMIN YM-ES connector allows technicians to orient the cable exit angle in any direction '
         '(upward, downward, or sideways into adjacent vertical wire ducts) without applying mechanical shear strain to the socket or battery enclosure.')
    ],
    cta='Designing containerized battery energy storage systems (BESS), commercial microgrids, or solar-plus-storage battery racks requiring UL 4128 and IEC 61984 certified 1500V energy storage quick connectors? YOMIN manufactures industrial-grade BESS connectors.',
    body='''
<h2>The Safety Backbone of Modern Battery Energy Storage Systems (BESS)</h2>
<p>As global utility grids rapidly transition to intermittent renewable power sources such as solar and wind, <strong>utility-scale Battery Energy Storage Systems (BESS)</strong> have become the indispensable foundation of grid stability, frequency regulation, and peak shaving.</p>
<p>To maximize energy density and inverter efficiency, modern commercial and utility storage installations operate at high voltages up to <strong>1500V DC</strong>. Thousands of lithium iron phosphate (LiFePO4) battery cells are grouped into modules, stacked in steel racks, and connected in series and parallel.</p>
<p>However, 1500V DC battery strings present unprecedented electrical hazards: immense prospective short-circuit currents, continuous non-zero-crossing DC arcs, and thermal runaway risks during maintenance.</p>
<p>The <strong>Energy Storage Connector (Model YM-ES / Rhino Series)</strong> provides the dedicated engineering solution: a robust, touch-proof quick-lock power disconnect engineered with integrated High Voltage Interlock (HVIL), IP67 sealing, and mechanical anti-reversal keying.</p>

<h2>Engineering Anatomy: Inside a 1500V BESS Power Connector</h2>
<ol>
  <li><strong>Silver-Plated Crown Spring Contact Pin:</strong> Machined from high-conductivity tellurium copper with multi-leaf spring louvers, delivering contact resistance &le; 0.3 m&Omega; to eliminate thermal buildup under 500A continuous charging.</li>
  <li><strong>High Voltage Interlock Loop (HVIL) Safety Circuit:</strong> Shorter auxiliary pins break first during unplugging, commanding the BMS to drop contactors before primary power pins separate, eradicating arc flash risks.</li>
  <li><strong>360-Degree Rotating Elbow Plug Body:</strong> Allows linemen and assembly technicians to route heavy 70–120 mm&sup2; battery cables cleanly without mechanical strain in compact rack enclosures.</li>
  <li><strong>Mechanical Physical Keying & Color Differentiation:</strong> Distinct physical keyways and high-visibility Safety Orange (+) and Jet Black (-) housings prevent catastrophic cross-polarity connections.</li>
  <li><strong>IP67 Dual-O-Ring Sealing & IP2X Finger Safety:</strong> Fluorosilicone seals protect internal contacts from moisture and condensation inside outdoor containers, while plastic shrouds prevent fingers from touching live parts during installation.</li>
</ol>

<h2>Comparison: Energy Storage Quick Connector vs. Standard Bolted Cable Lug vs. Industrial Cam-Lock Plug</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>Standard Bolted Cable Lug &amp; Stud</th>
      <th>YOMIN YM-ES Energy Storage Quick Connector</th>
      <th>Industrial Cam-Lock Power Plug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Connection &amp; Maintenance Speed</strong></td>
      <td>Slow: Requires torque wrenches and insulated hand tools aloft.</td>
      <td><strong>Instant: Tool-free push-pull quick-lock click in 3 seconds.</strong></td>
      <td>Twist-lock requiring manual alignment.</td>
    </tr>
    <tr>
      <td><strong>Live-Part Touch Protection (IP2X)</strong></td>
      <td>Unsafe: Bare live metallic stud exposed during cover removal.</td>
      <td><strong>100% Touch-proof: IP2X insulated shrouds isolate live pins.</strong></td>
      <td>Moderate; rubber boot can slip back.</td>
    </tr>
    <tr>
      <td><strong>High Voltage Interlock Loop (HVIL)</strong></td>
      <td>None: No signal circuit to prevent disconnect under load.</td>
      <td><strong>Integrated HVIL pins cut signal before power pins break.</strong></td>
      <td>None: Zero electrical interlock capability.</td>
    </tr>
    <tr>
      <td><strong>Reverse Polarity Prevention</strong></td>
      <td>Relies solely on visual cable tagging (prone to human error).</td>
      <td><strong>Mechanical physical keyway prevents reverse connection.</strong></td>
      <td>Color coded only; mechanical keying absent.</td>
    </tr>
    <tr>
      <td><strong>Vibration Loosening in Transit/Operation</strong></td>
      <td>Bolts can loosen under shipping and HVAC vibration.</td>
      <td><strong>Dual-stage positive snap-latch immune to vibration loosening.</strong></td>
      <td>Twist mechanism can back out under vibration.</td>
    </tr>
  </tbody>
</table>
'''
)

ESC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='bess-battery-packs-what-is-an-energy-storage-connector-fr',
    title="Systèmes de Stockage d'Énergie par Batterie (BESS) : Qu'est-ce qu'un Connecteur de Stockage d'Énergie ?",
    breadcrumb='Barres Souples &amp; Stockage d\'Énergie',
    read='10 min de lecture',
    alt='Connecteur de puissance étanche 1500V DC à verrouillage rapide (Série YM-ES) installé sur un rack de batteries lithium pour conteneur BESS',
    desc=('Systèmes de stockage d\'énergie par batterie (BESS) et raccordements de racks solaires : Qu\'est-ce qu\'un connecteur de stockage d\'énergie ? '
          'Tension nominale 1500V DC, boucle de verrouillage haute tension (HVIL), étanchéité IP67 et tête rotative à 360° pour éliminer les risques d\'arc électrique.'),
    model='Série YM-ES / Rhino : Connecteurs de Puissance Unipolaires à Verrouillage Rapide pour Stockage d\'Énergie (120A, 200A, 350A, 500A jusqu\'à 1500V DC)',
    category='Barres Souples & Stockage d\'Énergie / Connecteurs de Stockage d\'Énergie',
    kw='connecteur stockage énergie &middot; connecteur bess &middot; connecteur batterie lithium &middot; prise 1500v bess &middot; connecteur hvil &middot; raccord batterie',
    specs=[
        ('Tension Assignée de Service et Isolement', 'Tension assignée continue jusqu\'à 1500V DC ; tension d\'épreuve diélectrique &ge; 5000V AC pendant 1 minute'),
        ('Calibres de Courant Permanent Admissible', 'Gamme modulaire de courants continus : 120A, 200A, 250A, 350A et 500A (pour câbles blindés de 16 mm&sup2; à 120 mm&sup2;)'),
        ('Boucle de Verrouillage Haute Tension (HVIL)', 'Circuit de signalisation intégré à deux broches se déconnectant 10 à 30 ms *avant* les pôles de puissance pour coupure préalable'),
        ('Matériau des Contacts et Revêtement', 'Contacts en cuivre tellure haute conductivité à ressorts multiples avec argenture électrolytique épaisse (&ge; 3 &mu;m)'),
        ('Degré de Protection et Sécurité Tactile', 'Certifié IP67 à l\'état verrouillé avec double joint torique ; sécurité tactile IP2X à l\'état déconnecté'),
        ('Détrompage Mécanique et Code Couleur', 'Détrompage mécanique par rainure physique et repérage visuel : Orange Sécurité pour pôle (+), Noir pour pôle (-)'),
        ('Flexibilité de Montage et Verrouillage', 'Tête de prise coudée pivotant librement à 360° ; verrouillage rapide push-pull avec clic audible et loquet de sécurité'),
        ('Normes Internationales de Qualification', 'Entièrement conforme aux normes UL 4128 (systèmes de batteries électrochimiques), CEI 61984 et directives RoHS/REACH')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Connecteur de Stockage d\'Énergie et pourquoi une prise industrielle ordinaire est-elle proscrite sur un rack 1500V BESS ?',
         'Un Connecteur de Stockage d\'Énergie—souvent désigné sous le terme de connecteur BESS ou prise rapide de batterie—est '
         'un raccord électrique unipolaire étanche et sécurisé, spécialement conçu pour acheminer de forts courants continus (DC) '
         'entre les modules de batteries lithium (LiFePO4) et le jeu de barres principal dans les conteneurs de stockage. '
         'L\'usage de bornes à vis classiques ou de prises industrielles génériques est extrêmement dangereux à 1500V DC pour trois raisons : '
         '<ul>'
         '<li><strong>1. Arc Électrique DC Destructeur :</strong> Le courant continu ne possède aucun passage à zéro naturel. '
         'Déconnecter sous charge un courant de 300A sous 1500V DC génère un arc plasma ininterrompu provoquant une explosion thermique instantanée.</li>'
         '<li><strong>2. Risque Mortel d\'Inversion de Polarité :</strong> En série, brancher un pôle positif sur un négatif crée un court-circuit franc '
         'dépassant 50 000 ampères. Les connecteurs de stockage disposent d\'un détrompage mécanique physique rendant l\'inversion impossible.</li>'
         '<li><strong>3. Échauffement Extrême en Milieu Clos :</strong> Les cycles de charge/décharge exigent une résistance de contact inférieure à 0,3 m&Omega; '
         'obtenue uniquement grâce aux contacts à ressorts multiples argentés.</li>'
         '</ul>'),
        ('Comment la boucle de verrouillage haute tension (HVIL) protège-t-elle les techniciens ?',
         'La boucle HVIL (High Voltage Interlock Loop) est un système de sécurité intrinsèque. '
         'Deux petites broches pilotes sont intégrées dans le connecteur à côté du contact de puissance principal : '
         '<ul>'
         '<li><strong>À la déconnexion :</strong> Les broches HVIL étant plus courtes, elles se séparent 10 à 30 millisecondes <em>avant</em> '
         'la broche de puissance. Le système de gestion de batterie (BMS) détecte l\'ouverture du circuit et coupe immédiatement les contacteurs DC généraux, '
         'garantissant que la broche de puissance se déconnecte hors tension sans aucun arc électrique.</li>'
         '<li><strong>À la connexion :</strong> La broche de puissance s\'engage d\'abord, et ce n\'est qu\'une fois la prise verrouillée '
         'que les broches HVIL établissent le contact, autorisant l\'alimentation du circuit.</li>'
         '</ul>'),
        ('Pourquoi la tête rotative à 360° est-elle indispensable dans un conteneur BESS ?',
         'Dans un conteneur de stockage, les tiroirs de batteries sont extrêmement serrés et l\'espace avec la porte ne dépasse pas 10 à 15 cm. '
         'Les câbles de forte section (50 à 120 mm&sup2;) sont très rigides. '
         'Une prise fixe imposerait un rayon de courbure excessif qui endommagerait les cartes électroniques du module. '
         'La tête orientable à 360° permet d\'orienter le câble dans n\'importe quelle direction sans exercer d\'effort mécanique de torsion sur la prise.')
    ],
    cta='Vous intégrez des conteneurs de stockage d\'énergie par batterie (BESS), des micro-réseaux ou des installations solaires hybrides nécessitant des connecteurs 1500V certifiés UL 4128 ? YOMIN fabrique des connecteurs de stockage d\'énergie haute fiabilité.',
    body='''
<h2>Le Cœur Sécuritaire des Systèmes Modernes de Stockage par Batterie (BESS)</h2>
<p>Face à l\'essor mondial des énergies renouvelables intermittentes (solaire et éolien), les <strong>systèmes de stockage d\'énergie par batterie à grande échelle (BESS)</strong> sont devenus les piliers incontournables de la régulation de fréquence et de la résilience des réseaux électriques.</p>
<p>Afin de maximiser le rendement énergétique, les installations modernes fonctionnent sous de très hautes tensions continues atteignant <strong>1500V DC</strong>, regroupant des milliers de cellules lithium fer phosphate (LiFePO4) connectées en racks.</p>
<p>Ces niveaux de tension et d\'énergie imposent des contraintes draconiennes pour éliminer tout risque d\'arc électrique continu et d\'incendie lors des opérations de maintenance.</p>
<p>Le <strong>Connecteur de Stockage d\'Énergie (Série YM-ES / Rhino)</strong> constitue la réponse industrielle normalisée : un raccord rapide unipolaire certifié IP67 intégrant une boucle de sécurité HVIL et un détrompage physique absolu.</p>

<h2>Caractéristiques et Éléments de Conception</h2>
<ol>
  <li><strong>Broche à Ressorts Multiples en Cuivre Argenté :</strong> Garantit une résistance de contact &le; 0,3 m&Omega; évitant tout échauffement sous un régime permanent de 500A.</li>
  <li><strong>Boucle de Sécurité Haute Tension (HVIL) :</strong> Coupe le signal pilote avant la séparation des pôles de puissance pour neutraliser le risque d\'arc électrique DC.</li>
  <li><strong>Tête Pivotante à 360 Degrés :</strong> Facilite le cheminement des gros câbles dans les espaces restreints des armoires de batteries.</li>
  <li><strong>Détrompage Physique et Code Couleur Orange/Noir :</strong> Élimine tout risque d\'inversion de polarité pouvant provoquer un court-circuit destructeur.</li>
</ol>
'''
)

ESC_ES = dict(
    lang='es',
    dir='ltr',
    slug='bess-battery-packs-what-is-an-energy-storage-connector-es',
    title='Sistemas de Almacenamiento de Energía con Baterías (BESS): ¿Qué es un Conector de Almacenamiento de Energía?',
    breadcrumb='Barras Flexibles y Almacenamiento',
    read='10 min de lectura',
    alt='Conector de potencia unipolar para almacenamiento de energía a 1500V DC (Serie YM-ES) instalado en rack de baterías de litio BESS',
    desc=('Sistemas de almacenamiento de energía con baterías (BESS) y conexiones de potencia en racks solares: ¿Qué es un conector de almacenamiento de energía? '
          'Tensión de 1500V DC, lazo de enclavamiento de alta tensión (HVIL), estanqueidad IP67 y cabezal giratorio a 360° para prevenir arcos eléctricos.'),
    model='Serie YM-ES / Rhino: Conectores Unipolares de Desconexión Rápida para Almacenamiento de Energía (120A, 200A, 350A, 500A hasta 1500V DC)',
    category='Barras Flexibles y Almacenamiento / Conectores para Almacenamiento de Energía',
    kw='conector almacenamiento energia &middot; conector bess &middot; conector baterias litio &middot; enchufe 1500v bess &middot; conector hvil &middot; borne rapido bateria',
    specs=[
        ('Tensión Nominal de Operación y Prueba', 'Tensión nominal continua de servicio hasta 1500V DC; tensión de ensayo dieléctrico &ge; 5000V AC durante 1 minuto'),
        ('Capacidad de Corriente Continua Admisible', 'Gama modular de capacidades nominales: 120A, 200A, 250A, 350A y 500A (para cables apantallados de 16 mm&sup2; a 120 mm&sup2;)'),
        ('Lazo de Enclavamiento de Alta Tensión (HVIL)', 'Circuito de control integrado con dos pines que se desconectan 10 a 30 ms *antes* que los contactos de potencia para corte seguro'),
        ('Material del Contacto y Recubrimiento', 'Contacto de cobre al telurio con resortes laminares de alta elasticidad y recubrimiento grueso de plata pura (&ge; 3 &mu;m)'),
        ('Protección Ambiental y Grado de Estanqueidad', 'Certificado IP67 en estado acoplado con doble junta tórica; protección al tacto accidental IP2X en estado desacoplado'),
        ('Codificación Mecánica Antierror y Colores', 'Llave de posicionamiento físico y colores normalizados: Naranja de Seguridad para positivo (+), Negro Azabache para negativo (-)'),
        ('Flexibilidad de Enrutamiento y Enclavamiento', 'Cabezal acodado con giro libre de 360°; mecanismo de traba rápida push-pull con clic sonoro y pestillo de seguridad'),
        ('Cumplimiento de Estándares Internacionales', 'Totalmente conforme con normas UL 4128 (conectores para sistemas de baterías electroquímicas), IEC 61984 y directivas RoHS/REACH')
    ],
    faqs=[
        ('¿Qué es un Conector de Almacenamiento de Energía y por qué NO se pueden usar terminales convencionales en racks BESS de 1500V?',
         'Un Conector de Almacenamiento de Energía—conocido en la industria como conector BESS o enchufe rápido para baterías de litio—es '
         'un componente unipolar de conexión y desconexión rápida diseñado para transportar elevadas corrientes continuas (DC) '
         'entre los módulos de baterías (LiFePO4) y las barras colectoras principales dentro de contenedores BESS. '
         'El empleo de terminales atornillados comunes o conectores industriales estándar es inviable a 1500V DC por tres causas críticas: '
         '<ul>'
         '<li><strong>1. Arco Eléctrico en Corriente Continua:</strong> La corriente continua no tiene cruce por cero. '
         'Desconectar 300A a 1500V DC genera un arco de plasma continuo que funde el metal y provoca una explosión térmica inmediata.</li>'
         '<li><strong>2. Peligro de Inversión de Polaridad:</strong> Conectar por error el polo positivo con el negativo en un rack en serie crea un cortocircuito '
         'superior a 50.000 amperios. Los conectores BESS poseen chaveteros mecánicos que impiden físicamente una inserción invertida.</li>'
         '<li><strong>3. Mantenimiento Seguro y Veloz:</strong> Permite retirar y reemplazar módulos de batería en minutos sin herramientas metálicas expuestas.</li>'
         '</ul>'),
        ('¿Cómo previene accidentes el Lazo de Enclavamiento de Alta Tensión (HVIL)?',
         'El lazo HVIL (High Voltage Interlock Loop) es un circuito de seguridad pasiva. '
         'En el interior del conector hay dos pines auxiliares de control junto al pin principal de potencia: '
         '<ul>'
         '<li><strong>Al desconectar:</strong> Los pines HVIL son más cortos y se separan entre 10 y 30 milisegundos <em>antes</em> '
         'que el contacto principal de potencia. El sistema BMS detecta la apertura y abre los contactores generales de la batería, '
         'garantizando que el conector de potencia se separe sin corriente y sin riesgo de arco eléctrico.</li>'
         '<li><strong>Al conectar:</strong> El contacto de potencia se inserta primero y los pines HVIL cierran al final, '
         'asegurando que el circuito solo se energice cuando el conector está totalmente bloqueado.</li>'
         '</ul>'),
        ('¿Por qué es fundamental el cabezal giratorio a 360° en contenedores BESS?',
         'En los contenedores de almacenamiento BESS, los módulos están muy próximos a las compuertas (apenas 10 a 15 cm de luz). '
         'Los cables de potencia (50 a 120 mm&sup2;) son muy rígidos. '
         'Un conector con salida fija forzaría el cable provocando tensiones mecánicas que dañan los bornes internos del módulo. '
         'El cabezal giratorio a 360° permite canalizar los cables hacia bandejas superiores o laterales con total holgura mecánica.')
    ],
    cta='¿Diseña proyectos de almacenamiento de energía con baterías (BESS), microrredes industriales o instalaciones solares con acumulación a 1500V bajo norma UL 4128? YOMIN fabrica conectores de potencia para almacenamiento de energía de alta confiabilidad.',
    body='''
<h2>La Conexión de Alta Seguridad para Sistemas de Almacenamiento con Baterías</h2>
<p>En la transición energética global hacia fuentes solares y eólicas, los <strong>sistemas de almacenamiento de energía con baterías a escala de red (BESS)</strong> constituyen el componente fundamental para la estabilidad y el soporte de frecuencia eléctrica.</p>
<p>Para maximizar la eficiencia y reducir las pérdidas de conversión, los contenedores industriales operan actualmente a tensiones elevadas de hasta <strong>1500V DC</strong>, interconectando decenas de módulos de litio ferrofosfato (LiFePO4) en serie y paralelo.</p>
<p>Estos niveles de potencia demandan componentes que eliminen cualquier riesgo de choque eléctrico, arco persistente o error de polaridad durante las tareas de mantenimiento.</p>
<p>El <strong>Conector de Almacenamiento de Energía (Serie YM-ES / Rhino)</strong> representa la solución tecnológica estándar: un conector rápido unipolar con protección IP67, lazo de seguridad HVIL y chavetero antierror mecánico.</p>

<h2>Elementos de Ingeniería y Seguridad</h2>
<ol>
  <li><strong>Contacto de Cobre Plateado con Resortes de Corona:</strong> Logra una resistencia de contacto &le; 0,3 m&Omega; para mantener temperaturas frías bajo cargas continuas de hasta 500A.</li>
  <li><strong>Circuito de Enclavamiento de Seguridad (HVIL):</strong> Desconecta la señal de control milisegundos antes que la potencia, erradicando arcos eléctricos destructivos.</li>
  <li><strong>Cabezal Pivotante en 360 Grados:</strong> Permite orientar cables pesados en cualquier ángulo sin inducir fatiga mecánica sobre los módulos.</li>
  <li><strong>Diferenciación Mecánica y Código de Color Naranja/Negro:</strong> Impide físicamente cualquier conexión con polaridad cruzada.</li>
</ol>
'''
)

ESC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='bess-battery-packs-what-is-an-energy-storage-connector-ar',
    title='منظومات تخزين طاقة البطاريات (BESS): ما هو موصل تخزين الطاقة عالي الجهد؟',
    breadcrumb='القضبان المرنة وتخزين الطاقة',
    read='10 دقائق قراءة',
    alt='موصل أحادي القطب سريع القفل لبطاريات تخزين الطاقة بجهد 1500V DC (موديل YM-ES) مثبت على رفوف بطاريات الليثيوم في محطة BESS',
    desc=('منظومات تخزين الطاقة بالبطاريات على نطاق الشبكة (BESS) وتوصيلات رفوف الطاقة الشمسية: ما هو موصل تخزين الطاقة؟ '
          'جهد 1500V DC، حلقة القفل الداخلي عالي الجهد (HVIL)، العزل المقاوم للماء IP67، والرأس الدوار 360 درجة لمنع شرارات القوس الكهربائي.'),
    model='سلسلة YM-ES / Rhino: موصلات القدرة أحادية القطب سريعة التوصيل لمنظومات تخزين الطاقة (سعات 120A، 200A، 350A، 500A حتى 1500V DC)',
    category='القضبان المرنة وتخزين الطاقة / موصلات تخزين الطاقة BESS',
    kw='موصل تخزين الطاقة &middot; موصل bess &middot; موصل بطارية ليثيوم &middot; قابس بطاريات 1500v &middot; موصل hvil &middot; وصلة تخزين طاقة',
    specs=[
        ('جهد التشغيل المقنن واختبار العزل', 'جهد تشغيل مستمر مقنن يصل إلى 1500V DC؛ جهد صمود عازل للاختبار &ge; 5000V AC لمدة دقيقة كاملة'),
        ('سعات التيار المستمر الاسمية المتاحة', 'سعات تيار معيارية: 120A، 200A، 250A، 350A، و 500A (تستوعب كابلات معزولة ومحمية من 16 مم&sup2; إلى 120 مم&sup2;)'),
        ('حلقة القفل الداخلي عالي الجهد (HVIL)', 'دائرة تحكم إشارية مدمجة بدبوسين تفصل قبل أقطاب القدرة بفارق 10 إلى 30 مليثانية لقطع الجهد مسبقاً'),
        ('مادة ونقاوة نقاط التلامس والطلاء', 'نحاس تيلوريوم فائق التوصيل بنوابض تاجية مرنة مع طلاء فضة نقي سميك (&ge; 3 &mu;m) لأدنى مقاومة تلامس ممكنة'),
        ('درجة الحماية البيئية ومقاومة الماء', 'معتمد بدرجة عزل IP67 ضد الماء والأتربة في حالة الإغلاق؛ وحماية لمس بالأصابع IP2X في حالة الفصل'),
        ('الترميز الميكانيكي وألوان الأمان', 'مجرى ميكانيكي مانع للخطأ وتمييز لوني: برتقالي الأمان للقطب الموجب (+)، وأسود داكن للقطب السالب (-)'),
        ('مرونة التوجيه وقفل الأمان السريع', 'رأس قابس زاوي حر الدوران بزاوية 360 درجة؛ آلية سحب ودفع سريعة مع قفل ميكانيكي بصوت نقرة ومزلاج أمان مزدوج'),
        ('المعايير الدولية وشهادات الاعتماد', 'مطابق كلياً لمواصفات UL 4128 (موصلات أنظمة البطاريات الكهروكيميائية) و IEC 61984 وتوجيهات RoHS')
    ],
    faqs=[
        ('ما هو موصل تخزين الطاقة ولماذا لا يمكن استخدام القوابس الصناعية العادية في رفوف بطاريات 1500V BESS؟',
         'موصل تخزين الطاقة—والمعروف في محطات الطاقة النظيفة بموصل BESS أو قابس البطاريات عالي الجهد—هو '
         'وصلة كهربائية أحادية القطب سريعة الفصل والربط، مصممة خصيصاً لنقل التيارات المستمرة (DC) العالية بأمان '
         'بين وحدات بطاريات الليثيوم (LiFePO4) وقضبان التوزيع الرئيسية داخل حاويات تخزين الطاقة. '
         'إن استخدام المرابط المسننة العادية أو القوابس الصناعية العامة يمثل خطراً فادحاً عند جهد 1500V DC لثلاثة أسباب: '
         '<ul>'
         '<li><strong>1. القوس الكهربائي المستمر المدمر (DC Arc Flash):</strong> لا يمر التيار المستمر بنقطة الصفر الطبيعية كالتيار المتردد. '
         'وفصل موصل يحمل 300 أمبير عند 1500V DC يولد قوساً كهربائياً نارياً مستمراً يصهر المعادن ويسبب انفجاراً حرارياً في الرف.</li>'
         '<li><strong>2. كارثة عكس القطبية (Reverse Polarity):</strong> توصيل القطب الموجب بالسالب بالخطأ يسبب قصر دائرة يتجاوز 50,000 أمبير، '
         'مما يدمر بنك البطاريات فورياً. تتميز موصلات BESS بمجاري ميكانيكية وألوان مميزة تجعل التوصيل العكسي مستحيلاً فيزيائياً.</li>'
         '<li><strong>3. الصيانة السريعة دون لمس الأجزاء الحية:</strong> يتيح استبدال وحدات البطاريات خلال ثوانٍ مع عزل تام يمنع الصعق الكهربائي (IP2X).</li>'
         '</ul>'),
        ('كيف تحمي حلقة القفل الداخلي عالي الجهد (HVIL) أرواح المهندسين أثناء الصيانة؟',
         'تعتبر حلقة HVIL (High Voltage Interlock Loop) صمام الأمان الكهربائي الأهم في الموصل. '
         'يوجد داخل القابس دبوسان إشاريان صغيران بجوار قطب القدرة الرئيسي، ويتميز هذان الدبوسان بأنهما أقصر طولاً: '
         '<ul>'
         '<li><strong>عند الفصل:</strong> يفصل دبوسا HVIL قبل قطب القدرة بفارق 10 إلى 30 مليثانية. '
         'يرصد نظام إدارة البطارية (BMS) فتح الدائرة فيقوم فوراً بفصل قواطع الكونتاكتور الرئيسية، '
         'مما يجعل قطب القدرة يفصل في حالة خمول تام وخالٍ من أي تيار، ملغياً خطر حدوث شرارة كهربائية كلياً.</li>'
         '<li><strong>عند التوصيل:</strong> يكتمل دخول قطب القدرة في مكانه أولاً، ثم يغلق مسار HVIL لاحقاً لتأكيد الإغلاق قبل تفعيل الطاقة.</li>'
         '</ul>'),
        ('لماذا يعتبر الرأس الدوار 360 درجة أمراً حيوياً داخل حاويات BESS؟',
         'في حاويات تخزين الطاقة، توضع رفوف البطاريات في مساحات ضيقة للغاية بحيث لا تزيد المسافة بين واجهة البطارية وباب الحاوية عن 10 إلى 15 سم. '
         'وتكون كابلات القدرة (50 إلى 120 مم&sup2;) سميكة وقاسية وصعبة الانحناء. '
         'إن استخدام موصل ذي زاوية ثابتة سيجبر الكابل على الانحناء بعنف، مما يسبب إجهادات تكسر أطراف البطارية الداخلية. '
         'يتيح الرأس الدوار 360 درجة توجيه الكابل لأعلى أو لأسفل أو للجانب بحرية وسلاسة تامة دون أي إجهاد ميكانيكي.')
    ],
    cta='هل تعمل على تطوير محطات تخزين الطاقة بالبطاريات (BESS)، أو شبكات الطاقة الشمسية المصغرة، أو رفوف البطاريات بجهد 1500V المعتمدة لمعايير UL 4128؟ تصنع يمين (YOMIN) موصلات تخزين طاقة فائقة الأمان والاعتمادية.',
    body='''
<h2>شريان الأمان لمنظومات تخزين الطاقة بالبطاريات الحديثة (BESS)</h2>
<p>مع تسارع وتيرة التحول العالمي نحو مصادر الطاقة المتجددة مثل الطاقة الشمسية وطاقة الرياح، أصبحت <strong>منظومات تخزين طاقة البطاريات الكبرى (BESS)</strong> الركيزة الأساسية لضمان استقرار الشبكات الكهربائية ودعم التردد وتخزين فوائض التوليد.</p>
<p>ولرفع كفاءة النقل وتقليل الفواقد الكهربائية، تعمل محطات التخزين الحاوية الحديثة عند جهود مستمرة مرتفعة تصل إلى <strong>1500V DC</strong>، حيث تُربط آلاف خلايا الليثيوم (LiFePO4) في سلاسل متتالية ومتوازية.</p>
<p>وتفرض هذه الجهود الفائقة متطلبات أمان غير مسبوقة لمنع حوادث القوس الكهربائي المستمر وعكس القطبية أثناء التركيب والصيانة الميدانية.</p>
<p>يمثل <strong>موصل تخزين الطاقة عالي الجهد (سلسلة YM-ES / Rhino)</strong> الحل الهندسي المعتمد دولياً: موصل سريع أحادي القطب بدرجة حماية IP67 مزود بحلقة أمان ذكية HVIL وتشفير فيزيائي مانع للخطأ.</p>

<h2>المكونات الهندسية وميزات الحماية المتقدمة</h2>
<ol>
  <li><strong>أقطاب تلامس نحاسية مطلية بالفضة بنوابض تاجية:</strong> تحقق مقاومة تلامس &le; 0.3 m&Omega; لمنع الارتفاع الحراري تحت تيار تشغيلي مستمر حتى 500 أمبير.</li>
  <li><strong>حلقة الأمان الكهربائي المبكر (HVIL):</strong> تقطع إشارة التشغيل قبل فصل أقطاب القدرة بمليثوان، ملغية خطر تفريغ الشحنات والقوس الكهربائي.</li>
  <li><strong>رأس زاوي حر الدوران بزاوية 360 درجة:</strong> يتيح توجيه كابلات القدرة السميكة بسلاسة تامة داخل المساحات المحصورة لحاويات البطاريات.</li>
  <li><strong>ترميز ميكانيكي مانع للانعكاس وألوان مميزة:</strong> يمنع فيزيائياً أي توصيل خاطئ بين القطبين الموجب البرتقالي والسالب الأسود.</li>
</ol>
'''
)

# ==============================================================================
# 2. NEUTRAL LINK / EARTH TERMINAL BAR (EN, FR, ES, AR)
# ==============================================================================

NL_EN = dict(
    lang='en',
    dir='ltr',
    slug='distribution-switchboards-what-is-a-neutral-link',
    title='Electrical Distribution Switchboards: What Is a Neutral Link?',
    breadcrumb='Terminals &amp; Connectors',
    read='10 min read',
    alt='Heavy-duty solid brass Neutral Link and Earthing Terminal Bar (Model YM-NL series) installed inside an industrial low-voltage electrical main distribution board (MDB)',
    desc=('Low-voltage switchboards, consumer units, and industrial distribution panels: What is a neutral link? '
          'How solid high-purity brass bars, flame-retardant insulating standoffs, and removable disconnect links prevent floating neutrals and enable safe Megger insulation testing.'),
    model='Model YM-NL / TB Series High-Conductivity Solid Brass Neutral Disconnecting Links and Earthing Terminal Bars (4-Way to 48-Way, up to 250A)',
    category='Terminals & Connectors / Neutral Links & Earth Bars',
    kw='what is a neutral link &middot; neutral link &middot; earth terminal bar &middot; brass neutral link &middot; neutral disconnect link &middot; neutral bar',
    specs=[
        ('Bar Material Composition & Purity', 'Extruded high-conductivity solid free-cutting brass alloy (Cu &ge; 58–60%, Pb &le; 2.5%, balance Zn) or optional high-purity copper'),
        ('Rated Operational Voltage & Insulation Level', 'Rated operational voltage up to 690V / 1000V AC; insulation standoff rating tested to 2.5kV AC / 1 minute'),
        ('Continuous Current Rating Capacity', 'Standard modular continuous current ratings from 63A, 100A, 160A, up to 250A for main incoming neutral currents'),
        ('Number of Outgoing Terminal Ways', 'Available in modular lengths: 4, 6, 8, 12, 18, 24, 36, and 48 terminal ways (accommodating 1.5 mm&sup2; to 35 mm&sup2; branch cables)'),
        ('Removable Disconnect Link Bridge', 'Bolted central removable brass/copper bridge link allowing physical isolation of neutral without disconnecting individual branch wires'),
        ('Mounting Base & Insulation Standoff', 'Mounted on high-dielectric, flame-retardant polyamide (PA66 / UL 94 V-0) or phenolic insulating standoffs (isolated from switchboard metal)'),
        ('Terminal Clamping Screw Hardware', 'Zinc-plated or nickel-plated high-tensile brass clamping screws with wire-protecting pressure pads to prevent conductor strand cutting'),
        ('Applicable International Standards', 'Manufactured and compliant with IEC 61439-1, IEC 61439-2, BS 7671, and EN 60947-7-1 for low-voltage switchgear assemblies')
    ],
    faqs=[
        ('What is a Neutral Link and why is it essential in electrical distribution boards and consumer units?',
         'A Neutral Link—also termed a neutral bar, neutral disconnect bar, or neutral bus link—is '
         'a precision-machined solid brass or copper terminal bar mounted on electrical insulating standoffs inside an electrical distribution panel. '
         'Its primary engineering function is to serve as the common collection and return junction point for all neutral conductors ($N$) of branch circuits, '
         'connecting them back to the main incoming supply neutral. '
         'In modern electrical distribution boards, the neutral link fulfills three vital engineering roles: '
         '<ul>'
         '<li><strong>1. Safe Return Current Path:</strong> In single-phase circuits and unbalanced three-phase systems, return current continuously '
         'flows through the neutral wire. A loose or high-resistance neutral connection creates a severe fire hazard. A heavy brass neutral link provides '
         'a low-resistance, high-ampacity connection point for dozens of circuits.</li>'
         '<li><strong>2. Prevention of "Floating Neutral" Overvoltages:</strong> If a common neutral connection breaks or comes loose in a three-phase system, '
         'the neutral point "floats" dynamically. Single-phase loads on lightly loaded phases can experience up to 400V AC across their 230V terminals, '
         'instantly incinerating electronics, LED drivers, and sensitive appliances.</li>'
         '<li><strong>3. Selective Disconnection for Testing:</strong> Modern neutral links feature a removable bolted center link that allows electricians '
         'to isolate the neutral bar from the main incoming supply during maintenance and insulation resistance testing without unbolting dozens of wires.</li>'
         '</ul>'),
        ('What is the critical difference between a Neutral Link and an Earth Terminal Bar?',
         'While neutral links and earth terminal bars often look visually similar (both are brass bars with screw terminals), their electrical isolation '
         'and operational functions are completely opposite: '
         '<ul>'
         '<li><strong>Neutral Link (Active Live Conductor):</strong> The neutral bar connects active return current paths and operates at near-ground potential '
         'under normal conditions. Because it carries continuous return current, it MUST be electrically isolated from the metal panel enclosure '
         'by mounting on high-voltage flame-retardant insulating standoffs (such as red PA66 pillars). If a neutral link touches the metal enclosure, '
         'it causes nuisance tripping of Residual Current Devices (RCDs/ELCBs) or dangerous stray currents.</li>'
         '<li><strong>Earth Terminal Bar (Protective Earth Conductor):</strong> The earth bar connects protective grounding wires (PE) and carries current '
         'ONLY during an electrical fault condition. Consequently, the earth bar is bolted directly to the metal switchboard frame and bonded '
         'to the main grounding electrode without insulation standoffs.</li>'
         '</ul>'),
        ('Why do electrical regulations require a removable Disconnecting Link on the neutral bar?',
         'Electrical commissioning and periodic maintenance regulations (such as BS 7671 and IEC 60364-6) mandate periodic <strong>insulation resistance testing (Megger testing)</strong>. '
         'During a Megger test, a technician applies 500V or 1000V DC between phase conductors and earth, and between neutral and earth, to detect compromised insulation. '
         'If the neutral bar remains connected to the utility transformer supply neutral, the test voltage will either be shorted to earth through the transformer star point, '
         'or the 1000V DC test surge will backfeed into upstream electronic meters and utility equipment. '
         'By simply removing the two bolts on the central disconnecting link bridge, the entire neutral bar is cleanly isolated from the incoming grid, '
         'allowing instant, accurate insulation resistance testing of all building branch circuits in seconds.')
    ],
    cta='Manufacturing low-voltage electrical switchboards, main distribution boards (MDBs), or consumer units requiring certified solid brass neutral links and earthing terminal bars? YOMIN manufactures precision-machined neutral bars.',
    body='''
<h2>The Critical Return Junction in Low-Voltage Power Distribution</h2>
<p>Inside every electrical distribution switchboard—from residential consumer units to multi-megawatt industrial Main Distribution Boards (MDBs)—electrical power is split from incoming supply feeders into dozens of branch circuits supplying lighting, HVAC, and machinery.</p>
<p>While circuit breakers protect the live phase conductors ($L_1, L_2, L_3$), all return current from single-phase and unbalanced loads must return safely back to the power transformer through the <strong>neutral circuit ($N$)</strong>.</p>
<p>Connecting neutral conductors haphazardly with wire nuts or unrated terminal blocks leads to loose terminations, terminal overheating, and the catastrophic hazard known as a "floating neutral."</p>
<p>The <strong>Neutral Link / Earth Terminal Bar (Model YM-NL / TB Series)</strong> provides the standardized, heavy-duty solution: an insulated, multi-way solid brass terminal bar engineered for high-conductivity return current handling and selective testing isolation.</p>

<h2>Engineering Anatomy: Inside a Certified Neutral Disconnecting Link</h2>
<ol>
  <li><strong>Solid Extruded Brass Bar (Cu &ge; 58–60%):</strong> Precision-extruded and CNC-machined from high-strength electrical brass alloy. Resists thread stripping and delivers low contact resistance under full rated continuous current.</li>
  <li><strong>Removable Center Disconnect Bridge:</strong> A bolted copper/brass link bar that can be unfastened in seconds to isolate the neutral bar from the utility supply during 500V/1000V DC Megger insulation resistance testing.</li>
  <li><strong>Flame-Retardant Polyamide Insulating Standoffs (PA66, UL 94 V-0):</strong> Heavy-duty red insulating pillars elevate the neutral bar away from the metal switchboard backplate, providing &ge; 2.5kV dielectric isolation.</li>
  <li><strong>Wire-Guarded Clamping Screws:</strong> Zinc-plated high-torque screws clamp conductor strands evenly inside the bored tunnels without shearing fine wire strands.</li>
  <li><strong>Transparent Protective Polycarbonate Cover:</strong> Snap-on clear insulating shield prevents accidental finger contact (IP2X) while allowing visual inspection of wire terminations.</li>
</ol>

<h2>Comparison: Solid Brass Disconnecting Neutral Link vs. Uninsulated Terminal Strip vs. Wire Nut Cluster</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>Twisted Wire Nut Cluster</th>
      <th>Standard Uninsulated Terminal Strip</th>
      <th>YOMIN YM-NL Disconnecting Brass Neutral Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Continuous Current Capacity</strong></td>
      <td>Low (&le; 20A–30A); prone to melting under heavy unbalanced loads.</td>
      <td>Moderate (&le; 63A); limited by small screw contact area.</td>
      <td><strong>Heavy-Duty: Rated from 100A to 250A continuous neutral current.</strong></td>
    </tr>
    <tr>
      <td><strong>Electrical Isolation from Panel Frame</strong></td>
      <td>Hangs loose; risk of touching grounded enclosure.</td>
      <td>Plastic base can crack or track under dust and humidity.</td>
      <td><strong>Flame-retardant PA66 insulating standoffs rated for 2.5kV AC.</strong></td>
    </tr>
    <tr>
      <td><strong>Megger Insulation Testing Facility</strong></td>
      <td>Requires untwisting every wire individually (laborious).</td>
      <td>Must unscrew incoming feeder wire manually.</td>
      <td><strong>Removable bolted link isolates entire bar in seconds.</strong></td>
    </tr>
    <tr>
      <td><strong>Prevention of Floating Neutral Failures</strong></td>
      <td>Extremely poor; loose twists cause neutral detachment and 400V surges.</td>
      <td>Moderate; vibrations can loosen screw terminals.</td>
      <td><strong>Solid heavy brass block with high-torque wire-guard clamping screws.</strong></td>
    </tr>
    <tr>
      <td><strong>IEC 61439 Switchboard Compliance</strong></td>
      <td>Non-compliant; prohibited in commercial switchboards.</td>
      <td>Borderline; often fails temperature rise and short-circuit tests.</td>
      <td><strong>100% Compliant with IEC 61439-1/2 and BS 7671 requirements.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

NL_FR = dict(
    lang='fr',
    dir='ltr',
    slug='distribution-switchboards-what-is-a-neutral-link-fr',
    title="Tableaux de Distribution Électrique : Qu'est-ce qu'une Barrette de Neutre (Neutral Link) ?",
    breadcrumb='Bornes &amp; Connecteurs',
    read='10 min de lecture',
    alt='Barrette de neutre sectionnable en laiton massif (Modèle YM-NL) montée sur isolateurs dans un tableau général basse tension (TGBT)',
    desc=('Tableaux de distribution électrique basse tension (TGBT) et armoires industrielles : Qu\'est-ce qu\'une barrette de neutre (neutral link) ? '
          'Laiton massif haute conductivité, isolateurs thermoplastiques ignifugés et barrette de coupure amovible pour essais d\'isolement.'),
    model='Série YM-NL / TB : Barrettes de Neutre Sectionnables et Barres de Terre en Laiton Massif (4 à 48 Départs, jusqu\'à 250A)',
    category='Bornes & Connecteurs / Barrettes de Neutre & Borniers de Terre',
    kw='barrette de neutre &middot; neutral link &middot; bornier de neutre &middot; barrette de coupure neutre &middot; bornier de terre tgbt',
    specs=[
        ('Matériau du Profilé et Pureté du Laiton', 'Laiton de décolletage massif extrudé haute conductivité (Cu &ge; 58–60%, balance Zn) ou cuivre pur sur demande'),
        ('Tension Assignée d\'Emploi et Isolement', 'Tension assignée jusqu\'à 690V / 1000V AC ; tenue diélectrique des isolateurs testée à 2,5kV AC / 1 minute'),
        ('Courant Permanent Admissible du Barreau', 'Calibres de courant permanent modulaires : 63A, 100A, 160A et jusqu\'à 250A pour le neutre principal d\'arrivée'),
        ('Nombre de Départs et Raccordements', 'Disponible en longueurs modulaires de 4, 6, 8, 12, 18, 24, 36 et 48 trous (conducteurs de 1,5 mm&sup2; à 35 mm&sup2;)'),
        ('Liaison Démontable de Sectionnement', 'Barrette de pontage centrale démontable permettant d\'isoler le neutre sans débrancher les départs individuels'),
        ('Piliers Isolateurs et Support de Fixation', 'Monté sur isolateurs colonnettes en polyamide ignifugé haute rigidité (PA66 / UL 94 V-0) isolés du châssis métallique'),
        ('Vis de Serrage et Protection des Brins', 'Vis de serrage en laiton ou acier zingué à haute résistance avec étriers protège-brins pour éviter le cisaillage'),
        ('Conformité aux Normes Internationales', 'Fabriqué selon les normes CEI 61439-1, CEI 61439-2, NF C 15-100 et EN 60947-7-1 pour ensembles d\'appareillage')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Barrette de Neutre (Neutral Link) et quel est son rôle dans un tableau électrique ?',
         'Une Barrette de Neutre—souvent appelée bornier de neutre, répartiteur de neutre ou barrette de coupure—est '
         'une barre massive en laiton ou en cuivre usinée avec précision, montée sur des isolateurs à l\'intérieur du tableau de distribution électrique. '
         'Sa fonction est de centraliser tous les conducteurs de neutre ($N$) des circuits divisionnaires et de les raccorder au neutre d\'arrivée du réseau. '
         'Dans un tableau basse tension moderne (TGBT), elle remplit trois rôles vitaux : '
         '<ul>'
         '<li><strong>1. Retour Électrique Sécurisé :</strong> Dans les circuits monophasés et les réseaux triphasés déséquilibrés, le courant de retour '
         'transite en permanence par le neutre. Une barrette en laiton massif offre une liaison à très faible résistance capable d\'absorber de fortes intensités.</li>'
         '<li><strong>2. Prévention de la Rupture de Neutre (Neutre Flottant) :</strong> Si la connexion du neutre principal se rompt sur un réseau triphasé, '
         'le neutre "flotte", provoquant des surtensions mortelles pouvant atteindre 400V sur les récepteurs 230V, grillant instantanément les équipements électroniques.</li>'
         '<li><strong>3. Sectionnement pour Essais Diélectriques :</strong> La barrette comporte un pont amovible permettant d\'isoler le réseau de neutre '
         'du transformateur amont lors des mesures d\'isolement au mégohmmètre sans avoir à déconnecter les dizaines de fils divisionnaires.</li>'
         '</ul>'),
        ('Quelle est la différence fondamentale entre une Barrette de Neutre et une Barrette de Terre ?',
         'Bien que ces deux pièces se ressemblent visuellement, leur régime de fonctionnement et leur mode de fixation sont diamétralement opposés : '
         '<ul>'
         '<li><strong>Barrette de Neutre (Conducteur Actif sous Tension) :</strong> Le neutre véhicule le courant de retour en service normal. '
         'Par conséquent, il DOIT être rigoureusement isolé de la carcasse métallique du tableau par des colonnettes isolantes en plastique ignifugé. '
         'Si le neutre touchait la masse métallique, les disjoncteurs différentiels (DDR) déclencheraient instantanément.</li>'
         '<li><strong>Barrette de Terre (Conducteur de Protection PE) :</strong> Le bornier de terre ne conduit du courant qu\'en cas de défaut d\'isolement. '
         'Il est vissé directement sur la tôlerie métallique du tableau sans aucun isolateur, pour assurer l\'équipotentialité parfaite du coffret.</li>'
         '</ul>'),
        ('Pourquoi la barrette de coupure démontable est-elle exigée par les normes d\'installation ?',
         'Les normes d\'installation électrique (comme la NF C 15-100 et la CEI 60364-6) imposent des contrôles périodiques de la <strong>résistance d\'isolement (mesure au mégohmmètre)</strong> sous 500V ou 1000V DC. '
         'Si le neutre restait relié au réseau du distributeur, la tension d\'épreuve serait dérivée à la terre au niveau du transformateur public ou endommagerait les compteurs amont. '
         'En retirant simplement les deux vis de la barrette de sectionnement centrale, l\'ensemble du neutre du bâtiment est immédiatement isolé de l\'alimentation générale, '
         'permettant de mesurer l\'isolement de tous les circuits en quelques secondes.')
    ],
    cta='Vous assemblez des tableaux généraux basse tension (TGBT), des armoires de distribution industrielle ou des coffrets modulaires nécessitant des barrettes de neutre certifiées CEI 61439 ? YOMIN fabrique des borniers de neutre en laiton usiné.',
    body='''
<h2>Le Point Névralgique du Retour de Courant Basse Tension</h2>
<p>Dans chaque armoire de distribution électrique basse tension, l\'énergie provenant du transformateur est distribuée vers des dizaines de départs divisionnaires alimentant l\'éclairage, la climatisation et les machines.</p>
<p>Alors que chaque phase est protégée par un disjoncteur, l\'intégralité des courants de retour des charges monophasées doit impérativement retourner vers la source via le <strong>conducteur neutre ($N$)</strong>.</p>
<p>Un mauvais raccordement du neutre ou un desserrage accidentel engendre des surchauffes dangereuses et le risque redoutable de "rupture de neutre", injectant 400V dans les appareils ménagers et informatiques.</p>
<p>La <strong>Barrette de Neutre Sectionnable (Série YM-NL / TB)</strong> apporte la solution normalisée : un barreau en laiton massif isolé du coffret, garantissant une tenue thermique parfaite et un sectionnement rapide pour les contrôles réglementaires.</p>

<h2>Conception et Éléments de Sécurité</h2>
<ol>
  <li><strong>Corps en Laiton Électrotechnique Massif :</strong> Usiné avec précision pour garantir un serrage énergique sans foirer les filetages.</li>
  <li><strong>Pont de Coupure Amovible Central :</strong> Permet d\'isoler le réseau de neutre en un instant pour les mesures d\'isolement à 500V/1000V DC.</li>
  <li><strong>Colonnettes Isolantes Ignifugées (PA66, UL 94 V-0) :</strong> Isolateurs rouges garantissant une tenue diélectrique supérieure à 2,5kV vis-à-vis de la masse du tableau.</li>
  <li><strong>Vis avec Étriers de Protection :</strong> Assurent une pression homogène sur les brins sans les cisailler lors du serrage.</li>
</ol>
'''
)

NL_ES = dict(
    lang='es',
    dir='ltr',
    slug='distribution-switchboards-what-is-a-neutral-link-es',
    title='Tableros de Distribución Eléctrica: ¿Qué es una Barra de Neutro (Neutral Link)?',
    breadcrumb='Terminales y Conectores',
    read='10 min de lectura',
    alt='Barra seccionable de neutro en latón macizo (Modelo YM-NL) montada sobre aisladores en tablero general de distribución eléctrica',
    desc=('Tableros generales de distribución en baja tensión y cuadros industriales: ¿Qué es una barra de neutro (neutral link)? '
          'Latón macizo de alta conductividad, aisladores ignífugos de poliamida y puente seccionable para pruebas de aislamiento con megóhmetro.'),
    model='Serie YM-NL / TB: Barras Seccionables de Neutro y Barras de Tierra en Latón Macizo (4 a 48 Vías, hasta 250A)',
    category='Terminales y Conectores / Barras de Neutro y Barras de Tierra',
    kw='barra de neutro &middot; neutral link &middot; bornera de neutro &middot; barra seccionable neutro &middot; bornera tierra tablero',
    specs=[
        ('Composición del Perfil y Calidad de Latón', 'Latón macizo extruido de alta conductividad y fácil mecanizado (Cu &ge; 58–60%, Pb &le; 2,5%, balance Zn) o cobre puro'),
        ('Tensión Asignada de Servicio y Aislamiento', 'Tensión nominal de empleo hasta 690V / 1000V AC; rigidez dieléctrica de los aisladores probada a 2,5kV AC / 1 minuto'),
        ('Capacidad de Corriente Continua Admisible', 'Gama de corrientes nominales continuas: 63A, 100A, 160A y hasta 250A para el conductor neutro principal de acometida'),
        ('Número de Vías de Conexión Disponibles', 'Disponible en longitudes estándar de 4, 6, 8, 12, 18, 24, 36 y 48 vías (para cables de 1,5 mm&sup2; a 35 mm&sup2;)'),
        ('Puente Central Seccionable Desmontable', 'Puente apernado de cobre/latón que permite desconectar físicamente la barra sin soltar los cables de los circuitos'),
        ('Soportes Aisladores de Montaje al Chasis', 'Montada sobre aisladores de columna en poliamida ignífuga (PA66 / UL 94 V-0) rígidamente aislados del chasis metálico'),
        ('Tornillería de Apriete y Protección de Hilos', 'Tornillos de apriete de latón o acero cincado de alta resistencia con placas de presión para no cortar los hilos del cable'),
        ('Normativas Internacionales de Fabricación', 'Fabricada en total conformidad con normas IEC 61439-1, IEC 61439-2 y EN 60947-7-1 para cuadros de distribución')
    ],
    faqs=[
        ('¿Qué es una Barra de Neutro (Neutral Link) y cuál es su función en un tablero de distribución eléctrica?',
         'Una Barra de Neutro—denominada en cuadros eléctricos como neutral link, barra colectora de neutro o bornera seccionable de neutro—es '
         'una barra maciza de latón o cobre mecanizada con múltiples orificios y tornillos, montada sobre aisladores plásticos dentro del tablero. '
         'Su función es concentrar todos los cables neutros ($N$) de los circuitos derivados y unirlos con el neutro principal de la acometida eléctrica. '
         'En un tablero de distribución general, cumple tres misiones fundamentales: '
         '<ul>'
         '<li><strong>1. Retorno Seguro de la Corriente:</strong> En circuitos monofásicos y cargas trifásicas desequilibradas, la corriente de retorno '
         'circula permanentemente por el neutre. Una barra de latón macizo garantiza un punto de bajísima resistencia que no se recalienta.</li>'
         '<li><strong>2. Prevención del "Neutro Flotante":</strong> Si el neutro se afloja o corta en un sistema trifásico, el centro de estrella se desplaza. '
         'Las fases con menor carga reciben tensiones de hasta 400V en lugar de 230V, quemando electrodomésticos, variadores y luminarias LED.</li>'
         '<li><strong>3. Seccionamiento para Pruebas:</strong> Posee un puente apernado desmontable que permite aislar el neutro del transformador '
         'para realizar pruebas de resistencia de aislamiento con megóhmetro sin tener que desconectar decenas de conductores.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia crítica entre una Barra de Neutro y una Barra de Tierra?',
         'Aunque a menudo comparten dimensiones similares, su régimen eléctrico y aislamiento son completamente opuestos: '
         '<ul>'
         '<li><strong>Barra de Neutro (Conductor Activo):</strong> Conduce corriente continuamente durante la operación normal del edificio. '
         'Por esta razón, DEBE estar eléctricamente aislada del chasis metálico del tablero mediante soportes aisladores de poliamida roja. '
         'Si el neutro tocara el chasis, dispararía instantáneamente los interruptores diferenciales (RCD).</li>'
         '<li><strong>Barra de Tierra (Conductor de Protección PE):</strong> Conduce corriente ÚNICAMENTE ante fallas a tierra. '
         'Va apernada directamente al metal del tablero sin aisladores para asegurar que toda la envolvente esté al potencial de tierra.</li>'
         '</ul>'),
        ('¿Por qué es obligatorio el puente seccionable en la barra de neutro?',
         'Las normativas eléctricas exigen ensayos periódicos de <strong>resistencia de aislamiento con megóhmetro</strong> aplicando 500V o 1000V DC. '
         'Si el neutro del edificio estuviera conectado a la red pública durante la prueba, la tensión de prueba se derivaría a tierra en el transformador. '
         'Al retirar los tornillos del puente central seccionable, la barra de neutro queda totalmente aislada de la red en segundos, '
         'permitiendo verificar el aislamiento de todos los circuitos de la instalación con total precisión.')
    ],
    cta='¿Fabrica tableros generales de distribución (TGBT), cuadros de control industrial o centros de carga que requieren barras de neutro seccionables bajo norma IEC 61439? YOMIN fabrica barras colectoras de neutro en latón mecanizado de alta precisión.',
    body='''
<h2>El Punto Central de Retorno en Cuadros Eléctricos de Baja Tensión</h2>
<p>En el interior de cualquier tablero de distribución eléctrica—desde un cuadro domiciliario hasta un centro de control de motores (CCM) industrial—la energía eléctrica se reparte a decenas de circuitos ramales.</p>
<p>Mientras que cada fase está controlada por interruptores automáticos, la totalidad de las corrientes de retorno de las cargas monofásicas debe volver al transformador a través del <strong>conductor neutro ($N$)</strong>.</p>
<p>Conectar los neutros con empalmes precarios genera puntos calientes peligrosos y el riesgo crítico de la "pérdida de neutro", que somete los equipos monofásicos a 400V destructivos.</p>
<p>La <strong>Barra Seccionable de Neutro (Serie YM-NL / TB)</strong> proporciona la solución de ingeniería estandarizada: un bloque robusto de latón macizo aislado de la envolvente metálica, diseñado para conducir altas corrientes continuas y permitir el seccionamiento para pruebas.</p>

<h2>Elementos de Diseño y Seguridad</h2>
<ol>
  <li><strong>Cuerpo Macizo de Latón Extruido:</strong> Mecanizado con tolerancias exactas para admitir pares de apriete elevados sin falsear las roscas.</li>
  <li><strong>Puente Central Seccionable Apernado:</strong> Permite aislar el conjunto de neutros en segundos para ensayos dieléctricos con megóhmetro a 1000V DC.</li>
  <li><strong>Aisladores de Columna Ignífugos (PA66, UL 94 V-0):</strong> Soportes aislantes de alta resistencia dieléctrica (&ge; 2,5kV AC) que aíslan la barra del chasis metálico.</li>
  <li><strong>Tornillos con Placas Protectoras de Hilos:</strong> Evitan el cizallamiento de los hilos de cobre finos al apretar las conexiones.</li>
</ol>
'''
)

NL_AR = dict(
    lang='ar',
    dir='rtl',
    slug='distribution-switchboards-what-is-a-neutral-link-ar',
    title='لوحات التوزيع الكهربائية والقواطع: ما هو قضيب الربط المعزول للحيادي (Neutral Link)؟',
    breadcrumb='المرابط والموصلات الكهربائية',
    read='10 دقائق قراءة',
    alt='قضيب ربط الحيادي المعزول القابل للفصل المصنوع من النحاس الأصفر الصلب (موديل YM-NL) مثبت على عوازل داخل لوحة توزيع رئيسية (MDB)',
    desc=('لوحات التوزيع الكهربائية الرئيسية (MDB) ولوحات القواطع الفرعية: ما هو قضيب ربط الحيادي (Neutral Link)؟ '
          'نحاس أصفر صلب عالي التوصيل، عوازل بوليمرية مقاومة للهب، وجسر فصل يدوي لإجراء اختبارات مقاومة العزل بالميجر بأمان تام.'),
    model='سلسلة YM-NL / TB: قضبان ربط الحيادي القابلة للفصل وقضبان التأريض من النحاس الأصفر الصلب (من 4 إلى 48 مخرج، حتى 250A)',
    category='المرابط والموصلات / قضبان الحيادي والتأريض (Neutral & Earth Bars)',
    kw='قضيب حيادي &middot; neutral link &middot; بارة نيوترال &middot; بارة ارضي لوحة توزيع &middot; فاصل نيوترال &middot; بارة نحاس اصفر',
    specs=[
        ('تركيب مادة القضيب ونقاوة النحاس الأصفر', 'نحاس أصفر صلب مسحوب عالي النقاوة والتوصيل الكهربائي (Cu &ge; 58–60%، مع الزنك) أو نحاس أحمر نقي حسب الطلب'),
        ('جهد التشغيل المقنن ومستوى العزل المعتمد', 'جهد تشغيل مقنن يصل إلى 690V / 1000V AC؛ جهد صمود العوازل مختبر عند 2.5kV AC لمدة دقيقة كاملة'),
        ('سعة التيار الاسمي المستمر للقضيب', 'سعات تيار مستمر قياسية معيارية: 63A، 100A، 160A وحتى 250A لتيار موصل الحيادي الرئيسي المغذي'),
        ('عدد المخارج ونقاط التوصيل المتاحة', 'متوفر بأطوال معيارية تضم 4، 6، 8، 12، 18، 24، 36، و 48 مخرجاً (تستوعب أسلاكاً بمقاطع 1.5 مم&sup2; حتى 35 مم&sup2;)'),
        ('جسر الفصل المركزي القابل للفك السريع', 'وصلة ربط جسرية نحاسية مربوطة بمسامير تتيح عزل الحيادي كلياً دون الحاجة لفك أسلاك الدوائر الفرعية المنفردة'),
        ('قواعد التثبيت والأعمدة العازلة المقاومة', 'مثبت على أعمدة عازلة حمراء من البولي أميد المقاوم للهب (PA66 / UL 94 V-0) لعزل القضيب عن هيكل اللوحة المعدني'),
        ('مسامير التثبيت وصفائح حماية الأسلاك', 'مسامير ربط مجلفنة عالية القوة مع صفائح ضغط تمنع تمزق شعيرات الأسلاك النحاسية الدقيقة أثناء الشد'),
        ('المعايير الدولية والمطابقة الهندسية', 'مصنع ومطابق للمواصفات القياسية الدولية IEC 61439-1 و IEC 61439-2 و BS 7671 للوحات الجهد المنخفض')
    ],
    faqs=[
        ('ما هو قضيب ربط الحيادي (Neutral Link) وما هي أهميته القصوى في لوحات التوزيع الكهربائية؟',
         'قضيب ربط الحيادي—والمعروف في ورش تجميع اللوحات الكهربائية باسم بارة النيوترال المعزولة أو وصلة الحيادي القابلة للفصل—هو '
         'قضيب معدني مصمت ومصنع بدقة من النحاس الأصفر (Brass)، يُثبت على عوازل كهربائية خاصة داخل لوحة التوزيع. '
         'وظيفته الأساسية هي تجميع وتوحيد جميع أسلاك الحيادي ($N$) القادمة من دوائر الأحمال الفرعية، وربطها بالموصل الحيادي الرئيسي القادم من المحول. '
         'يؤدي هذا القضيب ثلاث وظائف حيوية: '
         '<ul>'
         '<li><strong>1. مسار آمن لتيار العودة:</strong> في الدوائر أحادية الطور والأحمال ثلاثية الطور غير المتزنة، يمر تيار العودة بالحيادي باستمرار. '
         'ويوفر القضيب النحاسي مساراً فائق التوصيل وذا مقاومة شبه منعدمة يمنع السخونة ونشوب الحرائق.</li>'
         '<li><strong>2. منع كارثة "الحيادي العائم" (Floating Neutral):</strong> في حال ارتخاء أو انقطاع سلك الحيادي في شبكة ثلاثية الأطوار، '
         'تتعرض الأجهزة أحادية الطور لجهد مدمر يصل إلى 400V بدلاً من 230V، مما يؤدي لاحتراق كافة الأجهزة والشاشات في المبنى فورياً.</li>'
         '<li><strong>3. الفصل السريع لإجراء اختبارات العزل:</strong> يحتوي القضيب على جسر ميكانيكي بمسامير يتيح فصل الحيادي عن شبكة الكهرباء العامة '
         'بضغطة مفك واحدة لإجراء اختبارات العزل بجهاز الميجر دون الحاجة لفك عشرات الأسلاك.</li>'
         '</ul>'),
        ('ما هو الفارق الجوهري الفاصل بين قضيب الحيادي (Neutral Link) وقضيب التأريض (Earth Bar)؟',
         'رغم تشابههما الخارجي في الشكل، إلا أن طبيعة عملهما وعزلهما متناقضان كلياً: '
         '<ul>'
         '<li><strong>قضيب الحيادي (موصل تشغيلي حي):</strong> يحمل تيار العودة في ظروف التشغيل العادية. '
         'لذلك، يَجِب أن يكون معزولاً كلياً عن جسم اللوحة المعدني بواسطة أعمدة عازلة حمراء من البولي أميد المقاوم للهب. '
         'ولو لامس الحيادي جسم اللوحة، فستفصل قواطع التسريب الأرضي (RCD/ELCB) على الفور.</li>'
         '<li><strong>قضيب التأريض (موصل حماية PE):</strong> لا يحمل أي تيار إلا في لحظة حدوث عطل أو انهيار عازل. '
         'لذلك، يُربط قضيب الأرضي مباشرة بهيكل اللوحة المعدني دون أي عوازل لتأمين التوصيل الكامل مع شبكة التأريض.</li>'
         '</ul>'),
        ('لماذا تفرض المواصفات القياسية وجود جسر فصل قابل للفك (Disconnecting Link) على قضيب الحيادي؟',
         'تفرض معايير التفتيش الكهربائي (مثل IEC 60364-6 و BS 7671) إجراء <strong>اختبارات مقاومة العزل الدورية (Megger Test)</strong> بحقن جهد 500V أو 1000V DC. '
         'إذا بقي قضيب الحيادي متصلاً بمحول شبكة الكهرباء العامة أثناء الفحص، فسوف تتسرب شحنة الفحص إلى الأرض عبر نقطة تعادل المحول وتتلف عدادات القياس الإلكترونية. '
         'بفك مسماري الجسر المركزي، يُعزل حيادي المبنى بالكامل عن الشبكة في ثوانٍ معدودة، مما يتيح فحص عازلية كافة الدوائر بدقة وسرعة فائقة.')
    ],
    cta='هل تعمل على تصنيع لوحات التوزيع الكهربائية الرئيسية (MDB)، أو لوحات التحكم الصناعي، أو وحدات التوزيع الفرعية المطابقة لمواصفة IEC 61439؟ تصنع يمين (YOMIN) قضبان ربط الحيادي والتأريض النحاسية الصلبة فائقة الجودة.',
    body='''
<h2>شريان العودة الحيوي في منظومات توزيع الكهرباء منخفضة الجهد</h2>
<p>في كل لوحة توزيع كهربائية—بدءاً من لوحات القواطع المنزلية الصغيرة وحتى لوحات التوزيع الرئيسية للمصانع (MDB)—تتوزع الطاقة الكهربائية إلى عشرات الدوائر الفرعية المغذية للإنارة والمكيفات والآلات.</p>
<p>وبينما تقوم القواطع الآلية بحماية خطوط الأطوار الحية ($L_1, L_2, L_3$)، فإن تيارات العودة الناتجة عن الأحمال أحادية الطور يجب أن تعود بأمان تام إلى المحول عبر <strong>موصل الحيادي ($N$)</strong>.</p>
<p>إن توصيل أسلاك الحيادي بروابط عشوائية أو روزيتات بلاستيكية ضعيفة يسبب سخونة شديدة وخطر "انقطاع الحيادي" الكارثي الذي يقفز بالجهد إلى 400V ويحرق المعدات الإلكترونية الحساسة.</p>
<p>يمثل <strong>قضيب ربط الحيادي المعزول القابل للفصل (سلسلة YM-NL / TB)</strong> الحل الهندسي المعتمد: قضيب مصمت من النحاس الأصفر مثبت على عوازل بوليمرية، يضمن تحملاً حرارياً فائقاً وإمكانية عزل فوري لإجراء الاختبارات الدورية.</p>

<h2>المكونات الهندسية وميزات الأمان المتقدمة</h2>
<ol>
  <li><strong>جسم من النحاس الأصفر الصلب المسحوب:</strong> يوفر توصيلاً كهربائياً ممتازاً ومخارج مسننة بدقة تتحمل عزم الربط الشديد دون تلف السنون.</li>
  <li><strong>جسر فصل مركزي قابل للفك بمسامير:</strong> يتيح عزل شبكة الحيادي فورياً لإجراء فحوصات الميجر بجهد 1000V DC دون لمس أسلاك الأحمال.</li>
  <li><strong>أعمدة تثبيت عازلة مقاومة للهب (PA66, UL 94 V-0):</strong> عوازل أسطوانية حمراء تضمن عزلاً كهربائياً يفوق 2.5kV AC عن جسم اللوحة المعدني.</li>
  <li><strong>مسامير ربط مدعومة بصفائح واقية:</strong> تمنع تلف وقص شعيرات الأسلاك النحاسية الدقيقة أثناء شد المسامير.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1006 = [
    ESC_EN, ESC_FR, ESC_ES, ESC_AR,
    NL_EN, NL_FR, NL_ES, NL_AR
]
