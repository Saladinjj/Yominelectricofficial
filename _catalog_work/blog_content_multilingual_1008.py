# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-08:
1. Industrial Control Transformers (JBK5) for Automation Panels (EN, FR, ES, AR)
2. Busbar Insulation Boots & Shrouds for Switchgear (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. INDUSTRIAL CONTROL TRANSFORMER (EN, FR, ES, AR)
# ==============================================================================

ICT_EN = dict(
    lang='en',
    dir='ltr',
    slug='industrial-control-panels-what-is-a-control-transformer',
    title='Industrial Control Panels & Automation: What Is a Control Transformer?',
    breadcrumb='Transformers &amp; Voltage Control',
    read='10 min read',
    alt='Heavy-duty single-phase Industrial Control Transformer (Model JBK5 series) with vacuum-varnished copper windings installed in an industrial CNC machine tool control panel',
    desc=('Industrial machinery control panels, CNC machine tools, and motor control centers (MCC): What is an industrial control transformer (CPT)? '
          'How galvanic isolation, stepped-down auxiliary voltages (24V/110V/220V AC), high inrush VA capacity, and IEC 61558-2-2 standards ensure reliable automation control.'),
    model='Model JBK5 Series Machine Tool Industrial Control Power Transformers (100VA to 5000VA, Primary 220V/380V/415V/480V, Secondary 24V/110V/220V AC)',
    category='Transformers & Voltage Control / Control Transformers (JBK5)',
    kw='what is a control transformer &middot; control transformer &middot; industrial control transformer &middot; machine tool transformer &middot; jbk5 transformer &middot; cpt transformer',
    specs=[
        ('Primary Rated Input Voltages', 'Multi-tap primary options: 220V, 380V, 400V, 415V, 440V, or 480V AC &plusmn; 5% at 50/60 Hz'),
        ('Secondary Auxiliary Output Voltages', 'Standard isolated secondary taps: 24V AC, 36V AC, 110V/120V AC, 220V/230V AC (isolated control and signaling power)'),
        ('Continuous Power Rating Capacity', 'Modular standard continuous power capacities: 100VA, 160VA, 250VA, 400VA, 500VA, 800VA, 1000VA, 1600VA, up to 5000VA'),
        ('Momentary Inrush VA Sizing Capability', 'High instantaneous inrush current capacity: delivers 300% to 800% of rated VA during contactor/solenoid pickup without voltage collapse'),
        ('Core Material & Magnetic Treatment', 'High-permeability, low-loss grain-oriented cold-rolled silicon steel laminations (CRGO) annealed for minimal eddy current losses'),
        ('Coil Winding & Vacuum Impregnation', 'Precision-wound Class F/H electrolytic copper magnet wire vacuum pressure impregnated (VPI) with high-grade insulating varnish'),
        ('Terminal Block & Fuse Protection Options', 'Touch-safe finger-proof IP20 screw terminal blocks; optional integrated primary and secondary fuse holders with status indicators'),
        ('Applicable International Quality Standards', 'Certified to IEC 61558-1, IEC 61558-2-2, EN 60204-1 (electrical equipment of machines), UL 5085, and CE/RoHS')
    ],
    faqs=[
        ('What is an Industrial Control Transformer (CPT) and why can control circuits NOT be powered directly from main supply lines?',
         'An Industrial Control Transformer—frequently abbreviated as a CPT (Control Power Transformer) or machine tool transformer—is '
         'a specialized single-phase, dry-type step-down isolation transformer engineered specifically to supply stable, low-voltage power '
         'to control circuit devices such as magnetic motor contactor coils, relays, timers, PLCs, solenoids, pilot lights, and emergency stop circuits. '
         'Powering control circuits directly from primary three-phase lines (e.g., 380V, 415V, or 480V AC) is forbidden in modern industrial panels for three critical reasons: '
         '<ul>'
         '<li><strong>1. Personnel Safety & Shock Hazard:</strong> Pushbuttons, foot pedals, limit switches, and cabinet indicator lamps are accessible to machine operators. '
         'Stepping down voltage to a safe control potential (such as 24V AC or 110V AC) drastically minimizes the risk of fatal electric shock during operation or maintenance.</li>'
         '<li><strong>2. Galvanic Isolation Against Supply Noise:</strong> Industrial mains supply lines suffer from severe voltage spikes, harmonic distortion, and lightning transients. '
         'A control transformer provides complete magnetic galvanic isolation between the primary utility feed and the secondary control loop, '
         'blocking common-mode electrical noise that would otherwise reset PLCs or damage sensitive microprocessor controls.</li>'
         '<li><strong>3. Ground Fault Containment:</strong> In an isolated secondary control loop, a single ground fault does not immediately trip the main upstream feeder breaker, '
         'preventing uncontrolled emergency machine shutdowns and allowing controlled diagnostic stopping.</li>'
         '</ul>'),
        ('How does the "Inrush VA" capacity of a control transformer differ from its continuous rated VA?',
         'When an electromechanical magnetic contactor or pneumatic solenoid valve energizes, its magnetic core is initially unseated (open air-gap). '
         'In this state, the coil exhibits extremely low inductive reactance, drawing a massive momentary <strong>inrush current equal to 6 to 10 times '
         'its normal sealed holding current</strong> for the first 30 to 50 milliseconds. '
         'Standard lighting or distribution transformers have high internal impedance; under such inrush surges, their output voltage severely collapses, '
         'causing contactors to chatter, weld contacts, or fail to pull in completely. '
         'YOMIN JBK5 Industrial Control Transformers are custom-engineered with heavy-gauge copper windings and high-saturation silicon steel cores '
         'that exhibit exceptionally low internal regulation impedance (&le; 5% to 8%). They deliver up to <strong>800% of their continuous VA rating '
         'momentarily while maintaining secondary voltage above 90% of nominal</strong>, ensuring instantaneous, positive contactor pickup every single cycle.'),
        ('What is the difference between an Autotransformer and an Isolated Industrial Control Transformer?',
         'The distinction lies in physical winding separation and electrical isolation: '
         '<ul>'
         '<li><strong>Autotransformer (Non-Isolated):</strong> Uses a single continuous winding where the secondary voltage is tapped from part of the same coil. '
         'While compact and cost-effective for pure voltage stepping (such as variacs or motor starters), it provides ZERO galvanic isolation. '
         'A primary line spike or ground fault passes directly through to the secondary side, making it unsafe for operator control circuits.</li>'
         '<li><strong>Control Transformer (Galvanically Isolated):</strong> Built with two or more physically separate, electrically insulated windings '
         '(primary and secondary) linked exclusively through magnetic induction. '
         'This provides complete electrical separation between the utility grid and control wiring, complying strictly with machine safety standard EN 60204-1.</li>'
         '</ul>')
    ],
    cta='Manufacturing industrial automation panels, motor control centers (MCC), CNC machine tools, or HVAC control cabinets requiring certified, heavy-duty industrial control transformers (100VA to 5000VA)? YOMIN manufactures precision-engineered JBK5 transformers.',
    body='''
<h2>The Electrical Foundation of Industrial Automation and Machinery Control</h2>
<p>Inside modern manufacturing plants, automated assembly lines, and CNC machine shops, industrial control panels house thousands of delicate control components: programmable logic controllers (PLCs), magnetic motor starters, safety relays, and human-machine interfaces (HMIs).</p>
<p>While heavy industrial machinery operates on high primary line voltages—such as <strong>380V, 415V, or 480V AC three-phase</strong>—delicate control relays and operator pushbuttons require safe, regulated auxiliary voltages such as <strong>24V AC, 110V AC, or 220V AC</strong>.</p>
<p>Attempting to power control circuits directly from the mains or using unrated commercial transformers leads to nuisance contactor chatter, PLC reboots from electrical noise, and hazardous operator shock risks.</p>
<p>The <strong>Industrial Control Transformer (Model JBK5 Series)</strong> provides the standardized solution: a heavy-duty, dry-type galvanic isolation transformer engineered for high momentary inrush capability, tight voltage regulation, and robust thermal endurance under continuous 24/7 industrial duty.</p>

<h2>Engineering Anatomy: Inside a Model JBK5 Machine Tool Control Transformer</h2>
<ol>
  <li><strong>High-Permeability Grain-Oriented Silicon Steel Core:</strong> Precision-stamped CRGO laminations tightly clamped with anti-vibration brackets to minimize no-load excitation losses and acoustic hum.</li>
  <li><strong>Vacuum Pressure Impregnated (VPI) Copper Windings:</strong> Heavy-gauge Class F (155&deg;C) or Class H (180&deg;C) insulated copper magnet wire vacuum-baked with golden electrical varnish to resist industrial moisture, dust, and vibration.</li>
  <li><strong>Exceptionally Low Voltage Regulation Impedance:</strong> Designed to supply massive instantaneous inrush currents (up to 8&times; rated VA) without dropping secondary control voltage below contactor pull-in thresholds.</li>
  <li><strong>Multi-Tap Primary &amp; Secondary Terminal Configurations:</strong> Multi-voltage primary taps (e.g., 220V/380V/415V/480V) allow international machine builders to export standardized panels globally without redesigning internal controls.</li>
  <li><strong>Touch-Safe IP20 Terminal Blocks with Integral Fuse Clips:</strong> Finger-proof shrouded terminal screws prevent accidental contact by maintenance technicians and accommodate optional midget fuses directly on the transformer frame.</li>
</ol>

<h2>Comparison: Industrial Control Transformer (JBK5) vs. Standard Distribution Transformer vs. Switched-Mode DC Power Supply (SMPS)</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>Standard Distribution Transformer</th>
      <th>YOMIN JBK5 Industrial Control Transformer</th>
      <th>Switched-Mode DC Power Supply (SMPS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Momentary Inrush VA Handling</strong></td>
      <td>Poor: High internal impedance causes severe secondary voltage collapse under coil pickup.</td>
      <td><strong>Superior: Low regulation impedance handles 300%–800% inrush VA with &lt; 10% voltage drop.</strong></td>
      <td>Poor: Trips into overcurrent foldback / hiccup mode under heavy inductive surges.</td>
    </tr>
    <tr>
      <td><strong>Galvanic Isolation &amp; Noise Rejection</strong></td>
      <td>Moderate: Interwinding capacitance passes high-frequency noise spikes.</td>
      <td><strong>High: Electrostatic shielding and dielectric isolation block utility harmonics and spikes.</strong></td>
      <td>Electronic isolation; sensitive to lightning surges and high-temperature degradation.</td>
    </tr>
    <tr>
      <td><strong>Output Voltage Type &amp; Applications</strong></td>
      <td>Stepped-down AC for general utility power.</td>
      <td><strong>Isolated AC (24V, 110V, 220V) for AC contactor coils, solenoids, and AC control loops.</strong></td>
      <td>Regulated 24V DC for sensors, PLCs, and digital electronic modules.</td>
    </tr>
    <tr>
      <td><strong>Thermal Resilience in Sealed Panels</strong></td>
      <td>Standard Class B insulation (130&deg;C limit).</td>
      <td><strong>Class F/H insulation (155&deg;C/180&deg;C) withstands hot, enclosed industrial control cabinets.</strong></td>
      <td>Electrolytic capacitors dry out rapidly in ambient temperatures above 50&deg;C.</td>
    </tr>
    <tr>
      <td><strong>Machine Safety Standard Compliance</strong></td>
      <td>Not rated for industrial machine tools.</td>
      <td><strong>Fully compliant with IEC 61558-2-2 and EN 60204-1 (Safety of Machinery).</strong></td>
      <td>Complies with low-voltage directive; requires auxiliary filtering for inductive kickback.</td>
    </tr>
  </tbody>
</table>
'''
)

ICT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='industrial-control-panels-what-is-a-control-transformer-fr',
    title="Armoires de Contrôle Industriel & Automatismes : Qu'est-ce qu'un Transformateur de Commande ?",
    breadcrumb='Transformateurs &amp; Régulation',
    read='10 min de lecture',
    alt='Transformateur de commande industrielle monophasé haute performance (Modèle JBK5) monté dans une armoire électrique de machine-outil CNC',
    desc=('Armoires de commande industrielle, machines-outils CNC et centres de contrôle moteurs (CCM) : Qu\'est-ce qu\'un transformateur de commande (CPT) ? '
          'Isolation galvanique, abaissement des tensions auxiliaires (24V/110V/220V AC), gestion des courants d\'appel (inrush VA) et norme CEI 61558-2-2.'),
    model='Série JBK5 : Transformateurs de Commande et de Puissance pour Machines-Outils (100VA à 5000VA, Primaire 220V/380V/415V/480V, Secondaire 24V/110V/220V AC)',
    category='Transformateurs & Régulation / Transformateurs de Commande (JBK5)',
    kw='transformateur de commande &middot; transformateur industriel &middot; transformateur jbk5 &middot; transformateur machine outil &middot; transformateur cpt &middot; alimentation commande 24v',
    specs=[
        ('Tensions Primaires Assignées d\'Entrée', 'Prises primaires multiples : 220V, 380V, 400V, 415V, 440V ou 480V AC &plusmn; 5% à 50/60 Hz'),
        ('Tensions Secondaires Isolées de Sortie', 'Sorties auxiliaires normalisées : 24V AC, 36V AC, 110V/120V AC, 220V/230V AC (circuits de commande et relayage)'),
        ('Puissance Continue Assignée (VA)', 'Gamme modulaire standard : 100VA, 160VA, 250VA, 400VA, 500VA, 800VA, 1000VA, 1600VA jusqu\'à 5000VA'),
        ('Capacité d\'Absorption du Courant d\'Appel', 'Capacité instantanée exceptionnelle : délivre 300% à 800% de la puissance assignée lors de l\'enclenchement des bobines'),
        ('Qualité du Circuit Magnétique', 'Tôles d\'acier au silicium à grains orientés (CRGO) à faibles pertes, recuites et traitées contre les courants de Foucault'),
        ('Bobinages et Imprégnation sous Vide', 'Cuivre électrolytique de classe thermique F/H imprégné sous vide et pression (VPI) de vernis isolant haute tenue'),
        ('Bornier de Raccordement et Protection', 'Bornier à vis protégé IP20 contre les contacts directs ; porte-fusibles amovibles intégrés en option'),
        ('Normes Internationales de Sécurité', 'Certifié selon les normes CEI 61558-1, CEI 61558-2-2, NF EN 60204-1 (sécurité des machines) et directives CE/RoHS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transformateur de Commande (CPT) et pourquoi est-il indispensable dans une armoire industrielle ?',
         'Un Transformateur de Commande—souvent appelé transformateur de machine-outil ou transformateur d\'isolement de contrôle—est '
         'un transformateur monophasé de type sec conçu spécifiquement pour alimenter les circuits de pilotage et de relayage '
         '(bobines de contacteurs, relais de sécurité, électrovannes, automates programmables et voyants lumineux) sous une tension réduite et stabilisée. '
         'L\'alimentation directe des circuits de commande par le réseau triphasé principal (380V ou 480V) est strictement proscrite pour trois raisons : '
         '<ul>'
         '<li><strong>1. Sécurité des Opérateurs :</strong> Les boutons-poussoirs, pédales et arrêts d\'urgence sont manipulés par le personnel. '
         'Abaisser la tension à un niveau sécurisé (24V ou 110V AC) réduit drastiquement le danger d\'électrocution en cas de contact accidentel.</li>'
         '<li><strong>2. Isolation Galvanique contre les Parasites :</strong> Les commutations de gros moteurs créent des harmoniques et des pointes de surtension. '
         'Le transformateur de commande forme une barrière magnétique étanche qui bloque ces perturbations, évitant les plantages d\'automates (PLC).</li>'
         '<li><strong>3. Maîtrise des Défauts d\'Isolement :</strong> Un premier défaut à la terre sur le circuit secondaire isolé n\'entraîne pas la disjonction '
         'générale immédiate de l\'usine, permettant d\'arrêter la machine de manière ordonnée et sécurisée.</li>'
         '</ul>'),
        ('Pourquoi la notion de puissance d\'appel (Inrush VA) est-elle capitale lors du dimensionnement ?',
         'Lorsqu\'un contacteur moteur ou une électrovanne s\'enclenche, son entrefer magnétique est ouvert. '
         'Pendant les 30 à 50 premières millisecondes, la bobine absorbe un <strong>courant d\'appel équivalent à 6 à 10 fois son courant de maintien</strong>. '
         'Un transformateur standard ordinaire s\'écroulerait en tension, provoquant le mitraillage des contacteurs et le soudage de leurs contacts. '
         'Les transformateurs de commande YOMIN JBK5 possèdent une impédance interne extrêmement basse. Ils sont capables de fournir '
         'instantanément jusqu\'à <strong>8 fois leur puissance nominale en conservant plus de 90% de la tension secondaire</strong>, assurant un collage net et franc des contacteurs.'),
        ('Quelle est la différence entre un Autotransformateur et un Transformateur de Commande Isolé ?',
         'La différence réside dans la séparation physique des enroulements : '
         '<ul>'
         '<li><strong>Autotransformateur (Sans Isolation) :</strong> Possède un enroulement unique commun au primaire et au secondaire. '
         'Bien qu\'économique, il ne procure AUCUNE isolation galvanique : une surtension primaire se répercute directement sur les boutons de commande.</li>'
         '<li><strong>Transformateur de Commande (Isolé Galvaniquement) :</strong> Comporte deux bobinages séparés reliés uniquement par flux magnétique. '
         'Il garantit une isolation totale conforme à la norme NF EN 60204-1 (Sécurité électrique des machines).</li>'
         '</ul>')
    ],
    cta='Vous concevez des armoires d\'automatismes industriels, des centres de commande moteurs (CCM) ou des machines-outils nécessitant des transformateurs de commande certifiés CEI 61558-2-2 ? YOMIN fabrique des transformateurs industriels JBK5 de haute précision.',
    body='''
<h2>Le Cœur Fiable de la Commande et de l\'Automatisme Industriel</h2>
<p>Dans les usines modernes et les lignes de fabrication automatisées, les armoires électriques abritent des organes de pilotage sophistiqués : automates programmables (PLC), contacteurs moteurs, relais de temporisation et interfaces homme-machine (IHM).</p>
<p>Alors que la force motrice des moteurs utilise de fortes tensions triphasées (<strong>380V, 400V ou 480V AC</strong>), les circuits de commande et boutons d\'arrêt d\'urgence exigent une tension basse et parfaitement isolée (<strong>24V AC, 110V AC ou 220V AC</strong>).</p>
<p>Utiliser une alimentation non protégée ou un transformateur standard mal calibré conduit inévitablement à des baisses de tension lors de l\'enclenchement des moteurs, provoquant le relâchement intempestif des contacteurs.</p>
<p>Le <strong>Transformateur de Commande Industrielle (Série JBK5)</strong> apporte la solution technique robuste : un transformateur sec à isolation galvanique renforcée, spécialement optimisé pour délivrer d\'immenses pointes de courant d\'appel avec une stabilité de tension exemplaire.</p>

<h2>Caractéristiques et Avantages Technologiques</h2>
<ol>
  <li><strong>Circuit Magnétique en Tôles d\'Acier au Silicium CRGO :</strong> Réduit les pertes à vide et élimine les vibrations sonores dans l\'armoire électrique.</li>
  <li><strong>Bobinages en Cuivre de Classe F/H Imprégnés sous Vide (VPI) :</strong> Résistent aux ambiances industrielles chaudes, humides et poussiéreuses.</li>
  <li><strong>Très Faible Impédance de Régulation :</strong> Absorbe les courants d\'appel des bobines de contacteurs sans chute de tension perturbatrice.</li>
  <li><strong>Prises Primaires et Secondaires Modulaires :</strong> Permettent d\'adapter facilement une même machine pour l\'exportation internationale.</li>
</ol>
'''
)

ICT_ES = dict(
    lang='es',
    dir='ltr',
    slug='industrial-control-panels-what-is-a-control-transformer-es',
    title='Tableros de Control Industrial y Automatización: ¿Qué es un Transformador de Control?',
    breadcrumb='Transformadores y Regulación',
    read='10 min de lectura',
    alt='Transformador de control industrial monofásico de servicio pesado (Modelo JBK5) instalado en tablero eléctrico de máquina herramienta CNC',
    desc=('Tableros de control industrial, maquinaria CNC y centros de control de motores (CCM): ¿Qué es un transformador de control (CPT)? '
          'Aislamiento galvánico, reducción a tensiones seguras (24V/110V/220V AC), capacidad de corriente de arranque (inrush VA) y norma IEC 61558-2-2.'),
    model='Serie JBK5: Transformadores de Potencia y Control Industrial para Máquinas Herramienta (100VA a 5000VA, Primario 220V/380V/415V/480V, Secundario 24V/110V/220V AC)',
    category='Transformadores y Regulación / Transformadores de Control (JBK5)',
    kw='transformador de control &middot; transformador industrial &middot; transformador jbk5 &middot; transformador maquina herramienta &middot; transformador cpt &middot; transformador 24v control',
    specs=[
        ('Tensiones Primarias de Entrada Asignadas', 'Múltiples tomas primarias: 220V, 380V, 400V, 415V, 440V o 480V AC &plusmn; 5% a 50/60 Hz'),
        ('Tensiones Secundarias Aisladas de Salida', 'Tomas normalizadas aisladas: 24V AC, 36V AC, 110V/120V AC, 220V/230V AC (alimentación de maniobra)'),
        ('Capacidad de Potencia Continua (VA)', 'Gama modular estándar: 100VA, 160VA, 250VA, 400VA, 500VA, 800VA, 1000VA, 1600VA hasta 5000VA'),
        ('Capacidad de Potencia de Arranque (Inrush VA)', 'Capacidad de sobrecorriente instantánea: suministra 300% a 800% de la potencia nominal durante el cierre de bobinas'),
        ('Núcleo Magnético de Altas Prestaciones', 'Chapas de acero al silicio de grano orientado (CRGO) de bajas pérdidas, recocidas contra corrientes parásitas'),
        ('Bobinado de Cobre e Impregnación al Vacío', 'Conductor de cobre electrolítico clase térmica F/H impregnado con barniz dieléctrico bajo presión y vacío (VPI)'),
        ('Bornera de Conexión y Opciones de Fusible', 'Borneras atornilladas protegidas IP20 contra contactos accidentales; portafusibles integrados en opción'),
        ('Cumplimiento de Normativas Internacionales', 'Certificado bajo normas IEC 61558-1, IEC 61558-2-2, EN 60204-1 (Seguridad de las máquinas), UL 5085 y CE/RoHS')
    ],
    faqs=[
        ('¿Qué es un Transformador de Control (CPT) y por qué es fundamental en tableros de automatización?',
         'Un Transformador de Control—denominado frecuentemente como transformador para máquinas herramienta o CPT (Control Power Transformer)—es '
         'un transformador reductor monofásico de tipo seco con aislamiento galvánico, diseñado específicamente para suministrar energía estable '
         'a los componentes de control y maniobra (bobinas de contactores, relés de seguridad, electroválvulas, temporizadores, PLCs y pulsadores). '
         'Alimentar los mandos directamente desde la red trifásica de fuerza (380V o 480V) está prohibido en tableros modernos por tres razones vitales: '
         '<ul>'
         '<li><strong>1. Seguridad Eléctrica del Operario:</strong> Los pulsadores y paradas de emergencia son manipulados por personas. '
         'Reducir el voltaje a niveles de seguridad (24V o 110V AC) elimina el peligro de choques eléctricos letales en caso de falla.</li>'
         '<li><strong>2. Aislamiento Galvánico y Filtrado de Ruido:</strong> La red eléctrica industrial presenta picos y armónicos causados por motores. '
         'El transformador de control crea una barrera magnética que bloquea estas interferencias, evitando reseteos inesperados de autómatas programables (PLCs).</li>'
         '<li><strong>3. Control de Fallas a Tierra:</strong> Un fallo a tierra en el circuito secundario aislado no dispara el interruptor principal de la planta, '
         'permitiendo una detención segura y controlada del proceso productivo.</li>'
         '</ul>'),
        ('¿Por qué es crucial considerar la potencia de arranque (Inrush VA) al seleccionar el transformador?',
         'Cuando la bobina de un contactor electromagnético o solenoide se energiza, su armadura magnética está abierta. '
         'Durante los primeros 30 a 50 milisegundos, la bobina consume una <strong>corriente de arranque instantánea entre 6 y 10 veces mayor que su corriente nominal</strong>. '
         'Un transformador de distribución convencional sufriría una caída drástica de voltaje, provocando el rebote del contactor y soldadura de platinos. '
         'Los transformadores YOMIN JBK5 poseen una impedancia interna muy reducida, entregando hasta <strong>8 veces su potencia continua momentáneamente '
         'manteniendo más del 90% del voltaje secundario</strong>, garantizando un cierre enérgico y seguro de los contactores.'),
        ('¿Cuál es la diferencia entre un Autotransformador y un Transformador de Control con Aislamiento?',
         'La diferencia radica en la separación física de los devanados: '
         '<ul>'
         '<li><strong>Autotransformador (Sin Aislamiento):</strong> Comparte un único bobinado para entrada y salida. '
         'Aunque es compacto y económico para regular voltaje, NO proporciona aislamiento galvánico: cualquier perturbación o falla primaria pasa directamente al mando.</li>'
         '<li><strong>Transformador de Control (Aislamiento Galvánico):</strong> Posee devanados primario y secundario completamente independientes acoplados magnéticamente. '
         'Cumple estrictamente la norma EN 60204-1 para la seguridad eléctrica en maquinaria industrial.</li>'
         '</ul>')
    ],
    cta='¿Fabrica tableros de control industrial, centros de control de motores (CCM) o maquinaria CNC que requieren transformadores de control certificados bajo norma IEC 61558-2-2? YOMIN fabrica transformadores industriales JBK5 de alto rendimiento.',
    body='''
<h2>El Núcleo Eléctrico Seguro para Tableros de Automatización Industrial</h2>
<p>En plantas manufactureras modernas, centros de mecanizado CNC y líneas de producción, los tableros de control albergan elementos electrónicos de alta precisión: autómatas programables (PLCs), arrancadores magnéticos y relés de protección.</p>
<p>Mientras que la fuerza motriz opera a altas tensiones trifásicas de <strong>380V, 415V o 480V AC</strong>, la botonera de control y las señales auxiliares exigen tensiones reducidas y aisladas de <strong>24V AC, 110V AC o 220V AC</strong>.</p>
<p>Alimentar los mandos sin un transformador adecuado provoca caídas de tensión que impiden el accionamiento de los contactores y somete a los operarios a graves riesgos eléctricos.</p>
<p>El <strong>Transformador de Control Industrial (Serie JBK5)</strong> ofrece la solución electromecánica estándar: un transformador de tipo seco con aislamiento galvánico reforzado, diseñado para entregar grandes potencias de arranque instantáneo manteniendo un voltaje secundario impecable.</p>

<h2>Elementos de Diseño y Robustez Constructiva</h2>
<ol>
  <li><strong>Núcleo Magnético de Acero al Silicio CRGO:</strong> Minimiza las pérdidas en vacío y suprime zumbidos molestos dentro del gabinete.</li>
  <li><strong>Devanados de Cobre Clase F/H con Barnizado al Vacío (VPI):</strong> Protegen contra la humedad, polvo industrial y vibraciones continuas.</li>
  <li><strong>Muy Baja Impedancia de Regulación:</strong> Suministra corrientes de inrush elevadas sin caídas de tensión que afecten a los contactores.</li>
  <li><strong>Borneras Protegidas IP20:</strong> Evitan contactos accidentales durante labores de mantenimiento conforme a la directiva de seguridad en máquinas.</li>
</ol>
'''
)

ICT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='industrial-control-panels-what-is-a-control-transformer-ar',
    title='لوحات التحكم الصناعي والأتمتة: ما هو محول التحكم الصناعي (Control Transformer)؟',
    breadcrumb='المحولات والتحكم بالجهد',
    read='10 دقائق قراءة',
    alt='محول تحكم صناعي أحادي الطور عالي الأداء للمكائن (موديل JBK5) بملفات نحاسية مغمورة بالورنيش داخل لوحة تحكم ماكينة CNC',
    desc=('لوحات التحكم في الآلات الصناعية، وماكينات CNC، ومراكز التحكم بالمحركات (MCC): ما هو محول التحكم الصناعي (CPT)؟ '
          'العزل الجلفاني التام، وخفض الجهود المساعدة (24V/110V/220V AC)، وقدرة امتصاص تيارات البدء العالية (Inrush VA)، ومطابقة معيار IEC 61558-2-2.'),
    model='سلسلة JBK5: محولات القدرة والتحكم الصناعي لماكينات الورش والتحكم الآلي (سعات من 100VA إلى 5000VA، جهود 220V/380V/415V/480V حتى 24V/110V/220V AC)',
    category='المحولات والتحكم بالجهد / محولات التحكم الصناعي (JBK5)',
    kw='محول تحكم صناعي &middot; محول تحكم &middot; محول jbk5 &middot; محول ماكينات cnc &middot; محول cpt &middot; محول 24v لوحات تحكم',
    specs=[
        ('جهود الدخل الابتدائية المقننة', 'خيارات متعددة للأطراف الابتدائية: 220V، 380V، 400V، 415V، 440V أو 480V AC &plusmn; 5% بتردد 50/60 هرتز'),
        ('جهود الخرج الثانوية المعزولة', 'مخارج تشغيل معيارية معزولة: 24V AC، 36V AC، 110V/120V AC، 220V/230V AC (لتغذية دوائر التحكم والإشارة)'),
        ('سعة القدرة التشغيلية المستمرة (VA)', 'سعات قياسية معيارية: 100VA، 160VA، 250VA، 400VA، 500VA، 800VA، 1000VA، 1600VA وحتى 5000VA'),
        ('سعة تحمل تيار البدء اللحظي (Inrush VA)', 'قدرة فائقة على امتصاص تيار التعشيق اللحظي: يمد الدائرة بـ 300% إلى 800% من قدرته المقننة دون انهيار الجهد'),
        ('مادة وجودة القلب المغناطيسي', 'صفائح فولاذ سيليكوني موجه الحبيبات عالي النفاذية (CRGO) ومعالج حرارياً لتقليل الفواقد المغناطيسية والتيارات الدوامية'),
        ('الملفات النحاسية والعزل بالورنيش', 'ملفات نحاس كهرولي نقية من الفئة الحرارية F/H معالجة بالتشريب بالورنيش العازل تحت الضغط والتفريغ الهوائي (VPI)'),
        ('أطراف التوصيل وخيارات الحماية بالفيوزات', 'مرابط أطراف لولبية آمنة للمس بالأصابع IP20؛ مع إمكانية إضافة قواعد فيوزات مدمجة لحماية دوائر الدخل والخرج'),
        ('المواصفات القياسية الدولية المعتمدة', 'مطابق كلياً للمواصفات الدولية IEC 61558-1 و IEC 61558-2-2 و EN 60204-1 (سلامة المعدات الكهربائية للآلات) و CE')
    ],
    faqs=[
        ('ما هو محول التحكم الصناعي (CPT) ولماذا لا يمكن تغذية دوائر التحكم مباشرة من خطوط الكهرباء الرئيسية؟',
         'محول التحكم الصناعي—والمعروف في التطبيقات الهندسية باسم محول الماكينات أو محول قدرة التحكم (Control Power Transformer)—هو '
         'محول خافض للجهد أحادي الطور من النوع الجاف ذو عزل جلفاني تام، مصمم خصيصاً لتزويد أجهزة التحكم والتشغيل '
         '(مثل بكرات الكونتاكتورات المغناطيسية، والريليهات، وصمامات السولينويد، ووحدات الـ PLC، ومفاتيح الإيقاف الطارئ) بجهد كهربائي منخفض وثابت. '
         'إن توصيل دوائر التحكم مباشرة بجهود القوى الرئيسية (مثل 380V أو 480V) يُعد محظوراً في اللوحات الحديثة لثلاثة أسباب رئيسية: '
         '<ul>'
         '<li><strong>1. حماية أرواح المشغلين من الصعق:</strong> يتعامل عمال المصانع مع أزرار التشغيل، والدواسات، ومفاتيح الطوارئ باستمرار. '
         'إن خفض الجهد إلى قيم آمنة (مثل 24V أو 110V AC) يلغي خطر الصعق الكهربائي القاتل في بيئات العمل الرطبة أو المعرضة للتلف الميكانيكي.</li>'
         '<li><strong>2. العزل الجلفاني وحجب التوافقيات:</strong> تتسبب محركات المصانع الكبرى في توليد شوشرة وارتفاعات مفاجئة في الجهد. '
         'يوفر محول التحكم عزلاً مغناطيسياً نقياً يحجب هذه الطفرات، مانعاً إعادة تشغيل أجهزة الـ PLC أو تلف كروت التحكم الحساسة.</li>'
         '<li><strong>3. حصر الأعطال الأرضية:</strong> في دائرة التحكم الثانوية المعزولة، لا يؤدي حدوث عطل أرضي أحادي إلى فصل القاطع العام للمصنع فورياً، '
         'مما يتيح إيقاف الماكينة بأمان دون تخريب خطوط الإنتاج.</li>'
         '</ul>'),
        ('ما هو الفرق بين قدرة التحمل اللحظية (Inrush VA) والقدرة المستمرة لمحول التحكم؟',
         'عندما تتلقى بكرة الكونتاكتور أو صمام السولينويد إشارة التفعيل، يكون قلبها المغناطيسي مفتوحاً. '
         'في هذه اللحظة (خلال أول 30 إلى 50 مليثانية)، تسحب البكرة <strong>تيار بدء هائل يعادل 6 إلى 10 أضعاف تيارها التشغيلي الدائم</strong>. '
         'إذا استُخدم محول عادي ذو ممانعة مرتفعة، فسوف ينهار الجهد فجأة، مما يسبب رفرفة الكونتاكتور وصهر وتلف نقاط تلامسه فورياً. '
         'تتميز محولات يمين JBK5 بممانعة داخلية بالغة الانخفاض، تمكنها من تزويد <strong>ما يصل إلى 800% من قدرتها المقننة لحظياً '
         'مع الحفاظ على أكثر من 90% من الجهد الاسمي</strong>، مما يضمن تعشيقاً قوياً وموثوقاً للكونتاكتورات في كل دورة تشغيل.'),
        ('ما هو الفارق بين المحول الذاتي (Autotransformer) ومحول التحكم الصناعي المعزول؟',
         'الفارق الجوهري يكمن في الفصل الفيزيائي للملفات: '
         '<ul>'
         '<li><strong>المحول الذاتي (غير معزول):</strong> يحتوي على ملف واحد مشترك بين الدخل والخرج. '
         'ورغم أنه اقتصادي وصغير الحجم، إلا أنه لا يوفر أي عزل جلفاني: فأي قصر أو شرارة في الجهد العالي تنتقل مباشرة لأزرار المشغلين.</li>'
         '<li><strong>محول التحكم الصناعي (عزل جلفاني تام):</strong> يحتوي على ملفين منفصلين ومتباعدين كلياً، وينتقل الجهد بينهما مغناطيسياً فقط. '
         'وهذا يضمن الامتثال الصارم لمعيار سلامة الماكينات الصناعية EN 60204-1.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع لوحات التحكم بالأتمتة الصناعية، أو مراكز التحكم بالمحركات (MCC)، أو ماكينات CNC التي تتطلب محولات تحكم مطابقة لمواصفة IEC 61558-2-2؟ تصنع يمين (YOMIN) محولات تحكم صناعية متطورة سلسلة JBK5 بأعلى مستويات الاعتمادية.',
    body='''
<h2>صمام الأمان الأساسي لمنظومات التحكم والأتمتة الصناعية</h2>
<p>في المصانع الحديثة وخطوط الإنتاج المؤتمتة وورش الماكينات الموجهة بالكمبيوتر (CNC)، تضم لوحات التحكم مئات العناصر الدقيقة: أجهزة التحكم المنطقي القابل للبرمجة (PLC)، وبكرات تشغيل المحركات، والريليهات، وشاشات المشغلين (HMI).</p>
<p>وبينما تعمل المحركات الكبرى بجهود تشغيل ثلاثية الأطوار مرتفعة تصل إلى <strong>380V أو 415V أو 480V AC</strong>، فإن أزرار التحكم والريليهات تتطلب جهوداً منخفضة وآمنة تماماً مثل <strong>24V AC أو 110V AC أو 220V AC</strong>.</p>
<p>إن محاولة تغذية دوائر المانول من الخطوط العامة دون محول متخصص يؤدي إلى انهيار الجهد عند تعشيق المحركات، مما يعطل الإنتاج ويهدد سلامة المشغلين.</p>
<p>يمثل <strong>محول التحكم الصناعي (سلسلة JBK5)</strong> الحل الهندسي القياسي: محول جاف ذو عزل جلفاني تام مصمم خصيصاً لتحمل تيارات التعشيق الهائلة للكونتاكتورات مع الحفاظ على استقرار الجهد تحت أقصى ظروف التشغيل الصناعي المستمر.</p>

<h2>المكونات الهندسية وميزات المتانة والتصنيع</h2>
<ol>
  <li><strong>قلب مغناطيسي من شرائح الفولاذ السيليكوني CRGO:</strong> يحد من فواقد المغنطة والحرارة ويلغي أي اهتزازات أو طنين صوتي داخل اللوحة.</li>
  <li><strong>ملفات نحاسية نقية معزولة بالورنيش تحت التفريغ الهوائي (VPI):</strong> تضمن مقاومة فائقة للرطوبة، والغبار الصناعي، والاهتزازات الميكانيكية.</li>
  <li><strong>ممانعة تنظيم جهد فائقة الانخفاض:</strong> تمد بكرات المحركات بتيارات بدء تصل إلى 8 أضعاف القدرة دون أي هبوط يعيق عمل القواطع.</li>
  <li><strong>مرابط أطراف لولبية آمنة للمس (IP20):</strong> تحمي أيدي فنيي الصيانة من الصعق الكهربائي وتوفر إمكانية تركيب فيوزات الحماية مباشرة.</li>
</ol>
'''
)

# ==============================================================================
# 2. BUSBAR INSULATION BOOT (EN, FR, ES, AR)
# ==============================================================================

BIB_EN = dict(
    lang='en',
    dir='ltr',
    slug='switchgear-busbar-joints-what-is-a-busbar-insulation-boot',
    title='Switchgear Busbar Joints & Terminations: What Is a Busbar Insulation Boot?',
    breadcrumb='Busbar Protection &amp; Insulation',
    read='10 min read',
    alt='Heavy-duty pre-molded Busbar Insulation Boots (Model YM-BS series) installed over bolted copper busbar tee-joints and elbow connections in a medium-voltage switchgear cabinet',
    desc=('Medium-voltage switchgear cabinets (11kV to 36kV), transformer bushings, and compact substations: What is a busbar insulation boot? '
          'How pre-molded dip-coated PVC/silicone boots, high dielectric breakdown strength, and reusable snap fasteners eliminate manual tape wrapping and prevent wildlife flashovers.'),
    model='Model YM-BS Series Medium-Voltage Pre-Molded Busbar Insulation Boots & Protective Shrouds (T-Joints, Elbows, Straight Joints, up to 36kV)',
    category='Busbar Protection & Insulation / Busbar Insulation Boots',
    kw='what is a busbar insulation boot &middot; busbar insulation boot &middot; busbar boot &middot; switchgear busbar shroud &middot; insulation shroud for busbar &middot; busbar joint cover',
    specs=[
        ('Rated System Operating Voltage Class', 'Engineered for low-voltage and medium-voltage applications from 1kV, 11kV, 24kV, up to 36kV AC distribution switchgear'),
        ('Dielectric Breakdown Strength & Proof', 'High dielectric strength &ge; 25 kV/mm; rated power-frequency withstand test voltage up to 95kV / 1 minute (dry)'),
        ('Material Composition & Elasticity', 'High-grade dip-molded polyvinyl chloride (PVC) elastomer, silicone rubber, or cross-linked polyolefin (radiation-vulcanized)'),
        ('Fire Retardancy & Temperature Class', 'Flame-retardant formulation certified to UL 94 V-0; continuous operating temperature range: -40&deg;C to +105&deg;C (up to 150&deg;C for silicone)'),
        ('Standard Joint Geometry Configurations', 'Pre-molded geometries available: Straight Inline Couplers, 90&deg; Elbow Bends, T-Connections, and Transformer Bushing Shrouds'),
        ('Fastening & Reusability Mechanism', 'Removable, reusable flame-retardant nylon snap-rivets, plastic push-pin fasteners, or heat-shrinkable adhesive collars'),
        ('Environmental & Chemical Resistance', 'Outstanding resistance to tracking, ozone degradation, industrial sulfur hexafluoride (SF6) byproducts, acids, and UV radiation'),
        ('Applicable International Quality Standards', 'Manufactured and type-tested to IEC 60060-1, IEC 62271-200 (AC metal-enclosed switchgear), IEEE C37.20.2, and RoHS')
    ],
    faqs=[
        ('What is a Busbar Insulation Boot and why is it used over bolted busbar joints in switchgear?',
         'A Busbar Insulation Boot—also widely termed a busbar shroud, switchgear insulating boot, or joint cover—is '
         'a pre-molded, high-dielectric flexible polymer shroud engineered specifically to enclose bolted copper or aluminium busbar connections '
         '(such as tees, 90-degree elbows, straight splice joints, and transformer bushing terminations) inside electrical switchgear cabinets. '
         'In modern medium-voltage and low-voltage distribution switchboards, busbar boots are essential for three primary engineering reasons: '
         '<ul>'
         '<li><strong>1. Flashover Prevention in Compact Cabinets:</strong> Urban substations demand compact switchgear enclosures with minimal phase-to-phase '
         'and phase-to-earth clearances. Exposed live bolted copper joints create intense electric field gradients at bolt heads and sharp edges. '
         'Installing a high-dielectric busbar boot suppresses corona discharges and prevents catastrophic phase-to-phase flashovers under lightning or switching surges.</li>'
         '<li><strong>2. Elimination of Labor-Intensive Tape Wrapping:</strong> Historically, electricians wrapped live busbar joints with multiple layers '
         'of self-amalgamating rubber tape and PVC tape—a laborious process requiring 30 to 45 minutes per joint that produces inconsistent insulation thickness. '
         'A pre-molded busbar boot slips over the joint and snaps shut with nylon fasteners in under 60 seconds with factory-guaranteed dielectric wall thickness.</li>'
         '<li><strong>3. Reusability for Thermal & Torque Inspections:</strong> Utility regulations require periodic infrared thermography and bolt torque inspections. '
         'Taped joints must be laboriously sliced away and discarded. A busbar boot can be opened in seconds for thermal inspection and re-installed repeatedly without damage.</li>'
         '</ul>'),
        ('How do busbar boots mitigate wildlife intrusions and environmental contamination in substations?',
         'Substations, outdoor kiosk units, and industrial switchgear rooms are vulnerable to environmental contamination and small wildlife intrusions '
         '(such as rodents, geckos, snakes, birds, or dust accumulation). '
         'When an animal enters an uninsulated switchboard and bridges the air gap between adjacent live phase busbars, it creates a dead short-circuit '
         'resulting in a devastating explosive arc flash, destroying entire switchgear lineups and causing regional blackouts. '
         'Busbar insulation boots form a continuous, touch-proof insulating barrier over all exposed metal terminations. '
         'Even if a rodent or lizard climbs directly across the busbars, the thick dielectric boot prevents electrical contact, '
         'completely eliminating animal-induced outages and saving utility operators millions in equipment replacement costs.'),
        ('What are the key material differences between PVC dip-molded boots and Silicone Rubber shrouds?',
         'The choice depends on operating voltage, ambient temperature, and mechanical requirements: '
         '<ul>'
         '<li><strong>Dip-Molded PVC Elastomer:</strong> Cost-effective, mechanically rugged, and highly flexible. Certified for continuous temperatures '
         'up to 105&deg;C and voltages up to 24kV. Ideal for standard indoor low-voltage switchboards, motor control centers, and medium-voltage distribution panels.</li>'
         '<li><strong>Silicone Rubber:</strong> Superior hydrophobic (water-repellent) properties, non-flammable, and resistant to extreme temperatures '
         '(-50&deg;C to +150&deg;C). Certified for applications up to 36kV and outdoor or coastal transformer bushings exposed to salt fog, condensation, and high UV radiation.</li>'
         '</ul>')
    ],
    cta='Manufacturing medium-voltage switchgear lineups, compact transformer substations, or industrial distribution switchboards requiring certified 1kV to 36kV busbar insulation boots and shrouds? YOMIN manufactures pre-molded busbar protection accessories.',
    body='''
<h2>The Pre-Molded Protective Shield for Modern Electrical Switchgear</h2>
<p>Inside low-voltage and medium-voltage <strong>electrical switchgear cabinets (1kV to 36kV)</strong>, primary power is routed through heavy rectangular copper and aluminium busbars. At busbar intersections—where incoming feeders branch into distribution circuit breakers—conductors are mechanically joined using high-tensile steel bolts, nuts, and washers.</p>
<p>These bolted busbar joints represent the most electrically vulnerable points in the entire switchboard. The sharp edges of hex bolts, Belleville washers, and overlapping copper bars concentrate electric field stress, creating localized ionization that drastically lowers the breakdown voltage of the surrounding air.</p>
<p>Furthermore, compact urban switchgear designs deliberately minimize physical phase clearances to reduce cabinet footprints. In these cramped busbar chambers, a single transient voltage surge, moisture condensation, or an intruding rodent can trigger a devastating phase-to-phase electrical flashover.</p>
<p>The <strong>Busbar Insulation Boot (Model YM-BS Series)</strong> provides the standardized utility solution: pre-molded, high-dielectric flexible insulating covers that slip over bolted busbar joints in seconds, delivering factory-certified insulation up to 36kV without messy tapes.</p>

<h2>Engineering Anatomy: Inside a Certified Medium-Voltage Busbar Insulation Boot</h2>
<ol>
  <li><strong>Engineered Dielectric Wall Thickness (&ge; 25 kV/mm):</strong> High-purity dip-molded polymer material delivers uniform insulation thickness across all complex curves, sharp corners, and bolt head recesses.</li>
  <li><strong>Pre-Molded Joint Geometries (T-Joints, Elbows, Splices):</strong> Anatomically shaped cavities match standard copper bar dimensions (e.g., 30&times;5mm up to 120&times;10mm), enclosing single and double busbar configurations cleanly.</li>
  <li><strong>Reusable Snap-Fit Fastener System:</strong> Molded eyelets secured with high-dielectric nylon push-pins allow maintenance teams to open the boot in 10 seconds for annual infrared thermography inspections.</li>
  <li><strong>Flame-Retardant &amp; Self-Extinguishing Polymer (UL 94 V-0):</strong> Will not support combustion or propagate flame in the event of an internal electrical fire or thermal overload.</li>
  <li><strong>Silicone Hydrophobic Surface Coating:</strong> Repels water droplets and condensation, preventing the formation of conductive moisture films in humid tropical or coastal substation environments.</li>
</ol>

<h2>Comparison: Pre-Molded Busbar Insulation Boot vs. Manual Self-Amalgamating Tape Wrapping vs. Heat-Shrink Tubing</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Manual Self-Amalgamating Tape</th>
      <th>YOMIN Pre-Molded Busbar Insulation Boot</th>
      <th>Heat-Shrink Insulating Tubing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Installation Time per Joint</strong></td>
      <td>Slow: 30 to 45 minutes of tedious manual wrapping aloft.</td>
      <td><strong>Instant: Under 60 seconds; slip over joint and push snap-rivets.</strong></td>
      <td>Moderate: Requires sliding over bar before bolting and gas torch heating.</td>
    </tr>
    <tr>
      <td><strong>Insulation Uniformity &amp; Quality</strong></td>
      <td>Unpredictable: Dependent on installer skill, tension, and overlap percentage.</td>
      <td><strong>Factory Controlled: Exact, uniform dielectric wall thickness across every surface.</strong></td>
      <td>Uniform along straight runs; thins unpredictably over sharp bolt heads.</td>
    </tr>
    <tr>
      <td><strong>Reusability for Maintenance &amp; Torque Check</strong></td>
      <td>Non-reusable: Must be cut away with knives and entirely replaced.</td>
      <td><strong>100% Reusable: Unfasten snap-rivets for IR scanning and re-close in seconds.</strong></td>
      <td>Non-reusable: Must be sliced off and re-shrunk with an open flame torch.</td>
    </tr>
    <tr>
      <td><strong>Open Flame Hazard During Installation</strong></td>
      <td>None (cold tape application).</td>
      <td><strong>Zero Hazard: 100% cold snap-fit application without tools or heat sources.</strong></td>
      <td>High: Requires propane torches or heat guns inside tight, solvent-rich panels.</td>
    </tr>
    <tr>
      <td><strong>Wildlife &amp; Flashover Protection</strong></td>
      <td>Prone to air voids and peeling over years of cyclic heat.</td>
      <td><strong>Heavy-duty thick dielectric shell completely shields metal from wildlife contact.</strong></td>
      <td>Good, but requires supplementary end-caps on complex tee joints.</td>
    </tr>
  </tbody>
</table>
'''
)

BIB_FR = dict(
    lang='fr',
    dir='ltr',
    slug='switchgear-busbar-joints-what-is-a-busbar-insulation-boot-fr',
    title="Jeu de Barres & Raccordements Haute Tension : Qu'est-ce qu'un Capuchon Isolant de Barre (Busbar Boot) ?",
    breadcrumb='Protection &amp; Isolation des Jeux de Barres',
    read='10 min de lecture',
    alt='Capuchons isolants préformés pour jeux de barres (Série YM-BS) installés sur des raccords en té et en équerre dans une cellule moyenne tension',
    desc=('Cellules moyenne tension (11kV à 36kV), traversées de transformateurs et postes compacts : Qu\'est-ce qu\'un capuchon isolant de barre (busbar boot) ? '
          'Élastomère PVC/silicone préformé haute rigidité diélectrique, fixation par rivets clipsables sans rubanage et protection contre les arcs électriques.'),
    model='Série YM-BS : Capuchons et Coiffes Isolantes Préformées pour Jeux de Barres Moyenne et Basse Tension (Tés, Équerres, Traversées, jusqu\'à 36kV)',
    category='Protection & Isolation des Jeux de Barres / Capuchons Isolants (Busbar Boots)',
    kw='capuchon isolant jeu de barres &middot; busbar boot &middot; coiffe isolante barre &middot; isolation raccordement cellule hta &middot; protection jeu de barres 24kv',
    specs=[
        ('Classe de Tension Assignée de Service', 'Conçu pour les réseaux basse et moyenne tension de 1kV, 11kV, 24kV jusqu\'à 36kV en appareillage sous enveloppe métallique'),
        ('Rigidité Diélectrique et Tenue au Choc', 'Rigidité diélectrique élevée &ge; 25 kV/mm ; tension de tenue à fréquence industrielle jusqu\'à 95kV / 1 min (à sec)'),
        ('Composition et Élasticité du Polymère', 'Élastomère de PVC haute pureté moulé par trempage, silicone réticulé ou polyoléfine autoextinguible'),
        ('Comportement au Feu et Plage Thermique', 'Formulation ignifugée certifiée UL 94 V-0 ; température de service continu : -40&deg;C à +105&deg;C (jusqu\'à 150&deg;C en silicone)'),
        ('Formes Géométriques Normalisées', 'Configurations préformées : Manchons droits, Équerres à 90&deg;, Raccords en Té et Coiffes pour traversées de transformateurs'),
        ('Système de Fermeture et Réutilisabilité', 'Fermeture par rivets plastiques amovibles en nylon ignifugé ou colliers clipsables réutilisables à volonté'),
        ('Résistance Chimique et Environnementale', 'Excellente tenue au cheminement électrique, à l\'ozone, aux sous-produits du SF6, à l\'humidité et aux rayons UV'),
        ('Conformité aux Normes Internationales', 'Fabriqué et testé selon les normes CEI 60060-1, CEI 62271-200 (appareillage HTA sous enveloppe), IEEE C37 et RoHS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Capuchon Isolant de Jeu de Barres (Busbar Boot) et pourquoi est-il indispensable dans une cellule HTA ?',
         'Un Capuchon Isolant de Jeu de Barres—couramment appelé busbar boot, coiffe isolante ou capot de raccordement—est '
         'une enveloppe polymère souple préformée à très haute rigidité diélectrique, conçue spécifiquement pour recouvrir '
         'les jonctions boulonnées entre barres de cuivre ou d\'aluminium (telles que les dérivations en Té, les coudes à 90° et les traversées) dans les cellules électriques. '
         'Dans les postes de distribution moyenne et basse tension, il remplit trois rôles techniques majeurs : '
         '<ul>'
         '<li><strong>1. Prévention des Arcs Électriques et Amorçages :</strong> Dans les cellules compactes modernes, les distances d\'isolement '
         'entre phases sont réduites au strict minimum. Les têtes de boulons et arêtes vives du cuivre concentrent le champ électrique. '
         'Le capuchon isolant supprime les effets de pointe et empêche les amorçages destructeurs entre phases lors de surtensions de foudre.</li>'
         '<li><strong>2. Élimination du Rubanage Manuel :</strong> Autrefois, isoler un raccordement exigeait 30 à 45 minutes d\'enroulement manuel de ruban '
         'auto-amalgamant, avec une épaisseur très aléatoire. Le capuchon préformé s\'enfile et se verrouille par rivets en moins d\'une minute avec une épaisseur garantie.</li>'
         '<li><strong>3. Réutilisation Immédiate pour la Thermographie :</strong> Les contrôles périodiques de maintenance exigent de mesurer l\'échauffement '
         'des boulons par caméra infrarouge. Le capuchon se déclipse en quelques secondes pour le contrôle et se referme sans aucune dégradation.</li>'
         '</ul>'),
        ('Comment les capuchons isolants protègent-ils les postes contre les intrusions d\'animaux ?',
         'Les postes de transformation et armoires de distribution sont fréquemment infiltrés par de petits animaux '
         '(rongeurs, geckos, serpents ou oiseaux cherchant la chaleur des équipements). '
         'Lorsqu\'un animal franchit la distance d\'isolement dans l\'air entre deux barres nues, il provoque un court-circuit franc monstrueux, '
         'déclenchant une explosion d\'arc électrique et privant d\'électricité des milliers d\'usagers. '
         'Les capuchons isolants YOMIN forment une armure isolante continue et étanche sur l\'ensemble des métaux nus. '
         'Même si un rongeur touche directement le capuchon, la barrière diélectrique prévient tout amorçage, évitant des réparations colossales.</li>'),
        ('Quelle est la différence entre le PVC moulé et le Caoutchouc Silicone ?',
         'Le choix dépend des conditions d\'exploitation : '
         '<ul>'
         '<li><strong>PVC Élastomère Moulé :</strong> Économique, très souple et d\'une grande robustesse mécanique. Idéal pour les cellules intérieures '
         'jusqu\'à 24kV et des températures atteignant 105&deg;C.</li>'
         '<li><strong>Caoutchouc Silicone :</strong> Totalement hydrophobe (repousse l\'eau et la condensation), ininflammable et résistant '
         'de -50&deg;C à +150&deg;C. Indispensable pour les applications sévères jusqu\'à 36kV et les traversées extérieures exposées aux brouillards salins.</li>'
         '</ul>')
    ],
    cta='Vous assemblez des cellules moyenne tension (HTA), des postes de transformation compacts ou des armoires de distribution nécessitant des capuchons isolants de barre certifiés jusqu\'à 36kV ? YOMIN produit des accessoires d\'isolation de jeux de barres haute performance.',
    body='''
<h2>La Protection Diélectrique Préformée des Postes de Distribution Moderne</h2>
<p>Dans les <strong>cellules et armoires de distribution électrique moyenne tension (1kV à 36kV)</strong>, l\'énergie transite par d\'épaisses barres de cuivre massif. Aux points de jonction où les câbles et disjoncteurs se raccordent, les barres sont assemblées par des boulons et rondelles en acier à haute résistance.</p>
<p>Ces jonctions boulonnées constituent les zones les plus vulnérables du tableau électrique. Les têtes hexagonales des vis et les arêtes tranchantes créent de redoutables effets de pointe qui concentrent le champ électrostatique, réduisant la tenue diélectrique de l\'air ambiant.</p>
<p>Dans les cellules modernes très compactes, la moindre humidité, condensation ou intrusion animale peut provoquer un arc électrique dévastateur entre phases.</p>
<p>Le <strong>Capuchon Isolant de Barre (Série YM-BS)</strong> apporte la solution normalisée : des coiffes isolantes préformées de haute rigidité diélectrique qui s\'installent en quelques secondes sans flamme ni ruban adhésif salissant.</p>

<h2>Caractéristiques et Avantages Technologiques</h2>
<ol>
  <li><strong>Épaisseur Diélectrique Calibrée en Usine :</strong> Garantit une isolation homogène et sans bulles d\'air supérieure à 25 kV/mm sur l\'ensemble des arêtes vives.</li>
  <li><strong>Formes Adaptées à Toutes les Configurations :</strong> Modèles spécifiques pour tés de dérivation, coudes d\'angle et bornes de transformateurs.</li>
  <li><strong>Fermeture Rapide par Rivets Plastiques Amovibles :</strong> Permet d\'ouvrir et refermer la coiffe en 10 secondes pour les inspections thermographiques infrarouges.</li>
  <li><strong>Polymère Autoextinguible Homologué UL 94 V-0 :</strong> Ne propage pas la flamme et n\'émet pas de gouttes incandescentes en cas de surchauffe.</li>
</ol>
'''
)

BIB_ES = dict(
    lang='es',
    dir='ltr',
    slug='switchgear-busbar-joints-what-is-a-busbar-insulation-boot-es',
    title='Uniones de Barras Colectoras y Transformadores: ¿Qué es una Bota Aislante para Barras (Busbar Boot)?',
    breadcrumb='Protección y Aislamiento de Barras',
    read='10 min de lectura',
    alt='Botas aislantes preformadas para barras colectoras (Serie YM-BS) instaladas en uniones en T y codos dentro de celda de media tensión',
    desc=('Celdas de media tensión (11kV a 36kV), pasamuros de transformadores y centros de transformación: ¿Qué es una bota aislante para barras (busbar boot)? '
          'Elastómero de PVC/silicona preformado, alta rigidez dieléctrica, cierre con remaches desmontables sin cintas y prevención de arcos por animales.'),
    model='Serie YM-BS: Botas y Cubiertas Aislantes Preformadas para Barras Colectoras en Media y Baja Tensión (Derivaciones en T, Codos, Pasamuros, hasta 36kV)',
    category='Protección y Aislamiento de Barras / Botas Aislantes (Busbar Boots)',
    kw='bota aislante barras &middot; busbar boot &middot; capuchon aislante barras &middot; aislante celdas media tension &middot; cubierta aislante pletina cobre',
    specs=[
        ('Clase de Tensión Asignada de Servicio', 'Diseñado para aplicaciones de baja y media tensión desde 1kV, 11kV, 24kV hasta 36kV en celdas blindadas bajo envolvente metálica'),
        ('Rigidez Dieléctrica y Tensión de Ensayo', 'Elevada rigidez dieléctrica &ge; 25 kV/mm; tensión soportada a frecuencia industrial hasta 95kV / 1 minuto (en seco)'),
        ('Composición y Elasticidad del Material', 'Elastómero de PVC de alta pureza por inmersión, caucho de silicona hidrofóbico o poliolefina reticulada'),
        ('Comportamiento ante el Fuego y Temperatura', 'Formulación autoextinguible certificada UL 94 V-0; temperatura continua de servicio: -40&deg;C a +105&deg;C (hasta 150&deg;C en silicona)'),
        ('Geometrías Normalizadas Disponibles', 'Modelos preformados: Manguitos rectos, Codos a 90&deg;, Uniones en T y Cubiertas para bornes de transformadores'),
        ('Mecanismo de Fijación y Reutilización', 'Cierre por remaches plásticos desmontables de poliamida ignífuga o abrazaderas reutilizables sin herramientas'),
        ('Resistencia Química y Ambiental', 'Excelente resistencia al tracking eléctrico, ozono, subproductos de SF6, ácidos industriales, humedad y rayos UV'),
        ('Cumplimiento de Normas Internacionales', 'Fabricado y ensayado según normas IEC 60060-1, IEC 62271-200 (celdas de media tensión), IEEE C37 y directiva RoHS')
    ],
    faqs=[
        ('¿Qué es una Bota Aislante para Barras Colectoras (Busbar Boot) y por qué se instala en celdas de media tensión?',
         'Una Bota Aislante para Barras—conocida internacionalmente como busbar boot, capuchón aislante o bota para pletinas—es '
         'una cubierta polimérica preformada y flexible de altísima rigidez dieléctrica, moldeada anatómicamente para cubrir '
         'las conexiones apernadas entre barras de cobre o aluminio (como derivaciones en T, codos a 90° y bornes de transformador) dentro de celdas eléctricas. '
         'En la distribución de media y baja tensión cumple tres funciones de ingeniería imprescindibles: '
         '<ul>'
         '<li><strong>1. Prevención de Arcos Eléctricos en Celdas Compactas:</strong> En celdas modernas el espacio entre fases es sumamente estrecho. '
         'Las cabezas de los pernos y las esquinas del cobre concentran el campo eléctrico provocando efecto corona. '
         'La bota aislante elimina los efectos de punta y previene descargas disruptivas entre fases durante sobretensiones por maniobra o rayos.</li>'
         '<li><strong>2. Erradicación del Encintado Manual:</strong> Aislar una unión con cintas autosoldables requería más de 30 minutos por punto, '
         'dejando un espesor irregular. La bota preformada se coloca y se fija con remaches plásticos en menos de un minuto con espesor uniforme garantizado.</li>'
         '<li><strong>3. Reutilización Inmediata para Termografía:</strong> El mantenimiento exige inspeccionar con cámara infrarroja el apriete de los pernos. '
         'Las uniones encintadas deben ser cortadas y destruidas. La bota se abre en segundos y se vuelve a cerrar sin ningún desperdicio de material.</li>'
         '</ul>'),
        ('¿Cómo evitan las botas aislantes los cortocircuitos provocados por fauna en subestaciones?',
         'Las subestaciones y centros de transformación sufren frecuentes intrusiones de pequeños animales '
         '(roedores, reptiles o aves que buscan calor en los gabinetes). '
         'Cuando un animal hace puente entre dos barras desnudas adyacentes, provoca un cortocircuito violento con explosión de arco '
         'que destruye la celda y deja sin servicio a ciudades enteras. '
         'Las botas aislantes YOMIN crean una barrera táctil continua e impenetrable sobre todos los metales vivos. '
         'Aunque un roedor camine directamente sobre la bota, el aislamiento impide el contacto eléctrico, salvando la continuidad del suministro.'),
        ('¿Cuál es la diferencia entre las botas de PVC y las de Caucho de Silicona?',
         'La selección depende de las exigencias operativas: '
         '<ul>'
         '<li><strong>Elastómero de PVC por Inmersión:</strong> Económico, flexible y mecánicamente robusto. Ideal para celdas interiores '
         'hasta 24kV y temperaturas continuas de hasta 105&deg;C.</li>'
         '<li><strong>Caucho de Silicona:</strong> Hidrofóbico (repele el agua y la niebla salina), incombustible y resistente '
         'desde -50&deg;C hasta +150&deg;C. Indispensable para niveles de hasta 36kV y bornes exteriores expuestos a alta radiación solar y condensación.</li>'
         '</ul>')
    ],
    cta='¿Fabrica celdas de media tensión, centros de transformación compactos o cuadros de distribución eléctrica que requieren botas aislantes de barras certificadas hasta 36kV? YOMIN fabrica accesorios de aislamiento de barras colectoras de alta confiabilidad.',
    body='''
<h2>La Solución Preformada para la Protección de Barras Colectoras en Media Tensión</h2>
<p>En el interior de <strong>celdas y gabinetes de distribución eléctrica de media tensión (1kV a 36kV)</strong>, la potencia se transmite mediante pletinas rectangulares de cobre electrolítico. En los puntos de empalme, las barras se unen mediante tornillería de acero de alta resistencia.</p>
<p>Estas uniones apernadas representan los puntos más vulnerables del tablero. Las cabezas hexagonales y tuercas concentran el gradiente de campo electrostático, reduciendo la rigidez dieléctrica del aire circundante.</p>
<p>En celdas compactas, cualquier exceso de humedad, polvo o ingreso de fauna puede desatar un arco destructivo entre fases contiguas.</p>
<p>La <strong>Bota Aislante para Barras Colectoras (Serie YM-BS)</strong> proporciona la solución de ingeniería estandarizada: cubiertas aislantes preformadas que se montan en segundos en frío, proporcionando una rigidez dieléctrica certificada en fábrica de hasta 36kV sin necesidad de engorrosas cintas adhesivas.</p>

<h2>Elementos de Diseño y Calidad Constructiva</h2>
<ol>
  <li><strong>Espesor Dieléctrico Calibrado (&ge; 25 kV/mm):</strong> Garantiza un aislamiento uniforme y sin poros sobre todas las aristas vivas y pernos.</li>
  <li><strong>Formas Anatómicas Normalizadas:</strong> Modelos dedicados para uniones en T, codos en ángulo recto y pasamuros de transformador.</li>
  <li><strong>Cierre Rápido con Remaches Desmontables:</strong> Permite retirar y reinstalar la bota en 10 segundos para inspecciones con cámara termográfica.</li>
  <li><strong>Polímero Autoextinguible UL 94 V-0:</strong> No propaga la llama en caso de sobrecargas térmicas accidentales.</li>
</ol>
'''
)

BIB_AR = dict(
    lang='ar',
    dir='rtl',
    slug='switchgear-busbar-joints-what-is-a-busbar-insulation-boot-ar',
    title='نقاط اتصال قضبان التوزيع والمحولات: ما هو الغطاء العازل لقضبان التوزيع (Busbar Boot)؟',
    breadcrumb='حماية وعزل قضبان التوزيع',
    read='10 دقائق قراءة',
    alt='أغطية عازلة مسبقة التشكيل لقضبان التوزيع (موديل YM-BS) مركبة على وصلات تفرع T وأكواع بزاوية 90 درجة في خلايا الجهد المتوسط',
    desc=('خلايا الجهد المتوسط (11kV إلى 36kV)، وعوازل المحولات، ومحطات التحويل المدمجة: ما هو الغطاء العازل لقضبان التوزيع (Busbar Boot)؟ '
          'بوليمر عازل مرن مسبق الصب بمتانة عازلة تفوق 25kV/mm، وتثبيت سريع بمسامير كبس قابلة لإعادة الفتح دون شريط لاصق لمنع الشرر والتماس الكهربائي.'),
    model='سلسلة YM-BS: الأغطية العازلة مسبقة التشكيل لوصلات قضبان التوزيع للجهد المنخفض والمتوسط (وصلات T، أكواع 90 درجة، عوازل المحولات حتى 36kV)',
    category='حماية وعزل قضبان التوزيع / أغطية قضبان التوزيع (Busbar Boots)',
    kw='غطاء عازل باسبار &middot; busbar boot &middot; عازل قضبان التوزيع &middot; غطاء عازل لوحات كهرباء &middot; عزل باسبار 24kv &middot; جلبة عازلة لمحولات الكهرباء',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة', 'مصمم لتطبيقات شبكات الجهد المنخفض والمتوسط من 1kV و 11kV و 24kV وحتى 36kV في خلايا التوزيع المعزولة بالهواء'),
        ('قوة صمود العزل وانهيار الجهد', 'قوة صمود عزل عالي &ge; 25 kV/mm؛ وجهد صمود عازل بتردد الشبكة يصل حتى 95kV لمدة دقيقة كاملة (في الهواء الجاف)'),
        ('المادة المصنعة والمرونة الميكانيكية', 'إلاستومر بوليمر PVC نقي مصبوب بالغمر، أو مطاط السيليكون المرن الكاره للماء، أو بولي أوليفين معالج إشعاعياً'),
        ('مقاومة اللهب ونطاق درجات الحرارة', 'تركيبة مثبطة للهب معتمدة طبقاً لـ UL 94 V-0؛ نطاق حرارة تشغيل مستمر: من -40&deg;C إلى +105&deg;C (حتى 150&deg;C للسيليكون)'),
        ('الأشكال الهندسية المعيارية لوصلات التوزيع', 'أشكال مسبقة الصب: وصلات مستقيمة مستمرة، أكواع بزاوية 90 درجة، وصلات تفرع على شكل T، وأغطية عوازل المحولات'),
        ('آلية الإغلاق وإعادة الاستخدام السريع', 'إغلاق عبر مسامير كبس بلاستيكية (Snap-rivets) من النايلون المقاوم للهب قابلة للفك وإعادة التركيب دون أي تلف'),
        ('مقاومة العوامل البيئية والكيميائية', 'مقاومة استثنائية للتتبع الكهربائي، والأوزون، وغاز سادس فلوريد الكبريت (SF6)، والرطوبة، والأشعة فوق البنفسجية'),
        ('مطابقة المواصفات القياسية الدولية', 'مصنع ومختبر وفقاً للمواصفات الدولية IEC 60060-1 و IEC 62271-200 (خلايا الجهد المتوسط) و IEEE C37 و RoHS')
    ],
    faqs=[
        ('ما هو الغطاء العازل لقضبان التوزيع (Busbar Boot) ولماذا يُركب على الوصلات المربوطة في خلايا الجهد المتوسط؟',
         'الغطاء العازل لقضبان التوزيع—والمعروف في محطات الكهرباء باسم Busbar Boot أو الكاب العازل لوصلات الباسبار—هو '
         'غلاف بوليمري مرن مسبق التشكيل يتمتع بمتانة عزل كهربائي هائلة، صُمم خصيصاً ليغلف بالكامل نقاط الربط الميكانيكية '
         'بين قضبان النحاس أو الألومنيوم (مثل تفرعات T، وأكواع الزوايا 90 درجة، ووصلات الربط بمسامير، ونقاط الدخول للمحولات) داخل لوحات التوزيع. '
         'يؤدي هذا الغطاء ثلاث وظائف هندسية حاسمة: '
         '<ul>'
         '<li><strong>1. منع الانهيار وشرارات القوس الكهربائي (Flashover):</strong> في خلايا التوزيع الحديثة المدمجة، تكون المسافات الهوائية بين الأطوار ضيقة جداً. '
         'وتتسبب رؤوس المسامير وحواف النحاس الحادة في تركيز المجال الكهربائي مما يخفض عزل الهواء المحيط. '
         'يقوم الغطاء العازل بإلغاء تأثيرات الحواف الحادة ويمنع حدوث وميض كهربائي كارثي بين الأطوار عند حدوث صواعق أو طفرات تشغيلية.</li>'
         '<li><strong>2. الاستغناء التام عن اللف اليدوي بالشريط اللاصق:</strong> في السابق، كان عزل الوصلة الواحدة يتطلب 30 إلى 45 دقيقة من اللف اليدوي المجهد '
         'للأشرطة المطاطية، مما يعطي سماكة غير متجانسة وعرضة للفك. أما الغطاء مسبق الصب فينزلق فوق الوصلة ويُقفل بمسامير كبس في أقل من دقيقة بسماكة عزل مضمونة.</li>'
         '<li><strong>3. إعادة الفتح السريع للفحص الحراري بالأشعة تحت الحمراء:</strong> تتطلب لوائح الصيانة الدورية فحص إحكام ربط المسامير ودرجة حرارتها بكاميرات حرارية. '
         'إن الأشرطة اللاصقة القديمة تتطلب القص والإتلاف، بينما يمكن فك مسامير كبس الغطاء العازل في ثوانٍ وإعادة إغلاقه دون أي هدر.</li>'
         '</ul>'),
        ('كيف تمنع الأغطية العازلة انقطاع الكهرباء الناتج عن تسلل الحيوانات في محطات التوزيع؟',
         'تتعرض محطات التحويل الأرضية والكبائن الخارجية لتسلل الحيوانات الصغيرة والزواحف '
         '(مثل القوارض، والطيور، والسحالي التي تجتذبها حرارة المحولات). '
         'وعندما يتحرك حيوان بين قضيبين مكشوفين من قضبان التوزيع، فإنه يقصر المسافة الهوائية مسبباً قصر دائرة كهربائياً متفجراً '
         'يدمر اللوحة بالكامل ويقطع الكهرباء عن أحياء سكنية بأكملها. '
         'تشكل أغطية يمين العازلة درعاً عازلاً مصمتاً يغطي كافة المعادن المكشوفة. '
         'وحتى لو لامس حيوان الغطاء مباشرة، فإن سماكة العزل تمنع مرور التيار نهائياً، مما يحمي الشبكة ويوفر على شركات الكهرباء تكاليف استبدال باهظة.'),
        ('ما هو الفارق بين أغطية الـ PVC المصبوبة وأغطية مطاط السيليكون؟',
         'يتحدد الاختيار طبقاً لبيئة التشغيل ومستوى الجهد: '
         '<ul>'
         '<li><strong>إلاستومر PVC المصبوب بالغمر:</strong> اقتصادي، وشديد المرونة والمتانة الميكانيكية. مثالي للخلايا الداخلية '
         'حتى جهد 24kV ودرجات حرارة تشغيل تصل إلى 105&deg;C.</li>'
         '<li><strong>مطاط السيليكون:</strong> يتمتع بخاصية طرد الماء والرطوبة (Hydrophobic)، وغير قابل للاشتعال، ويتحمل درجات حرارة '
         'من -50&deg;C إلى +150&deg;C. وهو الخيار الإلزامي لجهود 36kV وعوازل المحولات الخارجية المعرضة للضباب الملحي والتكثف الشديد.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع خلايا الجهد المتوسط (Switchgear)، أو محطات التحويل المدمجة (Kiosk)، أو لوحات التوزيع التي تتطلب أغطية عازلة لقضبان التوزيع معتمدة حتى 36kV؟ تصنع يمين (YOMIN) ملحقات عزل قضبان التوزيع مسبقة الصب بأعلى معايير الجودة العالمية.',
    body='''
<h2>الدرع العازل مسبق التشكيل لخلايا ومحطات توزيع الكهرباء الحديثة</h2>
<p>في <strong>خلايا الجهد المتوسط والمنخفض (من 1kV حتى 36kV)</strong>، تُنقل الطاقة الكهربائية عبر قضبان نحاسية مستطيلة ضخمة. وعند نقاط التفرع والتغذية، تُربط هذه القضبان بمسامير وصواميل فولاذية عالية الإجهاد.</p>
<p>تعتبر هذه الوصلات المربوطة بمثابة أضعف النقاط في منظومة التوزيع الكهربائي؛ إذ تتسبب الحواف السداسية للمسامير وزوايا القضبان الحادة في تركيز خطوط المجال الكهربائي الساكن، مما يضعف عازلية الهواء المحيط.</p>
<p>وفي اللوحات المدمجة الحديثة ذات المسافات المحصورة، تكفي أدنى نسبة رطوبة أو غبار أو تسلل قارض لإشعال شرارة تفريغ كهربائي هائلة (Flashover) تدمر القواطع بالكامل.</p>
<p>توفر <strong>الأغطية العازلة لقضبان التوزيع (سلسلة YM-BS)</strong> الحل الهندسي القياسي الحاسم: أغطية مرنة مسبقة الصب ذات عزل فائق تنزلق فوق نقاط الربط بمسامير في ثوانٍ معدودة، مقدمةً عازلية معتمدة مخبرياً حتى 36kV دون الحاجة إلى اللف اليدوي العشوائي بالأشرطة.</p>

<h2>المكونات الهندسية وميزات الأمان المتقدمة</h2>
<ol>
  <li><strong>سماكة جدار عازل متجانسة مخبرياً (&ge; 25 kV/mm):</strong> توفر عزلًا مصمتًا خاليًا من الفقاعات الهوائية يغلف كافة الرؤوس الحادة والمسامير.</li>
  <li><strong>أشكال هندسية معيارية مدروسة:</strong> قوالب جاهزة مخصصة لوصلات التفرع على شكل T، والأكواع بزاوية 90 درجة، وعوازل المحولات.</li>
  <li><strong>نظام قفل وتثبيت بمسامير كبس قابلة لإعادة الاستخدام:</strong> يتيح فك الغطاء في 10 ثوانٍ لإجراء الكشف الحراري بالأشعة تحت الحمراء ثم إعادة إغلاقه بإحكام.</li>
  <li><strong>بوليمر مطفئ لذاته معتمد UL 94 V-0:</strong> لا يساعد على الاشتعال ولا يطلق قطرات حارقة عند حدوث أي سخونة طارئة.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1008 = [
    ICT_EN, ICT_FR, ICT_ES, ICT_AR,
    BIB_EN, BIB_FR, BIB_ES, BIB_AR
]
