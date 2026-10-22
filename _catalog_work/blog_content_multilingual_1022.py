# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-22:
1. Distribution Boards: What Is an Over and Under Voltage Protector? (EN, FR, ES, AR)
2. Control Panels: What Is a Power Distribution Block? (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. OVER AND UNDER VOLTAGE PROTECTOR (EN, FR, ES, AR)
# ==============================================================================

OUV_EN = dict(
    lang='en',
    dir='ltr',
    slug='distribution-boards-what-is-an-over-and-under-voltage-protector',
    title='Distribution Boards: What Is an Over and Under Voltage Protector?',
    breadcrumb='Distribution Boards &amp; Voltage Protectors',
    read='10 min read',
    alt='Residential electrical consumer unit interior showing a digital DIN rail self-restoring over and under voltage protector with live dual LED display actively protecting branch circuits',
    desc=('Residential consumer units, commercial distribution boards, and HVAC compressor protection: What is an over and under voltage protector? '
          'How digital voltage monitoring relays detect sags, swells, brownouts, and neutral line disconnection, disconnect downstream loads in under 0.1s, '
          'and execute auto-reclosing timer delay sequences under IEC 60947-2.'),
    model='Model VAP-2P & VAP-3P Series 40A–63A–80A Single-Phase & Three-Phase Digital Self-Restoring Over and Under Voltage Protectors (Dual LED Display, Adjustable Thresholds, Auto-Reclosing Timer, Certified IEC 60947-2)',
    category='Distribution Boards & Voltage Protectors / Voltage Protection Devices',
    kw='what is an over and under voltage protector &middot; over and under voltage protector &middot; din rail voltage protector &middot; self reclosing voltage protector &middot; automatic voltage protector &middot; voltage surge protector home &middot; iec 60947-2',
    specs=[
        ('Rated Operational Voltage ($U_e$)', 'Standard ratings of $220\,\text{V} / 230\,\text{V AC}$ (Single Phase) and $380\,\text{V} / 400\,\text{V AC}$ (Three Phase, 50Hz/60Hz)'),
        ('Rated Operational Current ($I_e$)', 'Standard continuous load capacities of $40\,\text{A}$, $63\,\text{A}$, and $80\,\text{A}$ matching main consumer unit breaker ratings'),
        ('Overvoltage Tripping Threshold Range', 'User-adjustable from $230\,\text{V}$ to $300\,\text{V AC}$ (Default: $270\,\text{V}$); Disconnect trip response time $< 0.1\,\text{seconds}$'),
        ('Undervoltage Tripping Threshold Range', 'User-adjustable from $140\,\text{V}$ to $210\,\text{V AC}$ (Default: $170\,\text{V}$); Disconnect trip response time $< 0.1\,\text{seconds}$'),
        ('Auto-Reclosing Power Recovery Delay', 'Programmable reset delay from $1\,\text{s}$ to $500\,\text{s}$ (Default: $30\,\text{s}$) to prevent motor short-cycling after grid restoration'),
        ('Overcurrent Protection Setting', 'Adjustable overcurrent cut-off from $1\,\text{A}$ to $63\,\text{A}$ (or $80\,\text{A}$) providing auxiliary thermal overload protection'),
        ('Digital Measurement & Display Interface', 'Dual high-visibility 3-digit 7-segment LED displays showing real-time RMS grid voltage (Red) and actual load current (Green)'),
        ('International Manufacturing Standards', 'Fully tested and compliant with IEC 60947-2, IEC 60898-1, and CE Low Voltage Directive requirements')
    ],
    faqs=[
        ('What is an over and under voltage protector and how does it differ from a surge arrester (SPD)?',
         'An over and under voltage protector (often designated as Model VAP or self-restoring voltage relay) is an active digital protection '
         'switch that continuously monitors RMS grid voltage and disconnects downstream power whenever the voltage climbs above a safe ceiling '
         'or plunges below a safe floor. '
         '<strong>Crucial difference from a Surge Protective Device (SPD):</strong> '
         '<ul>'
         '<li><strong>Surge Protective Device (SPD / Type 2):</strong> Diverts microsecond-duration high-voltage transient spikes (such as indirect lightning strikes or utility switching transients of $1\,\text{kV}$ to $6\,\text{kV}$) to earth using metal oxide varistors (MOVs). SPDs cannot protect against sustained multi-second overvoltages or low-voltage brownouts.</li>'
         '<li><strong>Over/Under Voltage Protector (VAP):</strong> Handles sustained power-frequency abnormal voltages (sags, swells, brownouts, and neutral line disconnection) lasting from tens of milliseconds to hours. When grid voltage deviates, it opens its internal contactor, completely isolating appliances until voltage normalizes.</li>'
         '</ul>'
         'For complete consumer unit protection, engineering best practice places a Type 2 SPD in parallel, followed by a series-installed self-restoring voltage protector.'),
        ('Why is the auto-reclosing recovery delay timer essential for air conditioners and refrigerators?',
         'When utility grid power fluctuates or sags momentarily, power may bounce off and on within a few seconds. '
         'In refrigeration compressors, air conditioner heat pumps, and electric motors, the refrigerant gas remains under high head pressure '
         'immediately after shut-off. If voltage is reapplied instantly, the compressor motor attempts to start against this locked hydraulic pressure, '
         'drawing locked-rotor current ($I_{\text{LRA}}$), tripping motor overloads, and burning out motor stator windings. '
         'The adjustable <strong>auto-reclosing timer delay ($1\,\text{s}$ to $500\,\text{s}$, typically set to $180\,\text{s}$)</strong> '
         'ensures the protector waits until refrigerant pressures equalize before automatically restoring electricity.'),
        ('What happens if the utility neutral conductor breaks (floating neutral condition)?',
         'A broken neutral line on a three-phase distribution transformer (often caused by storms, poor connections, or copper theft) causes '
         'the neutral point to float. Consequently, phase-to-neutral voltages in single-phase homes become unbalanced: one phase can collapse '
         'to $100\,\text{V}$ while another phase surges to $380\,\text{V}$ or $400\,\text{V}$! '
         'A standard miniature circuit breaker (MCB) will NOT trip during a floating neutral because current draw may still be within nominal limits. '
         'A digital over and under voltage protector senses the $380\,\text{V}$ swell within $< 0.1\,\text{seconds}$ and snaps open, saving connected household appliances, televisions, and electronics from catastrophic fire.')
    ],
    cta='Designing residential consumer units, commercial distribution boards, or municipal housing developments in regions subject to volatile utility voltages or neutral line faults? YOMIN manufactures digital DIN rail self-restoring over and under voltage protectors from 40A to 80A certified to IEC 60947-2.',
    body='''
<h2>The Critical Challenge of Grid Voltage Instability in Distribution Systems</h2>
<p>Electrical equipment and home appliances are engineered to operate within strict voltage tolerances, typically $\pm 10\%$ of nominal utility voltage (e.g., $207\,\text{V}$ to $253\,\text{V}$ for a standard $230\,\text{V}$ grid). Across rapid-growth industrial corridors, rural distribution feeders, and developing utility networks, supply voltages routinely violate these limits:</p>
<ul>
  <li><strong>Voltage Swells and Overvoltage:</strong> Caused by sudden load shedding, capacitor bank switching, or distribution transformer tap mismatches. Sustained overvoltage forces excessive magnetizing current through iron cores, punctures dielectric insulation, and destroys power supply capacitors.</li>
  <li><strong>Voltage Sags and Brownouts:</strong> Caused by overloaded distribution feeders and high-current motor starts. When supply voltage drops, induction motors and refrigeration compressors draw excessive current to satisfy their shaft torque demands, leading to overheating and thermal burnout.</li>
  <li><strong>The Floating Neutral Catastrophe:</strong> When a shared utility three-phase neutral conductor is severed or disconnected, single-phase 230V residential sockets can suddenly see up to $400\,\text{V}$ phase-to-phase voltage, causing widespread appliance destruction and domestic fires.</li>
</ul>
<p>The <strong>DIN rail self-restoring over and under voltage protector</strong> provides an automated, autonomous defense system installed directly inside the consumer distribution board.</p>

<h2>Engineering Architecture: Microcontroller Sensing and Auto-Reclosing Logic</h2>
<table>
  <thead>
    <tr>
      <th>Operational Phase</th>
      <th>Grid Condition & Voltage State</th>
      <th>Protector Internal Action & Response Time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Normal Continuous Operation</strong></td>
      <td>Nominal Voltage: $200\,\text{V} \le U \le 250\,\text{V}$</td>
      <td>Internal latching relay / power contactor remains closed; Green status LED illuminated; Dual displays show live voltage and load current.</td>
    </tr>
    <tr>
      <td><strong>Overvoltage Fault Trip</strong></td>
      <td>$U > U_{\text{max}}$ (Adjustable $230\,\text{V}$ to $300\,\text{V}$)</td>
      <td>Microcontroller detects RMS threshold breach; opens internal power contacts within $< 0.1\,\text{s}$; Red overvoltage LED flashes.</td>
    </tr>
    <tr>
      <td><strong>Undervoltage Fault Trip</strong></td>
      <td>$U < U_{\text{min}}$ (Adjustable $140\,\text{V}$ to $210\,\text{V}$)</td>
      <td>Microcontroller detects brownout condition; opens internal power contacts within $< 0.1\,\text{s}$; Yellow undervoltage LED flashes.</td>
    </tr>
    <tr>
      <td><strong>Post-Fault Normalization</strong></td>
      <td>Voltage returns to safe band ($U_{\text{min}} < U < U_{\text{max}}$)</td>
      <td>Internal digital timer starts countdown ($1\,\text{s}$ to $500\,\text{s}$); display flashes countdown seconds; load remains safely disconnected.</td>
    </tr>
    <tr>
      <td><strong>Automatic Reclosing (Auto-Reset)</strong></td>
      <td>Voltage stable throughout countdown</td>
      <td>Contactor snaps closed automatically; power is restored to downstream branch circuits without manual electrician intervention.</td>
    </tr>
  </tbody>
</table>
'''
)

OUV_FR = dict(
    lang='fr',
    dir='ltr',
    slug='distribution-boards-what-is-an-over-and-under-voltage-protector-fr',
    title='Tableaux de Distribution : Qu\'est-ce qu\'un Protecteur de Surtension et Sous-Tension ?',
    breadcrumb='Tableaux de Distribution &amp; Protecteurs de Tension',
    read='10 min de lecture',
    alt='Intérieur d\'un tableau de distribution résidentiel montrant un protecteur modulaire de surtension et sous-tension avec affichage numérique LED',
    desc=('Tableaux électriques divisionnaires, protection des compresseurs et sécurité des réseaux : Qu\'est-ce qu\'un protecteur de surtension et sous-tension ? '
          'Surveillance numérique de la tension efficace, coupure ultra-rapide (<0,1s) en cas de rupture de neutre ou de baisse de tension, et réenclenchement automatique selon CEI 60947-2.'),
    model='Séries VAP-2P et VAP-3P : Protecteurs Modulaires Numériques de Surtension et Sous-Tension à Réarmement Automatique 40A–63A–80A (Double Affichage LED, Temporisation Réglable, Conformes CEI 60947-2)',
    category='Tableaux de Distribution & Protecteurs de Tension / Dispositifs de Protection Modulaire',
    kw='protecteur surtension sous tension &middot; relais de tension rail din &middot; disjoncteur rearmement automatique &middot; coupure neutre tableau &middot; protection compresseur frigorifique &middot; cei 60947-2',
    specs=[
        ('Tension Assignée d\'Emploi ($U_e$)', 'Tension nominale monophasée $220\,\text{V} / 230\,\text{V AC}$ ou triphasée $380\,\text{V} / 400\,\text{V AC}$ (50Hz/60Hz)'),
        ('Courant Assigné d\'Emploi ($I_e$)', 'Calibres de service continu de $40\,\text{A}$, $63\,\text{A}$ et $80\,\text{A}$ adaptés aux disjoncteurs de tête d\'installation'),
        ('Plage de Déclenchement en Surtension', 'Réglable de $230\,\text{V}$ à $300\,\text{V AC}$ (Défaut : $270\,\text{V}$) ; Temps de déclenchement $< 0,1\,\text{seconde}$'),
        ('Plage de Déclenchement en Sous-Tension', 'Réglable de $140\,\text{V}$ à $210\,\text{V AC}$ (Défaut : $170\,\text{V}$) ; Temps de déclenchement $< 0,1\,\text{seconde}$'),
        ('Temporisation au Réenclenchement', 'Temporisation réglable de $1\,\text{s}$ à $500\,\text{s}$ (Défaut : $30\,\text{s}$) évitant le redémarrage immédiat des moteurs et compresseurs'),
        ('Protection Complémentaire de Surintensité', 'Seuil de courant réglable de $1\,\text{A}$ à $63\,\text{A}$ pour limiter les surcharges thermiques sur l\'installation aval'),
        ('Interface de Mesure et Affichage Numérique', 'Double afficheur numérique LED 7 segments affichant la tension RMS en temps réel (Rouge) et le courant de charge (Vert)'),
        ('Normes Internationales et Conformité', 'Entièrement certifié selon les normes CEI 60947-2, CEI 60898-1 et directives européennes basse tension')
    ],
    faqs=[
        ('Quelle est la différence entre un parafoudre (SPD) et un protecteur de tension (VAP) ?',
         'Le parafoudre (SPD) évacue à la terre les surtensions transitoires de quelques microsecondes (comme la foudre). '
         'Il est incapable d\'agir contre les surtensions permanentes de plusieurs secondes ou les baisses de tension (brownouts). '
         'Le <strong>protecteur de surtension et sous-tension (VAP)</strong> surveille la tension réseau continue : '
         'dès que la tension sort de la plage admissible ou en cas de rupture du neutre, il ouvre son contacteur interne '
         'en moins de 0,1 seconde et réenclenche automatiquement dès retour à la normale.')
    ],
    cta='Vous concevez des tableaux électriques résidentiels ou tertiaires exposés aux instabilités de tension réseau et aux risques de rupture de neutre ? YOMIN fabrique des protecteurs de tension modulaires à réarmement automatique de 40A à 80A conformes à la norme CEI 60947-2.',
    body='''
<h2>La Protection Essentielle des Récepteurs Électriques Contre les Fluctuations du Réseau</h2>
<p>Les équipements modernes (climatiseurs, réfrigérateurs, électronique de puissance) sont conçus pour fonctionner dans une plage de tension étroite (±10%). Sur les réseaux électriques soumis à de fortes charges ou à des aléas climatiques, deux anomalies majeures surviennent fréquemment :</p>
<ul>
  <li><strong>Les chutes de tension (baisse de tension) :</strong> Le moteur électrique tire plus de courant pour maintenir son couple, s\'échauffe et finit par griller son bobinage.</li>
  <li><strong>La rupture de conducteur neutre :</strong> En réseau triphasé, la coupure du neutre déséquilibre les tensions et applique jusqu\'à 400V sur les prises monophasées, provoquant l\'explosion des alimentations.</li>
</ul>
<p>Le <strong>protecteur modulaire rail DIN</strong> isole les charges aval en moins de 0,1 s et assure un réarmement temporisé sans intervention humaine selon la norme <strong>CEI 60947-2</strong>.</p>
'''
)

OUV_ES = dict(
    lang='es',
    dir='ltr',
    slug='distribution-boards-what-is-an-over-and-under-voltage-protector-es',
    title='Cuadros de Distribución: ¿Qué Es un Protector de Sobretensión y Subtensión?',
    breadcrumb='Cuadros de Distribución &amp; Protectores de Tensión',
    read='10 min de lectura',
    alt='Interior de cuadro de distribución eléctrico residencial mostrando un protector modular de sobretensión y subtensión con pantalla digital LED dual',
    desc=('Cuadros eléctricos residenciales, protección de compresores de climatización y seguridad de red: ¿Qué es un protector de sobretensión y subtensión? '
          'Monitorización digital en tiempo real, desconexión ultrarrápida (<0.1s) ante fallos de neutro o caídas de tensión y reconexión automática bajo IEC 60947-2.'),
    model='Series VAP-2P y VAP-3P: Protectores Modulares Digitales de Sobretensión y Subtensión con Reconexión Automática 40A–63A–80A (Doble Pantalla LED, Temporizador Programable, Certificados IEC 60947-2)',
    category='Cuadros de Distribución & Protectores de Tensión / Dispositivos de Protección Modular',
    kw='protector sobretension subtension &middot; rele de tension carril din &middot; protector reenganche automatico &middot; fallo de neutro cuadro &middot; proteccion compresor aire acondicionado &middot; iec 60947-2',
    specs=[
        ('Tensión Asignada de Servicio ($U_e$)', 'Tensión nominal monofásica de $220\,\text{V} / 230\,\text{V AC}$ o trifásica de $380\,\text{V} / 400\,\text{V AC}$ (50Hz/60Hz)'),
        ('Corriente Asignada de Servicio ($I_e$)', 'Capacidad de servicio continuo de $40\,\text{A}$, $63\,\text{A}$ y $80\,\text{A}$ apto para cabecera de cuadro general'),
        ('Umbral de Disparo por Sobretensión', 'Ajustable de $230\,\text{V}$ a $300\,\text{V AC}$ (Por defecto: $270\,\text{V}$) ; Tiempo de disparo $< 0.1\,\text{segundos}$'),
        ('Umbral de Disparo por Subtensión', 'Ajustable de $140\,\text{V}$ a $210\,\text{V AC}$ (Por defecto: $170\,\text{V}$) ; Tiempo de disparo $< 0.1\,\text{segundos}$'),
        ('Temporizador de Reconexión Automática', 'Retardo programable de $1\,\text{s}$ a $500\,\text{s}$ (Por defecto: $30\,\text{s}$) para evitar arranques sucesivos en motores y compresores'),
        ('Límite de Protección de Sobreintensidad', 'Ajuste de corte de intensidad de $1\,\text{A}$ a $63\,\text{A}$ para protección térmica auxiliar de la línea'),
        ('Pantalla Digital de Medición Continua', 'Doble display LED de 3 dígitos que muestra la tensión eficaz en tiempo real (Rojo) y la corriente consumida (Verde)'),
        ('Normativas Internacionales Aplicables', 'Homologado y certificado conforme a las normas IEC 60947-2, IEC 60898-1 y marcado CE')
    ],
    faqs=[
        ('¿Cuál es la diferencia entre un protector contra sobretensiones (DPS) y un protector de tensión (VAP)?',
         'El protector contra sobretensiones (DPS / descargador) deriva a tierra picos transitorios de microsegundos producidos por rayos. '
         'No actúa frente a subidas de tensión continuas de varios segundos ni frente a caídas de tensión (subtensión). '
         'El <strong>protector de sobretensión y subtensión con reconexión automática (VAP)</strong> vigila el voltaje constante: '
         'ante una fluctuación sostenida o rotura del neutro, corta el suministro en menos de 0.1 s y se reconecta de forma '
         'autónoma cuando la red eléctrica se estabiliza.')
    ],
    cta='¿Diseña cuadros eléctricos para viviendas, locales comerciales o instalaciones expuestas a redes eléctricas inestables? YOMIN fabrica protectores de tensión modulares con reenganche automático de 40A a 80A conformes a IEC 60947-2.',
    body='''
<h2>La Protección Definitiva Frente a las Fluctuaciones y Fallos de Neutro en la Red Eléctrica</h2>
<p>Los aparatos electrodomésticos y sistemas de climatización requieren una tensión constante dentro de unos márgenes estrechos. En redes con perturbaciones severas o sobrecargas, se producen dos fallos destructivos:</p>
<ul>
  <li><strong>Subtensiones y caídas de voltaje :</strong> El compresor frigorífico sufre para arrancar, se calienta en exceso y termina quemando su devanado.</li>
  <li><strong>Rotura o desconexión del cable neutro :</strong> El neutro flotante traslada tensiones de hasta 400V a las tomas monofásicas, destruyendo al instante televisores y equipos electrónicos.</li>
</ul>
<p>El <strong>protector modular de carril DIN con reconexión automática</strong> abre el circuito en menos de 0.1 segundos y restablece el servicio automáticamente según la norma <strong>IEC 60947-2</strong>.</p>
'''
)

OUV_AR = dict(
    lang='ar',
    dir='rtl',
    slug='distribution-boards-what-is-an-over-and-under-voltage-protector-ar',
    title='لوحات التوزيع الكهربائية: ما هو جهاز الحماية من ارتفاع وانخفاض الجهد (Over and Under Voltage Protector)؟',
    breadcrumb='لوحات التوزيع &amp; أجهزة الحماية من تغير الجهد',
    read='10 دقائق قراءة',
    alt='لوحة قواطع توزيع كهربائية منزلية توضح جهاز الحماية الرقمي من ارتفاع وانخفاض الجهد المزود بشاشة رقمية مزدوجة مثبت على سكة التثبيت المعدنية',
    desc=('لوحات التوزيع الكهربائية، وحماية ضواغط أجهزة التكييف والتبريد، ومنع أضرار انقطاع سلك التعادل: ما هو جهاز الحماية من ارتفاع وانخفاض الجهد الكهربائي؟ '
          'مراقبة رقمية لحظية لجهد الشبكة، وفصل فائق السرعة في أقل من 0.1 ثانية، وإعادة تشغيل ذاتية مبرمجة طبقاً للمواصفة القياسية الدولية IEC 60947-2.'),
    model='سلاسل VAP-2P و VAP-3P: أجهزة الحماية الرقمية من ارتفاع وانخفاض الجهد ذاتية الإعادة للتشغيل 40A–63A–80A (شاشة رقمية مزدوجة، زمن تأخير مبرمج، معتمدة IEC 60947-2)',
    category='لوحات التوزيع & أجهزة الحماية من تغير الجهد / أجهزة الحماية الكهربائية النمطية',
    kw='جهاز حماية من ارتفاع وانخفاض الجهد &middot; over and under voltage protector &middot; قاطع حماية الجهد &middot; جهاز إعادة التوصيل التلقائي &middot; انقطاع سلك النيوترال &middot; حماية ضواغط التكييف &middot; iec 60947-2',
    specs=[
        ('جهد التشغيل الاسمي المقنن ($U_e$)', 'جهد أحادي الطور $220\,\text{V} / 230\,\text{V AC}$ أو ثلاثي الأطوار $380\,\text{V} / 400\,\text{V AC}$ بتردد 50/60 هرتز'),
        ('تيار التشغيل المستمر المقنن ($I_e$)', 'سعات تيار مستمر قياسية $40\,\text{A}$ و $63\,\text{A}$ و $80\,\text{A}$ متوافقة تماماً مع القواطع الرئيسية للوحات التوزيع'),
        ('نطاق ضبط عتبة ارتفاع الجهد (Overvoltage)', 'قابل للضبط من $230\,\text{V}$ إلى $300\,\text{V}$ (القيمة الافتراضية: $270\,\text{V}$)؛ زمن الفصل أقل من $0.1\,\text{ثانية}$'),
        ('نطاق ضبط عتبة انخفاض الجهد (Undervoltage)', 'قابل للضبط من $140\,\text{V}$ إلى $210\,\text{V}$ (القيمة الافتراضية: $170\,\text{V}$)؛ زمن الفصل أقل من $0.1\,\text{ثانية}$'),
        ('زمن تأخير إعادة التوصيل التلقائي', 'مؤقت مبرمج من $1\,\text{s}$ إلى $500\,\text{s}$ (القيمة الافتراضية: $30\,\text{s}$) لحماية ضواغط التبريد من التلف'),
        ('ضبط الحماية من زيادة التيار (Overcurrent)', 'حد تيار قابل للضبط من $1\,\text{A}$ إلى $63\,\text{A}$ لتوفير حماية إضافية من الأحمال الحرارية الزائدة'),
        ('شاشة القياس الرقمية المزدوجة', 'شاشتان رقميتان بإضاءة واضحة تعرضان الجهد اللحظي الحقيقي (باللون الأحمر) وتيار السحب المباشر (باللون الأخضر)'),
        ('المواصفات والشهادات القياسية الدولية', 'مختبر ومعتمد بالكامل وفق معايير اللجنة الكهروتقنية الدولية IEC 60947-2 و IEC 60898-1 وعلامة CE')
    ],
    faqs=[
        ('ما هو جهاز الحماية من ارتفاع وانخفاض الجهد وما فرقه عن مانع الصواعق (SPD)؟',
         'جهاز الحماية من ارتفاع وانخفاض الجهد (سلسلة VAP) هو قاطع إلكتروني ذكي يراقب جهد الشبكة باستمرار، '
         'ويقوم بفصل التيار فوراً عند تجاوز الجهد للحدود الآمنة. '
         '<strong>الفارق الجوهري بينه وبين مانع الصواعق (SPD):</strong> '
         '<ul>'
         '<li><strong>مانع الصواعق والجهد العابر (SPD):</strong> يقوم بتفريغ النبضات الكهربائية العابرة فائقة القصر (التي تدوم ميكروثانية والناتجة عن الصواعق) إلى الأرض عبر مقاومات الفاريستور. ولا يستطيع مانع الصواعق حماية الأجهزة من الارتفاع المستمر لعدة ثوانٍ أو انخفاض الجهد.</li>'
         '<li><strong>جهاز حماية الجهد (VAP):</strong> يتعامل مع الارتفاعات والانخفاضات المستمرة الناتجة عن اضطرابات الشبكة وانقطاع خط التعادل (سلك النيترال). يقوم بفصل الأحمال في أقل من 0.1 ثانية، ثم يعيد التوصيل تلقائياً بعد استقرار الجهد.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تجهيز لوحات توزيع كهربائية للمباني السكنية أو المنشآت التجارية في مناطق تعاني من تذبذب كهرباء الشبكة أو انقطاع سلك التعادل؟ تصنع يمين (YOMIN) أجهزة الحماية الرقمية ذاتية الإعادة للتشغيل بسعات من 40 إلى 80 أمبير طبقاً للمواصفة IEC 60947-2.',
    body='''
<h2>الأهمية الهندسية القصوى لحماية الأجهزة من تقلبات الجهد الكهربائي واضطرابات الشبكة</h2>
<p>في شبكات التوزيع الكهربائية الحديثة، صممت الأجهزة الكهربائية والمعدات الإلكترونية وضواغط التكييف لتعمل ضمن نطاق جهد تشغيلي محدد بدقة لا يتجاوز 10% صعوداً أو هبوطاً. وتتعرض المنظومات الكهربائية لتحديات متكررة تهدد سلامة المنشآت:</p>
<ul>
  <li><strong>ارتفاع الجهد المفاجئ والمستمر:</strong> يؤدي إلى انهيار العوازل الكهربائية وتلف المكثفات واحتراق اللوحات الإلكترونية الحساسة.</li>
  <li><strong>انخفاض الجهد الكهربائي (Brownout):</strong> يدفع المحركات الكهربائية وضواغط التبريد لسحب تيارات كهربائية عالية جداً لتعويض انخفاض الجهد، مما يؤدي إلى ارتفاع حرارتها واحتراق ملفاتها الداخلية.</li>
  <li><strong>كارثة انقطاع سلك التعادل (النيوترال):</strong> يؤدي انقطاع خط التعادل المشترك في الأنظمة ثلاثية الأطوار إلى ارتفاع الجهد في بعض الدوائر الأحادية ليصل إلى 400 فولت فجأة، مما يسبب احتراقاً فورياً لكافة الأجهزة المنزلية المتصلة واشتعال الحرائق.</li>
</ul>
<p>يقوم <strong>جهاز الحماية الرقمي من ارتفاع وانخفاض الجهد المخصص للتركيب على سكة التثبيت القياسية</strong> بمراقبة الجهد بصورة لحظية وفصل الدائرة في زمن قياسي يقل عن 0.1 ثانية، ثم إعادة التوصيل التلقائي بعد استقرار الشبكة وفقاً لمعايير <strong>IEC 60947-2</strong>.</p>
'''
)

# ==============================================================================
# 2. POWER DISTRIBUTION BLOCK (EN, FR, ES, AR)
# ==============================================================================

PDB_EN = dict(
    lang='en',
    dir='ltr',
    slug='control-panels-what-is-a-power-distribution-block',
    title='Control Panels: What Is a Power Distribution Block?',
    breadcrumb='Control Panels &amp; Power Distribution Blocks',
    read='10 min read',
    alt='Industrial electrical control panel interior showing modular DIN rail unipolar power distribution blocks splitting a heavy main copper feeder into multiple branch circuit wires',
    desc=('Industrial automation control panels, switchgear assemblies, and solar combiner boxes: What is a power distribution block? '
          'How modular unipolar distribution blocks (UKK series) split heavy primary feeder cables into multiple branch circuits, eliminate hazardous terminal daisy-chaining, '
          'provide IP20 finger-safe touch protection, and deliver high short-circuit current ratings (SCCR) under IEC 60947-7-1 and UL 1059.'),
    model='Model UKK-80A, UKK-125A, UKK-160A, UKK-250A, UKK-400A, UKK-500A & FJ6 Series Modular DIN Rail Unipolar Power Distribution Blocks (Tinned Brass Conductor, PA66 Flame-Retardant Housing, IP20 Touch-Proof Cover, Rated 690V/1000V AC/DC, Tested to IEC 60947-7-1 & UL 1059)',
    category='Control Panels & Power Distribution Blocks / Terminal Blocks & Connectors',
    kw='what is a power distribution block &middot; power distribution block &middot; din rail power distribution block &middot; unipolar distribution block &middot; ukk distribution block &middot; terminal block distribution &middot; iec 60947-7-1',
    specs=[
        ('Rated Insulation Voltage ($U_i$)', 'Standard ratings of $690\,\text{V AC}$ and $1000\,\text{V AC/DC}$ suitable for industrial switchgear and solar PV DC combiner boxes'),
        ('Rated Current Capacity ($I_n$)', 'Standard modular models rated for $80\,\text{A}$, $125\,\text{A}$, $160\,\text{A}$, $250\,\text{A}$, $400\,\text{A}$, and $500\,\text{A}$ continuous load'),
        ('Internal Conductor Block Material', 'High-conductivity forged solid brass ($Cu \ge 58\text{--}60\%$) with electrolytic matte tin electroplating to prevent copper oxidation'),
        ('Insulating Housing Material', 'Halogen-free, self-extinguishing polyamide (PA66) certified flammability rating **UL 94V-0** with high tracking resistance (CTI 600)'),
        ('Ingress & Touch Safety Rating', 'Integrated transparent blue hinged cover providing certified **IP20 finger-safe touch protection** under IEC 60529'),
        ('Primary Incoming Wire Range', 'Accommodates single heavy incoming copper/aluminum feeder cables from $16\,\text{mm}^2$ up to $185\,\text{mm}^2$ (AWG 6 to 350 kcmil)'),
        ('Secondary Outgoing Branch Ports', 'Engineered with $4, 6, 8, \text{or } 12$ precision tunnel exit ports accepting branch wiring from $2.5\,\text{mm}^2$ up to $35\,\text{mm}^2$'),
        ('Mounting Versatility & Standards', 'Dual-mounting capability: Standard $35\,\text{mm}$ DIN rail snap-on mounting (EN 50022) or direct panel backplate screw mounting; Certified IEC 60947-7-1 & UL 1059')
    ],
    faqs=[
        ('What is a power distribution block and why is it used instead of daisy-chain terminal wiring?',
         'A power distribution block (PDB, often termed a unipolar distribution block or modular feeder splitter) is an engineered electrical '
         'terminal device designed to receive a single large incoming power feeder conductor and split it into multiple smaller outgoing branch circuit conductors. '
         '<strong>Why daisy-chaining terminals is dangerous:</strong> '
         '<ul>'
         '<li><strong>Thermal Overloading:</strong> Jamming two or three wires into a single circuit breaker or standard terminal clamp creates uneven mechanical pressure, leading to loose strands, localized hotspots, and electrical arcing.</li>'
         '<li><strong>Code Violations:</strong> Most electrical installation codes (such as NEC Article 110.14 and IEC 61439-1) strictly prohibit terminating multiple conductors into a terminal lug unless specifically tested and rated for multi-wire use.</li>'
         '<li><strong>Space and Aesthetics:</strong> Daisy-chaining creates a chaotic "bird\'s nest" of jumpers inside the wire ducting, impeding airflow and complicating troubleshooting.</li>'
         '</ul>'
         'A dedicated distribution block provides a compact, centralized, and certified splitting point with zero wire crowding.'),
        ('How does a power distribution block achieve IP20 finger-safe protection?',
         'Under IEC 60529, an IP20 rating certifies that live hazardous electrical parts cannot be touched by a standardized test finger '
         '($12.5\,\text{mm}$ diameter probe). '
         'YOMIN\'s UKK series power distribution blocks feature a fully enclosed insulating polyamide body and a transparent polycarbonate hinged top cover. '
         'All screw access ports and wire entry funnels are deeply recessed. Panel assembly technicians and maintenance engineers can inspect wire '
         'terminations and torque screws safely without accidental contact with live 1000V electrical conductors.'),
        ('Can power distribution blocks be used for DC voltages in solar photovoltaic systems and energy storage (BESS)?',
         'Yes. High-quality power distribution blocks manufactured with tinned brass conductors and UL 94V-0 polyamide housings are rated for '
         'both $690\,\text{V AC}$ and $1000\,\text{V DC}$. In solar combiner boxes and battery energy storage system (BESS) racks, UKK distribution blocks '
         'are widely used to parallel multiple positive or negative DC string inputs before feeding the main DC isolation switch or inverter input, '
         'providing robust, corrosion-resistant current sharing.')
    ],
    cta='Designing industrial automation control panels, motor control centers (MCC), or commercial solar combiner boxes requiring compact, finger-safe DIN rail power distribution blocks from 80A to 500A? YOMIN manufactures modular UKK series distribution blocks tested to IEC 60947-7-1 and UL 1059.',
    body='''
<h2>Streamlining Power Distribution Inside Industrial Electrical Enclosures</h2>
<p>Inside electrical control panels, switchgear cubicles, and machinery power distribution units, power distribution is an everyday engineering requirement: a primary electrical supply (for example, a 160A or 250A feeder cable entering from the main disconnect switch) must be subdivided into branch circuits feeding multiple variable frequency drives (VFDs), motor starters, miniature circuit breakers, and auxiliary power supplies.</p>
<p>Historically, panel builders relied on custom copper busbar fabrications or hazardous terminal jumper bars. Today, the <strong>modular DIN rail power distribution block (UKK Series)</strong> has become the international industry standard for clean, safe, and code-compliant power distribution.</p>

<h2>Engineering Advantages of Modular Unipolar Distribution Blocks</h2>
<ul>
  <li><strong>High Current Carrying Efficiency:</strong> The solid tinned brass conductor block provides an exceptionally low-resistance current path, ensuring minimal voltage drop and low operational temperature rise during continuous full-load operation.</li>
  <li><strong>Universal Conductor Compatibility:</strong> Each tunnel terminal accommodates solid, stranded, or fine-stranded flexible copper conductors fitted with bootlace ferrules. Precision hex-socket set screws deliver uniform clamping pressure without severing fragile conductor strands.</li>
  <li><strong>Modular Gangability:</strong> UKK blocks can be mounted individually or interlocked side-by-side on a standard 35mm DIN rail to create multi-phase power distribution assemblies (3-Phase 3-Wire, 3-Phase 4-Wire, or DC positive/negative pairs) with minimal footprint.</li>
  <li><strong>High Short-Circuit Withstand Capability (SCCR):</strong> High mechanical strength PA66 housing and robust internal geometry prevent catastrophic terminal rupture during downstream short-circuit faults.</li>
</ul>
'''
)

PDB_FR = dict(
    lang='fr',
    dir='ltr',
    slug='control-panels-what-is-a-power-distribution-block-fr',
    title='Armoires Électriques : Qu\'est-ce qu\'un Bloc de Distribution de Puissance ?',
    breadcrumb='Armoires Électriques &amp; Blocs de Distribution',
    read='10 min de lecture',
    alt='Intérieur d\'armoire d\'automatisme industriel montrant des répartiteurs modulaires unipolaires rail DIN divisant un câble principal vers plusieurs départs',
    desc=('Armoires d\'automatismes industriels, tableaux de distribution et coffrets solaires : Qu\'est-ce qu\'un bloc de distribution de puissance (répartiteur modulaire) ? '
          'Division propre d\'une grosse alimentation vers plusieurs départs, suppression des pontages dangereux, protection tactile IP20 et conformité CEI 60947-7-1.'),
    model='Séries UKK-80A à UKK-500A et FJ6 : Blocs Répartiteurs Modulaires Unipolaires Rail DIN (Conducteur Laiton Étamé, Boîtier PA66 Auto-extinguible, Capot Transparent IP20, Tension 690V/1000V, Conformes CEI 60947-7-1)',
    category='Armoires Électriques & Blocs de Distribution / Borniers & Connectique Électrique',
    kw='bloc de distribution de puissance &middot; repartiteur modulaire rail din &middot; bornier repartiteur unipolaire &middot; repartiteur ukk &middot; division cable armoire electrique &middot; cei 60947-7-1',
    specs=[
        ('Tension Assignée d\'Isolement ($U_i$)', 'Tension nominale de $690\,\text{V AC}$ et $1000\,\text{V AC/DC}$ adaptée aux armoires industrielles et coffrets solaires'),
        ('Courant Assigné d\'Emploi ($I_n$)', 'Gamme modulaire de $80\,\text{A}$, $125\,\text{A}$, $160\,\text{A}$, $250\,\text{A}$, $400\,\text{A}$ et $500\,\text{A}$ en charge continue'),
        ('Matériau du Bloc Conducteur Interne', 'Laiton massif forgé haute conductivité avec étamage électrolytique mat anticorrosion'),
        ('Matériau Isolant de l\'Enveloppe', 'Polyamide (PA66) sans halogène, auto-extinguible classé **UL 94V-0** à haute tenue au cheminement (CTI 600)'),
        ('Degré de Protection Tactile', 'Capot transparent articulé offrant une protection certifiée **IP20 contre les contacts directs** selon CEI 60529'),
        ('Section du Conducteur d\'Entrée Principal', 'Accepte les câbles d\'alimentation en cuivre ou aluminium de $16\,\text{mm}^2$ à $185\,\text{mm}^2$'),
        ('Nombre et Sections des Départs Secondaires', 'Conçu avec $4, 6, 8 \text{ ou } 12$ tunnels de sortie recevant des câbles de départs de $2,5\,\text{mm}^2$ à $35\,\text{mm}^2$'),
        ('Modes de Fixation et Normes', 'Double fixation : Clipsable sur rail DIN normalisé $35\,\text{mm}$ ou vissable directement sur platine ; Certifié CEI 60947-7-1')
    ],
    faqs=[
        ('Pourquoi utiliser un bloc de répartition plutôt que de doubler les câbles sous les bornes ?',
         'Le serrage de deux câbles sous une même borne de disjoncteur est formellement interdit par les normes d\'installation électrique : '
         'les pressions mécaniques inégales provoquent des desserrages, des échauffements par effet Joule et des incendies. '
         'Le <strong>répartiteur modulaire unipolaire (série UKK)</strong> assure une répartition centralisée, équilibrée '
         'et parfaitement sécurisée dans un encombrement minimal.')
    ],
    cta='Vous assemblez des armoires de contrôle-commande, des centres de contrôle moteurs (MCC) ou des coffrets solaires nécessitant des blocs répartiteurs modulaires rail DIN certifiés CEI 60947-7-1 ? YOMIN fabrique la gamme complète UKK de 80A à 500A.',
    body='''
<h2>Optimisation et Sécurisation du Câblage dans les Tableaux Électriques Industriels</h2>
<p>Dans la construction de tableaux et armoires d\'automatisme, il est constamment nécessaire de subdiviser une arrivée de puissance principale (par exemple un câble d\'alimentation de 50 mm² ou 120 mm²) vers de multiples départs divisionnaires (variateurs, départs-moteurs, alimentations auxiliaires).</p>
<p>Le <strong>répartiteur modulaire unipolaire pour rail DIN (série UKK)</strong> remplace avantageusement les jeux de barres encombrants et supprime les pontages hasardeux grâce à sa conception compacte et étamée conforme à la norme <strong>CEI 60947-7-1</strong>.</p>
'''
)

PDB_ES = dict(
    lang='es',
    dir='ltr',
    slug='control-panels-what-is-a-power-distribution-block-es',
    title='Cuadros de Control: ¿Qué Es un Bloque Distribuidor de Potencia?',
    breadcrumb='Cuadros de Control &amp; Distribuidores de Potencia',
    read='10 min de lectura',
    alt='Interior de cuadro de automatización industrial mostrando bloques distribuidores modulares de potencia para carril DIN dividiendo un cable principal',
    desc=('Cuadros de automatización industrial, aparamenta eléctrica y cajas de conexión solar: ¿Qué es un bloque distribuidor de potencia (repartidor modular)? '
          'Derivación limpia de cables principales hacia múltiples salidas, eliminación de puentes inseguros, protección táctil IP20 y norma IEC 60947-7-1.'),
    model='Series UKK-80A a UKK-500A y FJ6: Bloques Distribuidores Modulares Unipolares para Carril DIN (Conductor de Latón Estañado, Cuerpo PA66 Autoextinguible, Tapa IP20 Transparente, Tensión 690V/1000V, Certificados IEC 60947-7-1)',
    category='Cuadros de Control & Distribuidores de Potencia / Bornas y Conectores de Cuadro',
    kw='bloque distribuidor de potencia &middot; repartidor modular carril din &middot; bloque distribucion unipolar &middot; repartidor ukk &middot; derivacion cable cuadro electrico &middot; iec 60947-7-1',
    specs=[
        ('Tensión Asignada de Aislamiento ($U_i$)', 'Tensión nominal de $690\,\text{V AC}$ y $1000\,\text{V AC/DC}$ adecuada para cuadros industriales y fotovoltaica'),
        ('Capacidad de Corriente Nominal ($I_n$)', 'Gama modular con intensidades nominales de $80\,\text{A}$, $125\,\text{A}$, $160\,\text{A}$, $250\,\text{A}$, $400\,\text{A}$ y $500\,\text{A}$'),
        ('Material del Bloque Conductor Interno', 'Latón macizo forjado de alta conductividad con baño electrolítico de estaño mate anticorrosión'),
        ('Material Aislante de la Carcasa', 'Poliamida (PA66) libre de halógenos, autoextinguible clasificada **UL 94V-0** con alto índice CTI 600'),
        ('Grado de Protección Contra Contacto', 'Tapa abatible de policarbonato transparente con protección certificada **IP20 a prueba de dedos** según IEC 60529'),
        ('Capacidad del Cable de Entrada Principal', 'Admite conductores principales de cobre o aluminio desde $16\,\text{mm}^2$ hasta $185\,\text{mm}^2$'),
        ('Puertos y Secciones de Salidas Secundarias', 'Equipado con $4, 6, 8 \text{ o } 12$ túneles de salida para cableado de distribución desde $2.5\,\text{mm}^2$ hasta $35\,\text{mm}^2$'),
        ('Opciones de Montaje y Cumplimiento', 'Montaje rápido sobre carril DIN simétrico de $35\,\text{mm}$ o fijación directa por tornillo a placa de montaje ; Certificado IEC 60947-7-1')
    ],
    faqs=[
        ('¿Por qué no se deben puentear varios cables en un mismo borne en lugar de usar un repartidor?',
         'Embornar dos o más cables en una misma borna de interruptor está prohibido por los reglamentos electrotécnicos : '
         'la presión desigual provoca que los hilos finos se suelten, generando puntos calientes por resistencia de contacto y fuego. '
         'Un <strong>bloque distribuidor unipolar (serie UKK)</strong> proporciona una división centralizada, limpia y segura '
         'con apriete individual para cada circuito derivado.')
    ],
    cta='¿Fabrica armarios de control industrial, centros de control de motores o cuadros de combinación solar que precisan bloques distribuidores de potencia homologados bajo IEC 60947-7-1? YOMIN suministra repartidores modulares UKK de 80A a 500A.',
    body='''
<h2>Distribución Eficiente y Segura de Energía en Cuadros de Automatización</h2>
<p>En el montaje de cuadros eléctricos y armarios de control industrial, la derivación de líneas principales hacia múltiples cargas secundarias (variadores de frecuencia, arrancadores y protecciones auxiliares) requiere soluciones limpias y fiables.</p>
<p>El <strong>bloque distribuidor modular para carril DIN (serie UKK)</strong> sustituye a las barras de cobre desnudas y a los puentes improvisados, garantizando una conexión segura con protección IP20 conforme a la norma <strong>IEC 60947-7-1</strong>.</p>
'''
)

PDB_AR = dict(
    lang='ar',
    dir='rtl',
    slug='control-panels-what-is-a-power-distribution-block-ar',
    title='لوحات التحكم والتوزيع: ما هي كتل توزيع القدرة الكهربائية (Power Distribution Block)؟',
    breadcrumb='لوحات التحكم &amp; كتل توزيع القدرة الكهربائية',
    read='10 دقائق قراءة',
    alt='لوحة تحكم صناعية داخلية توضح كتل توزيع القدرة الكهربائية النمطية المركبة على سكة التثبيت المعدنية لتقسيم كابل التغذية الرئيسي',
    desc=('لوحات التحكم الآلي الصناعية، ومراكز التحكم بالمحركات، وصناديق تجميع الطاقة الشمسية: ما هي كتل توزيع القدرة الكهربائية (موزعات الكابلات النمطية)؟ '
          'تقسيم كابلات التغذية الرئيسية الضخمة إلى فروع متعددة بأمان تام، وإلغاء التوصيل العشوائي، وتوفير حماية كاملة من اللمس المباشر IP20 وفقاً لـ IEC 60947-7-1.'),
    model='سلاسل UKK-80A إلى UKK-500A و FJ6: كتل توزيع القدرة الكهربائية النمطية أحادية القطب لسكة التثبيت (نحاس أصفر مطلي بالقصدير، غلاف PA66 مقاوم للاشتعال، غطاء شفاف IP20، جهد 690V/1000V، معتمدة IEC 60947-7-1)',
    category='لوحات التحكم & كتل توزيع القدرة الكهربائية / كتل التوصيل ونقاط التوزيع الكهربائية',
    kw='كتل توزيع القدرة الكهربائية &middot; power distribution block &middot; موزع كابلات لوحة التحكم &middot; موزع نمطي ukk &middot; تفريع كابلات التغذية &middot; حماية اللمس ip20 &middot; iec 60947-7-1',
    specs=[
        ('جهد العزل الاسمي المقنن ($U_i$)', 'جهود تشغيل معتمدة $690\,\text{V AC}$ و $1000\,\text{V AC/DC}$ مناسبة للوحات التوزيع الصناعية وصناديق الطاقة الشمسية'),
        ('سعة تيار الحمل المستمر المقنن ($I_n$)', 'تشكيلة قياسية بسعات تيار $80\,\text{A}$ و $125\,\text{A}$ و $160\,\text{A}$ و $250\,\text{A}$ و $400\,\text{A}$ و $500\,\text{A}$'),
        ('مادة كتلة التوصيل الداخلي', 'نحاس أصفر مصمت عالي التوصيل مطلي بطبقة كهرلية متينة من القصدير النقي لمنع الأكسدة وتقليل المقاومة'),
        ('المادة العازلة للهيكل الخارجي', 'بولي أميد (PA66) ذاتي الإطفاء خالي من الهالوجين ومصنف **UL 94V-0** لمقاومة درجات الحرارة والاشتعال'),
        ('مستوى الحماية والأمان من اللمس', 'غطاء علوي مفصلي شفاف من البولي كربونات يوفر حماية معتمدة **IP20 ضد اللمس المباشر بالأصابع** وفق معيار IEC 60529'),
        ('نطاق كابل التغذية الرئيسي الداخلي', 'يستقبل كابل تغذية نحاسي أو ألومنيوم ضخم من مقطع $16\,\text{mm}^2$ وحتى $185\,\text{mm}^2$ عبر نقطة ربط ميكانيكية محكمة'),
        ('منافذ ومقاطع الفروع الثانوية الخارجة', 'مصمم بعدد $4$ أو $6$ أو $8$ أو $12$ منفذ خروج لتوزيع خطوط الفروع بمقاطع من $2.5\,\text{mm}^2$ وحتى $35\,\text{mm}^2$'),
        ('طرق التثبيت والمعايير المعتمدة', 'تثبيت سريع ومزدوج: تعشيق مباشر على سكة DIN النمطية $35\,\text{mm}$ أو تثبيت مباشر بمسامير على اللوح المعدني؛ معتمد IEC 60947-7-1')
    ],
    faqs=[
        ('لماذا تعتبر كتل توزيع القدرة الكهربائية أفضل وأأمن من التوصيل العشوائي للكابلات داخل اللوحة؟',
         'إن محاولة حشر كابلين أو أكثر داخل فتحة قاطع تيار واحدة أو عمل توصيلات متتالية عشوائية تؤدي إلى تخلخل الأسلاك وارتفاع مقاومة التلامس واحتراق اللوحة. '
         'تقوم <strong>كتل توزيع القدرة الكهربائية النمطية (طراز UKK)</strong> بتوفير نقطة تفريع مركزية معزولة ومحمية بغطاء شفاف، '
         'مما يتيح تقسيم كابل المغذي الرئيسي بكفاءة متناهية وأمان ميكانيكي وكهربائي كامل.')
    ],
    cta='هل تعمل على تصنيع لوحات التحكم الآلي، أو مراكز تشغيل المحركات (MCC)، أو صناديق تجميع الألواح الشمسية التي تتطلب كتل توزيع قدرة معتمدة بمعيار IP20 طبقاً للمواصفة IEC 60947-7-1؟ تصنع يمين (YOMIN) عائلة موزعات UKK المتطورة بسعات من 80A إلى 500A.',
    body='''
<h2>تنظيم وتأمين توزيع القدرة الكهربائية داخل لوحات التحكم الصناعية</h2>
<p>في تصنيع لوحات التحكم والتشغيل الآلي ومراكز توزيع القدرة، يواجه مهندسو الكهرباء متطلباً رئيسياً مستمراً: الحاجة إلى تفريع كابل تغذية رئيسي ضخم قادم من القاطع الرئيسي (مثلاً كابل بمقطع 50 مم² أو 120 مم²) لتغذية عدة دوائر فرعية مثل مغيرات السرعة وقواطع المحركات ومصادر التغذية المساعدة.</p>
<p>توفر <strong>كتل توزيع القدرة الكهربائية النمطية أحادية القطب (سلسلة UKK)</strong> حلاً هندسياً فائق التطور يغني عن استخدام قضبان النحاس المكشوفة، مع ضمان سلامة الفنيين بفضل الحماية من اللمس المباشر IP20 والمطابقة للمواصفة القياسية الدولية <strong>IEC 60947-7-1</strong>.</p>
'''
)

ALL_MULTILINGUAL_POSTS_1022 = [
    OUV_EN, OUV_FR, OUV_ES, OUV_AR,
    PDB_EN, PDB_FR, PDB_ES, PDB_AR
]
