# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-09-29 Batch 2:
1. Solar DC Photovoltaic Surge Protective Device (SPD) (EN, FR, ES, AR)
2. Medium-Voltage Vacuum Circuit Breaker (VCB) (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. SOLAR DC PHOTOVOLTAIC SURGE PROTECTIVE DEVICE (EN, FR, ES, AR)
# ==============================================================================

DC_SPD_EN = dict(
    lang='en',
    dir='ltr',
    slug='photovoltaic-protection-what-is-a-solar-dc-spd',
    title='Photovoltaic Array Lightning Protection: What Is a Solar DC SPD?',
    breadcrumb='Solar &amp; PV Products',
    read='10 min read',
    alt='Modular 1000V DC photovoltaic surge protective device actively operating inside an outdoor solar combiner box',
    desc=('Commercial and utility solar photovoltaic lightning protection: What is a solar DC SPD? '
          'How modular DC surge protective devices clamp high-voltage lightning transients, isolate 1000V/1500V DC arcing faults, and protect solar inverters.'),
    model='Model YM-PV-SPD Series Type 1+2 & Type 2 1000V/1500V DC Photovoltaic Surge Protective Devices',
    category='Solar & PV Products / DC Surge Protectors',
    kw='what is a solar dc spd &middot; solar dc spd &middot; photovoltaic spd &middot; dc surge protection device &middot; 1000v dc spd &middot; solar combiner box spd',
    specs=[
        ('Rated Maximum Continuous Operating Voltage (Ucpv)', '600V DC, 1000V DC, and 1500V DC configurations engineered specifically for high-voltage PV strings'),
        ('SPD Classification & Test Class', 'Type 1+2 / Class I+II (combined direct lightning impulse & induced surge) and Type 2 / Class II (induced transient clamping)'),
        ('Lightning Impulse Current (Iimp 10/350 &mu;s)', '12.5 kA per pole (Type 1+2) simulating direct physical lightning strikes on exposed solar array racking structures'),
        ('Nominal & Maximum Discharge Current', 'In 20 kA (8/20 &mu;s); Imax 40 kA to 80 kA (8/20 &mu;s) for severe indirect lightning electromagnetic pulses (LEMP)'),
        ('Voltage Protection Level (Up)', '&le; 3.2 kV at 1000V DC; &le; 4.5 kV at 1500V DC (strictly coordinated below solar inverter impulse withstand ratings)'),
        ('Internal Circuit Topology', 'U-configuration (Y-topology) with three high-energy metal oxide varistors (MOV) and thermal disconnectors preventing single-MOV burnout'),
        ('Thermal Disconnector & Status Indication', 'Patented mechanical thermal fuse disconnect with optical green/red visual flag window and optional 3-pin remote telemetry contact'),
        ('Applicable International Standards', 'EN 50539-11 (Surge protective devices for photovoltaic installations), IEC 61643-31, UL 1449 4th Edition, CE certified, TUV Rheinland tested')
    ],
    faqs=[
        ('What is a Solar DC SPD and why can\'t standard AC surge protectors be used on photovoltaic arrays?',
         'A Solar DC Surge Protective Device (SPD) is a specialized transient voltage suppressor engineered to protect direct-current photovoltaic circuits from lightning strikes '
         'and grid switching overvoltages. **Standard AC surge protectors must never be installed on solar DC circuits** for a critical physical reason: '
         'Alternating current naturally crosses zero voltage 100 or 120 times every second, allowing internal AC spark gaps and thermal disconnectors to extinguish power arcs easily. '
         'Direct current from solar panels maintains a relentless, continuous voltage without zero crossings. If an AC surge protector fails under a lightning surge on a 1000V DC '
         'array, the resulting DC arc will fail to extinguish, generating plasma heat exceeding 3,000&deg;C that rapidly incinerates combiner boxes and causes catastrophic fires. '
         'Photovoltaic DC SPDs feature specialized arc-extinguishing chambers, rotational thermal disconnectors, and Y-shaped MOV arrays designed to safely quench high-voltage DC arcs.'),
        ('What is the difference between Type 1+2 and Type 2 DC SPDs in solar farm installations?',
         'The choice between Type 1+2 and Type 2 DC SPDs depends on the facility\'s lightning risk assessment per IEC 62305 and IEC 61643-32: '
         '<ul>'
         '<li><strong>Type 1+2 DC SPD (Class I+II):</strong> Tested with both a $10/350\\,\\mu\\text{s}$ direct lightning current waveform (Iimp) and an $8/20\\,\\mu\\text{s}$ induced '
         'waveform. Mandatory for rooftop solar arrays equipped with external lightning protection rods (LPS) where the separation distance \'s\' cannot be maintained, '
         'as well as ground-mount solar farms in open terrain prone to direct lightning strikes.</li>'
         '<li><strong>Type 2 DC SPD (Class II):</strong> Tested with an $8/20\\,\\mu\\text{s}$ current waveform (In/Imax) to suppress indirect, induced overvoltages caused by '
         'cloud-to-cloud lightning flashes or nearby ground strikes. Standard installation choice inside string inverters and secondary array combiner boxes.</li>'
         '</ul>'),
        ('What is the Y-shaped (U-configuration) internal circuit topology in a solar DC SPD?',
         'In early solar installations, surge arresters were wired directly line-to-earth (+ to PE and - to PE). If insulation degraded on the positive DC line, '
         'a double earth fault would drive the entire string voltage through a single varistor, causing catastrophic thermal runaway. '
         'Modern certified solar DC SPDs use a **Y-configuration** containing three varistor branches: one connected from DC+ to a common floating point, '
         'one from DC- to the common point, and a third from the common point to protective earth (PE). This balanced delta ensures that even if a continuous insulation fault '
         'occurs on one solar cable, the remaining varistors continue dividing the string voltage safely, completely preventing thermal burnout.')
    ],
    cta='Specifying 1000V or 1500V DC surge protective devices for utility-scale solar farms, commercial rooftop combiner boxes, or central solar inverter stations? YOMIN manufactures TUV and CE certified photovoltaic SPDs engineered to IEC 61643-31 and EN 50539-11.',
    body='''
<h2>Shielding Photovoltaic Infrastructure from High-Energy Lightning Transients</h2>
<p>Solar photovoltaic installations represent expansive metallic collector networks installed across open fields, industrial warehouse roofs, and desert terrains. These extensive conductor loops act as massive antennas, capturing electromagnetic fields generated by lightning strikes occurring miles away.</p>
<p>Direct lightning strikes and indirect lightning electromagnetic pulses (LEMP) induce massive transient voltage spikes exceeding 15,000 to 40,000 volts along DC string wiring. Because sensitive maximum power point tracking (MPPT) semiconductor circuits inside modern solar inverters have an impulse withstand rating (Uw) of only 4,000 to 6,000 volts, an unprotected solar array will suffer destroyed inverter bridges and catastrophic downtime.</p>
<p>The <strong>Solar DC Surge Protective Device (SPD)</strong> is the essential barrier that clamps incoming lightning surges within nanoseconds, shunting thousands of amperes safely to earth before transient voltages reach inverter electronics.</p>

<h2>Physical Realities of DC Arcing vs. AC Suppression</h2>
<p>Photovoltaic surge protection requires fundamentally different engineering compared to building AC electrical panels:</p>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Standard AC Surge Protector</th>
      <th>Dedicated Solar DC Photovoltaic SPD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Operating Voltage Nature</strong></td>
      <td>Sinusoidal AC crossing zero 100/120 times/sec.</td>
      <td><strong>Continuous, relentless DC voltage (0V to 1500V DC).</strong></td>
    </tr>
    <tr>
      <td><strong>Arc Extinguishment Physics</strong></td>
      <td>Self-extinguishes as AC voltage passes through zero.</td>
      <td><strong>Requires mechanical rotary barriers & arc splitter chambers.</strong></td>
    </tr>
    <tr>
      <td><strong>Internal Varistor Topology</strong></td>
      <td>Single or dual MOV branches (Line to Neutral/PE).</td>
      <td><strong>3-Branch Y-topology (DC+, DC-, PE) with thermal fuse disconnects.</strong></td>
    </tr>
    <tr>
      <td><strong>End-of-Life Failure Mode</strong></td>
      <td>Trips upstream AC breaker safely.</td>
      <td><strong>High risk of continuous DC fire without certified DC disconnectors.</strong></td>
    </tr>
    <tr>
      <td><strong>Applicable Metrology Standard</strong></td>
      <td>IEC 61643-11 / EN 61643-11</td>
      <td><strong>IEC 61643-31 / EN 50539-11 (Photovoltaic Specific).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

DC_SPD_FR = dict(
    lang='fr',
    dir='ltr',
    slug='photovoltaic-protection-what-is-a-solar-dc-spd-fr',
    title="Protection Foudre des Panneaux Solaires : Qu'est-ce qu'un Parafoudre DC Photovoltaïque ?",
    breadcrumb='Solaire &amp; Photovoltaïque',
    read='10 min de lecture',
    alt='Parafoudre photovoltaïque modulaire 1000V DC en fonctionnement dans un coffret de jonction solaire extérieur',
    desc=('Protection foudre des installations solaires commerciales et industrielles : Qu\'est-ce qu\'un parafoudre DC photovoltaïque ? '
          'Comment les parafoudres DC protègent les onduleurs solaires, écrêtent les surtensions transitoires et éliminent les risques d\'arc électrique continu sous 1000V/1500V.'),
    model='Série YM-PV-SPD : Parafoudres Photovoltaïques DC Type 1+2 & Type 2 (1000V / 1500V DC)',
    category='Solaire & Photovoltaïque / Parafoudres DC',
    kw='parafoudre dc solaire &middot; parafoudre photovoltaïque &middot; parafoudre 1000v dc &middot; protection foudre solaire &middot; coffret dc photovoltaïque',
    specs=[
        ('Tension Maximale de Service Continu (Ucpv)', 'Configurations 600V DC, 1000V DC et 1500V DC spécialement dimensionnées pour les chaînes photovoltaïques'),
        ('Classification & Classe d\'Essai', 'Type 1+2 / Classe I+II (choc direct et surtensions induites) et Type 2 / Classe II (écrêtage des surtensions indirectes)'),
        ('Courant d\'Impulsion de Foudre (Iimp 10/350 &mu;s)', '12,5 kA par pôle (Type 1+2) simulant un coup de foudre direct sur la structure métallique des panneaux'),
        ('Courant Nominal et Maximal de Décharge', 'In 20 kA (8/20 &mu;s) ; Imax 40 kA à 80 kA (8/20 &mu;s) pour les impulsions électromagnétiques de foudre (LEMP)'),
        ('Niveau de Protection en Tension (Up)', '&le; 3,2 kV sous 1000V DC ; &le; 4,5 kV sous 1500V DC (inférieur à la tenue aux chocs des onduleurs solaires)'),
        ('Topologie de Circuit Interne', 'Schéma en Y (configuration U) avec trois varistances à oxyde de zinc (MOV) évitant l\'emballement thermique sur défaut d\'isolement'),
        ('Déconnecteur Thermique & Signalisation', 'Déconnexion mécanique brevetée avec voyant visuel d\'état vert/rouge et contact de télésignalisation à distance inverseur'),
        ('Normes Internationales Applicables', 'EN 50539-11 (Parafoudres pour installations photovoltaïques), CEI 61643-31, certifié CE et testé TUV Rheinland')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un parafoudre DC photovoltaïque et pourquoi les parafoudres AC sont-ils strictement interdits en solaire ?',
         'Un parafoudre DC photovoltaïque est un limiteur de surtension spécialement conçu pour sécuriser les circuits en courant continu des générateurs solaires. '
         '**Il est formellement interdit d\'installer un parafoudre AC classique sur un circuit solaire DC** pour une raison physique majeure : '
         'Le courant alternatif s\'annule naturellement 100 fois par seconde (passage par zéro), ce qui permet à l\'arc électrique de s\'éteindre spontanément lors du déclenchement. '
         'À l\'inverse, le courant continu issu des panneaux solaires ne passe jamais par zéro. Si un parafoudre AC tente d\'évacuer une surtension sur une chaîne de 1000V DC, '
         'l\'arc électrique ne s\'éteint pas et génère un plasma à plus de 3 000&deg;C qui embrase instantanément le coffret électrique. '
         'Les parafoudres solaires DC intègrent des chambres de soufflage magnétique et des déconnecteurs thermiques rotatifs certifiés selon la norme EN 50539-11.'),
        ('Quelle est la différence entre un parafoudre DC Type 1+2 et un Type 2 en centrale solaire ?',
         'Le choix dépend de l\'analyse du risque foudre selon les normes CEI 62305 et CEI 61643-32 : '
         '<ul>'
         '<li><strong>Type 1+2 (Classe I+II) :</strong> Testé avec une onde de courant direct $10/350\\,\\mu\\text{s}$ (Iimp). Il est obligatoire lorsque la toiture ou la centrale '
         'au sol est équipée d\'un paratonnerre extérieur et que la distance de séparation de sécurité ne peut pas être respectée.</li>'
         '<li><strong>Type 2 (Classe II) :</strong> Éprouvé avec l\'onde $8/20\\,\\mu\\text{s}$ (In/Imax). Il protège contre les surtensions induites par des éclairs proches '
         'ou des décharges entre nuages. C\'est le choix standard à l\'intérieur des onduleurs de branche et des coffrets de raccordement secondaires.</li>'
         '</ul>'),
        ('Qu\'est-ce que la topologie de câblage en Y dans un parafoudre solaire DC ?',
         'Historiquement, les parafoudres étaient raccordés directement entre le pôle positif et la terre (+/PE) et entre le pôle négatif et la terre (-/PE). '
         'En cas de défaut d\'isolement sur un câble, la pleine tension de chaîne traversait une seule varistance, entraînant sa destruction par emballement thermique. '
         'Les parafoudres DC modernes adoptent une **topologie en Y** comportant trois branches de varistances : une branche DC+/point milieu, une branche DC-/point milieu, '
         'et une branche point milieu/terre (PE). Cette configuration divise la tension même en présence d\'un défaut d\'isolement franc, garantissant une sécurité incendie totale.')
    ],
    cta='Vous concevez des centrales solaires au sol, des toitures photovoltaïques commerciales ou des coffrets de jonction DC 1000V/1500V nécessitant des parafoudres certifiés EN 50539-11 ? YOMIN fabrique des parafoudres solaires haute performance testés TUV.',
    body='''
<h2>Protéger les Investissements Solaires contre les Effets Destructeurs de la Foudre</h2>
<p>Les centrales solaires photovoltaïques sont par nature déployées sur de vastes surfaces dégagées : toitures d'usines, ombrières de parking et parcs au sol. Ces structures métalliques et leurs kilomètres de câbles forment de gigantesques boucles d'induction captant le rayonnement électromagnétique de la foudre.</p>
<p>Les coups de foudre directs et les impulsions induites génèrent des pics de surtension transitoire dépassant 15 000 à 40 000 volts sur les lignes continues. Sachant que les semi-conducteurs des onduleurs solaires ne supportent qu'une tension de tenue aux chocs de 4 000 à 6 000 volts, un champ solaire sans parafoudre adapté s'expose à la destruction immédiate de ses étages d'entrée MPPT.</p>
<p>Le <strong>Parafoudre DC Photovoltaïque</strong> constitue le bouclier indispensable qui dérive les courants de foudre à la terre en quelques nanosecondes avant qu'ils n'atteignent l'onduleur.</p>

<h2>Les Exigences Spécifiques du Courant Continu Solaire</h2>
<p>La protection contre les surtensions en courant continu impose des technologies radicalement différentes du courant alternatif :</p>
<table>
  <thead>
    <tr>
      <th>Paramètre Technique</th>
      <th>Parafoudre Réseau AC Classique</th>
      <th>Parafoudre DC Solaire Spécifique</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nature de la Tension</strong></td>
      <td>Sinusoïdale AC avec 100 passages par zéro/sec.</td>
      <td><strong>Tension continue ininterrompue de 0V à 1500V DC.</strong></td>
    </tr>
    <tr>
      <td><strong>Extinction de l'Arc Électrique</strong></td>
      <td>Naturelle au passage par zéro de l'onde.</td>
      <td><strong>Obligation de chambres de coupure et barrières mécaniques.</strong></td>
    </tr>
    <tr>
      <td><strong>Schéma Interne des Varistances</strong></td>
      <td>Branches directes Phase/Neutre/Terre.</td>
      <td><strong>Schéma en Y à trois varistances haute énergie.</strong></td>
    </tr>
    <tr>
      <td><strong>Risque en Fin de Vie</strong></td>
      <td>Déclenchement du disjoncteur amont.</td>
      <td><strong>Risque d'incendie majeur sans déconnecteur thermique rotatif.</strong></td>
    </tr>
    <tr>
      <td><strong>Norme Métrologique Dédiée</strong></td>
      <td>CEI 61643-11</td>
      <td><strong>EN 50539-11 / CEI 61643-31 (Spécifique Photovoltaïque).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

DC_SPD_ES = dict(
    lang='es',
    dir='ltr',
    slug='photovoltaic-protection-what-is-a-solar-dc-spd-es',
    title='Protección contra Rayos en Arreglos Fotovoltaicos: ¿Qué es un SPD Solar DC?',
    breadcrumb='Solar y Fotovoltaica',
    read='10 min de lectura',
    alt='Dispositivo de protección contra sobretensiones fotovoltaico modular de 1000V DC operando dentro de una caja combinadora solar exterior',
    desc=('Protección contra rayos en instalaciones solares comerciales e industriales: ¿Qué es un SPD solar DC? '
          'Cómo los protectores contra sobretensiones DC limitan picos de tensión por descargas atmosféricas, aíslan arcos continuos bajo 1000V/1500V y protegen inversores.'),
    model='Serie YM-PV-SPD: Dispositivos de Protección contra Sobretensiones DC Tipo 1+2 y Tipo 2 (1000V / 1500V DC)',
    category='Solar y Fotovoltaica / Protectores contra Sobretensiones DC',
    kw='spd solar dc &middot; protector sobretensiones fotovoltaico &middot; spd 1000v dc &middot; protección contra rayos solar &middot; caja combinadora solar',
    specs=[
        ('Tensión Máxima de Operación Continua (Ucpv)', 'Configuraciones de 600V DC, 1000V DC y 1500V DC calibradas específicamente para cadenas fotovoltaicas de alta tensión'),
        ('Clasificación y Clase de Ensayo', 'Tipo 1+2 / Clase I+II (impacto directo de rayo y sobretensión inducida) y Tipo 2 / Clase II (sobretensiones indirectas inducidas)'),
        ('Corriente de Impulso de Rayo (Iimp 10/350 &mu;s)', '12,5 kA por polo (Tipo 1+2) simulando el impacto físico directo de rayos en estructuras metálicas solares'),
        ('Corriente Nominal y Máxima de Descarga', 'In 20 kA (8/20 &mu;s); Imax 40 kA a 80 kA (8/20 &mu;s) para pulsos electromagnéticos de rayo (LEMP)'),
        ('Nivel de Protección en Tensión (Up)', '&le; 3,2 kV a 1000V DC; &le; 4,5 kV a 1500V DC (coordinado por debajo del límite de tensión de impulso de los inversores)'),
        ('Topología de Circuito Interno', 'Configuración en Y (conexión en U) con tres varistores de óxido metálico (MOV) que evitan fallas por degradación de aislamiento'),
        ('Desconectador Térmico y Señalización', 'Desconexión mecánica patentada con indicador visual de inspección verde/rojo y contacto seco inversor de telemetría remota'),
        ('Normas Internacionales Aplicables', 'EN 50539-11 (Dispositivos de protección para sistemas fotovoltaicos), IEC 61643-31, certificado CE y probado por TUV Rheinland')
    ],
    faqs=[
        ('¿Qué es un SPD solar DC y por qué está prohibido instalar protectores de corriente alterna (AC) en paneles solares?',
         'Un SPD solar DC (Surge Protective Device) es un supresor de sobretensiones transitorias fabricado para circuitos en corriente continua de plantas solares. '
         '**Bajo ninguna circunstancia debe instalarse un protector AC convencional en un circuito solar DC**, debido a una ley física elemental: '
         'La corriente alterna cruza por cero 100 o 120 veces por segundo, lo que permite que los desconectadores térmicos y vías de chispa apaguen el arco eléctrico fácilmente. '
         'En cambio, la corriente continua de los paneles solares mantiene una tensión ininterrumpida sin pasos por cero. Si un protector AC se dispara ante un rayo en un circuito '
         'de 1000V DC, se generará un arco continuo a más de 3.000&deg;C que no se apagará, incendiando la caja combinadora en segundos. '
         'Los protectores solares DC cuentan con cámaras especiales de extinción magnética y desconectadores mecánicos certificados según la norma EN 50539-11.'),
        ('¿Cuál es la diferencia entre un SPD solar Tipo 1+2 y un Tipo 2 en plantas fotovoltaicas?',
         'La selección se basa en la evaluación del nivel de riesgo de rayos según IEC 62305 e IEC 61643-32: '
         '<ul>'
         '<li><strong>Tipo 1+2 (Clase I+II):</strong> Probado con onda directa de corriente de rayo $10/350\\,\\mu\\text{s}$ (Iimp). Es obligatorio cuando la estructura solar '
         'cuenta con pararrayos externos y no se puede mantener la distancia de seguridad, así como en parques solares en terreno abierto propensos a impactos directos.</li>'
         '<li><strong>Tipo 2 (Clase II):</strong> Probado con onda inducida $8/20\\,\\mu\\text{s}$ (In/Imax) para derivar sobretensiones indirectas causadas por rayos cercanos '
         'o descargas nube a nube. Es el estándar para cajas de nivel de string y entradas de inversores.</li>'
         '</ul>'),
        ('¿Qué ventajas ofrece la configuración interna en Y en un protector solar DC?',
         'En los inicios de la energía solar, los protectores se conectaban directamente positivo a tierra (+/PE) y negativo a tierra (-/PE). '
         'Si ocurría una falla de aislamiento en un cable, la tensión total del arreglo solar atravesaba un solo varistor, destruyéndolo por embalamiento térmico. '
         'Los protectores solares certificados actuales utilizan una **topología en Y** compuesta por tres varistores: uno de positivo a nodo común, uno de negativo a nodo común, '
         'y un tercero del nodo común a tierra (PE). Esta distribución garantiza que incluso ante una falla de aislamiento a tierra, los varistores restantes se repartan la tensión, '
         'evitando incendios.')
    ],
    cta='¿Diseña parques solares a gran escala, techos industriales o cajas combinadoras de 1000V/1500V que requieren protectores solares certificados bajo norma EN 50539-11? YOMIN fabrica descargadores fotovoltaicos de alto rendimiento con certificación TUV.',
    body='''
<h2>Protección de la Infraestructura Solar frente a Descargas Atmosféricas</h2>
<p>Las instalaciones solares fotovoltaicas abarcan extensas áreas al aire libre en cubiertas industriales, estacionamientos y campos abiertos. Estos grandes bucles conductores actúan como antenas receptoras que capturan la radiación electromagnética de rayos caídos a kilómetros de distancia.</p>
<p>Los impactos directos y las sobretensiones inducidas generan picos de voltaje que superan los 15.000 a 40.000 voltios en los cables de corriente continua. Dado que los semiconductores MPPT de los inversores solares solo soportan entre 4.000 y 6.000 voltios de tensión al impulso, un arreglo solar desprotegido sufrirá la destrucción inmediata de sus inversores.</p>
<p>El <strong>Dispositivo de Protección contra Sobretensiones Solar DC (SPD)</strong> es la barrera indispensable que deriva a tierra las corrientes de rayo en nanosegundos, manteniendo el voltaje dentro de niveles seguros para el inversor.</p>

<h2>Diferencias Críticas entre Supresores DC Fotovoltaicos y Supresores AC</h2>
<p>El comportamiento de los circuitos de corriente continua exige tecnologías de extinción de arco muy superiores a las del corriente alterna:</p>
<table>
  <thead>
    <tr>
      <th>Parámetro Técnico</th>
      <th>Protector contra Sobretensiones AC</th>
      <th>Protector Solar DC Fotovoltaico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Naturaleza de la Tensión</strong></td>
      <td>Senoidal con 100/120 pasos por cero por segundo.</td>
      <td><strong>Tensión continua constante de 0V a 1500V DC.</strong></td>
    </tr>
    <tr>
      <td><strong>Extinción del Arco Eléctrico</strong></td>
      <td>Se apaga solo al pasar la onda por cero.</td>
      <td><strong>Requiere cámaras de soplado y barreras mecánicas de corte.</strong></td>
    </tr>
    <tr>
      <td><strong>Topología Interna de Varistores</strong></td>
      <td>Conexión directa Fase/Neutro/Tierra.</td>
      <td><strong>Topología en Y con tres ramas de varistores de alta energía.</strong></td>
    </tr>
    <tr>
      <td><strong>Riesgo al Final de Vida Útil</strong></td>
      <td>Dispara el interruptor automático aguas arriba.</td>
      <td><strong>Alto riesgo de fuego si no dispone de desconectador térmico DC.</strong></td>
    </tr>
    <tr>
      <td><strong>Normativa de Ensayo</strong></td>
      <td>IEC 61643-11</td>
      <td><strong>EN 50539-11 / IEC 61643-31 (Específica Fotovoltaica).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

DC_SPD_AR = dict(
    lang='ar',
    dir='rtl',
    slug='photovoltaic-protection-what-is-a-solar-dc-spd-ar',
    title='حماية مصفوفات الطاقة الشمسية من الصواعق: ما هو مانع الصواعق المستمر (DC SPD)؟',
    breadcrumb='الطاقة الشمسية والكهرومغناطيسية',
    read='10 دقائق قراءة',
    alt='مانع صواعق كهروضوئي للتيار المستمر بجهد 1000 فولت يعمل داخل صندوق تجميع خلايا شمسية خارجي',
    desc=('حماية محطات الطاقة الشمسية التجارية من الصواعق: ما هو مانع الصواعق المستمر (DC SPD)؟ '
          'كيف تحد أجهزة الحماية من التيارات العابرة الفائقة، وتخمد أقواس التيار المستمر عند 1000V/1500V، وتحمي العواكس الشمسية من التلف.'),
    model='سلسلة YM-PV-SPD: موانع صواعق كهروضوئية للتيار المستمر فئة Type 1+2 و Type 2 (1000V / 1500V DC)',
    category='الطاقة الشمسية / موانع صواعق التيار المستمر',
    kw='مانع صواعق طاقة شمسية &middot; مانع صواعق dc &middot; مانع صواعق 1000 فولت &middot; حماية العاكس الشمسي &middot; صندوق تجميع الطاقة الشمسية',
    specs=[
        ('أقصى جهد تشغيلي مستمر (Ucpv)', 'تكوينات مخصصة بجهود 600V DC و 1000V DC و 1500V DC مصممة خصيصاً لسلاسل الألواح الشمسية عالية الجهد'),
        ('تصنيف واختبار مانع الصواعق', 'فئة Type 1+2 / Class I+II (للصدمات المباشرة والتفريغ الحثي) وفئة Type 2 / Class II (لحماية التيارات الحثية غير المباشرة)'),
        ('تيار نبضة الصاعقة المباشرة (Iimp 10/350 &mu;s)', 'سعة 12.5 كيلو أمبير لكل قطب (فئة Type 1+2) لمحاكاة ضربات الصواعق المباشرة على هياكل الألواح المعدنية'),
        ('تيار التفريغ الاسمي والأقصى', 'الاسمي In 20 kA (8/20 &mu;s)؛ الأقصى Imax من 40 kA إلى 80 kA لمقاومة النبضات الكهرومغناطيسية للصواعق (LEMP)'),
        ('مستوى حماية الجهد (Up)', '&le; 3.2 kV عند 1000V DC؛ &le; 4.5 kV عند 1500V DC (منسق بدقة ليكون أدنى من قدرة تحمل العواكس الشمسية)'),
        ('طوبولوجيا الدائرة الداخلية', 'توصيل على شكل حرف Y (طوبولوجيا U) يحتوي على ثلاثة مقاومات فاريستور أكسيد الزنك (MOV) لمنع الاحتراق عند انهيار العزل'),
        ('الفصل الحراري ومؤشرات الفحص', 'آلية فصل حراري ميكانيكية حاصلة على براءة اختراع مع نافذة فحص بصرية (أخضر/أحمر) ومخرج إشارة إنذار عن بُعد ثلاثي الأطراف'),
        ('المعايير الدولية المعتمدة', 'EN 50539-11 (موانع الصواعق للأنظمة الكهروضوئية)، IEC 61643-31، شهادة CE وتوثيق من مختبرات TUV Rheinland')
    ],
    faqs=[
        ('ما هو مانع الصواعق المستمر (DC SPD) ولماذا يُحظر تماماً استخدام موانع صواعق التيار المتردد (AC) في أنظمة الطاقة الشمسية؟',
         'مانع الصواعق المستمر (DC SPD) هو جهاز حماية متخصص مصمم لحماية دوائر التيار المستمر في محطات الطاقة الشمسية من التيارات العابرة الناجمة عن الصواعق. '
         '**ويُحظر تماماً تركيب موانع صواعق التيار المتردد (AC) على دوائر الألواح الشمسية المستمرة** لسبب فيزيائي جوهري: '
         'يمر التيار المتردد بنقطة الصفر في الجهد 100 أو 120 مرة في الثانية، مما يساعد أجهزة الحماية وغرف الإخماد على إطفاء القوس الكهربائي فوراً. '
         'أما التيار المستمر المتولد من الألواح الشمسية فلا يمر بنقطة الصفر أبداً. فإذا فرغ مانع الصواعق المتردد تيار صاعقة على خط 1000 فولت مستمر، '
         'سينشأ قوس كهربائي مستمر تتجاوز حرارته 3,000 درجة مئوية يعجز الجهاز عن إطفائه، مما يؤدي إلى اشتعال صندوق التجميع فوراً واحتراق المحطة. '
         'لذلك تحتوي موانع الصواعق الشمسية المستمرة على غرف إخماد مغناطيسي وفواصل حرارية دوارة معتمدة وفق معيار EN 50539-11.'),
        ('ما الفرق بين مانع الصواعق فئة Type 1+2 وفئة Type 2 في مصفوفات الطاقة الشمسية؟',
         'يتحدد الاختيار بناءً على دراسة تقييم مخاطر الصواعق وفق معايير IEC 62305 و IEC 61643-32: '
         '<ul>'
         '<li><strong>فئة Type 1+2 (Class I+II):</strong> تم اختبارها بموجة تيار الصاعقة المباشرة $10/350\\,\\mu\\text{s}$ (Iimp). وهي إلزامية للمحطات والمباني المزودة '
         'بصواري مانعات صواعق خارجية على الأسطح، وكذلك في محطات الطاقة الشمسية المفتوحة في الصحراء والمناطق المعرضة لضربات مباشرة.</li>'
         '<li><strong>فئة Type 2 (Class II):</strong> تم اختبارها بموجة $8/20\\,\\mu\\text{s}$ (In/Imax) لحماية الدوائر من التيارات الحثية غير المباشرة الناتجة عن الصواعق البعيدة. '
         'وهي الاختيار القياسي داخل صناديق التجميع ومدخل العواكس الشمسية.</li>'
         '</ul>'),
        ('ما هي طوبولوجيا التوصيل الداخلي على شكل حرف Y في مانعات صواعق الطاقة الشمسية؟',
         'في السابق، كانت موانع الصواعق توصل مباشرة بين القطب الموجب والأرضي (+/PE) وبين السالب والأرضي (-/PE). '
         'فعند حدوث أي عطل في عزل كابلات الألواح، كان جهد السلسلة بالكامل يمر عبر فاريستور واحد، مما يسبب احتراقه حرارياً. '
         'تعتمد موانع الصواعق الحديثة المعتمدة **طوبولوجيا على شكل حرف Y** تضم ثلاثة أفرع من مقاومات الفاريستور: فرع بين القطب الموجب ونقطة وسطية، '
         'وفرع بين القطب السالب والنقطة الوسطية، وفرع ثالث بين النقطة الوسطية والأرضي (PE). يضمن هذا التوزيع تقسيم الجهد بأمان حتى في حالة حدوث تماس أرضي، '
         'مما يمنع اندلاع الحرائق تماماً.')
    ],
    cta='هل تصمم محطات طاقة شمسية كبرى، أو أسطح مصانع كهروضوئية، أو صناديق تجميع بجهد 1000V/1500V تتطلب موانع صواعق معتمدة بمعايير EN 50539-11 و IEC 61643-31؟ تصنع يمين (YOMIN) موانع صواعق كهروضوئية فائقة الاعتمادية موثقة باختبارات TUV الدولية.',
    body='''
<h2>حماية استثمارات الطاقة الشمسية من مخاطر الصواعق العنيفة</h2>
<p>تمتد محطات الطاقة الكهروضوئية على مساحات شاسعة مفتوحة فوق أسطح المنشآت الصناعية والمستودعات والمزارع الشمسية الميدانية. وتشكل هذه الهياكل المعدنية وشبكات الكابلات الممتدة هوائيات عملاقة تستقطب الحقول الكهرومغناطيسية الناتجة عن الصواعق على بعد أميال.</p>
<p>تولد ضربات الصواعق المباشرة والنبضات الحثية قفزات جهد عابرة خطيرة تتجاوز 15,000 إلى 40,000 فولت على خطوط التيار المستمر. وبما أن دوائر تتبع نقطة الاستطاعة العظمى (MPPT) في العواكس الشمسية الحديثة لا تتحمل نبضات جهد تزيد عن 4,000 إلى 6,000 فولت، فإن أي مصفوفة شمسية غير محمية تتعرض لتدمير فوري لعواكسها وتوقف كامل لتوليد الطاقة.</p>
<p>يعد <strong>مانع الصواعق المستمر (Solar DC SPD)</strong> الدرع الواقي الحاسم الذي يفرغ آلاف الأمبيرات بأمان إلى الأرضي في أجزاء من النانو ثانية قبل أن تصل جهود الصاعقة إلى مكونات العاكس الحساسة.</p>

<h2>الفروق الهندسية الجوهرية بين حماية التيار المستمر وحماية التيار المتردد</h2>
<p>تتطلب حماية دوائر التيار المستمر الشمسي تقنيات إخماد مختلفة جذرياً عن لوحات التيار المتردد التقليدية:</p>
<table>
  <thead>
    <tr>
      <th>المعيار الهندسي</th>
      <th>مانع صواعق التيار المتردد (AC) التقليدي</th>
      <th>مانع صواعق الطاقة الشمسية المستمر (DC SPD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>طبيعة الجهد الكهربائي</strong></td>
      <td>تيار جيبي متردد يمر بنقطة الصفر 100/120 مرة في الثانية.</td>
      <td><strong>جهد مستمر ثابت وشديد القوة من 0 إلى 1500 فولت.</strong></td>
    </tr>
    <tr>
      <td><strong>فيزياء إخماد القوس الكهربائي</strong></td>
      <td>ينطفئ القوس تلقائياً عند مرور الجهد بنقطة الصفر.</td>
      <td><strong>يتطلب غرف إخماد مغناطيسية وحواجز فصل ميكانيكية عازلة.</strong></td>
    </tr>
    <tr>
      <td><strong>طوبولوجيا الدائرة الداخلية</strong></td>
      <td>أفرع مباشرة بين الطور والمحايد والأرضي.</td>
      <td><strong>طوبولوجيا متوازنة على شكل حرف Y بثلاثة مقاومات فاريستور.</strong></td>
    </tr>
    <tr>
      <td><strong>خطورة نهاية العمر الافتراضي</strong></td>
      <td>يفصل القاطع الكهربائي المغذي بأمان.</td>
      <td><strong>خطر اشتعال حريق مستمر في حال غياب فواصل ميكانيكية مخصصة.</strong></td>
    </tr>
    <tr>
      <td><strong>المعايير المترولوجية المعتمدة</strong></td>
      <td>IEC 61643-11</td>
      <td><strong>EN 50539-11 / IEC 61643-31 (خاص بالطاقة الشمسية).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

# ==============================================================================
# 2. MEDIUM-VOLTAGE VACUUM CIRCUIT BREAKER (EN, FR, ES, AR)
# ==============================================================================

VCB_EN = dict(
    lang='en',
    dir='ltr',
    slug='substation-switching-what-is-a-vacuum-circuit-breaker',
    title='Medium-Voltage Substation Protection: What Is a Vacuum Circuit Breaker?',
    breadcrumb='Fuse &amp; Protection',
    read='10 min read',
    alt='Heavy-duty 12kV indoor vacuum circuit breaker draw-out truck unit actively installed in a medium-voltage electrical substation switchgear room',
    desc=('Medium-voltage power grid switching and substation protection: What is a vacuum circuit breaker (VCB)? '
          'How vacuum interrupters extinguish 12kV–36kV high-voltage electrical arcs in high vacuum without SF6 greenhouse gas, providing 31.5kA fault interruption.'),
    model='Model ZN63 (VS1) / ZN28 Series 12kV, 24kV & 36kV Indoor & Outdoor Vacuum Circuit Breakers',
    category='Fuse & Protection / Medium Voltage Vacuum Circuit Breakers',
    kw='what is a vacuum circuit breaker &middot; vacuum circuit breaker &middot; vcb breaker &middot; 11kv vacuum circuit breaker &middot; vacuum interrupter &middot; substation vcb',
    specs=[
        ('Rated Voltage & Insulation Levels', 'Rated voltage 12kV, 24kV, and 36kV; power frequency withstand 42kV/54kV/95kV; lightning impulse withstand (BIL) 75kV/125kV/170kV'),
        ('Rated Continuous Current (Ir)', '630A, 1250A, 1600A, 2000A, 2500A, and 3150A frame sizes with forced or natural convection cooling'),
        ('Rated Short-Circuit Breaking Capacity (Isc)', '20 kA, 25 kA, and 31.5 kA (tested up to 40 kA at 12kV); rated short-circuit duration 4 seconds'),
        ('Arc Quenching Medium & Vacuum Level', 'Hermetically sealed ceramic vacuum bottle interrupter maintained at an ultra-high vacuum level of &le; 10&minus;5 Pa (10&minus;7 mbar)'),
        ('Contact Materials & Geometry', 'Cup-shaped copper-chromium (CuCr25/CuCr50) alloy contacts generating transverse or axial magnetic fields (AMF) to diffuse high-current arcs'),
        ('Operating Mechanism Architecture', 'Integrated modular spring energy storage mechanism (manual charging lever or 220V AC/DC electric charging motor) with trip-free linkage'),
        ('Mechanical & Electrical Endurance', 'Class M2 high mechanical endurance (&ge; 20,000 operational cycles); Class E2 electrical endurance (274 full short-circuit interruptions)'),
        ('Applicable International Standards', 'IEC 62271-100 (High-voltage switchgear and controlgear - Alternating-current circuit-breakers), GB/T 1984, CE certified, KEMA tested')
    ],
    faqs=[
        ('What is a Vacuum Circuit Breaker (VCB) and how does arc extinction occur inside a vacuum interrupter?',
         'A Vacuum Circuit Breaker (VCB) is a medium-voltage electrical switchgear apparatus (typically operating between 3.3kV and 36kV) '
         'that uses an ultra-high vacuum environment to extinguish electrical arcs. In traditional air or oil circuit breakers, arcs are cooled by blowing gas or liquid over them. '
         'In a VCB, the contacts are sealed inside a ceramic **vacuum interrupter** bottle maintained at a vacuum pressure lower than $10^{-5}\\,\\text{Pa}$. '
         'When the contacts separate under a fault, an arc is initiated not by ionizing surrounding air (since there are no gas molecules), but by vaporizing a minuscule amount of contact metal. '
         'Because the vacuum has immense dielectric strength, as soon as the AC current passes through natural zero, the metal vapor condenses back onto surrounding metal condensation shields '
         'in micro-seconds, instantly restoring dielectric insulation and preventing arc re-ignition.'),
        ('Why are Vacuum Circuit Breakers replacing SF6 gas circuit breakers in medium-voltage electrical substations?',
         'Vacuum circuit breakers have become the dominant global standard across 12kV to 36kV power distribution for three decisive reasons: '
         '1. **Environmental Decarbonization:** Sulfur hexafluoride (SF6) gas is the most potent greenhouse gas known to science, with a global warming potential (GWP) 23,500 times '
         'greater than CO2 and an atmospheric lifetime of 3,200 years. Environmental regulations (such as EU F-gas mandates) are banning SF6 equipment. VCBs are 100% SF6-free. '
         '2. **Zero Maintenance & Long Life:** Vacuum interrupters are hermetically sealed for life, requiring zero gas pressure refilling or oil purification, '
         'providing over 20,000 mechanical switching cycles (Class M2). '
         '3. **Explosion & Fire Safety:** Unlike oil or high-pressure gas breakers, VCBs present zero fire hazard, emit no toxic decomposition byproducts (like disulfur decafluoride), '
         'and operate with exceptionally low mechanical impact.'),
        ('What is the difference between a fixed-type VCB and a draw-out (withdrawable) truck-type VCB?',
         'The two mounting formats serve distinct substation architectural roles: '
         '<ul>'
         '<li><strong>Fixed-Type VCB:</strong> Bolted permanently to the switchgear steel structure with cable or busbar terminations. Cost-effective and compact, '
         'typically used in compact secondary ring main units (RMU) and packaged modular substations.</li>'
         '<li><strong>Draw-Out (Withdrawable Truck) VCB:</strong> Mounted on a wheeled steel trolley with self-aligning primary disconnect tulip contacts. '
         'Using a mechanical racking handle, the breaker can be racked between "Connected", "Test/Disconnected", and "Removed" positions behind closed switchgear doors. '
         'Automatic safety earthing shutters close over live busbars when the breaker is racked out, providing maximum safety during maintenance in primary substations.</li>'
         '</ul>')
    ],
    cta='Engineering 11kV, 24kV, or 33kV utility distribution substations, industrial power plant switchgear, or renewable solar/wind grid-tie stations requiring certified vacuum circuit breakers? YOMIN manufactures KEMA-tested VCBs built to IEC 62271-100 standards.',
    body='''
<h2>The Critical Defense for Medium-Voltage Power Grids</h2>
<p>Electrical substations, industrial processing plants, and commercial utility networks operating at medium voltages—from 3,300 to 36,000 volts—form the vital distribution bridge between high-voltage transmission lines and low-voltage consumers. In these networks, electrical equipment carries thousands of kilowatts of continuous power.</p>
<p>When an insulation breakdown, transformer flashover, or cable fault occurs on an 11kV or 33kV feeder, the prospective short-circuit fault current can reach 25,000 to 31,500 amperes. At medium voltages, an electrical arc will violently ionize open air into an explosive plasma fireball, destroying entire switchboard rooms unless interrupted in under 50 milliseconds.</p>
<p>The <strong>Vacuum Circuit Breaker (VCB)</strong> provides the ultimate medium-voltage interrupting technology, leveraging the unparalleled dielectric properties of a deep vacuum to extinguish high-voltage fault arcs safely, cleanly, and reliably.</p>

<h2>Inside the Vacuum Interrupter: The Physics of High-Vacuum Arc Quenching</h2>
<p>The core innovation of a modern VCB is the <strong>hermetically sealed ceramic vacuum interrupter</strong>. Maintained at an ultra-deep vacuum level below 10&minus;5 Pascals, it operates without any insulating oil or pressurized gas:</p>
<ul>
  <li><strong>Metal Vapor Diffusion Arc:</strong> At low currents, the arc burns as a diffuse multi-cathode spot discharge. The contact material—a specialized metallurgical alloy of copper and chromium (CuCr)—emits minimal vapor that disperses rapidly across the vacuum chamber.</li>
  <li><strong>Axial Magnetic Field (AMF) Contact Technology:</strong> Under extreme short-circuit currents (e.g. 31.5kA), ordinary arcs constrict into a stationary, concentrated hot spot that could melt contact faces. YOMIN vacuum interrupters feature spiral or slotted cup contact geometries that generate an <em>Axial Magnetic Field</em> parallel to the arc. This magnetic field forces the arc to remain diffuse and rotate at high velocity, preventing localized contact erosion and keeping arc voltage exceptionally low.</li>
  <li><strong>Ultra-Fast Dielectric Recovery:</strong> Because there are no ambient gas molecules to remain ionized, the instant the AC current waveform crosses natural zero, metal vapor condenses onto the internal stainless steel condensation shield within microseconds. The dielectric breakdown strength of the contact gap recovers at a staggering rate of tens of kilovolts per microsecond, completely preventing transient recovery voltage (TRV) restrikes.</li>
</ul>

<h2>Comparison: Air vs. Oil vs. SF6 vs. Vacuum Circuit Breakers</h2>
<table>
  <thead>
    <tr>
      <th>Technology Parameter</th>
      <th>Air Blast Circuit Breaker</th>
      <th>Oil Circuit Breaker (OCB)</th>
      <th>SF6 Gas Circuit Breaker</th>
      <th>Vacuum Circuit Breaker (VCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Arc Quenching Medium</strong></td>
      <td>High-pressure compressed air.</td>
      <td>Mineral insulating oil.</td>
      <td>Sulfur hexafluoride gas (SF6).</td>
      <td><strong>High vacuum (&le; 10&minus;5 Pa).</strong></td>
    </tr>
    <tr>
      <td><strong>Environmental Impact</strong></td>
      <td>Zero greenhouse impact.</td>
      <td>Toxic oil spill risk; flammable.</td>
      <td>Extreme GWP (23,500x CO2); EU bans.</td>
      <td><strong>100% Green & Eco-friendly; zero gas.</strong></td>
    </tr>
    <tr>
      <td><strong>Fire & Explosion Hazard</strong></td>
      <td>Low.</td>
      <td>High fire and explosion hazard.</td>
      <td>Low (produces toxic arcing gases).</td>
      <td><strong>Zero fire or explosion hazard.</strong></td>
    </tr>
    <tr>
      <td><strong>Mechanical Endurance</strong></td>
      <td>2,000 to 5,000 cycles.</td>
      <td>1,000 to 3,000 cycles.</td>
      <td>5,000 to 10,000 cycles.</td>
      <td><strong>Class M2: &ge; 20,000 cycles.</strong></td>
    </tr>
    <tr>
      <td><strong>Maintenance Requirement</strong></td>
      <td>Frequent compressor servicing.</td>
      <td>Frequent oil filtration/testing.</td>
      <td>Gas pressure monitoring & leak tests.</td>
      <td><strong>Virtually maintenance-free for life.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

VCB_FR = dict(
    lang='fr',
    dir='ltr',
    slug='substation-switching-what-is-a-vacuum-circuit-breaker-fr',
    title="Protection des Postes Moyenne Tension : Qu'est-ce qu'un Disjoncteur à Vide (VCB) ?",
    breadcrumb='Fusibles &amp; Protection',
    read='10 min de lecture',
    alt='Disjoncteur à vide 12kV moyenne tension débrochable sur chariot installé dans une cellule de poste électrique',
    desc=('Coupure et protection des réseaux moyenne tension en poste électrique : Qu\'est-ce qu\'un disjoncteur à vide (VCB) ? '
          'Comment les ampoules à vide éteignent les arcs de 12kV à 36kV sans gaz à effet de serre SF6, assurant un pouvoir de coupure de 31,5kA.'),
    model='Série ZN63 (VS1) / ZN28 : Disjoncteurs Moyenne Tension à Vide Intérieur & Extérieur (12kV–36kV)',
    category='Fusibles & Protection / Disjoncteurs Moyenne Tension à Vide',
    kw='disjoncteur à vide &middot; vcb &middot; disjoncteur moyenne tension &middot; ampoule à vide &middot; poste 11kv &middot; disjoncteur sans sf6',
    specs=[
        ('Tension Nominale & Niveaux d\'Isolement', 'Tension assignée 12kV, 24kV et 36kV ; tenue à fréquence industrielle 42kV/54kV/95kV ; tenue aux chocs de foudre (BIL) 75kV/125kV/170kV'),
        ('Courant Assigné de Service (Ir)', 'Calibres de 630A, 1250A, 1600A, 2000A, 2500A et 3150A avec refroidissement par convection naturelle ou forcée'),
        ('Pouvoir de Coupure en Court-Circuit (Isc)', '20 kA, 25 kA et 31,5 kA (testé jusqu\'à 40 kA sous 12kV) ; durée admissible de court-circuit de 4 secondes'),
        ('Milieu d\'Extinction & Niveau de Vide', 'Ampoule à vide étanche en céramique maintenue à un vide poussé supérieur à &le; 10&minus;5 Pa (10&minus;7 mbar)'),
        ('Matériau des Contacts d\'Arc', 'Alliage fritté cuivre-chrome (CuCr) avec géométrie à champ magnétique axial (AMF) pour maintenir l\'arc diffus'),
        ('Mécanisme de Commande', 'Mécanisme à accumulation d\'énergie par ressorts (armement manuel par levier ou électrique par motorisation 220V AC/DC)'),
        ('Endurance Mécanique et Électrique', 'Classe M2 pour l\'endurance mécanique (&ge; 20 000 manœuvres) ; Classe E2 pour l\'endurance électrique (274 coupures de court-circuit)'),
        ('Normes Internationales Applicables', 'CEI 62271-100 (Appareillage à haute tension - Disjoncteurs à courant alternatif), certifié CE et testé selon normes KEMA')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un disjoncteur à vide (VCB) et comment l\'arc électrique s\'éteint-il dans le vide absolu ?',
         'Un disjoncteur à vide (VCB - Vacuum Circuit Breaker) est un appareil d\'interruption moyenne tension (généralement de 3,3kV à 36kV) '
         'qui utilise le vide poussé comme milieu de coupure et d\'isolation. Dans un disjoncteur classique à air ou à huile, l\'arc est refroidi par un fluide. '
         'Dans un disjoncteur VCB, les contacts sont enfermés dans une **ampoule en céramique étanche** sous un vide inférieur à $10^{-5}\\,\\text{Pa}$. '
         'À la séparation des contacts, l\'arc ne provient pas de l\'ionisation de l\'air (puisqu\'il n\'y a aucune molécule de gaz), mais de l\'évaporation d\'une infime quantité '
         'de métal des contacts. Dès que le courant alternatif passe par zéro, la vapeur métallique se recondense sur les écrans métalliques en quelques microsecondes. '
         'La rigidité diélectrique du vide se régénère instantanément, empêchant tout réamorçage de l\'arc.'),
        ('Pourquoi les disjoncteurs à vide remplacent-ils massivement les disjoncteurs au gaz SF6 en moyenne tension ?',
         'Les disjoncteurs à vide sont devenus la référence absolue en distribution 12kV à 36kV pour trois raisons majeures : '
         '1. **Protection de l\'Environnement :** Le gaz hexafluorure de soufre (SF6) est le gaz à effet de serre le plus destructeur, avec un potentiel de réchauffement '
         'global (PRG) 23 500 fois supérieur au CO2. Les réglementations européennes interdisent désormais le SF6. Les disjoncteurs à vide sont 100% écologiques. '
         '2. **Maintenance Nulle et Longévité :** L\'ampoule à vide est scellée à vie, ne nécessitant aucune recharge de gaz ni traitement d\'huile, '
         'garantissant plus de 20 000 manœuvres mécaniques (Classe M2). '
         '3. **Sécurité Totale :** Aucun risque d\'explosion ou d\'incendie, aucune émission de gaz toxiques de décomposition lors de la coupure.'),
        ('Quelle est la différence entre un disjoncteur à vide fixe et un disjoncteur débrochable sur chariot ?',
         'Ces deux formats répondent à des besoins d\'exploitation distincts : '
         '<ul>'
         '<li><strong>Version Fixe :</strong> Boulonnée à demeure dans la cellule avec raccordement direct des barres ou câbles. Compacte et économique, '
         'elle équipe les tableaux de distribution secondaire et les postes compacts préfabriqués.</li>'
         '<li><strong>Version Débrochable sur Chariot :</strong> Montée sur un chariot mobile à roues avec pinces de raccordement arrière type tulipe. '
         'À l\'aide d\'une manivelle, l\'appareil passe de la position "En Service" à "Test/Déconnecté" ou "Extrait" porte fermée. '
         'Des volets métalliques de sécurité isolent automatiquement les jeux de barres sous tension, garantissant une sécurité maximale lors des maintenances.</li>'
         '</ul>')
    ],
    cta='Vous concevez des postes de distribution moyenne tension 11kV, 24kV ou 33kV, des cellules industrielles ou des raccordements éoliens/solaires nécessitant des disjoncteurs à vide ? YOMIN fabrique des VCB certifiés CEI 62271-100 conformes aux exigences KEMA.',
    body='''
<h2>L'Organe Maître de Sécurité des Réseaux Moyenne Tension</h2>
<p>Les postes de distribution électrique et les réseaux industriels fonctionnant en moyenne tension—de 3,3kV à 36kV—assurent l'acheminement de puissances électriques colossales entre les réseaux de transport et les usines de production.</p>
<p>Lorsqu'un défaut d'isolement ou un amorçage survient sur un câble souterrain ou un transformateur 20kV, le courant de court-circuit présumé atteint couramment 25 000 à 31 500 ampères. À ces niveaux de tension, un arc électrique à l'air libre ionise l'air en une boule de feu de plasma destructrice capable de détruire un poste entier en moins de 50 millisecondes.</p>
<p>Le <strong>Disjoncteur à Vide Moyenne Tension (VCB)</strong> représente la technologie d'interruption par excellence, exploitant les propriétés diélectriques exceptionnelles du vide poussé pour éteindre instantanément les arcs de court-circuit.</p>

<h2>La Physique de Coupure dans l'Ampoule à Vide</h2>
<p>L'innovation clé du disjoncteur VCB réside dans son <strong>ampoule de coupure sous vide scellée en céramique</strong> exempte de tout fluide toxique :</p>
<ul>
  <li><strong>Arc Diffus à Vapeur Métallique :</strong> Aux faibles courants, l'arc brûle sous forme de décharge diffuse à multiples taches cathodiques. L'alliage spécial cuivre-chrome (CuCr) émet une vapeur métallique minime qui se disperse instantanément.</li>
  <li><strong>Technologie à Champ Magnétique Axial (AMF) :</strong> Sous des courants de court-circuit extrêmes (ex. 31,5kA), l'arc aurait tendance à se contracter en un point chaud détruisant les contacts. Les contacts YOMIN génèrent un <em>champ magnétique axial</em> qui force l'arc à rester diffus et en rotation rapide, préservant l'intégrité des portées de contact.</li>
  <li><strong>Régénération Diélectrique Ultra-Rapide :</strong> Dès le passage à zéro du courant alternatif, la vapeur métallique se condense sur les écrans métalliques en quelques microsecondes, reconstituant une barrière isolante capable de tenir des dizaines de kilovolts par microseconde.</li>
</ul>

<h2>Tableau Comparatif : Disjoncteur à Air vs. Huile vs. SF6 vs. Vide (VCB)</h2>
<table>
  <thead>
    <tr>
      <th>Critère de Comparaison</th>
      <th>Disjoncteur à Air Comprimé</th>
      <th>Disjoncteur à Bain d'Huile</th>
      <th>Disjoncteur au Gaz SF6</th>
      <th>Disjoncteur à Vide (VCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Milieu de Coupure</strong></td>
      <td>Air comprimé haute pression.</td>
      <td>Huile minérale diélectrique.</td>
      <td>Hexafluorure de soufre (SF6).</td>
      <td><strong>Vide poussé (&le; 10&minus;5 Pa).</strong></td>
    </tr>
    <tr>
      <td><strong>Impact Écologique</strong></td>
      <td>Neutre.</td>
      <td>Risque de pollution des sols.</td>
      <td>Gaz à effet de serre extrême (23 500x CO2).</td>
      <td><strong>100% Écologique et sans gaz.</strong></td>
    </tr>
    <tr>
      <td><strong>Risque d'Incendie</strong></td>
      <td>Faible.</td>
      <td>Risque majeur d'incendie et d'explosion.</td>
      <td>Faible (dégagement de sous-produits toxiques).</td>
      <td><strong>Aucun risque d'incendie ou d'explosion.</strong></td>
    </tr>
    <tr>
      <td><strong>Endurance Mécanique</strong></td>
      <td>2 000 à 5 000 manœuvres.</td>
      <td>1 000 à 3 000 manœuvres.</td>
      <td>5 000 à 10 000 manœuvres.</td>
      <td><strong>Classe M2 : &ge; 20 000 manœuvres.</strong></td>
    </tr>
    <tr>
      <td><strong>Maintenance Requise</strong></td>
      <td>Maintenance lourde du compresseur.</td>
      <td>Filtration et analyse d'huile régulières.</td>
      <td>Contrôle permanent de pression et fuites.</td>
      <td><strong>Totalement sans entretien à vie.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

VCB_ES = dict(
    lang='es',
    dir='ltr',
    slug='substation-switching-what-is-a-vacuum-circuit-breaker-es',
    title='Protección en Subestaciones de Media Tensión: ¿Qué es un Disyuntor de Vacío (VCB)?',
    breadcrumb='Fusibles y Protección',
    read='10 min de lectura',
    alt='Disyuntor de vacío de media tensión de 12kV extraíble sobre carro instalado dentro de una celda de subestación eléctrica',
    desc=('Maniobra y protección en subestaciones de media tensión: ¿Qué es un disyuntor de vacío (VCB)? '
          'Cómo las botellas de vacío extinguen arcos de 12kV a 36kV sin gas SF6 de efecto invernadero, proporcionando una capacidad de ruptura de 31,5kA.'),
    model='Serie ZN63 (VS1) / ZN28: Disyuntores de Media Tensión en Vacío para Interior y Exterior (12kV–36kV)',
    category='Fusibles y Protección / Disyuntores de Media Tensión en Vacío',
    kw='disyuntor de vacío &middot; vcb &middot; interruptor de media tensión &middot; botella de vacío &middot; subestación 11kv 33kv &middot; disyuntor sin sf6',
    specs=[
        ('Tensión Nominal y Niveles de Aislamiento', 'Tensión asignada 12kV, 24kV y 36kV; tensión soportada a frecuencia industrial 42kV/54kV/95kV; impulso tipo rayo (BIL) 75kV/125kV/170kV'),
        ('Corriente Nominal Continua (Ir)', 'Calibres de 630A, 1250A, 1600A, 2000A, 2500A y 3150A con refrigeración natural o por ventilación forzada'),
        ('Capacidad de Ruptura en Cortocircuito (Isc)', '20 kA, 25 kA y 31,5 kA (probado hasta 40 kA a 12kV); duración admisible de cortocircuito de 4 segundos'),
        ('Medio de Extinción y Nivel de Vacío', 'Botella de vacío sellada de cerámica mantenida a un ultra-alto vacío de &le; 10&minus;5 Pa (10&minus;7 mbar)'),
        ('Material y Geometría de Contactos', 'Aleación sinterizada de cobre-cromo (CuCr) con diseño de campo magnético axial (AMF) para mantener el arco difuso'),
        ('Mecanismo de Operación por Resortes', 'Mecanismo modular integrado de acumulación de energía por resortes (carga manual con palanca o motorizada 220V AC/DC)'),
        ('Endurancia Mecánica y Eléctrica', 'Clase M2 de alta endurancia mecánica (&ge; 20.000 maniobras); Clase E2 de endurancia eléctrica (274 cortes a cortocircuito pleno)'),
        ('Normas Internacionales Aplicables', 'IEC 62271-100 (Aparamenta de alta tensión - Interruptores para corriente alterna), certificado CE y probado bajo normas KEMA')
    ],
    faqs=[
        ('¿Qué es un disyuntor de vacío (VCB) y cómo se apaga el arco eléctrico dentro del vacío?',
         'Un disyuntor de vacío (VCB - Vacuum Circuit Breaker) es un interruptor automático de media tensión (típicamente entre 3,3kV y 36kV) '
         'que utiliza el alto vacío como medio dieléctrico para extinguir arcos eléctricos. A diferencia de los interruptores de aire o aceite, '
         'en un VCB los contactos están encerrados en una **botella de cerámica sellada** al vacío a presiones inferiores a $10^{-5}\\,\\text{Pa}$. '
         'Al abrirse los contactos bajo falla, el arco no se produce por ionización del aire (no hay moléculas gaseosas), sino por la evaporación de una mínima '
         'cantidad de metal de los contactos. Al pasar la corriente alterna por su cruce natural por cero, el vapor metálico se condensa en microsegundos '
         'sobre las pantallas metálicas internas, restableciendo de inmediato la rigidez dieléctrica y evitando el cebado del arco.'),
        ('¿Por qué los disyuntores de vacío están reemplazando a los disyuntores de gas SF6 en media tensión?',
         'Los disyuntores de vacío dominan el mercado de media tensión de 12kV a 36kV por tres razones determinantes: '
         '1. **Sostenibilidad Ambiental:** El gas hexafluoruro de azufre (SF6) es el gas de efecto invernadero más potente del planeta, con un potencial de calentamiento '
         '23.500 veces superior al CO2. Las normativas internacionales están prohibiendo el SF6. Los disyuntores de vacío son 100% ecológicos. '
         '2. **Cero Mantenimiento:** La botella de vacío está herméticamente sellada de por vida, sin necesidad de recargar gas ni filtrar aceite, '
         'garantizando más de 20.000 operaciones mecánicas (Clase M2). '
         '3. **Seguridad contra Incendios:** No presentan riesgo de explosión ni fuego, y no generan subproductos tóxicos de descomposición tras un cortocircuito.'),
        ('¿Cuál es la diferencia entre un disyuntor VCB fijo y uno extraíble sobre carro?',
         'Ambos formatos responden a distintas necesidades de diseño en subestaciones: '
         '<ul>'
         '<li><strong>Tipo Fijo:</strong> Se atornilla directamente a la estructura de la celda con conexiones fijas de barras o cables. Es compacto y económico, '
         'ideal para centros de transformación secundarios y celdas compactas tipo RMU.</li>'
         '<li><strong>Tipo Extraíble sobre Carro:</strong> Montado sobre un chasis con ruedas y contactos posteriores tipo tulipa. Mediante una manivela, '
         'el disyuntor se desplaza entre las posiciones "Conectado", "Prueba/Desconectado" y "Extraído" con la puerta cerrada. '
         'Guillotinas metálicas de seguridad cubren automáticamente las barras energizadas al extraerlo, brindando máxima seguridad al personal de mantenimiento.</li>'
         '</ul>')
    ],
    cta='¿Diseña subestaciones de media tensión de 11kV, 24kV o 33kV, celdas de distribución industrial o plantas renovables que requieren disyuntores de vacío certificados? YOMIN fabrica interruptores VCB conformes con la norma IEC 62271-100 y probados en laboratorios KEMA.',
    body='''
<h2>La Protección Definitiva en Redes de Media Tensión</h2>
<p>Las subestaciones de distribución y las redes industriales que operan en media tensión—entre 3.300 y 36.000 voltios—son el enlace vital que transporta grandes bloques de energía desde las líneas de transmisión hasta las plantas de producción.</p>
<p>Cuando ocurre una falla de aislamiento en un transformador de potencia o un cable de 13,8kV o 34,5kV, la corriente de cortocircuito puede alcanzar entre 25.000 y 31.500 amperios. A estos voltajes, un arco eléctrico en aire libre forma una bola de plasma explosiva capaz de destruir salas eléctricas completas en menos de 50 milisegundos.</p>
<p>El <strong>Disyuntor de Vacío de Media Tensión (VCB)</strong> constituye la tecnología de corte más avanzada y confiable, aprovechando las extraordinarias propiedades del vacío para despejar fallas con total seguridad.</p>

<h2>La Física de Extinción de Arco en la Botella de Vacío</h2>
<p>El componente principal del disyuntor VCB es su <strong>interruptor en botella de vacío de cerámica</strong> libre de gases contaminantes:</p>
<ul>
  <li><strong>Arco Difuso por Vapor Metálico:</strong> En corrientes de carga normales, el arco se mantiene en estado difuso. La aleación sinterizada de cobre y cromo (CuCr) emite una mínima nube de vapor metálico que se dispersa inmediatamente en la cámara.</li>
  <li><strong>Contactos con Campo Magnético Axial (AMF):</strong> Ante corrientes de cortocircuito severas (31,5kA), el arco tendería a concentrarse en un punto caliente que fundiría los contactos. Los contactos YOMIN generan un <em>campo magnético axial</em> que mantiene el arco difuso y en rotación constante, minimizando la erosión del metal.</li>
  <li><strong>Recuperación Dieléctrica en Microsegundos:</strong> Al no haber gas ionizado, en el instante en que la corriente pasa por cero, el vapor metálico se condensa en los blindajes internos en microsegundos, restableciendo una barrera dieléctrica de decenas de kilovoltios por microsegundo que impide cualquier reencendido del arco.</li>
</ul>

<h2>Tabla Comparativa: Interruptor de Aire vs. Aceite vs. SF6 vs. Vacío (VCB)</h2>
<table>
  <thead>
    <tr>
      <th>Parámetro Tecnológico</th>
      <th>Interruptor de Aire Comprimido</th>
      <th>Interruptor en Aceite (OCB)</th>
      <th>Interruptor en Gas SF6</th>
      <th>Disyuntor de Vacío (VCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Medio de Extinción</strong></td>
      <td>Aire comprimido a alta presión.</td>
      <td>Aceite mineral aislante.</td>
      <td>Gas hexafluoruro de azufre (SF6).</td>
      <td><strong>Alto vacío (&le; 10&minus;5 Pa).</strong></td>
    </tr>
    <tr>
      <td><strong>Impacto Ambiental</strong></td>
      <td>Cero impacto ecológico.</td>
      <td>Riesgo de derrames contaminantes.</td>
      <td>Efecto invernadero crítico (23.500x CO2).</td>
      <td><strong>100% Ecológico y libre de gases.</strong></td>
    </tr>
    <tr>
      <td><strong>Riesgo de Fuego / Explosión</strong></td>
      <td>Bajo.</td>
      <td>Alto peligro de incendio y explosión.</td>
      <td>Bajo (genera subproductos tóxicos).</td>
      <td><strong>Cero riesgo de incendio o explosión.</strong></td>
    </tr>
    <tr>
      <td><strong>Vida Útil Mecánica</strong></td>
      <td>2.000 a 5.000 maniobras.</td>
      <td>1.000 a 3.000 maniobras.</td>
      <td>5.000 a 10.000 maniobras.</td>
      <td><strong>Clase M2: &ge; 20.000 maniobras.</strong></td>
    </tr>
    <tr>
      <td><strong>Mantenimiento Exigido</strong></td>
      <td>Mantenimiento frecuente de compresores.</td>
      <td>Filtración y análisis periódico de aceite.</td>
      <td>Control constante de fugas de gas.</td>
      <td><strong>Totalmente libre de mantenimiento.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

VCB_AR = dict(
    lang='ar',
    dir='rtl',
    slug='substation-switching-what-is-a-vacuum-circuit-breaker-ar',
    title='حماية محطات التوزيع الكهربائي متوسطة الجهد: ما هو قاطع الدائرة المفرغ من الهواء (VCB)؟',
    breadcrumb='المصهرات والحماية',
    read='10 دقائق قراءة',
    alt='قاطع دائرة مفرغ من الهواء متوسط الجهد بجهد 12 كيلو فولت قابل للسحب على عربة مثبت داخل خلية لوحة توزيع محطة فرعية',
    desc=('التحكم والحماية في محطات التوزيع الكهربائي متوسطة الجهد: ما هو قاطع الدائرة المفرغ من الهواء (VCB)؟ '
          'كيف تخمد زجاجات التفريغ أقواس الجهد العالي من 12kV إلى 36kV بدون غاز SF6 المسبب للاحتباس الحراري، بسعة قطع لتيارات القصر تصل إلى 31.5 كيلو أمبير.'),
    model='سلسلة ZN63 (VS1) / ZN28: قواطع الدوائر المفرغة من الهواء متوسطة الجهد للتركيب الداخلي والخارجي (12kV–36kV)',
    category='المصهرات والحماية / قواطع الدوائر متوسطة الجهد المفرغة من الهواء',
    kw='قاطع مفرغ من الهواء &middot; vcb &middot; قاطع متوسط الجهد &middot; غرفة التفريغ &middot; محطة تحويل 11kv &middot; قاطع خالي من sf6',
    specs=[
        ('الجهد الاسمي ومستويات العزل', 'الجهد المقنن 12kV و 24kV و 36kV؛ جهد تحمل تردد الشبكة 42kV/54kV/95kV؛ جهد صدمة الصاعقة (BIL) 75kV/125kV/170kV'),
        ('التيار الاسمي المستمر (Ir)', 'سعات 630A و 1250A و 1600A و 2000A و 2500A و 3150A مع تبريد بالحمل الحراري الطبيعي أو القسري'),
        ('سعة كسر تيار القصر الاسمي (Isc)', '20 kA و 25 kA و 31.5 kA (مختبر حتى 40 kA عند 12kV)؛ زمن تحمل تيار القصر المقنن 4 ثوانٍ'),
        ('وسط إخماد القوس ومستوى التفريغ', 'غرفة تفريغ سيراميكية محكمة الإغلاق تحت ضغط تفريغ فائق الدقة يقل عن &le; 10&minus;5 باسكال (10&minus;7 ملي بار)'),
        ('مادة وهندسة نقاط التلامس', 'سبيكة نحاس-كروم متكلسة (CuCr) بتصميم مجال مغناطيسي محوري (AMF) للحفاظ على القوس في حالة انتشار ومنع تآكل المعادن'),
        ('آلية التشغيل وتخزين طاقة الياي', 'آلية تشغيل متكاملة بنظام تخزين الطاقة في يايات نابضة (شحن يدوي بالذراع أو بمحرك كهربائي 220V AC/DC) مع فصل حر'),
        ('التحمل الميكانيكي والكهربائي', 'فئة M2 للتحمل الميكانيكي العالي (&ge; 20,000 دورة تشغيل)؛ فئة E2 للتحمل الكهربائي (274 عملية قطع لتيار قصر كامل)'),
        ('المعايير الدولية المعتمدة', 'IEC 62271-100 (المفاتيح وأجهزة التحكم عالية الجهد - قواطع التيار المتردد)، شهادة CE ومختبر وفقاً لمعايير KEMA الدولية')
    ],
    faqs=[
        ('ما هو قاطع الدائرة المفرغ من الهواء (VCB) وكيف ينطفئ القوس الكهربائي في الفراغ المطلق؟',
         'قاطع الدائرة المفرغ من الهواء (Vacuum Circuit Breaker - VCB) هو جهاز فصل وحماية كهربائي متوسط الجهد (يعمل عادة بين 3.3 و 36 كيلو فولت) '
         'يستخدم الفراغ الفائق كوسط عازل لإطفاء الأقواس الكهربائية. على عكس القواطع التقليدية التي تستخدم الهواء المضغوط أو الزيت لتبريد القوس، '
         'توضع نقاط التلامس في قاطع VCB داخل **غرفة سيراميكية مفرغة من الهواء** تماماً تحت ضغط يقل عن $10^{-5}\\,\\text{Pa}$. '
         'عند تباعد نقاط التلامس أثناء العطل، لا ينشأ القوس عن تأين جزيئات الغاز (لعدم وجود أي جزيئات)، بل ينشأ عن تبخر كمية ضئيلة جداً من معدن نقاط التلامس. '
         'وبمجرد مرور موجة التيار المتردد بنقطة الصفر الطبيعية، يتكثف البخار المعدني على الدروع المعدنية الداخلية في أجزاء من الميكروثانية، '
         'مما يعيد القوة العازلة للفراغ فوراً ويمنع إعادة اشتعال القوس نهائياً.'),
        ('لماذا تحل قواطع التفريغ (VCB) محل قواطع غاز سداسي فلوريد الكبريت (SF6) في محطات الجهد المتوسط؟',
         'أصبحت قواطع التفريغ المعيار العالمي الأول في شبكات الجهد المتوسط من 12 إلى 36 كيلو فولت لثلاثة أسباب رئيسية: '
         '1. **الحفاظ على البيئة والمناخ:** يُعد غاز سداسي فلوريد الكبريت (SF6) أخطر غاز دفيء معروف علمياً، إذ تفوق قدرته على إحداث الاحتباس الحراري غاز ثاني أكسيد الكربون '
         'بـ 23,500 مرة، ويمتد بقاؤه في الغلاف الجوي لـ 3,200 عام. تفرض القوانين الدولية حظر استخدامه. وتعد قواطع التفريغ خالية 100% من غاز SF6. '
         '2. **انعدام الصيانة والعمر المديد:** غرف التفريغ محكمة الغلق مدى الحياة، ولا تحتاج لأي إعادة تعبئة غاز أو تكرير زيت، وتوفر أكثر من 20,000 دورة تشغيل ميكانيكية. '
         '3. **السلامة المطلقة من الحرائق:** لا تسبب أي خطر انفجار أو اشتعال، ولا تنتج أي غازات كيميائية سامة عند قطع تيارات القصر.'),
        ('ما الفرق بين قاطع التفريغ الثابت وقاطع التفريغ القابل للسحب على عربة داخل خلايا المحطة؟',
         'يخدم كلا التصميمين متطلبات تشغيلية محددة في محطات التحويل: '
         '<ul>'
         '<li><strong>النوع الثابت (Fixed Type):</strong> يُثبت بمسامير مباشرة في هيكل الخلية مع توصيل ثابت للكابلات أو القضبان. يتميز بصغر الحجم والتكلفة الاقتصادية، '
         'ويستخدم في وحدات الربط الحلقي (RMU) المدمجة والمحطات الجاهزة.</li>'
         '<li><strong>النوع القابل للسحب (Draw-Out Truck Type):</strong> مركب على عربة فولاذية متحركة بعجلات مع نقاط تلامس خلفية من نوع الزهرة (Tulip). '
         'باستخدام ذراع تدوير ميكانيكي، ينتقل القاطع بين أوضاع "في الخدمة" و"فحص/مفصول" و"مستخرج بالكامل" والباب مغلق تماماً. '
         'تغلق ستائر معدنية واقية تلقائياً على قضبان التوزيع الحية عند سحب القاطع، مما يوفر أقصى درجات الأمان لفرق الصيانة في المحطات الرئيسية.</li>'
         '</ul>')
    ],
    cta='هل تخطط لبناء محطات تحويل كهربائية متوسطة الجهد بقدرات 11kV أو 24kV أو 33kV، أو خلايا توزيع صناعية ومحطات ربط طاقة متجددة تتطلب قواطع تفريغ معتمدة؟ تصنع يمين (YOMIN) قواطع VCB مختبرة في مختبرات KEMA ومطابقة لمعيار IEC 62271-100 الدولي.',
    body='''
<h2>صمام الأمان الأساسي لشبكات التوزيع الكهربائية متوسطة الجهد</h2>
<p>تشكل محطات التحويل الفرعية والشبكات الصناعية العاملة على مستويات الجهد المتوسط—من 3,300 إلى 36,000 فولت—حلقة الوصل الحيوية لنقل وتوزيع القدرات الكهربائية الهائلة من خطوط النقل العالي إلى المجمعات الصناعية والمدن.</p>
<p>فعند حدوث انهيار في العزل أو قصر كهربائي مباشر على كابل مغذٍ بجهد 11 أو 33 كيلو فولت، يمكن لتيار القصر أن يقفز إلى 25,000 أو 31,500 أمبير. وتحت هذه الجهود العالية، يتحول القوس الكهربائي في الهواء الطلق إلى كرة لهب بلازمية تنفجر مسببة تدمير خلايا التوزيع بالكامل في أقل من 50 جزءاً من الألف من الثانية ما لم يتم فصلها فوراً.</p>
<p>يمثل <strong>قاطع الدائرة المفرغ من الهواء (VCB)</strong> ذروة تكنولوجيا الفصل والحماية في شبكات الجهد المتوسط، حيث يستثمر الخصائص العازلة الفائقة للفراغ المطلق لإخماد أقواس القصر الكهربائي بأمان وموثوقية متناهية.</p>

<h2>فيزياء إخماد القوس الكهربائي داخل غرفة التفريغ السيراميكية</h2>
<p>يكمن الابتكار الهندسي لقواطع VCB في <strong>غرفة التفريغ السيراميكية محكمة الإغلاق</strong> الخالية تماماً من الزيوت والغازات الكيميائية الضارة:</p>
<ul>
  <li><strong>القوس المنتشر بالبخار المعدني:</strong> عند تيارات الحمل العادية، يحترق القوس في حالة انتشار رقيقة عبر نقاط كاثودية متعددة. وتطلق سبيكة النحاس والكروم (CuCr) المتخصصة كمية ضئيلة جداً من البخار المعدني الذي يتشتت فوراً داخل الفراغ.</li>
  <li><strong>تقنية المجال المغناطيسي المحوري (AMF):</strong> عند تيارات القصر العنيفة (مثل 31.5kA)، تميل الأقواس للتجمع في بؤرة ساخنة قد تصهر المعدن. تولد نقاط تلامس يمين (YOMIN) <em>مجالاً مغناطيسياً محورياً</em> موازياً للقوس يجبره على البقاء في حالة انتشار والدوران السريع، مما يمنع التآكل الموضعي ويحافظ على انخفاض حرارة التلامس.</li>
  <li><strong>الاستعادة العازلة فائقة السرعة:</strong> لعدم وجود جزيئات غاز متأينة، يتكثف البخار المعدني على الدروع الداخلية في أجزاء من الميكروثانية بمجرد مرور التيار بنقطة الصفر، لتبلغ سرعة استعادة القوة العازلة عشرات الكيلوفولت في الميكروثانية الواحدة، مما يحبط أي محاولة لعودة اشتعال القوس.</li>
</ul>

<h2>جدول مقارنة تكنولوجي: القواطع الهوائية مقابل القواطع الزيتية مقابل قواطع SF6 مقابل قواطع التفريغ (VCB)</h2>
<table>
  <thead>
    <tr>
      <th>المعيار التكنولوجي</th>
      <th>قاطع الهواء المضغوط</th>
      <th>القاطع الزيتي (OCB)</th>
      <th>قاطع غاز سداسي فلوريد الكبريت (SF6)</th>
      <th>قاطع التفريغ من الهواء (VCB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>وسط إخماد القوس</strong></td>
      <td>هواء مضغوط عالي الضغط.</td>
      <td>زيت معدني عازل.</td>
      <td>غاز سداسي فلوريد الكبريت (SF6).</td>
      <td><strong>فراغ فائق الدقة (&le; 10&minus;5 باسكال).</strong></td>
    </tr>
    <tr>
      <td><strong>الأثر البيئي والمناخي</strong></td>
      <td>عديم الأثر المناخي.</td>
      <td>خطر تلوث التربة وقابلية الاشتعال.</td>
      <td>غاز دفيء فائق الخطورة (23,500 ضعف CO2).</td>
      <td><strong>100% صديق للبيئة وخالٍ تماماً من الغازات.</strong></td>
    </tr>
    <tr>
      <td><strong>مخاطر الحريق والانفجار</strong></td>
      <td>منخفضة.</td>
      <td>عالية جداً وخطر انفجار الزيت وارد.</td>
      <td>منخفضة (ينتج غازات ثانوية سامة).</td>
      <td><strong>منعدمة تماماً ولا يوجد أي خطر حريق.</strong></td>
    </tr>
    <tr>
      <td><strong>التحمل الميكانيكي</strong></td>
      <td>من 2,000 إلى 5,000 دورة.</td>
      <td>من 1,000 إلى 3,000 دورة.</td>
      <td>من 5,000 إلى 10,000 دورة.</td>
      <td><strong>فئة M2: أكثر من 20,000 دورة تشغيل.</strong></td>
    </tr>
    <tr>
      <td><strong>متطلبات الصيانة الدورية</strong></td>
      <td>صيانة دورية معقدة لضاغط الهواء.</td>
      <td>تنقية الزيت واختبارات دورية مستمرة.</td>
      <td>مراقبة ضغط الغاز وفحص التسريبات.</td>
      <td><strong>منعدمة الصيانة تماماً ومغلق مدى الحياة.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

ALL_MULTILINGUAL_POSTS_0929_B2 = [
    DC_SPD_EN, DC_SPD_FR, DC_SPD_ES, DC_SPD_AR,
    VCB_EN, VCB_FR, VCB_ES, VCB_AR
]
