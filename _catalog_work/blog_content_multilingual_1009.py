# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-09:
1. CT-Operated Energy Meters for Commercial & Industrial Power (EN, FR, ES, AR)
2. Composite Pin Insulators for Medium-Voltage Overhead Distribution (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. CT-OPERATED ENERGY METER (EN, FR, ES, AR)
# ==============================================================================

CTM_EN = dict(
    lang='en',
    dir='ltr',
    slug='commercial-metering-what-is-a-ct-operated-energy-meter',
    title='Commercial & Industrial Metering: What Is a CT-Operated Energy Meter?',
    breadcrumb='Energy Meters &amp; Smart Grid',
    read='10 min read',
    alt='Three-phase CT-Operated Smart Multi-Function Energy Meter (Model DTSD series) with LCD display wired to window current transformers on copper busbars in an industrial switchgear panel',
    desc=('Commercial power distribution, industrial tenant sub-metering, and utility substations: What is a CT-operated energy meter? '
          'How external current transformers, secondary 5A/1A inputs, Class 0.5S high precision, DLMS/COSEM protocols, and CT multiplier ratios measure heavy loads above 100A.'),
    model='Model DTSD / DSSD Series 3-Phase CT-Connected Smart Multi-Function Energy Meters (3x1.5(6)A / 3x5(6)A, Class 0.5S / Class 0.2S, DLMS/COSEM, Modbus RS485)',
    category='Energy Meters & Smart Grid / CT-Operated Energy Meters',
    kw='what is a ct operated energy meter &middot; ct operated energy meter &middot; three phase ct operated energy meter &middot; transformer operated meter &middot; ct connected smart meter &middot; dtsd energy meter',
    specs=[
        ('Rated Input Current & Measurement Range', 'Rated secondary input current: 3x1.5(6)A or 3x5(6)A via external current transformers; starting current &le; 0.001 In (1.5mA)'),
        ('Rated Reference Voltage & Connection Mode', 'Standard 3-Phase 4-Wire: 3x220/380V, 3x230/400V, 3x240/415V AC; 3-Phase 3-Wire: 3x100V or 3x380V AC (50/60 Hz)'),
        ('Measurement Accuracy Class Ratings', 'Active Energy: Class 0.5S or Class 0.2S (IEC 62053-22 high-precision standard); Reactive Energy: Class 2.0 (IEC 62053-23)'),
        ('Energy Measurement & Quadrant Capabilities', 'Bi-directional active energy (import/export), 4-quadrant reactive energy (kvarh), apparent energy, instantaneous V, I, kW, kvar, kVA, PF, Hz'),
        ('Programmable CT & PT Multiplication Ratios', 'Freely programmable primary CT ratios (e.g., 100/5A up to 5000/5A) and PT ratios; auto-calculates primary utility consumption on LCD'),
        ('Time-of-Use (TOU) & Multi-Tariff Billing', 'Up to 8 tariff rates, 14 daily time intervals, 2 seasonal tariff tables, 12 monthly billing history records, and 15-minute sliding maximum demand'),
        ('Digital Communication & Protocol Support', 'Dual optical port (IEC 62056-21) and RS485 communication interfaces supporting open DLMS/COSEM and Modbus RTU industrial protocols'),
        ('Anti-Tampering & Security Protection', 'Full anti-tampering architecture: terminal cover opening detection, reverse current logging, phase failure detection, magnetic interference immunity')
    ],
    faqs=[
        ('What is a CT-Operated Energy Meter and why can direct-connected meters NOT be used for loads above 100A?',
         'A CT-Operated Energy Meter—often designated as a transformer-operated meter, CT-connected meter, or indirect meter—is '
         'a specialized three-phase electricity revenue meter engineered to measure electrical energy via external <strong>Current Transformers (CTs)</strong> '
         'rather than passing the full circuit load current directly through its internal terminal block. '
         'Direct-connected meters (whole-current meters) are physically limited to maximum continuous loads of 80A to 100A for three fundamental engineering reasons: '
         '<ul>'
         '<li><strong>1. Physical Terminal Constraints &amp; Cable Bending:</strong> Industrial loads drawing 200A, 400A, 800A, or 2000A use thick power cables '
         '(e.g., 185 mm&sup2;, 300 mm&sup2;, or 500 mm&sup2;) or rigid copper busbars. It is mechanically impossible to terminate such heavy conductors directly into '
         'the compact terminals of a meter. A CT-operated meter measures a scaled-down 5A or 1A secondary signal, using standard 2.5 mm&sup2; flexible control wiring.</li>'
         '<li><strong>2. Terminal Heating &amp; Thermal Burnout:</strong> Passing hundreds of continuous amperes through standard internal current shunt coils generates '
         'immense heat dissipation ($I^2R$ losses). Over time, contact resistance causes thermal runaway and catastrophic terminal fires. '
         'In a CT-operated system, primary current remains entirely on the heavy main copper busbars; only harmless micro-watts enter the meter itself.</li>'
         '<li><strong>3. Revenue Meter Accuracy Standards (Class 0.5S vs. Class 1.0):</strong> Commercial billing and industrial tariff structures mandate high-precision metering. '
         'Whole-current meters typically achieve Class 1.0. CT-operated smart meters provide certified Class 0.5S or Class 0.2S laboratory-grade precision, '
         'guaranteeing accurate billing across wide current swings from light load (1% rated current) to full industrial production.</li>'
         '</ul>'),
        ('How does the CT Multiplier Ratio work when reading and calculating consumption on a CT meter?',
         'A CT-operated meter measures the secondary current (0 to 5A) produced by the external current transformers installed on the primary power bus. '
         'To determine the true electrical energy consumed by the facility: '
         '<ul>'
         '<li><strong>CT Ratio Concept:</strong> If a factory has 400/5A current transformers, the primary current (400A) is scaled down by a factor of 80 (400 &divide; 5 = 80). '
         'Every 1 Ampere flowing through the meter represents 80 Amperes flowing in the main plant busbars.</li>'
         '<li><strong>Programmable Display (Primary Billing):</strong> YOMIN DTSD meters feature fully programmable internal registers. '
         'When the commissioning engineer enters the CT ratio (e.g., 400/5) and PT ratio into the meter via software or optical probe, '
         'the meter automatically multiplies the internal register by 80 and displays the true total primary consumption (e.g., in MWh or kWh) directly on the LCD.</li>'
         '<li><strong>Unprogrammed Display (Secondary Multiplier):</strong> In legacy utility installations where the meter is set to display secondary energy (1:1), '
         'the billing utility multiplies the difference between monthly register readings by the external multiplier factor (MF = 80) on the final invoice.</li>'
         '</ul>'),
        ('Why is a Test Terminal Block (TTB) mandatory when installing a CT-operated energy meter?',
         'An external current transformer operates as a constant current source. If a CT secondary circuit is opened while the primary conductor is carrying load current, '
         'the demagnetizing secondary ampere-turns vanish, causing the iron core to saturate violently and generating <strong>destructive, lethal peak voltages '
         'exceeding several thousand volts</strong> that vaporize insulation, destroy the meter, and cause fatal flashovers. '
         'A dedicated <strong>Test Terminal Block (TTB)</strong> is installed directly below the meter. '
         'The TTB incorporates heavy-duty shorting links and isolation screws that allow technicians to safely short-circuit the CT secondaries and disconnect the voltage taps '
         'before removing, testing, or replacing the energy meter without interrupting the customer\'s electrical power supply.'),
    ],
    cta='Designing industrial power distribution panels, commercial tenant billing networks, or utility smart metering substations requiring high-accuracy Class 0.5S CT-operated energy meters? YOMIN manufactures precision DTSD/DSSD multi-function smart meters.',
    body='''
<h2>The Critical Measurement Engine for Commercial &amp; Industrial Energy</h2>
<p>In modern commercial high-rises, manufacturing plants, shopping centers, and municipal distribution substations, electrical power distribution operates at continuous current levels far beyond the reach of conventional residential electricity meters.</p>
<p>While residential homes consume 20A to 60A and use direct-connected meters, industrial facilities routinely draw <strong>200A, 400A, 800A, 1600A, up to 5000A</strong> across three-phase distribution busbars. Passing these massive currents directly into an electricity meter is physically impossible and thermally hazardous.</p>
<p>The <strong>CT-Operated Energy Meter (Model DTSD / DSSD Series)</strong> is the standardized utility instrument: an advanced, high-precision electronic revenue meter designed to measure electrical consumption indirectly through external instrument current transformers (CTs) with standardized <strong>5A or 1A secondary inputs</strong>.</p>

<h2>Engineering Anatomy: Inside a Class 0.5S CT-Operated Smart Energy Meter</h2>
<ol>
  <li><strong>Precision Current Measurement Inputs (3x1.5/6A or 3x5/6A):</strong> Internal high-permeability nanometre alloy isolation transformers step down the 5A/1A secondary current to millivolt signals with negligible phase angle error across temperatures from -25&deg;C to +65&deg;C.</li>
  <li><strong>High-Resolution Digital Signal Processor (DSP):</strong> A 32-bit metering core samples voltage and current waveforms simultaneously at thousands of samples per second, computing true RMS voltage, active power, reactive power, power factor, and individual harmonics up to the 31st order.</li>
  <li><strong>Programmable CT and PT Transformation Ratios:</strong> Built-in non-volatile EEPROM memory stores user-configured primary CT ratios (e.g., 200/5, 400/5, 1000/5, 2500/5) and PT ratios, enabling direct primary energy reading on the illuminated LCD screen.</li>
  <li><strong>Time-of-Use (TOU) Multi-Tariff Engine:</strong> Incorporates a temperature-compensated real-time clock (RTC accurate to &le; 0.5 s/day) managing up to 8 separate tariff rates, peak/off-peak billing intervals, and 15-minute sliding maximum demand registers.</li>
  <li><strong>Dual Communication Architecture:</strong> Equipped with an optical communication port on the front cover for hand-held field interrogations, plus an isolated RS485 communication port supporting open industrial protocols including <strong>DLMS/COSEM and Modbus RTU</strong> for automated meter reading (AMR/AMI) and SCADA integration.</li>
</ol>

<h2>Comparison: Direct-Connected (Whole-Current) Meter vs. CT-Operated Energy Meter</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Direct-Connected (Whole-Current) Meter</th>
      <th>YOMIN CT-Operated Smart Energy Meter (DTSD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Current Carrying Capacity</strong></td>
      <td>Direct connection: Max 80A or 100A continuous load.</td>
      <td><strong>Unlimited Capacity: Measures any load (100A to 5000A+) via external current transformers.</strong></td>
    </tr>
    <tr>
      <td><strong>Meter Terminal Wiring Size</strong></td>
      <td>Requires thick main cables (up to 35 mm&sup2;) into meter block.</td>
      <td><strong>Standard 2.5 mm&sup2; or 4 mm&sup2; flexible control wiring from CT secondary terminals.</strong></td>
    </tr>
    <tr>
      <td><strong>Accuracy Class (IEC 62053-22)</strong></td>
      <td>Standard Class 1.0 or Class 2.0.</td>
      <td><strong>High-Precision Class 0.5S or Class 0.2S laboratory revenue-grade accuracy.</strong></td>
    </tr>
    <tr>
      <td><strong>Terminal Thermal Dissipation &amp; Safety</strong></td>
      <td>High heat dissipation ($I^2R$); risk of terminal meltdown.</td>
      <td><strong>Negligible internal heat (&le; 0.2W burden); main current stays safely on plant busbars.</strong></td>
    </tr>
    <tr>
      <td><strong>Testing &amp; In-Service Replacement</strong></td>
      <td>Requires de-energizing the entire facility to swap meter.</td>
      <td><strong>Test Terminal Block (TTB) allows hot-swap meter testing without cutting facility power.</strong></td>
    </tr>
    <tr>
      <td><strong>Ideal Application Sector</strong></td>
      <td>Residential homes, small retail shops, light commercial.</td>
      <td><strong>Factories, commercial towers, shopping malls, data centers, and utility substations.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

CTM_FR = dict(
    lang='fr',
    dir='ltr',
    slug='commercial-metering-what-is-a-ct-operated-energy-meter-fr',
    title="Comptage Industriel & Tertiaire : Qu'est-ce qu'un Compteur d'Énergie sur Transformateurs de Courant (TC) ?",
    breadcrumb='Comptage Électrique &amp; Smart Grid',
    read='10 min de lecture',
    alt='Compteur d\'énergie communicant triphasé sur transformateurs de courant (Modèle DTSD) raccordé à des TC tores dans une armoire de distribution industrielle',
    desc=('Distribution électrique industrielle, sous-comptage tertiaire et postes de transformation : Qu\'est-ce qu\'un compteur d\'énergie raccordé sur TC ? '
          'Entrées secondaires 5A/1A, haute précision Classe 0.5S, communication DLMS/COSEM, coefficients de multiplication et mesure des courants supérieurs à 100A.'),
    model='Série DTSD / DSSD : Compteurs d\'Énergie Électronique Triphasés sur TC (3x1,5(6)A / 3x5(6)A, Classe 0.5S / 0.2S, DLMS/COSEM, Modbus RS485)',
    category='Comptage Électrique & Smart Grid / Compteurs d\'Énergie sur TC',
    kw='compteur sur tc &middot; compteur d energie sur transformateur de courant &middot; compteur triphase tc &middot; compteur dtsd &middot; comptage tarifaire tertiaire',
    specs=[
        ('Courant Assigné d\'Entrée et Calibre', 'Entrée secondaire sur TC externe : 3x1,5(6)A ou 3x5(6)A ; courant de démarrage &le; 0,001 In (1,5 mA)'),
        ('Tension Assignée de Référence et Réseau', 'Réseau Triphasé 4 Fils : 3x220/380V, 3x230/400V, 3x240/415V AC ; Triphasé 3 Fils : 3x100V ou 3x380V (50/60 Hz)'),
        ('Classe de Précision de Mesure (CEI)', 'Énergie Active : Classe 0.5S ou Classe 0.2S (norme haute précision CEI 62053-22) ; Énergie Réactive : Classe 2.0'),
        ('Mesure d\'Énergie et 4 Quadrants', 'Énergie active bidirectionnelle (import/export), réactive 4 quadrants (kvarh), puissances instantanées P, Q, S, cos &phi;, Hz'),
        ('Programmation des Rapports TC et TP', 'Rapports primaires configurables (ex : 100/5A jusqu\'à 5000/5A) ; calcul et affichage automatique de l\'énergie primaire réelle'),
        ('Gestion Multitarif et Dépassement de Puissance', 'Jusqu\'à 8 index tarifaires, 14 tranches horaires quotidiennes, 12 historiques mensuels et calcul de puissance maximale atteinte'),
        ('Interfaces et Protocoles de Communication', 'Port optique frontal (CEI 62056-21) et liaison série RS485 intégrant les protocoles ouverts DLMS/COSEM et Modbus RTU'),
        ('Dispositifs Anti-Fraude et Sécurité', 'Enregistrement des ouvertures de capot, inversion de sens de courant, coupure de phase et insensibilité aux champs magnétiques')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Compteur d\'Énergie sur TC et pourquoi le raccordement direct est-il impossible au-delà de 100A ?',
         'Un Compteur d\'Énergie sur TC (Transformateur de Courant)—aussi désigné sous le nom de compteur semi-direct ou compteur indirect—est '
         'un compteur d\'électricité triphasé haute précision conçu pour mesurer la consommation par l\'intermédiaire de transformateurs de courant externes. '
         'Le comptage en raccordement direct est physiquement impossible au-delà de 100A pour trois raisons techniques fondamentales : '
         '<ul>'
         '<li><strong>1. Section des Conducteurs et Câblage :</strong> Une usine consommant 200A, 400A ou 1000A est alimentée par d\'épaisses barres de cuivre '
         'ou des câbles de 150 à 300 mm&sup2;. Il est impossible d\'insérer ces câbles dans les bornes compactes d\'un compteur. '
         'Le compteur sur TC ne reçoit qu\'un courant secondaire réduit de 5A ou 1A véhiculé par des fils souples standard de 2,5 mm&sup2;.</li>'
         '<li><strong>2. Échauffement Thermique et Sécurité Incendie :</strong> Faire transiter des centaines d\'ampères continus à l\'intérieur du boîtier du compteur '
         'génère d\'immenses pertes par effet Joule ($I^2R$), provoquant des surchauffes destructrices. Sur TC, le courant de puissance reste sur le jeu de barres.</li>'
         '<li><strong>3. Exigence de Haute Précision Facturation (Classe 0.5S) :</strong> Les tarifs industriels exigent une très haute précision. '
         'Les compteurs directs sont de Classe 1.0, tandis que les compteurs sur TC certifiés Classe 0.5S garantissent une mesure exacte même à faible charge.</li>'
         '</ul>'),
        ('Comment fonctionne le coefficient de multiplication (Rapport TC) lors de la facturation ?',
         'Le compteur mesure le courant secondaire de 0 à 5A produit par les TC de mesure installés sur les barres principales : '
         '<ul>'
         '<li><strong>Principe du Rapport TC :</strong> Si l\'armoire est équipée de TC de rapport 400/5A, le courant principal est réduit d\'un facteur 80 (400 &divide; 5 = 80). '
         'Chaque ampère mesuré par le compteur correspond à 80 ampères réels dans l\'installation.</li>'
         '<li><strong>Affichage Primaire Automatique :</strong> Sur les compteurs YOMIN DTSD, le rapport de transformation (400/5) est enregistré en mémoire. '
         'Le compteur multiplie automatiquement la mesure interne par 80 et affiche directement les kilowattheures ou mégawattheures réels sur l\'écran LCD.</li>'
         '</ul>'),
        ('Pourquoi la boîte d\'essai (Test Terminal Block - TTB) est-elle obligatoire ?',
         'Un transformateur de courant ne doit JAMAIS avoir son circuit secondaire ouvert en charge sous peine de générer des surtensions mortelles de plusieurs milliers de volts. '
         'La <strong>boîte d\'essai (TTB)</strong> installée sous le compteur permet aux techniciens de court-circuiter en toute sécurité les secondaires des TC '
         'et d\'isoler les tensions pour remplacer ou étalonner le compteur sans jamais couper l\'alimentation électrique de l\'usine.')
    ],
    cta='Vous concevez des armoires de distribution industrielle, des tableaux de comptage tarifaire tertiaire ou des postes de transformation nécessitant des compteurs sur TC de Classe 0.5S compatibles DLMS/COSEM ? YOMIN fabrique des compteurs intelligents DTSD de haute précision.',
    body='''
<h2>L\'Instrument de Mesure Indispensable pour l\'Énergie Tertiaire et Industrielle</h2>
<p>Dans les usines de production, les centres commerciaux, les tours de bureaux et les postes de transformation HTA/BT, la consommation électrique atteint des intensités continues considérables.</p>
<p>Tandis qu\'une habitation consomme quelques dizaines d\'ampères avec un compteur direct, les installations industrielles sollicitent <strong>200A, 400A, 800A jusqu\'à plus de 3000A</strong> par phase. Faire transiter de telles intensités à l\'intérieur d\'un appareil de mesure traditionnel est à la fois irréalisable et dangereux.</p>
<p>Le <strong>Compteur d\'Énergie sur Transformateurs de Courant (Série DTSD / DSSD)</strong> constitue la solution universelle des distributeurs d\'électricité : un compteur électronique haute performance mesurant le courant indirectement via des transformateurs de courant (TC) avec des <strong>entrées secondaires standardisées de 5A ou 1A</strong>.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série DTSD</h2>
<ol>
  <li><strong>Précision Laboratoire Certifiée Classe 0.5S :</strong> Conforme à la norme CEI 62053-22 pour garantir une facturation loyale même sous régimes de charge très faibles.</li>
  <li><strong>Mesure Complète 4 Quadrants :</strong> Enregistre l\'énergie active importée et exportée ainsi que l\'énergie réactive inductive et capacitive pour le contrôle du facteur de puissance.</li>
  <li><strong>Gestion Multitarif et Puissance Maximale :</strong> Horloge temps réel compensée en température gérant jusqu\'à 8 tarifs pour optimiser les coûts aux heures de pointe.</li>
  <li><strong>Communication Ouverte DLMS/COSEM et Modbus RS485 :</strong> Intégration immédiate dans les logiciels de télérelève (AMR/AMI) et systèmes de supervision GTB/GTC.</li>
</ol>
'''
)

CTM_ES = dict(
    lang='es',
    dir='ltr',
    slug='commercial-metering-what-is-a-ct-operated-energy-meter-es',
    title='Medición Comercial e Industrial: ¿Qué es un Medidor de Energía Operado por TC?',
    breadcrumb='Medidores de Energía y Redes Inteligentes',
    read='10 min de lectura',
    alt='Medidor de energía electrónico trifásico operado por transformadores de corriente (Modelo DTSD) instalado en tablero de distribución industrial',
    desc=('Distribución de energía comercial, submedición en centros comerciales y subestaciones industriales: ¿Qué es un medidor operado por TC? '
          'Entradas secundarias de 5A/1A, precisión Clase 0.5S, protocolos DLMS/COSEM, factor multiplicador y medición de corrientes superiores a 100A.'),
    model='Serie DTSD / DSSD: Medidores Electrónicos Multifunción Trifásicos Conectados por TC (3x1,5(6)A / 3x5(6)A, Clase 0.5S / 0.2S, DLMS/COSEM, Modbus RS485)',
    category='Medidores de Energía y Redes Inteligentes / Medidores Operados por TC',
    kw='medidor operado por tc &middot; medidor con transformadores de corriente &middot; medidor trifasico indirecto &middot; medidor dtsd &middot; medicion comercial clase 0.5s',
    specs=[
        ('Corriente Asignada de Entrada y Rango', 'Entrada secundaria por TC externo: 3x1,5(6)A o 3x5(6)A ; corriente de arranque mínima &le; 0,001 In (1,5 mA)'),
        ('Tensión Nominal de Referencia y Red', 'Trifásico 4 Hilos: 3x220/380V, 3x230/400V, 3x240/415V AC ; Trifásico 3 Hilos: 3x100V o 3x380V (50/60 Hz)'),
        ('Clase de Precisión de Medición (IEC)', 'Energía Activa: Clase 0.5S o Clase 0.2S (norma de alta precisión IEC 62053-22) ; Energía Reactiva: Clase 2.0'),
        ('Capacidad de Medición en 4 Cuadrantes', 'Energía activa bidireccional (importación/exportación), reactiva 4 cuadrantes (kvarh), potencia instantánea, factor de potencia y armónicos'),
        ('Relaciones de Transformación TC/TP Configurables', 'Relación de TC primario programable (ej. 100/5A hasta 5000/5A) ; cálculo y visualización directa del consumo primario real'),
        ('Tarificación Horaria (TOU) y Demanda Máxima', 'Hasta 8 tarifas horarias, 14 intervalos diarios, 12 registros de facturación mensual y registro de demanda máxima por ventana deslizante'),
        ('Interfaces y Protocolos de Comunicación', 'Puerto óptico frontal (IEC 62056-21) y puerto serial RS485 con protocolos abiertos DLMS/COSEM y Modbus RTU para telemetría'),
        ('Seguridad Antifraude y Registro de Eventos', 'Detección de apertura de tapa de bornes, registro de inversión de corriente, caída de fase e inmunidad magnética total')
    ],
    faqs=[
        ('¿Qué es un Medidor Operado por TC y por qué no se puede utilizar medición directa para cargas superiores a 100A?',
         'Un Medidor Operado por TC (Transformador de Corriente)—también llamado medidor de medición indirecta o semidirecta—es '
         'un equipo de medición tarifaria trifásico de alta precisión diseñado para medir la electricidad a través de transformadores de corriente externos. '
         'La medición directa no es viable por encima de 100A por tres razones técnicas insoslayables: '
         '<ul>'
         '<li><strong>1. Limitación Física del Cableado:</strong> Las corrientes industriales de 200A, 400A o 1000A requieren conductores de gran sección '
         '(150 mm&sup2; a 300 mm&sup2;) o pletinas de cobre rígidas que no pueden entrar físicamente en la bornera de un medidor. '
         'El medidor sobre TC solo recibe corrientes secundarias estandarizadas de 5A o 1A con cables de control delgados de 2,5 mm&sup2;.</li>'
         '<li><strong>2. Disipación Térmica y Seguridad:</strong> El paso de cientos de amperios continuos dentro del medidor generaría un calor extremo ($I^2R$) '
         'que derretiría los terminales. En un medidor sobre TC, la corriente de potencia permanece en las barras colectoras del tablero.</li>'
         '<li><strong>3. Exigencia de Alta Precisión (Clase 0.5S):</strong> Los medidores directos ofrecen precisión Clase 1.0. '
         'Las tarifas industriales exigen medidores Clase 0.5S para registrar fielmente consumos multimillonarios incluso con cargas ligeras.</li>'
         '</ul>'),
        ('¿Cómo se aplica el Factor de Multiplicación del TC en la facturación?',
         'El medidor registra la corriente secundaria proporcional que entregan los transformadores de corriente: '
         '<ul>'
         '<li><strong>Concepto de Relación de TC:</strong> Si se utilizan transformadores de 400/5A, la corriente real es 80 veces mayor (400 &divide; 5 = 80). '
         'Cada unidad registrada en el secundario equivale a 80 unidades en el primario.</li>'
         '<li><strong>Lectura Directa Programable:</strong> Los medidores YOMIN DTSD permiten programar la relación 400/5 directamente. '
         'El medidor realiza la multiplicación de forma automática y muestra directamente los kWh o MWh reales consumidos en la pantalla LCD.</li>'
         '</ul>'),
        ('¿Por qué es obligatoria una Regleta de Pruebas (Test Terminal Block - TTB)?',
         'Un transformador de corriente nunca debe quedar con el secundario abierto mientras haya carga en el primario, ya que se generarían sobretensiones destructivas de miles de voltios. '
         'La <strong>Regleta de Pruebas (TTB)</strong> permite cortocircuitar los secundarios de los TC de forma segura e interrumpir las señales de tensión '
         'para sustituir o contrastar el medidor sin interrumpir el suministro eléctrico de la fábrica.')
    ],
    cta='¿Diseña tableros de distribución industrial, centros comerciales o subestaciones eléctricas que requieren medidores operados por TC de Clase 0.5S con comunicación DLMS/COSEM? YOMIN fabrica medidores inteligentes DTSD de máxima confiabilidad.',
    body='''
<h2>El Instrumento Clave para la Medición Eléctrica Comercial e Industrial</h2>
<p>En complejos industriales, rascacielos comerciales, centros de datos y subestaciones eléctricas de distribución, el suministro de energía opera bajo niveles de corriente que superan ampliamente las capacidades de los medidores convencionales.</p>
<p>Mientras que una vivienda residencial opera entre 20A y 60A con medidores directos, las empresas industriales consumen de forma continua <strong>200A, 400A, 800A o más de 2000A</strong> por fase. Conducir estas corrientes al interior de un medidor resultaría inviable e inflamable.</p>
<p>El <strong>Medidor de Energía Operado por Transformadores de Corriente (Serie DTSD / DSSD)</strong> ofrece la respuesta estandarizada del sector utility: un medidor inteligente de alta precisión diseñado para conectarse a transformadores de corriente externos con <strong>entradas secundarias de 5A o 1A</strong>.</p>

<h2>Ventajas y Características Constructivas de la Serie DTSD</h2>
<ol>
  <li><strong>Precisión Grado Facturación Clase 0.5S:</strong> Homologado bajo norma IEC 62053-22 para evitar pérdidas no técnicas en tarifas de alta demanda.</li>
  <li><strong>Medición Bidireccional en Cuatro Cuadrantes:</strong> Registra importación y exportación de energía activa y reactiva para el control de penalizaciones por factor de potencia.</li>
  <li><strong>Tarificación Horaria Multitarifa (TOU):</strong> Reloj en tiempo real de alta exactitud que gestiona hasta 8 tarifas y curvas de demanda máxima en ventanas de 15 minutos.</li>
  <li><strong>Comunicaciones Abiertas DLMS/COSEM y Modbus RS485:</strong> Comunicación remota fluida para plataformas de telelectura (AMI/AMR) y sistemas SCADA industriales.</li>
</ol>
'''
)

CTM_AR = dict(
    lang='ar',
    dir='rtl',
    slug='commercial-metering-what-is-a-ct-operated-energy-meter-ar',
    title='قياس الطاقة للقطاع التجاري والصناعي: ما هو عداد الكهرباء المتصل بمحولات التيار (CT-Operated Meter)؟',
    breadcrumb='عدادات الطاقة والشبكات الذكية',
    read='10 دقائق قراءة',
    alt='عداد طاقة إلكتروني ذكي ثلاثي الطور متصل بمحولات تيار (موديل DTSD) مركب في لوحة قواطع صناعية مع محولات تيار وقضبان نحاسية',
    desc=('لوحات التوزيع الصناعية، والمجمعات التجارية، ومحطات التوزيع الفرعية: ما هو عداد الطاقة المتصل بمحولات التيار (CT-Operated Meter)؟ '
          'مداخل تيار ثانوية 5A/1A، دقة فائقة فئة 0.5S، بروتوكولات DLMS/COSEM، معاملات الضرب، وقياس الأحمال العالية التي تتجاوز 100 أمبير.'),
    model='سلسلة DTSD / DSSD: عدادات الطاقة الإلكترونية الذكية ثلاثية الأطوار المتصلة بمحولات تيار (3x1.5(6)A / 3x5(6)A، دقة Class 0.5S/0.2S، DLMS/COSEM، Modbus RS485)',
    category='عدادات الطاقة والشبكات الذكية / عدادات القياس عبر محولات التيار',
    kw='عداد كهرباء بمحولات تيار &middot; ct operated energy meter &middot; عداد قياس غير مباشر &middot; عداد dtsd &middot; عداد كهرباء صناعي كلاس 0.5s &middot; عداد ذكي 3 فاز',
    specs=[
        ('تيار الدخل المقنن ومجال القياس', 'تيار الدخل الثانوي عبر محولات التيار الخارجية: 3x1.5(6)A أو 3x5(6)A؛ تيار البدء الحساس &le; 0.001 In (1.5 ملي أمبير)'),
        ('جهد التشغيل المرجعي ونوع الربط', 'ربط ثلاثي الطور 4 أسلاك: 3x220/380V، 3x230/400V، 3x240/415V AC؛ ربط 3 أسلاك: 3x100V أو 3x380V (تردد 50/60 هرتز)'),
        ('فئة الدقة المعيارية لقياس الطاقة', 'الطاقة الفعالة: فئة Class 0.5S أو Class 0.2S (المواصفة الدولية IEC 62053-22)؛ الطاقة غير الفعالة: فئة Class 2.0'),
        ('قياس الطاقة في الأرباع الأربعة', 'قياس الطاقة الفعالة ثنائي الاتجاه (استيراد/تصدير)، والطاقة غير الفعالة في 4 أرباع (kvarh)، والقدرة الآنية، ومعامل القدرة، والتوافقيات'),
        ('برمجة نسب تحويل محولات التيار والجهد', 'إمكانية برمجة نسب محولات التيار CT (مثل 100/5A حتى 5000/5A) ونسب محولات الجهد؛ لحساب وعرض الاستهلاك الابتدائي الفعلي فورياً'),
        ('التعرفة المتعددة وتسجيل أقصى طلب (MD)', 'يدعم حتى 8 فترات تعرفة، و14 شريحة زمنية يومية، و12 سجلاً شهرياً، وحساب أقصى حمل مسحوب (Maximum Demand) بنظام النافذة المنزلقة'),
        ('منافذ وبروتوكولات الاتصال الرقمي', 'منفذ بصري أمامي (IEC 62056-21) ومنفذ تسلسلي RS485 معتمدين لبروتوكولات القراءة الآلية المفتوحة DLMS/COSEM و Modbus RTU'),
        ('أنظمة الأمان ومكافحة التلاعب والاحتيال', 'حماية متكاملة: كشف فتح غطاء الأطراف، وتسجيل عكس اتجاه التيار، وكشف انقطاع أحد الأطوار، ومناعة مطلقة ضد المجالات المغناطيسية')
    ],
    faqs=[
        ('ما هو عداد الطاقة المتصل بمحولات التيار (CT-Operated Meter) ولماذا يتعذر استخدام العدادات المباشرة للأحمال فوق 100A؟',
         'عداد الطاقة المتصل بمحولات التيار—والمعروف هندسياً باسم عداد القياس غير المباشر أو العداد المتصل عبر محولات كهرومغناطيسية (CT)—هو '
         'عداد إلكتروني رقمي ثلاثي الطور مخصص لقياس استهلاك المنشآت الكبرى من خلال تحويل تيارات الأحمال الضخمة إلى تيارات ثانوية معيارية آمنة. '
         'إن استخدام العدادات ذات التوصيل المباشر (Direct-Connected) يُعد مستحيلاً للأحمال التي تفوق 100 أمبير لثلاثة أسباب قاطعة: '
         '<ul>'
         '<li><strong>1. صعوبة التوصيل الفيزيائي لكابلات القدرة:</strong> تسحب المصانع والمجمعات تيارات تصل إلى 400A أو 800A أو 2000A عبر كابلات '
         'ذات مقاطع هائلة (150 إلى 500 مم&sup2;) أو قضبان نحاسية صلبة يستحيل ثنيها وإدخالها في أطراف العداد. '
         'أما العداد المتصل عبر CT فيستقبل تياراً ثانوياً ضئيلاً (5A أو 1A) عبر أسلاك تحكم مرنة بمقطع 2.5 مم&sup2;.</li>'
         '<li><strong>2. الحرارة الشديدة وخطر الاحتراق:</strong> يؤدي مرور مئات الأمبيرات عبر ملفات العداد الداخلية إلى توليد حرارة بالغة الارتفاع ($I^2R$) '
         'تسبب صهر المرابط واحتراق العداد. في نظام القياس عبر CT، يبقى تيار الحمل الرئيسي آمناً على قضبان التوزيع النحاسية.</li>'
         '<li><strong>3. الدقة الفائقة المطلوبة للفوترة الصناعية (Class 0.5S):</strong> العدادات المباشرة تعمل بدقة عادية Class 1.0. '
         'أما عدادات القياس غير المباشر فتعمل بفئة Class 0.5S المعتمدة مخبرياً لضمان الفوترة الدقيقة للأموال الضخمة حتى عند تشغيل الأحمال الخفيفة.</li>'
         '</ul>'),
        ('كيف يعمل معامل الضرب (CT Multiplier Ratio) عند قراءة الاستهلاك واحتساب الفاتورة؟',
         'يقيس العداد تياراً متناسباً مصغراً (من 0 إلى 5 أمبير) ناتجاً عن محولات التيار الخارجية المركبة على الخطوط الرئيسية: '
         '<ul>'
         '<li><strong>مبدأ نسبة التحويل:</strong> إذا رُكبت محولات تيار بنسبة 400/5A، فإن التيار الابتدائي أكبر بمقدار 80 ضعفاً (400 &divide; 5 = 80). '
         'كل كيلوواط/ساعة يسجله العداد يمثل في الواقع 80 كيلوواط/ساعة استهلكتها المنشأة فعلياً.</li>'
         '<li><strong>العرض المبرمج المباشر:</strong> تتيح عدادات يمين DTSD إدخال نسبة محول التيار (400/5) في ذاكرة العداد برمجياً، '
         'ليقوم العداد بضرب القيمة المقروءة تلقائياً وعرض الاستهلاك الحقيقي الإجمالي مباشرة على شاشة الـ LCD دون أي حسابات يدوية.</li>'
         '</ul>'),
        ('لماذا تعتبر علبة الاختبار (Test Terminal Block - TTB) إلزامية عند تركيب عداد القياس عبر CT؟',
         'يُعد فتح دائرة محول التيار الثانوية أثناء سريان الحمل خطراً مميتاً يولد جهوداً كهربائية تفوق آلاف الفولتات تؤدي لانفجار المحول وصعق الفنيين. '
         'تُركب <strong>علبة الاختبار (TTB)</strong> مباشرة تحت العداد، وتحتوي على مسامير وجسور قصر خاصة تسمح لمهندسي شركة الكهرباء بقصر أطراف محولات التيار بأمان تام '
         'وفصل إشارات الجهد لاستبدال العداد أو اختباره دون الحاجة لفصل التيار الكهربائي عن المصنع نهائياً.')
    ],
    cta='هل تعمل على تجهيز لوحات التوزيع الصناعية، أو مجمعات المكاتب والمراكز التجارية، أو محطات التحويل الكهربائية التي تتطلب عدادات طاقة ذكية عبر محولات التيار بدقة Class 0.5S متوافقة مع DLMS/COSEM؟ تصنع يمين (YOMIN) عدادات DTSD المتطورة بأعلى معايير الدقة والاعتمادية.',
    body='''
<h2>حجر الزاوية لقياس الطاقة الكهربائية في المنشآت التجارية والصناعية الكبرى</h2>
<p>في المجمعات الصناعية، والمباني الإدارية الشاهقة، ومراكز البيانات، ومحطات التحويل التابعة لشركات توزيع الكهرباء، تتدفق طاقات كهربائية هائلة بتيارات تشغيلية تفوق قدرات عدادات القياس المباشر السكنية بمراحل.</p>
<p>فبينما تستهلك المنازل تيارات بين 20 و 60 أمبير عبر عدادات مباشرة، تسحب المنشآت الإنتاجية <strong>200A، 400A، 800A، وحتى أكثر من 3000 أمبير</strong> لكل طور. وإن إدخال هذه التيارات إلى داخل عداد القياس يُعد درباً من المستحيل عملياً ومصدراً لمخاطر حرارية كارثية.</p>
<p>يمثل <strong>عداد الطاقة المتصل بمحولات التيار (سلسلة DTSD / DSSD)</strong> الحل الهندسي القياسي الحاسم المعتمد عالمياً: عداد إلكتروني ذكي فائق الدقة يقيس الطاقة بشكل غير مباشر عبر محولات تيار متخصصة ذات <strong>مخارج ثانوية معيارية 5A أو 1A</strong>.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة عدادات DTSD الذكية</h2>
<ol>
  <li><strong>دقة متناهية مخصصة للفوترة (Class 0.5S):</strong> مطابقة للمواصفة القياسية العالمية IEC 62053-22 لضمان عدم ضياع أي جزء من الطاقة المباعة.</li>
  <li><strong>قياس متكامل في الأرباع الأربعة (4-Quadrant):</strong> يراقب الطاقة الفعالة المصدرة والمستوردة والطاقة غير الفعالة الحثية والسعوية للحد من غرامات انخفاض معامل القدرة.</li>
  <li><strong>نظام التعرفة متعدد الأوقات (TOU) وأقصى حمل (MD):</strong> مدعوم بساعة توقيت بلورية دقيقة تتيح احتساب كلفة الكهرباء طبقاً لساعات الذروة لتشجيع كفاءة الطاقة.</li>
  <li><strong>اتصالات رقمية مفتوحة DLMS/COSEM و Modbus RS485:</strong> سهولة الربط المباشر مع شبكات القراءة الآلية الذكية (AMI) ومنظومات التحكم والمراقبة SCADA.</li>
</ol>
'''
)

# ==============================================================================
# 2. COMPOSITE PIN INSULATOR (EN, FR, ES, AR)
# ==============================================================================

CPI_EN = dict(
    lang='en',
    dir='ltr',
    slug='overhead-distribution-lines-what-is-a-composite-pin-insulator',
    title='Overhead Medium-Voltage Lines: What Is a Composite Pin Insulator?',
    breadcrumb='Line Hardware &amp; Insulators',
    read='10 min read',
    alt='Medium-voltage Composite Polymer Pin Insulator (Model FPQ series, 24kV) with brick-red silicone rubber sheds mounted on a steel pole crossarm supporting an overhead distribution conductor',
    desc=('Medium-voltage overhead distribution lines (11kV to 33kV), rural power networks, and utility crossarms: What is a composite pin insulator? '
          'How hydrophobic silicone rubber sheds, high-tensile fiberglass epoxy core rods, hot-dip galvanized steel pins, and 12.5kN cantilever strength replace heavy porcelain insulators.'),
    model='Model FPQ Series 11kV / 24kV / 33kV Polymeric Composite Pin Insulators with High-Strength Forged Steel Spindle Pin (IEC 61952 / ANSI C29.18)',
    category='Line Hardware & Insulators / Composite Pin Insulators',
    kw='what is a composite pin insulator &middot; composite pin insulator &middot; polymer pin insulator &middot; pin insulator for distribution line &middot; 11kv 33kv pin insulator &middot; silicone pin insulator',
    specs=[
        ('Rated System Operating Voltage Class', 'Standard utility medium-voltage distribution ratings: 11kV, 15kV, 24kV, up to 36kV (highest system voltage: 38.5kV AC)'),
        ('Cantilever Mechanical Bending Strength', 'Standard rated mechanical cantilever failing load (SML): 5kN, 8kN, 10kN, up to 12.5kN bending strength'),
        ('Insulator Housing Material & Shed Design', 'High-temperature vulcanized (HTV) hydrophobic silicone rubber molded seamlessly over core rod (aerodynamic rain shed profile)'),
        ('Internal Structural Core Rod Material', 'Corrosion-resistant electrical-grade (ECR) glass-fiber reinforced epoxy resin core rod with high axial and bending modulus'),
        ('Mounting Spindle Pin Construction', 'Forged high-strength carbon steel spindle pin hot-dip galvanized to ASTM A153 / ISO 1461 with lead-threaded or nylon alloy head'),
        ('Creepage Distance & Pollution Performance', 'Extended specific creepage distance &ge; 31 mm/kV (Class IV heavy pollution / coastal marine resistance)'),
        ('Impulse Withstand & Power Frequency Test', 'Lightning impulse withstand voltage (BIL): up to 170kV–200kV peak; 1-minute wet power frequency withstand &ge; 70kV–85kV RMS'),
        ('Applicable International Quality Standards', 'Manufactured and type-tested to IEC 61952, ANSI C29.18, IEC 60815 (pollution evaluation), and ISO 9001 certified')
    ],
    faqs=[
        ('What is a Composite Pin Insulator and where is it installed on overhead electrical distribution networks?',
         'A Composite Pin Insulator—frequently termed a polymer pin insulator, silicone pin insulator, or composite line post/pin assembly—is '
         'a rigid, upright-mounted electrical distribution insulator engineered from advanced non-ceramic composite materials. '
         'It is mounted vertically (or angle-canted) on the wooden, steel, or concrete crossarms of utility distribution poles via a heavy threaded steel spindle pin. '
         'It serves two primary mechanical and electrical roles in 11kV to 33kV distribution networks: '
         '<ul>'
         '<li><strong>1. Mechanical Conductor Support on Straight Lines:</strong> The primary overhead bare aluminium conductor (such as ACSR, AAAC, or covered conductor) '
         'rests directly in the top saddle groove of the insulator head, secured firmly with preformed aluminium tie wires or ties. '
         'The insulator absorbs vertical conductor weight spans and lateral transverse wind loads.</li>'
         '<li><strong>2. High-Dielectric Line-to-Ground Isolation:</strong> The composite body maintains complete electrical isolation between the energized high-voltage line '
         'and the grounded crossarm and pole, preventing leakage currents and ground flashovers under all weather extremes.</li>'
         '</ul>'),
        ('Why are electrical utilities replacing traditional porcelain/ceramic pin insulators with composite polymer pin insulators?',
         'For over a century, electrical utilities relied on heavy porcelain pin insulators. However, modern distribution network operators '
         '(across Latin America, the Middle East, Central Asia, and Europe) are aggressively converting overhead lines to composite polymer pin insulators for four game-changing reasons: '
         '<ul>'
         '<li><strong>1. Superior Hydrophobicity &amp; Pollution Flashover Immunity:</strong> In coastal regions with salt fog or desert areas with industrial dust storms, '
         'porcelain surfaces become wetted and form a continuous conductive moisture film, triggering violent dry-band flashovers and outages. '
         'HTV silicone rubber possesses natural, permanent hydrophobicity (water-repellency). It breaks moisture into isolated discrete beads and transfers '
         'its hydrophobic low-molecular-weight chains into dust layers, completely suppressing leakage currents without requiring periodic manual insulator washing.</li>'
         '<li><strong>2. Extreme Vandalism &amp; Impact Resistance:</strong> Porcelain is brittle; stones, gunfire, or dropped tools during installation shatter ceramic sheds, '
         'destroying the insulator. The flexible silicone rubber sheds and internal fiberglass rod of a composite insulator absorb mechanical impacts without chipping, cracking, or breaking.</li>'
         '<li><strong>3. 70% Weight Reduction:</strong> A composite pin insulator weighs roughly 1.5 to 2.5 kg—up to 70% lighter than an equivalent heavy multi-skirt porcelain unit (6 to 9 kg). '
         'This drastically reduces transport shipping costs to remote rural sites, accelerates pole dressing times for linemen, and reduces structural pole crossarm loading.</li>'
         '<li><strong>4. Zero Explosive Shattering:</strong> When subjected to direct lightning strikes or heavy power arcs, porcelain can shatter explosively, showering hazardous shrapnel onto personnel below. '
         'Composite insulators do not shatter, providing safe puncture-proof mechanical retention.</li>'
         '</ul>'),
        ('How does the internal ECR fiberglass rod provide mechanical bending strength against wind and ice loads?',
         'The mechanical backbone of a composite pin insulator is its pultruded <strong>Electrical Corrosion Resistant (ECR) fiberglass rod</strong>. '
         'Composed of millions of continuous, axially aligned ECR glass filaments bound under high pressure with premium epoxy resin, '
         'the core rod exhibits exceptional tensile strength (&gt; 1000 MPa) and high flexural cantilever modulus. '
         'When gale-force winds or ice loads push the overhead conductor sideways, the bending forces are transmitted directly into the core rod '
         'and the hot-dip galvanized steel spindle, easily withstanding cantilever loads up to 10kN to 12.5kN without permanent plastic deformation.')
    ],
    cta='Procuring utility-grade medium-voltage line hardware, overhead distribution pole insulators, or hydrophobic silicone composite pin insulators (11kV to 33kV) compliant with IEC 61952 and ANSI C29.18? YOMIN manufactures high-reliability composite line insulators.',
    body='''
<h2>The Modern Insulating Vanguard for Medium-Voltage Overhead Distribution Lines</h2>
<p>Across thousands of miles of rural, suburban, and urban electrical grids worldwide, medium-voltage distribution lines operating at <strong>11kV, 15kV, 24kV, and 33kV</strong> deliver electrical power from primary zone substations to pole-mounted transformers and customer load centers.</p>
<p>Along these distribution routes, overhead bare aluminium conductors (ACSR, AAC, AAAC) must be rigidly supported aloft on pole crossarms while maintaining absolute dielectric isolation from the grounded wooden, concrete, or steel utility structures.</p>
<p>For decades, utilities relied on heavy, multi-part glazed porcelain pin insulators. However, in modern operating environments plagued by desert dust storms, ocean salt fog, severe seismic vibrations, and vandalism, ceramic insulators suffer frequent cracking, catastrophic pollution flashovers, and costly maintenance washing cycles.</p>
<p>The <strong>Polymeric Composite Pin Insulator (Model FPQ Series)</strong> represents the field-proven modern standard: a lightweight, shatterproof distribution insulator combining a high-strength fiberglass epoxy structural core with permanently hydrophobic silicone rubber sheds that repel water and prevent electrical leakage in the most severe industrial and coastal environments.</p>

<h2>Engineering Anatomy: Inside a Certified High-Performance Composite Pin Insulator</h2>
<ol>
  <li><strong>High-Temperature Vulcanized (HTV) Silicone Rubber Housing:</strong> Injection-molded seamlessly over the core under high pressure and temperature, eliminating internal voids or air pockets. The silicone formulation provides permanent hydrophobicity and resistance to ultraviolet (UV) radiation and ozone.</li>
  <li><strong>Corrosion-Resistant (ECR) Fiberglass Core Rod:</strong> Pultruded from boron-free electrical corrosion resistant glass fibers and epoxy resin, delivering exceptional cantilever bending strength (up to 12.5kN) and immunity to brittle acid-rot fracture.</li>
  <li><strong>Aerodynamic Rain Shed Profile:</strong> Precision-molded alternating shed geometry maximizes creepage distance (&ge; 31 mm/kV) while allowing natural wind self-cleaning and preventing continuous water cascades during tropical downpours.</li>
  <li><strong>Hot-Dip Galvanized Forged Steel Spindle Pin:</strong> Heavy-duty forged carbon steel mounting pin galvanized to ASTM A153 with standardized thread diameters (e.g., 20mm or 25mm), secured to the pole crossarm with a curved lock washer and hex nut.</li>
  <li><strong>Tie-Top Conductor Groove with Wire-Binding Saddle:</strong> Precision-formed top saddle groove accommodates distribution conductors from 35 mm&sup2; up to 240 mm&sup2;, secured with standard preformed helical ties or aluminium tie wire without conductor abrasion.</li>
</ol>

<h2>Comparison: Polymeric Composite Pin Insulator vs. Traditional Glazed Porcelain Pin Insulator</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Traditional Glazed Porcelain Pin Insulator</th>
      <th>YOMIN Polymeric Composite Pin Insulator (FPQ Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Total Unit Weight &amp; Handling</strong></td>
      <td>Heavy (6.0 kg to 9.5 kg); high freight costs and arduous pole climbing.</td>
      <td><strong>Ultra-Lightweight (1.8 kg to 2.8 kg): ~70% lighter; fast, ergonomic installation.</strong></td>
    </tr>
    <tr>
      <td><strong>Pollution &amp; Salt Fog Performance</strong></td>
      <td>Hydrophilic surface; water films cause leakage currents and flashovers.</td>
      <td><strong>Permanently Hydrophobic: Silicone beads water; zero washing required in heavy pollution.</strong></td>
    </tr>
    <tr>
      <td><strong>Mechanical Impact &amp; Vandalism Resilience</strong></td>
      <td>Brittle: Shatters easily from stone impacts, transport vibration, or dropped tools.</td>
      <td><strong>Shatterproof: Flexible silicone sheds and fiberglass core absorb severe mechanical impacts.</strong></td>
    </tr>
    <tr>
      <td><strong>Safety Under Flashover / Arc Events</strong></td>
      <td>Risk of explosive ceramic shrapnel injuring linemen and ground personnel.</td>
      <td><strong>Zero Shrapnel: Polymer housing does not fragment or violently rupture under arc faults.</strong></td>
    </tr>
    <tr>
      <td><strong>Long-Term Lifecycle Maintenance Costs</strong></td>
      <td>Requires periodic costly high-pressure washing and replacement of cracked units.</td>
      <td><strong>Maintenance-free 30+ year service life; eliminates wash cycles and line inspection trips.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

CPI_FR = dict(
    lang='fr',
    dir='ltr',
    slug='overhead-distribution-lines-what-is-a-composite-pin-insulator-fr',
    title="Lignes Aériennes Moyenne Tension : Qu'est-ce qu'un Isolateur Rigide Composite (Pin Insulator) ?",
    breadcrumb='Matériel de Ligne &amp; Isolateurs',
    read='10 min de lecture',
    alt='Isolateur rigide composite moyenne tension (Série FPQ, 24kV) à ailettes en silicone brique monté sur traverse métallique de poteau de distribution électrique',
    desc=('Lignes aériennes de distribution moyenne tension (11kV à 33kV), réseaux ruraux et traverses de poteaux : Qu\'est-ce qu\'un isolateur rigide composite (Pin Insulator) ? '
          'Jupe en silicone hydrophobe, tige en fibre de verre résine époxy, tige de fixation en acier galvanisé à chaud et tenue en flexion de 12,5kN.'),
    model='Série FPQ : Isolateurs Rigides Composites pour Réseaux de Distribution HTA (11kV / 24kV / 33kV, Tige en Acier Forgé, CEI 61952 / ANSI C29.18)',
    category='Matériel de Ligne & Isolateurs / Isolateurs Rigides Composites',
    kw='isolateur composite &middot; isolateur pin insulator &middot; isolateur moyenne tension 24kv &middot; isolateur silicone hta &middot; materiel de ligne aerienne &middot; isolateur support poteau',
    specs=[
        ('Classe de Tension Assignée du Réseau', 'Tensions normalisées de distribution moyenne tension : 11kV, 15kV, 24kV jusqu\'à 36kV (tension la plus élevée : 38,5kV AC)'),
        ('Charge Mécanique de Rupture en Flexion', 'Charge mécanique nominale de rupture en flexion (SML) : 5kN, 8kN, 10kN jusqu\'à 12,5kN'),
        ('Matériau de l\'Enveloppe et Ailettes', 'Silicone HTV vulcanisé à chaud sans soudure, hydrophobe permanent avec profil aérodynamique auto-nettoyant'),
        ('Tige Centrale Isolante Structurelle', 'Tige en résine époxy renforcée de fibres de verre sans bore (ECR) à haute résistance mécanique et électrique'),
        ('Tige de Fixation Métallique (Spindle Pin)', 'Acier forgé à haute résistance galvanisé à chaud selon ISO 1461 avec embout fileté en alliage de plomb'),
        ('Ligne de Fuite et Tenue à la Pollution', 'Ligne de fuite spécifique supérieure à 31 mm/kV (Classe IV pour environnements de très forte pollution côtière ou désertique)'),
        ('Tenue Diélectrique aux Chocs et à Fréquence', 'Tension de tenue au choc de foudre (BIL) jusqu\'à 170kV–200kV crête ; tension sous pluie 1 min &ge; 70kV–85kV RMS'),
        ('Normes Internationales Applicables', 'Conforme aux normes CEI 61952, ANSI C29.18, CEI 60815 (sélection des isolateurs sous pollution) et certifié ISO 9001')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Isolateur Rigide Composite (Pin Insulator) et quel est son rôle sur les poteaux de distribution ?',
         'Un Isolateur Rigide Composite—universellement appelé isolateur à tige composite ou Pin Insulator—est '
         'un appareil d\'isolation électromécanique monté dressé sur les traverses métalliques, en béton ou en bois des poteaux de lignes aériennes HTA (11kV à 33kV). '
         'Il remplit deux missions indissociables sur le réseau : '
         '<ul>'
         '<li><strong>1. Support Mécanique du Conducteur de Ligne :</strong> Le câble conducteur nu en aluminium (ACSR, Aster) repose dans la gorge supérieure '
         'de la tête de l\'isolateur, maintenu par un lien préformé. L\'isolateur supporte le poids vertical de la portée et les poussées transversales du vent.</li>'
         '<li><strong>2. Isolation Diélectrique vis-à-vis de la Terre :</strong> Le corps composite isole parfaitement la ligne sous tension par rapport à la traverse '
         'mise à la terre, empêchant tout courant de fuite et amorçage par tous les temps.</li>'
         '</ul>'),
        ('Pourquoi les distributeurs remplacent-ils les isolateurs traditionnels en porcelaine par des isolateurs composites en silicone ?',
         'Les compagnies d\'électricité abandonnent massivement la porcelaine au profit des isolateurs composites pour quatre raisons techniques majeures : '
         '<ul>'
         '<li><strong>1. Hydrophobie Permanente et Résistance aux Amorçages :</strong> En zone côtière (brouillard salin) ou désertique (poussières et sable), '
         'la porcelaine se recouvre d\'un film d\'eau conducteur qui provoque des arcs de contournement dévastateurs. '
         'Le caoutchouc de silicone est naturellement hydrophobe : il fragmente l\'eau en gouttelettes isolées et transfère ses propriétés hydrophobes '
         'aux dépôts de poussière, éliminant tout besoin de lavage périodique sous tension.</li>'
         '<li><strong>2. Immunité Totale contre le Vandalisme et les Chocs :</strong> La porcelaine est cassante et éclate sous les jets de pierres. '
         'Les ailettes souples en silicone et le noyau en fibre de verre encaissent les chocs sans aucune fissuration.</li>'
         '<li><strong>3. Allègement de 70% :</strong> Un isolateur composite pèse environ 2 kg contre 7 à 9 kg pour son équivalent en porcelaine, '
         'ce qui facilite considérablement le transport en zone rurale d\'accès difficile et le travail des lignards en tête de poteau.</li>'
         '<li><strong>4. Aucun Éclat Dangereux :</strong> En cas d\'impact de foudre direct, la porcelaine explose en éclats tranchants dangereux pour le personnel au sol. '
         'L\'isolateur composite ne vole pas en éclats.</li>'
         '</ul>'),
        ('Comment la tige interne en fibre de verre ECR encaisse-t-elle les contraintes mécaniques du vent ?',
         'L\'ossature de l\'isolateur est constituée d\'une tige en résine époxy pultrudée chargée de millions de filaments de verre continu (verre ECR insensible aux acides). '
         'Avec une résistance à la traction supérieure à 1000 MPa, cette tige absorbe les efforts de flexion colossaux générés par les tempêtes sur les câbles, '
         'résistant à des charges de flexion de 10kN à 12,5kN sans déformation permanente.')
    ],
    cta='Vous déployez des réseaux aériens moyenne tension (11kV à 33kV), des projets d\'électrification rurale ou recherchez des isolateurs composites rigides certifiés CEI 61952 ? YOMIN fabrique des isolateurs composites haute performance résistants aux climats sévères.',
    body='''
<h2>Le Standard Moderne d\'Isolation pour les Réseaux de Distribution Aériens HTA</h2>
<p>Sur des millions de kilomètres de réseaux électriques moyenne tension à travers le monde, les lignes aériennes fonctionnant à <strong>11kV, 15kV, 24kV et 33kV</strong> acheminent l\'énergie depuis les postes sources vers les transformateurs de distribution.</p>
<p>Le long de ces lignes, les conducteurs nus en aluminium doivent être solidement maintenus au sommet des poteaux tout en garantissant un isolement diélectrique absolu par rapport aux structures métalliques reliées à la terre.</p>
<p>Pendant plus d\'un siècle, les électriciens ont utilisé de lourds isolateurs rigides en porcelaine vernissée. Mais dans les environnements pollués, soumis aux vents marins, aux tempêtes de sable et aux actes de malveillance, la porcelaine se fissure, s\'encrasse et génère de fréquents contournements d\'arc électrique.</p>
<p>L\'<strong>Isolateur Rigide Composite en Silicone (Série FPQ)</strong> s\'impose aujourd\'hui comme la référence universelle : un isolateur léger, incassable, associant une tige en fibre de verre haute résistance à une jupe en caoutchouc de silicone hydrophobe qui repousse l\'eau et la saleté dans les pires conditions climatiques.</p>

<h2>Conception Mécanique et Éléments de Robustesse</h2>
<ol>
  <li><strong>Enveloppe en Silicone HTV Vulcanisée sous Haute Pression :</strong> Élimine tout interstice ou bulle d\'air interne, assurant une protection totale contre les rayonnements UV et l\'ozone.</li>
  <li><strong>Noyau en Fibre de Verre ECR Résistant à la Corrosion :</strong> Pultrudé avec une résine époxy de haute pureté pour supporter des efforts de flexion allant jusqu\'à 12,5kN.</li>
  <li><strong>Profil d\'Ailettes Aérodynamique Auto-Nettoyant :</strong> Permet une ligne de fuite généreuse supérieure à 31 mm/kV empêchant la création de ponts aqueux sous pluies battantes.</li>
  <li><strong>Tige de Fixation en Acier Forgé Galvanisé à Chaud :</strong> Fixe solidement l\'isolateur sur la traverse métallique avec une tenue anticorrosion irréprochable.</li>
</ol>
'''
)

CPI_ES = dict(
    lang='es',
    dir='ltr',
    slug='overhead-distribution-lines-what-is-a-composite-pin-insulator-es',
    title='Líneas Aéreas de Media Tensión: ¿Qué es un Aislador Tipo Espiga Compuesto (Pin Insulator)?',
    breadcrumb='Herrajes de Línea y Aisladores',
    read='10 min de lectura',
    alt='Aislador tipo espiga compuesto polimérico de media tensión (Serie FPQ, 24kV) con aletas de caucho de silicona instalado en cruceta de poste de distribución eléctrica',
    desc=('Líneas aéreas de distribución en media tensión (11kV a 33kV), redes rurales y crucetas de postes: ¿Qué es un aislador tipo espiga compuesto (pin insulator)? '
          'Aletas de silicona hidrofóbica, núcleo de fibra de vidrio y resina epoxi, perno de acero galvanizado en caliente y resistencia a la flexión de 12,5kN.'),
    model='Serie FPQ: Aisladores Tipo Espiga Compuestos para Distribución Eléctrica en Media Tensión (11kV / 24kV / 33kV, Perno Forjado, IEC 61952 / ANSI C29.18)',
    category='Herrajes de Línea y Aisladores / Aisladores Tipo Espiga Compuestos',
    kw='aislador compuesto tipo espiga &middot; aislador pin insulator &middot; aislador polimerico 24kv &middot; aislador de silicona media tension &middot; aislador cruceta poste',
    specs=[
        ('Clase de Tensión Asignada del Sistema', 'Tensiones normalizadas de distribución en media tensión: 11kV, 15kV, 24kV hasta 36kV (tensión máxima del equipo: 38,5kV AC)'),
        ('Carga Mecánica de Rotura a la Flexión', 'Carga mecánica nominal de rotura en voladizo (SML): 5kN, 8kN, 10kN hasta 12,5kN de esfuerzo a la flexión'),
        ('Material del Revestimiento y Diseño de Aletas', 'Caucho de silicona HTV vulcanizado a alta temperatura sin costuras, con hidrofobicidad permanente y perfil autolimpiante'),
        ('Núcleo Estructural Aislante Interior', 'Varilla de resina epoxi reforzada con fibras de vidrio continuas libres de boro (ECR) resistente a la corrosión ácida'),
        ('Perno de Fijación a la Cruceta (Spindle Pin)', 'Perno de acero forjado de alta resistencia galvanizado por inmersión en caliente según ISO 1461 con rosca de aleación de plomo'),
        ('Distancia de Fuga y Comportamiento ante Polución', 'Distancia de fuga específica superior a 31 mm/kV (Clase IV para zonas de contaminación industrial y niebla marina severa)'),
        ('Tensión de Ensayo al Impulso y Frecuencia', 'Tensión soportada al impulso tipo rayo (BIL) hasta 170kV–200kV cresta ; tensión soportada bajo lluvia a frecuencia industrial &ge; 70kV–85kV RMS'),
        ('Normativas Internacionales de Calidad', 'Fabricado y ensayado bajo normas IEC 61952, ANSI C29.18, IEC 60815 (aisladores bajo contaminación) y certificación ISO 9001')
    ],
    faqs=[
        ('¿Qué es un Aislador Tipo Espiga Compuesto (Pin Insulator) y dónde se instala en las redes de distribución?',
         'Un Aislador Tipo Espiga Compuesto—conocido en el sector eléctrico como aislador de espiga polimérico o Pin Insulator—es '
         'un dispositivo de aislamiento electromecánico rígido que se monta de forma vertical sobre las crucetas de madera, acero o concreto en postes de distribución aérea (11kV a 33kV). '
         'Cumple dos funciones técnicas insustituibles en la red: '
         '<ul>'
         '<li><strong>1. Soporte Físico del Conductor Eléctrico:</strong> El cable de aluminio desnudo (ACSR, AAC o protegido) descansa en la ranura superior '
         'del cabezal del aislador y se fija firmemente con ataduras de alambre o lazos preformados. Soporta el peso del vano y los empujes laterales del viento.</li>'
         '<li><strong>2. Aislamiento Dieléctrico frente a Tierra:</strong> El cuerpo compuesto impide que la corriente de alta tensión se fugue hacia la cruceta '
         'y la estructura del poste, evitando cortocircuitos a tierra bajo cualquier condición climática.</li>'
         '</ul>'),
        ('¿Por qué las compañías eléctricas están reemplazando los aisladores tradicionales de porcelana por aisladores compuestos de silicona?',
         'Las empresas distribuidoras de energía en todo el mundo están sustituyendo la porcelana por aisladores poliméricos debido a cuatro ventajas concluyentes: '
         '<ul>'
         '<li><strong>1. Hidrofobicidad Permanente e Inmunidad al Flameo:</strong> En costas con niebla salina o desiertos con polvo, la porcelana '
         'se moja formando una película continua de agua conductora que provoca arcos eléctricos destructivos (flameos). '
         'La silicona HTV es permanentemente hidrofóbica: fragmenta el agua en gotas aisladas y transfiere sus moléculas a las capas de polvo, '
         'eliminando por completo las corrientes de fuga sin requerir lavados periódicos.</li>'
         '<li><strong>2. Resistencia al Vandalismo y Golpes:</strong> La porcelana se astilla y quiebra con impactos de piedras o caídas durante el montaje. '
         'Las aletas flexibles de silicona y el núcleo de fibra de vidrio absorben impactos mecánicos sin romperse jamás.</li>'
         '<li><strong>3. Reducción de Peso del 70%:</strong> Pesa entre 1,5 y 2,5 kg frente a los 7 a 9 kg de un aislador de porcelana equivalente, '
         'lo que facilita el transporte a zonas rurales remotas y alivia el esfuerzo de los linieros en altura.</li>'
         '<li><strong>4. Cero Fragmentación Peligrosa:</strong> Ante impactos directos de rayos, la porcelana puede explotar esparciendo metralla cortante. '
         'El aislador compuesto no se fragmenta, salvaguardando la seguridad del personal en tierra.</li>'
         '</ul>'),
        ('¿Cómo resiste la varilla interior de fibra de vidrio los vientos extremos?',
         'La columna vertebral del aislador es una varilla de resina epoxi pultruida con millones de fibras continuas de vidrio ECR de alta resistencia química. '
         'Con una resistencia a la tracción superior a 1000 MPa, esta barra absorbe las tremendas cargas laterales del viento y el hielo sobre los conductores, '
         'soportando esfuerzos en voladizo de 10kN a 12,5kN sin sufrir deformación plástica permanente.')
    ],
    cta='¿Construye líneas de distribución aérea en media tensión (11kV a 33kV), redes de electrificación rural o requiere aisladores tipo espiga compuestos bajo norma IEC 61952? YOMIN fabrica aisladores poliméricos de alta confiabilidad técnica para climas exigentes.',
    body='''
<h2>La Evolución Tecnológica del Aislamiento en Líneas Aéreas de Media Tensión</h2>
<p>A lo largo de incontables kilómetros de redes eléctricas de distribución en todo el planeta, las líneas aéreas que operan en <strong>11kV, 15kV, 24kV y 33kV</strong> transportan energía eléctrica desde subestaciones transformadoras hasta centros urbanos y rurales.</p>
<p>En este tendido, los cables conductores de aluminio deben mantenerse firmemente suspendidos en lo alto de las crucetas de los postes, garantizando un aislamiento dieléctrico infranqueable respecto a las estructuras puestas a tierra.</p>
<p>Durante décadas se utilizaron aisladores de porcelana vidriada. Sin embargo, en zonas costeras salinas, desiertos polvorientos o áreas expuestas a vandalismo, la porcelana sufre roturas mecánicas, acumulación de suciedad y costosos arcos de contorneo.</p>
<p>El <strong>Aislador Tipo Espiga Compuesto Polimérico (Serie FPQ)</strong> representa el estándar consolidado en las compañías de distribución: un aislador sumamente liviano e irrompible que combina un núcleo estructural de fibra de vidrio con un recubrimiento de silicona hidrofóbica que repele el agua y la contaminación en los climas más severos.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería</h2>
<ol>
  <li><strong>Revestimiento de Silicona HTV Vulcanizado en una Sola Pieza:</strong> Moldeado a alta presión sobre el núcleo de fibra de vidrio para eliminar cualquier espacio de aire interno y resistir la radiación UV y el ozono.</li>
  <li><strong>Núcleo de Fibra de Vidrio ECR Resistente a la Corrosión:</strong> Proporciona una rigidez estructural insuperable capaz de soportar cargas a la flexión de hasta 12,5kN sin fracturarse.</li>
  <li><strong>Aletas de Diseño Aerodinámico Autolimpiante:</strong> Maximizan la distancia de fuga (&ge; 31 mm/kV) impidiendo la formación de caminos conductores durante tormentas severas.</li>
  <li><strong>Perno de Acero Forjado Galvanizado en Caliente:</strong> Asegura una fijación sólida e inalterable sobre la cruceta del poste con protección anticorrosiva para más de 30 años de servicio.</li>
</ol>
'''
)

CPI_AR = dict(
    lang='ar',
    dir='rtl',
    slug='overhead-distribution-lines-what-is-a-composite-pin-insulator-ar',
    title='خطوط التوزيع الهوائية للجهد المتوسط: ما هو العازل المسماري المركب (Composite Pin Insulator)؟',
    breadcrumb='مهمات الخطوط والعوازل',
    read='10 دقائق قراءة',
    alt='عازل مسماري مركب للجهد المتوسط (موديل FPQ، جهد 24kV) بمظلات سيليكون حمراء مثبت على ذراع معدني لعمود توزيع كهربائي هوائي',
    desc=('خطوط التوزيع الهوائية للجهد المتوسط (11kV إلى 33kV)، والشبكات الريفية، وأذرع الأعمدة: ما هو العازل المسماري المركب (Pin Insulator)؟ '
          'مظلات مطاط السيليكون الكارهة للماء، وقلب ألياف الزجاج والراتنج الإيبوكسي فائق المتانة، ومسمار الصلب المجلفن بالغمس الساخن، وصمود ميكانيكي حتى 12.5kN.'),
    model='سلسلة FPQ: عوازل التوزيع الهوائية المسمارية المركبة لشبكات الجهد المتوسط (11kV / 24kV / 33kV، مسمار صلب مطروق، معتمدة IEC 61952 / ANSI C29.18)',
    category='مهمات الخطوط والعوازل / العوازل المسمارية المركبة',
    kw='عازل مسماري مركب &middot; composite pin insulator &middot; عازل سيليكون 24kv &middot; عازل خطوط هوائية &middot; عازل عمود كهرباء &middot; عازل بوليمري جهد متوسط',
    specs=[
        ('فئة جهد التشغيل المقنن للشبكة', 'فئات تشغيل معيارية لشبكات التوزيع: 11kV، 15kV، 24kV وحتى 36kV (أعلى جهد تشغيلي للمعدة: 38.5kV AC)'),
        ('قوة التحمل الميكانيكية للكسر بالانحناء', 'الحمل الميكانيكي الاسمي المعياري للكسر بالانحناء (SML): 5kN، 8kN، 10kN وحتى 12.5kN قوة انحناء كابولية'),
        ('مادة غلاف العازل وتصميم المظلات', 'مطاط سيليكون مبركن حرارياً (HTV) عالي الكراهية للماء مصبوب دون أي فواصل بتصميم انسيابي طارد للأمطار'),
        ('مادة القلب الإنشائي العازل الداخلي', 'قضيب متين من الألياف الزجاجية المقاومة للتآكل الحمضي (ECR) المدمجة براتنج الإيبوكسي المسحوب بالبثق الحراري'),
        ('مسمار التثبيت الفولاذي (Spindle Pin)', 'مسمار فولاذ كربوني مطروق عالي المتانة مجلفن بالغمس الساخن طبقاً لـ ISO 1461 بسن ملولب من سبائك الرصاص المتينة'),
        ('مسافة التسرب السطحي والأداء تحت التلوث', 'مسافة تسرب نوعية ممتدة تفوق 31 mm/kV (الفئة الرابعة Class IV لمقاومة أعتى البيئات الملوثة والضباب الساحلي الملحي)'),
        ('صمود جهد الصواعق والتردد الصناعي', 'جهد صمود نبضات الصواعق (BIL) حتى 170kV–200kV ذروة؛ وجهد صمود التردد الصناعي تحت المطر لمدة دقيقة &ge; 70kV–85kV RMS'),
        ('مطابقة المواصفات القياسية الدولية', 'مصنع ومختبر بالكامل وفقاً للمواصفات الدولية IEC 61952 و ANSI C29.18 و IEC 60815 ومطابق لنظام إدارة الجودة ISO 9001')
    ],
    faqs=[
        ('ما هو العازل المسماري المركب (Composite Pin Insulator) وأين يُركب في خطوط التوزيع الهوائية؟',
         'العازل المسماري المركب—والمعروف في مشاريع الكهرباء باسم عازل البوليمر المسماري أو عازل السيليكون الرأسي—هو '
         'عازل كهربائي صلب يُثبت رأسياً على الأذرع العرضية (الكروس آرم) الخشبية أو الفولاذية أو الخرسانية لأعمدة التوزيع الهوائي (11kV إلى 33kV). '
         'يؤدي هذا العازل وظيفتين هندسيتين حاسمتين لضمان استقرار الشبكة: '
         '<ul>'
         '<li><strong>1. التثبيت الميكانيكي لموصلات الخط:</strong> يستقر الموصل الهوائي المصنوع من الألومنيوم المقوى بالفولاذ (ACSR) في المجرى العلوي '
         'لرأس العازل، ويُربط بإحكام باستخدام أسلاك أو روابط ربط حلزونية مسبقة التشكيل، ليتحمل وزن السلك وقوى الرياح الجانبية.</li>'
         '<li><strong>2. العزل الكهربائي التام عن الأرض:</strong> يوفر الجسم البوليمري عزلاً ديإلكتريكياً مطلقاً بين سلك الجهد العالي الحي وجسم الذراع والعمود المؤرضين، '
         'مانعاً تسرب التيارات الكهربائية وحدوث تفريغ أرضي تحت كافة الظروف المناخية.</li>'
         '</ul>'),
        ('لماذا تستبدل شركات الكهرباء وهيئات التوزيع عوازل الخزف التقليدية بالعوازل المسمارية المركبة المصنوعة من السيليكون؟',
         'تتجه شركات الكهرباء في الشرق الأوسط وأوروبا وأمريكا اللاتينية نحو اعتماد العوازل المركبة لعدة أسباب فنية قاطعة: '
         '<ul>'
         '<li><strong>1. كراهية الماء ومقاومة التلوث الساحلي والصحراوي:</strong> في المناطق الساحلية المعرضة للضباب الملحي أو الصحراوية ذات الغبار الكثيف، '
         'يتبلل سطح الخزف مشكلاً طبقة ماء ناقلة تسبب وميضاً كهربائياً متفجراً (Flashover). '
         'أما مطاط السيليكون فيتمتع بخاصية كراهية الماء الدائمة (Hydrophobic)؛ إذ يفتت المياه إلى قطرات معزولة وينقل جزيئاته الطاردة للرطوبة '
         'إلى طبقة الغبار، ملغياً تيارات التسرب دون الحاجة لأي غسيل يدوي مكلف.</li>'
         '<li><strong>2. المقاومة التامة للصدمات والعبث:</strong> الخزف مادة هشة تنكسر برمي الحجارة أو الاهتزازات. '
         'أما مظلات السيليكون المرنة وقلب ألياف الزجاج الصلب فيمتصان الصدمات الميكانيكية دون أي تصدع أو تشقق نهائياً.</li>'
         '<li><strong>3. خفة الوزن الفائقة (توفير 70% من الوزن):</strong> يزن العازل المركب حوالي 2 كغ فقط مقابل 7 إلى 9 كغ لنظيره الخزفي، '
         'مما يقلل تكاليف الشحن إلى المناطق الريفية الوعرة ويسهل عمل الفنيين على قمة العمود.</li>'
         '<li><strong>4. انعدام الشظايا المتطايرة:</strong> عند تعرض الخط لصاعقة مباشرة، قد يتفجر العازل الخزفي لشظايا حادة تصيب المارة؛ أما العازل المركب فلا يتشظى.</li>'
         '</ul>'),
        ('كيف يقاوم قضيب الألياف الزجاجية الداخلي (ECR) قوى الرياح العاتية وثقل الأسلاك؟',
         'يمثل قضيب الراتنج الإيبوكسي المدعم بألياف الزجاج المقاوم للتآكل (ECR Core) العمود الفقري للعازل. '
         'يحتوي على ملايين الخيوط الزجاجية الموجهة محورياً، ويتميز بمقاومة شد تتجاوز 1000 ميغاباسكال، '
         'مما يمكنه من امتصاص عزوم الانحناء الهائلة الناتجة عن هبوب العواصف على الأسلاك وتحمل إجهادات كابولية تصل إلى 12.5kN دون أي انحناء دائم.')
    ],
    cta='هل تعمل على مد شبكات التوزيع الهوائي للجهد المتوسط (11kV إلى 33kV)، أو مشاريع كهربة القرى، أو توريد العوازل المسمارية المركبة المعتمدة طبقاً لمواصفات IEC 61952؟ تصنع يمين (YOMIN) عوازل توزيع سيليكونية مركبة فائقة الاعتمادية للبيئات القاسية.',
    body='''
<h2>الجيل المتطور لعزل شبكات توزيع الكهرباء الهوائية للجهد المتوسط</h2>
<p>عبر مئات الآلاف من الكيلومترات من خطوط التوزيع الكهربائي حول العالم، تقوم الشبكات الهوائية العاملة عند جهود <strong>11kV و 15kV و 24kV و 33kV</strong> بنقل الطاقة من محطات التوزيع الرئيسية إلى المحولات وأعمدة الإنارة والمجمعات السكنية.</p>
<p>وطوال مسار هذه الخطوط، يجب أن تُثبت موصلات الألومنيوم الهوائية بقوة فوق أذرع الأعمدة مع ضمان عزل ديإلكتريكي مطلق لا يسمح بتسرب الطاقة إلى الهيكل المؤرض للعمود.</p>
<p>لعقود طويلة، اعتمدت شركات الكهرباء على عوازل الخزف المزجج الثقيلة. لكن في البيئات المعاصرة المعرضة للعواصف الرملية في الصحاري، والضباب الملحي البحري، وحوادث الرشق والاهتزاز، باتت عوازل الخزف مصدراً لانقطاعات متكررة وتكاليف صيانة باهظة.</p>
<p>يقدم <strong>العازل المسماري المركب المصنوع من السيليكون (سلسلة FPQ)</strong> الحل الهندسي القياسي المتفوق: عازل خفيف الوزن وغير قابل للكسر، يجمع بين قلب إنشائي متين من الألياف الزجاجية الإيبوكسية ومظلات سيليكونية كارهة للماء والشوائب، محققاً استقراراً دائماً للشبكة في أقسى المناخات.</p>

<h2>المكونات الهندسية وميزات المتانة والتصنيع</h2>
<ol>
  <li><strong>غلاف من مطاط السيليكون المبركن حرارياً (HTV):</strong> مصبوب بالحقن المتكامل تحت ضغط عالٍ ليمنع تشكل أي فجوات هوائية ويقاوم الأشعة فوق البنفسجية والأوزون.</li>
  <li><strong>قلب إنشائي من ألياف الزجاج ECR المعالج:</strong> مسحوب بأحدث تقنيات البثق ليتحمل إجهادات انحناء تفوق 12.5kN لمقاومة العواصف العاتية.</li>
  <li><strong>مظلات هوائية طاردة للأمطار:</strong> تصميم هندسي يضاعف مسافة التسرب السطحي (&ge; 31 mm/kV) ويمنع تشكل مسارات مائية موصلة تحت الأمطار الغزيرة.</li>
  <li><strong>مسمار فولاذي صلب مجلفن بالغمس الساخن:</strong> يوفر تثبيتاً حديدياً لا يتزعزع على الذراع العرضي للعمود مع حماية فائقة من الصدأ لعشرات السنين.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1009 = [
    CTM_EN, CTM_FR, CTM_ES, CTM_AR,
    CPI_EN, CPI_FR, CPI_ES, CPI_AR
]
