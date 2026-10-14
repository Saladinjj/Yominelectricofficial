# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-14:
1. High-Voltage SF6 Gas Circuit Breakers for Substation Protection (EN, FR, ES, AR)
2. Busbar Window-Type Current Transformers for Switchgear Metering (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. SF6 CIRCUIT BREAKER (EN, FR, ES, AR)
# ==============================================================================

SF6_EN = dict(
    lang='en',
    dir='ltr',
    slug='high-voltage-substations-what-is-an-sf6-circuit-breaker',
    title='High-Voltage Substations: What Is an SF6 Circuit Breaker?',
    breadcrumb='High-Voltage Switchgear &amp; Substations',
    read='10 min read',
    alt='Three-phase outdoor high-voltage SF6 Gas Circuit Breaker (Model LW36 series, 110kV rating) installed in an electrical transmission substation switchyard',
    desc=('High-voltage transmission substations (40.5kV to 126kV), utility switchyards, and short-circuit fault interruption: What is an SF6 circuit breaker? '
          'How sulfur hexafluoride gas dielectric properties, puffer-type interrupters, 25kA–40kA breaking capacities, spring operating mechanisms, and IEC 62271-100 standards protect transmission grids.'),
    model='Model LW36 / LW8 Series 3-Phase Outdoor High-Voltage SF6 Gas Circuit Breakers (40.5kV to 126kV, 1250A to 3150A, 25kA to 40kA, IEC 62271-100)',
    category='High-Voltage Switchgear & Substations / SF6 Gas Circuit Breakers',
    kw='what is an sf6 circuit breaker &middot; sf6 circuit breaker &middot; sf6 gas circuit breaker &middot; high voltage sf6 breaker &middot; outdoor sf6 breaker 40.5kv &middot; lw36 circuit breaker',
    specs=[
        ('Rated System Operating Voltage Class', 'Engineered for high-voltage transmission & sub-transmission: 40.5kV, 72.5kV, and 126kV AC (50/60 Hz, 3-Phase)'),
        ('Rated Continuous Nominal Current ($I_n$)', 'Heavy current-carrying capacities: 1250 A, 1600 A, 2000 A, 2500 A, and 3150 A (temperature rise compliant with IEC 62271-1)'),
        ('Rated Short-Circuit Breaking Capacity', 'Symmetrical short-circuit fault interruption ratings: 25 kA, 31.5 kA, and 40 kA (short-circuit duration: 3.0 seconds)'),
        ('Arc Quenching Medium & Puffer Design', 'Pure sulfur hexafluoride ($SF_6$) gas with mono-pressure puffer-type (thermal blast) interrupter chambers'),
        ('Operating Mechanism Type & Drive', 'Heavy-duty motor-charged spring operating mechanism (Model CT26) with O-0.3s-CO-180s-CO rapid auto-reclosing duty cycle'),
        ('Gas Density Monitoring & Temperature Gauge', 'Integrated temperature-compensated $SF_6$ gas density monitor manometer with multi-stage electrical alarm & lockout contacts'),
        ('Annual Gas Leakage Rate Standard', 'Ultra-low hermetic sealing: certified annual $SF_6$ leakage rate $< 0.5\%$ per year (exceeding IEC 62271-1 requirements)'),
        ('Lightning Impulse & Power-Frequency Withstand', 'Dry lightning impulse withstand (BIL): up to 550 kV across open contacts; 1-min wet power frequency withstand: up to 230 kV')
    ],
    faqs=[
        ('What is an SF6 Circuit Breaker and why is Sulfur Hexafluoride gas used in high-voltage substations?',
         'An SF6 Circuit Breaker—frequently designated as a sulfur hexafluoride gas circuit breaker or gas-insulated high-voltage breaker—is '
         'a specialized high-voltage electrical switching device that utilizes pressurized sulfur hexafluoride ($SF_6$) gas as both an arc-quenching medium '
         'and a dielectric insulating barrier between open contacts. '
         'In high-voltage transmission grids and regional distribution substations: '
         '<ul>'
         '<li><strong>The Dielectric Superiority of $SF_6$:</strong> At standard atmospheric pressure, $SF_6$ gas possesses a dielectric breakdown strength '
         'approximately <strong>three times greater than air</strong>. Furthermore, $SF_6$ molecules exhibit powerful <em>electronegativity</em>—they instantly capture '
         'free electrons generated during an electrical arc, converting highly mobile electrons into heavy, slow-moving negative ions. This causes dielectric recovery '
         'speeds up to <strong>100 times faster than air</strong>, quenching massive 40,000-ampere fault arcs within milliseconds (under 3 cycles).</li>'
         '<li><strong>High-Voltage Transition Beyond Vacuum:</strong> While Vacuum Circuit Breakers (VCBs) dominate medium-voltage distribution up to 36kV/40.5kV, '
         'at higher transmission voltages (72.5kV, 110kV, 126kV, and 220kV), vacuum contact gaps become impractically large and suffer from micro-discharges and X-ray emissions. '
         '$SF_6$ circuit breakers provide seamless single-break interrupting capability at 126kV with minimal contact erosion and virtually zero current chopping transients.</li>'
         '</ul>'),
        ('How does a Puffer-Type SF6 Interrupter chamber extinguish short-circuit arcs during contact separation?',
         'YOMIN LW36 Series SF6 Circuit Breakers utilize the advanced <strong>mono-pressure puffer arc-quenching principle</strong>: '
         '<ul>'
         '<li><strong>1. Closed Position:</strong> The moving contact and puffer cylinder rest inside the stationary contact fingers, maintaining a continuous low-resistance current path.</li>'
         '<li><strong>2. Opening Initiation &amp; Compression:</strong> When a fault occurs, the spring mechanism drives the moving contact assembly backward. '
         'As the puffer cylinder slides over a fixed piston, $SF_6$ gas inside the cylinder is dynamically compressed to high pressure.</li>'
         '<li><strong>3. Contact Separation &amp; Arc Inception:</strong> As the arcing contacts separate, an intense electrical arc is drawn across the contact tips.</li>'
         '<li><strong>4. High-Velocity Gas Blast:</strong> The compressed $SF_6$ gas is forced axially through an insulating PTFE nozzle directly across the arc column. '
         'The intense axial blast cools the arc plasma, deionizes the gap, and quenches the arc at the immediate current zero transition.</li>'
         '<li><strong>5. Arc Extinction &amp; Recombination:</strong> The disassociated $SF_6$ molecules rapidly recombine into stable gas molecules, '
         'leaving zero conductive soot or toxic residue inside the sealed chamber.</li>'
         '</ul>'),
        ('How does the SF6 gas density monitor protect the high-voltage substation against low gas pressure?',
         'Dielectric strength and breaking capacity depend directly on the molecular density of the $SF_6$ gas inside the interrupter poles. '
         'Because gas pressure changes with ambient temperature, YOMIN LW36 breakers are equipped with an advanced <strong>temperature-compensated gas density monitor</strong>: '
         'The gauge uses a reference gas chamber or bimetallic compensation system that measures absolute gas density regardless of whether ambient temperatures are -40&deg;C or +50&deg;C. '
         'If gas density drops due to a slow seal leak: '
         '<ul>'
         '<li><strong>Stage 1 Alarm Contact (e.g. 0.45 MPa):</strong> Triggers an early SCADA warning to substation operators to schedule maintenance without interrupting power.</li>'
         '<li><strong>Stage 2 Electrical Lockout Contact (e.g. 0.40 MPa):</strong> Electrically locks out the breaker trip and close coils, preventing the breaker from attempting '
         'to interrupt a fault under insufficient dielectric gas pressure, which could cause breaker destruction.</li>'
         '</ul>')
    ],
    cta='Designing high-voltage transmission substations, utility switchyard expansions, renewable wind/solar interconnection bays, or industrial primary switchgear requiring certified IEC 62271-100 outdoor SF6 circuit breakers (40.5kV to 126kV, 25kA to 40kA)? YOMIN manufactures precision-engineered LW36 series gas circuit breakers.',
    body='''
<h2>The Critical Heavyweight Protection for High-Voltage Electrical Power Grids</h2>
<p>Across national high-voltage transmission grids, regional utility step-down substations, and utility-scale renewable wind and solar power plants operating at <strong>40.5kV, 72.5kV, and 126kV</strong>, the circuit breaker represents the supreme guardian of grid stability.</p>
<p>Under normal conditions, transmission circuit breakers carry continuous load currents reaching thousands of amperes. But when catastrophic line faults strike—such as direct lightning strikes on overhead transmission towers, insulator flashovers, or violent storm line clashing—fault currents surge to 25,000 to 40,000 amperes within milliseconds.</p>
<p>If a circuit breaker fails to interrupt this gargantuan flow of energy within three electrical cycles (under 60 milliseconds), massive electromagnetic forces and explosive thermal energy will incinerate multi-million-dollar power transformers, vaporize switchyard busbars, and trigger catastrophic regional blackouts.</p>
<p>The <strong>Outdoor High-Voltage SF6 Gas Circuit Breaker (Model LW36 / LW8 Series)</strong> delivers the pinnacle of heavy-duty transmission protection: utilizing the extraordinary arc-quenching and dielectric insulation properties of sulfur hexafluoride ($SF_6$) gas to extinguish violent high-voltage fault arcs with absolute reliability and zero restrike.</p>

<h2>Engineering Anatomy: Inside a Model LW36 High-Voltage SF6 Circuit Breaker</h2>
<ol>
  <li><strong>Puffer-Type Mono-Pressure Interrupter Chamber:</strong> Encased inside high-strength glazed porcelain or composite silicone insulating columns. Operates on the dynamic compression principle where moving contacts compress $SF_6$ gas to blast and extinguish short-circuit arcs at current zero.</li>
  <li><strong>Arc-Resistant Copper-Tungsten Contacts:</strong> Contact tips are precision-cast from copper-tungsten alloy ($CuW$) that withstands temperatures exceeding 10,000&deg;C during arc interruption, ensuring electrical lifespans exceeding 20 full short-circuit interruptions at 40kA.</li>
  <li><strong>Hermetically Sealed Aluminum Base &amp; Leakage Control:</strong> High-precision CNC-machined aluminum alloy enclosures with dual O-ring EPDM seals maintain certified annual gas leakage rates below 0.5%, compliant with strict environmental standards.</li>
  <li><strong>Motor-Charged Spring Operating Mechanism (CT26):</strong> Robust mechanical spring mechanism charges close and trip springs via electric motor, providing full O-0.3s-CO-180s-CO rapid auto-reclosing duty cycles independent of station auxiliary power fluctuations.</li>
  <li><strong>Temperature-Compensated Gas Density Monitor:</strong> Hermetically sealed manometer measuring true molecular gas density, featuring two-stage electrical alarm and interlock contacts to prevent switching under low dielectric pressure.</li>
</ol>

<h2>Comparison: High-Voltage SF6 Circuit Breaker vs. Vacuum Circuit Breaker vs. Air-Blast Circuit Breaker</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Obsolete Air-Blast Circuit Breaker</th>
      <th>Vacuum Circuit Breaker (VCB)</th>
      <th>YOMIN Outdoor SF6 Gas Circuit Breaker (LW36 Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Applicable Voltage Range</strong></td>
      <td>66kV to 500kV (Obsolete utility technology).</td>
      <td>Dominates Low &amp; Medium Voltage up to 36kV/40.5kV.</td>
      <td><strong>Universal High Voltage: 40.5kV, 72.5kV, 126kV, up to 252kV+.</strong></td>
    </tr>
    <tr>
      <td><strong>Dielectric Recovery &amp; Restrike Risk</strong></td>
      <td>Slow recovery; high risk of destructive restrikes.</td>
      <td>Extremely fast; but prone to high-frequency current chopping.</td>
      <td><strong>Ultra-Fast Recovery: Electronegative $SF_6$ prevents restrikes with zero current chopping.</strong></td>
    </tr>
    <tr>
      <td><strong>Maintenance Intervals &amp; Contact Wear</strong></td>
      <td>Extremely frequent (compressor maintenance every 6 months).</td>
      <td>Low maintenance; sealed vacuum bottle replaced at end-of-life.</td>
      <td><strong>Minimal Maintenance: 10,000 mechanical operations; 20+ years between major overhauls.</strong></td>
    </tr>
    <tr>
      <td><strong>Physical Footprint &amp; Noise Levels</strong></td>
      <td>Massive air compressors and deafening explosive exhaust noise.</td>
      <td>Very compact, quiet indoor switchgear installation.</td>
      <td><strong>Compact Outdoor Switchyard Footprint: Completely sealed and whisper-quiet operation.</strong></td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Breaking Reliability</strong></td>
      <td>Inconsistent under high rate-of-rise recovery voltage (RRRV).</td>
      <td>Subject to contact re-ignition at transmission voltages above 40.5kV.</td>
      <td><strong>Flawless 25kA–40kA breaking under severe out-of-phase and short-line fault conditions.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

SF6_FR = dict(
    lang='fr',
    dir='ltr',
    slug='high-voltage-substations-what-is-an-sf6-circuit-breaker-fr',
    title="Postes Électriques Haute Tension : Qu'est-ce qu'un Disjoncteur SF6 ?",
    breadcrumb='Appareillage Haute Tension &amp; Postes Électriques',
    read='10 min de lecture',
    alt='Disjoncteur haute tension extérieur triphasé à gaz SF6 (Série LW36, 110kV) installé sur structure métallique dans un poste de transformation de transport électrique',
    desc=('Postes de transport haute tension (40,5kV à 126kV), coupure des courants de court-circuit et appareillage extérieur : Qu\'est-ce qu\'un disjoncteur SF6 ? '
          'Propriétés diélectriques du gaz hexafluorure de soufre, chambres de coupure autopneumatiques, pouvoir de coupure 25kA–40kA, commande à ressorts et norme CEI 62271-100.'),
    model='Série LW36 / LW8 : Disjoncteurs Extérieurs Haute Tension à Gaz SF6 (40,5kV à 126kV, 1250A à 3150A, 25kA à 40kA, CEI 62271-100)',
    category='Appareillage Haute Tension & Postes Électriques / Disjoncteurs SF6',
    kw='disjoncteur sf6 &middot; disjoncteur haute tension sf6 &middot; disjoncteur gaz sf6 &middot; poste haute tension 110kv &middot; lw36 breaker &middot; coupure sf6',
    specs=[
        ('Tension Assignée de Service du Réseau', 'Conçu pour les réseaux de transport et de répartition HT : 40,5kV, 72,5kV et 126kV AC triphasé (50/60 Hz)'),
        ('Courant Nominal Permanent Assigné ($I_n$)', 'Capacité thermique continue : 1250 A, 1600 A, 2000 A, 2500 A et 3150 A (échauffement normalisé selon CEI 62271-1)'),
        ('Pouvoir Assigné de Coupure en Court-Circuit', 'Pouvoir de coupure symétrique : 25 kA, 31,5 kA et 40 kA (durée assignée de court-circuit : 3,0 secondes)'),
        ('Milieu d\'Extinction de l\'Arc et Chambre', 'Gaz hexafluorure de soufre pur ($SF_6$) sous pression avec chambre de coupure autopneumatique mono-pression (puffer)'),
        ('Mécanisme de Commande et Réarmement', 'Commande mécanique à accumulation d\'énergie par ressorts motorisés (Type CT26) avec cycle de réenclenchement O-0,3s-FO-180s-FO'),
        ('Surveillance de Densité du Gaz et Manomètre', 'Densimètre de gaz $SF_6$ à compensation thermique automatique avec contacts électriques d\'alarme et de verrouillage'),
        ('Taux Annuel de Fuite de Gaz Normalisé', 'Étanchéité hermétique renforcée : taux de fuite annuel certifié $< 0,5\%$ par an (strictement conforme CEI 62271-1)'),
        ('Tension de Tenue aux Chocs de Foudre (BIL)', 'Onde de choc de foudre 1,2/50 &mu;s jusqu\'à 550 kV ; tension de tenue à fréquence industrielle sous pluie jusqu\'à 230 kV')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Disjoncteur SF6 et pourquoi l\'hexafluorure de soufre est-il le fluide roi en haute tension ?',
         'Un Disjoncteur SF6—couramment désigné sous le terme de disjoncteur à gaz hexafluorure de soufre—est '
         'un appareil électromécanique haute tension qui utilise le gaz $SF_6$ sous pression à la fois comme milieu d\'extinction d\'arc '
         'et comme isolant diélectrique entre contacts ouverts. '
         'Dans les postes de transport et de transformation HT : '
         '<ul>'
         '<li><strong>Les Propriétés Exceptionnelles du $SF_6$ :</strong> À pression atmosphérique, le $SF_6$ possède une rigidité diélectrique '
         '<strong>trois fois supérieure à celle de l\'air</strong>. De plus, sa molécule est fortement <em>électronégative</em> : elle capture instantanément '
         'les électrons libres de l\'arc électrique pour former des ions lourds et stables. La régénération diélectrique est <strong>100 fois plus rapide que dans l\'air</strong>, '
         'éteignant des arcs de court-circuit de 40 000 ampères en moins de 50 millisecondes.</li>'
         '<li><strong>Le Relais Naturel du Vide au-delà de 40,5kV :</strong> Si les ampoules à vide dominent en moyenne tension (jusqu\'à 36kV), '
         'aux tensions de 72,5kV et 110kV l\'intervalle entre contacts dans le vide nécessiterait des courses mécaniques excessives avec risque d\'émission de rayons X. '
         'Le disjoncteur SF6 permet une coupure unique simple et ultra-fiable sans aucun phénomène d\'arrachement de courant destructeur.</li>'
         '</ul>'),
        ('Comment fonctionne la chambre de coupure autopneumatique (puffer) lors de l\'ouverture ?',
         'Les disjoncteurs YOMIN Série LW36 utilisent le principe <strong>autopneumatique à soufflage de gaz</strong> : '
         'Lors du déclenchement, les contacts mobiles reculent sous l\'action des ressorts. Un cylindre solidaire du contact mobile coulisse sur un piston fixe, '
         'comprimant mécaniquement le gaz $SF_6$. Dès que les contacts d\'arc se séparent, une buse isolante en PTFE canalise un jet violent de gaz froid sous pression '
         'directement sur la colonne de l\'arc électrique, le refroidissant et le soufflant au passage par zéro du courant.'),
        ('Comment le densimètre protège-t-il le disjoncteur contre une baisse de pression de gaz ?',
         'La rigidité diélectrique dépendant de la masse moléculaire du gaz, les disjoncteurs YOMIN LW36 intègrent un <strong>densimètre à compensation de température</strong> : '
         'Il mesure la densité absolue du gaz indépendamment des variations climatiques (-40&deg;C à +50&deg;C). En cas de fuite lente : '
         '<ul>'
         '<li><strong>Contact Seuil 1 (Alarme, 0,45 MPa) :</strong> Émet une alerte télétransmise au centre de conduite pour planifier un appoint de gaz sans couper le courant.</li>'
         '<li><strong>Contact Seuil 2 (Verrouillage, 0,40 MPa) :</strong> Verrouille électriquement les circuits de déclenchement et d\'enclenchement, empêchant le disjoncteur '
         'de couper sous une pression insuffisante qui risquerait de détruire l\'appareil.</li>'
         '</ul>')
    ],
    cta='Vous concevez des postes de transport haute tension, des sous-stations d\'évacuation d\'énergie renouvelable éolienne/solaire ou recherchez des disjoncteurs extérieurs SF6 certifiés CEI 62271-100 (40,5kV à 126kV, 25kA à 40kA) ? YOMIN fabrique des disjoncteurs haute tension série LW36 de premier ordre.',
    body='''
<h2>Le Protecteur Suprême des Réseaux Électriques de Transport Haute Tension</h2>
<p>Sur les réseaux de transport et de grand transport d\'électricité fonctionnant sous des tensions de <strong>40,5kV, 72,5kV et 126kV</strong>, le disjoncteur de poste constitue l\'organe de sécurité absolu du réseau national.</p>
<p>En exploitation normale, ces appareils assurent le transit de puissances considérables. Mais lorsqu\'un court-circuit violent frappe la ligne aérienne—suite à un coup de foudre direct ou à la rupture d\'un conducteur—l\'intensité du courant bondit instantanément à plus de 40 000 ampères.</p>
<p>Si le disjoncteur n\'interrompt pas cette énergie colossale en moins de trois périodes (soit 60 millisecondes), les efforts électrodynamiques et l\'énergie thermique détruisent instantanément les transformateurs de puissance et provoquent des blackouts régionaux généralisés.</p>
<p>Le <strong>Disjoncteur Extérieur Haute Tension à Gaz SF6 (Série LW36 / LW8)</strong> apporte la solution technologique éprouvée mondialement : il exploite les propriétés exceptionnelles de l\'hexafluorure de soufre ($SF_6$) pour étouffer les arcs électriques les plus violents avec une sécurité absolue et sans réamorçage.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série LW36</h2>
<ol>
  <li><strong>Chambre de Coupure Autopneumatique Mono-Pression :</strong> Logée dans des colonnes isolantes en porcelaine vitrifiée ou en silicone composite, elle assure une extinction d\'arc douce et sans surtension grâce à une tuyère en PTFE haute température.</li>
  <li><strong>Contacts d\'Arc en Cuivre-Tungstène Haute Ténacité :</strong> Alliage réfractaire résistant à des températures d\'arc de plus de 10 000&deg;C, garantissant plus de 20 coupures en court-circuit maximal sans remplacement de contacts.</li>
  <li><strong>Étanchéité Renforcée et Taux de Fuite $< 0,5\%$ par An :</strong> Enveloppes usinées sous contrôle numérique avec joints toriques EPDM doublés garantissant le confinement parfait du gaz pendant des décennies.</li>
  <li><strong>Commande Mécanique à Ressorts Motorisés CT26 :</strong> Mécanisme robuste permettant des cycles complets de réenclenchement rapide sans dépendre de compresseurs d\'air comprimé ou de circuits hydrauliques complexes.</li>
  <li><strong>Densimètre à Compensation Thermique :</strong> Surveillance en continu de la densité moléculaire du gaz avec double seuil d\'alarme et de verrouillage électrique.</li>
</ol>
'''
)

SF6_ES = dict(
    lang='es',
    dir='ltr',
    slug='high-voltage-substations-what-is-an-sf6-circuit-breaker-es',
    title='Subestaciones de Alta Tensión: ¿Qué es un Interruptor de Potencia en SF6?',
    breadcrumb='Aparamenta de Alta Tensión y Subestaciones',
    read='10 min de lectura',
    alt='Interruptor de potencia exterior de alta tensión en gas SF6 trifásico (Serie LW36, 110kV) instalado sobre estructura de acero en patio de subestación eléctrica',
    desc=('Subestaciones de transmisión en alta tensión (40,5kV a 126kV), patios de maniobras y despeje de fallas de cortocircuito: ¿Qué es un interruptor de potencia en SF6? '
          'Propiedades dieléctricas del gas hexafluoruro de azufre, cámaras de autosoplado tipo puffer, capacidad de corte 25kA–40kA, mando por resortes y norma IEC 62271-100.'),
    model='Serie LW36 / LW8: Interruptores de Potencia Tipo Intemperie en Gas SF6 para Alta Tensión (40,5kV a 126kV, 1250A a 3150A, 25kA a 40kA, IEC 62271-100)',
    category='Aparamenta de Alta Tensión y Subestaciones / Interruptores en SF6',
    kw='interruptor sf6 &middot; interruptor de potencia alta tension &middot; interruptor en gas sf6 &middot; subestacion 110kv &middot; lw36 interruptor &middot; disyuntor sf6',
    specs=[
        ('Clase de Tensión Asignada de Servicio', 'Diseñado para redes de transmisión y subtransmisión en alta tensión: 40,5kV, 72,5kV y 126kV AC trifásico (50/60 Hz)'),
        ('Corriente Nominal Continua Asignada ($I_n$)', 'Capacidades de corriente permanente: 1250 A, 1600 A, 2000 A, 2500 A y 3150 A (elevación de temperatura bajo norma IEC 62271-1)'),
        ('Poder Asignado de Corte en Cortocircuito', 'Capacidad simétrica de interrupción de falla: 25 kA, 31,5 kA y 40 kA (duración de cortocircuito asignada: 3,0 segundos)'),
        ('Medio de Extinción del Arco y Cámara', 'Gas hexafluoruro de azufre puro ($SF_6$) presurizado con cámara de extinción autopneumática mono-presión tipo puffer'),
        ('Tipo de Mecanismo de Accionamiento', 'Mando mecánico por resortes precargados por motor eléctrico (Tipo CT26) con ciclo de recierre rápido O-0,3s-CO-180s-CO'),
        ('Monitor de Densidad de Gas con Manómetro', 'Densímetro de gas $SF_6$ con compensación térmica automática dotado de contactos eléctricos de alarma y enclavamiento'),
        ('Tasa Anual de Fuga de Gas Certificada', 'Sellado hermético de alta seguridad: tasa anual de fuga certificada $< 0,5\%$ anual (cumplimiento estricto IEC 62271-1)'),
        ('Tensión Soportada al Impulso de Rayo (BIL)', 'Onda de rayo 1,2/50 &mu;s de hasta 550 kV entre contactos abiertos ; tensión soportada bajo lluvia a frecuencia industrial hasta 230 kV')
    ],
    faqs=[
        ('¿Qué es un Interruptor en SF6 y por qué el hexafluoruro de azufre es el medio rey en alta tensión?',
         'Un Interruptor de Potencia en SF6—también denominado disyuntor en gas hexafluoruro de azufre—es '
         'un equipo de interrupción electromecánico de alta tensión que utiliza gas $SF_6$ presurizado como medio de extinción del arco eléctrico '
         'y aislante dieléctrico entre sus contactos abiertos. '
         'En subestaciones de transmisión y patios de maniobras: '
         '<ul>'
         '<li><strong>Superioridad Dieléctrica del Gas $SF_6$:</strong> A presión atmosférica, el gas $SF_6$ posee una rigidez dieléctrica '
         '<strong>tres veces superior a la del aire</strong>. Su molécula es extraordinariamente <em>electronegativa</em>: captura al instante '
         'los electrones libres generados por el arco, convirtiéndolos en iones pesados. Esto permite una velocidad de recuperación dieléctrica '
         '<strong>100 veces más rápida que el aire</strong>, extinguiendo arcos de 40.000 amperios en menos de 3 ciclos (50 ms).</li>'
         '<li><strong>El Límite del Vacío por Encima de 40,5kV:</strong> Aunque los interruptores de vacío (VCB) dominan en media tensión hasta 36kV, '
         'a tensiones de transmisión de 72,5kV o 110kV las botellas de vacío requerirían carreras mecánicas excesivas con riesgo de emisión de rayos X. '
         'El interruptor en SF6 proporciona una interrupción limpia, suave y sin sobretensiones por corte de corriente en un solo punto de ruptura.</li>'
         '</ul>'),
        ('¿Cómo extingue el cortocircuito la cámara de soplado autopneumático (tipo puffer)?',
         'Los interruptores YOMIN Serie LW36 utilizan el principio de <strong>autosoplado mecánico tipo puffer</strong>: '
         'Al producirse el disparo, el cilindro móvil retrocede accionado por los resortes mecánicos, deslizándose sobre un pistón fijo. '
         'Este movimiento comprime mecánicamente el gas $SF_6$ contenido en su interior. En cuanto los contactos de arco se separan, '
         'una tobera de PTFE dirige un chorro de gas frío a alta velocidad contra la columna de plasma, enfriándolo y extinguiéndolo al cruce por cero de la corriente.'),
        ('¿Cómo protege el densímetro al interruptor ante una fuga imprevista de presión?',
         'La capacidad de corte y aislamiento depende de la masa molecular del gas. Los interruptores YOMIN LW36 cuentan con un <strong>densímetro con compensación de temperatura</strong>: '
         'Mide la densidad real del gas sin verse afectado por si la temperatura exterior es de -40&deg;C o +50&deg;C. Si la densidad cae por una fuga: '
         '<ul>'
         '<li><strong>Contacto Nivel 1 (Alarma a 0,45 MPa):</strong> Envía una señal al centro de control SCADA para recargar gas sin desconectar la línea.</li>'
         '<li><strong>Contacto Nivel 2 (Enclavamiento a 0,40 MPa):</strong> Bloquea eléctricamente los circuitos de apertura y cierre, impidiendo que el interruptor '
         'intente operar con presión insuficiente, lo que destruiría el equipo.</li>'
         '</ul>')
    ],
    cta='¿Diseña subestaciones de transmisión en alta tensión, proyectos de evacuación de energía solar/eólica o requiere interruptores de potencia en SF6 certificados bajo norma IEC 62271-100 (40,5kV a 126kV, 25kA a 40kA)? YOMIN suministra interruptores de alta tensión serie LW36 de máxima confiabilidad.',
    body='''
<h2>El Guardián Principal de las Redes de Transmisión Eléctrica en Alta Tensión</h2>
<p>En redes de transmisión de energía eléctrica, subestaciones reductoras de servicios públicos y parques de generación renovable solar y eólica que operan en <strong>40,5kV, 72,5kV y 126kV</strong>, el interruptor de potencia es el equipo más crítico para la estabilidad del sistema.</p>
<p>Bajo condiciones normales, conduce miles de amperios continuos. Sin embargo, cuando ocurre un cortocircuito severo en la línea de transmisión—provocado por rayos o tormentas—la corriente de falla alcanza valores destructivos de entre 25.000 y 40.000 amperios.</p>
<p>Si el interruptor no despeja esta colosal cantidad de energía en menos de tres ciclos eléctricos (60 milisegundos), las fuerzas electromagnéticas y térmicas destruyen transformadores de potencia y provocan apagones masivos en ciudades enteras.</p>
<p>El <strong>Interruptor de Potencia Tipo Intemperie en Gas SF6 (Serie LW36 / LW8)</strong> constituye el estándar probado en subestaciones de todo el mundo: utiliza las propiedades únicas del gas hexafluoruro de azufre ($SF_6$) para extinguir arcos eléctricos violentos con total seguridad y sin reigniciones.</p>

<h2>Componentes y Excelencia de Ingeniería de la Serie LW36</h2>
<ol>
  <li><strong>Cámara de Interrupción de Autosoplado Mono-Presión:</strong> Alojada en columnas aislantes de porcelana o silicona compuesta, asegura una rápida extinción del arco mediante una tobera de PTFE resistente al desgaste.</li>
  <li><strong>Contactos de Arco de Aleación Cobre-Tungsteno:</strong> Resistentes a temperaturas de arco de más de 10.000&deg;C, garantizan más de 20 operaciones a máxima capacidad de cortocircuito sin necesidad de recambio.</li>
  <li><strong>Sellado Hermético de Alta Confiabilidad:</strong> Carcasas de aleación de aluminio mecanizadas con precisión CNC y sellos EPDM que aseguran una tasa de fuga inferior al 0,5% anual.</li>
  <li><strong>Mando Mecánico por Resortes Motorizados CT26:</strong> Robusto accionamiento mecánico que asegura ciclos de recierre rápido sin requerir costosos compresores de aire ni sistemas hidráulicos.</li>
  <li><strong>Densímetro con Compensación de Temperatura:</strong> Supervisión continua con doble contacto eléctrico de alarma y enclavamiento ante caídas de presión dieléctrica.</li>
</ol>
'''
)

SF6_AR = dict(
    lang='ar',
    dir='rtl',
    slug='high-voltage-substations-what-is-an-sf6-circuit-breaker-ar',
    title='محطات التحويل الكهربائية للجهد العالي: ما هو قاطع الدورة بغاز سداسي فلوريد الكبريت (SF6 Circuit Breaker)؟',
    breadcrumb='مهمات الجهد العالي ومحطات التحويل',
    read='10 دقائق قراءة',
    alt='قاطع دورة للجهد العالي خارجي ثلاثي الأطوار بغاز سداسي فلوريد الكبريت SF6 (موديل LW36، جهد 110kV) مركب في ساحة محطة تحويل كهربائية',
    desc=('محطات نقل الكهرباء للجهد العالي (40.5kV إلى 126kV)، وقواطع الدورة الخارجية، وفصل تيارات القصر الكهربائي: ما هو قاطع الدورة بغاز SF6؟ '
          'الخصائص العازلة الفائقة لغاز سداسي فلوريد الكبريت، وغرف الإطفاء بالنفخ الذاتي، وقدرة القطع 25kA–40kA، وآلية التشغيل بالزنبرك ومعيار IEC 62271-100.'),
    model='سلسلة LW36 / LW8: قواطع الدورة الخارجية للجهد العالي بغاز سداسي فلوريد الكبريت SF6 (40.5kV إلى 126kV، 1250A إلى 3150A، 25kA إلى 40kA، معتمدة IEC 62271-100)',
    category='مهمات الجهد العالي ومحطات التحويل / قواطع الدورة بغاز SF6',
    kw='قاطع دورة sf6 &middot; قاطع جهد عالي sf6 &middot; قاطع غاز سداسي فلوريد الكبريت &middot; محطة تحويل 110kv &middot; lw36 breaker &middot; قاطع كهربائي للجهد العالي',
    specs=[
        ('فئة جهد التشغيل الاسمي للشبكة', 'مصمم لشبكات نقل وتوزيع الطاقة للجهد العالي: 40.5kV و 72.5kV و 126kV AC ثلاثي الأطوار (تردد 50/60 هرتز)'),
        ('التيار الاسمي الدائم لقاطع الدورة ($I_n$)', 'قدرات تيار مستمر فائقة: 1250 A و 1600 A و 2000 A و 2500 A و 3150 A (ارتفاع حرارة معتمد وفقاً للمواصفة IEC 62271-1)'),
        ('سعة قطع تيار القصر المتماثل المعتمدة', 'قدرة إطفاء تيارات القصر الكهربائي: 25 kA و 31.5 kA و 40 kA (فترة صمود تيار القصر الاسمي: 3.0 ثوانٍ)'),
        ('وسط إطفاء الشرر الكهربائي وتصميم الغرفة', 'غاز سداسي فلوريد الكبريت النقي ($SF_6$) تحت الضغط مع غرف إطفاء أحادية الضغط بنظام النفخ الذاتي (Puffer-Type)'),
        ('آلية التشغيل الميكانيكي وشحن الحركة', 'آلية تشغيل ميكانيكية بزنبركات مشحونة بمحرك كهربائي (طراز CT26) بدورة إعادة وصل أوتوماتيكية سريعة O-0.3s-CO-180s-CO'),
        ('مراقبة كثافة الغاز ومقياس الضغط', 'مانومتر مراقبة كثافة غاز $SF_6$ معوض حرارياً ومزود بنقاط تلامس كهربائية مزدوجة للإنذار المبكر وحظر التشغيل الآلي'),
        ('معدل تسريب الغاز السنوي المعتمد دولياً', 'إحكام غلق هرمسي فائق الدقة: معدل تسريب سنوي معتمد أقل من ($< 0.5\%$) سنوياً (مطابق بصرامة للمواصفة IEC 62271-1)'),
        ('صمود نبضات الصواعق والتردد الصناعي', 'جهد صمود نبضة صاعقة 1.2/50 &mu;s حتى 550 kV بين الأطراف؛ جهد صمود تردد صناعي مبلل لمدة دقيقة حتى 230 kV')
    ],
    faqs=[
        ('ما هو قاطع الدورة بغاز SF6 ولماذا يعتبر غاز سداسي فلوريد الكبريت هو الأفضل عالمياً في محطات الجهد العالي؟',
         'قاطع الدورة بغاز SF6—والمعروف هندسياً باسم قاطع القدرة الغازي أو قاطع الجهد العالي بغاز سداسي فلوريد الكبريت—هو '
         'جهاز فصل ووصل كهروميكانيكي عالي القدرة يستخدم غاز $SF_6$ المضغوط كوسيط لإطفاء القوس الكهربائي وعازل ديزلكتريكي بين نقاط التلامس المفتوحة. '
         'وفي محطات نقل الكهرباء والتحويل الرئيسية: '
         '<ul>'
         '<li><strong>الخصائص العازلة الخارقة لغاز $SF_6$:</strong> عند الضغط الجوي العادي، يمتلك غاز $SF_6$ قوة عزل كهربائي تفوق <strong>ثلاثة أضعاف قوة الهواء</strong>. '
         'وعلاوة على ذلك، تتميز جزيئات الغاز بخاصية <em>الكهروسلبية الشديدة</em>؛ حيث تلتهم الإلكترونات الحرة المتولدة داخل القوس الكهربائي فوراً '
         'وتحولها إلى أيونات سالبة ثقيلة. هذا يمنح الغاز سرعة استعادة عزل تفوق <strong>100 ضعف سرعة الهواء</strong>، متمكناً من إخماد أقواس قصر '
         'تتجاوز 40,000 أمبير في أقل من 50 مللي ثانية (أقل من 3 دورات كهربائية).</li>'
         '<li><strong>بديل التفريغ في الجهود العالية:</strong> بينما تسيطر قواطع التفريغ (VCB) على الجهد المتوسط حتى 36kV، فإنه عند جهود النقل '
         '(72.5kV و 110kV و 126kV) تتطلب حجرات التفريغ مسافات فصل كبيرة جداً وتصدر إشعاعات سينية. يوفر قاطع الـ SF6 نقطة قطع واحدة فائقة النظافة '
         'ودون أي قفزات جهدية ناتجة عن التقطيع الحاد للتيار.</li>'
         '</ul>'),
        ('كيف تعمل غرفة الإطفاء بالنفخ الذاتي (Puffer-Type) على إخماد تيارات القصر الهائلة؟',
         'تعتمد قواطع يمين سلسلة LW36 على تقنية <strong>النفخ الذاتي أحادي الضغط</strong>: '
         'عند صدور أمر الفصل، تتحرك نقاط التلامس المتحركة للخلف بقوة زنبركات الميكانيزم. ويتحرك أسطوانة النفخ فوق مكبس ثابت، '
         'مما يؤدي لضغط غاز $SF_6$ ميكانيكياً داخل الأسطوانة. وبمجرد تباعد نقاط تلامس الشرر، توجه فوهة عازلة من مادة PTFE تياراً عاتياً '
         'من الغاز البارد عالي الضغط على عمود القوس الكهربائي، مما يبرده ويزيل تأينه فور وصول موجة التيار إلى نقطة الصفر الطبيعي.'),
        ('كيف يحمي مقياس كثافة الغاز القاطع من مخاطر انخفاض الضغط الداخلي؟',
         'بما أن كفاءة العزل وإطفاء الشرر ترتبط بالكتلة الجزيئية للغاز، زُودت قواطع LW36 بـ <strong>مقياس كثافة غاز معوض حرارياً</strong>: '
         'يقيس الكثافة الحقيقية لجزيئات الغاز بغض النظر عما إذا كانت حرارة الجو الخارجية -40&deg;C أو +50&deg;C. وإذا حدث تسريب تدريجي: '
         '<ul>'
         '<li><strong>المرحلة الأولى (إنذار عند 0.45 MPa):</strong> يرسل إشارة تحذير لنظام المراقبة SCADA لجدولة شحن الغاز دون فصل الكهرباء عن الشبكة.</li>'
         '<li><strong>المرحلة الثانية (حظر التشغيل عند 0.40 MPa):</strong> يغلق دوائر الفصل والوصل كهربائياً، مانعاً القاطع من محاولة إطفاء تيار القصر '
         'تحت ضغط عازل غير كافٍ قد يؤدي لانفجار القاطع.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصميم محطات التحويل الكهربائية للجهد العالي، أو مشاريع ربط محطات الطاقة الشمسية وطاقة الرياح بالشبكة العامة، أو تحتاج لقواطع دورة خارجية بغاز SF6 معتمدة IEC 62271-100 (جهد 40.5kV إلى 126kV، وقدرة قطع 25kA إلى 40kA)؟ تصنع يمين (YOMIN) قواطع LW36 بأعلى معايير الأمان الهندسي.',
    body='''
<h2>الحارس الفولاذي الأهم لشبكات نقل وتوزيع الطاقة الكهربائية للجهد العالي</h2>
<p>عبر شبكات نقل الكهرباء الوطنية، ومحطات التحويل الرئيسية، ومحطات توليد الطاقة المتجددة الكبرى العاملة بجهد <strong>40.5kV و 72.5kV و 126kV</strong>، يمثل قاطع الدورة الحصن الحصين لاستقرار المنظومة الكهربائية بأكملها.</p>
<p>في ظروف التشغيل العادية، تمر عبر القاطع تيارات حمل مستمرة تبلغ آلاف الأمبيرات. ولكن عند وقوع عطل قصر كارثي على خطوط النقل الهوائية—بسبب الصواعق أو العواصف العاتية—تقفز تيارات العطل في أجزاء من الثانية إلى قيم تدميرية تتراوح بين 25,000 و 40,000 أمبير.</p>
<p>وإذا عجز قاطع الدورة عن عزل هذه الطاقة الهائلة خلال ثلاثة أجزاء من الثانية (أقل من 60 مللي ثانية)، فإن القوى الكهروديناميكية والحرارية الانفجارية ستدمر محولات القدرة وتؤدي إلى انهيار الشبكة الكهربائية وانقطاع التيار عن مدن بأكملها.</p>
<p>يقدم <strong>قاطع الدورة الخارجي للجهد العالي بغاز سداسي فلوريد الكبريت (سلسلة LW36 / LW8)</strong> الحل الهندسي القياسي المعتمد عالمياً: حيث يستغل الخواص الفريدة لغاز $SF_6$ لإخماد أعنف أقواس القصر الكهربائي بأعلى درجات الموثوقية وبدون أي ارتداد شرري.</p>

<h2>المكونات الهندسية وميزات الأداء الفائق لسلسلة قواطع LW36</h2>
<ol>
  <li><strong>غرفة قطع بنظام النفخ الذاتي أحادي الضغط:</strong> محاطة بأعمدة عازلة من البورسلين المزجج أو السيليكون المركب، تضمن إطفاءً انسيابياً للقوس عبر فوهة تيفلون PTFE شديدة المقاومة للحرارة.</li>
  <li><strong>نقاط تلامس شرر من سبيكة النحاس والتنجستن:</strong> تتحمل درجات حرارة شرر تتجاوز 10,000&deg;C وتصمد لأكثر من 20 عملية قطع لتيار القصر الأقصى دون الحاجة لصيانة.</li>
  <li><strong>هيكل محكم السد بمعدل تسريب سنوي $< 0.5\%$:</strong> تصنيع دقيق بآلات التحكم الرقمي CNC مع حلقات جوان EPDM مزدوجة تمنع أي تسرب للغاز على مدار عشرات السنين.</li>
  <li><strong>آلية تشغيل ميكانيكية بزنبركات مشحونة CT26:</strong> توفر طاقة حركية جبارة لإتمام دورات إعادة الوصل السريع دون الاعتماد على ضواغط هواء أو دوائر زيت هيدروليكية معقدة.</li>
  <li><strong>مقياس كثافة غاز معوض حرارياً:</strong> رصد مستمر لكثافة الغاز مع مرحلتي إنذار وحظر تشغيل لحماية الشبكة والمحطة من أي خطأ تشغيلي.</li>
</ol>
'''
)

# ==============================================================================
# 2. BUSBAR CURRENT TRANSFORMER (EN, FR, ES, AR)
# ==============================================================================

BCT_EN = dict(
    lang='en',
    dir='ltr',
    slug='switchgear-metering-what-is-a-busbar-current-transformer',
    title='Switchgear Metering: What Is a Busbar Current Transformer?',
    breadcrumb='Current Transformers &amp; Switchgear Metering',
    read='10 min read',
    alt='Low-voltage measuring Busbar Window-Type Current Transformer (Model MSQ series, Class 0.5) mounted directly over vertical copper busbars inside an electrical switchboard',
    desc=('Low-voltage switchboards, main distribution boards (MDB), motor control centers (MCC), and busbar metering: What is a busbar current transformer? '
          'How rectangular window apertures (30x10 to 120x10mm), primary currents 100A–5000A, secondary 5A/1A outputs, Class 0.5/0.2 accuracy, and IEC 61869-2 standards simplify switchgear panel instrumentation.'),
    model='Model MSQ / BH-0.66 Series Low-Voltage Measuring Busbar Window-Type Current Transformers (0.66kV, 100A to 5000A, Class 0.5 / Class 0.2, IEC 61869-2)',
    category='Current Transformers & Switchgear Metering / Busbar Window CTs',
    kw='what is a busbar current transformer &middot; busbar current transformer &middot; window type current transformer &middot; msq current transformer &middot; switchgear ct 5a &middot; bh 0.66 ct',
    specs=[
        ('Rated System Operating Voltage Class', 'Low-voltage distribution class: $U_m = 0.72$ kV / 0.66 kV AC (insulation test voltage: 3.0 kV for 1 minute at 50/60 Hz)'),
        ('Primary Current Measurement Range ($I_{pn}$)', 'Standard primary ratings: 100A, 150A, 200A, 250A, 300A, 400A, 500A, 600A, 800A, 1000A, 1200A, up to 5000A'),
        ('Rated Secondary Output Current ($I_{sn}$)', 'Standard switchboard secondary instrument ratings: 5 A (standard) or 1 A (long cable runs to remote control panels)'),
        ('Measurement Accuracy Classes Available', 'Class 0.5 (standard utility billing & switchboard submetering) and Class 0.2 / 0.2S (high-precision laboratory & revenue metering)'),
        ('Window Aperture Dimensions Available', 'Engineered to fit standard copper busbars: 30x10mm (MSQ-30), 40x10mm (MSQ-40), 60x10mm (MSQ-60), up to 120x10mm (MSQ-120)'),
        ('Rated Output Burden & Capacity Rating', 'Standard secondary burden ratings: 2.5 VA, 5 VA, 10 VA, 15 VA, up to 30 VA (matching digital multifunction meters)'),
        ('Housing Construction & Fire Retardancy', 'Ultrasonically welded self-extinguishing flame-retardant ABS / polycarbonate casing (UL94 V-0 flame rating)'),
        ('Mounting Accessories & Terminal Security', 'Integrated plastic busbar clamping screws, metal bottom DIN-rail/chassis brackets, and sealable transparent terminal cover')
    ],
    faqs=[
        ('What is a Busbar Current Transformer and how does its window-type design function in low-voltage switchboards?',
         'A Busbar Current Transformer—frequently designated as a window-type current transformer, busbar-mounted CT, or ring-type measuring CT—is '
         'a specialized low-voltage instrument transformer designed with a hollow central window aperture that slips directly over '
         'a solid copper or aluminum busbar without requiring any physical disconnection, cutting, or bolting of the primary electrical conductor. '
         'In modern electrical distribution switchboards and motor control centers (MCC): '
         '<ul>'
         '<li><strong>The Window-Type Operating Principle:</strong> The solid copper busbar itself serves as the single-turn primary winding ($N_1 = 1$). '
         'As alternating load current ($I_p$) flows through the busbar, it induces a proportional magnetic flux inside the high-permeability toroidal silicon steel core. '
         'The secondary coil, tightly wound with multiple turns of enameled copper wire ($N_2$), produces a stepped-down proportional secondary current ($I_s = 5$A or 1A) '
         'governed by the transformer turns ratio: $$I_s = I_p \times \frac{N_1}{N_2}$$</li>'
         '<li><strong>Seamless Panel Assembly:</strong> During switchgear fabrication, panel builders slide the lightweight MSQ series CT over the busbar riser, '
         'tighten the integrated insulated clamping screws against the copper bar, and wire the secondary terminals (S1, S2) directly to digital power meters, '
         'multimeters, or energy management controllers.</li>'
         '</ul>'),
        ('How do switchboard builders select the correct window aperture size for copper busbars?',
         'Selecting the correct window-type CT aperture is essential to avoid mechanical interference and thermal overheating: '
         '<ul>'
         '<li><strong>MSQ-30 (Window 30x10mm or &phi;30mm round):</strong> Ideal for smaller distribution boards with primary currents from 100A to 300A. '
         'Accommodates a single 30x10mm copper bar or insulated power cables up to 30mm diameter.</li>'
         '<li><strong>MSQ-40 (Window 40x10mm):</strong> Used for 300A to 600A main breakers and feeder switches, accepting standard 40x10mm copper busbars.</li>'
         '<li><strong>MSQ-60 (Window 60x10mm or two 50x10mm bars):</strong> The workhorse for 600A to 1200A main distribution boards, accepting single or double busbars.</li>'
         '<li><strong>MSQ-100 / MSQ-120 (Window 100x10mm to 120x10mm):</strong> High-capacity switchboards from 1200A to 5000A, fitting multiple parallel busbars.</li>'
         '</ul>'),
        ('What is the difference between Class 0.5 and Class 0.2 accuracy, and when should 1A secondary be chosen over 5A?',
         'The accuracy class defines the maximum allowable percentage ratio error at rated current according to IEC 61869-2: '
         '<ul>'
         '<li><strong>Class 0.5 (&plusmn;0.5% Ratio Error):</strong> The universal industry standard for commercial submetering, motor control centers, '
         'and industrial power quality monitors.</li>'
         '<li><strong>Class 0.2 (&plusmn;0.2% Ratio Error):</strong> Required for high-precision utility revenue billing, data center colocation tenant metering, '
         'and grid interconnection points.</li>'
         '<li><strong>5A vs. 1A Secondary Output:</strong> 5A is standard when the CT is mounted inside the same cabinet as the digital meter (cable runs $< 10$ meters). '
         'If the meter is located in a remote control room 50 to 200 meters away, a <strong>1A secondary output</strong> must be selected: because cable power loss '
         'is proportional to the square of the current ($P = I^2 R$), a 1A secondary reduces cable burden resistance losses by <strong>25 times ($25\times$)</strong>, '
         'preventing CT core saturation and maintaining high measurement accuracy.</li>'
         '</ul>')
    ],
    cta='Designing low-voltage main distribution boards (MDB), motor control centers (MCC), generator synchronization panels, or energy submetering systems requiring certified IEC 61869-2 busbar window-type current transformers (100A to 5000A, Class 0.5 & 0.2)? YOMIN manufactures precision MSQ/BH series measuring CTs.',
    body='''
<h2>The Essential Measurement Interface for Low-Voltage Power Distribution Switchgear</h2>
<p>Inside every commercial main distribution board (MDB), industrial motor control center (MCC), generator synchronizing panel, and data center power distribution unit (PDU), accurate current measurement is the foundational prerequisite for power management.</p>
<p>Digital power meters, energy monitors, power factor controllers, and protective relays cannot accept heavy raw currents ranging from hundreds to thousands of amperes directly into their delicate electronic terminals.</p>
<p>To measure these heavy currents safely, electrical switchboard panel builders rely on instrument current transformers. However, traditional wound-primary current transformers require cutting the main power busbar and bolting cumbersome terminal blocks, introducing electrical joint resistance and severe physical bulk.</p>
<p>The <strong>Low-Voltage Busbar Window-Type Current Transformer (Model MSQ / BH-0.66 Series)</strong> represents the universal, space-saving engineering standard: a compact toroidal measuring transformer featuring a rectangular window aperture that slips directly over the continuous copper busbar, delivering Class 0.5 and Class 0.2 precision with zero busbar cutting.</p>

<h2>Engineering Anatomy: Inside a Model MSQ Busbar Window Current Transformer</h2>
<ol>
  <li><strong>Continuous Toroidal Low-Loss Silicon Steel Core:</strong> Wound from high-permeability, cold-rolled grain-oriented silicon steel sheet ($CRGO$). Its gapless circular magnetic circuit ensures ultra-low excitation current, minimal phase angle error, and high accuracy across the entire load range (5% to 120% of rated current).</li>
  <li><strong>Precision Machine-Wound Secondary Copper Coil:</strong> Wound uniformly around the toroidal core using high-grade enameled electrolytic copper wire, minimizing leakage flux and maximizing secondary burden capacity (up to 30 VA).</li>
  <li><strong>Ultrasonically Welded Flame-Retardant ABS Casing:</strong> Impact-resistant polycarbonate/ABS housing certified to UL94 V-0 flame retardancy. Provides 3.0 kV dielectric isolation between the primary live busbar and secondary instrumentation circuits.</li>
  <li><strong>Integrated Insulated Busbar Clamping Screws:</strong> Heavy-duty plastic-headed clamping screws thread through the housing to lock the CT rigidly onto the copper busbar, preventing mechanical rattling and acoustic humming caused by 50Hz/60Hz electromagnetic vibration.</li>
  <li><strong>Sealable Transparent Secondary Terminal Cover:</strong> Transparent polycarbonate terminal cover with lead-sealing holes protects secondary brass screw terminals (S1, S2) against accidental contact and prevents unauthorized tampering with utility billing circuits.</li>
</ol>

<h2>Comparison: Window-Type Busbar CT vs. Wound-Primary CT vs. Split-Core Retrofit CT</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Wound-Primary Current Transformer</th>
      <th>Split-Core Retrofit Current Transformer</th>
      <th>YOMIN Busbar Window-Type CT (MSQ Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Busbar Installation &amp; Fabrication</strong></td>
      <td>Requires cutting busbar and bolting heavy primary terminals into the circuit.</td>
      <td>Clamps over existing cables; hinged split core with magnetic air gap.</td>
      <td><strong>Slips directly over continuous copper busbars; zero cutting or joint resistance.</strong></td>
    </tr>
    <tr>
      <td><strong>Measurement Accuracy &amp; Phase Error</strong></td>
      <td>Good; but high thermal stress on internal primary winding.</td>
      <td>Lower: Air gap between split core halves introduces ratio &amp; phase errors.</td>
      <td><strong>Superior Accuracy: Gapless toroidal core delivers certified Class 0.5 &amp; Class 0.2.</strong></td>
    </tr>
    <tr>
      <td><strong>Physical Size &amp; Switchgear Space Efficiency</strong></td>
      <td>Extremely bulky and heavy; consumes valuable switchboard depth.</td>
      <td>Bulky external hinges and spring-loaded locking clips.</td>
      <td><strong>Ultra-Compact Profile: Mounts flush against busbars, saving switchboard space.</strong></td>
    </tr>
    <tr>
      <td><strong>Vibration &amp; Acoustic Hum Under Load</strong></td>
      <td>Moderate; bolted joints can loosen under thermal cycling.</td>
      <td>Prone to acoustic buzzing if split core mating surfaces collect dust.</td>
      <td><strong>Silent Operation: Seamless resin-encapsulated core with busbar clamping screws.</strong></td>
    </tr>
    <tr>
      <td><strong>Primary Application in Power Networks</strong></td>
      <td>Low-current specialized applications (< 100A).</td>
      <td>Live-line retrofits where power cannot be de-energized during installation.</td>
      <td><strong>New OEM switchgear, MCCs, MDBs, and factory-built distribution panels (100A–5000A).</strong></td>
    </tr>
  </tbody>
</table>
'''
)

BCT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='switchgear-metering-what-is-a-busbar-current-transformer-fr',
    title="Tableaux de Distribution & Comptage : Qu'est-ce qu'un Transformateur de Courant pour Jeu de Barres (Busbar CT) ?",
    breadcrumb='Transformateurs de Mesure &amp; Comptage Électrique',
    read='10 min de lecture',
    alt='Transformateur de courant basse tension de mesure à passage de barre (Série MSQ, Classe 0.5) monté directement sur barre de cuivre verticale dans un TGBT',
    desc=('Tableaux généraux basse tension (TGBT), centres de contrôle de moteurs (MCC) et comptage sur jeu de barres : Qu\'est-ce qu\'un transformateur de courant pour jeu de barres (busbar CT) ? '
          'Fenêtres rectangulaires de passage (30x10 à 120x10mm), primaires 100A–5000A, sorties secondaires 5A/1A, classes de précision 0.5/0.2 et norme CEI 61869-2.'),
    model='Série MSQ / BH-0.66 : Transformateurs de Courant de Mesure BT à Passage de Barre (0,66kV, 100A à 5000A, Classe 0.5 / Classe 0.2, CEI 61869-2)',
    category='Transformateurs de Mesure & Comptage Électrique / Transformateurs à Passage de Barre',
    kw='transformateur de courant jeu de barres &middot; busbar ct &middot; transformateur torique fenetre &middot; tc msq &middot; transformateur de mesure 5a &middot; tc bh 0.66',
    specs=[
        ('Tension Assignée d\'Isolement de Service', 'Basse tension industrielle : $U_m = 0,72$ kV / 0,66 kV AC (tension d\'épreuve diélectrique : 3,0 kV pendant 1 min à 50/60 Hz)'),
        ('Plage de Courant Primaire Assigné ($I_{pn}$)', 'Calibres primaires normalisés : 100A, 150A, 200A, 250A, 300A, 400A, 500A, 600A, 800A, 1000A, 1200A jusqu\'à 5000A'),
        ('Courant Secondaire Assigné de Sortie ($I_{sn}$)', 'Standard pour appareillage de mesure : 5 A (liaison directe) ou 1 A (pour liaisons déportées sur de longues distances)'),
        ('Classes de Précision de Mesure Disponibles', 'Classe 0.5 (sous-comptage industriel et gestion d\'énergie) et Classe 0.2 / 0.2S (comptage transactionnel de haute précision)'),
        ('Dimensions des Fenêtres Rectangulaires', 'Adaptées aux jeux de barres normalisés : 30x10mm (MSQ-30), 40x10mm (MSQ-40), 60x10mm (MSQ-60) jusqu\'à 120x10mm (MSQ-120)'),
        ('Puissance de Précision Secondaire Assignée', 'Puissances de précision disponibles : 2,5 VA, 5 VA, 10 VA, 15 VA jusqu\'à 30 VA (pour centrales de mesure numériques)'),
        ('Matériau du Boîtier et Tenue au Feu', 'Boîtier en ABS / polycarbonate thermoplastique auto-extinguible soudé par ultrasons (classe d\'inflammabilité UL94 V-0)'),
        ('Accessoires de Fixation et Sécurité', 'Vis de serrage isolées pour verrouillage sur barre de cuivre, équerres métalliques de fond d\'armoire et capot plombable')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transformateur de Courant pour Jeu de Barres et comment fonctionne son principe à fenêtre traversante ?',
         'Un Transformateur de Courant pour Jeu de Barres—couramment appelé TC de mesure à passage de barre, tore de mesure ou transformateur type fenêtre—est '
         'un transformateur de mesure basse tension conçu avec une ouverture centrale rectangulaire ou circulaire permettant de l\'enfiler '
         'directement sur une barre de cuivre sans aucune découpe ni perçage du conducteur principal. '
         'Dans les Tableaux Généraux Basse Tension (TGBT) et armoires de distribution : '
         '<ul>'
         '<li><strong>Le Principe du Primaire Passant :</strong> La barre de cuivre fait office d\'enroulement primaire unique ($N_1 = 1$). '
         'Le passage du courant de charge ($I_p$) génère un flux magnétique dans le circuit magnétique torique en acier au silicium. '
         'L\'enroulement secondaire ($N_2$) délivre un courant proportionnel réduit ($I_s = 5$A ou 1A) directement exploitable par les centrales de mesure.</li>'
         '<li><strong>Montage Rapide et Fiable :</strong> Le tableautier glisse simplement le TC Série MSQ le long de la barre, serre les vis de blocage '
         'en plastique pour éviter toute vibration, et raccorde les bornes secondaires (S1, S2) aux instruments de mesure du panneau.</li>'
         '</ul>'),
        ('Comment choisir la taille de fenêtre appropriée pour les barres de cuivre ?',
         'Le choix de la fenêtre dépend de la section de barre requise par l\'intensité nominale : '
         '<ul>'
         '<li><strong>MSQ-30 (Fenêtre 30x10mm) :</strong> Idéal pour les départs divisionnaires de 100A à 300A (barre de 30x10mm ou câble de 30mm).</li>'
         '<li><strong>MSQ-40 (Fenêtre 40x10mm) :</strong> Utilisé pour les disjoncteurs de 300A à 600A avec barre de 40x10mm.</li>'
         '<li><strong>MSQ-60 (Fenêtre 60x10mm ou double 50x10mm) :</strong> Le modèle standard pour les arrivées TGBT de 600A à 1200A.</li>'
         '<li><strong>MSQ-100 / MSQ-120 (Fenêtre 100x10 à 120x10mm) :</strong> Conçu pour les fortes puissances de 1200A à 5000A à barres multiples en parallèle.</li>'
         '</ul>'),
        ('Quelle est la différence entre la Classe 0.5 et la Classe 0.2, et quand choisir une sortie 1A plutôt que 5A ?',
         'La classe définit l\'erreur maximale de mesure selon la norme CEI 61869-2 : '
         '<ul>'
         '<li><strong>Classe 0.5 (&plusmn;0,5% d\'erreur) :</strong> Le standard universel pour le sous-comptage en usine et les centrales de mesure.</li>'
         '<li><strong>Classe 0.2 (&plusmn;0,2% d\'erreur) :</strong> Requis pour la facturation d\'énergie de haute précision et les data centers.</li>'
         '<li><strong>Sortie 5A vs. 1A :</strong> La sortie 5A est standard quand le compteur est sur la porte de la même armoire ($< 10$ mètres). '
         'Si le compteur est situé à 50 ou 100 mètres dans un local distant, la <strong>sortie 1A est obligatoire</strong> : les pertes par effet Joule '
         'étant proportionnelles au carré du courant ($P = I^2 R$), le secondaire 1A <strong>divise les pertes en ligne par 25 ($25\times$)</strong>, '
         'évitant la saturation du transformateur et garantissant une mesure d\'une parfaite exactitude.</li>'
         '</ul>')
    ],
    cta='Vous fabriquez des Tableaux Généraux Basse Tension (TGBT), des centres de contrôle moteurs (MCC) ou des armoires de comptage d\'énergie nécessitant des transformateurs de courant à passage de barre certifiés CEI 61869-2 (100A à 5000A, Classe 0.5 & 0.2) ? YOMIN fabrique des TC série MSQ de haute précision.',
    body='''
<h2>L\'Interface de Mesure Essentielle pour les Tableaux Électriques Basse Tension</h2>
<p>Dans chaque Tableau Général Basse Tension (TGBT), centre de contrôle de moteurs (MCC), armoire de synchronisation de groupe électrogène et unité de distribution d\'énergie de data center, la mesure précise du courant est le socle de toute la gestion énergétique.</p>
<p>Les centrales de mesure numériques, les wattmètres, les régulateurs d\'énergie réactive et les relais de protection ne peuvent recevoir directement des intensités colossales de centaines ou de milliers d\'ampères sur leurs bornes électroniques.</p>
<p>Pour mesurer ces courants en toute sécurité, les tableautiers utilisent des transformateurs de courant de mesure. Cependant, les anciens transformateurs à primaire bobiné exigeaient de sectionner la barre de cuivre principale et d\'ajouter de lourds raccordements boulonnés, sources d\'échauffement et de pertes de place.</p>
<p>Le <strong>Transformateur de Courant Basse Tension à Passage de Barre (Série MSQ / BH-0.66)</strong> s\'impose comme la référence compacte universelle : un transformateur torique doté d\'une fenêtre rectangulaire qui s\'enfile directement sur la barre de cuivre continue, offrant une précision de Classe 0.5 et Classe 0.2 sans aucune découpe de barre.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série MSQ</h2>
<ol>
  <li><strong>Circuit Magnétique Torique sans Entrefer en Acier au Silicium :</strong> Tôles feuilletées à grains orientés ($CRGO$) assurant un courant magnétisant minime et une précision exemplaire sur toute la plage de charge (de 5% à 120% de $I_n$).</li>
  <li><strong>Bobinage Secondaire Automatisé en Cuivre Électrolytique :</strong> Répartition rigoureusement uniforme du fil de cuivre assurant une puissance de précision élevée (jusqu\'à 30 VA) sans saturation.</li>
  <li><strong>Boîtier en ABS Auto-Extinguible Soudé par Ultrasons :</strong> Enveloppe rigide conforme à la norme d\'inflammabilité UL94 V-0 assurant un isolement diélectrique de 3,0 kV face au jeu de barres.</li>
  <li><strong>Vis de Blocage Isolées Intégrées :</strong> Vis en thermoplastique renforcé venant serrer le transformateur sur la barre de cuivre pour supprimer toute vibration sous 50Hz/60Hz.</li>
  <li><strong>Capot Secondaire Transparent Plombable :</strong> Protège les bornes à vis secondaires (S1, S2) contre les contacts accidentels et prévient toute fraude sur les circuits de comptage d\'énergie.</li>
</ol>
'''
)

BCT_ES = dict(
    lang='es',
    dir='ltr',
    slug='switchgear-metering-what-is-a-busbar-current-transformer-es',
    title='Tableros de Distribución y Medición: ¿Qué es un Transformador de Corriente para Barras (Busbar CT)?',
    breadcrumb='Transformadores de Medida y Tableros Eléctricos',
    read='10 min de lectura',
    alt='Transformador de corriente de medida tipo ventana para barras en baja tensión (Serie MSQ, Clase 0.5) montado sobre barras de cobre verticales en tablero de distribución',
    desc=('Tableros generales de distribución (TGBT), centros de control de motores (CCM) y medición sobre barras colectoras: ¿Qué es un transformador de corriente para barras (busbar CT)? '
          'Ventanas rectangulares pasantes (30x10 a 120x10mm), corrientes primarias 100A–5000A, salidas secundarias 5A/1A, precisión Clase 0.5/0.2 y norma IEC 61869-2.'),
    model='Serie MSQ / BH-0.66: Transformadores de Corriente de Medida BT Tipo Ventana para Barras (0,66kV, 100A a 5000A, Clase 0.5 / Clase 0.2, IEC 61869-2)',
    category='Transformadores de Medida y Tableros Eléctricos / Transformadores Tipo Ventana para Barras',
    kw='transformador de corriente para barras &middot; busbar ct &middot; transformador tipo ventana &middot; tc msq &middot; transformador de medida 5a &middot; tc bh 0.66',
    specs=[
        ('Clase de Tensión Asignada de Aislamiento', 'Baja tensión industrial: $U_m = 0,72$ kV / 0,66 kV AC (tensión de prueba dieléctrica: 3,0 kV durante 1 min a 50/60 Hz)'),
        ('Rango de Corriente Primaria Nominal ($I_{pn}$)', 'Calibres primarios normalizados: 100A, 150A, 200A, 250A, 300A, 400A, 500A, 600A, 800A, 1000A, 1200A hasta 5000A'),
        ('Corriente Secundaria Nominal de Salida ($I_{sn}$)', 'Salidas estandarizadas para medición: 5 A (para tableros locales) o 1 A (para tiradas largas hacia salas remotas)'),
        ('Clases de Precisión Metrológica Disponibles', 'Clase 0.5 (estándar para submedición industrial y control) y Clase 0.2 / 0.2S (alta precisión para facturación y data centers)'),
        ('Dimensiones de Ventana Rectangular Pasante', 'Adaptadas a barras de cobre estándar: 30x10mm (MSQ-30), 40x10mm (MSQ-40), 60x10mm (MSQ-60) hasta 120x10mm (MSQ-120)'),
        ('Capacidad y Carga Nominal Secundaria (Burden)', 'Cargas nominales disponibles: 2,5 VA, 5 VA, 10 VA, 15 VA hasta 30 VA (compatibles con multímetros digitales de panel)'),
        ('Material Constructivo y Autoextinguibilidad', 'Carcasa de ABS / policarbonato autoextinguible sellada por ultrasonido (clasificación al fuego UL94 V-0)'),
        ('Accesorios de Fijación y Seguridad en Bornes', 'Tornillos plásticos aislados para fijación directa a barra de cobre, soportes metálicos de riel DIN y tapa precintable')
    ],
    faqs=[
        ('¿Qué es un Transformador de Corriente para Barras y cómo opera su diseño tipo ventana?',
         'Un Transformador de Corriente para Barras—conocido comúnmente como transformador de corriente tipo ventana, TC toroidal de paso o TC pasante para barra—es '
         'un transformador de medida en baja tensión diseñado con un orificio central rectangular o circular que permite deslizarlo '
         'directamente sobre una barra de cobre o aluminio continua sin necesidad de cortar, taladrar o empernar el conductor principal. '
         'En tableros generales de distribución (TGBT) y centros de control de motores (CCM): '
         '<ul>'
         '<li><strong>Principio de Primario Pasante:</strong> La barra de cobre actúa como primario de una sola espira ($N_1 = 1$). '
         'El paso de la corriente de carga ($I_p$) induce un flujo magnético en el núcleo toroidal de acero al silicio de alta permeabilidad. '
         'El devanado secundario ($N_2$) entrega una corriente proporcionalmente reducida ($I_s = 5$A o 1A) a los medidores de energía.</li>'
         '<li><strong>Facilidad de Armado de Tableros:</strong> El tablerista inserta el TC Serie MSQ en la pletina de cobre, ajusta los tornillos plásticos '
         'para inmovilizarlo sin vibraciones acústicas y conecta los bornes secundarios (S1, S2) al analizador de redes en minutos.</li>'
         '</ul>'),
        ('¿Cómo seleccionar el tamaño de ventana adecuado para las barras de cobre?',
         'El tamaño de la ventana se define según la sección de la pletina de cobre utilizada: '
         '<ul>'
         '<li><strong>MSQ-30 (Ventana 30x10mm o &phi;30mm redondo):</strong> Para interruptores de 100A a 300A con barra de 30x10mm o cables de hasta 30mm.</li>'
         '<li><strong>MSQ-40 (Ventana 40x10mm):</strong> Utilizado para circuitos de 300A a 600A con barra de 40x10mm.</li>'
         '<li><strong>MSQ-60 (Ventana 60x10mm o doble barra 50x10mm):</strong> El modelo más popular para acometidas principales de 600A a 1200A.</li>'
         '<li><strong>MSQ-100 / MSQ-120 (Ventana 100x10 a 120x10mm):</strong> Diseñado para grandes acometidas de 1200A a 5000A con barras paralelas.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre Clase 0.5 y Clase 0.2, y cuándo usar secundaria de 1A en vez de 5A?',
         'La clase define el error porcentual de medición según la norma IEC 61869-2: '
         '<ul>'
         '<li><strong>Clase 0.5 (&plusmn;0,5% de error):</strong> El estándar de la industria para submedición de fábricas y gestión energética.</li>'
         '<li><strong>Clase 0.2 (&plusmn;0,2% de error):</strong> Obligatorio para facturación de energía fiscalizada y centros de datos.</li>'
         '<li><strong>Salida 5A vs. 1A:</strong> La salida de 5A es estándar cuando el medidor está en la misma puerta del tablero ($< 10$ metros). '
         'Si el medidor se encuentra en una sala de control a 50 o 100 metros, la <strong>salida de 1A es obligatoria</strong> : al ser las pérdidas proporcionales '
         'al cuadrado de la corriente ($P = I^2 R$), el secundario de 1A <strong>reduce las pérdidas por resistencia del cable en 25 veces ($25\times$)</strong>, '
         'evitando la saturación del núcleo y manteniendo una exactitud perfecta.</li>'
         '</ul>')
    ],
    cta='¿Fabrica tableros generales de distribución (TGBT), centros de control de motores (CCM) o sistemas de submedición eléctrica que requieren transformadores de corriente tipo ventana para barras certificados IEC 61869-2 (100A a 5000A, Clase 0.5 y 0.2)? YOMIN suministra TCs serie MSQ de máxima precisión.',
    body='''
<h2>La Interfaz de Medición Imprescindible para Tableros Eléctricos de Baja Tensión</h2>
<p>En tableros generales de distribución (TGBT), centros de control de motores (CCM), cuadros de transferencia y centros de datos, la medición exacta de la corriente es el pilar de toda la gestión de energía.</p>
<p>Los medidores multifunción digitales, analizadores de redes, controladores de factor de potencia y relés de protección no pueden recibir directamente intensidades de cientos o miles de amperios en sus terminales electrónicos.</p>
<p>Para medir estas corrientes con seguridad, los fabricantes de tableros utilizan transformadores de corriente. Sin embargo, los antiguos transformadores de primario bobinado exigían cortar las barras colectoras de cobre e incorporar pesadas uniones empernadas que generaban puntos calientes y robaban espacio valioso.</p>
<p>El <strong>Transformador de Corriente para Barras Tipo Ventana (Serie MSQ / BH-0.66)</strong> representa el estándar moderno y compacto: un transformador toroidal que se desliza directamente sobre la barra de cobre continua, alcanzando una precisión de Clase 0.5 y Clase 0.2 sin cortar ni perforar el conductor.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie MSQ</h2>
<ol>
  <li><strong>Núcleo Toroidal de Acero al Silicio de Grano Orientado ($CRGO$):</strong> Circuito magnético continuo sin entrehierro que minimiza las corrientes de magnetización y asegura una precisión lineal en todo el rango de carga (5% al 120% de $I_n$).</li>
  <li><strong>Devanado Secundario de Cobre Electrolítico de Alta Pureza:</strong> Bobinado con distribución geométrica uniforme que entrega altas potencias de precisión (hasta 30 VA) sin saturación.</li>
  <li><strong>Carcasa de ABS Autoextinguible Sellada por Ultrasonido:</strong> Envolvente resistente al impacto con certificación de autoextinguibilidad UL94 V-0 y aislamiento dieléctrico de 3,0 kV.</li>
  <li><strong>Tornillos Plásticos Aislados de Fijación a Barra:</strong> Presionan firmemente el transformador contra la pletina de cobre para suprimir zumbidos y vibraciones electromagnéticas.</li>
  <li><strong>Tapa de Bornes Secundaria Transparente y Precintable:</strong> Protege los terminales S1 y S2 contra contactos involuntarios e impide manipulaciones no autorizadas en circuitos de facturación.</li>
</ol>
'''
)

BCT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='switchgear-metering-what-is-a-busbar-current-transformer-ar',
    title='لوحات التوزيع وقياس الطاقة: ما هو محول التيار لقضبان التوزيع (Busbar Current Transformer)؟',
    breadcrumb='محولات التيار وقياس الطاقة باللوحات',
    read='10 دقائق قراءة',
    alt='محول تيار قياس منخفض الجهد نوع نافذة لقضبان التوزيع (موديل MSQ، فئة دقة 0.5) مركب مباشرة فوق قضبان النحاس الرأسية داخل لوحة توزيع رئيسية',
    desc=('لوحات التوزيع الكهربائية الرئيسية (MDB)، ومراكز التحكم بالمحركات (MCC)، وقياس تيارات قضبان التوزيع النحاسية: ما هو محول التيار لقضبان التوزيع (Busbar CT)؟ '
          'فتحات نافذة مستطيلة (30x10 إلى 120x10 مم)، وتيارات ابتدائية 100A–5000A، ومخرجات ثانوية 5A/1A، وفئات دقة 0.5 و 0.2 ومعايير IEC 61869-2.'),
    model='سلسلة MSQ / BH-0.66: محولات تيار القياس منخفضة الجهد نوع نافذة لقضبان التوزيع (0.66kV، من 100A إلى 5000A، فئة دقة 0.5 و 0.2، معتمدة IEC 61869-2)',
    category='محولات التيار وقياس الطاقة باللوحات / محولات التيار نوع نافذة للقضبان',
    kw='محول تيار قضبان &middot; busbar ct &middot; محول تيار نوع نافذة &middot; محول تيار msq &middot; محول قياس 5 امبير &middot; محول تيار bh 0.66',
    specs=[
        ('فئة جهد العزل والتشغيل الاسمي للشبكة', 'جهد عزل منخفض معتمد: $U_m = 0.72$ kV / 0.66 kV AC (جهد اختبار العزل الديزلكتريكي: 3.0 kV لمدة دقيقة واحدة عند 50/60 هرتز)'),
        ('نطاق قياس التيار الابتدائي الاسمي ($I_{pn}$)', 'سعات تيار ابتدائي معيارية: 100A و 150A و 200A و 300A و 400A و 600A و 800A و 1000A و 1200A وحتى 5000A'),
        ('التيار الثانوي الاسمي لأجهزة القياس ($I_{sn}$)', 'مخرجات معيارية لأجهزة القياس: 5 أمبير (قياسي للوحات المحلية) أو 1 أمبير (للمسافات الطويلة نحو غرف التحكم)'),
        ('فئات دقة القياس المترولوجية المتاحة', 'فئة 0.5 (قياسية لحساب الطاقة الداخلي بالمنشآت) وفئة 0.2 / 0.2S (فائقة الدقة لفوترة الطاقة ومراكز البيانات)'),
        ('أبعاد فتحات النوافذ المستطيلة المتاحة', 'مصممة لتناسب مقاطع القضبان النحاسية: 30x10 مم (MSQ-30) و 40x10 مم (MSQ-40) و 60x10 مم (MSQ-60) وحتى 120x10 مم (MSQ-120)'),
        ('قدرة الحمل الثانوي الاسمي (Burden)', 'قدرات حمل معيارية: 2.5 VA و 5 VA و 10 VA و 15 VA وحتى 30 VA (متوافقة تماماً مع أجهزة القياس الرقمية الحديثة)'),
        ('مادة تصنيع الهيكل ومقاومة الاشتعال', 'غلاف من البوليكربونات / ABS المقاوم للصدمات والملحوم بالموجات فوق الصوتية (تصنيف مقاومة اللهب UL94 V-0)'),
        ('ملحقات التثبيت وحماية أطراف التوصيل', 'مسامير زنق بلاستيكية معزولة للتثبيت المحكم على قضيب النحاس، وقواعد تثبيت معدنية لقضيب DIN وغطاء شفاف قابل للرصاص')
    ],
    faqs=[
        ('ما هو محول التيار لقضبان التوزيع (Busbar CT) وكيف يعمل تصميمه بنظام النافذة المفتوحة؟',
         'محول التيار لقضبان التوزيع—والمعروف هندسياً باسم محول التيار نوع نافذة أو محول تيار الباص بار أو محول القياس الحلقي—هو '
         'محول قياس كهربائي للجهد المنخفض صُمم بنافذة وسطية مستطيلة أو دائرية مفرغة تسمح بإدخاله وانزلاقه '
         'مباشرة فوق قضيب التوزيع النحاسي أو الألومنيوم دون الحاجة لقطع القضيب أو ثقبه أو فكه. '
         'وفي لوحات التوزيع الرئيسية ومراكز التحكم بالمحركات (MCC): '
         '<ul>'
         '<li><strong>مبدأ الملف الابتدائي العابر:</strong> يمثل قضيب النحاس ذاته الملف الابتدائي أحادي اللفة ($N_1 = 1$). '
         'ومع مرور تيار الحمل ($I_p$)، يتولد فيض مغناطيسي داخل القلب الحديدي الحلقي المصنوع من صلب السيليكون عالي النفاذية. '
         'ويقوم الملف الثانوي ($N_2$) بتوليد تيار مخفض متناسب بدقة ($I_s = 5$A أو 1A) يغذي عدادات الطاقة الرقمية مباشرة.</li>'
         '<li><strong>سهولة وسرعة التجميع باللوحات:</strong> يقوم مصنع اللوحات بتمرير محول MSQ فوق قضيب النحاس، وشده بمسامير الزنق البلاستيكية '
         'لمنع الاهتزاز، ثم توصيل أطراف الثانوي (S1, S2) بجهاز القياس الرقمي في ثوانٍ معدودة.</li>'
         '</ul>'),
        ('كيف يختار مصممو اللوحات مقاس فتحة النافذة المناسب لقضبان النحاس؟',
         'يتم تحديد مقاس فتحة محول التيار طبقاً لمقاس قطاع قضيب النحاس المستخدم: '
         '<ul>'
         '<li><strong>طراز MSQ-30 (نافذة 30x10 مم):</strong> مثالي لقواطع التوزيع من 100A إلى 300A مع قضيب نحاسي مفرد مقاس 30x10 مم.</li>'
         '<li><strong>طراز MSQ-40 (نافذة 40x10 مم):</strong> يُستخدم للقواطع من 300A إلى 600A مع قضيب مقاس 40x10 مم.</li>'
         '<li><strong>طراز MSQ-60 (نافذة 60x10 مم أو قضيبين 50x10 مم):</strong> المقاس الأكثر استخداماً في اللوحات الرئيسية لقواطع 600A إلى 1200A.</li>'
         '<li><strong>طراز MSQ-100 / MSQ-120 (نافذة 100x10 إلى 120x10 مم):</strong> مخصص للأحمال الضخمة من 1200A إلى 5000A ذات القضبان المزدوجة المتوازية.</li>'
         '</ul>'),
        ('ما هو الفرق بين فئة الدقة 0.5 وفئة 0.2، ومتى يجب اختيار مخرج 1 أمبير بدلاً من 5 أمبير؟',
         'تحدد فئة الدقة نسبة الخطأ المسموح بها في القياس طبقاً للمواصفة القياسية IEC 61869-2: '
         '<ul>'
         '<li><strong>فئة 0.5 (نسبة خطأ &plusmn;0.5%):</strong> المعيار العالمي المعتمد لحساب الطاقة الداخلي بالمصانع والمنشآت التجارية.</li>'
         '<li><strong>فئة 0.2 (نسبة خطأ &plusmn;0.2%):</strong> إلزامية لفوترة الطاقة المالية الدقيقة، ونقاط الربط مع شبكة الكهرباء، ومراكز البيانات.</li>'
         '<li><strong>مخرج 5 أمبير مقابل 1 أمبير:</strong> يعتبر مخرج 5A قياسياً إذا كان جهاز القياس مركباً على باب نفس اللوحة الكهربائية ($< 10$ أمتار). '
         'أما إذا كان العداد في غرفة تحكم بعيدة على مسافة 50 إلى 150 متراً، فإن <strong>اختيار مخرج 1 أمبير إلزامي</strong> : نظراً لأن الفقد في كابل القياس '
         'يتناسب طردياً مع مربع التيار ($P = I^2 R$)، فإن مخرج 1A <strong>يخفض الفقد في الكابلات بمقدار 25 ضعفاً ($25\times$)</strong>، '
         'مانعاً تشبع المحول ومحافظاً على أعلى مستويات دقة القياس.</li>'
         '</ul>')
    ],
    cta='هل تعمل على تصنيع لوحات التوزيع الكهربائية الرئيسية (MDB)، أو مراكز التحكم بالمحركات (MCC)، أو أنظمة قياس الطاقة التي تتطلب محولات تيار نوع نافذة لقضبان التوزيع معتمدة IEC 61869-2 (من 100A إلى 5000A، فئة دقة 0.5 و 0.2)؟ تصنع يمين (YOMIN) محولات MSQ بأعلى معايير الدقة.',
    body='''
<h2>واجهة القياس الكهربائي الحيوية لقضبان التوزيع باللوحات منخفضة الجهد</h2>
<p>داخل كل لوحة توزيع رئيسية (MDB)، ومركز تحكم بالمحركات (MCC)، ولوحة مزامنة للمولدات الكهربائية، ووحدة توزيع طاقة بمراكز البيانات، يعتبر القياس الدقيق للتيار الكهربائي الأساس الجوهري لإدارة الطاقة.</p>
<p>ولا تستطيع عدادات الطاقة الرقمية وأجهزة قياس معامل القدرة ومرحلات الوقاية استقبال تيارات الأحمال الضخمة التي تصل إلى مئات أو آلاف الأمبيرات مباشرة في أطرافها الإلكترونية الدقيقة.</p>
<p>ولقياس هذه التيارات بأمان، يعتمد مصنعو اللوحات على محولات التيار. غير أن المحولات القديمة ذات الملف الابتدائي الملفوف كانت تتطلب قطع قضيب النحاس وإضافة وصلات ربط ضخمة بالمسامير تسبب نقاط سخونة وتستهلك مساحة كبيرة داخل اللوحة.</p>
<p>يمثل <strong>محول التيار منخفض الجهد لقضبان التوزيع نوع نافذة (سلسلة MSQ / BH-0.66)</strong> المعيار الهندسي القياسي الأكثر توفيراً للمساحة: محول حلقي مصمت بنافذة مستطيلة يمر عبرها قضيب النحاس المستمر دون أدنى حاجة لقطع القضيب، محققاً دقة متناهية من فئة 0.5 وفئة 0.2.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة محولات MSQ المدمجة</h2>
<ol>
  <li><strong>قلب حلقي متصل من صلب السيليكون عالي النفاذية ($CRGO$):</strong> دائرة مغناطيسية تامة دون أي فجوات هوائية تضمن تيار مغنطة منخفضاً للغاية ودقة متناهية عبر كامل نطاق الحمل (من 5% إلى 120% من التيار الاسمي).</li>
  <li><strong>ملف ثانوي نحاسي كهرلي دقيق اللف:</strong> توزيع هندسي متماثل لأسلاك النحاس المعزولة يضمن قدرة حمل ثانوي عالية (تصل إلى 30 VA) دون أي تشبع مغناطيسي.</li>
  <li><strong>غلاف خارجي من مادة ABS المقاومة للهب والمغلقة بالموجات فوق الصوتية:</strong> هيكل متين مطابق للمعيار UL94 V-0 يوفر عزلاً ديزلكتريكياً بجهد 3.0 kV بين قضيب النحاس ودوائر القياس.</li>
  <li><strong>مسامير تثبيت معزولة مدمجة:</strong> مسامير زنق بلاستيكية قوية تضغط المحول على القضيب النحاسي لتمنع الاهتزاز والطنين الميكانيكي تحت تردد 50/60 هرتز.</li>
  <li><strong>غطاء ثانوي شفاف قابل للترصيص:</strong> يحمي أطراف التوصيل الثانوية S1 و S2 من التلامس العرضي ويمنع التلاعب غير المصرح به بدوائر حساب الطاقة.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1014 = [
    SF6_EN, SF6_FR, SF6_ES, SF6_AR,
    BCT_EN, BCT_FR, BCT_ES, BCT_AR
]
