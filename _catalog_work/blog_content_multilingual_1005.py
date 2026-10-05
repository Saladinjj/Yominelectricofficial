# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-05:
1. Capacitor Switching Contactor for APFC Panels (EN, FR, ES, AR)
2. Overhead Line Parallel Groove Clamps (PG Clamps) (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. CAPACITOR SWITCHING CONTACTOR (EN, FR, ES, AR)
# ==============================================================================

CSC_EN = dict(
    lang='en',
    dir='ltr',
    slug='apfc-capacitor-switching-what-is-a-capacitor-switching-contactor',
    title='Power Factor Correction & APFC Panels: What Is a Capacitor Switching Contactor?',
    breadcrumb='Circuit Breakers &amp; Protection',
    read='10 min read',
    alt='Heavy-duty three-phase Capacitor Switching Contactor (Model CJ19) operating inside an industrial Automatic Power Factor Correction (APFC) switchgear panel',
    desc=('Industrial Automatic Power Factor Correction (APFC) and capacitor bank inrush current protection: What is a capacitor switching contactor? '
          'How early-make auxiliary damping resistor blocks, AC-6b operational duty ratings, and microsecond arc quenching protect capacitors and eliminate contact welding.'),
    model='Model CJ19 / CJ19C Series AC Contactors for Switching Low-Voltage Power Capacitors (AC-6b Duty, 25A–95A, up to 50 kvar)',
    category='Circuit Breakers & Protection / Capacitor Switching Contactors',
    kw='what is a capacitor switching contactor &middot; capacitor switching contactor &middot; capacitor contactor &middot; apfc contactor &middot; cj19 contactor &middot; ac-6b contactor',
    specs=[
        ('Rated Operational Voltage & Frequency', 'Rated operational voltage (Ue): AC 380V / 400V / 415V / 690V at 50/60 Hz; insulation voltage (Ui): 690V / 1000V'),
        ('Controlled Power Capacitor Bank Capacity', 'Modular ratings controlling capacitor banks from 12.5 kvar, 20 kvar, 25 kvar, 30 kvar, up to 50 kvar (single or multi-stage APFC)'),
        ('Inrush Current Peak Suppression Ratio', 'Suppresses severe initial inrush current from &gt; 200 &times; In down to &le; 20–30 &times; In via leading damping wire coils'),
        ('Operational Utilization Category', 'Certified for IEC 60947-4-1 Utilization Category AC-6b (dedicated capacitive load switching, exceeding standard AC-3 motor duty)'),
        ('Early-Make Leading Contact Mechanism', 'Auxiliary contact block makes contact 2 to 5 milliseconds *before* main contacts, automatically disconnecting damping resistors once closed'),
        ('Damping Resistor Wire Loop Construction', 'Specialized high-temperature resistance alloy wire loops mounted on top housing, dissipating pre-charge transient energy safely'),
        ('Mechanical and Electrical Endurance Life', 'Mechanical life &ge; 1,000,000 operations; electrical life under full AC-6b rated capacitive duty &ge; 100,000 operations'),
        ('Applicable International Testing Standards', 'Fully compliant with IEC 60947-4-1, EN 60947-4-1, GB/T 14048.4, and CE low-voltage directives')
    ],
    faqs=[
        ('What is a Capacitor Switching Contactor and why can standard AC-3 motor contactors NOT be used for capacitor banks?',
         'A Capacitor Switching Contactor—commonly designated under international standards as an AC-6b duty contactor or APFC contactor—is '
         'a specialized electromagnetic contactor engineered with early-make auxiliary contacts and inrush-limiting damping resistors to safely switch low-voltage power factor correction capacitors. '
         'Standard general-purpose contactors (designed for AC-3 inductive motor loads) suffer catastrophic failure when connected to capacitors for three physical reasons: '
         '<ul>'
         '<li><strong>1. Massive Initial Inrush Current ($200 \times I_n$):</strong> At the instant of voltage switch-on, an uncharged capacitor acts as a pure electrical short-circuit. '
         'The resulting inrush current can spike to between 100 and 200 times the capacitor\'s rated nominal current within a fraction of a millisecond.</li>'
         '<li><strong>2. Contact Welding:</strong> Standard AC-3 contactor contacts experience contact bounce upon closing. '
         'Under a 200 $I_n$ surge, this micro-arcing instantly melts the silver-cadmium contacts, permanently welding them shut and preventing the stage from turning off.</li>'
         '<li><strong>3. Capacitor Dielectric Degradation & Voltage Surges:</strong> High-frequency inrush oscillations generate destructive transient overvoltages '
         'that puncture metallized polypropylene capacitor film, blow upstream branch fuses, and disrupt sensitive PLCs and variable frequency drives on the same bus.</li>'
         '</ul>'
         'Capacitor contactors eliminate these hazards by routing the initial surge through current-limiting damping resistors milliseconds before the main contacts touch.'),
        ('How does the two-stage early-make contact mechanism physically suppress capacitor inrush current?',
         'The operation of an advanced capacitor contactor (such as the YOMIN CJ19 series) follows an exact mechanical timing sequence during each closing cycle: '
         '<ul>'
         '<li><strong>Stage 1 (Pre-Charge via Damping Resistors):</strong> When the contactor coil energizes, mechanical linkages cause the top-mounted '
         'auxiliary contact block to close approximately 2 to 5 milliseconds <em>before</em> the main power contacts touch. '
         'The incoming AC power flows through looped high-resistance damping wires into the capacitor bank. '
         'These resistors act as an instantaneous buffer, absorbing the peak surge energy and capping the inrush current below 20 to 30 times rated current while pre-charging the capacitor.</li>'
         '<li><strong>Stage 2 (Main Contact Engagement & Resistor Disconnection):</strong> As the armature reaches full stroke, the heavy silver-nickel main power contacts close, '
         'carrying the full continuous operating current with near-zero contact resistance. '
         'Simultaneously, a spring-loaded mechanical release automatically separates the auxiliary contacts, completely disconnecting the damping resistors '
         'so they do not consume continuous power or overheat during normal steady-state operation.</li>'
         '</ul>'),
        ('How do you calculate and select the correct capacitor contactor rating for an APFC panel stage?',
         'Contactor sizing requires factoring in harmonic distortion and continuous overcurrent margins per IEC 60831: '
         '<ul>'
         '<li><strong>Standard 1.35x Safety Factor:</strong> Capacitor standards require equipment to withstand up to 130% continuous nominal current '
         'due to harmonic voltage distortion plus a 10% capacitor capacitance tolerance ($1.30 \times 1.10 \approx 1.43$).</li>'
         '<li><strong>Selection by kvar Rating:</strong> Always select the contactor directly by its AC-6b rated reactive power (kvar) at the operational voltage. '
         'For example, for a 25 kvar 400V capacitor step, specify a <strong>CJ19-43</strong> or <strong>CJ19-63</strong> rated for &ge; 25 kvar. '
         'Never size a capacitor contactor using standard AC-3 motor horsepower or kW charts, as doing so leads to severe undersizing and premature burnout.</li>'
         '</ul>')
    ],
    cta='Designing automatic power factor correction (APFC) panels, low-voltage capacitor banks, or reactive power switchboards requiring certified AC-6b capacitor switching contactors? YOMIN manufactures high-durability CJ19 / CJ19C contactors.',
    body='''
<h2>The Critical Challenge of Switching Power Factor Correction Capacitors</h2>
<p>In modern industrial manufacturing facilities, commercial office towers, and utility substations, inductive loads such as induction motors, HVAC chillers, and welding transformers consume substantial reactive power. This lowers the electrical <strong>power factor (PF)</strong>, triggering severe utility penalty charges, reducing transformer capacity, and causing excessive distribution line voltage drop.</p>
<p>To maintain a unity power factor (&ge; 0.95), facilities install <strong>Automatic Power Factor Correction (APFC) panels</strong>. These multi-stage switchboards continuously monitor the grid and step capacitor banks in and out of service as factory loads fluctuate.</p>
<p>However, energizing a power capacitor is among the most severe switching duties in electrical engineering. Without specialized control gear, switching inrush currents will instantly weld standard contactor contacts and destroy capacitor dielectric film.</p>
<p>The <strong>Capacitor Switching Contactor (Model CJ19 / CJ19C Series)</strong> provides the dedicated engineering solution: an AC-6b rated device that dampens inrush spikes by up to 90%, ensuring reliable, maintenance-free capacitor switching for millions of cycles.</p>

<h2>Engineering Anatomy: Inside a Dedicated AC-6b Capacitor Contactor</h2>
<ol>
  <li><strong>Top-Mounted Auxiliary Early-Make Contact Block:</strong> Features spring-loaded mechanical linkages that bridge the circuit 2–5 ms ahead of main contacts, absorbing the initial transient shock wave.</li>
  <li><strong>Looped High-Resistance Damping Wire Coils:</strong> Specialized nichrome or alloy damping loops connect across the auxiliary poles, converting the explosive inrush current pulse into safe, dissipated thermal energy.</li>
  <li><strong>Heavy-Duty Silver Alloy Main Contacts:</strong> High-purity silver-nickel or silver-tin-oxide contacts designed for maximum conductivity and minimal contact resistance under continuous capacitive load.</li>
  <li><strong>Automatic Resistor Disconnect Mechanism:</strong> Automatically breaks the auxiliary circuit after main contact closure, ensuring damping resistors remain cool and consume zero standby power during steady-state operation.</li>
  <li><strong>Arc-Quenching De-Ionizing Chamber:</strong> High-temperature thermoset arc chutes rapidly extinguish opening arcs, preventing restrike during capacitor de-energization.</li>
</ol>

<h2>Comparison: Capacitor Switching Contactor (AC-6b) vs. Standard AC-3 Motor Contactor</h2>
<table>
  <thead>
    <tr>
      <th>Comparison Parameter</th>
      <th>Standard AC-3 Motor Contactor</th>
      <th>YOMIN CJ19 Capacitor Switching Contactor (AC-6b)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Applicable IEC Load Category</strong></td>
      <td>AC-3 (Squirrel-cage motor starting &amp; running).</td>
      <td><strong>AC-6b (Low-voltage power capacitor bank switching).</strong></td>
    </tr>
    <tr>
      <td><strong>Peak Inrush Surge Handling</strong></td>
      <td>Direct undamped inrush: Spikes to 150–200 &times; In.</td>
      <td><strong>Pre-charge damped inrush: Suppressed to &le; 20–30 &times; In.</strong></td>
    </tr>
    <tr>
      <td><strong>Contact Welding Vulnerability</strong></td>
      <td>Extremely high; contacts frequently weld on first surge.</td>
      <td><strong>Zero contact welding; auxiliary contacts absorb peak surge.</strong></td>
    </tr>
    <tr>
      <td><strong>Capacitor Life Expectancy Impact</strong></td>
      <td>Severe; high-frequency voltage spikes degrade dielectric film.</td>
      <td><strong>Extends capacitor service life by up to 300%–400%.</strong></td>
    </tr>
    <tr>
      <td><strong>Auxiliary Damping Circuitry</strong></td>
      <td>None (Direct main terminal connection only).</td>
      <td><strong>Integrated early-make contacts + alloy damping wire loops.</strong></td>
    </tr>
    <tr>
      <td><strong>Grid Power Quality Impact</strong></td>
      <td>Creates severe line voltage dips and harmonics for PLCs/VFDs.</td>
      <td><strong>Smooth capacitive connection with negligible grid disturbance.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

CSC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='apfc-capacitor-switching-what-is-a-capacitor-switching-contactor-fr',
    title="Compensation d'Énergie Réactive & Armoires APFC : Qu'est-ce qu'un Contacteur pour Condensateurs ?",
    breadcrumb='Disjoncteurs &amp; Protection',
    read='10 min de lecture',
    alt='Contacteur pour condensateurs triphasé de forte puissance (Modèle CJ19) en service dans une armoire de compensation automatique',
    desc=('Armoires de compensation automatique d\'énergie réactive (APFC) et suppression des pointes de courant d\'enclenchement : Qu\'est-ce qu\'un contacteur pour condensateurs ? '
          'Comment les blocs de contacts auxiliaires avancés à résistances d\'amortissement, la catégorie d\'emploi AC-6b et l\'extinction d\'arc protègent les batteries de condensateurs.'),
    model='Série CJ19 / CJ19C : Contacteurs pour Enclenchement de Condensateurs de Puissance Basse Tension (Catégorie AC-6b, 25A à 95A, jusqu\'à 50 kvar)',
    category='Disjoncteurs & Protection / Contacteurs pour Condensateurs',
    kw='contacteur pour condensateurs &middot; contacteur condensateur &middot; contacteur cj19 &middot; contacteur ac-6b &middot; armoire apfc compensation',
    specs=[
        ('Tension Assignée d\'Emploi et Fréquence', 'Tension nominale de service (Ue) : AC 380V / 400V / 415V / 690V à 50/60 Hz ; tension d\'isolement (Ui) : 690V / 1000V'),
        ('Puissance Réactive Contrôlée de la Batterie', 'Calibres modulaires commandant des gradins de condensateurs de 12,5 kvar, 20 kvar, 25 kvar, 30 kvar, jusqu\'à 50 kvar'),
        ('Taux d\'Atténuation du Courant d\'Appel', 'Réduit la pointe initiale de courant d\'enclenchement de &gt; 200 &times; In à moins de 20 à 30 &times; In grâce aux boucles d\'amortissement'),
        ('Catégorie d\'Emploi Selon Norme CEI', 'Certifié selon la norme CEI 60947-4-1 en catégorie d\'emploi AC-6b (commutation spécifique de charges capacitives)'),
        ('Mécanisme de Contacts Auxiliaires Avancés', 'Bloc auxiliaire supérieur se fermant 2 à 5 millisecondes *avant* les pôles principaux, s\'ouvrant automatiquement une fois fermé'),
        ('Structure des Résistances d\'Amortissement', 'Boucles de fil résistif spécial à haute tenue thermique montées sur la tête de l\'appareil pour dissiper l\'énergie transitoire'),
        ('Endurance Mécanique et Électrique', 'Durée de vie mécanique &ge; 1 000 000 de manœuvres ; endurance électrique sous charge capacitive AC-6b &ge; 100 000 manœuvres'),
        ('Conformité aux Normes Internationales', 'Parfaitement conforme aux normes CEI 60947-4-1, EN 60947-4-1, GB/T 14048.4 et directives basse tension CE')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Contacteur pour Condensateurs et pourquoi un contacteur moteur AC-3 ordinaire est-il proscrit ?',
         'Un Contacteur pour Condensateurs—désigné dans les normes sous la catégorie d\'emploi AC-6b—est '
         'un contacteur électromagnétique spécialement équipé de contacts avancés à résistances de décharge pour commuter en toute sécurité les gradins de condensateurs. '
         'Un contacteur standard AC-3 (prévu pour les moteurs) subit une destruction rapide s\'il est raccordé à des condensateurs pour trois raisons : '
         '<ul>'
         '<li><strong>1. Courant d\'Appel Monstrueux (jusqu\'à 200 fois In) :</strong> À la mise sous tension, un condensateur déchargé se comporte comme un court-circuit franc. '
         'Le courant d\'appel atteint 150 à 200 fois le courant nominal en quelques microsecondes.</li>'
         '<li><strong>2. Soudure des Pôles Principaux :</strong> Lors de l\'enclenchement, les rebonds mécaniques créent des micro-arcs sous ce courant colossal. '
         'L\'alliage d\'argent fond instantanément, soudant définitivement les contacts entre eux.</li>'
         '<li><strong>3. Vieillissement Prématuré des Condensateurs :</strong> Ces oscillations violentes dégradent le film diélectrique en polypropylène '
         'et génèrent des surtensions destructrices pour les automates et variateurs du réseau.</li>'
         '</ul>'
         'Le contacteur pour condensateurs résout ce problème en dérivant le pic d\'enclenchement à travers des résistances d\'amortissement quelques millisecondes avant la fermeture principale.'),
        ('Comment fonctionne le mécanisme d\'enclenchement en deux temps ?',
         'Lors de l\'excitation de la bobine du contacteur CJ19, la cinématique s\'effectue en deux étapes précises : '
         '<ul>'
         '<li><strong>Étape 1 (Pré-charge amortie) :</strong> Le bloc auxiliaire supérieur s\'enclenche 2 à 5 ms avant les contacts principaux. '
         'Le courant transite par les fils résistifs qui absorbent l\'énergie d\'appel et limitent le courant à une valeur inoffensive.</li>'
         '<li><strong>Étape 2 (Fermeture principale et déconnexion) :</strong> Les contacts principaux massifs en argent se ferment pour porter le courant nominal permanent. '
         'Simultanément, un système mécanique déclenche l\'ouverture des contacts auxiliaires, isolant les résistances pour éviter tout échauffement continu.</li>'
         '</ul>'),
        ('Comment dimensionner un contacteur pour batterie de condensateurs ?',
         'Il convient d\'appliquer les règles de surdimensionnement de la norme CEI 60831 : '
         '<ul>'
         '<li><strong>Coefficient de Sécurité 1,35 :</strong> Prévoir une surintensité permanente de 30% liée aux harmoniques et 10% de tolérance de capacité.</li>'
         '<li><strong>Choix Direct en kvar :</strong> Sélectionner le contacteur directement selon sa puissance réactive assignée en kvar (ex. pour un gradin de 25 kvar à 400V, choisir un modèle CJ19-43 ou CJ19-63 adapté pour &ge; 25 kvar).</li>'
         '</ul>')
    ],
    cta='Vous concevez des armoires de compensation automatique d\'énergie réactive (APFC), des batteries de condensateurs ou des tableaux généraux basse tension ? YOMIN fabrique des contacteurs pour condensateurs CJ19 / CJ19C haute performance.',
    body='''
<h2>Le Défi Électrotechnique de la Commutation des Condensateurs de Puissance</h2>
<p>Dans les installations industrielles et tertiaires, les moteurs et transformateurs consomment une quantité importante d\'énergie réactive, dégradant le <strong>facteur de puissance (cos phi)</strong> et entraînant de lourdes pénalités de la part des distributeurs d\'énergie.</p>
<p>Pour rétablir le facteur de puissance au-dessus de 0,95, les usines déploient des <strong>armoires de compensation automatique (APFC)</strong> qui enclenchent des gradins de condensateurs au gré des variations de charge.</p>
<p>Cependant, l\'enclenchement d\'un condensateur de puissance produit un choc transitoire d\'une extrême violence qui soude instantanément les contacteurs conventionnels.</p>
<p>Le <strong>Contacteur Spécial Condensateurs (Série CJ19 / CJ19C)</strong> apporte la réponse technologique indispensable : un appareil certifié AC-6b qui étouffe le pic d\'enclenchement jusqu\'à 90%, garantissant une longévité exceptionnelle aux condensateurs et au tableau électrique.</p>

<h2>Conception et Éléments de Sécurité</h2>
<ol>
  <li><strong>Bloc Auxiliaire Supérieur à Fermeture Anticipée :</strong> S\'enclenche quelques millisecondes avant les pôles de puissance pour pré-charger le condensateur en douceur.</li>
  <li><strong>Résistances d\'Amortissement en Alliage Spécial :</strong> Boucles de fil résistif montées en tête qui absorbent l\'énergie d\'onde de choc sans chauffer.</li>
  <li><strong>Contacts Principaux en Alliage d\'Argent Renforcé :</strong> Assurent une conductivité optimale et un échauffement nul en régime permanent continu.</li>
  <li><strong>Mécanisme de Déconnexion Automatique des Résistances :</strong> Isole les résistances après fermeture principale pour économiser l\'énergie et éviter tout risque thermique.</li>
</ol>
'''
)

CSC_ES = dict(
    lang='es',
    dir='ltr',
    slug='apfc-capacitor-switching-what-is-a-capacitor-switching-contactor-es',
    title='Corrección del Factor de Potencia y Tableros APFC: ¿Qué es un Contactor para Condensadores?',
    breadcrumb='Disyuntores y Protección',
    read='10 min de lectura',
    alt='Contactor tripolar especial para bancos de condensadores (Modelo CJ19) operando en un tablero de corrección automática de factor de potencia',
    desc=('Tableros automáticos de corrección de factor de potencia (APFC) y supresión de picos de corriente de inserción: ¿Qué es un contactor para condensadores? '
          'Bloques de contactos auxiliares con resistencias de amortiguación, categoría de servicio AC-6b y extinción de arco para proteger bancos capacitivos.'),
    model='Serie CJ19 / CJ19C: Contactores Tripolares para Conmutación de Condensadores de Potencia en Baja Tensión (Servicio AC-6b, 25A a 95A, hasta 50 kvar)',
    category='Disyuntores y Protección / Contactores para Condensadores',
    kw='contactor para condensadores &middot; contactor de condensador &middot; contactor cj19 &middot; contactor ac-6b &middot; tablero apfc factor de potencia',
    specs=[
        ('Tensión Nominal de Servicio y Frecuencia', 'Tensión de empleo (Ue): AC 380V / 400V / 415V / 690V a 50/60 Hz; tensión de aislamiento (Ui): 690V / 1000V'),
        ('Capacidad de Banco de Condensadores Controlada', 'Modelos modulares para conmutar pasos de condensadores de 12,5 kvar, 20 kvar, 25 kvar, 30 kvar, hasta 50 kvar'),
        ('Atenuación del Pico de Corriente de Inserción', 'Reduce la corriente de conexión violenta de &gt; 200 &times; In a menos de 20 a 30 &times; In gracias a las resistencias de amortiguamiento'),
        ('Categoría de Utilización Internacional', 'Certificado bajo norma IEC 60947-4-1 en Categoría de Utilización AC-6b (conmutación específica de cargas capacitivas)'),
        ('Mecanismo de Contactos Auxiliares Adelantados', 'El bloque auxiliar superior cierra de 2 a 5 milisegundos *antes* que los polos principales, desconectándose al cerrar estos'),
        ('Diseño de las Resistencias de Amortiguación', 'Espirales de alambre de aleación resistiva para alta temperatura montadas en la parte superior para disipar la energía de choque'),
        ('Vida Útil Mecánica y Eléctrica Garantizada', 'Vida mecánica &ge; 1.000.000 de maniobras; vida eléctrica bajo servicio capacitivo AC-6b &ge; 100.000 maniobras'),
        ('Homologación y Cumplimiento Normativo', 'Totalmente conforme con normas internacionales IEC 60947-4-1, EN 60947-4-1, GB/T 14048.4 y directivas CE')
    ],
    faqs=[
        ('¿Qué es un Contactor para Condensadores y por qué NO se puede usar un contactor estándar de motor AC-3?',
         'Un Contactor para Condensadores—denominado bajo normas internacionales como contactor de servicio AC-6b—es '
         'un contactor electromagnético equipado con contactos auxiliares de cierre adelantado y resistencias disipadoras de choque. '
         'El uso de contactores comunes AC-3 (diseñados para motores) en bancos de condensadores provoca fallas destructivas inmediatas por tres causas: '
         '<ul>'
         '<li><strong>1. Corriente de Inserción Violenta (hasta 200 veces In):</strong> En el microsegundo de conexión, un condensador actúa como un cortocircuito perfecto. '
         'La corriente de conexión puede dispararse entre 100 y 200 veces la corriente nominal del banco.</li>'
         '<li><strong>2. Soldadura Inmediata de los Contactos:</strong> El rebote mecánico durante el cierre bajo este pico colosal genera microarcos que funden '
         'las pastillas de plata, soldando permanentemente los contactos e impidiendo la desconexión del paso.</li>'
         '<li><strong>3. Daño en el Dieléctrico del Condensador:</strong> Las ondas oscilatorias de alta frecuencia perforan el polipropileno metalizado del condensador, '
         'destruyendo su vida útil y perturbando los variadores y PLCs del tablero.</li>'
         '</ul>'
         'El contactor para condensadores soluciona esto desviando la corriente inicial a través de resistencias amortiguadoras milisegundos antes del cierre principal.'),
        ('¿Cómo funciona el mecanismo de cierre en dos etapas?',
         'Al energizarse la bobina del contactor CJ19, se activa una secuencia mecánica rigurosamente sincronizada: '
         '<ul>'
         '<li><strong>Etapa 1 (Pre-carga amortiguada):</strong> Los contactos auxiliares superiores se cierran entre 2 y 5 ms antes que los principales. '
         'La corriente ingresa a través de las resistencias de aleación que amortiguan el impacto y cargan el banco suavemente.</li>'
         '<li><strong>Etapa 2 (Cierre principal y desconexión de resistencias):</strong> Los contactos principales de plata cierran para conducir la corriente permanente. '
         'Al mismo tiempo, un resorte mecánico abre los contactos auxiliares, desconectando las resistencias para que no consuman energía ni se sobrecalienten.</li>'
         '</ul>'),
        ('¿Cómo seleccionar el contactor adecuado para un tablero APFC?',
         'La selección debe contemplar los márgenes de sobrecorriente por armónicos según norma IEC 60831: '
         '<ul>'
         '<li><strong>Factor de Seguridad 1,35:</strong> Considerar un 30% adicional por corrientes armónicas y 10% por tolerancia capacitiva.</li>'
         '<li><strong>Selección Directa en kvar:</strong> Escoger el contactor directamente por su potencia reactiva nominal en kvar (ej. para un paso de 25 kvar en 400V, seleccionar un modelo CJ19-43 o CJ19-63 especificado para &ge; 25 kvar).</li>'
         '</ul>')
    ],
    cta='¿Fabrica tableros automáticos de corrección de factor de potencia (APFC), bancos de condensadores en baja tensión o cuadros de maniobra industrial? YOMIN fabrica contactores para condensadores CJ19 / CJ19C de alta resistencia.',
    body='''
<h2>El Desafío Crítico en la Conmutación de Bancos de Condensadores</h2>
<p>En industrias manufactureras, complejos mineros y edificios comerciales, los motores y transformadores demandan una alta potencia reactiva, degradando el <strong>factor de potencia</strong> y generando severas penalizaciones en la factura eléctrica.</p>
<p>Para corregir este problema, se instalan <strong>tableros automáticos de corrección de factor de potencia (tableros APFC)</strong> que conectan y desconectan pasos capacitivos de forma automática.</p>
<p>Sin embargo, energizar un condensador representa una de las maniobras más severas de la electrotecnia: la corriente de inserción alcanza picos de hasta 200 veces la corriente nominal, soldando los contactores comunes al instante.</p>
<p>El <strong>Contactor para Condensadores (Serie CJ19 / CJ19C)</strong> proporciona la solución de ingeniería especializada: un equipo con categoría AC-6b que suprime hasta un 90% del pico transitorio, protegiendo los condensadores y asegurando maniobras libres de mantenimiento por cientos de miles de ciclos.</p>

<h2>Elementos de Diseño y Seguridad</h2>
<ol>
  <li><strong>Bloque Auxiliar Superior de Cierre Adelantado:</strong> Cierra microsegundos antes para amortiguar el choque inicial de tensión.</li>
  <li><strong>Espirales Resistivas de Aleación Especial:</strong> Absorben la energía transitoria de la inserción disipando el calor de forma segura.</li>
  <li><strong>Contactos Principales de Aleación de Plata Reforzada:</strong> Ofrecen máxima conductividad y mínima elevación de temperatura en servicio permanente.</li>
  <li><strong>Desconexión Mecánica Automática de las Resistencias:</strong> Evita que las resistencias queden conectadas bajo carga continua, eliminando pérdidas de energía.</li>
</ol>
'''
)

CSC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='apfc-capacitor-switching-what-is-a-capacitor-switching-contactor-ar',
    title='تحسين معامل القدرة ولوحات المكثفات الآلية (APFC): ما هو كونتاكتور تبديل المكثفات؟',
    breadcrumb='القواطع الكهربائية والحماية',
    read='10 دقائق قراءة',
    alt='كونتاكتور كهرومغناطيسي خاص بتبديل مكثفات تحسين القدرة (موديل CJ19) يعمل داخل لوحة توزيع وتحسين معامل القدرة',
    desc=('لوحات تحسين معامل القدرة الآلية (APFC) وإخماد تيارات الاندفاع الفائقة للمكثفات: ما هو كونتاكتور تبديل المكثفات؟ '
          'كيف تحمي كتل التلامس المسبق ذات مقاومات التخميد وتصنيف فئة التشغيل AC-6b مكثفات القدرة وتمنع التحام نقاط التلامس بالحرارة.'),
    model='سلسلة CJ19 / CJ19C: كونتاكتورات تبديل مكثفات القدرة منخفضة الجهد المعتمدة لفئة التشغيل AC-6b (سعات 25A إلى 95A، حتى 50 كفار)',
    category='القواطع والحماية / كونتاكتورات تبديل المكثفات',
    kw='كونتاكتور مكثفات &middot; capacitor contactor &middot; كونتاكتور cj19 &middot; كونتاكتور ac-6b &middot; لوحة تحسين معامل القدرة apfc',
    specs=[
        ('جهد التشغيل الاسمي والتردد المعتمد', 'جهد التشغيل الاسمي (Ue): AC 380V / 400V / 415V / 690V بتردد 50/60 هرتز؛ جهد العزل (Ui): 690V / 1000V'),
        ('سعة بنك المكثفات المحكوم بالكيلوفار', 'طرازات معيارية تتحكم في درجات بنوك المكثفات من 12.5، 20، 25، 30، وحتى 50 كيلوفار (kvar)'),
        ('نسبة كبح تيار الاندفاع الأولي الهائل', 'تخفيض تيار الاندفاع الأولي الفائق من أكثر من 200 &times; In إلى أقل من 20 إلى 30 &times; In عبر مقاومات التخميد'),
        ('فئة الاستخدام والتشغيل القياسية الدولية', 'معتمد طبقاً للمواصفة القياسية الدولية IEC 60947-4-1 تحت فئة الاستخدام AC-6b المخصصة للأحمال السعوية'),
        ('آلية التلامس المسبق المبكر الدقيقة', 'كتلة التلامس المساعد العلوية تغلق مسبقاً بفارق 2 إلى 5 أجزاء من الألف من الثانية قبل تلامس الأقطاب الرئيسية'),
        ('هيكل مقاومات التخميد الحرارية', 'حلقات سلكية من سبائك النيكل كروم المقاومة لدرجات الحرارة المرتفعة مثبتة في الرأس لامتصاص الصدمة العابرة'),
        ('العمر الافتراضي الميكانيكي والكهربائي', 'عمر تشغيل ميكانيكي &ge; 1,000,000 مناورة؛ وعمر كهربائي تحت الحمل السعوي الاسمي AC-6b &ge; 100,000 مناورة'),
        ('المعايير الدولية وشهادات الاختبار', 'مطابق كلياً للمواصفات الدولية IEC 60947-4-1 و EN 60947-4-1 و GB/T 14048.4 والتوجيهات الأوروبية CE')
    ],
    faqs=[
        ('ما هو كونتاكتور تبديل المكثفات ولماذا لا يمكن استخدام كونتاكتورات المحركات العادية (AC-3) لبنوك المكثفات؟',
         'كونتاكتور تبديل المكثفات—والمصنف دولياً تحت فئة التشغيل AC-6b—هو '
         'كونتاكتور كهرومغناطيسي متخصص مزود بنقاط تلامس مساعدة تسبق التلامس الرئيسي ومقاومات سلكية لكبح تيارات الاندفاع العالية. '
         'إن استخدام كونتاكتورات المحركات العادية فئة AC-3 مع المكثفات يؤدي إلى انهيار كارثي سريع للأسباب التالية: '
         '<ul>'
         '<li><strong>1. تيار اندفاع أولي مدمر (يصل إلى 200 ضعف التيار الاسمي):</strong> في لحظة التوصيل، يتصرف المكثف الفارغ كدائرة قصر تامة، '
         'مما يولد تيار اندفاع هائل يتراوح بين 100 و 200 ضعف التيار المقنن في أجزاء من المليثانية.</li>'
         '<li><strong>2. التحام وانصهار نقاط التلامس (Contact Welding):</strong> يؤدي ارتداد الملامسات الميكانيكية تحت هذا التيار الرهيب إلى تولد شرارات '
         'تصهر نقاط التلامس الفضية وتلحمها ببعضها بصورة دائمة، مما يمنع فصل المكثف ويسبب احتراقه.</li>'
         '<li><strong>3. تلف عازل المكثفات وتدهور شبكة المصنع:</strong> تتسبب الموجات الترددية العنيفة في ثقب عازل البولي بروبيلين داخل المكثفات '
         'وتوليد قفزات جهدية تشوش على شاشات التحكم والمغيرات الترددية (Inverters) في المصنع.</li>'
         '</ul>'
         'يقضي كونتاكتور المكثفات على هذا الخطر بتمرير التيار الأولي عبر مقاومات تخميد قبل التوصيل الرئيسي بمليثوان معدودة.'),
        ('كيف تعمل آلية التوصيل المبكر على مرحلتين لإخماد التيار؟',
         'تتم عملية الإغلاق في كونتاكتور CJ19 وفق تتابع زمني ميكانيكي هندسي فائق الدقة: '
         '<ul>'
         '<li><strong>المرحلة الأولى (الشحن المسبق المخمد):</strong> تغلق نقاط التلامس المساعدة العلوية قبل نقاط التلامس الرئيسية بفارق 2 إلى 5 مليثانية. '
         'يمر التيار عبر الأسلاك المقاومة التي تمتص الصدمة العابرة وتشحن المكثف بهدوء دون قفزات مفاجئة.</li>'
         '<li><strong>المرحلة الثانية (التوصيل الرئيسي وفصل المقاومات):</strong> تغلق نقاط التلامس الرئيسية المصنوعة من سبائك الفضة لتحمل تيار التشغيل الدائم. '
         'وفي نفس اللحظة، تفصل آلية نوابض ميكانيكية نقاط التلامس المساعدة تماماً، مما يخرج مقاومات التخميد من الدائرة لمنع استهلاكها للطاقة أو سخونتها.</li>'
         '</ul>'),
        ('كيف يتم اختيار سعة كونتاكتور المكثفات للوحة تحسين معامل القدرة (APFC)؟',
         'يجب مراعاة تيارات التوافقيات طبقاً للمواصفة القياسية IEC 60831: '
         '<ul>'
         '<li><strong>معامل أمان 1.35:</strong> مراعاة زيادة بنسبة 30% لتيارات التوافقيات و 10% لتفاوت سعة المكثفات المصنعية.</li>'
         '<li><strong>الاختيار المباشر بالكيلوفار (kvar):</strong> اختيار مقاس الكونتاكتور مباشرة حسب السعة المقننة لدرجة المكثف بالكيلوفار (مثلاً لدرجة مكثف 25 كفار على جهد 400V، يتم اختيار موديل CJ19-43 أو CJ19-63 المخصص لـ 25 كفار أو أكثر).</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع لوحات تحسين معامل القدرة الآلية (APFC)، أو بنوك المكثفات الصناعية، أو لوحات التوزيع منخفضة الجهد؟ تصنع يمين (YOMIN) كونتاكتورات تبديل المكثفات CJ19 / CJ19C عالية الاعتمادية.',
    body='''
<h2>التحدي الكهروميكانيكي الأبرز في تشغيل بنوك مكثفات تحسين القدرة</h2>
<p>في المنشآت الصناعية والمصانع والمباني التجارية الكبرى، تسحب المحركات الحثية والمحولات كميات هائلة من الطاقة غير الفعالة (Reactive Power)، مما يؤدي إلى انخفاض <strong>معامل القدرة (Power Factor)</strong> وفرض غرامات مالية باهظة من شركات الكهرباء.</p>
<p>ولرفع معامل القدرة إلى المستوى المثالي (&ge; 0.95)، تعتمد المصانع على <strong>لوحات تحسين معامل القدرة الآلية (APFC)</strong> التي تقوم بتبديل درجات بنوك المكثفات أوتوماتيكياً حسب تذبذب أحمال المصنع.</p>
<p>ومع ذلك، فإن إدخال مكثف كهربائي في الشبكة يمثل صدمة ميكانيكية وكهربائية عنيفة قد تؤدي لالتحام أقطاب الكونتاكتورات العادية وانفجارها.</p>
<p>يمثل <strong>كونتاكتور تبديل المكثفات (سلسلة CJ19 / CJ19C)</strong> الحل الهندسي القياسي الحاسم: جهاز معتمد بفئة AC-6b يخمد صدمة تيار الاندفاع بنسبة 90%، مما يحمي المكثفات ويضمن تشغيلاً آمناً لملايين المناورات دون صيانة.</p>

<h2>المكونات الهندسية وميزات الأمان المتطورة</h2>
<ol>
  <li><strong>كتلة تلامس مساعدة علوية مبكرة:</strong> تغلق قبل الملامسات الرئيسية بأجزاء من الثانية لامتصاص صدمة الشحن الأولى.</li>
  <li><strong>حلقات سلكية من سبائك النيكل كروم المقاومة:</strong> تحول طاقة الصدمة الكهربائية إلى طاقة حرارية مخمدة بشكل آمن وفوري.</li>
  <li><strong>أقطاب رئيسية من سبائك الفضة عالية النقاوة:</strong> تضمن أدنى مقاومة تلامس وتمنع ارتفاع درجات الحرارة أثناء التشغيل الدائم.</li>
  <li><strong>آلية الفصل الميكانيكي التلقائي للمقاومات:</strong> تفصل مقاومات التخميد بمجرد استقرار التوصيل لمنع هدر الطاقة وضمان برودة الجهاز.</li>
</ol>
'''
)

# ==============================================================================
# 2. PARALLEL GROOVE CLAMP (PG CLAMP) (EN, FR, ES, AR)
# ==============================================================================

PGC_EN = dict(
    lang='en',
    dir='ltr',
    slug='overhead-line-tapping-what-is-a-parallel-groove-clamp',
    title='Overhead Line Tapping & Hardware: What Is a Parallel Groove Clamp (PG Clamp)?',
    breadcrumb='Terminals &amp; Connectors',
    read='10 min read',
    alt='Heavy-duty two-bolt aluminium Parallel Groove Clamp (PG Clamp Model JB) installed on an outdoor overhead power distribution utility pole crossarm',
    desc=('Overhead transmission and distribution non-tension connections: What is a parallel groove clamp (PG clamp)? '
          'How extruded aluminium alloy bodies, friction-welded copper-aluminium bimetallic plates, and Belleville spring washers prevent galvanic corrosion and thermal joint failure.'),
    model='Model JB / CAPG Series Aluminium and Bimetallic Parallel Groove Clamps (Main/Tap Range: 16 mm² to 300 mm²)',
    category='Terminals & Connectors / Parallel Groove Clamps',
    kw='what is a parallel groove clamp &middot; parallel groove clamp &middot; pg clamp &middot; bimetallic pg clamp &middot; capg clamp &middot; overhead line clamp',
    specs=[
        ('Applicable Overhead Conductor Types', 'Bare all-aluminium conductors (AAC), aluminium conductor steel reinforced (ACSR), aluminium alloy (AAAC), and copper conductors'),
        ('Conductor Cross-Section Accommodation', 'Accommodates main run and branch tap conductors from 16 mm&sup2;, 25 mm&sup2;, 50 mm&sup2;, 70 mm&sup2;, 120 mm&sup2;, up to 300 mm&sup2; (equal and transition sizes)'),
        ('Clamp Body Material & Manufacturing', 'High-strength, corrosion-resistant cast or extruded aluminium alloy (Al &ge; 99.5%) with precision-contoured parallel conductor grooves'),
        ('Bimetallic Transition Technology (CAPG)', 'Friction-welded or hot-rolled electrolytic copper sheet lining metallurgically bonded to one groove for aluminium-to-copper tap connections'),
        ('Bolt Hardware & Tensile Strength Grade', 'Hot-dip galvanized high-tensile carbon steel (Grade 8.8) or stainless steel bolts (1, 2, or 3 bolts depending on current rating)'),
        ('Dynamic Thermal Expansion Compensation', 'Fitted with concave conical Belleville spring washers beneath bolt nuts to maintain constant contact pressure through heating/cooling cycles'),
        ('Electrical Conductivity & Temperature Rise', 'Contact electrical resistance lower than equivalent length of conductor; joint temperature rise lower than adjacent conductor under load'),
        ('Standards Compliance & Testing', 'Compliant with IEC 61284, BS 3288, ANSI C119.4 Class A, and EN 50483-4 for overhead line non-tension fittings')
    ],
    faqs=[
        ('What is a Parallel Groove Clamp (PG Clamp) and what specific role does it perform in overhead power lines?',
         'A Parallel Groove Clamp—universally abbreviated by linemen and transmission engineers as a PG Clamp—is '
         'a bolt-tightened electrical mechanical connector featuring two parallel longitudinal grooves designed to join two parallel overhead conductors. '
         'In electrical power transmission and distribution networks, conductors must frequently be tapped or bridged without severing the main wire: '
         '<ul>'
         '<li><strong>1. Transformer & Equipment Taps:</strong> Branching down-leads from the overhead main feeder line down to pole-mounted distribution transformers, '
         'surge arresters, and drop-out fuse cutouts.</li>'
         '<li><strong>2. Jumper Loops at Strain Poles:</strong> Bridging the electrical circuit around dead-end tension insulator assemblies at corner and terminal poles.</li>'
         '<li><strong>3. Mid-Span Tap Lines:</strong> Tapping rural branch lines off an existing medium-voltage or low-voltage trunk circuit.</li>'
         '</ul>'
         'Because PG clamps are non-tension connectors (used where the conductors are slack or held by strain insulators), '
         'their primary engineering mission is electrical: providing an ultra-low-resistance, permanent electrical bond that withstands outdoor weather '
         'without developing high-resistance hotspots.'),
        ('Why are bimetallic PG clamps (Al-Cu / CAPG) essential when connecting aluminium conductors to copper equipment?',
         'When aluminium and copper metals come into direct physical contact in the presence of outdoor atmospheric moisture (electrolyte), '
         'an electrochemical reaction called <strong>galvanic corrosion</strong> occurs. '
         'Aluminium is far more electronegative (-1.66V standard potential) than copper (+0.34V). '
         'In direct contact, the aluminium rapidly sacrifices itself: it oxidizes, pits, and disintegrates into white powder. '
         'Within months, the joint loses electrical contact, overheats, and burns off. '
         'Bimetallic PG clamps (Model CAPG series) solve this by metallurgically bonding a pure electrolytic copper liner into one groove '
         'using molecular friction welding. The aluminium main conductor rests entirely in the aluminium groove; '
         'the copper branch conductor rests entirely in the copper-lined groove. '
         'Because the copper-aluminium interface inside the clamp body is molecularly welded without air or moisture gaps, galvanic corrosion is completely prevented.'),
        ('Why are conical Belleville spring washers mandatory on PG clamp clamping bolts?',
         'During daily operation, overhead distribution lines undergo dramatic temperature swings: '
         'solar radiation and heavy peak electrical loads heat conductors up to 75&deg;C–90&deg;C, followed by cooling down to ambient night temperatures. '
         'Aluminium expands at approximately twice the rate of the steel clamping bolts ($23 \times 10^{-6}/\text{K}$ for aluminium vs $12 \times 10^{-6}/\text{K}$ for steel). '
         'Under heat, the expanding aluminium would deform plastically against a rigid bolt. '
         'When the line cools, the conductor shrinks, leaving the connection loose. '
         'A loose connection has high contact resistance, leading to rapid thermal runaway and joint burnout. '
         'Belleville spring washers act as mechanical energy reservoirs: they flex elastically to absorb the thermal expansion during peak load '
         'and push back continuously during cooling, maintaining constant, calibrated clamping pressure over decades of service.')
    ],
    cta='Procuring low-voltage and medium-voltage overhead line hardware, aluminium parallel groove clamps (JB Series), or bimetallic copper-aluminium PG clamps (CAPG Series) compliant with IEC 61284? YOMIN manufactures forged PG clamps.',
    body='''
<h2>The Essential Non-Tension Tapping Fitting for Overhead Power Lines</h2>
<p>Along thousands of kilometers of medium-voltage and low-voltage overhead transmission and distribution lines, electrical energy must be branched, tapped, and transferred around insulator assemblies. Unlike dead-end anchor clamps that bear tons of pulling tension, these jumper and equipment tap connections are non-tension connections.</p>
<p>However, an overhead electrical connection must endure decades of severe environmental exposure: harsh solar UV radiation, high-velocity wind vibration, thermal load cycling, and corrosive atmospheric pollutants.</p>
<p>The <strong>Parallel Groove Clamp (PG Clamp / Model JB &amp; CAPG Series)</strong> is the internationally standardized connector developed to provide a secure, high-conductivity, solderless electrical connection between parallel overhead conductors.</p>

<h2>Engineering Anatomy: Inside a Certified Parallel Groove Clamp</h2>
<ol>
  <li><strong>Precision-Grooved Aluminium Body:</strong> Molded or extruded from high-purity aluminium alloy (Al &ge; 99.5%). The parallel grooves feature precision radii that cradle the circular stranded conductor, maximizing contact surface area and preventing strand crushing.</li>
  <li><strong>Friction-Welded Bimetallic Lining (CAPG Series):</strong> A plate of pure electrolytic copper is friction-welded into the tap groove, preventing lethal galvanic oxidation when tapping copper leads off aluminium main conductors.</li>
  <li><strong>Grade 8.8 High-Tensile Steel Bolts:</strong> Hot-dip galvanized clamping bolts (with minimum 85 &mu;m zinc coating) deliver massive clamping torque without thread stripping.</li>
  <li><strong>Belleville Conical Spring Washers:</strong> High-resilience spring washers absorb differential thermal expansion between the aluminium clamp body and steel bolts, maintaining constant contact force through seasonal thermal cycles.</li>
  <li><strong>Anti-Corrosive Neutral Contact Grease:</strong> Factory-coated grooves filled with neutral petrolatum antioxidant compound containing silica particles to break down aluminium surface oxide films.</li>
</ol>

<h2>Comparison: Parallel Groove Clamp vs. Split-Bolt Connector vs. Wedge Tap Connector</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>Mechanical Split-Bolt Connector</th>
      <th>YOMIN Parallel Groove Clamp (JB / CAPG)</th>
      <th>Explosive / Mechanical Wedge Tap Connector</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Conductor Alignment & Seating</strong></td>
      <td>Perpendicular crossing; pinches wires at single contact point.</td>
      <td><strong>Parallel longitudinal grooves; wide contact surface area.</strong></td>
      <td>C-shaped member with driven wedge.</td>
    </tr>
    <tr>
      <td><strong>Aluminium to Copper Tapping</strong></td>
      <td>Requires loose bi-metal washers (prone to misalignment).</td>
      <td><strong>Integrated friction-welded copper liner (CAPG series).</strong></td>
      <td>Requires specialized bimetallic cartridges.</td>
    </tr>
    <tr>
      <td><strong>Thermal Cycling Compensation</strong></td>
      <td>None (Threaded nut loosens over thermal cycles).</td>
      <td><strong>Belleville conical spring washers maintain constant pressure.</strong></td>
      <td>Spring action of C-body maintains force.</td>
    </tr>
    <tr>
      <td><strong>Installation & Reusability</strong></td>
      <td>Requires wrenches; threads often gall or strip.</td>
      <td><strong>Standard socket wrench; fully removable and reusable.</strong></td>
      <td>Requires explosive powder gun or specialized tool; single-use.</td>
    </tr>
    <tr>
      <td><strong>Conductor Damage Risk</strong></td>
      <td>High; narrow bolt edges easily sever outer conductor strands.</td>
      <td><strong>Zero strand damage; smooth contoured groove radius.</strong></td>
      <td>Can shear strands if wedge is overdriven.</td>
    </tr>
  </tbody>
</table>
'''
)

PGC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='overhead-line-tapping-what-is-a-parallel-groove-clamp-fr',
    title="Lignes Aériennes & Raccordements : Qu'est-ce qu'un Raccord à Gorge Parallèle (Pince PG) ?",
    breadcrumb='Bornes &amp; Connecteurs',
    read='10 min de lecture',
    alt='Raccord à gorge parallèle en aluminium à deux boulons (Pince PG Modèle JB) installé sur une traverse de poteau de ligne aérienne',
    desc=('Lignes aériennes de transport et distribution électrique et raccordements hors traction : Qu\'est-ce qu\'un raccord à gorge parallèle (pince PG) ? '
          'Corps en aluminium extrudé, plaques bimétalliques cuivre-alu soudées par friction et rondelles élastiques Belleville contre la corrosion galvanique.'),
    model='Série JB / CAPG : Raccords à Gorge Parallèle en Aluminium et Bimétalliques Cuivre-Alu (Capacité : 16 mm² à 300 mm²)',
    category='Bornes & Connecteurs / Raccords à Gorge Parallèle',
    kw='pince pg &middot; raccord à gorge parallèle &middot; connecteur pg &middot; raccord bimétallique capg &middot; pince de dérivation aérienne',
    specs=[
        ('Types de Conducteurs Aériens Compatibles', 'Conducteurs nus en aluminium (AAC), aluminium-acier (ACSR), alliage d\'aluminium (ASTER/AAAC) et cuivre'),
        ('Capacité de Serrage des Conducteurs', 'Accepte les conducteurs principaux et dérivés de 16, 25, 50, 70, 120 jusqu\'à 300 mm&sup2; (sections identiques ou étagées)'),
        ('Matériau du Corps et Procédé de Fabrication', 'Alliage d\'aluminium haute résistance coulé ou extrudé (Al &ge; 99,5%) avec gorges longitudinales au profil du câble'),
        ('Technologie Bimétallique Anti-Corrosion (CAPG)', 'Feuille de cuivre électrolytique pure liée par soudage par friction dans la gorge dérivée pour raccordements alu-cuivre'),
        ('Boulonnerie et Classe de Résistance', 'Boulons en acier zingué au trempé à chaud (Classe 8.8) ou acier inoxydable (1, 2 ou 3 boulons selon l\'intensité)'),
        ('Compensation des Dilatations Thermiques', 'Équipé de rondelles élastiques coniques Belleville sous les écrous pour maintenir une pression de contact permanente'),
        ('Conductivité Électrique et Échauffement', 'Résistance de contact inférieure à celle d\'une longueur équivalente de conducteur ; échauffement maîtrisé sous charge'),
        ('Normes et Essais de Qualification Réseau', 'Conforme aux normes internationales CEI 61284, BS 3288, ANSI C119.4 Classe A et EN 50483-4 pour ferrures aériennes')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Raccord à Gorge Parallèle (Pince PG) et à quoi sert-il sur une ligne aérienne ?',
         'Un Raccord à Gorge Parallèle—universellement appelé par les lignards et monteurs Pince PG (Parallel Groove Clamp)—est '
         'un connecteur électrique mécanique à boulons comportant deux rainures parallèles profilées pour réunir deux conducteurs électriques. '
         'Sur les réseaux de transport et de distribution aériens, il remplit trois fonctions de dérivation hors traction : '
         '<ul>'
         '<li><strong>1. Raccordement des Équipements :</strong> Dérivation des conducteurs descendants vers les transformateurs de distribution sur poteau, '
         'parafoudres et coupe-circuits à expulsion.</li>'
         '<li><strong>2. Boucles de Shunt (Jumpers) :</strong> Assurer la continuité électrique entre deux portées au niveau des chaînes d\'ancrage d\'angle.</li>'
         '<li><strong>3. Antennes et Dérivations :</strong> Piquer une ligne secondaire sur une artère principale sans couper le conducteur passant.</li>'
         '</ul>'
         'Ne subissant pas la traction mécanique du câble, sa mission est purement électrique : offrir un contact à très faible résistance qui ne s\'échauffe pas.'),
        ('Pourquoi les pinces PG bimétalliques (alu-cuivre / CAPG) sont-elles indispensables pour raccorder l\'aluminium au cuivre ?',
         'Lorsque l\'aluminium et le cuivre sont en contact direct sous la pluie ou l\'humidité, il se produit une réaction électrochimique redoutable : '
         'la <strong>corrosion galvanique</strong>. L\'aluminium étant beaucoup plus électronégatif que le cuivre, il s\'oxyde et se désagrège en poudre blanche. '
         'En quelques mois, le raccordement chauffe et la ligne se coupe. '
         'Les pinces bimétalliques CAPG résolvent ce phénomène en intégrant dans la gorge dérivée une feuille de cuivre pur soudée par friction moléculaire au corps alu. '
         'Le câble alu repose dans la gorge alu, et le câble cuivre repose dans la gorge cuivre. L\'interface cuivre-alu étant hermétiquement scellée en usine, '
         'aucune corrosion galvanique ne peut survenir.'),
        ('Pourquoi les rondelles coniques Belleville sont-elles obligatoires sur les boulons de serrage ?',
         'Avec les variations de charge et l\'ensoleillement, l\'aluminium se dilate deux fois plus vite que l\'acier des boulons. '
         'Sans rondelle ressort, l\'aluminium subirait un écrasement plastique sous la chaleur, puis se retrouverait desserré au refroidissement. '
         'Un raccord desserré s\'échauffe par effet Joule et fond rapidement. '
         'Les rondelles Belleville agissent comme des ressorts de puissance : elles absorbent la dilatation thermique et maintiennent une pression de serrage '
         'rigoureusement constante pendant des décennies.')
    ],
    cta='Vous déployez des réseaux électriques aériens moyenne et basse tension, des dérivations de transformateurs ou recherchez des pinces PG bimétalliques conformes CEI 61284 ? YOMIN fabrique des raccords à gorge parallèle forgés haute fiabilité.',
    body='''
<h2>Le Connecteur de Dérivation par Excellence pour Lignes Aériennes</h2>
<p>Sur les réseaux de distribution d\'électricité aériens en conducteurs nus, les lignes doivent fréquemment être pontées, dérivées ou raccordées aux transformateurs et parafoudres. Contrairement aux pinces d\'ancrage qui supportent la traction du câble, ces liaisons électriques sont dites hors traction.</p>
<p>Cependant, ces connexions doivent résister aux pires agressions extérieures : vents violents, vibrations, cycles thermiques intenses et atmosphères corrosives.</p>
<p>Le <strong>Raccord à Gorge Parallèle (Pince PG / Séries JB et CAPG)</strong> est le raccord électromécanique normalisé conçu pour garantir un contact électrique irréprochable et démontable entre deux conducteurs parallèles.</p>

<h2>Conception et Éléments de Fiabilité</h2>
<ol>
  <li><strong>Corps en Alliage d\'Aluminium Profilé :</strong> Deux rainures parallèles épousant le rayon du câble pour maximiser la surface de contact sans écraser les brins.</li>
  <li><strong>Revêtement Bimétallique Cuivre Soudé par Friction (Série CAPG) :</strong> Empêche la corrosion galvanique destructrice lors du raccordement d\'un câble cuivre sur une ligne alu.</li>
  <li><strong>Boulonnerie en Acier Galvanisé à Chaud Haute Résistance (Classe 8.8) :</strong> Permet un couple de serrage puissant et durable sans grippage.</li>
  <li><strong>Rondelles Ressorts Coniques Belleville :</strong> Compensent en continu les dilatations thermiques du métal pour empêcher tout desserrage dans le temps.</li>
</ol>
'''
)

PGC_ES = dict(
    lang='es',
    dir='ltr',
    slug='overhead-line-tapping-what-is-a-parallel-groove-clamp-es',
    title='Líneas Aéreas y Derivaciones Eléctricas: ¿Qué es una Grapa de Ranuras Paralelas (Grapa PG)?',
    breadcrumb='Terminales y Conectores',
    read='10 min de lectura',
    alt='Grapa de ranuras paralelas de aluminio de dos pernos (Grapa PG Modelo JB) instalada en cruceta de poste de distribución aérea',
    desc=('Líneas aéreas de transmisión y distribución eléctrica y derivaciones sin tensión mecánica: ¿Qué es una grapa de ranuras paralelas (grapa PG)? '
          'Cuerpos de aleación de aluminio extruido, láminas bimetálicas cobre-aluminio soldadas por fricción y arandelas Belleville contra la corrosión galvánica.'),
    model='Serie JB / CAPG: Grapas de Ranuras Paralelas en Aluminio y Bimetálicas Cobre-Aluminio (Capacidad: 16 mm² a 300 mm²)',
    category='Terminales y Conectores / Grapas de Ranuras Paralelas',
    kw='grapa pg &middot; grapa de ranuras paralelas &middot; conector pg &middot; grapa bimetalica capg &middot; derivacion linea aerea &middot; conector paralelo',
    specs=[
        ('Conductores Aéreos Compatibles', 'Conductores desnudos de aluminio (AAC), aluminio con alma de acero (ACSR), aleación de aluminio (AAAC) y cobre'),
        ('Rango de Sección Transversal de Cables', 'Acomoda conductores principales y derivados de 16, 25, 50, 70, 120 hasta 300 mm&sup2; (secciones iguales o de reducción)'),
        ('Material del Cuerpo y Fabricación', 'Aleación de aluminio forjado o extruido de alta pureza (&ge; 99,5%) con ranuras contorneadas al radio exacto del cable'),
        ('Tecnología Bimetálica Antigalvánica (CAPG)', 'Chapa de cobre electrolítico puro unida por soldadura por fricción en la ranura secundaria para uniones aluminio-cobre'),
        ('Bulonería y Calidad de Acero', 'Pernos de acero al carbono de alta resistencia (Grado 8.8) galvanizados en caliente (1, 2 o 3 pernos según calibre)'),
        ('Compensación Térmica Dinámica', 'Equipada con arandelas cónicas elásticas Belleville bajo las tuercas para mantener una presión constante ante ciclos de frío/calor'),
        ('Conductividad y Elevación de Temperatura', 'Resistencia de contacto eléctrica inferior a un tramo equivalente de cable continuo; baja temperatura en servicio pleno'),
        ('Normativas y Certificaciones Internacionales', 'Conforme con normas internacionales IEC 61284, BS 3288, ANSI C119.4 Clase A y EN 50483-4 para herrajes de líneas aéreas')
    ],
    faqs=[
        ('¿Qué es una Grapa de Ranuras Paralelas (Grapa PG) y cuál es su función en tendidos aéreos?',
         'Una Grapa de Ranuras Paralelas—abreviada internacionalmente por las distribuidoras como Grapa PG (Parallel Groove Clamp)—es '
         'un conector eléctrico apernado que cuenta con dos cavidades o ranuras longitudinales paralelas diseñadas para unir mecánicamente dos conductores. '
         'En redes aéreas de media y baja tensión cumple funciones de derivación y puenteo fuera de tracción mecánica: '
         '<ul>'
         '<li><strong>1. Bajadas a Transformadores y Equipos:</strong> Conectar las derivaciones hacia transformadores en poste, seccionadores y pararrayos.</li>'
         '<li><strong>2. Puentes de Retención (Puentes Jumper):</strong> Dar continuidad eléctrica alrededor de los aisladores de retención en postes de esquina o fin de línea.</li>'
         '<li><strong>3. Tomas y Derivaciones en Vano:</strong> Derivar ramales secundarios sin necesidad de cortar el conductor principal pasante.</li>'
         '</ul>'
         'Al ser un conector sin tracción mecánica longitudinal, su misión primordial es eléctrica: garantizar una unión de bajísima resistencia que no se caliente.'),
        ('¿Por qué son indispensables las grapas PG bimetálicas (CAPG) para unir aluminio con cobre?',
         'Cuando el aluminio y el cobre se conectan en contacto directo bajo la humedad exterior, se desencadena una intensa <strong>corrosión galvánica</strong>. '
         'El aluminio actúa como ánodo de sacrificio, corroyéndose y destruyéndose rápidamente en forma de óxido blanco. '
         'En pocos meses, el empalme se sobrecalienta y el cable se corta. '
         'Las grapas bimetálicas CAPG solucionan esto integrando en una de las ranuras una chapa de cobre puro soldada por fricción molecular al cuerpo de aluminio. '
         'El cable de aluminio se aloja en la ranura de aluminio, y el cable de cobre en la ranura de cobre, aislando la interfase molecular de la intemperie.'),
        ('¿Cuál es la función crítica de las arandelas elásticas Belleville en los pernos?',
         'El aluminio se expande con el calor el doble de rápido que el acero de los pernos. '
         'Sin arandelas elásticas, el aluminio se aplastaría plásticamente durante los picos de carga y quedaría flojo al enfriarse de noche. '
         'Una conexión floja aumenta su resistencia eléctrica y termina quemándose. '
         'Las arandelas elásticas cónicas Belleville absorben la dilatación térmica y mantienen una presión de apriete constante y calibrada por décadas.')
    ],
    cta='¿Suministra herrajes para líneas aéreas de media y baja tensión, derivaciones de transformadores o grapas bimetálicas PG conforme a norma IEC 61284? YOMIN fabrica grapas de ranuras paralelas forjadas de alta calidad.',
    body='''
<h2>El Conector de Derivación Esencial para Líneas Eléctricas Aéreas</h2>
<p>A lo largo de miles de kilómetros de tendidos eléctricos aéreos en conductores desnudos, la corriente debe derivarse hacia transformadores, puentearse en aisladores de retención y distribuirse a ramales secundarios sin soportar la tensión mecánica del vano.</p>
<p>Sin embargo, estos puntos de conexión deben resistir durante décadas las inclemencias del clima: viento, radiación solar UV, vibraciones y ciclos térmicos extremos.</p>
<p>La <strong>Grapa de Ranuras Paralelas (Grapa PG / Series JB y CAPG)</strong> es el herraje electromecánico estandarizado para brindar una conexión eléctrica desmontable, segura y de alta conductividad entre conductores paralelos.</p>

<h2>Elementos de Diseño y Calidad Constructiva</h2>
<ol>
  <li><strong>Cuerpo Ranurado de Aleación de Aluminio Forjado:</strong> Dos canales perfilados al radio del conductor que maximizan la superficie de contacto sin dañar los hilos exteriores.</li>
  <li><strong>Chapa Bimetálica de Cobre Soldada por Fricción (Serie CAPG):</strong> Impide la corrosión galvánica en empalmes mixtos de conductores de aluminio con cobre.</li>
  <li><strong>Pernos de Acero de Alta Resistencia Grado 8.8:</strong> Galvanizados en caliente para brindar un torque de apriete elevado y duradero.</li>
  <li><strong>Arandelas Elásticas Cónicas Belleville:</strong> Garantizan una presión constante ante las dilataciones y contracciones térmicas del conductor.</li>
</ol>
'''
)

PGC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='overhead-line-tapping-what-is-a-parallel-groove-clamp-ar',
    title='تفريعات الخطوط الهوائية وعوازل التوزيع: ما هو قفيص المجرى المتوازي (PG Clamp)؟',
    breadcrumb='المرابط والموصلات الكهربائية',
    read='10 دقائق قراءة',
    alt='قفيص المجرى المتوازي من الألمنيوم بمسمارين (موديل JB) مثبت على ذراع عمود توزيع كهربائي هوائي',
    desc=('خطوط نقل وتوزيع الكهرباء الهوائية وتفريعات التيار خارج الشد الميكانيكي: ما هو قفيص المجرى المتوازي (PG Clamp)؟ '
          'هياكل الألمنيوم المطروق، والشرائح ثنائية المعدن نحاس-ألمنيوم باللحام الاحتكاكي، وحلقات بيليفيل النوابض لمنع التآكل الجلفاني.'),
    model='سلسلة JB / CAPG: أقفاص المجرى المتوازي من سبائك الألمنيوم وثنائية المعدن نحاس-ألمنيوم (مقاطع 16 مم² إلى 300 مم²)',
    category='المرابط والموصلات / أقفاص المجرى المتوازي PG Clamps',
    kw='قفيص pg &middot; parallel groove clamp &middot; كلمب pg &middot; قفيص ثنائي المعدن capg &middot; تفريع خط هوائي &middot; مربط مجرى متوازي',
    specs=[
        ('أنواع الموصلات الهوائية المتوافقة', 'الموصلات الهوائية العارية من الألمنيوم (AAC) والألمنيوم المقوى بالفولاذ (ACSR) وسبائك الألمنيوم (AAAC) والنحاس'),
        ('نطاق مقاطع الموصلات المقبولة بالمليمتر', 'تتسع للموصلات الرئيسية والفرعية بمقاطع: 16، 25، 50، 70، 120 وحتى 300 مم&sup2; (مقاطع متطابقة أو تفريعات متدرجة)'),
        ('مادة تصنيع جسم القفيص والمجرى', 'سبائك ألمنيوم عالية النقاوة (&ge; 99.5%) مطروقة ومقاومة للتآكل مع مجريين طوليين متوازيين مطابقين لقطر السلك'),
        ('تقنية ثنائي المعدن لمنع الصدأ (CAPG)', 'شريحة نحاس إلكتروليتي نقي ملتحمة بالاحتكاك الجزيئي داخل مجرى التفريع لمنع التآكل الجلفاني بين الألمنيوم والنحاس'),
        ('مواصفات مسامير الربط الميكانيكي', 'مسامير صلب كربوني عالي المتانة (رتبة 8.8) مجلفنة بالغمس الساخن (مسمار واحد، مسمارين، أو ثلاثة مسامير)'),
        ('تعويض التمدد والانكماش الحراري', 'مزود بحلقات نوابض بيليفيل (Belleville) المخروطية تحت الصواميل للحفاظ على ثبات ضغط التلامس مع تغير الفصول'),
        ('الموصلية الكهربائية ومقاومة التلامس', 'مقاومة تلامس كهربائية أقل من طول مكافئ من الموصل؛ ارتفاع حراري متزن تحت أقصى تيار تشغيلي'),
        ('المطابقة القياسية والاختبارات الدولية', 'مطابق كلياً للمواصفات الدولية IEC 61284 و BS 3288 و ANSI C119.4 Class A و EN 50483-4 لعتاد الخطوط الهوائية')
    ],
    faqs=[
        ('ما هو قفيص المجرى المتوازي (PG Clamp) وما هي وظيفته في خطوط الكهرباء الهوائية؟',
         'قفيص المجرى المتوازي—والمعروف في مصطلحات شبكات التوزيع باسم كلمب PG أو قفيص التفريع المتوازي—هو '
         'موصل ميكانيكي كهربائي مقفل بالمسامير يحتوي على مجريين طوليين متوازيين مصممين لربط موصلين كهربائيين هوائيين بجانب بعضهما. '
         'يؤدي القفيص ثلاث وظائف تفريع هامة خارج الشد الميكانيكي: '
         '<ul>'
         '<li><strong>1. تفريعات المحولات والمعدات:</strong> توصيل الأسلاك الهابطة من خط التوزيع الرئيسي إلى محولات التوزيع على الأعمدة ومانعات الصواعق والفيوزات.</li>'
         '<li><strong>2. جسور التوصيل (Jumpers):</strong> نقل التيار حول عوازل الشد عند أعمدة الزوايا ونهايات الخطوط لتأمين استمرارية الدائرة.</li>'
         '<li><strong>3. تفريعات الخطوط الفرعية:</strong> أخذ تفريعة لقرية أو مزرعة من الخط الرئيسي المستمر دون الحاجة لقطعه.</li>'
         '</ul>'
         'وبما أنه لا يتحمل الشد الميكانيكي لوزن الخط، فإن مهمته الهندسية تنحصر في تحقيق اتصال كهربائي فائق الموصلية وخالٍ من السخونة.'),
        ('لماذا تعتبر أقفاص PG ثنائية المعدن (CAPG) ضرورية جداً عند ربط كابل ألمنيوم مع كابل نحاس؟',
         'عند تلامس الألمنيوم والنحاس بشكل مباشر في الهواء الطلق بوجود الرطوبة، ينشأ تفاعل كهروكيميائي عنيف يُعرف بـ <strong>التآكل الجلفاني</strong>. '
         'حيث يتآكل الألمنيوم كقطب مضحي ويتحول إلى بودرة بيضاء هشة، مما يؤدي لارتفاع المقاومة واحتراق الوصلة وانقطاع الكهرباء. '
         'تحل أقفاص CAPG ثنائية المعدن هذه المشكلة بدمج شريحة نحاس إلكتروليتي ملتحمة جزيئياً باحتكاك المصنع في مجرى التفريع. '
         'يستقر سلك الألمنيوم في مجرى الألمنيوم، وسلك النحاس في مجرى النحاس، مما يعزل التفاعل الجلفاني نهائياً عن الهواء.'),
        ('ما هي الفائدة الحيوية لحلقات نوابض بيليفيل (Belleville Washers) في مسامير القفيص؟',
         'يتمدد الألمنيوم بالحرارة بضعف سرعة تمدد حديد المسامير. '
         'وبدون حلقات نوابض، سينضغط الألمنيوم بشكل دائم تحت الحمل الحراري العالي ثم يرتخي تماماً عند برودة الليل. '
         'والوصلة المرتخية تسخن وتحترق بسرعة. '
         'تعمل حلقات بيليفيل المخروطية كنوابض طاقة ميكانيكية تمتص التمدد بالحرارة وتعيد الضغط باستمرار عند الانكماش، مما يضمن ضغط تلامس محكم لعشرات السنين.')
    ],
    cta='هل تعمل على توريد عتاد الخطوط الهوائية لشبكات التوزيع، أو تفريعات المحولات، أو أقفاص المجرى المتوازي ثنائية المعدن المطابقة لمعايير IEC 61284؟ تصنع يمين (YOMIN) أقفاص PG مطروقة عالية الجودة.',
    body='''
<h2>الموصل القياسي لتفريعات الخطوط الهوائية وجسور التوصيل</h2>
<p>على امتداد آلاف الكيلومترات من خطوط نقل وتوزيع الكهرباء الهوائية بالأسلاك العارية، يحتاج المهندسون إلى تفريع التيار وتوصيل المحولات وجسور عوازل الشد دون تعريض الوصلة لقوى الشد الميكانيكية لوزن السلك.</p>
<p>ومع ذلك، يجب أن تصمد هذه الوصلات أمام أقسى تقلبات الطقس: الرياح العاتية، والأشعة فوق البنفسجية، وتذبذب درجات الحرارة بين الليل والنهار.</p>
<p>يمثل <strong>قفيص المجرى المتوازي (سلسلة JB وسلسلة CAPG ثنائية المعدن)</strong> الحل الهندسي القياسي لتأمين اتصال كهربائي ممتاز وقابل للفك والتعديل بين موصلين متوازيين.</p>

<h2>المكونات الهندسية وميزات المتانة</h2>
<ol>
  <li><strong>جسم من سبائك الألمنيوم عالي النقاوة:</strong> مجريان متوازيان بدقة هندسية تمنع سحق شعيرات السلك وتوفر أقصى مساحة تلامس.</li>
  <li><strong>شريحة نحاسية ملتحمة بالاحتكاك (سلسلة CAPG):</strong> تمنع التآكل الجلفاني الكارثي عند تفريع أسلاك النحاس من خطوط الألمنيوم.</li>
  <li><strong>مسامير صلب مجلفنة عالية القوة (رتبة 8.8):</strong> توفر عزم ربط هائل ومقاومة تامة للصدأ لأكثر من 30 عاماً.</li>
  <li><strong>حلقات نوابض بيليفيل المخروطية:</strong> تعوض التمدد والانكماش الحراري وتحافظ على ثبات ضغط الربط بشكل دائم.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1005 = [
    CSC_EN, CSC_FR, CSC_ES, CSC_AR,
    PGC_EN, PGC_FR, PGC_ES, PGC_AR
]
