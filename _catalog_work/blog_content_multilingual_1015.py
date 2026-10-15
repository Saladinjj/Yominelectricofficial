# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-15:
1. Automatic Power Factor Controllers for Reactive Power Compensation (EN, FR, ES, AR)
2. Station Post Insulators for Substation Busbar Support (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. AUTOMATIC POWER FACTOR CONTROLLER (EN, FR, ES, AR)
# ==============================================================================

APFC_EN = dict(
    lang='en',
    dir='ltr',
    slug='power-factor-correction-what-is-an-automatic-power-factor-controller',
    title='Power Factor Correction: What Is an Automatic Power Factor Controller?',
    breadcrumb='Power Quality &amp; Capacitor Banks',
    read='10 min read',
    alt='Digital Automatic Power Factor Controller (Model JKL5C series) flush-mounted on the door of an industrial APFC capacitor bank panel displaying power factor and step LEDs',
    desc=('Industrial power factor correction, capacitor bank switching, and utility penalty mitigation: What is an automatic power factor controller (APFC controller)? '
          'How microprocessor-driven reactive power Q-calculation, circular step switching, hunting prevention, over-voltage/harmonic protection, and RS485 Modbus optimize power quality.'),
    model='Model JKL5C / RPCF Series Automatic Reactive Power Compensation Controllers (6 to 16 Relay Steps, Dynamic Q Calculation, Circular Cycling, RS485 Modbus, IEC 61000-4)',
    category='Power Quality & Capacitor Banks / Automatic Power Factor Controllers',
    kw='what is an automatic power factor controller &middot; automatic power factor controller &middot; apfc controller &middot; power factor controller 12 step &middot; reactive power controller &middot; jkl5c controller',
    specs=[
        ('Rated System Operating Voltage Class', 'Sampling voltage input: 220V / 380V / 400V / 415V AC (&plusmn;20%, 50/60 Hz, Phase-to-Neutral or Phase-to-Phase)'),
        ('Current Sampling Input Rating ($I_{in}$)', 'Standard CT secondary current input: 0–5A (Class 0.5 or Class 0.2 input with internal burden $< 0.5$ VA)'),
        ('Available Control Output Steps', 'Multi-stage relay output configurations: 6, 8, 10, 12, 14, or 16 step contact outputs (rated 250V AC / 5A resistive)'),
        ('Power Factor Target & Sensitivity Setting', 'Programmable target $\cos\phi$: 0.800 inductive to 0.800 capacitive (factory default target: 0.950 to 0.980 lag)'),
        ('Switching Control Algorithms Supported', 'Dynamic Reactive Power ($Q$ kvar) calculation mode, Progressive Step mode, and Equal-Capacity Circular Cycling mode'),
        ('Capacitor Step Switching Delay Time', 'Programmable switching delay: 1 to 300 seconds (ensures complete capacitor discharge via bleed resistors before re-energization)'),
        ('Harmonic & Electrical Protection Features', 'Over-voltage trip, under-voltage lockout, current unbalance detection, over-temperature cutoff, and THD-V harmonic alarm'),
        ('Digital Communication & Telemetry Port', 'Standard isolated RS485 serial communication port supporting Modbus RTU protocol for factory SCADA / EMS integration')
    ],
    faqs=[
        ('What is an Automatic Power Factor Controller (APFC Controller) and what is its primary function?',
         'An Automatic Power Factor Controller—frequently designated as an APFC relay, reactive power controller, or automatic capacitor bank regulator—is '
         'a specialized microprocessor-based digital monitoring and switching device that serves as the "intelligent brain" of an industrial '
         'Automatic Power Factor Correction (APFC) capacitor bank panel. '
         'In commercial and industrial electrical distribution systems: '
         '<ul>'
         '<li><strong>The Low Power Factor Problem:</strong> Industrial facilities operate large inductive loads—such as induction motors, '
         'welders, arc furnaces, and transformers—that consume both active power (kW) and reactive power (kvar). '
         'This reactive magnetization current causes the system displacement power factor ($\cos\phi$) to drop from 1.0 down to 0.70 or lower. '
         'Low power factor overloads supply transformers, creates excessive voltage drop along cables, and triggers massive financial penalty surcharges '
         'on monthly electricity utility bills.</li>'
         '<li><strong>The APFC Controller Solution:</strong> The controller continuously samples line voltage ($V$) and load current ($I$ via a current transformer), '
         'calculates real-time active power ($P$), reactive power ($Q$), and instantaneous power factor ($\cos\phi$). '
         'Whenever the measured power factor falls below the user-programmed target (e.g. 0.98), the controller automatically calculates the exact reactive kvar '
         'deficit and sequentially energizes output relays connected to heavy-duty capacitor switching contactors. '
         'This injects precisely the right amount of capacitive reactive power to neutralize inductive lag, keeping the utility meter at near-unity power factor '
         'and completely eliminating power factor penalty fees.</li>'
         '</ul>'),
        ('How do Circular and Progressive step switching algorithms prevent capacitor degradation?',
         'Conventional basic controllers always switch capacitor Step 1 first, followed by Step 2 and Step 3. '
         'This causes Step 1 to endure thousands more switching operations than later steps, leading to premature dielectric breakdown of the first capacitor. '
         'YOMIN JKL5C Series APFC Controllers solve this through intelligent algorithms: '
         '<ul>'
         '<li><strong>Equal-Capacity Circular Cycling (FIFO - First In, First Out):</strong> For capacitor steps with identical kvar ratings, '
         'the controller cycles switching duty evenly across all banks. The capacitor bank that has been connected the longest is disconnected first, '
         'and the bank that has been resting the longest is energized first. This equalizes thermal stress and contact wear across all contactors and capacitors.</li>'
         '<li><strong>Anti-Hunting Deadband Logic:</strong> The controller maintains a programmable reactive power deadband ($C/k$ sensitivity ratio). '
         'It will never energize a capacitor step if switching that step would push the system into leading (capacitive) power factor, '
         'preventing continuous cyclic switching ("hunting") that burns out contactors.</li>'
         '</ul>'),
        ('Why is a programmable switching discharge delay critical for capacitor safety?',
         'When an AC power capacitor is disconnected from the live busbar, it retains a trapped DC charge equal to the peak line voltage (up to $1.414 \times V_{RMS}$). '
         'Discharge resistors built into the capacitor require 30 to 60 seconds to safely bleed this residual voltage down below 50V. '
         'If a controller re-energizes a charged capacitor while its residual voltage is in opposite phase to the incoming AC sine wave, '
         'the resulting phase opposition causes a catastrophic inrush current surge exceeding <strong>200 times rated current</strong>, '
         'welding contactor points and rupturing capacitor casing. '
         'YOMIN controllers enforce a programmable inter-step re-switching delay (default 60 seconds) that physically locks out any capacitor step '
         'from being reconnected until it has fully discharged.')
    ],
    cta='Designing industrial APFC capacitor panels, commercial power factor correction banks, or facility energy efficiency upgrades requiring certified IEC 61000-4 automatic power factor controllers (6 to 16 relay steps, dynamic Q switching, RS485 Modbus)? YOMIN manufactures precision JKL5C/RPCF series controllers.',
    body='''
<h2>The Intelligent Master Brain of Industrial Power Factor Correction Systems</h2>
<p>In modern industrial manufacturing plants, commercial high-rise towers, automated sorting logistics hubs, and heavy process facilities worldwide, electrical efficiency directly dictates operational profitability.</p>
<p>Industrial machinery—such as electric induction motors, centrifugal chillers, air compressors, stamping presses, and induction furnaces—relies on electromagnetic fields to operate. These inductive magnetic fields draw massive amounts of lagging reactive power ($Q$ kvar) from the power grid without performing mechanical work.</p>
<p>When reactive power flows uncompensated through factory transformers and distribution cables, it inflates total apparent power demand ($S$ kVA), increases $I^2R$ resistive heat losses, drags system voltage down, and causes regional electric utilities to levy punitive low power factor financial penalty surcharges that can add tens of thousands of dollars to monthly utility bills.</p>
<p>The <strong>Automatic Power Factor Controller (Model JKL5C / RPCF Series)</strong> provides the universal digital solution: an advanced microprocessor-based instrument that continuously calculates facility reactive power demand and dynamically switches multi-stage capacitor banks to maintain target power factor ($\cos\phi \ge 0.98$) with zero manual intervention.</p>

<h2>Engineering Anatomy: Inside a Model JKL5C Automatic Power Factor Controller</h2>
<ol>
  <li><strong>Dual High-Speed Microcontroller Engine:</strong> Continuously samples AC voltage and CT secondary current at 64 samples per cycle, executing real-time Fast Fourier Transforms (FFT) to accurately extract fundamental active power, reactive power, and displacement power factor even in the presence of severe harmonic distortion.</li>
  <li><strong>High-Visibility Multi-Parameter Digital Display:</strong> Dual digital display displays system power factor, active power (kW), reactive power (kvar), line voltage (V), load current (A), total harmonic distortion (THD-V), and ambient cabinet temperature simultaneously.</li>
  <li><strong>Multi-Channel Isolated Relay Output Array:</strong> Features 6, 8, 12, or 16 heavy-duty electro-mechanical output relays (rated 250V AC, 5A) engineered to directly drive the control coils of capacitor switching contactors or thyristor static switching modules.</li>
  <li><strong>Dynamic Reactive Power ($Q$-Based) Switching Logic:</strong> Rather than relying solely on phase angle ($\phi$), the controller measures true reactive kvar deficit and selects the optimal combination of capacitor step ratings (e.g. 1:1:1 or 1:2:4:8 binary codes) to reach the target power factor in the minimum number of switching operations.</li>
  <li><strong>Comprehensive Safety &amp; Harmonic Protection Suite:</strong> Automatically trips all capacitor steps upon detecting line over-voltage (> 115%), grid under-voltage blackout, excessive voltage total harmonic distortion (THD-V > 7%), or panel over-temperature, preventing capacitor dielectric breakdown.</li>
</ol>

<h2>Comparison: Microprocessor Dynamic APFC Controller vs. Fixed Capacitor Bank vs. Manual Rotary Switch Control</h2>
<table>
  <thead>
    <tr>
      <th>Operational Metric</th>
      <th>Fixed (Unswitched) Capacitor Bank</th>
      <th>Manual Multi-Step Rotary Switch</th>
      <th>YOMIN Intelligent APFC Controller (JKL5C Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Response to Load Fluctuations</strong></td>
      <td>Zero: Injects constant kvar regardless of whether factory motors are running or idling.</td>
      <td>Extremely slow: Relies on manual operator intervention to turn rotary knobs.</td>
      <td><strong>Instantaneous &amp; Dynamic: Microprocessor recalculates and switches steps within seconds.</strong></td>
    </tr>
    <tr>
      <td><strong>Risk of Leading PF Over-Compensation</strong></td>
      <td>Severe: During nights and weekends, fixed capacitors cause leading PF and dangerous over-voltage.</td>
      <td>High: Operators frequently forget to switch off banks after factory shifts end.</td>
      <td><strong>Zero Over-Compensation Risk: Automatically disconnects capacitor steps as load drops.</strong></td>
    </tr>
    <tr>
      <td><strong>Utility Power Factor Penalty Elimination</strong></td>
      <td>Unreliable: Fails during variable production shifts; penalties frequently recur.</td>
      <td>Poor: Constant human error leads to missed target power factor windows.</td>
      <td><strong>100% Penalty Elimination: Maintains target $\cos\phi \ge 0.98$ 24/7/365 automatically.</strong></td>
    </tr>
    <tr>
      <td><strong>Component Wear &amp; Life Expectancy</strong></td>
      <td>Capacitors degrade under continuous unswitched harmonic heating.</td>
      <td>Contactors burn out due to random uncoordinated switching.</td>
      <td><strong>Maximized Longevity: Equal-capacity circular switching (FIFO) doubles contactor &amp; capacitor life.</strong></td>
    </tr>
    <tr>
      <td><strong>SCADA Telemetry &amp; Remote Integration</strong></td>
      <td>None: No communication or telemetry capability.</td>
      <td>None: Purely mechanical manual switches.</td>
      <td><strong>Full Remote Telemetry: Isolated RS485 Modbus RTU interface connects to factory SCADA / EMS.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

APFC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='power-factor-correction-what-is-an-automatic-power-factor-controller-fr',
    title="Compensation d'Énergie Réactive : Qu'est-ce qu'un Régulateur Automatique de Facteur de Puissance (APFC Controller) ?",
    breadcrumb='Qualité de l\'Énergie &amp; Batteries de Condensateurs',
    read='10 min de lecture',
    alt='Régulateur numérique automatique de facteur de puissance (Série JKL5C) encastré sur la porte d\'une armoire de compensation affichant le cosinus phi et les LED d\'étages',
    desc=('Compensation automatique de l\'énergie réactive, gradins de condensateurs et suppression des pénalités de dépassement : Qu\'est-ce qu\'un régulateur APFC ? '
          'Calcul microprocesseur de la puissance réactive Q, permutation circulaire FIFO, protection anti-pompage, alarmes harmoniques THD et communication RS485 Modbus.'),
    model='Série JKL5C / RPCF : Régulateurs Automatiques de Facteur de Puissance pour Batteries de Condensateurs (6 à 16 Gradins, Calcul Dynamique Q, Modbus RS485, CEI 61000-4)',
    category='Qualité de l\'Énergie & Batteries de Condensateurs / Régulateurs Automatiques de Facteur de Puissance',
    kw='regulateur facteur de puissance &middot; apfc controller &middot; relais varmetrique &middot; compensation energie reactive &middot; jkl5c controller &middot; regulateur cos phi',
    specs=[
        ('Tension Assignée d\'Alimentation et Mesure', 'Entrée de mesure de tension : 220V / 380V / 400V / 415V AC (&plusmn;20%, 50/60 Hz, Phase-Neutre ou Phase-Phase)'),
        ('Calibre d\'Entrée du Courant de Mesure ($I_{in}$)', 'Entrée normalisée secondaire TC : 0–5A (transformateur de courant Classe 0.5 ou 0.2, consommation $< 0.5$ VA)'),
        ('Nombre de Gradins de Sortie Disponibles', 'Configurations de relais de commande d\'étages : 6, 8, 10, 12, 14 ou 16 sorties relais (assignées 250V AC / 5A)'),
        ('Plage de Réglage de la Consigne de $\cos\phi$', 'Facteur de puissance cible programmable : de 0,800 inductif à 0,800 capacitif (consigne usine : 0,950 à 0,980 lag)'),
        ('Algorithmes de Commande et Commutation', 'Mode de calcul dynamique de puissance réactive ($Q$ kvar), mode séquentiel linéaire et mode circulaire à usure égale'),
        ('Temporisation de Reconnexion des Gradins', 'Délai de sécurité programmable : 1 à 300 secondes (garantit la décharge complète des condensateurs par résistances de fuite)'),
        ('Protections Électriques et Harmoniques', 'Déclenchement sur surtension, verrouillage sous-tension, coupure surchauffe armoire et alarme de distorsion harmonique THD-V'),
        ('Port de Communication et Supervision', 'Port série isolé RS485 avec protocole standard Modbus RTU pour intégration directe dans la GTB / GTC ou logiciel SCADA')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Régulateur Automatique de Facteur de Puissance (Contrôleur APFC) et quel est son rôle ?',
         'Un Régulateur Automatique de Facteur de Puissance—couramment désigné sous le nom de relais varmétrique, contrôleur APFC ou régulateur de $\cos\phi$—est '
         'un appareil électronique numérique à microprocesseur qui constitue le "cerveau intelligent" des armoires de compensation automatique d\'énergie réactive. '
         'Dans les installations industrielles et tertiaires : '
         '<ul>'
         '<li><strong>Le Problème de l\'Énergie Réactive Inductive :</strong> Les moteurs asynchrones, transformateurs, compresseurs et fours industriels '
         'consomment de l\'énergie active (kW) pour produire le travail mécanique, mais également de l\'énergie réactive (kvar) pour magnétiser leurs circuits. '
         'Cette demande dégrade le facteur de puissance ($\cos\phi$) bien en-dessous de 0,90, surchargeant les transformateurs et déclenchant '
         'des pénalités financières massives sur les factures d\'électricité des distributeurs d\'énergie.</li>'
         '<li><strong>La Solution du Régulateur APFC :</strong> Le régulateur mesure en temps réel la tension et le courant via un TC, '
         'calcule le déficit exact en kvar capacitifs, et pilote automatiquement la mise sous tension séquentielle des contacteurs de condensateurs. '
         'Il ajuste en permanence la compensation pour maintenir le $\cos\phi$ proche de 1,0 (0,98), supprimant totalement les pénalités d\'énergie réactive.</li>'
         '</ul>'),
        ('Comment l\'algorithme de permutation circulaire protège-t-il les condensateurs contre l\'usure prématurée ?',
         'Sur les anciens régulateurs basiques, le premier gradin s\'enclenchait systématiquement en premier, s\'usant dix fois plus vite que les autres. '
         'Les régulateurs YOMIN JKL5C intègrent un mode de <strong>permutation circulaire (FIFO - Premier Entré, Premier Sorti)</strong> : '
         'Pour des gradins de puissance identique, l\'appareil fait tourner les cycles d\'enclenchement de manière rigoureusement équitable. '
         'Le gradin enclenché depuis le plus longtemps est le premier déconnecté, et celui au repos depuis le plus longtemps est le premier appelé, '
         'équilibrant parfaitement l\'échauffement thermique et doublant la durée de vie des contacteurs et condensateurs.'),
        ('Pourquoi la temporisation de décharge est-elle vitale avant de réenclencher un condensateur ?',
         'Lorsqu\'un condensateur de puissance est déconnecté du réseau, il conserve une charge résiduelle continue très élevée (jusqu\'à 560V en crête). '
         'Les résistances de décharge internes mettent entre 30 et 60 secondes pour évacuer cette énergie sous les 50V de sécurité. '
         'Si le régulateur réenclenchait ce condensateur immédiatement en opposition de phase avec la sinusoïde du réseau, le choc provoquerait '
         'un courant d\'appel destructeur supérieur à <strong>200 fois le courant nominal</strong>, soudant les pôles du contacteur et faisant exploser le condensateur. '
         'Le régulateur YOMIN applique une temporisation de sécurité obligatoire (60 secondes par défaut) interdisant tout réenclenchement prématuré.')
    ],
    cta='Vous concevez des armoires de compensation automatique d\'énergie réactive (batteries de condensateurs), des tableaux TGBT d\'efficacité énergétique ou recherchez des régulateurs de cos phi certifiés CEI 61000-4 (6 à 16 gradins, Modbus RS485) ? YOMIN fabrique des régulateurs varmétriques JKL5C/RPCF de haute précision.',
    body='''
<h2>Le Cerveau Intelligent des Systèmes de Compensation d\'Énergie Réactive</h2>
<p>Dans les usines de production industrielle, les centres commerciaux, les complexes de pompage et les data centers du monde entier, la facture énergétique constitue un poste de dépenses stratégique.</p>
<p>Les machines tournantes—moteurs électriques, groupes froids, ponts roulants et lignes de convoyage—font appel à des champs électromagnétiques pour fonctionner. Ces champs magnétiques absorbent une quantité considérable d\'énergie réactive ($Q$ kvar) qui ne produit aucun travail mécanique direct.</p>
<p>Lorsque cette énergie réactive transite sur le réseau, elle sature la capacité des transformateurs abaisseurs, augmente les pertes par effet Joule dans les câbles et déclenche des pénalités financières particulièrement lourdes de la part des gestionnaires de réseaux de distribution.</p>
<p>Le <strong>Régulateur Automatique de Facteur de Puissance (Série JKL5C / RPCF)</strong> apporte la solution technique standardisée : un contrôleur numérique qui analyse en temps réel les besoins réactifs de l\'installation et pilote automatiquement les étages de condensateurs pour maintenir un $\cos\phi \ge 0,98$ en permanence.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série JKL5C</h2>
<ol>
  <li><strong>Double Microprocesseur d\'Échantillonnage Rapide :</strong> Échantillonne les ondes de tension et de courant à haute fréquence, isolant l\'énergie active et réactive fondamentale même en présence d\'harmoniques industrielles sévères.</li>
  <li><strong>Afficheur Numérique Multifonction Haute Luminosité :</strong> Visualisation simultanée du facteur de puissance instantané, de la tension, du courant, de la puissance réactive requise (kvar) et de l\'état d\'enclenchement des gradins.</li>
  <li><strong>Gestion Intelligente par Permutation Circulaire FIFO :</strong> Répartit équitablement les manœuvres entre gradins de même calibre, prévenant le vieillissement asymétrique des condensateurs et contacteurs.</li>
  <li><strong>Sécurité Thermique et Harmonique Avancée :</strong> Déconnecte automatiquement les condensateurs en cas de surtension réseau (> 115%) ou de taux de distorsion harmonique excessif (THD-V > 7%) pour éviter tout phénomène de résonance destructive.</li>
  <li><strong>Interface de Communication Industrielle RS485 Modbus :</strong> Permet la télérelève des paramètres électriques et l\'intégration directe dans les systèmes de supervision GTB/GTC de l\'usine.</li>
</ol>
'''
)

APFC_ES = dict(
    lang='es',
    dir='ltr',
    slug='power-factor-correction-what-is-an-automatic-power-factor-controller-es',
    title='Corrección del Factor de Potencia: ¿Qué es un Controlador Automático de Factor de Potencia (APFC)?',
    breadcrumb='Calidad de Energía y Bancos de Capacitores',
    read='10 min de lectura',
    alt='Controlador digital automático de factor de potencia (Serie JKL5C) montado al frente de un tablero de banco de capacitores mostrando el cos phi y luces LED de pasos',
    desc=('Corrección automática del factor de potencia, maniobra de pasos de capacitores y eliminación de penalizaciones eléctricas: ¿Qué es un controlador APFC? '
          'Cálculo por microprocesador de potencia reactiva Q, rotación circular de pasos, prevención de oscilación (hunting), protección por armónicos THD y RS485 Modbus.'),
    model='Serie JKL5C / RPCF: Controladores Automáticos de Factor de Potencia para Bancos de Condensadores (6 a 16 Pasos, Cálculo Dinámico Q, Ciclado Circular, Modbus RS485, IEC 61000-4)',
    category='Calidad de Energía y Bancos de Capacitores / Controladores Automáticos de Factor de Potencia',
    kw='controlador factor de potencia &middot; apfc controller &middot; rele varmetrico &middot; correccion factor de potencia &middot; jkl5c controller &middot; banco de condensadores',
    specs=[
        ('Tensión Asignada de Alimentación y Medición', 'Tensión de entrada de muestreo: 220V / 380V / 400V / 415V AC (&plusmn;20%, 50/60 Hz, Fase-Neutro o Fase-Fase)'),
        ('Entrada Nominal de Corriente de Muestreo', 'Entrada estándar de secundario de TC: 0–5A (transformador de corriente Clase 0.5 o 0.2, carga interna $< 0.5$ VA)'),
        ('Cantidad de Pasos de Salida Disponibles', 'Configuraciones de relevadores de maniobra: 6, 8, 10, 12, 14 o 16 salidas de relé (capacidad 250V AC / 5A resistivo)'),
        ('Ajuste de Consigna de Factor de Potencia', 'Consigna programable de $\cos\phi$: 0.800 inductivo a 0.800 capacitivo (ajuste estándar de fábrica: 0.950 a 0.980 lag)'),
        ('Algoritmos de Conmutación Soportados', 'Modo de cálculo dinámico de potencia reactiva ($Q$ kvar), modo progresivo secuencial y modo de ciclado circular homogéneo'),
        ('Tiempo de Retardo de Descarga de Paso', 'Retardo de reconexión programable: 1 a 300 segundos (asegura la descarga segura del capacitor por resistencias internas)'),
        ('Protecciones Eléctricas y Armónicas', 'Disparo por sobretensión, bloqueo por subtensión, corte por sobretemperatura y alarma de distorsión armónica THD-V'),
        ('Puerto Digital de Comunicación y Monitoreo', 'Puerto serial aislado RS485 compatible con protocolo Modbus RTU estándar para integración a sistemas SCADA y EMS')
    ],
    faqs=[
        ('¿Qué es un Controlador Automático de Factor de Potencia (Controlador APFC) y cuál es su función?',
         'Un Controlador Automático de Factor de Potencia—conocido habitualmente como relé varmétrico, regulador de factor de potencia o controlador APFC—es '
         'un equipo electrónico digital basado en microprocesador que actúa como el "cerebro inteligente" de los tableros de bancos automáticos de capacitores. '
         'En plantas industriales y edificios comerciales: '
         '<ul>'
         '<li><strong>El Problema del Bajo Factor de Potencia:</strong> Motores de inducción, transformadores, compresores y hornos consumen energía activa (kW) '
         'para el trabajo útil y energía reactiva (kvar) para magnetizar sus bobinas. '
         'Esta demanda reduce el factor de potencia ($\cos\phi$) a niveles inferiores a 0.85 o 0.70, sobrecargando las líneas eléctricas, '
         'generando caídas de voltaje y provocando severas penalizaciones económicas en las facturas de la compañía eléctrica suministradora.</li>'
         '<li><strong>La Solución del Controlador APFC:</strong> El equipo mide continuamente la tensión y corriente mediante un TC, '
         'calcula en tiempo real el déficit exacto de reactivos en kvar y acciona automáticamente los relés de salida conectados a los contactores de capacitores. '
         'Inyecta la cantidad exacta de potencia capacitiva para neutralizar el retraso inductivo, manteniendo el $\cos\phi$ cerca de 1.0 (0.98) '
         'y eliminando por completo cualquier recargo tarifario por bajo factor de potencia.</li>'
         '</ul>'),
        ('¿Cómo protege el algoritmo de ciclado circular a los bancos de capacitores?',
         'En controladores antiguos, el paso 1 se conectaba siempre primero, sufriendo un desgaste diez veces superior a los últimos pasos. '
         'Los controladores YOMIN Serie JKL5C implementan un <strong>ciclado circular equitativo (FIFO - Primero en Entrar, Primero en Salir)</strong> : '
         'Para pasos de igual potencia, distribuye las conmutaciones de manera equilibrada. El paso que ha estado conectado por más tiempo es el primero en desconectarse, '
         'y el que ha descansado por más tiempo es el primero en conectarse, igualando el esfuerzo térmico y duplicando la vida útil de capacitores y contactores.'),
        ('¿Por qué es indispensable un tiempo de retardo para la descarga del capacitor?',
         'Al desconectarse un capacitor de la red eléctrica, retiene una elevada carga residual de corriente continua (hasta el valor pico de la onda AC). '
         'Las resistencias internas de descarga requieren entre 30 y 60 segundos para drenar ese voltaje por debajo de 50V. '
         'Si el controlador intentara reconectar ese capacitor de inmediato en oposición de fase con la onda de la red, se produciría una corriente de choque '
         'superior a <strong>200 veces la corriente nominal</strong>, destruyendo el contactor y perforando el dieléctrico del capacitor. '
         'El controlador YOMIN aplica un retardo de bloqueo obligatorio (60 segundos por defecto) que impide reconexiones peligrosas.')
    ],
    cta='¿Fabrica tableros de corrección de factor de potencia (bancos automáticos de capacitores), cuadros TGBT de eficiencia energética o requiere controladores de factor de potencia certificados bajo norma IEC 61000-4 (6 a 16 pasos, Modbus RS485)? YOMIN suministra controladores varmétricos serie JKL5C/RPCF de máxima confiabilidad.',
    body='''
<h2>El Cerebro Maestro Inteligente de los Bancos de Capacitores Industriales</h2>
<p>En plantas de manufactura industrial, centros comerciales, estaciones de bombeo y centros de procesamiento de datos en todo el mundo, la eficiencia eléctrica impacta directamente en los costos operativos de la empresa.</p>
<p>La maquinaria electromecánica—como motores de jaula de ardilla, compresores de refrigeración, extrusoras y prensas hidráulicas—utiliza campos electromagnéticos para operar. Estos campos consumen una gran cantidad de potencia reactiva inductiva ($Q$ kvar) que no realiza trabajo mecánico directo pero satura las redes eléctricas.</p>
<p>Cuando la potencia reactiva circula sin compensación por los transformadores y cables de la planta, incrementa las pérdidas por calor $I^2R$, degrada el voltaje y provoca cuantiosas multas y recargos por bajo factor de potencia por parte de la empresa suministradora de energía.</p>
<p>El <strong>Controlador Automático de Factor de Potencia (Serie JKL5C / RPCF)</strong> representa el estándar tecnológico definitivo: un instrumento digital que calcula con precisión los requerimientos reactivos de la instalación y conmuta dinámicamente los pasos de capacitores para mantener el $\cos\phi \ge 0.98$ de manera automática las 24 horas del día.</p>

<h2>Componentes y Calidad de Ingeniería de la Serie JKL5C</h2>
<ol>
  <li><strong>Microprocesador Dual de Muestreo de Alta Velocidad:</strong> Analiza las ondas senoidales de voltaje y corriente en tiempo real mediante transformada rápida de Fourier (FFT), calculando la potencia activa y reactiva exacta incluso ante presencia de armónicos en la red.</li>
  <li><strong>Pantalla Digital Multifunción de Gran Visibilidad:</strong> Muestra simultáneamente el factor de potencia, voltaje, corriente, potencia reactiva requerida en kvar y el estado encendido/apagado de cada uno de los pasos de capacitores.</li>
  <li><strong>Algoritmo de Rotación Homogénea de Pasos FIFO:</strong> Alterna de forma circular los bancos de capacitores de igual potencia, garantizando un desgaste térmico y mecánico uniforme en todos los contactores.</li>
  <li><strong>Protección Integral por Sobretensión y Distorsión Armónica:</strong> Desconecta automáticamente los capacitores si la tensión supera el 115% o si la distorsión armónica total de voltaje (THD-V) rebasa el 7%, protegiendo los bancos contra resonancias destructivas.</li>
  <li><strong>Puerto de Comunicación Serial RS485 Modbus RTU:</strong> Facilita la supervisión remota de parámetros eléctricos y su integración con los sistemas SCADA y de gestión energética de la planta.</li>
</ol>
'''
)

APFC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='power-factor-correction-what-is-an-automatic-power-factor-controller-ar',
    title='تحسين معامل القدرة والتعويض الديناميكي: ما هو جهاز التحكم الآلي في معامل القدرة (APFC Controller)؟',
    breadcrumb='جودة الطاقة ومكثفات تحسين معامل القدرة',
    read='10 دقائق قراءة',
    alt='جهاز تحكم آلي رقمي في معامل القدرة (موديل JKL5C) مركب على باب لوحة مكثفات صناعية يعرض قيمة معامل القدرة ومؤشرات المراحل LED',
    desc=('تحسين معامل القدرة الصناعي، والتحكم في مراحل بنوك المكثفات، وإلغاء غرامات شركات الكهرباء: ما هو جهاز التحكم في معامل القدرة (APFC Controller)؟ '
          'حسابات القدرة غير الفعالة Q بالمعالج الرقمي، والتبديل الدائري FIFO، ومنع التأرجح، والحماية من التوافقيات THD واتصال RS485 Modbus.'),
    model='سلسلة JKL5C / RPCF: أجهزة التحكم الرقمية التلقائية في معامل القدرة لبنوك المكثفات (6 إلى 16 مرحلة تتابع، حساب ديناميكي لـ Q، بروتوكول Modbus RS485، معتمد IEC 61000-4)',
    category='جودة الطاقة ومكثفات تحسين معامل القدرة / أجهزة التحكم الآلي في معامل القدرة',
    kw='جهاز تحكم معامل القدرة &middot; apfc controller &middot; منظم معامل القدرة &middot; لوحة مكثفات &middot; jkl5c controller &middot; تحسين معامل القدرة',
    specs=[
        ('فئة جهد التشغيل والقياس الاسمي للشبكة', 'جهد إشارة أخذ العينات: 220V / 380V / 400V / 415V AC (&plusmn;20%، تردد 50/60 هرتز، طور-تعادل أو طور-طور)'),
        ('تيار إشارة العينات من محول التيار ($I_{in}$)', 'دخل تيار معياري من ثانوي محول التيار CT: من 0 إلى 5 أمبير (فئة دقة 0.5 أو 0.2، حمل داخلي $< 0.5$ VA)'),
        ('عدد مراحل التتابع والتحكم المتاحة', 'مخرجات تتابع للتحكم في كونتاكتورات المكثفات: 6 أو 8 أو 10 أو 12 أو 14 أو 16 مخرج ريليه (تصنيف 250V AC / 5A)'),
        ('نطاق ضبط القيمة المستهدفة لمعامل القدرة', 'معامل قدرة مستهدف قابل للبرمجة: من 0.800 حثي إلى 0.800 سعوي (القيمة الافتراضية بالمصنع: 0.950 إلى 0.980 متأخر)'),
        ('خوارزميات التبديل والتحكم المعتمدة', 'نمط الحساب الديناميكي للقدرة غير الفعالة ($Q$ kvar)، والنمط التتابعي، ونمط التدوير الدائري المتساوي FIFO'),
        ('زمن تأخير إعادة توصيل مرحلة المكثف', 'زمن أمان لتفريغ الشحنة قابل للبرمجة: 1 إلى 300 ثانية (لضمان تفريغ شحنة المكثف عبر مقاومات التفريغ الداخلية)'),
        ('منظومة الحماية الكهربائية والتوافقية', 'فصل أوتوماتيكي عند ارتفاع الجهد، وحظر عند هبوط الجهد، وفصل عند زيادة حرارة اللوحة، وإنذار تشوه التوافقيات THD-V'),
        ('منفذ الاتصال والمراقبة الرقمية عن بُعد', 'منفذ تسلسلي معزول RS485 يدعم بروتوكول Modbus RTU القياسي للربط مع أنظمة إدارة الطاقة والمراقبة SCADA')
    ],
    faqs=[
        ('ما هو جهاز التحكم الآلي في معامل القدرة (APFC Controller) وما هي وظيفته الأساسية؟',
         'جهاز التحكم الآلي في معامل القدرة—والمعروف في قطاع الكهرباء الصناعي باسم منظم معامل القدرة أو ريليه الفار (Var Relay) أو عقل لوحة المكثفات—هو '
         'جهاز إلكتروني رقمي متطور يعتمد على معالج دقيق، ويمثل "العقل الذكي والمتحكم الرئيسي" في لوحات بنوك مكثفات تحسين معامل القدرة (APFC Panels). '
         'وفي المنشآت الصناعية والتجارية: '
         '<ul>'
         '<li><strong>أزمة انخفاض معامل القدرة:</strong> تسحب الأحمال الحثية مثل المحركات الكهربائية، والمضخات، والضواغط، والمحولات '
         'قدرة فعالة (kW) لإنجاز العمل الميكانيكي وقدرة غير فعالة (kvar) لبناء المجالات المغناطيسية. '
         'هذا الطلب يؤدي إلى تدهور معامل القدرة ($\cos\phi$) لأقل من 0.80 أو 0.70، مما يسبب تحميل الكابلات والمحولات بتيارات زائدة '
         'ويفرض غرامات مالية باهظة شهرياً من شركات الكهرباء على المنشأة.</li>'
         '<li><strong>الحل الجذري بجهاز APFC:</strong> يقوم الجهاز بقياس الجهد والتيار لحظياً عبر محول تيار، ويحسب العجز الدقيق بالكيلوفار (kvar)، '
         'ثم يعطي أوامر كهربية للمرحلات لتشغيل كونتاكتورات المكثفات خطوة بخطوة لإدخال السعة المطلوبة تماماً، محافظاً على معامل القدرة عند 0.98 '
         'ويلغي غرامات فاتورة الكهرباء نهائياً.</li>'
         '</ul>'),
        ('كيف تحمي خوارزمية التدوير الدائري (FIFO) بنك المكثفات من التلف المبكر؟',
         'في الأجهزة القديمة، كانت المرحلة الأولى من المكثفات تعمل دائماً أولاً، مما يجعلها تهلك أسرع بعشر مرات من باقي المراحل. '
         'تحتوي أجهزة يمين JKL5C على نظام <strong>التدوير الدائري المتساوي (FIFO - الداخل أولاً يخرج أولاً)</strong> : '
         'يقوم الجهاز بتوزيع ساعات التشغيل بعدالة تامة على المراحل المتساوية في السعة؛ فالمكثف الذي ظل يعمل لأطول فترة يتم فصله أولاً، '
         'والمكثف الذي ظل في وضع الراحة لأطول فترة يتم تشغيله أولاً، مما يضاعف العمر الافتراضي للمكثفات والكونتاكتورات.'),
        ('لماذا يعتبر زمن تأخير إعادة التوصيل حيوياً للغاية لسلامة المكثفات؟',
         'عند فصل مكثف القدرة عن الشبكة، يظل محتفظاً بشحنة تيار مستمر داخلية هائلة تعادل القيمة اللحظية لقمة موجة الجهد. '
         'وتحتاج مقاومات التفريغ الداخلية المدمجة بالمكثف من 30 إلى 60 ثانية لتفريغ هذا الجهد لأقل من 50 فولت الآمنة. '
         'فإذا حاول جهاز التحكم إعادة توصيل المكثف فورياً وهو لا يزال مشحوناً في عكس طور موجة الشبكة، فإن هذا التضاد يتسبب في اندفاع تيار صدمي هائل '
         'يتجاوز <strong>200 ضعف التيار الاسمي</strong>، مما يلحم نقاط تلامس الكونتاكتور ويفجر المكثف فوراً. '
         'يطبق جهاز يمين فترة حظر زمنية إلزامية (60 ثانية افتراضياً) تمنع أي إعادة توصيل قبل اكتمال التفريغ.')
    ],
    cta='هل تعمل على تصنيع لوحات بنوك مكثفات تحسين معامل القدرة (APFC Panels)، أو مشاريع كفاءة الطاقة للمصانع الكبرى، أو تحتاج لأجهزة تحكم رقمية معتمدة IEC 61000-4 (من 6 إلى 16 مرحلة، مع Modbus RS485)؟ تصنع يمين (YOMIN) أجهزة تحكم JKL5C/RPCF بأعلى معايير الدقة.',
    body='''
<h2>العقل الرقمي الذكي لمنظومات تحسين معامل القدرة الكهربائية الصناعية</h2>
<p>في المصانع وورش الإنتاج، والمجمعات التجارية الضخمة، ومحطات معالجة المياه، ومراكز البيانات حول العالم، تمثل كفاءة استهلاك الطاقة عنصراً حاسماً في خفض تكاليف التشغيل وزيادة الأرباح.</p>
<p>تعتمد كافة الماكينات الكهروميكانيكية—مثل المحركات الحثية، ومجموعات التبريد والتكييف، ومضخات السوائل، والضواغط الهوائية—على المجالات الكهرومغناطيسية لكي تعمل. وتسحب هذه المجالات قدراً كبيراً من القدرة غير الفعالة ($Q$ kvar) من شبكة التوزيع دون أن تبذل أي شغل ميكانيكي حقيقي.</p>
<p>ومع مرور هذه القدرة غير الفعالة عبر المحولات والكابلات، فإنها تتسبب في ارتفاع حرارة الموصلات وفقداً بالجهد، مما يدفع شركات الكهرباء لفرض غرامات مالية قاسية جداً على فواتير الطاقة للمنشآت ذات معامل القدرة المنخفض.</p>
<p>يمثل <strong>جهاز التحكم الآلي في معامل القدرة (سلسلة JKL5C / RPCF)</strong> الحل القياسي المتكامل: جهاز رقمي ميكروبروسيسور يحلل طلب القدرة غير الفعالة على مدار الساعة ويقوم بإدخال وإخراج مراحل بنوك المكثفات بدقة متناهية ليحافظ على معامل القدرة ($\cos\phi \ge 0.98$) بصورة أوتوماتيكية بالكامل.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة أجهزة JKL5C</h2>
<ol>
  <li><strong>معالج رقمي مزدوج فائق السرعة:</strong> يحلل عينات موجات الجهد والتيار اللحظية باستخدام تحويل فوريه السريع (FFT)، مستخرجاً القدرة الفعالة وغير الفعالة بدقة تامة حتى مع وجود تشوهات توافقية في شبكة المصنع.</li>
  <li><strong>شاشة عرض رقمية عالية الإضاءة والوضوح:</strong> تعرض في آن واحد معامل القدرة، والجهد، والتيار، وحجم الكيلوفار المطلوب، وحالة تشغيل كل مرحلة من مراحل المكثفات عبر لمبات LED واضحة.</li>
  <li><strong>خوارزمية التدوير الدائري الذكي لحماية المكثفات:</strong> توازن فترات التشغيل بين المراحل المتساوية في السعة بنظام FIFO، مانعةً الإجهاد الحراري غير المتوازن على المكثفات.</li>
  <li><strong>منظومة حماية متكاملة من التوافقيات والجهود الزائدة:</strong> تفصل مراحل المكثفات فورياً عند ارتفاع جهد الشبكة لأكثر من 115% أو عند تجاوز نسبة التوافقيات للحدود الآمنة لحماية البنك من ظاهرة الرنين المدمر.</li>
  <li><strong>منفذ اتصال تسلسلي صناعي معزول RS485 Modbus:</strong> يتيح القراءة والمراقبة اللحظية لمعامل القدرة وإدماج اللوحة مباشرة في برامج المراقبة والتحكم بالمنشأة SCADA.</li>
</ol>
'''
)

# ==============================================================================
# 2. STATION POST INSULATOR (EN, FR, ES, AR)
# ==============================================================================

SPI_EN = dict(
    lang='en',
    dir='ltr',
    slug='substation-busbar-supports-what-is-a-station-post-insulator',
    title='Substation Busbar Supports: What Is a Station Post Insulator?',
    breadcrumb='Substation Hardware &amp; Insulators',
    read='10 min read',
    alt='Three vertical high-voltage Composite Station Post Insulators (Model FZSW series, 110kV rating) supporting horizontal tubular aluminum busbars in an outdoor electrical substation',
    desc=('High-voltage electrical substations (11kV to 110kV), outdoor switchyards, and busbar support structures: What is a station post insulator? '
          'How solid ECR fiberglass core rods, hydrophobic HTV silicone sheds, massive cantilever/compressive strength, seismic resilience, and IEC 62231 / ANSI C29.9 standards support substation busbars.'),
    model='Model FZSW Series 11kV–110kV High-Voltage Composite Station Post Insulators (Solid Core Rod, 4kN to 16kN Cantilever SCL, 80kN to 250kN Compression, IEC 62231 / ANSI C29.9)',
    category='Substation Hardware & Insulators / Composite Station Post Insulators',
    kw='what is a station post insulator &middot; station post insulator &middot; substation post insulator &middot; composite station post insulator &middot; station post insulator 33kv 110kv &middot; fzsw insulator',
    specs=[
        ('Rated System Operating Voltage Class', 'Engineered for high-voltage outdoor substations & switchyards: 11kV, 24kV, 33kV, 66kV, and 110kV AC (50/60 Hz)'),
        ('Specified Cantilever Failing Load (SCL)', 'Heavy mechanical cantilever bending strength: 4 kN, 8 kN, 10 kN, 12.5 kN, and 16 kN (compliant with IEC 62231)'),
        ('Rated Compressive Load Strength (Compression)', 'Extreme axial compressive strength: 80 kN, 120 kN, 160 kN, up to 250 kN (supports heavy busbars and disconnect switches)'),
        ('Rated Torsional Failing Moment (Torsion)', 'High torsional resistance: 1.0 kN&middot;m, 2.0 kN&middot;m, up to 3.5 kN&middot;m (for motorized rotary disconnector switch blades)'),
        ('Core Rod Construction & Fiberglass Type', 'Large-diameter solid electrical-grade boron-free ECR fiberglass epoxy core rod (zero internal voids; acid-resistant)'),
        ('Shed Material & Weatherproof Housing', 'Seamless high-temperature vulcanized (HTV) liquid silicone rubber housing (permanent hydrophobicity class HC1/HC2)'),
        ('Top & Bottom Metal Flange Specifications', 'Hot-dip galvanized ductile iron (ASTM A153) with standard 4-hole or 8-hole Pitch Circle Diameter (PCD) bolt patterns'),
        ('Pollution Creepage Distance & BIL Rating', 'Specific creepage distance &ge; 31 mm/kV for heavy industrial/desert pollution; Lightning impulse (BIL) up to 550 kV')
    ],
    faqs=[
        ('What is a Station Post Insulator and where is it installed inside electrical substations?',
         'A Station Post Insulator—frequently designated as a substation post insulator, busbar support insulator, or high-voltage apparatus standoff—is '
         'a heavy-duty rigid vertical or horizontal insulating pillar designed to provide electrical isolation and rigid mechanical physical support '
         'for high-voltage electrical conductors and apparatus inside outdoor air-insulated substations (AIS), industrial switchyards, and power generating plants. '
         'In high-voltage transmission substations (11kV to 110kV/220kV): '
         '<ul>'
         '<li><strong>1. Substation Busbar Support:</strong> Installed atop structural steel lattice pedestals to support long spans of rigid tubular aluminum busbars '
         'or stranded flexible conductors connecting transformers to circuit breakers.</li>'
         '<li><strong>2. Disconnector &amp; Isolator Switch Pedestals:</strong> Serves as the fixed contact support and rotating insulating drive shaft '
         'for outdoor high-voltage disconnect switches and earthing switches, transferring rotating mechanical torque while isolated at 110kV.</li>'
         '<li><strong>3. Surge Arrester &amp; Wave Trap Standoffs:</strong> Electrically isolates and physically mounts line traps, capacitor bank racks, '
         'reactor coils, and cable termination structures against ground potential.</li>'
         '</ul>'),
        ('How does a Station Post Insulator differ from an overhead Line Post Insulator?',
         'While both insulators feature rigid post designs, their mechanical application profiles and end fittings are fundamentally different: '
         '<ul>'
         '<li><strong>Station Post Insulator (Substation Busbar &amp; Apparatus):</strong> Engineered with <strong>flanged metal fittings at BOTH ends</strong> '
         '(multi-hole PCD bolt patterns top and bottom). It is subjected to complex multi-axial mechanical forces: heavy <strong>downward axial compression (up to 250kN)</strong> '
         'from tubular busbar weight, lateral cantilever bending during short-circuit electromagnetic repulsion, and <strong>torsional twisting (up to 3.5 kN&middot;m)</strong> '
         'from rotating disconnect switch blades. Tested under substation standard <strong>IEC 62231 / ANSI C29.9</strong>.</li>'
         '<li><strong>Line Post Insulator (Overhead Transmission &amp; Distribution):</strong> Engineered with a curved pole base flange at the bottom '
         'and a conductor clamp or tie-top neck at the top. It is subjected primarily to pure transverse cantilever bending from wind and conductor tension, '
         'installed on transmission poles along transmission lines. Tested under <strong>IEC 61952 / ANSI C29.18</strong>.</li>'
         '</ul>'),
        ('Why are composite silicone station post insulators replacing porcelain posts in seismic and desert substations?',
         'Traditional porcelain station post insulators suffer from catastrophic weaknesses in demanding substation environments: '
         '<ul>'
         '<li><strong>1. Seismic Fracture Immunity:</strong> Porcelain is brittle; during earthquakes, high ground accelerations shatter rigid porcelain posts, '
         'collapsing high-voltage busbars. YOMIN composite station posts utilize an elastic ECR fiberglass core that flexes harmlessly under severe seismic shocks (exceeding 0.5g acceleration).</li>'
         '<li><strong>2. Zero Washing in Desert &amp; Coastal Environments:</strong> Porcelain requires frequent high-pressure water washing to prevent salt and sand pollution flashovers. '
         'HTV silicone rubber possesses permanent hydrophobicity and hydrophobicity transfer (HTM), causing water to bead into isolated non-conductive droplets even when coated in desert dust.</li>'
         '<li><strong>3. Vandalism &amp; Explosion Safety:</strong> If an internal power flashover occurs, porcelain explodes into razor-sharp projectiles that damage surrounding switchgear. '
         'Composite insulators do not shatter, protecting nearby personnel and multi-million-dollar power transformers.</li>'
         '</ul>')
    ],
    cta='Designing high-voltage outdoor substations, switchyard busbar expansions, disconnect switch pedestals, or seismic-rated capacitor bank racks requiring certified IEC 62231 / ANSI C29.9 composite station post insulators (11kV to 110kV, 4kN to 16kN cantilever, up to 250kN compression)? YOMIN manufactures precision FZSW series post insulators.',
    body='''
<h2>The Unyielding Structural Support for High-Voltage Substation Busbars and Switchgear</h2>
<p>Inside every high-voltage electrical transmission substation, step-down distribution switchyard, and renewable utility-scale substation operating at <strong>11kV, 33kV, 66kV, and 110kV</strong>, high-voltage busbars form the central arteries of electrical power flow.</p>
<p>These massive tubular aluminum busbars carry continuous currents reaching thousands of amperes between power transformers, circuit breakers, and outgoing transmission lines. Under normal operating conditions, these busbars require rigid, immovable physical support several meters above ground to maintain electrical safety clearances.</p>
<p>However, during catastrophic substation short-circuit faults (reaching 40,000 amperes), violent electromagnetic repulsion forces erupt between adjacent phase busbars. These lateral electromagnetic shockwaves exert instantaneous cantilever bending moments reaching tens of thousands of newton-meters on the underlying insulator supports.</p>
<p>The <strong>Composite High-Voltage Station Post Insulator (Model FZSW Series)</strong> provides the unshakeable foundation: a heavy-duty, high-strength composite insulating column engineered to withstand tremendous cantilever bending, compressive column loads, and torsional forces under full substation short-circuit and seismic conditions.</p>

<h2>Engineering Anatomy: Inside a Model FZSW Composite Station Post Insulator</h2>
<ol>
  <li><strong>Heavy-Diameter Solid ECR Fiberglass Core:</strong> Pultruded from electrical-grade, boron-free glass fibers impregnated with high-temperature epoxy resin. Designed with an extra-large solid cross-section to deliver extreme cantilever bending moments and axial compressive buckling resistance up to 250 kN.</li>
  <li><strong>High-Temperature Vulcanized (HTV) Silicone Rubber Housing:</strong> High-pressure injection molded over the core rod in a single seamless operation. Its unique chemical formulation provides permanent surface hydrophobicity that prevents leakage currents and eliminates flashovers in heavy industrial and coastal desert zones.</li>
  <li><strong>Dual Precision Ductile Iron Mounting Flanges:</strong> Both top and bottom ends feature hot-dip galvanized ductile iron flanges with standardized 4-hole or 8-hole bolt patterns (PCD 76mm, 127mm, or 225mm) that bolt directly to steel support structures and busbar clamps.</li>
  <li><strong>Acoustic Emission Monitored Swaged Crimping:</strong> Flanges are attached to the solid core rod using computerized multi-jaw radial crimping with real-time acoustic emission feedback, guaranteeing maximum mechanical grip without micro-fracturing the internal fiberglass matrix.</li>
  <li><strong>Torsional Spline Keying Design:</strong> Internal mechanical locking geometry between the metal flange and fiberglass rod provides certified torsional failure limits exceeding 3.5 kN&middot;m, essential for operating motorized outdoor disconnect switches.</li>
</ol>

<h2>Comparison: Composite Silicone Station Post Insulator vs. Traditional Porcelain Station Post Insulator</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Traditional Porcelain Station Post Insulator</th>
      <th>YOMIN Composite Station Post Insulator (FZSW Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Seismic Shock &amp; Earthquake Performance</strong></td>
      <td>Brittle and vulnerable: High ground acceleration shears porcelain columns catastrophically.</td>
      <td><strong>High Elastic Resilience: Fiberglass core rod flexes elastically and absorbs ground shock waves without fracture.</strong></td>
    </tr>
    <tr>
      <td><strong>Maintenance &amp; Washing in Polluted Environments</strong></td>
      <td>Requires periodic de-energization and high-pressure water washing to prevent salt flashovers.</td>
      <td><strong>Zero Washing Required: Hydrophobic HTV silicone naturally prevents conductive moisture film formation.</strong></td>
    </tr>
    <tr>
      <td><strong>Total Unit Weight &amp; Installation Handling</strong></td>
      <td>Extremely heavy (40 to 90 kg per post); requires mobile crane trucks to hoist aloft onto steel stands.</td>
      <td><strong>Ultra-Lightweight (70% weight reduction): Easy manual rigging and rapid bolt-up by substation crews.</strong></td>
    </tr>
    <tr>
      <td><strong>Explosive Shattering &amp; Projectile Hazard</strong></td>
      <td>Explosive fragmentation during power arc flashovers, spraying razor-sharp porcelain shards across switchyard.</td>
      <td><strong>Non-Shattering Safety: Tough silicone and composite core do not explode, protecting adjacent equipment.</strong></td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Cantilever Bending Strength</strong></td>
      <td>Prone to micro-cracking and sudden catastrophic shear under high fault repulsion forces.</td>
      <td><strong>Superior Cantilever SCL: Certified from 4 kN up to 16 kN, handling 40kA short-circuit forces with ease.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

SPI_FR = dict(
    lang='fr',
    dir='ltr',
    slug='substation-busbar-supports-what-is-a-station-post-insulator-fr',
    title="Postes Électriques & Jeux de Barres : Qu'est-ce qu'un Isolateur Support de Poste (Station Post Insulator) ?",
    breadcrumb='Appareillage de Poste &amp; Isolateurs Haute Tension',
    read='10 min de lecture',
    alt='Trois isolateurs composites rigides supports de poste (Série FZSW, 110kV) supportant des jeux de barres tubulaires en aluminium dans un poste électrique extérieur',
    desc=('Postes de transformation haute tension (11kV à 110kV), jeux de barres rigides et supports d\'appareillage : Qu\'est-ce qu\'un isolateur support de poste (station post insulator) ? '
          'Jonc plein en fibre de verre ECR, ailettes silicone HTV hydrophobe, résistance extrême à la flexion (4kN–16kN) et à la compression (80kN–250kN), et normes CEI 62231 / ANSI C29.9.'),
    model='Série FZSW : Isolateurs Composites Rigides Supports de Poste pour Jeux de Barres HT (11kV à 110kV, Flexion 4kN à 16kN, Compression 80kN à 250kN, CEI 62231 / ANSI C29.9)',
    category='Appareillage de Poste & Isolateurs Haute Tension / Isolateurs Supports de Poste',
    kw='isolateur support de poste &middot; station post insulator &middot; isolateur de sous-station &middot; support jeu de barres ht &middot; isolateur fzsw &middot; isolateur composite 110kv',
    specs=[
        ('Tension Assignée de Service du Réseau', 'Conçu pour les postes électriques haute tension extérieurs : 11kV, 24kV, 33kV, 66kV et 110kV AC (50/60 Hz)'),
        ('Charge Mécanique Spécifiée de Flexion (SCL)', 'Charges nominales de rupture à la flexion en porte-à-faux : 4 kN, 8 kN, 10 kN, 12,5 kN et 16 kN (norme CEI 62231)'),
        ('Résistance Nominale à la Compression Axiale', 'Capacité de compression extrême : 80 kN, 120 kN, 160 kN jusqu\'à 250 kN (supporte les jeux de barres lourds et sectionneurs)'),
        ('Couple de Rupture à la Torsion Assigné', 'Résistance élevée à la torsion : 1,0 kN&middot;m, 2,0 kN&middot;m jusqu\'à 3,5 kN&middot;m (pour commandes rotatives de sectionneurs)'),
        ('Jonc Central Porteur et Matériau Synthétique', 'Jonc plein de très fort diamètre en résine époxyde armée de fibres de verre ECR sans bore (zéro porosité interne)'),
        ('Enveloppe Protectrice et Ailettes Isolantes', 'Moulage sans joint en élastomère de silicone HTV vulcanisé à chaud à hydrophobicité permanente (Classe HC1/HC2)'),
        ('Brides Métalliques Supérieure et Inférieure', 'Brides d\'extrémité en fonte ductile galvanisée à chaud (ASTM A153) avec perçages normalisés à 4 ou 8 trous (PCD)'),
        ('Ligne de Fuite Spécifique et Tenue au Choc', 'Ligne de fuite spécifique pour pollution sévère &ge; 31 mm/kV ; niveau d\'isolement aux chocs de foudre (BIL) jusqu\'à 550 kV')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Isolateur Support de Poste (Station Post Insulator) et quel est son rôle dans un poste HT ?',
         'Un Isolateur Support de Poste—couramment appelé colonne isolante de poste, isolateur piédestal ou support de jeu de barres—est '
         'une colonne rigide isolante haute tension conçue pour assurer l\'isolation électrique et le support mécanique inébranlable '
         'des barres omnibus et des appareils haute tension dans les postes de transformation extérieurs (AIS). '
         'Dans les postes de 11kV à 110kV : '
         '<ul>'
         '<li><strong>1. Support des Jeux de Barres :</strong> Fixé sur des charpentes métalliques pour soutenir les tubes d\'aluminium rigides '
         'assurant la liaison électrique entre transformateurs et disjoncteurs.</li>'
         '<li><strong>2. Colonne de Sectionneur :</strong> Sert de support fixe ou d\'arbre de transmission rotatif isolant pour les lames '
         'de sectionneurs haute tension, transmettant des couples de rotation tout en étant sous tension.</li>'
         '<li><strong>3. Support d\'Appareils :</strong> Isole et maintient rigidement les bobines de selfs, les parafoudres et les batteries de condensateurs.</li>'
         '</ul>'),
        ('Quelle est la différence entre un isolateur Station Post de poste et un Line Post de ligne aérienne ?',
         'Leurs configurations d\'extrémité et leurs régimes mécaniques sont distincts : '
         '<ul>'
         '<li><strong>Isolateur Support de Poste (Station Post) :</strong> Équipé de <strong>brides plates métalliques aux deux extrémités</strong> '
         '(perçages normalisés PCD en haut et en bas). Il subit des efforts combinés : forte <strong>compression axiale (jusqu\'à 250kN)</strong> '
         'due au poids des barres, flexion lors des courts-circuits et <strong>torsion (jusqu\'à 3,5 kN&middot;m)</strong> lors de la manœuvre des sectionneurs. '
         'Normé selon la <strong>CEI 62231 et ANSI C29.9</strong>.</li>'
         '<li><strong>Isolateur Line Post de Ligne :</strong> Fixé sur poteau avec une embase incurvée et une pince supérieure de câble. '
         'Il travaille principalement en flexion transversale sous le vent et la tension des câbles aériens (CEI 61952).</li>'
         '</ul>'),
        ('Pourquoi les isolateurs composites remplacent-ils la porcelaine dans les postes sismiques et pollués ?',
         'La porcelaine traditionnelle casse net lors des tremblements de terre et exige des nettoyages fréquents. '
         'Les isolateurs composites YOMIN FZSW apportent des atouts majeurs : '
         '<ul>'
         '<li><strong>Résistance Sismique Absolue :</strong> Le jonc en fibre de verre ECR absorbe élastiquement les secousses telluriques sans rupture.</li>'
         '<li><strong>Zéro Lavage en Zone Polluée :</strong> La silicone HTV repousse l\'eau et empêche les amorçages sous brouillard salin ou poussière.</li>'
         '<li><strong>Sécurité des Personnels :</strong> En cas de court-circuit extrême, l\'isolateur composite n\'éclate pas en éclats tranchants.</li>'
         '</ul>')
    ],
    cta='Vous concevez des postes électriques haute tension, des extensions de jeux de barres en sous-station ou des colonnes de sectionneurs nécessitant des isolateurs composites supports de poste certifiés CEI 62231 / ANSI C29.9 (11kV à 110kV, compression jusqu\'à 250kN) ? YOMIN fabrique des isolateurs FZSW de haute précision.',
    body='''
<h2>Le Supportage Mécanique Inébranlable des Jeux de Barres en Postes Haute Tension</h2>
<p>Au cœur de chaque poste de transformation et de répartition d\'énergie haute tension fonctionnant sous des tensions de <strong>11kV, 33kV, 66kV et 110kV</strong>, les jeux de barres constituent les artères principales de transit de la puissance.</p>
<p>Ces imposants tubes d\'aluminium transportent en permanence des milliers d\'ampères entre les transformateurs de puissance, les disjoncteurs et les départs de lignes. En service normal, ils doivent être fermement maintenus à plusieurs mètres au-dessus du sol pour garantir les distances de sécurité électrique.</p>
<p>Cependant, lors d\'un court-circuit franc en sous-station (atteignant 40 000 ampères), des forces électromagnétiques de répulsion colossales s\'exercent instantanément entre les barres de phases voisines. Ces ondes de choc mécaniques soumettent les isolateurs supports à des moments de flexion violents.</p>
<p>L\'<strong>Isolateur Composite Rigide Support de Poste (Série FZSW)</strong> constitue la solution de référence : une colonne synthétique ultra-résistante conçue pour encaisser des efforts considérables de flexion, de compression axiale et de torsion sans aucune défaillance.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série FZSW</h2>
<ol>
  <li><strong>Jonc Massif en Fibre de Verre ECR :</strong> Diamètre renforcé garantissant une résistance à la compression axiale jusqu\'à 250 kN et une tenue en flexion jusqu\'à 16 kN sans fatigue structurelle.</li>
  <li><strong>Enveloppe en Élastomère de Silicone HTV :</strong> Hydrophobicité permanente qui empêche tout contournement diélectrique sous pluie battante ou pollution marine sans nécessité de lavage.</li>
  <li><strong>Brides Conformes aux Standards PCD :</strong> Brides supérieure et inférieure en fonte ductile galvanisée à chaud permettant un boulonnage rigide direct sur les charpentes et les pinces de barres.</li>
  <li><strong>Sertissage Radial Contrôlé par Émission Acoustique :</strong> Garantit une adhérence mécanique indestructible entre la bride métallique et le jonc composite sans microfissuration interne.</li>
  <li><strong>Conception Anti-Torsion Renforcée :</strong> Verrouillage interne permettant d\'encaisser des couples de manœuvre de sectionneurs supérieurs à 3,5 kN&middot;m.</li>
</ol>
'''
)

SPI_ES = dict(
    lang='es',
    dir='ltr',
    slug='substation-busbar-supports-what-is-a-station-post-insulator-es',
    title='Soportes de Barras en Subestaciones: ¿Qué es un Aislador Soporte de Subestación (Station Post Insulator)?',
    breadcrumb='Aparamenta de Subestación y Aisladores MT/AT',
    read='10 min de lectura',
    alt='Tres aisladores compuestos soporte de subestación (Serie FZSW, 110kV) soportando barras colectoras tubulares de aluminio en subestación eléctrica exterior',
    desc=('Subestaciones eléctricas de alta tensión (11kV a 110kV), patios de maniobras y soportes de barras colectoras: ¿Qué es un aislador soporte de subestación (station post)? '
          'Núcleo macizo de fibra de vidrio ECR, aletas de silicona HTV hidrófuga, resistencia extrema a flexión (4kN–16kN) y compresión (80kN–250kN), y normas IEC 62231 / ANSI C29.9.'),
    model='Serie FZSW: Aisladores Poliméricos Compuestos Soporte de Subestación para Alta Tensión (11kV a 110kV, Flexión 4kN a 16kN, Compresión 80kN a 250kN, IEC 62231 / ANSI C29.9)',
    category='Aparamenta de Subestación y Aisladores MT/AT / Aisladores Soporte de Subestación',
    kw='aislador soporte de subestacion &middot; station post insulator &middot; aislador pedestal &middot; soporte barras subestacion &middot; aislador fzsw &middot; aislador 110kv',
    specs=[
        ('Clase de Tensión Asignada de Servicio', 'Diseñado para subestaciones y patios de maniobras en alta tensión: 11kV, 24kV, 33kV, 66kV y 110kV AC (50/60 Hz)'),
        ('Carga Mecánica Especificada de Flexión (SCL)', 'Capacidad de rotura por flexión en voladizo: 4 kN, 8 kN, 10 kN, 12,5 kN y 16 kN (bajo norma IEC 62231)'),
        ('Resistencia Nominal a la Compresión Axial', 'Capacidad extrema a la compresión: 80 kN, 120 kN, 160 kN hasta 250 kN (soporta barras pesadas y seccionadores)'),
        ('Par Nominal de Rotura por Torsión Asignado', 'Alta resistencia torsional: 1,0 kN&middot;m, 2,0 kN&middot;m hasta 3,5 kN&middot;m (para ejes de seccionadores de maniobra)'),
        ('Material del Núcleo Portante de Tracción', 'Varilla maciza de gran calibre de resina epoxi reforzada con fibra de vidrio ECR libre de boro (cero porosidad interna)'),
        ('Recubrimiento Aislante y Aletas Protectoras', 'Envolvente continua moldeada en caucho de silicona HTV con hidrofobicidad permanente (Clase HC1/HC2)'),
        ('Bridas Metálicas Superior e Inferior', 'Bridas de fundición dúctil galvanizada en caliente (ASTM A153) con patrones de pernos normalizados de 4 u 8 orificios (PCD)'),
        ('Línea de Fuga Específica y Tensión de Impulso', 'Línea de fuga específica para zonas de polución muy pesada &ge; 31 mm/kV ; impulso de rayo (BIL) de hasta 550 kV')
    ],
    faqs=[
        ('¿Qué es un Aislador Soporte de Subestación (Station Post Insulator) y dónde se instala?',
         'Un Aislador Soporte de Subestación—conocido técnicamente como aislador tipo estación, aislador soporte de barras o aislador pedestal—es '
         'una columna aislante rígida de alta resistencia electromecánica diseñada para aislar eléctricamente y sostener rígidamente '
         'las barras colectoras y los equipos de maniobra en patios de subestaciones de alta tensión (AIS). '
         'En subestaciones de 11kV a 110kV : '
         '<ul>'
         '<li><strong>1. Soporte de Barras Colectoras:</strong> Montado sobre pedestales de acero para sostener tramos de tubos de aluminio '
         'que interconectan transformadores de potencia y disyuntores.</li>'
         '<li><strong>2. Columnas de Seccionadores:</strong> Sirve como soporte fijo de contactos o como columna giratoria aislante '
         'que transmite el par mecánico de apertura de las cuchillas de seccionadores de potencia.</li>'
         '<li><strong>3. Soportes de Equipos:</strong> Sostiene y aísla bancos de capacitores, trampas de onda, reactores de línea y terminales de cables.</li>'
         '</ul>'),
        ('¿En qué se diferencia un aislador Station Post de subestación de un Line Post de línea aérea?',
         'Sus terminaciones y requerimientos mecánicos son totalmente distintos: '
         '<ul>'
         '<li><strong>Aislador Station Post (Subestaciones y Barras):</strong> Posee <strong>bridas metálicas planas en ambos extremos</strong> '
         '(círculos de pernos PCD estandarizados arriba y abajo). Soporta esfuerzos multiaxiales combinados: alta <strong>compresión axial (hasta 250kN)</strong> '
         'por el peso de las barras, flexión por cortocircuitos y <strong>torsión (hasta 3,5 kN&middot;m)</strong> por maniobra de seccionadores (IEC 62231 / ANSI C29.9).</li>'
         '<li><strong>Aislador Line Post (Líneas Aéreas):</strong> Lleva una base curva para poste y una mordaza para cable arriba; trabaja solo en flexión transversal (IEC 61952).</li>'
         '</ul>'),
        ('¿Por qué los aisladores poliméricos superan a los de porcelana en subestaciones sísmicas y costeras?',
         'La porcelana es frágil y se quiebra fácilmente ante sismos. Los aisladores compuestos YOMIN FZSW ofrecen ventajas insuperables: '
         '<ul>'
         '<li><strong>Inmunidad Sísmica:</strong> El núcleo elástico de fibra de vidrio ECR absorbe las aceleraciones del terreno sin quebrarse.</li>'
         '<li><strong>Cero Lavado en Zonas Contaminadas:</strong> La silicona HTV repele el agua, anulando las corrientes de fuga bajo niebla salina sin requerir lavado.</li>'
         '<li><strong>Seguridad Operativa:</strong> No se astillan explosivamente ante arcos eléctricos, protegiendo a los operarios y transformadores vecinos.</li>'
         '</ul>')
    ],
    cta='¿Diseña subestaciones eléctricas de alta tensión, ampliaciones de barras en patios de maniobras o requiere aisladores soporte certificados bajo norma IEC 62231 / ANSI C29.9 (11kV a 110kV, compresión hasta 250kN)? YOMIN suministra aisladores soporte de subestación serie FZSW de máxima resistencia.',
    body='''
<h2>El Soporte Mecánico Inamovible para Barras Colectoras en Subestaciones de Alta Tensión</h2>
<p>En el corazón de cada subestación de transmisión y distribución de energía eléctrica que opera en <strong>11kV, 33kV, 66kV y 110kV</strong>, las barras colectoras son las arterias principales que canalizan los flujos de potencia.</p>
<p>Estos gruesos tubos de aluminio conducen continuamente miles de amperios entre los transformadores principales, los interruptores y las líneas salientes. En servicio normal, deben mantenerse rígidamente fijados a varios metros del suelo para respetar las distancias de seguridad dieléctrica.</p>
<p>No obstante, durante cortocircuitos severos en la subestación (que pueden alcanzar 40.000 amperios), surgen violentas fuerzas electromagnéticas de repulsión entre las barras de fases adyacentes. Estas ondas de choque mecánicas someten a los aisladores soporte a esfuerzos de flexión descomunales.</p>
<p>El <strong>Aislador Polimérico Compuesto Soporte de Subestación (Serie FZSW)</strong> proporciona la base estructural confiable: una columna aislante diseñada para resistir esfuerzos severos de flexión en voladizo, compresión axial y torsión bajo condiciones sísmicas y de cortocircuito pleno.</p>

<h2>Componentes y Excelencia de Ingeniería de la Serie FZSW</h2>
<ol>
  <li><strong>Varilla Maciza de Gran Calibre en Fibra de Vidrio ECR:</strong> Núcleo pultruido de alta densidad que ofrece una resistencia a la compresión axial de hasta 250 kN y una resistencia a flexión de hasta 16 kN sin fatiga.</li>
  <li><strong>Cubierta y Aletas de Caucho de Silicona HTV Hidrófuga:</strong> Proceso de moldeo continuo que anula cualquier posibilidad de fuga dieléctrica bajo niebla marina o polvo del desierto.</li>
  <li><strong>Bridas Planas Normalizadas bajo Estándar PCD:</strong> Extremos superior e inferior de fundición dúctil galvanizada en caliente con patrones de 4 u 8 orificios para empernado directo a estructuras y mordazas.</li>
  <li><strong>Engaste Radial Controlado por Emisión Acústica:</strong> Asegura una fijación mecánica perfecta entre la varilla de fibra y las bridas sin microfracturas internas.</li>
  <li><strong>Capacidad Antitorsión Reforzada:</strong> Mecanismo interno de retención que soporta pares de torsión de más de 3,5 kN&middot;m durante la maniobra de seccionadores.</li>
</ol>
'''
)

SPI_AR = dict(
    lang='ar',
    dir='rtl',
    slug='substation-busbar-supports-what-is-a-station-post-insulator-ar',
    title='محطات التحويل وقضبان التوزيع: ما هو عازل حامل محطة التحويل (Station Post Insulator)؟',
    breadcrumb='مهمات محطات التحويل وعوازل الجهد العالي',
    read='10 دقائق قراءة',
    alt='ثلاثة عوازل بوليمرية مركبة حاملة لمحطة التحويل (موديل FZSW، جهد 110kV) تحمل قضبان توزيع ألومنيوم أنبوبية في ساحة محطة تحويل خارجية',
    desc=('محطات التحويل الكهربائية للجهد العالي (11kV إلى 110kV)، وقضبان التوزيع الأنبوبية، وحوامل المعدات: ما هو عازل حامل محطة التحويل (Station Post Insulator)؟ '
          'قضيب ألياف زجاجية ECR مصمت، ومظلات مطاط السيليكون HTV، ومقاومة هائلة للانحناء (4kN–16kN) والضغط (80kN–250kN)، ومعايير IEC 62231 / ANSI C29.9.'),
    model='سلسلة FZSW: عوازل حوامل محطات التحويل البوليمرية المركبة للجهد العالي (11kV إلى 110kV، قوة انحناء 4kN إلى 16kN، قوة ضغط 80kN إلى 250kN، معتمدة IEC 62231 / ANSI C29.9)',
    category='مهمات محطات التحويل وعوازل الجهد العالي / عوازل حوامل محطات التحويل',
    kw='عازل حامل محطة تحويل &middot; station post insulator &middot; عازل بوست محطة &middot; حامل باص بار 110kv &middot; عازل fzsw &middot; عازل ستيشن بوست',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة والمحطة', 'مصمم لمحطات التحويل وساحات القواطع الخارجية للجهد العالي: 11kV و 24kV و 33kV و 66kV و 110kV AC (تردد 50/60 هرتز)'),
        ('حمل الانهيار الاسمي للانحناء الكابولي (SCL)', 'مقاومة ميكانيكية فائقة لعزوم الانحناء: 4 kN و 8 kN و 10 kN و 12.5 kN و 16 kN طبقاً للمواصفة IEC 62231'),
        ('قدرة الصمود الاسمية لقوى الضغط المحوري', 'مقاومة انضغاط محوري خارقة: 80 kN و 120 kN و 160 kN وحتى 250 kN (لحمل أثقل قضبان التوزيع والمفاتيح العازلة)'),
        ('عزم الانهيار المقنن لمقاومة قوى الالتواء', 'مقاومة عالية للالتواء الدوراني: 1.0 kN&middot;m و 2.0 kN&middot;m وحتى 3.5 kN&middot;m (لتشغيل سكاكين الفصل الدوارة بمحركات)'),
        ('مادة تصنيع القضيب المركزي الحامل', 'قضيب مصمت سميك القطر من ألياف الزجاج الإيبوكسية فئة ECR الخالية من البورون (خالٍ تماماً من الفجوات ومقاوم للأحماض)'),
        ('غلاف الحماية الخارجي ومظلات العزل', 'غلاف ومظلات مصبوبة بالحقن من مطاط السيليكون المعالج حرارياً HTV عالي الطرد للماء (فئة طرد الماء HC1/HC2)'),
        ('مواصفات الفلنجات المعدنية العلوية والسفلية', 'فلنجات من الحديد المرن المجلفن بالغمس الساخن (ASTM A153) بفتحات مسامير دائرية معيارية بـ 4 أو 8 ثقوب (PCD)'),
        ('مسافة التسرب السطحي وصمود نبضات الصواعق', 'مسافة تسرب مخصصة للتلوث الشديد &ge; 31 مم/كيلوفولت؛ صمود نبضات الصواعق العازل (BIL) حتى 550 kV')
    ],
    faqs=[
        ('ما هو عازل حامل محطة التحويل (Station Post Insulator) وما هي وظيفته الأساسية؟',
         'عازل حامل محطة التحويل—والمعروف هندسياً باسم عازل الستيشن بوست، أو عازل حامل قضبان التوزيع، أو عمود العزل الثابت للمحطات—هو '
         'عمود عزل صلب فائق المتانة الميكانيكية صُمم لتوفير العزل الكهربائي التام والدعم الميكانيكي الصلب لقضبان التوزيع الأنبوبية '
         'والمعدات الكهربائية داخل محطات التحويل الهوائية الخارجية (AIS). '
         'وفي محطات الجهد العالي من 11kV إلى 110kV : '
         '<ul>'
         '<li><strong>1. دعم قضبان التوزيع (Busbars):</strong> يثبت فوق هياكل فولاذية لحمل أنابيب الألمنيوم الثقيلة التي تربط المحولات بالقواطع.</li>'
         '<li><strong>2. قواعد سكاكين الفصل (Disconnectors):</strong> يعمل كقاعدة عزل ثابتة أو كعمود دوران عازل لنقل الحركة الدورانية لسكاكين الفصل.</li>'
         '<li><strong>3. حوامل المعدات:</strong> يحمل ويعزل مانعات الصواعق، ومصائد الموجات، وبنوك المكثفات، ونهايات الكابلات الأرضية.</li>'
         '</ul>'),
        ('ما هو الفرق الجوهري بين عازل محطة التحويل (Station Post) وعازل الخط الهوائي (Line Post)؟',
         'يختلف العازلان جذرياً في أطراف التثبيت ونمط الإجهادات الميكانيكية: '
         '<ul>'
         '<li><strong>عازل حامل المحطة (Station Post):</strong> ينتهي بـ <strong>فلنجات معدنية مستوية في كلا الطرفين</strong> '
         '(دائرة ثقوب مسامير PCD في الأعلى والأسفل). ويتحمل قوى ميكانيكية مركبة: <strong>قوى ضغط محورية هائلة (حتى 250kN)</strong> من وزن القضبان، '
         'وقوى انحناء أثناء القصر، و <strong>قوى التواء دورانية (حتى 3.5 kN&middot;m)</strong> ناتجة عن حركة سكاكين الفصل (IEC 62231 / ANSI C29.9).</li>'
         '<li><strong>عازل الخط الهوائي (Line Post):</strong> ينتهي بقاعدة منحنية للعمود من الأسفل ومشبك موصل من الأعلى؛ ويعمل في الانحناء فقط (IEC 61952).</li>'
         '</ul>'),
        ('لماذا تتفوق عوازل المحطات البوليمرية على عوازل البورسلين القديمة في البيئات الزلزالية والصحراوية؟',
         'يعتبر البورسلين مادة هشة تنكسر عند الزلازل وتتطلب غسيلاً دورياً بالمياه. توفر عوازل يمين FZSW مزايا خارقة: '
         '<ul>'
         '<li><strong>المقاومة الزلزالية:</strong> يمتص قضيب الألياف الزجاجية المرن الهزات الأرضية العنيفة دون أي كسر.</li>'
         '<li><strong>إلغاء الغسيل الدوري:</strong> يطرد مطاط السيليكون HTV المياه ويمنع تكون مسارات مائية موصلة في الضباب الملحي والأتربة.</li>'
         '<li><strong>أمان الموقع:</strong> في حال حدوث شرر كهربي، لا تتشظى العوازل المركبة لقطع حادة متطايرة، مما يحمي الفنيين والمحولات المجاورة.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصميم محطات التحويل الكهربائية للجهد العالي، أو توسعة ساحات قضبان التوزيع، أو تحتاج لعوازل حوامل محطات مركبة معتمدة IEC 62231 / ANSI C29.9 (جهد 11kV إلى 110kV، وضغط حتى 250kN)؟ تصنع يمين (YOMIN) عوازل FZSW بأعلى درجات الصلابة والمتانة.',
    body='''
<h2>الدعامة الميكانيكية الصلبة لقضبان التوزيع ومهمات محطات التحويل للجهد العالي</h2>
<p>في قلب كل محطة تحويل وتوزيع كهربائية للجهد العالي تعمل بجهد <strong>11kV و 33kV و 66kV و 110kV</strong>، تمثل قضبان التوزيع (الباص بار) الشرايين الرئيسية لتدفق الطاقة الكهربائية.</p>
<p>تنقل هذه الأنابيب الألومنيومية الضخمة تيارات مستمرة تبلغ آلاف الأمبيرات بين محولات القدرة وقواطع الدورة وخطوط النقل الخارجة. وفي ظروف التشغيل العادية، يجب أن تظل مثبتة بصلابة تامة على ارتفاع أمتار فوق سطح الأرض للحفاظ على مسافات الأمان الكهربائية.</p>
<p>ولكن عند حدوث عطل قصر كهربائي عنيف داخل المحطة (يصل إلى 40,000 أمبير)، تنشأ قوى تنافر كهرومغناطيسية هائلة بين قضبان الأطوار المتجاورة. وتسلط هذه الصدمات الميكانيكية اللحظية عزوم انحناء كابولية عنيفة على العوازل الحاملة للقضبان.</p>
<p>يقدم <strong>عازل حامل محطة التحويل البوليمري المركب (سلسلة FZSW)</strong> الأساس الهيكلي الصلب الذي لا يتزعزع: عمود عزل فائق المتانة صُمم خصيصاً لمقاومة أعتى قوى الانحناء، والضغط المحوري، والالتواء الدوراني تحت أشد ظروف القصر الكهربائي والزلازل.</p>

<h2>المكونات الهندسية وميزات الأداء الفائق لسلسلة عوازل FZSW</h2>
<ol>
  <li><strong>قضيب مصمت سميك القطر من ألياف الزجاج ECR:</strong> تصنيع دقيق بالبثق الحراري يوفر مقاومة انضغاط محوري تصل إلى 250 كيلو نيوتن ومقاومة انحناء تصل إلى 16 كيلو نيوتن دون أي إجهاد ميكانيكي.</li>
  <li><strong>غلاف ومظلات من مطاط السيليكون HTV الطارد للماء:</strong> خاصية طرد مياه دائمة تمنع تكوّن طبقات موصلة تحت الأمطار أو في البيئات الساحلية والصحراوية دون الحاجة لغسيل العوازل.</li>
  <li><strong>فلنجات معدنية مستوية مطابقة لمعايير PCD:</strong> فلنجات علوية وسفلية من الحديد المرن المجلفن بالغمس الساخن بـ 4 أو 8 ثقوب للتثبيت المباشر بالمسامير في الهياكل ومشابك القضبان.</li>
  <li><strong>كبس هيدروليكي شعاعي مراقب بالانبعاث الصوتي:</strong> يضمن تثبيتاً ميكانيكياً خارقاً بين الفلنجات المعدنية والقضيب الزجاجي دون إحداث أي شروخ مجهرية بالداخل.</li>
  <li><strong>تصميم معزز لمقاومة الالتواء الدوراني:</strong> يقاوم عزوم التواء دورانية تتجاوز 3.5 كيلو نيوتن&middot;متر، وهو أمر حاسم لتشغيل سكاكين الفصل الدوارة بمحركات.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1015 = [
    APFC_EN, APFC_FR, APFC_ES, APFC_AR,
    SPI_EN, SPI_FR, SPI_ES, SPI_AR
]
