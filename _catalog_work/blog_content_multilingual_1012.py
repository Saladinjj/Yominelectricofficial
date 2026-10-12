# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-12:
1. Detuned Harmonic Filter Reactors for Power Factor Correction Banks (EN, FR, ES, AR)
2. Composite Suspension Long-Rod Insulators for High-Voltage Transmission Lines (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. DETUNED REACTOR (EN, FR, ES, AR)
# ==============================================================================

DTR_EN = dict(
    lang='en',
    dir='ltr',
    slug='harmonic-mitigation-what-is-a-detuned-reactor',
    title='Harmonic Mitigation & APFC: What Is a Detuned Reactor?',
    breadcrumb='Power Quality &amp; Harmonic Filters',
    read='10 min read',
    alt='Three-phase dry-type iron-core Detuned Series Filter Reactor (Model CKSG series, 7% detuning) with laminated silicon steel core installed in an automatic power factor correction panel',
    desc=('Industrial power quality, APFC capacitor banks, and harmonic resonance protection: What is a detuned reactor? '
          'How 7% (189Hz) and 14% (134Hz) detuning factors, grain-oriented silicon steel cores with air-gap spacers, Class H copper windings, and IEC 60076-6 standards protect capacitors from harmonic overcurrents.'),
    model='Model CKSG Series 3-Phase Low-Voltage Dry-Type Iron-Core Detuned Series Filter Reactors (0.4kV / 0.45kV / 0.525kV, 7% & 14%, 10 to 100 kvar, IEC 60076-6)',
    category='Power Quality & Harmonic Filters / Detuned Series Reactors',
    kw='what is a detuned reactor &middot; detuned reactor &middot; harmonic filter reactor &middot; series reactor for capacitor &middot; 7 percent detuned reactor &middot; cksg reactor',
    specs=[
        ('Rated System Operating Voltage Class', 'Low-voltage utility ratings: 400V, 440V, 480V, 525V, up to 690V AC 3-Phase (50/60 Hz)'),
        ('Standard Detuning Factors & Frequencies', 'p = 7% ($f_r = 189$ Hz at 50Hz, blocking 5th & 7th harmonics) and p = 14% ($f_r = 134$ Hz, blocking 3rd harmonic)'),
        ('Matching Capacitor Bank Output Sizing', 'Calibrated for standard APFC steps from 10 kvar, 15 kvar, 20 kvar, 25 kvar, 30 kvar, 50 kvar, up to 100 kvar'),
        ('Magnetic Core Material & Air-Gap Design', 'Low-loss grain-oriented cold-rolled silicon steel sheet laminations with multi-section precision ceramic air-gap spacers'),
        ('Winding Conductor & Thermal Insulation', 'High-purity electrolytic copper (or aluminium) foil/wire windings with Class H (180&deg;C) or Class C (200&deg;C) insulation'),
        ('Impregnation & Environmental Sealing', 'Vacuum pressure impregnated (VPI) with solventless polymerizing epoxy resin for minimal acoustic hum (< 45–55 dB)'),
        ('Linearity Threshold & Current Saturation', 'High saturation linearity: Inductance $L$ remains &ge; 0.95 $L_n$ up to 1.80–2.00 times rated nominal current ($I_{lin} \ge 1.80 I_n$)'),
        ('Thermal Protection & Built-in Sensor', 'Integrated micro-thermostat temperature sensor switch (NC, 125&deg;C–140&deg;C) embedded in the central phase coil winding')
    ],
    faqs=[
        ('What is a Detuned Reactor and why must it be connected in series with power capacitors in APFC banks?',
         'A Detuned Reactor—frequently designated as a harmonic filter reactor, series detuning choke, or capacitor protection reactor—is '
         'a specialized three-phase iron-core inductor connected in series with each power capacitor step in an automatic power factor correction (APFC) bank. '
         'In modern industrial manufacturing facilities, commercial data centers, and hospitals: '
         '<ul>'
         '<li><strong>The Parallel Resonance Catastrophe:</strong> Modern facilities are packed with non-linear electrical loads: Variable Frequency Drives (VFDs), '
         'UPS systems, DC rectifiers, and solar PV inverters. These devices inject severe harmonic distortion currents—primarily the <strong>5th harmonic (250Hz) '
         'and 7th harmonic (350Hz)</strong>. When standard un-choked power capacitors are switched onto the bus, their capacitive reactance ($X_C = 1/2\pi fC$) '
         'decreases as frequency rises, while upstream transformer inductive reactance ($X_L = 2\pi fL$) increases. At some frequency, $X_C = X_L$, creating '
         'a <strong>parallel resonant tank circuit</strong>. Harmonic currents are magnified by 300% to 500%, causing capacitor bulging, blown fuses, breaker tripping, and transformer burnout.</li>'
         '<li><strong>The Detuned Reactor Solution:</strong> By connecting an inductor in series with the capacitor, the combination forms a series LC branch. '
         'The reactor\'s inductance is mathematically chosen so that the circuit\'s natural resonant frequency ($f_r$) is tuned <strong>well below the lowest prevalent harmonic</strong> '
         '(e.g., 189Hz for a 7% reactor, safely below 250Hz). Below 189Hz (at fundamental 50Hz/60Hz), the branch remains capacitive and improves power factor. '
         'At and above 250Hz, the branch behaves inductively ($X_L > X_C$), making parallel resonance physically impossible and shielding capacitors from harmonic overloads.</li>'
         '</ul>'),
        ('How do electrical engineers choose between a 7% (189Hz) and a 14% (134Hz) detuned reactor?',
         'The choice between detuning factors depends strictly on the harmonic spectrum present on the facility\'s electrical distribution bus: '
         '<ul>'
         '<li><strong>7% Detuned Reactor ($p = 7\%$, $f_r = 189$ Hz at 50Hz / 227 Hz at 60Hz):</strong> The global industry standard for 3-phase commercial and industrial '
         'facilities where non-linear loads are primarily 6-pulse converters (VFDs, AC drives, pumps, fans) producing 5th (250Hz) and 7th (350Hz) harmonics. '
         'It safely suppresses 5th harmonic resonance while maintaining high power factor correction efficiency.</li>'
         '<li><strong>14% Detuned Reactor ($p = 14\%$, $f_r = 134$ Hz at 50Hz / 160 Hz at 60Hz):</strong> Required when the distribution network contains significant '
         'single-phase non-linear loads (LED driver lighting, computers, switched-mode power supplies) producing heavy <strong>3rd harmonic (150Hz / 180Hz)</strong> currents, '
         'or in networks with high audio-frequency utility ripple control signals. Tuning down to 134Hz ensures the branch remains inductive even at the 3rd harmonic.</li>'
         '</ul>'),
        ('Why do power capacitors experience higher operating voltage when connected in series with a detuned reactor?',
         'Connecting an inductive reactor in series with a capacitor causes a physical voltage rise across the capacitor terminals according to the formula: '
         '$$U_C = \frac{U_N}{1 - p}$$ '
         'For example, on a standard 400V grid ($U_N = 400$V) with a 7% detuned reactor ($p = 0.07$): '
         '$$U_C = \frac{400\text{V}}{1 - 0.07} = \frac{400\text{V}}{0.93} \approx 430\text{V}$$ '
         'If standard 400V-rated capacitors are installed, they will operate in continuous overvoltage and fail within months. '
         'Therefore, engineers must always select up-rated capacitors—specifically <strong>440V, 480V, or 525V rated capacitors</strong>—when pairing with 7% or 14% detuned reactors.')
    ],
    cta='Designing automatic power factor correction (APFC) panels, detuned harmonic filter banks, or industrial capacitor protection systems requiring certified IEC 60076-6 dry-type iron-core detuned reactors (10 to 100 kvar, 7% & 14%)? YOMIN manufactures precision-engineered CKSG series series reactors.',
    body='''
<h2>The Critical Defense Against Harmonic Resonance in Modern Industrial Power Networks</h2>
<p>In modern industrial manufacturing plants, commercial high-rise towers, and automated distribution substations, the rapid proliferation of non-linear power electronic equipment—such as variable speed drives (VFDs), solar inverters, battery storage converters, DC rectifiers, and LED lighting drivers—has radically altered the nature of alternating current power grids.</p>
<p>While these power electronics provide unprecedented motor speed control and energy efficiency, their rapid solid-state switching draws distorted non-sinusoidal currents, injecting massive harmonic pollution (primarily the 5th, 7th, 11th, and 13th harmonic currents) back into the electrical distribution bus.</p>
<p>When plant managers install traditional power factor correction capacitor banks to eliminate low power factor utility penalty fees, an unforeseen catastrophe frequently strikes: the capacitive reactance of the capacitor bank interacts with the inductive reactance of the main supply transformer, creating a <strong>parallel resonant circuit</strong>.</p>
<p>At the resonant frequency, harmonic currents are amplified by 300% to 500%. This dramatic overcurrent leads to capacitor bulging, ruptured dielectric cans, blown high-rupturing-capacity (HRC) fuses, nuisance circuit breaker tripping, and destructive overheating of distribution transformers.</p>
<p>The <strong>Dry-Type Iron-Core Detuned Series Filter Reactor (Model CKSG Series)</strong> represents the essential, non-negotiable solution: a precision-engineered three-phase inductor connected in series with each capacitor step to alter the circuit resonance point, blocking harmonic amplification and ensuring decades of trouble-free capacitor operation.</p>

<h2>Engineering Anatomy: Inside a Model CKSG Detuned Iron-Core Series Reactor</h2>
<ol>
  <li><strong>Multi-Section Silicon Steel Core with Ceramic Air Gaps:</strong> Assembled from high-grade, cold-rolled grain-oriented low-loss silicon steel laminations ($< 1.0$ W/kg). Multiple discrete air gaps spaced with high-temperature ceramic insulators prevent magnetic saturation during severe harmonic overcurrent conditions.</li>
  <li><strong>Class H Electrolytic Copper Windings:</strong> Precision-wound using electrolytic copper foil or heavy enameled rectangular wire with Class H (180&deg;C) thermal insulation, providing exceptional thermal dissipation and withstanding continuous harmonic current overloads.</li>
  <li><strong>Vacuum Pressure Impregnation (VPI):</strong> The entire core and coil assembly undergoes high-vacuum pressure impregnation using solvent-free polymerizing epoxy resin, cured in high-temperature ovens. This eliminates micro-vibrations, resists moisture, and ensures whisper-quiet acoustic noise levels ($< 50$ dB).</li>
  <li><strong>Linearity Under Overcurrent ($I_{lin} \ge 1.80 I_n$):</strong> High saturation linearity guarantees that inductance ($L$) remains strictly constant ($> 95\%$) even when subjected to inrush currents and harmonic distortion spikes reaching nearly double the rated nominal current.</li>
  <li><strong>Embedded Thermal Protection Sensor:</strong> A normally closed (NC) bimetallic micro-thermostat is factory-embedded directly within the central phase coil winding. If winding temperatures exceed 125&deg;C, it trips the APFC controller step contactor to safely de-energize the stage.</li>
</ol>

<h2>Comparison: Standard Unprotected Capacitor Bank vs. Detuned Filter Reactor Capacitor Bank (CKSG Series)</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Standard Unprotected Capacitor Bank</th>
      <th>YOMIN Detuned Filter Capacitor Bank (CKSG Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Susceptibility to Harmonic Parallel Resonance</strong></td>
      <td>Extreme: High risk of resonant amplification ($3\times$ to $5\times$) with 5th and 7th harmonics.</td>
      <td><strong>Zero Resonance: Resonance frequency shifted below 189Hz (for 7%) where no harmonics exist.</strong></td>
    </tr>
    <tr>
      <td><strong>Capacitor Lifespan &amp; Failure Rates</strong></td>
      <td>Severely shortened (often 1–3 years); frequent capacitor bulging, oil leaks, and explosions.</td>
      <td><strong>Full 100,000+ Hour Lifespan: Capacitors operate cool with low harmonic distortion stress.</strong></td>
    </tr>
    <tr>
      <td><strong>Electrical Behavior at Harmonic Frequencies</strong></td>
      <td>Capacitive ($X_C$ drops as frequency rises), drawing heavy harmonic currents into the bank.</td>
      <td><strong>Inductive ($X_L > X_C$ above 189Hz), naturally repelling and blocking harmonic frequencies.</strong></td>
    </tr>
    <tr>
      <td><strong>Switching Inrush Current Damping</strong></td>
      <td>High inrush current transients (up to $100\times I_n$) during step energization without damping.</td>
      <td><strong>Inrush Suppressed: Series inductance naturally chokes and damps fast current rise transients.</strong></td>
    </tr>
    <tr>
      <td><strong>Utility Grid Power Quality &amp; Compliance</strong></td>
      <td>Amplified voltage distortion exceeds IEEE 519 and IEC 61000-2-4 regulatory limits.</td>
      <td><strong>Attenuates grid harmonic distortion, ensuring full compliance with IEEE 519 standards.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

DTR_FR = dict(
    lang='fr',
    dir='ltr',
    slug='harmonic-mitigation-what-is-a-detuned-reactor-fr',
    title="Filtrage d'Harmoniques & Batterie de Condensateurs : Qu'est-ce qu'une Self Anti-Harmonique (Detuned Reactor) ?",
    breadcrumb='Qualité de l\'Énergie &amp; Filtres Harmoniques',
    read='10 min de lecture',
    alt='Self anti-harmonique triphasée de type sec à circuit magnétique feuilleté (Série CKSG, accord 7%) installée dans une armoire de compensation automatique',
    desc=('Qualité de l\'énergie industrielle, batteries de condensateurs automatiques et protection contre la résonance harmonique : Qu\'est-ce qu\'une self anti-harmonique (detuned reactor) ? '
          'Facteurs d\'accord 7% (189Hz) et 14% (134Hz), tôles magnétiques au silicium à entrefer, bobinages cuivre classe H et norme CEI 60076-6.'),
    model='Série CKSG : Réactances de Filtrage d\'Harmoniques Triphasées Sèches à Circuit Magnétique (0,4kV / 0,45kV / 0,525kV, Facteur d\'Accord 7% & 14%, CEI 60076-6)',
    category='Qualité de l\'Énergie & Filtres Harmoniques / Selfs Anti-Harmoniques',
    kw='self anti harmonique &middot; detuned reactor &middot; reactance de filtrage &middot; reactance en serie condensateur &middot; self 7 pourcent &middot; cksg reactor',
    specs=[
        ('Tension Assignée de Service du Réseau', 'Tensions industrielles normalisées : 400V, 440V, 480V, 525V jusqu\'à 690V AC triphasé (50/60 Hz)'),
        ('Facteurs d\'Accord et Fréquences d\'Accord', 'p = 7% ($f_r = 189$ Hz à 50Hz, bloque les harmoniques 5 et 7) et p = 14% ($f_r = 134$ Hz, bloque le rang 3)'),
        ('Puissance Réactive Échelonnée Associée', 'Calibré pour les gradins de batteries de condensateurs : 10 kvar, 15 kvar, 20 kvar, 25 kvar, 30 kvar, 50 kvar jusqu\'à 100 kvar'),
        ('Circuit Magnétique et Technologie d\'Entrefer', 'Tôles magnétiques en acier au silicium à grains orientés à faibles pertes avec entrefers multiples calés par céramique'),
        ('Matériau des Enroulements et Isolation', 'Enroulements en cuivre électrolytique de haute pureté imprégnés sous vide avec isolants thermiques de Classe H (180&deg;C)'),
        ('Imprégnation sous Vide et Pression (VPI)', 'Traitement VPI complet sous résine polymérisée sans solvant ; fonctionnement ultra-silencieux (< 45–55 dB)'),
        ('Linéarité d\'Inductance sous Surcharge', 'Haute linéarité magnétique : Inductance $L \ge 0,95 L_n$ jusqu\'à 1,80–2,00 fois le courant nominal ($I_{lin} \ge 1,80 I_n$)'),
        ('Protection Thermique Interne Intégrée', 'Sonde thermique bimétallique miniature incorporée au cœur du bobinage de la phase centrale (NF, 125&deg;C–140&deg;C)')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une Self Anti-Harmonique (Detuned Reactor) et pourquoi est-elle indispensable en série avec les condensateurs ?',
         'Une Self Anti-Harmonique—appelée réactance de désaccord, bobine d\'inductance série ou self de filtrage—est '
         'une inductance triphasée à circuit magnétique raccordée en série avec chaque gradin de condensateurs dans une armoire de compensation automatique. '
         'Dans les usines et bâtiments modernes : '
         '<ul>'
         '<li><strong>Le Danger de Résonance Harmonique :</strong> Les charges non linéaires (variateurs de fréquence, onduleurs, redresseurs) génèrent '
         'des courants harmoniques de rang 5 (250Hz) et 7 (350Hz). Lorsqu\'on connecte des condensateurs standards, leur impédance capacitive diminue '
         'avec la fréquence tandis que celle du transformateur augmente. À une certaine fréquence, les deux s\'annulent, créant un <strong>phénomène de résonance parallèle</strong> '
         'qui multiplie les courants harmoniques par 3 à 5, faisant exploser les condensateurs et disjoncter les départs.</li>'
         '<li><strong>La Solution par la Self Anti-Harmonique :</strong> En associant une self en série avec le condensateur, la fréquence de résonance propre du circuit LC '
         'est décalée à <strong>189 Hz (pour un accord 7%)</strong>, bien en dessous du premier harmonique 5 (250 Hz). '
         'À 50 Hz, l\'ensemble reste capacitif et compense le facteur de puissance ; mais dès 250 Hz, le circuit devient inductif, rendant '
         'la résonance physiquement impossible et protégeant durablement les condensateurs.</li>'
         '</ul>'),
        ('Comment choisir entre un facteur d\'accord de 7% (189Hz) et 14% (134Hz) ?',
         'Le choix dépend de la nature des harmoniques polluant l\'installation : '
         '<ul>'
         '<li><strong>Accord 7% (189 Hz à 50Hz) :</strong> C\'est le standard industriel prépondérant pour les réseaux pollués par des variateurs de vitesse '
         'triphasés à 6 pulsations (harmoniques 5 et 7). Il élimine le risque de résonance tout en maintenant une excellente efficacité de compensation.</li>'
         '<li><strong>Accord 14% (134 Hz à 50Hz) :</strong> Indispensable sur les réseaux tertiaires ou hospitaliers comportant de nombreux équipements '
         'monophasés (éclairage LED, informatique, serveurs) générant un fort courant d\'<strong>harmonique de rang 3 (150Hz)</strong>, ou en présence de signaux tarifaires de télécommande.</li>'
         '</ul>'),
        ('Pourquoi la tension aux bornes des condensateurs augmente-t-elle avec une self en série ?',
         'L\'association série d\'une inductance et d\'une capacité provoque un effet de surtension calculé par $U_C = U_N / (1 - p)$. '
         'Sur un réseau 400V avec self 7%, la tension permanente aux bornes du condensateur monte à environ <strong>430V</strong>. '
         'Il est donc impératif d\'utiliser des condensateurs renforcés dimensionnés pour <strong>440V, 480V ou 525V</strong> sous peine de claquage prématuré.')
    ],
    cta='Vous assemblez des armoires de compensation automatique d\'énergie réactive (APFC) avec selfs anti-harmoniques ou recherchez des réactances triphasées sèches certifiées CEI 60076-6 (10 à 100 kvar, 7% & 14%) ? YOMIN fabrique des selfs série CKSG de haute technologie.',
    body='''
<h2>Le Bouclier Indispensable Contre la Résonance Harmonique dans les Usines Modernes</h2>
<p>Dans les installations industrielles modernes et les data centers, la prolifération massive des équipements d\'électronique de puissance—variateurs de fréquence (VFD), redresseurs, alimentations sans interruption (ASI / UPS) et onduleurs solaires—a profondément altéré la qualité de l\'onde électrique.</p>
<p>Ces appareils génèrent d\'importants courants harmoniques (principalement de rangs 5, 7 et 11) qui déforment la tension du réseau de distribution.</p>
<p>Lorsque les industriels installent des batteries de condensateurs classiques pour effacer les pénalités de dépassement de puissance réactive, un phénomène destructeur se produit fréquemment : l\'impédance capacitive des condensateurs entre en résonance parallèle avec l\'inductance du transformateur amont.</p>
<p>Cette résonance amplifie les courants harmoniques jusqu\'à 500%, provoquant le gonflement des condensateurs, la fusion intempestive des fusibles HPC, le déclenchement des disjoncteurs généraux et l\'échauffement anormal des transformateurs de puissance.</p>
<p>La <strong>Self Anti-Harmonique Triphasée Sèche (Série CKSG)</strong> apporte la solution technique absolue : une inductance connectée en série avec chaque échelon de condensateur qui décale la fréquence de résonance du circuit bien en dessous du rang 5, bloquant toute résonance et protégeant l\'armoire de compensation pour plus de 20 ans.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série CKSG</h2>
<ol>
  <li><strong>Circuit Magnétique Feuilleté à Faibles Pertes :</strong> Tôles d\'acier au silicium à grains orientés de premier choix assemblées avec des entrefers multiples pour garantir une linéarité parfaite sous forte surcharge.</li>
  <li><strong>Bobinages en Cuivre Électrolytique Classe H (180&deg;C) :</strong> Conducteurs largement dimensionnés capables de supporter en permanence les courants harmoniques déformés sans dégradation thermique.</li>
  <li><strong>Imprégnation sous Vide et Pression (VPI) :</strong> Polymérisation sous résine époxy sans solvant éliminant les bruits de vibration magnétique pour un niveau sonore inférieur à 50 dB.</li>
  <li><strong>Sonde Thermique Intégrée :</strong> Détecteur thermique bilame miniature monté au cœur du bobinage central déconnectant le gradin en cas de surchauffe accidentelle.</li>
</ol>
'''
)

DTR_ES = dict(
    lang='es',
    dir='ltr',
    slug='harmonic-mitigation-what-is-a-detuned-reactor-es',
    title='Mitigación de Armónicos y Bancos de Capacitores: ¿Qué es una Reactancia Antiharmónica (Detuned Reactor)?',
    breadcrumb='Calidad de Energía y Filtros de Armónicos',
    read='10 min de lectura',
    alt='Reactancia antiharmónica trifásica seca con núcleo de hierro laminado (Serie CKSG, sintonizada al 7%) instalada en tablero de corrección de factor de potencia',
    desc=('Calidad de energía industrial, bancos de capacitores automáticos (APFC) y protección contra resonancia armónica: ¿Qué es una reactancia antiharmónica (detuned reactor)? '
          'Factores de desintonía 7% (189Hz) y 14% (134Hz), núcleo de acero al silicio con entrehierros, devanados de cobre clase H y norma IEC 60076-6.'),
    model='Serie CKSG: Reactancias de Filtrado de Armónicos Trifásicas Secas con Núcleo de Hierro (0,4kV / 0,45kV / 0,525kV, Factor 7% y 14%, IEC 60076-6)',
    category='Calidad de Energía y Filtros de Armónicos / Reactancias Antiharmónicas',
    kw='reactancia antiharmonica &middot; detuned reactor &middot; reactancia de sintonizacion &middot; reactor serie para capacitor &middot; reactancia 7 por ciento &middot; cksg reactor',
    specs=[
        ('Clase de Tensión Asignada de Servicio', 'Tensiones industriales normalizadas: 400V, 440V, 480V, 525V hasta 690V AC trifásico (50/60 Hz)'),
        ('Factores de Desintonía y Frecuencias', 'p = 7% ($f_r = 189$ Hz en 50Hz, bloquea armónicos 5º y 7º) y p = 14% ($f_r = 134$ Hz, bloquea armónico 3º)'),
        ('Escalones de Potencia Reactiva Asociada', 'Calibrada para pasos estándar de bancos de capacitores: 10 kvar, 15 kvar, 20 kvar, 25 kvar, 30 kvar, 50 kvar hasta 100 kvar'),
        ('Material del Núcleo y Entrehierros Múltiples', 'Láminas de acero al silicio de grano orientado de bajas pérdidas con entrehierros seccionados mediante separadores cerámicos'),
        ('Conductor de Devanados y Aislamiento', 'Bobinas de cobre electrolítico de alta pureza con aislamiento térmico Clase H (180&deg;C) o Clase C (200&deg;C)'),
        ('Impregnación al Vacío y Presión (VPI)', 'Tratamiento completo VPI con resina polimérica epoxi libre de disolventes; nivel sonoro ultrasilencioso (< 45–55 dB)'),
        ('Umbral de Linealidad ante Sobrecargas', 'Excelente linealidad magnética: Inductancia $L \ge 0,95 L_n$ hasta 1,80–2,00 veces la corriente nominal ($I_{lin} \ge 1,80 I_n$)'),
        ('Sensor de Protección Térmica Incorporado', 'Interruptor termostático bimetálico en miniatura (NC, 125&deg;C–140&deg;C) embebido en el devanado de la fase central')
    ],
    faqs=[
        ('¿Qué es una Reactancia Antiharmónica (Detuned Reactor) y por qué se conecta en serie con los capacitores?',
         'Una Reactancia Antiharmónica—también denominada reactor de rechazo de armónicos, choque de desintonía o inductancia serie—es '
         'un inductor trifásico con núcleo de hierro conectado en serie con cada escalón de capacitores en un banco automático de factor de potencia (APFC). '
         'En plantas industriales y edificios comerciales: '
         '<ul>'
         '<li><strong>El Riesgo de Resonancia Paralela:</strong> Equipos como variadores de frecuencia (VFD), rectificadores y fuentes conmutadas inyectan '
         'corrientes armónicas (especialmente de 5º orden a 250Hz y 7º a 350Hz). Al conectar capacitores ordinarios, su reactancia capacitiva disminuye '
         'con la frecuencia mientras la inductancia del transformador aumenta. A cierta frecuencia, ambas se igualan creando una <strong>resonancia paralela destructiva</strong> '
         'que multiplica las corrientes armónicas hasta por 5 veces, haciendo estallar los capacitores y quemando transformadores.</li>'
         '<li><strong>La Solución con la Reactancia Serie:</strong> La reactancia desplaza la frecuencia de resonancia natural del conjunto LC '
         'a <strong>189 Hz (en reactancias del 7%)</strong>, situándola con seguridad por debajo del armónico 5º (250 Hz). '
         'A 50 Hz el conjunto se comporta como capacitor aportando reactivos; pero a 250 Hz o más, se vuelve inductivo, bloqueando físicamente '
         'la resonancia y absorbiendo parte de las corrientes armónicas sin dañar el banco.</li>'
         '</ul>'),
        ('¿Cómo seleccionar entre un factor de desintonía del 7% (189Hz) y del 14% (134Hz)?',
         'La selección depende del espectro armónico presente en la red de la fábrica: '
         '<ul>'
         '<li><strong>Factor del 7% (189 Hz en 50Hz / 227 Hz en 60Hz):</strong> Es el estándar predominante en la industria para redes con cargas trifásicas '
         'como variadores de frecuencia de 6 pulsos (armónicos 5º y 7º). Previene la resonancia y mantiene una óptima compensación de potencia reactiva.</li>'
         '<li><strong>Factor del 14% (134 Hz en 50Hz / 160 Hz en 60Hz):</strong> Es indispensable en redes con abundante carga monofásica (computadoras, '
         'iluminación LED, electrónica comercial) que generan fuertes corrientes de <strong>3º armónico (150Hz / 180Hz)</strong>, o en sistemas con señales de telemando de red.</li>'
         '</ul>'),
        ('¿Por qué los capacitores experimentan una mayor tensión cuando se colocan en serie con reactancias?',
         'La conexión en serie de un inductor y un capacitor provoca una elevación física de tensión sobre los bornes del capacitor según la fórmula $U_C = U_N / (1 - p)$. '
         'En una red de 400V con reactancia al 7%, la tensión efectiva sobre el capacitor sube a unos <strong>430V continuos</strong>. '
         'Por esta razón, es obligatorio utilizar capacitores reforzados dimensionados para <strong>440V, 480V o 525V</strong> para evitar su destrucción prematura.')
    ],
    cta='¿Diseña tableros automáticos de corrección de factor de potencia (APFC) con filtros de armónicos o requiere reactancias antiharmónicas secas certificadas IEC 60076-6 (10 a 100 kvar, 7% y 14%)? YOMIN fabrica reactancias serie CKSG de máxima confiabilidad.',
    body='''
<h2>La Defensa Indispensable Contra la Resonancia Armónica en Redes Industriales</h2>
<p>En complejos manufactureros, estaciones de bombeo, plantas automotrices y centros de datos, la adopción masiva de equipos de electrónica de potencia—como variadores de frecuencia (VFD), servomotores, arrancadores suaves y cargadores de baterías—ha transformado las redes eléctricas modernas.</p>
<p>Aunque estos equipos aportan un extraordinario control operativo y ahorro de energía, sus conmutaciones rápidas introducen severas corrientes armónicas distorsionadas (principalmente armónicos de 5º y 7º orden) que contaminan el sistema de distribución.</p>
<p>Cuando los ingenieros de planta instalan bancos de capacitores convencionales para eliminar las penalizaciones por bajo factor de potencia, se desata frecuentemente un problema grave: la reactancia de los capacitores entra en resonancia paralela con la inductancia del transformador de suministro.</p>
<p>Esta resonancia magnifica las corrientes armónicas hasta en un 500%, provocando el hinchamiento y explosión de botes de capacitores, disparo intempestivo de interruptores automáticos, fundición de fusibles y sobrecalentamiento crítico de transformadores y cables.</p>
<p>La <strong>Reactancia Antiharmónica Trifásica Seca (Serie CKSG)</strong> ofrece la respuesta definitiva: un inductor con núcleo de hierro conectado en serie con cada escalón que desplaza la frecuencia de resonancia por debajo del 5º armónico, garantizando una operación estable y segura del banco durante décadas.</p>

<h2>Componentes Constructivos y Calidad de Ingeniería de la Serie CKSG</h2>
<ol>
  <li><strong>Núcleo de Acero al Silicio con Entrehierros Cerámicos:</strong> Láminas de grano orientado de bajísimas pérdidas con entrehierros fraccionados que mantienen la inductancia lineal incluso con fuertes sobrecorrientes.</li>
  <li><strong>Devanados de Cobre Electrolítico Clase H (180&deg;C):</strong> Bobinas dimensionadas generosamente que disipan el calor eficientemente y resisten sobrecargas armónicas permanentes.</li>
  <li><strong>Impregnación al Vacío y Presión (VPI):</strong> Resina polimérica curada en horno que compacta rígidamente el ensamble, eliminando ruidos molestos ($< 50$ dB).</li>
  <li><strong>Termostato de Protección Integrado:</strong> Sensor bimetálico embebido en el bobinado central que desconecta el paso ante cualquier elevación anormal de temperatura.</li>
</ol>
'''
)

DTR_AR = dict(
    lang='ar',
    dir='rtl',
    slug='harmonic-mitigation-what-is-a-detuned-reactor-ar',
    title='تخميد التوافقيات وتحسين معامل القدرة: ما هو مفاعل التخميد التوافقي (Detuned Reactor)؟',
    breadcrumb='جودة الطاقة وفلاتر التوافقيات',
    read='10 دقائق قراءة',
    alt='مفاعل تخميد توافقي جاف ثلاثي الأطوار بقلب حديدي مصفح (موديل CKSG، بنسبة تخميد 7%) مركب داخل لوحة تحسين معامل القدرة الأوتوماتيكية',
    desc=('جودة الطاقة الكهربائية في المصانع، ولوحات مكثفات تحسين معامل القدرة (APFC)، والحماية من الرنين التوافقي: ما هو مفاعل التخميد التوافقي (Detuned Reactor)؟ '
          'نسب تخميد 7% (189Hz) و 14% (134Hz)، وقلب حديدي من صلب السيليكون ذو فجوات هوائية، وملفات نحاسية فئة H، ومعايير IEC 60076-6 لحماية المكثفات.'),
    model='سلسلة CKSG: مفاعلات تخميد التوافقيات ثلاثية الأطوار الجافة ذات القلب الحديدي (0.4kV / 0.45kV / 0.525kV، نسب تخميد 7% و 14%، معتمدة IEC 60076-6)',
    category='جودة الطاقة وفلاتر التوافقيات / مفاعلات التخميد التوافقي',
    kw='مفاعل تخميد توافقي &middot; detuned reactor &middot; خانق توافقيات &middot; ملف تخميد لمكثف &middot; مفاعل 7 بالمئة &middot; مفاعل cksg',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة', 'فئات تشغيل معيارية لشبكات التوزيع: 400V، 440V، 480V، 525V وحتى 690V AC ثلاثي الأطوار (50/60 هرتز)'),
        ('نسب وفترات تردد التخميد القياسية', 'p = 7% ($f_r = 189$ هرتز عند 50 هرتز، لحجب التوافقيين الخامس والسابع) و p = 14% ($f_r = 134$ هرتز، لحجب التوافقي الثالث)'),
        ('سعات خطوات بنك المكثفات المتوافقة', 'معاير لخطوات لوحات الـ APFC المعيارية: 10 كفار، 15 كفار، 20 كفار، 25 كفار، 30 كفار، 50 كفار وحتى 100 كفار'),
        ('مادة تصنيع القلب والفتحات الهوائية', 'شرائح صلب سيليكوني مدرفل على البارد ذو حبيبات موجهة قليل الفواقد مع فواصل فجوات هوائية سيراميكية دقيقة متعددة'),
        ('مادة تصنيع الملفات والعزل الحراري', 'ملفات نحاس كهربائي عالي النقاوة معزولة بعوازل حرارية متطورة من الفئة H (180&deg;C) أو الفئة C (200&deg;C)'),
        ('المعالجة بالعزل تحت الضغط والتفريغ', 'معالجة كاملة بتقنية VPI براتنج الإيبوكسي البوليمري عديم المذيبات؛ تشغيل فائق الهدوء بمستوى صوت أقل من (< 45–55 ديسيبل)'),
        ('حد الخطية المغناطيسية عند زيادة التيار', 'خطية تشبع فائقة: تظل الحثية $L \ge 0.95 L_n$ حتى 1.80 إلى 2.00 أضعاف التيار الاسمي للمكثف ($I_{lin} \ge 1.80 I_n$)'),
        ('منظومة الحماية الحرارية المدمجة', 'مفتاح حساس حراري ميكانيكي ثنائي المعدن مدمج مصنعياً في قلب ملف الطور الأوسط (مغلق طبيعياً NC، 125&deg;C–140&deg;C)')
    ],
    faqs=[
        ('ما هو مفاعل التخميد التوافقي (Detuned Reactor) ولماذا يجب ربطه على التوالي مع مكثفات تحسين معامل القدرة؟',
         'مفاعل التخميد التوافقي—ويعرف أيضاً باسم خانق التوافقيات أو مفاعل الرنين التوافقي أو سلف حماية المكثفات—هو '
         'ملف حثي ثلاثي الأطوار بقلب حديدي يوصل على التوالي مع كل خطوة من خطوات المكثفات داخل لوحة تحسين معامل القدرة (APFC). '
         'وفي المنشآت الصناعية الحديثة ومراكز البيانات: '
         '<ul>'
         '<li><strong>كارثة الرنين التوافقي المتوازي:</strong> الأجهزة الإلكترونية الحديثة (مغيرات السرعة VFD، محولات الطاقة الشمسية، شواحن البطاريات) '
         'تولد تيارات توافقية مشوهة للشبكة—وبالأخص <strong>التوافقي الخامس (250Hz) والسابع (350Hz)</strong>. وعند توصيل مكثفات عادية، تقل معاوقة المكثف '
         'مع زيادة التردد بينما تزداد معاوقة محول التوزيع. وعند تردد معين، تتساوى المعاوقتان، مما يخلق <strong>دائرة رنين متوازي كارثية</strong> '
         'تضاعف التيارات التوافقية بنسبة 300% إلى 500%، متسببة في انتفاخ المكثفات واحتراقها وانفجار الفيوزات واحتراق المحولات.</li>'
         '<li><strong>الحل بمفاعل التخميد:</strong> عند ربط مفاعل حثي على التوالي مع المكثف، تُضبط دائرة الرنين عند تردد آمن يبلغ <strong>189 هرتز (للمفاعل 7%)</strong>، '
         'وهو تردد يقع عمداً تحت التوافقي الخامس (250 هرتز). وعند التردد الأساسي (50Hz) يظل المسار سعوياً ويحسن معامل القدرة؛ أما عند 250 هرتز وما فوق، '
         'يتحول المسار إلى حثي ($X_L > X_C$)، مما يجعل حدوث الرنين مستحيلاً فيزيائياً ويحمي المكثفات تماماً من التلف.</li>'
         '</ul>'),
        ('كيف يختار مهندسو الكهرباء بين مفاعل تخميد بنسبة 7% (189Hz) ونسبة 14% (134Hz)؟',
         'يعتمد الاختيار على الطيف التوافقي الملوث للشبكة: '
         '<ul>'
         '<li><strong>مفاعل بنسبة 7% (تردد 189 هرتز):</strong> هو المعيار الصناعي العالمي الشائع للمصانع والشبكات التي تحتوي على مغيرات سرعة ثلاثية الأطوار (VFDs) '
         'تولد توافقيات من الرتبتين الخامسة والسابعة. يمنع الرنين بكفاءة عالية ويحافظ على أداء تعويض القدرة غير الفعالة.</li>'
         '<li><strong>مفاعل بنسبة 14% (تردد 134 هرتز):</strong> إلزامي في الشبكات التجارية ومباني المكاتب والمستشفيات التي تحتوي على أحمال أحادية الطور '
         'كثيفة (إضاءة ليد، كمبيوترات، خوادم) تولد تياراً توافقياً عالياً من <strong>الرتبة الثالثة (150 هرتز)</strong>، أو عند وجود إشارات تحكم شبكي من شركة الكهرباء.</li>'
         '</ul>'),
        ('لماذا يرتفع الجهد الكهربائي على أطراف المكثفات عند توصيل مفاعل تخميد معها على التوالي؟',
         'يتسبب ربط ملف حثي مع مكثف على التوالي في حدوث ارتفاع فيزيائي للجهد عبر أطراف المكثف طبقاً للمعادلة: $U_C = U_N / (1 - p)$. '
         'فعلى شبكة بجهد 400 فولت مع مفاعل 7%، يرتفع الجهد الفعلي على المكثف إلى نحو <strong>430 فولت باستمرار</strong>. '
         'لذلك يجب على المهندسين دائماً اختيار مكثفات ذات جهد مقنن أعلى—تحديداً <strong>مكثفات بجهد 440V أو 480V أو 525V</strong>—لتجنب تلفها السريع.')
    ],
    cta='هل تعمل على تصنيع لوحات تحسين معامل القدرة الأوتوماتيكية (APFC)، أو فلاتر التوافقيات، أو تحتاج إلى مفاعلات تخميد جافة ذات قلب حديدي معتمدة طبقاً للمواصفة IEC 60076-6 (من 10 إلى 100 كفار، 7% و 14%)؟ تصنع يمين (YOMIN) مفاعلات CKSG بأعلى درجات الدقة الهندسية.',
    body='''
<h2>الدرع الهندسي الحاسم ضد كوارث الرنين التوافقي في الشبكات الكهربائية الصناعية</h2>
<p>في المصانع الحديثة ومراكز البيانات ومحطات معالجة المياه، أدى الانتشار الهائل لأجهزة إلكترونيات القوى غير الخطية—مثل مغيرات السرعة للمحركات (VFDs)، ومحولات الطاقة الشمسية، ومصادر التغذية غير المنقطعة (UPS)—إلى ثورة في التحكم الصناعي، لكنه أفرز في الوقت ذاته تلوثاً توافقياً حاداً في موجات التيار الكهربائي.</p>
<p>هذه الأجهزة تضخ تيارات توافقية مشوهة (خاصة التوافقيات من الرتب 5 و 7 و 11) ترتد مباشرة نحو قضبان التوزيع الرئيسية.</p>
<p>وعندما يركب مهندسو المصانع بنوك مكثفات تقليدية لإلغاء غرامات معامل القدرة المنخفض، تقع مفاجأة كارثية: تتفاعل المعاوقة السعوية للمكثفات مع المعاوقة الحثية لمحول التوزيع لتخلق <strong>دائرة رنين توافقي متوازي</strong>.</p>
<p>يؤدي هذا الرنين إلى تضخيم التيارات التوافقية حتى 5 أضعاف قيمتها، مسبباً انتفاخ المكثفات وانفجارها، واحتراق الفيوزات، وفصل القواطع الكهربائية بصورة متكررة، وسخونة المحولات إلى درجات حرارة خطيرة تهدد بانهيارها.</p>
<p>يمثل <strong>مفاعل التخميد التوافقي الجاف ذو القلب الحديدي (سلسلة CKSG)</strong> الحل الوقائي المعتمد عالمياً: ملف حثي ثلاثي الأطوار يُربط على التوالي مع كل خطوة مكثفات ليغير تردد الرنين ويجعله دون الرتبة الخامسة، ملغياً أي فرصة لحدوث الرنين وحامياً مكونات اللوحة لأكثر من عشرين عاماً.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة مفاعلات CKSG</h2>
<ol>
  <li><strong>قلب حديدي مصفح من صلب السيليكون ذو فجوات هوائية دقيقة:</strong> شرائح موجهة الحبيبات منخفضة الفواقد مع فتحات هوائية مجزأة تضمن بقاء الحثية خطية تماماً حتى مع تيارات التوافقيات العالية.</li>
  <li><strong>ملفات نحاسية فئة H (180&deg;C):</strong> موصلات نحاسية كهرلية ذات مقاطع سميكة تتحمل التيارات المشوهة دون أي ارتفاع مفرط في درجات الحرارة.</li>
  <li><strong>معالجة العزل بالتفريغ والضغط (VPI):</strong> غمر كامل تحت الضغط والتفريغ براتنج الإيبوكسي عديم المذيبات لمنع الاهتزازات الميكانيكية وتوفير تشغيل فائق الهدوء دون طنين.</li>
  <li><strong>حساس حراري مدمج للحماية:</strong> ثرموستات دقيق ثنائي المعدن داخل ملف الطور الأوسط يفصل التغذية عن خطوة المكثف آلياً عند حدوث أي سخونة طارئة.</li>
</ol>
'''
)

# ==============================================================================
# 2. COMPOSITE SUSPENSION INSULATOR (EN, FR, ES, AR)
# ==============================================================================

CSI_EN = dict(
    lang='en',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-composite-suspension-insulator',
    title='Overhead Transmission & Distribution: What Is a Composite Suspension Insulator?',
    breadcrumb='Overhead Line Hardware &amp; Insulators',
    read='10 min read',
    alt='High-voltage Composite Polymer Suspension Long-Rod Insulator (Model FXBW series, 110kV rating, 100kN mechanical tension) suspended from a steel lattice transmission tower crossarm',
    desc=('High-voltage overhead transmission lines (11kV to 110kV), tension towers, and river crossings: What is a composite suspension insulator? '
          'How high-tensile ECR fiberglass core rods, hydrophobic HTV silicone rubber sheds, forged steel end fittings (70kN–160kN), and IEC 61109 standards prevent pollution flashovers and eliminate porcelain disc string failures.'),
    model='Model FXBW Series 11kV–110kV Composite Polymer Suspension & Tension Long-Rod Insulators (70kN to 160kN SML, IEC 61109 / ANSI C29.13)',
    category='Overhead Line Hardware & Insulators / Composite Suspension Insulators',
    kw='what is a composite suspension insulator &middot; composite suspension insulator &middot; polymer suspension insulator &middot; transmission line suspension insulator &middot; 70kn composite insulator &middot; fxbw insulator',
    specs=[
        ('Rated System Operating Voltage Class', 'Engineered for medium and high-voltage transmission & distribution lines: 11kV, 24kV, 33kV, 66kV, and 110kV AC (up to 220kV)'),
        ('Specified Mechanical Tensile Failing Load', 'Standard tensile ratings: 70 kN, 100 kN, 120 kN, and 160 kN (mechanical tension and suspension tower applications)'),
        ('Core Rod Material & Construction', 'High-tensile, electrical-grade epoxy-resin impregnated boron-free E-glass or ECR fiberglass rod (crimped with multi-directional swaging)'),
        ('Insulating Housing & Shed Weather Cover', 'High-temperature vulcanized (HTV) liquid silicone rubber (LSR) injection molded seamlessly onto the rod (hydrophobic class HC1/HC2)'),
        ('End Fitting Types & Material Quality', 'Hot-dip galvanized forged steel end fittings: Ball & Socket (IEC 60120), Clevis & Tongue (IEC 60471), or Y-Clevis / Eye'),
        ('Pollution Performance & Creepage Distance', 'Extra-heavy pollution resistance (&ge; 31 mm/kV specific creepage distance); aerodynamic sheds resist sandstorms and salt accumulation'),
        ('Lightning Impulse & Power-Frequency Withstand', 'Dry lightning impulse withstand (BIL): up to 550 kV; 1-minute wet power-frequency withstand: up to 230 kV (110kV class)'),
        ('Applicable Quality & Safety Standards', 'Fully tested and compliant with IEC 61109, IEC 62217, ANSI C29.13, IEEE 987, and ISO 9001 quality management')
    ],
    faqs=[
        ('What is a Composite Suspension Insulator and where is it used on overhead transmission grids?',
         'A Composite Suspension Insulator—commonly known as a polymer suspension insulator, silicone long-rod insulator, or non-ceramic insulator (NCI)—is '
         'a specialized high-voltage insulating tension device designed to mechanically suspend energized transmission conductors while electrically insulating '
         'them from grounded steel lattice towers, wooden poles, or substation crossarms. '
         'It is utilized extensively across utility power grids: '
         '<ul>'
         '<li><strong>1. Suspension Towers (Straight Runs):</strong> Hung vertically from tower crossarms, supporting the massive vertical weight and wind lateral loads '
         'of bare aluminum conductor steel reinforced (ACSR) or all-aluminum alloy conductors (AAAC).</li>'
         '<li><strong>2. Tension &amp; Dead-End Towers:</strong> Mounted horizontally or obliquely in dead-end tension assemblies, resisting full longitudinal line tension '
         '(70kN to 160kN) where the transmission line terminates, crosses highways or rivers, or navigates sharp directional angles.</li>'
         '<li><strong>3. Coastal, Desert &amp; Heavy Industrial Corridors:</strong> Deployed in high-salinity coastal areas, desert sandstorm zones, and chemical industrial corridors '
         'where traditional ceramic insulators suffer catastrophic pollution flashover outages.</li>'
         '</ul>'),
        ('Why are composite long-rod insulators replacing traditional porcelain and glass disc insulator strings?',
         'For over a century, high-voltage lines relied on strings of porcelain or toughened glass cap-and-pin disc insulators. '
         'However, utilities worldwide are rapidly migrating to composite silicone long-rod insulators for four decisive engineering reasons: '
         '<ul>'
         '<li><strong>1. Dramatic Weight Reduction (Up to 80% Lighter):</strong> A 110kV porcelain disc string weighs 40 to 60 kg, requiring heavy cranes and strenuous lineman handling. '
         'An equivalent 110kV composite insulator weighs only 5 to 8 kg, drastically reducing tower structural steel weight and accelerating helicopter or bucket truck installation.</li>'
         '<li><strong>2. Superior Hydrophobic Flashover Immunity:</strong> Ceramic surfaces become hydrophilic when wet, allowing conductive water film and salt/dust layers to cause '
         'violent electrical flashovers. Silicone rubber exhibits permanent <strong>hydrophobicity (water-repellency)</strong> and transfers hydrophobic low-molecular-weight silicone oils '
         'into the accumulated pollution layer, causing moisture to bead into isolated droplets and preventing leakage current flow.</li>'
         '<li><strong>3. High Vandalism &amp; Shatter Resistance:</strong> Porcelain and glass insulators are brittle and easily shattered by gunshots, vandalism, flying rocks, '
         'or mechanical impacts during transport. Composite insulators absorb shock without cracking or shattering.</li>'
         '<li><strong>4. Zero Zero-Value Insulator Degradation:</strong> Porcelain discs suffer from hidden microscopic internal puncture cracks that necessitate regular, costly '
         'on-line voltage distribution testing. Composite rods are solid and immune to internal punctures.</li>'
         '</ul>'),
        ('How does the swaged forged steel end fitting transfer massive tensile forces without slipping off the fiberglass core rod?',
         'The interface between the steel end fitting and the fiberglass rod is the critical mechanical load-bearing point. '
         'YOMIN FXBW Composite Insulators utilize high-precision <strong>multi-directional radial swaging (crimping) technology</strong>: '
         'A computerized 24-point circumferential swaging press compresses the hot-dip galvanized forged steel sleeve radially into the fiberglass rod. '
         'Precision acoustic emission monitoring sensors verify that the crimping force permanently locks the steel into the rod surface without crushing the internal glass fibers. '
         'This creates a mechanical grip that reliably exceeds the Specified Mechanical Load (e.g., 100kN or 160kN) without slippage across decades of thermal cycling.')
    ],
    cta='Engineering high-voltage overhead transmission lines, tension towers, substation dead-end structures, or anti-pollution grid upgrades requiring certified IEC 61109 composite suspension insulators (70kN to 160kN, 11kV to 110kV)? YOMIN manufactures high-durability FXBW series polymer long-rod insulators.',
    body='''
<h2>The Modern Technological Revolution in High-Voltage Overhead Transmission Line Insulation</h2>
<p>Across national electrical power transmission grids, regional sub-transmission networks, and renewable wind and solar interconnection corridors operating at <strong>33kV, 66kV, and 110kV</strong>, high-voltage overhead lines transport bulk electrical energy over hundreds of kilometers of rugged terrain.</p>
<p>Along these transmission corridors, line insulators must perform two demanding, simultaneous functions: mechanically supporting heavy multi-ton spans of conductor wire under gale-force winds and heavy ice loading, while providing flawless dielectric electrical insulation against grounded steel towers.</p>
<p>For more than a century, utilities relied on heavy strings of porcelain or toughened glass disc insulators. However, porcelain strings are heavy, fragile, and vulnerable to catastrophic electrical flashover outages when coastal salt fog or desert sandstorm dust accumulates on their hydrophilic surfaces.</p>
<p>The <strong>Composite Polymer Suspension &amp; Tension Long-Rod Insulator (Model FXBW Series)</strong> represents the definitive modern standard: lightweight, high-strength insulators built from aerospace-grade fiberglass core rods and hydrophobic silicone rubber weather housings that eliminate pollution flashovers and reduce installation labor by over 70%.</p>

<h2>Engineering Anatomy: Inside a Model FXBW Composite Suspension Long-Rod Insulator</h2>
<ol>
  <li><strong>Corrosion-Resistant ECR Fiberglass Core Rod:</strong> Pultruded from electrical-grade, boron-free glass fibers impregnated with high-grade epoxy resin. Delivers tensile strength exceeding 1,000 MPa—stronger than structural steel—while providing superior resistance to brittle fracture and acid attack.</li>
  <li><strong>High-Temperature Vulcanized (HTV) Silicone Rubber Housing:</strong> Injection-molded seamlessly over the core rod under high pressure. Exhibits natural hydrophobicity (water-repellency) and unique hydrophobic transfer, migrating silicone oils into dust and salt layers to prevent conductive water film formation.</li>
  <li><strong>Aerodynamic Alternating Shed Profile:</strong> Alternating larger and smaller shed diameters optimize creepage distance (&ge; 31 mm/kV) while allowing self-cleaning by natural wind and rain, preventing ice-bridging and dust build-up.</li>
  <li><strong>Hot-Dip Galvanized Forged Steel End Fittings:</strong> Heavy-duty forged steel ball-and-socket (IEC 60120) or clevis-and-tongue fittings hot-dip galvanized to ASTM A153 for maximum corrosion resistance, swaged to the rod via computerized radial crimping.</li>
  <li><strong>Aluminum Alloy Corona Grading Rings:</strong> Installed on insulators operating at 66kV and 110kV to smooth electrical field gradients, prevent surface corona discharge, and protect silicone sheds from electrical degradation.</li>
</ol>

<h2>Comparison: Composite Suspension Long-Rod Insulator vs. Traditional Porcelain Cap-and-Pin Disc String</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Porcelain Cap-and-Pin Disc String (110kV)</th>
      <th>YOMIN Composite Suspension Insulator (FXBW Series, 110kV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Total Unit Weight &amp; Handling Effort</strong></td>
      <td>Extremely Heavy: 45 to 60 kg per string; requires cranes and multi-man line crews.</td>
      <td><strong>Ultra-Lightweight: 5 to 7 kg (approx. 85% lighter); easy one-man handling aloft.</strong></td>
    </tr>
    <tr>
      <td><strong>Pollution Flashover Immunity &amp; Surface Behavior</strong></td>
      <td>Hydrophilic: Wet dust forms conductive sheets; requires regular high-pressure washing.</td>
      <td><strong>Permanently Hydrophobic: Water forms isolated droplets; zero washing required in desert/salt areas.</strong></td>
    </tr>
    <tr>
      <td><strong>Impact Resistance &amp; Vandalism Durability</strong></td>
      <td>Brittle ceramic: Easily shattered by gunshots, rocks, handling drops, or hail storms.</td>
      <td><strong>Shatter-Proof: Flexible composite construction absorbs mechanical impacts without damage.</strong></td>
    </tr>
    <tr>
      <td><strong>Mechanical Tensile Strength Consistency</strong></td>
      <td>Cement joints between caps and pins degrade over decades under thermal cycling.</td>
      <td><strong>Continuous Pultruded Core: Uniform tensile failing loads from 70kN to 160kN without cement joints.</strong></td>
    </tr>
    <tr>
      <td><strong>Installation &amp; Tower Structural Cost</strong></td>
      <td>High: Heavy strings require reinforced tower crossarms and prolonged crane time.</td>
      <td><strong>Low: Lighter weight reduces tower steel tonnage and slashes helicopter/bucket truck installation hours.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

CSI_FR = dict(
    lang='fr',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-composite-suspension-insulator-fr',
    title="Lignes Aériennes Moyenne & Haute Tension : Qu'est-ce qu'un Isolateur Composite Suspendu (Suspension Insulator) ?",
    breadcrumb='Matériel de Ligne &amp; Isolateurs HT',
    read='10 min de lecture',
    alt='Isolateur composite suspendu longue tige haute tension (Série FXBW, 110kV, 100kN) suspendu à la traverse d\'un pylône métallique en treillis',
    desc=('Lignes aériennes de transport et de répartition haute tension (11kV à 110kV), pylônes d\'ancrage et traversées : Qu\'est-ce qu\'un isolateur composite suspendu ? '
          'Jonc en fibre de verre ECR haute résistance, ailettes hydrophobes en élastomère de silicone HTV, embouts acier forgé (70kN–160kN) et norme CEI 61109.'),
    model='Série FXBW : Isolateurs composites suspendus et d\'ancrage longue tige pour lignes aériennes HT (11kV à 110kV, 70kN à 160kN, CEI 61109 / ANSI C29.13)',
    category='Matériel de Ligne & Isolateurs HT / Isolateurs Composites Suspendus',
    kw='isolateur composite suspendu &middot; isolateur polymere &middot; isolateur suspension 110kv &middot; isolateur longue tige silicone &middot; fxbw insulator &middot; isolateur 70kn',
    specs=[
        ('Classe de Tension Assignée de Service', 'Conçu pour les lignes aériennes de distribution et de transport HT : 11kV, 24kV, 33kV, 66kV et 110kV AC (jusqu\'à 220kV)'),
        ('Charge Mécanique Spécifiée de Rupture (SML)', 'Charges mécaniques de traction standardisées : 70 kN, 100 kN, 120 kN et 160 kN (en suspension et ancrage d\'arrêt)'),
        ('Jonc Central Porteur et Matériau', 'Jonc en résine époxyde armée de fibres de verre sans bore de qualité électrique ECR (résistant à la corrosion sous contrainte)'),
        ('Revêtement Protecteur et Ailettes', 'Enveloppe et ailettes moulées par injection sous haute pression en élastomère de silicone HTV hydrophobe (Classe HC1/HC2)'),
        ('Types d\'Embouts Métalliques d\'Extrémité', 'Embouts en acier forgé galvanisé à chaud : Rotule & Logement de rotule (CEI 60120), Chape & Tenon (CEI 60471) ou Œillet'),
        ('Tenue à la Pollution et Ligne de Fuite', 'Ligne de fuite spécifique pour pollution très lourde (&ge; 31 mm/kV) ; profil aérodynamique auto-nettoyant par vent et pluie'),
        ('Tension de Tenue aux Chocs de Foudre (BIL)', 'Onde de choc de foudre normalisée 1,2/50 &mu;s jusqu\'à 550 kV ; tension de tenue à fréquence industrielle sous pluie jusqu\'à 230 kV'),
        ('Normes Internationales et Homologations', 'Conforme aux normes CEI 61109, CEI 62217, ANSI C29.13, certifié ISO 9001 pour réseaux de transport d\'électricité')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Isolateur Composite Suspendu et quel est son rôle sur les pylônes de transport d\'électricité ?',
         'Un Isolateur Composite Suspendu—couramment désigné sous le terme d\'isolateur polymère longue tige ou isolateur synthétique en silicone—est '
         'un appareil d\'isolation haute tension conçu pour suspendre mécaniquement les câbles conducteurs aériens sous tension tout en assurant '
         'leur isolement diélectrique absolu par rapport au pylône métallique relié à la terre. '
         'Il est déployé massivement sur les réseaux électriques : '
         '<ul>'
         '<li><strong>1. Sur les Pylônes d\'Alignement (Suspension) :</strong> Accroché verticalement sous les traverses, il supporte le poids des conducteurs '
         'en aluminium-acier (Almélec / ACSR) et résiste aux rafales de vent transversales.</li>'
         '<li><strong>2. Sur les Pylônes d\'Angle et d\'Arrêt (Ancrage) :</strong> Monté horizontalement en chaîne d\'ancrage, il retient la traction longitudinale '
         'extrême de la portée de ligne (de 70kN à 160kN) aux virages de lignes et franchissements de fleuves ou d\'autoroutes.</li>'
         '<li><strong>3. En Environnements Pollués :</strong> Indispensable sur les littoraux marins exposés au sel et les zones désertiques sableuses.</li>'
         '</ul>'),
        ('Pourquoi les isolateurs composites remplacent-ils les chaînes traditionnelles de disques en verre ou porcelaine ?',
         'Pendant des décennies, les lignes HT utilisaient des chaînes composées de disques en verre trempé ou en porcelaine assemblés par rotules. '
         'Les isolateurs composites en silicone s\'imposent aujourd\'hui pour quatre raisons déterminantes : '
         '<ul>'
         '<li><strong>1. Réduction de Poids Spectaculaire (85% plus légers) :</strong> Une chaîne 110kV en verre pèse environ 50 kg ; l\'isolateur composite '
         'équivalent ne pèse que 6 kg, facilitant la manutention par les monteurs et allégeant les charpentes des pylônes.</li>'
         '<li><strong>2. Immunité Totale au Contournement par Pollution (Hydrophobie) :</strong> Le silicone repousse l\'eau et transfère son hydrophobicité '
         'aux couches de poussière et de sel, empêchant la formation d\'un film conducteur continu et supprimant tout lavage de ligne.</li>'
         '<li><strong>3. Résistance aux Chocs et aux Actes de Malveillance :</strong> Insensible aux impacts de cailloux, tirs d\'armes à feu et vibrations.</li>'
         '<li><strong>4. Absence de Défaut Zéro :</strong> Pas de perforation diélectrique interne invisible nécessitant des contrôles coûteux.</li>'
         '</ul>'),
        ('Comment le sertissage des embouts garantit-il la tenue à des tractions de 100 kN sans glissement ?',
         'La jonction entre l\'embout en acier forgé et le jonc en fibre de verre est réalisée par <strong>sertissage radial multidirectionnel sous contrôle électronique</strong>. '
         'Des mâchoires compriment l\'acier sur le jonc avec contrôle par émission acoustique pour verrouiller les pièces sans écraser les fibres internes, '
         'garantissant une tenue mécanique supérieure à la charge de rupture spécifiée (70kN ou 160kN) sans aucun fluage pendant 40 ans.')
    ],
    cta='Vous construisez des lignes aériennes haute tension, des postes de transformation ou menez des rénovations de réseaux anti-pollution nécessitant des isolateurs composites suspendus certifiés CEI 61109 (70kN à 160kN, 11kV à 110kV) ? YOMIN fabrique des isolateurs synthétiques FXBW de haute performance.',
    body='''
<h2>La Révolution des Isolateurs Composites sur les Lignes Aériennes Haute Tension</h2>
<p>Sur les réseaux de transport et de grand transport d\'électricité opérant sous des tensions de <strong>33kV, 63kV, 90kV et 110kV</strong>, les lignes aériennes parcourent des centaines de kilomètres à travers des zones géographiques extrêmes.</p>
<p>Le long de ces corridors, les isolateurs doivent remplir deux missions simultanées et critiques : supporter des portées de câbles pesant plusieurs tonnes sous des vents de tempête et des charges de givre, tout en maintenant une isolation diélectrique sans faille face aux pylônes métalliques reliés à la terre.</p>
<p>Pendant plus d\'un siècle, les chaînes de disques en verre trempé ou en porcelaine ont été la norme. Cependant, elles sont très lourdes, fragiles et sensibles aux contournements électriques violents en atmosphère saline ou industrielle polluée.</p>
<p>L\'<strong>Isolateur Composite Suspendu Longue Tige (Série FXBW)</strong> incarne le standard moderne incontournable : un appareil ultra-léger et incassable associant un jonc porteur en fibre de verre et une enveloppe en élastomère de silicone hydrophobe qui élimine les amorçages et divise par deux les coûts de montage.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série FXBW</h2>
<ol>
  <li><strong>Jonc Central en Fibre de Verre ECR Haute Ténacité :</strong> Résistance à la traction supérieure à 1 000 MPa (plus résistant que l\'acier de structure), totalement insensible à la corrosion sous tension acide.</li>
  <li><strong>Revêtement en Silicone HTV à Hydrophobicité Permanente :</strong> Repousse naturellement l\'eau sous forme de gouttelettes séparées, bloquant les courants de fuite superficiels sans aucun nettoyage.</li>
  <li><strong>Profil d\'Ailettes Aérodynamique Alterné :</strong> Optimise la ligne de fuite (&ge; 31 mm/kV) et favorise l\'auto-nettoyage naturel sous l\'action du vent et de la pluie.</li>
  <li><strong>Embouts en Acier Forgé Galvanisé à Chaud :</strong> Sertis radialement avec une précision micrométrique pour garantir une résistance à la traction de 70 kN à 160 kN sans jeu mécanique.</li>
</ol>
'''
)

CSI_ES = dict(
    lang='es',
    dir='ltr',
    slug='overhead-transmission-lines-what-is-a-composite-suspension-insulator-es',
    title='Líneas Aéreas de Transmisión y Distribución: ¿Qué es un Aislador Compuesto de Suspensión (Suspension Insulator)?',
    breadcrumb='Herrajes de Línea y Aisladores AT',
    read='10 min de lectura',
    alt='Aislador polimérico compuesto de suspensión tipo varilla larga de alta tensión (Serie FXBW, 110kV, 100kN) suspendido de la cruceta de una torre metálica de celosía',
    desc=('Líneas aéreas de transmisión y distribución en alta tensión (11kV a 110kV), torres de retención y cruces: ¿Qué es un aislador compuesto de suspensión? '
          'Varilla de fibra de vidrio ECR de alta resistencia, aletas de silicona HTV hidrófuga, herrajes de acero forjado (70kN–160kN) y norma IEC 61109.'),
    model='Serie FXBW: Aisladores Poliméricos Compuestos de Suspensión y Retención Tipo Long-Rod (11kV a 110kV, 70kN a 160kN SML, IEC 61109 / ANSI C29.13)',
    category='Herrajes de Línea y Aisladores AT / Aisladores Compuestos de Suspensión',
    kw='aislador compuesto de suspension &middot; aislador polimerico &middot; aislador suspension 110kv &middot; aislador long rod silicona &middot; aislador fxbw &middot; aislador 70kn',
    specs=[
        ('Clase de Tensión Asignada de Servicio', 'Diseñado para líneas aéreas de distribución y transmisión en alta tensión: 11kV, 24kV, 33kV, 66kV y 110kV AC (hasta 220kV)'),
        ('Carga Mecánica Especificada de Rotura (SML)', 'Capacidades de tracción nominal estándar: 70 kN, 100 kN, 120 kN y 160 kN (para suspensión y amarre en retención)'),
        ('Material del Núcleo Portante de Tracción', 'Varilla de resina epoxi reforzada con fibra de vidrio ECR de calidad eléctrica libre de boro (inmune a fractura por corrosión ácida)'),
        ('Recubrimiento Aislante y Aletas Protectoras', 'Aletas y envolvente moldeadas por inyección continua de caucho de silicona HTV de alta hidrofobicidad (Clase HC1/HC2)'),
        ('Herrajes Metálicos de Sujeción Extrema', 'Accesorios de acero forjado galvanizado en caliente: Rótula & Alojamiento (IEC 60120), Horquilla & Lengüeta (IEC 60471) u Ojo'),
        ('Resistencia a la Contaminación Ambiental', 'Línea de fuga específica para zonas de polución muy pesada (&ge; 31 mm/kV) ; perfil aerodinámico autolimpiable por viento y lluvia'),
        ('Tensión Soportada al Impulso de Rayo (BIL)', 'Tensión al impulso tipo rayo normalizado 1,2/50 &mu;s de hasta 550 kV ; tensión soportada bajo lluvia a frecuencia industrial hasta 230 kV'),
        ('Normativas Internacionales de Calidad', 'Fabricado y ensayado bajo normas IEC 61109, IEC 62217, ANSI C29.13 y sistema de gestión de calidad ISO 9001')
    ],
    faqs=[
        ('¿Qué es un Aislador Compuesto de Suspensión y cuál es su función en torres de transmisión eléctrica?',
         'Un Aislador Compuesto de Suspensión—conocido comúnmente como aislador polimérico tipo varilla larga (long-rod) o aislador sintético de silicona—es '
         'un dispositivo electromecánico de alta tensión diseñado para sostener físicamente los cables conductores energizados manteniéndolos '
         'aislados eléctricamente de la estructura metálica conectada a tierra de la torre de celosía o poste. '
         'Se utiliza en puntos fundamentales de las redes eléctricas: '
         '<ul>'
         '<li><strong>1. En Torres de Alineación (Suspensión):</strong> Colgado verticalmente de las crucetas, soportando el peso del conductor '
         'de aluminio con alma de acero (ACSR) y las fuerzas laterales provocadas por el viento.</li>'
         '<li><strong>2. En Torres de Retención y Amarre (Tensión):</strong> Instalado horizontalmente en cadenas de amarre, soportando la tensión mecánica '
         'longitudinal completa del vano (de 70kN a 160kN) en curvas de línea y cruces de autopistas o ríos.</li>'
         '<li><strong>3. En Zonas Costeras e Industriales Contaminadas:</strong> Donde la niebla salina marina causa descargas en aisladores de porcelana.</li>'
         '</ul>'),
        ('¿Por qué los aisladores poliméricos sustituyen a las cadenas tradicionales de campanas de vidrio o porcelana?',
         'Durante décadas se emplearon cadenas de platos de vidrio templado o porcelana acoplados por rótulas. '
         'Los aisladores compuestos se han convertido en el estándar moderno por cuatro ventajas determinantes: '
         '<ul>'
         '<li><strong>1. Reducción de Peso de hasta un 85%:</strong> Una cadena de vidrio de 110kV pesa entre 45 y 60 kg; el aislador polimérico '
         'equivalente pesa solo entre 5 y 7 kg, facilitando enormemente el izado manual por linieros y aligerando el peso en crucetas.</li>'
         '<li><strong>2. Inmunidad Total al Flameo por Contaminación (Hidrofobicidad):</strong> La silicona HTV repele el agua y transfiere su repelencia '
         'a la suciedad acumulada, formando gotas aisladas que impiden caminos continuos de fuga eléctrica y eliminan el lavado de aisladores.</li>'
         '<li><strong>3. Resistencia a Impactos y Vandalismo:</strong> No se quiebra ni astilla ante golpes de transporte, pedradas o disparos de armas.</li>'
         '<li><strong>4. Cero Fisuras Ocultas:</strong> No sufre de pérdidas de rigidez dieléctrica interna invisibles que exijan pruebas costosas.</li>'
         '</ul>'),
        ('¿Cómo asegura el engaste de los herrajes soportar tensiones de 100 kN o 160 kN sin desprenderse?',
         'La unión entre el herraje de acero forjado y la varilla de fibra de vidrio se realiza mediante <strong>engaste o engrapado radial multidireccional computarizado</strong>. '
         'Prensas de alta precisión comprimen el acero sobre la fibra con monitoreo de emisión acústica que garantiza un amarre sólido '
         'sin dañar las microfibras internas, superando la Carga Mecánica Especificada (SML) durante más de 40 años de vida útil.')
    ],
    cta='¿Construye líneas de transmisión de alta tensión, subestaciones eléctricas o proyectos de repotenciación de redes que requieren aisladores compuestos de suspensión certificados IEC 61109 (70kN a 160kN, 11kV a 110kV)? YOMIN fabrica aisladores poliméricos FXBW de máxima durabilidad.',
    body='''
<h2>La Evolución Tecnológica en el Aislamiento de Líneas Aéreas de Alta Tensión</h2>
<p>En redes de transmisión de energía eléctrica en alta tensión que operan en <strong>33kV, 66kV y 110kV</strong>, los tendidos aéreos transportan grandes bloques de potencia a lo largo de cientos de kilómetros de topografías exigentes.</p>
<p>A lo largo de estas rutas, los aisladores de línea deben cumplir dos misiones críticas de forma simultánea: soportar el peso de conductores de varias toneladas sometidos a ráfagas de viento y cargas de hielo, garantizando un aislamiento dieléctrico perfecto respecto a la estructura metálica conectada a tierra.</p>
<p>Durante más de un siglo, las cadenas de platos de vidrio o porcelana fueron el estándar. Sin embargo, su elevado peso, fragilidad ante golpes y alta vulnerabilidad al contorneo eléctrico en ambientes húmedos y salinos representan un serio problema para las empresas eléctricas.</p>
<p>El <strong>Aislador Compuesto de Suspensión Tipo Varilla Larga (Serie FXBW)</strong> constituye la solución homologada del sector utility moderno: un herraje ultra liviano e irrompible compuesto por un núcleo de fibra de vidrio de alta resistencia y una cubierta de silicona hidrófuga que suprime los cortes por contaminación y abarata los costes de montaje.</p>

<h2>Componentes y Excelencia de Ingeniería de la Serie FXBW</h2>
<ol>
  <li><strong>Varilla Central de Fibra de Vidrio ECR:</strong> Resistencia a la tracción superior a 1.000 MPa (más resistente que el acero estructural), inmune a la corrosión bajo tensión.</li>
  <li><strong>Cubierta y Aletas de Caucho de Silicona HTV Hidrófuga:</strong> Rechaza naturalmente la humedad en gotas aisladas impidiendo la formación de películas conductoras de corriente.</li>
  <li><strong>Perfil Aerodinámico de Aletas Alternadas:</strong> Maximiza la línea de fuga (&ge; 31 mm/kV) y favorece la autolimpieza natural mediante el viento y la lluvia.</li>
  <li><strong>Herrajes de Acero Forjado Galvanizado en Caliente:</strong> Engastados radialmente con precisión micrométrica para garantizar cargas mecánicas de rotura de 70 kN a 160 kN.</li>
</ol>
'''
)

CSI_AR = dict(
    lang='ar',
    dir='rtl',
    slug='overhead-transmission-lines-what-is-a-composite-suspension-insulator-ar',
    title='خطوط النقل والتوزيع الهوائية: ما هو العازل المعلق المركب (Composite Suspension Insulator)؟',
    breadcrumb='مهمات الخطوط الهوائية وعوازل الجهد العالي',
    read='10 دقائق قراءة',
    alt='عازل معلق مركب من البوليمر للجهد العالي (موديل FXBW، جهد 110kV، قوة شد 100kN) معلق على ذراع برج نقل كهربائي شبكي',
    desc=('خطوط النقل الكهربائي الهوائي للجهد العالي (11kV إلى 110kV)، وأبراج الشد، ومعابر الأنهار: ما هو العازل المعلق المركب (Composite Suspension Insulator)؟ '
          'قضيب ألياف زجاجية ECR فائق الشد، ومظلات مطاط السيليكون HTV الطارد للماء، ونهايات صلب مطروق (70kN–160kN)، ومعيار IEC 61109 لمنع وميض التلوث الكهربائي.'),
    model='سلسلة FXBW: عوازل التعليق والشد البوليمرية المركبة للجهد العالي (11kV إلى 110kV، قوة شد 70kN إلى 160kN، معتمدة IEC 61109 / ANSI C29.13)',
    category='مهمات الخطوط الهوائية وعوازل الجهد العالي / عوازل التعليق المركبة',
    kw='عازل معلق مركب &middot; composite suspension insulator &middot; عازل بوليمر 110kv &middot; عازل سيليكون لخطوط النقل &middot; عازل fxbw &middot; عازل شد 70kn',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة', 'مصمم لخطوط التوزيع والنقل الهوائي للجهد العالي: 11kV و 24kV و 33kV و 66kV و 110kV AC (وحتى 220kV)'),
        ('حمل الانهيار الميكانيكي الاسمي للشد (SML)', 'قدرات شد ميكانيكية قياسية: 70 kN و 100 kN و 120 kN و 160 kN (لأبراج التعليق وأبراج الشد والإنهاء)'),
        ('مادة تصنيع القضيب المركزي الحامل', 'قضيب ألياف زجاجية إيبوكسي عالي المتانة خالٍ من البورون من فئة ECR (مقاوم للتآكل الإجهادي الحمضي الميكانيكي)'),
        ('الغلاف الواقي ومظلات العزل الخارجية', 'غلاف ومظلات مصبوبة بالحقن من مطاط السيليكون المعالج حرارياً (HTV) عالي الطرد للماء (فئة طرد الماء HC1/HC2)'),
        ('أنواع النهايات المعدنية وطبقة الحماية', 'نهايات صلب مطروق مجلفن بالغمس الساخن: كرة ومقبس (IEC 60120)، وشوكة ولسان (IEC 60471) أو حلقة دائرية'),
        ('مقاومة التلوث ومسافة التسرب السطحية', 'مسافة تسرب مخصصة للتلوث الشديد جداً (&ge; 31 مم/كيلوفولت)؛ تصميم أيروديناميكي ينظف ذاتياً بالرياح والأمطار'),
        ('جهد صمود نبضات الصواعق والتردد الصناعي', 'جهد صمود نبضة صاعقة جافة 1.2/50 &mu;s حتى 550 kV؛ جهد صمود تردد صناعي مبلل لمدة دقيقة حتى 230 kV (لفئة 110kV)'),
        ('المواصفات القياسية والشهادات الدولية', 'مختبر ومطابق كلياً للمواصفات الدولية IEC 61109 و IEC 62217 و ANSI C29.13 وشهادة ISO 9001 لشركات نقل الكهرباء')
    ],
    faqs=[
        ('ما هو العازل المعلق المركب (Composite Suspension Insulator) وما هي وظيفته على أبراج نقل الكهرباء؟',
         'العازل المعلق المركب—والمعروف في قطاع نقل الكهرباء باسم العازل البوليمري أو عازل السيليكون طويل الساق (Long-Rod)—هو '
         'جهاز عزل ميكانيكي وكهربائي عالي الجهد صُمم لتعليق أسلاك خطوط النقل الهوائية المشحونة بالكهرباء وحمل أوزانها الشديدة '
         'مع توفير عزل ديزلكتريكي تام لمنع انتقال التيار إلى جسم البرج المعدني المؤرض. '
         'ويُستخدم العازل على نطاق واسع في شبكات النقل: '
         '<ul>'
         '<li><strong>1. على أبراج التعليق المستقيمة (Suspension Towers):</strong> يُعلق رأسياً أسفل ذراع البرج ليحمل الوزن الرأسي الثقيل لموصلات الألمنيوم '
         'المسلحة بالفولاذ (ACSR) ويتحمل القوى الجانبية الناتجة عن الرياح.</li>'
         '<li><strong>2. على أبراج الشد والزوايا ونهايات الخطوط (Tension / Dead-End Towers):</strong> يُركب أفقياً ليتحمل كامل قوى الشد الميكانيكية للخط '
         '(من 70kN إلى 160kN) عند المنعطفات الحادة ومعابر الأنهار والبحيرات والطرق السريعة.</li>'
         '<li><strong>3. في البيئات الساحلية والصحراوية الملوثة:</strong> حيث يمنع تماماً ظاهرة الوميض الكهربائي التي تعاني منها عوازل الخزف والزجاج.</li>'
         '</ul>'),
        ('لماذا حلت عوازل السيليكون المركبة محل سلاسل أطباق الزجاج والخزف القديمة؟',
         'لعقود طويلة، اعتمدت خطوط الجهد العالي على سلاسل مكونة من أطباق الزجاج المقسى أو البورسلين. '
         'وقد أصبحت العوازل المركبة المعيار العالمي الحديث لأربعة أسباب هندسية فارقة: '
         '<ul>'
         '<li><strong>1. خفة الوزن الهائلة (أخف بنسبة 85%):</strong> تزن سلسلة الزجاج لجهد 110kV نحو 50 كجم، بينما لا يتجاوز وزن العازل المركب المكافئ 6 كجم، '
         'مما يسهل رفعه وتركيبه يدوياً ويقلل أوزان أذرع الأبراج الحديدية.</li>'
         '<li><strong>2. خاصية طرد الماء ومقاومة وميض التلوث:</strong> سطح السيليكون طارد طبيعي للماء (Hydrophobic) ويفرز زيوتاً ميكروسكوبية تنفذ '
         'إلى ذرات الغبار والأملاح، مما يجعل الماء يتجمع على شكل قطرات معزولة تمنع تشكل مسار مائي موصل، ملغيةً الحاجة لغسيل العوازل تماماً.</li>'
         '<li><strong>3. مقاومة الكسر والتخريب:</strong> لا ينكسر أو يتشظى عند اصطدامه بالأحجار أو الرصاص أو أثناء النقل في الجبال والوعور.</li>'
         '<li><strong>4. انعدام العيوب الداخلية الخفية:</strong> لا يعاني من شروخ داخلية تثقبه كهربائياً وتتطلب فحوصات دورية مكلفة.</li>'
         '</ul>'),
        ('كيف يتحمل كبس النهايات المعدنية قوى شد عملاقة تتجاوز 100 كيلو نيوتن دون انزلاق القضيب الداخلي؟',
         'تُنفذ عملية الربط بين نهايات الصلب المطروق وقضيب الألياف الزجاجية بواسطة <strong>تقنية الكبس الدائري متعدد المحاور المُحوسب</strong>. '
         'حيث تضغط مكابس هيدروليكية فائقة الدقة معدن الصلب على القضيب مع مراقبة الانبعاث الصوتي الدقيق للتأكد من تداخل المعدن '
         'دون تكسير الألياف الزجاجية الداخلية، محققة صموداً ميكانيكياً خارقاً يفوق حمل الانهيار الاسمي (70kN أو 160kN) لعشرات السنين دون أي ارتخاء.')
    ],
    cta='هل تعمل على مد خطوط نقل الكهرباء الهوائية للجهد العالي، أو محطات التحويل الفرعية، أو مشاريع استبدال العوازل القديمة في البيئات الساحلية والصحراوية التي تتطلب عوازل تعليق مركبة معتمدة IEC 61109 (قوة 70kN إلى 160kN، جهد 11kV إلى 110kV)؟ تصنع يمين (YOMIN) عوازل FXBW بأعلى معايير المتانة.',
    body='''
<h2>القفزة التكنولوجية الكبرى في عزل خطوط نقل الطاقة الكهربائية للجهد العالي</h2>
<p>عبر شبكات نقل الكهرباء الإقليمية والوطنية العاملة بجهد <strong>33kV و 66kV و 110kV</strong>، تنقل الخطوط الهوائية طاقات كهربائية ضخمة عبر آلاف الكيلومترات من الصحاري والسهول والمناطق الساحلية الوعرة.</p>
<p>وعلى طول هذه المسارات الممتدة، تؤدي عوازل الخطوط وظيفتين مصيريتين في آن واحد: حمل أوزان موصلات الألمنيوم الثقيلة ومقاومة قوى الشد الميكانيكية العاتية للرياح والعواصف، مع ضمان عزل ديزلكتريكي صارم يمنع تسرب التيار إلى الأبراج الحديدية المؤرضة.</p>
<p>وعلى مدار أكثر من مئة عام، كانت سلاسل أطباق الزجاج المقسى أو الخزف هي الخيار الوحيد، غير أن وزنها الثقيل جداً وسرعة انكسارها وقابليتها للانهيار الكهربائي عند تراكم الأملاح والغبار شكل كابوساً تشغيلياً مستمراً لشركات الكهرباء.</p>
<p>يقدم <strong>العازل المعلق البوليمري المركب طويل الساق (سلسلة FXBW)</strong> الحل الهندسي القياسي المتفوق: عازل فائق الخفة والمتانة، مصنع من قضيب ألياف زجاجية عالي الشد ومكسو بمطاط السيليكون الطارد للمياه، ملغياً وميض التلوث ومخفضاً تكاليف النقل والتركيب بأكثر من 70%.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة عوازل FXBW المتطورة</h2>
<ol>
  <li><strong>قضيب ألياف زجاجية ECR عالي قوة الشد:</strong> يتحمل قوى شد تفوق 1,000 ميجا باسكال (أقوى من الفولاذ الإنشائي) ومقاوم كلياً للتآكل الإجهادي والتفتت الحمضي.</li>
  <li><strong>غلاف ومظلات من مطاط السيليكون HTV الطارد للماء:</strong> خاصية طرد مياه ميكروسكوبية ذاتية تمنع تكون المسارات الرطبة الموصلة للتيار وتلغي الحاجة لغسيل العوازل نهائياً.</li>
  <li><strong>تصميم مظلات أيروديناميكي ذو أقطار متبادلة:</strong> يمنح مسافة تسرب سطحية ممتازة (&ge; 31 مم/كيلوفولت) ويحفز التنظيف الذاتي للعازل بواسطة الرياح والأمطار.</li>
  <li><strong>نهايات صلب مطروق مجلفن على الساخن:</strong> مثبتة بكبس شعاعي دقيق للغاية لتحمل قوى شد اسمية تتراوح بين 70 و 160 كيلو نيوتن دون أي انزلاق.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1012 = [
    DTR_EN, DTR_FR, DTR_ES, DTR_AR,
    CSI_EN, CSI_FR, CSI_ES, CSI_AR
]
