# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-17:
1. PLC (Power Line Carrier) Smart Energy Meters for Advanced Metering Infrastructure (EN, FR, ES, AR)
2. AC Current Transducers with 4-20mA DC Analog Output for Industrial Automation & PLCs (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. PLC SMART ENERGY METER (EN, FR, ES, AR)
# ==============================================================================

PLC_EN = dict(
    lang='en',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-plc-smart-energy-meter',
    title='Smart Metering & AMI: What Is a PLC Smart Energy Meter?',
    breadcrumb='Smart Energy Meters &amp; AMI Telemetry',
    read='10 min read',
    alt='Three-phase digital PLC Smart Electricity Meter (Model DTS series) installed with sealed power cables and active Power Line Carrier communication LEDs',
    desc=('Advanced Metering Infrastructure (AMI/AMR), multi-tenant apartment towers, and power grid automation: What is a PLC smart energy meter? '
          'How broadband power line carrier (HPLC) OFDM modulation (2-12 MHz), transmission over existing 220V/380V cables, zero cellular SIM fees, and DLMS/COSEM protocols eliminate radio dead zones.'),
    model='Model DTS / DDS Series 3-Phase & Single-Phase Smart Electricity Meters with Broadband PLC / HPLC Plug-and-Play Modules (Class 1.0 / 0.5S, OFDM 2-12 MHz, DLMS/COSEM Compliant)',
    category='Smart Energy Meters & AMI Telemetry / Power Line Carrier Meters',
    kw='what is a plc energy meter &middot; plc smart energy meter &middot; power line carrier energy meter &middot; hplc broadband plc smart meter &middot; plc amr meter &middot; dts plc meter',
    specs=[
        ('Communication Technology & Carrier Frequency', 'Broadband High-Speed Power Line Carrier (HPLC) utilizing Orthogonal Frequency Division Multiplexing (OFDM, 2 MHz to 12 MHz)'),
        ('Telemetry Data Transmission Media', 'Direct modulation onto existing low-voltage AC power distribution cables (220V / 380V, 50/60 Hz; zero dedicated communication cabling)'),
        ('Metering Accuracy Class Standards', 'Class 1.0 (IEC 62053-21) active energy, Class 2.0 (IEC 62053-23) reactive energy (Optional Class 0.5S high-precision transformer operated)'),
        ('Carrier Data Transmission Rate & Latency', 'High-throughput PHY data rates up to 10 Mbps (effective application layer throughput &gt; 100 kbps; sub-second query latency)'),
        ('Application Layer Protocol & Interoperability', 'Standardized open utility protocols: DLMS/COSEM (IEC 62056) and PRIME / G3-PLC international smart grid standards'),
        ('Operating Voltage & Current Ratings', 'Rated nominal voltage: 3&times;230/400V AC (3-Phase 4-Wire); Direct-connected current ratings: 5(60)A, 10(100)A; CT-operated: 1.5(6)A'),
        ('Anti-Tamper & Revenue Protection Security', 'Comprehensive multi-event detection: magnetic interference detection, neutral line missing bypass detection, terminal cover open alarm'),
        ('Power Consumption & Environmental Tolerance', 'Internal voltage circuit burden: &le; 1.5W / 6VA; Operating temperature range: $-40^\circ\text{C}$ to $+70^\circ\text{C}$; IP54 weatherproof enclosure')
    ],
    faqs=[
        ('What is a PLC Smart Energy Meter and how does Power Line Carrier communication work?',
         'A PLC Smart Energy Meter—frequently designated as a Power Line Carrier electricity meter, HPLC smart meter, or CPL energy meter—is '
         'a digital electronic revenue meter equipped with an integrated or modular power line carrier transceiver that transmits metering data '
         'directly over the existing low-voltage AC power cables supplying the building. '
         'In modern Advanced Metering Infrastructure (AMI) and automated meter reading (AMR / ASKUE) networks: '
         '<ul>'
         '<li><strong>Physical Signal Superimposition:</strong> The meter converts digital telemetry bytes (active/reactive kWh, voltage, current, load curves) '
         'into high-frequency carrier wave packets using advanced Orthogonal Frequency Division Multiplexing (OFDM) modulation. '
         'These micro-voltage signals are superimposed directly onto the fundamental 50Hz/60Hz AC sine wave traveling through the building\'s copper conductors.</li>'
         '<li><strong>Zero-Cabling Gateway Aggregation:</strong> At the local distribution transformer substation, a Data Concentrator Unit (DCU) equipped with '
         'a matching PLC receiver captures and demodulates the carrier signals from all connected meters, aggregating billing records and forwarding them '
         'via fiber optic or 4G backhaul to the utility central head-end software (HES).</li>'
         '</ul>'),
        ('Why do utilities deploy PLC Smart Meters instead of Cellular (4G/NB-IoT) or Wireless RF meters in urban areas?',
         'While wireless smart meters function well in open rural landscapes, they encounter severe physical and financial roadblocks in dense urban centers: '
         '<ul>'
         '<li><strong>100% Penetration in RF Blind Spots:</strong> In multi-story apartment towers, high-rise condominiums, shopping malls, and underground basement electrical rooms, '
         'thick reinforced concrete walls, steel elevator shafts, and subterranean earth completely block cellular (4G/LTE, NB-IoT) and wireless RF (LoRa, Zigbee) signals. '
         'Because every building and apartment is physically connected to the electrical power grid, PLC signals flow unhindered through existing cables directly to the basement meters.</li>'
         '<li><strong>Zero Cellular SIM Data Fees &amp; Permanent Ownership:</strong> Cellular meters require an active telecom SIM card with monthly carrier subscription fees '
         'multiplied across hundreds of thousands of utility meters, alongside risks of telecom 2G/3G network shutdowns. '
         'PLC communication runs over utility-owned physical wires with <strong>zero recurring carrier data bills</strong> and permanent operational lifespan.</li>'
         '</ul>'),
        ('What is the difference between legacy Narrowband PLC and modern Broadband HPLC?',
         'Early generation narrowband PLC (operating below 500 kHz, such as legacy FSK or BPSK) suffered from slow transmission speeds (< 2.4 kbps), '
         'high sensitivity to electrical grid noise (from LED power supplies, inverter air conditioners, and arc welders), and frequent packet loss. '
         '<strong>Broadband High-Speed PLC (HPLC)</strong> operates in the high-frequency 2 MHz to 12 MHz spectrum using multi-carrier OFDM with dynamic subcarrier channel estimation. '
         'It automatically avoids noisy frequency bands, achieving transmission speeds exceeding 100 kbps to 10 Mbps with mesh automatic routing, '
         'enabling real-time second-level meter queries, power outage event push notifications, and remote firmware upgrades.')
    ],
    cta='Designing Advanced Metering Infrastructure (AMI/AMR), dense residential apartment submetering, or utility smart grid rollouts requiring certified DLMS/COSEM Broadband PLC / HPLC smart electricity meters (1-phase & 3-phase, zero cellular SIM fees, OFDM communication)? YOMIN manufactures precision DTS/DDS series PLC smart meters.',
    body='''
<h2>The Zero-Telecom Carrier Solution Powering Urban Smart Grid Telemetry</h2>
<p>Across modern municipal power distribution utilities, high-density residential apartment complexes, commercial shopping centers, and industrial facilities, deploying automated smart metering faces a major connectivity dilemma.</p>
<p>While wireless smart meters (utilizing 4G cellular, NB-IoT, or RF mesh) perform well in flat suburban neighborhoods, they suffer catastrophic communication dropouts in high-rise concrete buildings and underground electrical basement vaults where Faraday cage shielding blocks wireless radio waves.</p>
<p>Furthermore, deploying tens of thousands of cellular-connected meters locks utilities into millions of dollars in recurring monthly SIM card telecom contracts and exposes infrastructure to carrier cellular network sunsetting.</p>
<p>The <strong>Power Line Carrier (PLC) Smart Energy Meter (Model DTS / DDS Series)</strong> provides the definitive engineering answer: an intelligent electronic revenue meter that utilizes the physical electrical copper cables already wired into the building to transmit high-speed digital metering data directly to the substation Data Concentrator Unit (DCU) with zero radio blind spots and zero recurring carrier fees.</p>

<h2>Engineering Anatomy: Inside a Model DTS Broadband HPLC Smart Energy Meter</h2>
<ol>
  <li><strong>Broadband HPLC Modulator-Demodulator Engine:</strong> Features an integrated 32-bit high-performance DSP processing Orthogonal Frequency Division Multiplexing (OFDM) across 2 MHz to 12 MHz sub-carrier frequencies with adaptive channel modulation and Reed-Solomon forward error correction.</li>
  <li><strong>High-Precision Metering Analog Front-End (AFE):</strong> Dedicated metering chip sampling multi-channel phase voltage and current with Class 1.0 (or Class 0.5S) active energy accuracy and Class 2.0 reactive energy accuracy over a wide dynamic load range from 0.05% starting current to maximum nominal current.</li>
  <li><strong>High-Coupling Line Interface Transformer &amp; Surge Filter:</strong> High-dielectric isolation transformer and transient voltage suppressor (TVS) circuit that safely couples low-voltage high-frequency PLC communication signals onto the 230V/400V power lines while protecting internal microelectronics from 6kV lightning surges.</li>
  <li><strong>Backlit Multi-Parameter LCD Display:</strong> High-contrast industrial LCD screen displaying cumulative active kWh, reactive kvarh, instant active power (kW), line voltages, phase currents, power factor, tariff rate, and active PLC communication indicators.</li>
  <li><strong>Tamper Detection &amp; Revenue Protection Circuitry:</strong> Continuous hardware monitoring that detects and logs magnetic field tampering, meter cover opening, reverse power flow, and neutral line disconnection, transmitting immediate alarm alerts to utility head-end software.</li>
</ol>

<h2>Comparison: Broadband HPLC Smart Meter vs. Wireless LoRaWAN Smart Meter vs. Cellular 4G/NB-IoT Smart Meter</h2>
<table>
  <thead>
    <tr>
      <th>Operational Metric</th>
      <th>Cellular 4G / NB-IoT Smart Meter</th>
      <th>Wireless LoRaWAN Smart Meter</th>
      <th>YOMIN Broadband HPLC Smart Meter (DTS Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Transmission Physical Medium</strong></td>
      <td>Public cellular telecommunication towers.</td>
      <td>Unlicensed Sub-GHz wireless RF radio (868/915 MHz).</td>
      <td><strong>Existing 230V/400V low-voltage AC power cables; zero wireless RF.</strong></td>
    </tr>
    <tr>
      <td><strong>Penetration in Concrete &amp; Basements</strong></td>
      <td>Poor: Fails in underground electrical vaults and concrete basements.</td>
      <td>Moderate: Struggles through multiple floors of dense reinforced concrete.</td>
      <td><strong>100% Penetration: Follows physical copper power wires directly into meter rooms.</strong></td>
    </tr>
    <tr>
      <td><strong>Recurring Operational Telecom Costs</strong></td>
      <td>High: Requires monthly SIM card cellular data contracts for every meter.</td>
      <td>Zero: Private gateway ownership; but requires RF gateway site leases.</td>
      <td><strong>100% Free Communication: Utility owns the power wires; zero telecom carrier bills.</strong></td>
    </tr>
    <tr>
      <td><strong>Data Throughput &amp; Reading Latency</strong></td>
      <td>High throughput (Mbps); but dependent on cell tower congestion.</td>
      <td>Low throughput (&lt; 5 kbps); strict regional RF duty cycle limits.</td>
      <td><strong>High Speed: Broadband OFDM (&gt; 100 kbps to 10 Mbps); sub-second response times.</strong></td>
    </tr>
    <tr>
      <td><strong>Ideal Utility Deployment Scenario</strong></td>
      <td>Scattered rural single-phase consumer connections.</td>
      <td>Expansive industrial campuses, solar farms, and water/gas combo metering.</td>
      <td><strong>Dense urban apartment towers, commercial plazas, and municipal transformer grids.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

PLC_FR = dict(
    lang='fr',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-plc-smart-energy-meter-fr',
    title="Comptage Intelligent & Télérelève AMI : Qu'est-ce qu'un Compteur d'Énergie CPL (PLC) ?",
    breadcrumb='Comptage Intelligent &amp; Télérelève CPL',
    read='10 min de lecture',
    alt='Compteur électrique intelligent triphasé CPL (Série DTS) installé avec câbles d\'alimentation scellés et voyants de communication CPL actifs',
    desc=('Télérelève des compteurs (AMI/AMR), immeubles collectifs et modernisation des réseaux électriques : Qu\'est-ce qu\'un compteur communicant CPL (Courant Porteur en Ligne) ? '
          'Transmission haut débit HPLC par modulation OFDM (2 à 12 MHz) sur câbles 230V/400V existants, zéro abonnement télécom GSM et protocole DLMS/COSEM.'),
    model='Série DTS / DDS : Compteurs d\'Énergie Intelligents Triphasés et Monophasés à Courant Porteur en Ligne Haut Débit HPLC (Classe 1.0, OFDM 2-12 MHz, DLMS/COSEM)',
    category='Comptage Intelligent & Télérelève AMI / Compteurs à Courant Porteur en Ligne (CPL)',
    kw='compteur cpl &middot; compteur d energie cpl &middot; plc smart meter &middot; compteur communicant hplc &middot; telereleve cpl amr &middot; compteur dts cpl',
    specs=[
        ('Technologie de Communication & Fréquences', 'Courant Porteur en Ligne Haut Débit (CPL / HPLC) par multiplexage orthogonal OFDM (2 MHz à 12 MHz)'),
        ('Support Physique de Transmission des Données', 'Modulation directe sur le réseau électrique basse tension existant (230V / 400V, 50/60 Hz ; zéro câblage réseau dédié)'),
        ('Classe de Précision Météorologique Normalisée', 'Classe 1.0 (CEI 62053-21) énergie active, Classe 2.0 (CEI 62053-23) énergie réactive (Classe 0.5S sur TC disponible)'),
        ('Débit Binaire et Vitesse de Transmission', 'Débit physique PHY jusqu\'à 10 Mbit/s (débit applicatif utile &gt; 100 kbit/s ; temps de réponse sous la seconde)'),
        ('Protocole Applicatif et Interopérabilité', 'Standards ouverts internationaux pour réseaux intelligents : DLMS/COSEM (CEI 62056) et profils G3-PLC / PRIME'),
        ('Caractéristiques Électriques et Calibres', 'Tension nominale : 3&times;230/400V AC (Triphasé 4 Fils) ; Raccordement direct : 5(60)A, 10(100)A ; Raccordement sur TC : 1,5(6)A'),
        ('Protection Anti-Fraude et Détection Événements', 'Surveillance active permanente : détection de champ magnétique, rupture de neutre, ouverture du capot bornier avec alerte'),
        ('Consommation Propre et Robustesse Climat', 'Consommation circuit de tension : &le; 1,5W / 6VA ; Température de service : $-40^\circ\text{C}$ à $+70^\circ\text{C}$ ; Boîtier étanche IP54')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Compteur d\'Énergie CPL (PLC) et quel est son principe de fonctionnement ?',
         'Un Compteur d\'Énergie CPL (Courant Porteur en Ligne)—également désigné sous les appellations de compteur communicant PLC ou compteur HPLC—est '
         'un compteur d\'électricité électronique équipé d\'un modem CPL qui transmet les données de comptage et de télérelève '
         'directement sur les câbles électriques d\'alimentation du bâtiment. '
         'Dans une infrastructure de comptage avancé (AMI / AMR) : '
         '<ul>'
         '<li><strong>Superposition du Signal Numérique :</strong> Le compteur module les index d\'énergie (kWh actifs/réactifs, tensions, courbes de charge) '
         'en signaux haute fréquence par modulation OFDM. Ces signaux micro-volts se superposent à l\'onde sinusoïdale 50Hz/60Hz du réseau électrique.</li>'
         '<li><strong>Agrégation au Poste de Transformation :</strong> Au niveau du transformateur de distribution de quartier, '
         'un Concentrateur de Données (DCU) capte et démodule les signaux CPL de tous les compteurs raccordés sur le départ basse tension, '
         'puis transmet les relevés au serveur central de la régie d\'électricité via fibre optique ou liaison 4G sécurisée.</li>'
         '</ul>'),
        ('Pourquoi les gestionnaires de réseau privilégient-ils le CPL par rapport au GSM/4G en zone urbaine ?',
         'Dans les centres urbains et les grands ensembles collectifs, les compteurs cellulaires se heurtent à des contraintes sévères : '
         '<ul>'
         '<li><strong>Pénétration Parfaite dans les Sous-Sols :</strong> Dans les locaux compteurs situés en sous-sol ou dans les gaines techniques en béton armé, '
         'les ondes cellulaires (4G, NB-IoT) sont bloquées par effet de cage de Faraday. Le signal CPL, empruntant les câbles d\'alimentation en cuivre, '
         'pénètre à 100% sans aucun angle mort radio.</li>'
         '<li><strong>Zéro Coût d\'Abonnement SIM Télécom :</strong> Les compteurs cellulaires imposent un forfait data mensuel par compteur, '
         'représentant des millions d\'euros de coûts d\'exploitation récurrents. Le CPL fonctionne sur le réseau physique appartenant au distributeur, '
         'sans aucun abonnement télécom mensuel.</li>'
         '</ul>'),
        ('Quelle est la différence entre le CPL bande étroite classique et le CPL haut débit (HPLC) ?',
         'Les anciens systèmes CPL bande étroite (< 500 kHz) souffraient de débits très lents (< 2,4 kbit/s) et d\'une forte sensibilité aux bruits '
         'parasites des alimentations à découpage. Le <strong>CPL Haut Débit (HPLC)</strong> opère entre 2 MHz et 12 MHz en modulation multi-porteuses OFDM. '
         'Il adapte dynamiquement les fréquences pour contourner le bruit électrique, atteignant des débits de plus de 100 kbit/s à 10 Mbit/s avec routage maillé automatique.')
    ],
    cta='Vous concevez des projets de comptage intelligent (AMI/AMR), de sous-comptage résidentiel ou de modernisation de réseaux électriques nécessitant des compteurs CPL / HPLC certifiés DLMS/COSEM (sans abonnement SIM GSM, transmission par câbles existants) ? YOMIN fabrique des compteurs communicants série DTS performants.',
    body='''
<h2>La Solution de Télérelève Économique et Fiable pour les Réseaux Électriques Urbains</h2>
<p>Pour les compagnies d\'électricité, distributeurs d\'énergie municipaux et gestionnaires d\'immeubles tertiaires ou résidentiels, automatiser le relevé des consommations d\'énergie représente un impératif d\'efficacité et de rentabilité.</p>
<p>Cependant, les compteurs communicants sans fil (fonctionnant sur réseaux cellulaires 4G ou radiofréquences RF) rencontrent de graves échecs de liaison dans les sous-sols techniques et les immeubles en béton armé qui bloquent la propagation des ondes radio.</p>
<p>De plus, équiper des centaines de milliers de compteurs de cartes SIM cellulaires expose les distributeurs à des millions d\'euros de frais d\'abonnement récurrents auprès des opérateurs télécoms et à l\'obsolescence programmée des générations de réseaux mobiles.</p>
<p>Le <strong>Compteur d\'Énergie Intelligent à Courant Porteur en Ligne (Série DTS / DDS CPL)</strong> apporte la réponse technologique idéale : un compteur électronique certifié qui utilise les câbles électriques existants pour transmettre les données de facturation directement au concentrateur de poste, sans aucun angle mort radio et sans aucun frais d\'abonnement télécom.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série DTS CPL</h2>
<ol>
  <li><strong>Modem CPL Haut Débit HPLC Intégré :</strong> Traitement du signal par DSP 32 bits avec modulation OFDM multi-porteuses de 2 MHz à 12 MHz, assurant une immunité totale aux parasites harmoniques du réseau.</li>
  <li><strong>Circuit de Mesure Haute Précision :</strong> Échantillonnage numérique simultané des tensions et courants avec une précision Classe 1.0 (ou Classe 0.5S) en énergie active et Classe 2.0 en réactif selon les normes CEI 62053.</li>
  <li><strong>Transformateur de Couplage Haute Tension et Protection Surtensions :</strong> Isolement diélectrique renforcé protégeant l\'électronique contre les surtensions transitoires jusqu\'à 6 kV selon la norme CEI 62052-11.</li>
  <li><strong>Afficheur LCD Rétroéclairé Multifonction :</strong> Visualisation en temps réel des kWh actifs, kvarh réactifs, puissance instantanée en kW, tensions, courants et voyant d\'activité de communication CPL.</li>
  <li><strong>Détection Anti-Fraude et Alerte en Temps Réel :</strong> Détection de présence de champ magnétique perturbateur, inversion de phases ou ouverture du capot bornier avec envoi automatique d\'alerte au serveur central.</li>
</ol>
'''
)

PLC_ES = dict(
    lang='es',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-plc-smart-energy-meter-es',
    title='Medición Inteligente e Infraestructura AMI: ¿Qué es un Medidor de Energía Inteligente PLC?',
    breadcrumb='Medición Inteligente y Telemetría PLC',
    read='10 min de lectura',
    alt='Medidor de energía digital trifásico PLC (Serie DTS) instalado con cables de alimentación precintados y LED activo de comunicación por línea eléctrica',
    desc=('Infraestructura de medición avanzada (AMI/AMR), edificios residenciales y redes eléctricas inteligentes: ¿Qué es un medidor inteligente PLC (Power Line Carrier)? '
          'Transmisión de datos por modulación OFDM HPLC (2 a 12 MHz) sobre cables existentes de 230V/400V, cero costos de SIM celular y protocolo DLMS/COSEM.'),
    model='Serie DTS / DDS: Medidores de Energía Inteligentes Trifásicos y Monofásicos por Portadora de Corriente (PLC / HPLC) (Clase 1.0, OFDM 2-12 MHz, DLMS/COSEM)',
    category='Medición Inteligente e Infraestructura AMI / Medidores por Línea Eléctrica (PLC)',
    kw='medidor inteligente plc &middot; medidor de energia plc &middot; power line carrier meter &middot; medidor comunicante hplc &middot; telemetria ami plc &middot; medidor dts plc',
    specs=[
        ('Tecnología de Comunicación y Frecuencias', 'Portadora por Línea de Potencia de Alta Velocidad (HPLC) con modulación OFDM multialportadora (2 MHz a 12 MHz)'),
        ('Medio Físico de Transmisión de Datos', 'Transmisión directa sobre la red eléctrica de baja tensión existente (230V / 400V, 50/60 Hz ; sin cableado de datos dedicado)'),
        ('Clase de Exactitud Metrológica Certificada', 'Clase 1.0 (IEC 62053-21) energía activa, Clase 2.0 (IEC 62053-23) energía reactiva (Clase 0.5S con TC disponible)'),
        ('Velocidad de Transmisión de Datos en Línea', 'Velocidad de capa física PHY de hasta 10 Mbps (velocidad útil en capa de aplicación &gt; 100 kbps ; respuesta en sub-segundos)'),
        ('Protocolo de Aplicación e Interoperabilidad', 'Estándares abiertos internacionales: protocolo DLMS/COSEM (IEC 62056) y perfiles smart grid G3-PLC / PRIME'),
        ('Rangos Nominales de Tensión y Corriente', 'Tensión nominal: 3&times;230/400V AC (Trifásico 4 Hilos) ; Corriente directa: 5(60)A, 10(100)A ; Medición semidirecta TC: 1,5(6)A'),
        ('Seguridad Anti-Fraude y Detección de Eventos', 'Monitoreo activo integral: detección de campo magnético, neutro ausente, apertura de tapa de bornes con alarma en tiempo real'),
        ('Consumo Propio y Tolerancia Ambiental', 'Carga interna de tensión: &le; 1,5W / 6VA ; Rango de temperatura: $-40^\circ\text{C}$ a $+70^\circ\text{C}$ ; Grado de protección IP54')
    ],
    faqs=[
        ('¿Qué es un Medidor de Energía Inteligente PLC y cómo funciona la comunicación por línea eléctrica?',
         'Un Medidor de Energía Inteligente PLC (Power Line Carrier)—denominado también medidor CPL o medidor por línea de potencia HPLC—es '
         'un medidor electrónico digital equipado con un transceptor que envía los datos de consumo y telemetría '
         'directamente a través de los cables eléctricos de potencia que alimentan la instalación. '
         'En sistemas de medición inteligente (AMI / AMR) : '
         '<ul>'
         '<li><strong>Superposición de la Señal Digital:</strong> El medidor convierte las lecturas de energía (kWh activos/reactivos, voltajes, corrientes) '
         'en señales de alta frecuencia mediante modulación OFDM. Estas señales se superponen sobre la onda senoidal de 50Hz/60Hz del cable eléctrico.</li>'
         '<li><strong>Recepción en la Subestación de Distribución:</strong> En el transformador de distribución del barrio, '
         'un Concentrador de Datos (DCU) recibe y procesa las señales PLC de todos los medidores conectados, '
         'enviando las lecturas al software central de la empresa eléctrica mediante fibra óptica o módem celular 4G protegido.</li>'
         '</ul>'),
        ('¿Por qué las empresas eléctricas prefieren la tecnología PLC sobre los medidores celulares 4G en ciudades?',
         'En zonas urbanas de alta densidad y edificios de departamentos, los medidores celulares presentan grandes desventajas : '
         '<ul>'
         '<li><strong>100% Cobertura en Sótanos y Cuartos Eléctricos:</strong> En salas de medidores ubicadas en sótanos de concreto armado, '
         'las señales celulares (4G, NB-IoT) quedan bloqueadas por efecto de jaula de Faraday. La señal PLC viaja por los conductores de cobre '
         'llegando sin interrupciones a todos los medidores.</li>'
         '<li><strong>Cero Costos de Conectividad SIM Mensual:</strong> Los medidores celulares requieren un plan de datos mensual por cada equipo, '
         'lo que representa enormes costos operativos recurrentes. El sistema PLC utiliza la propia red eléctrica de la empresa, sin pagar tarifas celulares.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre el PLC de banda estrecha tradicional y el PLC de banda ancha (HPLC)?',
         'El PLC antiguo de banda estrecha (< 500 kHz) era lento (< 2,4 kbps) y muy vulnerable al ruido eléctrico de motores y fuentes conmutadas. '
         'El <strong>PLC de Banda Ancha de Alta Velocidad (HPLC)</strong> opera entre 2 MHz y 12 MHz con modulación multiportadora OFDM, '
         'esquivando automáticamente las bandas ruidosas y alcanzando velocidades de más de 100 kbps a 10 Mbps con enrutamiento de malla automático.')
    ],
    cta='¿Diseña proyectos de medición inteligente (AMI/AMR), submedición en edificios residenciales o modernización de redes de distribución que requieren medidores inteligentes PLC / HPLC certificados bajo DLMS/COSEM (sin pagos de SIM celular, transmisión por cables existentes)? YOMIN suministra medidores serie DTS de alta precisión.',
    body='''
<h2>La Solución de Telemetría Económica y Confiable para Redes Eléctricas Inteligentes</h2>
<p>Para las empresas distribuidoras de electricidad, cooperativas eléctricas y administradores de grandes complejos residenciales y comerciales, automatizar la toma de lecturas de energía es indispensable para reducir pérdidas no técnicas y optimizar la facturación.</p>
<p>Sin embargo, los medidores inteligentes inalámbricos (basados en redes celulares 4G o radiofrecuencia RF) sufren pérdidas de comunicación severas en salas eléctricas ubicadas en sótanos y edificios de hormigón armado que bloquean las ondas electromagnéticas.</p>
<p>Además, mantener miles de tarjetas SIM celulares activas genera gastos recurrentes millonarios en planes de telefonía móvil y expone el sistema al apagón de redes móviles antiguas.</p>
<p>El <strong>Medidor de Energía Inteligente por Portadora de Línea Eléctrica (Serie DTS / DDS PLC)</strong> proporciona la solución definitiva: un medidor electrónico homologado que utiliza los propios cables eléctricos de la instalación para transmitir los datos de facturación hacia el concentrador de datos, sin puntos ciegos de cobertura y sin pagar suscripciones celulares.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie DTS PLC</h2>
<ol>
  <li><strong>Módem de Banda Ancha HPLC Integrado:</strong> Procesamiento digital de señales DSP de 32 bits con modulación OFDM multialportadora de 2 MHz a 12 MHz con alta inmunidad al ruido eléctrico del transformador.</li>
  <li><strong>Módulo de Medición Metrológica de Alta Precisión:</strong> Muestreo simultáneo de voltajes y corrientes con exactitud Clase 1.0 (o Clase 0.5S) en energía activa y Clase 2.0 en energía reactiva bajo norma IEC 62053.</li>
  <li><strong>Transformador de Acoplamiento Dieléctrico y Filtro de Sobretensión:</strong> Aislamiento galvánico que protege los componentes electrónicos contra sobretensiones transitorias y descargas de rayo de hasta 6 kV.</li>
  <li><strong>Pantalla LCD Multifuncional con Luz de Fondo:</strong> Lectura clara en tiempo real de kWh acumulados, kvarh reactivos, potencia activa en kW, voltajes de fase, corrientes y estado de comunicación PLC.</li>
  <li><strong>Detección de Fraude y Notificación Instantánea:</strong> Alertas automáticas ante detección de imanes externos, manipulación del neutro o apertura de la tapa de bornes, enviadas de inmediato a la central.</li>
</ol>
'''
)

PLC_AR = dict(
    lang='ar',
    dir='rtl',
    slug='smart-metering-infrastructure-what-is-a-plc-smart-energy-meter-ar',
    title='العدادات الذكية والبنية التحتية المتقدمة AMI: ما هو عداد الكهرباء الذكي عبر شبكة الكهرباء CPL (PLC Energy Meter)؟',
    breadcrumb='العدادات الذكية وأنظمة الاتصال CPL/PLC',
    read='10 دقائق قراءة',
    alt='عداد كهرباء ذكي إلكتروني ثلاثي الأوجه يعمل بتقنية خطوط القدرة PLC (موديل DTS) مركب مع أسلاك طاقة مرصصة ومؤشرات اتصال نشطة',
    desc=('البنية التحتية المتقدمة لقياس الطاقة (AMI/AMR)، والأبراج السكنية، وأتمتة شبكات الكهرباء: ما هو عداد الكهرباء الذكي عبر شبكة الكهرباء (PLC)؟ '
          'إرسال البيانات عبر تقنية النطاق العريض HPLC وتعديل OFDM (تردد 2 إلى 12 ميجاهرتز) على كابلات 230V/400V الحالية، بدون اشتراكات شرائح اتصالات وببروتوكول DLMS/COSEM.'),
    model='سلسلة DTS / DDS: عدادات الكهرباء الذكية ثلاثية وأحادية الطور بتقنية نقل البيانات عبر شبكة الكهرباء (HPLC / PLC) (فئة دقة 1.0، تعديل OFDM، معتمدة DLMS/COSEM)',
    category='العدادات الذكية وأنظمة الاتصال AMI / عدادات خطوط القدرة الكهربائية (PLC)',
    kw='عداد كهرباء plc &middot; عداد طاقة cpl &middot; عداد ذكي plc smart meter &middot; عداد hplc &middot; قراءة العدادات عن بعد amr &middot; عداد كهرباء dts',
    specs=[
        ('تقنية الاتصال اللاسلكي والترددات الحاملة', 'تقنية خطوط القدرة الكهربائية عريضة النطاق (HPLC / PLC) بتعديل الترددات المتعامدة OFDM (من 2 إلى 12 ميجاهرتز)'),
        ('الوسيط الفيزيائي لنقل بيانات القراءات', 'تعديل مباشر على كابلات شبكة توزيع الكهرباء الحالية للجهد المنخفض (230V / 400V، 50/60 هرتز؛ بدون كابلات اتصالات إضافية)'),
        ('فئة الدقة المترولوجية المعتمدة للعداد', 'فئة 1.0 (IEC 62053-21) للطاقة الفعالة، وفئة 2.0 (IEC 62053-23) للطاقة غير الفعالة (تتوفر فئة 0.5S عبر محولات التيار)'),
        ('سرعة نقل البيانات وزمن الاستجابة للشبكة', 'سرعة طبقة فيزيائية تصل إلى 10 ميجابت/ثانية (معدل بيانات تطبيقي فعال &gt; 100 كيلوبت/ثانية؛ استجابة في أجزاء من الثانية)'),
        ('بروتوكول التطبيق والتوافقية القياسية', 'بروتوكولات قياسية مفتوحة لشركات الكهرباء: بروتوكول DLMS/COSEM (IEC 62056) ومعايير G3-PLC / PRIME الدولية'),
        ('الجهد والتيارات المقننة للتشغيل المباشر', 'الجهد الاسمي: 3&times;230/400V AC (ثلاثي الطور 4 أسلاك)؛ تيار التوصيل المباشر: 5(60)A و 10(100)A؛ قياس عبر CT: 1.5(6)A'),
        ('حماية الإيرادات ومكافحة التلاعب والسرقة', 'كشف ومراقبة مستمرة: رصد المجالات المغناطيسية الخارجية، والتلاعب بخط التعادل، والفتح غير المصرح به لغطاء الأطراف مع إرسال إنذار فوري'),
        ('الاستهلاك الذاتي للعداد وتحمل البيئة', 'استهلاك دائرة الجهد: &le; 1.5W / 6VA؛ نطاق درجة حرارة التشغيل: من $-40^\circ\text{C}$ إلى $+70^\circ\text{C}$؛ غلاف محكم IP54')
    ],
    faqs=[
        ('ما هو عداد الكهرباء الذكي عبر شبكة الكهرباء (PLC Smart Meter) وكيف يعمل نظام نقل البيانات CPL؟',
         'عداد الكهرباء الذكي بتقنية خطوط القدرة—والمعروف في قطاع شركات الكهرباء باسم عداد PLC أو عداد CPL عريض النطاق HPLC—هو '
         'عداد إلكتروني رقمي مجهز بمودم اتصال داخلي ينقل بيانات استهلاك الطاقة والقراءات اللحظية '
         'مباشرة عبر كابلات الكهرباء النحاسية الفعلية التي تغذي المشترك بالتيار الكهربائي. '
         'وفي منظومات القراءة التلقائية الذكية (AMI / AMR) : '
         '<ul>'
         '<li><strong>تضمين الإشارة الرقمية على موجة الكهرباء:</strong> يحول العداد قراءات الاستهلاك (كيلوواط/ساعة، والجهود، والتيارات، ومنحنيات الأحمال) '
         'إلى حزم إشارات رقمية عالية التردد بتعديل OFDM المتطور. وتُركب هذه الإشارات الدقيقة فوق الموجة الجيبية للكهرباء (50/60 هرتز) المارة في الكابل.</li>'
         '<li><strong>تجميع البيانات عند محول التوزيع:</strong> عند محول التغذية بالمنطقة، يقوم جهاز مجمع البيانات (DCU) بالتقاط '
         'وفك تشفير إشارات العدادات المربوطة على نفس المحول، ثم يرسلها مجمعة إلى مركز التحكم الرئيسي بالشركة عبر الألياف الضوئية أو شبكة 4G الآمنة.</li>'
         '</ul>'),
        ('لماذا تفضل شركات الكهرباء تقنية PLC على العدادات بشرائح الاتصالات 4G في المناطق الحضرية؟',
         'في المجمعات السكنية الشاهقة والمدن الكثيفة، تواجه العدادات بشرائح الاتصالات اللاسلكية عقبات جسيمة : '
         '<ul>'
         '<li><strong>تغطية تامة بنسبة 100% في غرف البدروم:</strong> في غرف العدادات الواقعة في سراديب المباني والخرسانات المسلحة، '
         'تنعدم إشارات شبكات المحمول تماماً (4G / NB-IoT) بسبب حجب الخرسانة. بينما تسري إشارة PLC عبر أسلاك النحاس لتصل لكافة العدادات دون أي عائق.</li>'
         '<li><strong>انعدام اشتراكات باقات المحمول الشهرية:</strong> تفرض عدادات المحمول تكاليف باقات إنترنت شهرية على كل عداد، '
         'مما يكلف ملايين الدولارات سنوياً. بينما تعمل تقنية PLC على كابلات الكهرباء المملوكة لشركة التوزيع مجاناً مدى الحياة دون أي فواتير لشركات الاتصالات.</li>'
         '</ul>'),
        ('ما هو الفرق بين تقنية PLC القديمة ضيقة النطاق وتقنية HPLC عريضة النطاق الحديثة؟',
         'كانت أنظمة PLC القديمة ضيقة النطاق (Narrowband) تعاني من بطء القراءة (< 2.4 كيلوبت/ثانية) وتأثرها بالضوضاء الكهربائية للأجهزة المنزلية. '
         'بينما تعمل تقنية <strong>HPLC الحديثة عريضة النطاق</strong> بترددات من 2 إلى 12 ميجاهرتز بتعديل OFDM متعدد القنوات، '
         'مما يمكنها من تجنب الترددات المشوشة تلقائياً وتحقيق سرعات فائقة من 100 كيلوبت/ثانية حتى 10 ميجابت/ثانية مع توجيه شبكي ذاتي مرن.')
    ],
    cta='هل تعمل على تنفيذ مشاريع العدادات الذكية والبنية التحتية المتقدمة (AMI/AMR)، أو أنظمة قياس الأبراج السكنية التي تتطلب عدادات ذكية بتقنية خطوط القدرة PLC / HPLC معتمدة DLMS/COSEM (بدون شرائح محمول، وقراءة عبر الكابلات القائمة)؟ تصنع يمين (YOMIN) عدادات سلسلة DTS بأعلى درجات الموثوقية.',
    body='''
<h2>الحل الهندسي الاقتصادي المثالي لقراءة عدادات الكهرباء في البيئات الحضرية</h2>
<p>بالنسبة لشركات وهيئات توزيع الكهرباء الحكومية، ومطوري المجمعات السكنية والتجارية الكبرى، يمثل التحول إلى القراءة الرقمية المؤتمتة للعدادات مطلباً حيوياً لتقليل الفواقد المالية وتأمين الإيرادات.</p>
<p>ومع ذلك، تواجه العدادات الذكية اللاسلكية (التي تعتمد على شرائح الهاتف المحمول 4G أو موجات الراديو RF) فشلاً ذريعاً في غرف الكهرباء بالسراديب والأبراج الخرسانية الشاهقة التي تعزل الإشارات اللاسلكية بالكامل.</p>
<p>وفضلاً عن ذلك، فإن تزويد مئات الآلاف من العدادات بشرائح اتصال يكبّل الشركات بفواتير اشتراكات شهرية متكررة تدفع لشركات الاتصالات، مع مخاطر توقف الخدمة مستقبلاً عند إلغاء الأجيال اللاسلكية القديمة.</p>
<p>يقدم <strong>عداد الكهرباء الذكي عبر شبكة الكهرباء (سلسلة DTS / DDS PLC)</strong> الإجابة الهندسية النموذجية: عداد إلكتروني معتمد يستغل كابلات الكهرباء النحاسية الممتدة بالفعل داخل المبنى لنقل بيانات الفوترة مباشرة إلى مركز التحكم، دون أي نقاط حجب لاسلكية ودون أي رسوم اشتراكات اتصالات.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة عدادات DTS PLC</h2>
<ol>
  <li><strong>مودم خطوط القدرة عريض النطاق HPLC:</strong> معالجة إشارات رقمية متطورة بمعالج 32 بت وتعديل OFDM متعدد الترددات (2 إلى 12 ميجاهرتز) يضمن مناعة كاملة ضد التوافقيات والتشويش الكهربائي.</li>
  <li><strong>دائرة قياس مترولوجية متناهية الدقة:</strong> أخذ عينات رقمية متزامنة لجهود وتيارات الأوجه بدقة فئة 1.0 (أو 0.5S) للطاقة الفعالة وفئة 2.0 للطاقة غير الفعالة طبقاً للمواصفة IEC 62053.</li>
  <li><strong>محول اقتران ديزلكتريكي وحماية من الصواعق:</strong> عزل داخلي متين يحمي الدوائر الإلكترونية الحساسة من النبضات العابرة وصدمات الصواعق حتى 6 كيلوفولت طبقاً لمعايير IEC 62052-11.</li>
  <li><strong>شاشة LCD واضحة ومتعددة المعلمات:</strong> استعراض فوري ومستمر للطاقة التراكمية، والقدرة اللحظية بالكيلوواط، وجهود وتيارات الأوجه، مع مؤشر LED ضوئي يوضح نشاط إرسال واستقبال بيانات PLC.</li>
  <li><strong>منظومة كشف التلاعب ومكافحة سرقة الكهرباء:</strong> رصد وتوثيق فوري لمحاولات التأثير المغناطيسي، أو عكس الأطوار، أو فتح غطاء التوصيل مع إرسال إنذار مباشر وفوري لمركز التحكم.</li>
</ol>
'''
)

# ==============================================================================
# 2. AC CURRENT TRANSDUCER (EN, FR, ES, AR)
# ==============================================================================

ACT_EN = dict(
    lang='en',
    dir='ltr',
    slug='industrial-automation-what-is-an-ac-current-transducer',
    title='Industrial Automation: What Is an AC Current Transducer?',
    breadcrumb='Current Sensors &amp; Industrial Transducers',
    read='10 min read',
    alt='Compact DIN-rail AC Current Transducer (Model YM-ACT series) with shielded 4-20mA analog signal wiring connected to a PLC analog input module',
    desc=('Industrial automation control panels, PLC analog I/O, motor load telemetry, and SCADA telemetry systems: What is an AC current transducer? '
          'How true-RMS signal conditioning, loop-powered 2-wire 4-20mA DC analog outputs, 3kV AC galvanic isolation, and split-core ease eliminate CT signal converter bottlenecks.'),
    model='Model YM-ACT / ACT Series Split-Core & Solid-Core True-RMS AC Current Transducers (0-10A to 0-500A AC Input, 4-20mA / 0-10V DC Analog Output, 3kV Isolation, Class 0.5)',
    category='Current Sensors & Industrial Transducers / AC Current Transducers',
    kw='what is an ac current transducer &middot; ac current transducer &middot; current transmitter 4-20ma &middot; split core current transducer &middot; loop powered current sensor &middot; ym-act transducer',
    specs=[
        ('Primary AC Current Measurement Range', 'Standard input selections: 0–10A, 0–20A, 0–50A, 0–100A, 0–200A, 0–300A, up to 0–500A AC (50/60 Hz sine or distorted waveforms)'),
        ('Standardized DC Analog Output Signals', 'Industrial telemetry standard: 4–20 mA DC current loop (Optional: 0–5 V DC, 0–10 V DC, or 1–5 V DC voltage outputs)'),
        ('Signal Conditioning & Measurement Technology', 'True-RMS (TRMS) precision electronic conversion (Accurate on VFD inverter harmonics and non-linear power supplies)'),
        ('Measurement Accuracy & Linearity Class', 'High metrological precision: Class 0.5 (&plusmn;0.5% of full-scale reading, linearity &lt; 0.2% across full dynamic range)'),
        ('Galvanic Dielectric Isolation Barrier', 'Optocoupler &amp; magnetic isolation: Tested dielectric withstand up to 3000 V AC / 1 min (Primary cable to secondary output)'),
        ('Power Supply Configuration & Loop Burden', '2-Wire loop-powered: +24V DC nominal (12V to 30V DC range; Maximum loop burden resistance $R_L \le 500\,\Omega$)'),
        ('Response Time & Signal Bandwidth', 'High-speed analog response: Step response time &le; 200 ms (Frequency bandwidth: 20 Hz to 1 kHz for harmonic monitoring)'),
        ('Housing Construction & Mounting Standard', 'Flame-retardant ABS/polycarbonate enclosure (UL 94 V-0); 35mm DIN-rail mountable and flat panel surface screw mounting')
    ],
    faqs=[
        ('What is an AC Current Transducer and why cannot PLCs read standard current transformers directly?',
         'An AC Current Transducer—frequently designated as an AC current transmitter, 4–20mA current sensor, or current-to-DC converter—is '
         'a precision solid-state electronic device that measures alternating current (AC) flowing through a power conductor '
         'and converts it into an electrically isolated, standardized low-voltage direct current (DC) analog signal (typically 4–20 mA DC or 0–10 V DC). '
         'In industrial PLC and SCADA automation panels: '
         '<ul>'
         '<li><strong>The Incompatibility of Traditional CTs:</strong> Standard current transformers (CTs) output an alternating current of 0–5 A AC. '
         'Programmable Logic Controllers (PLCs from Siemens, Allen-Bradley, Schneider, Omron) and microcontrollers are strictly DC microelectronic circuits '
         'whose analog input cards only accept 4–20 mA DC or 0–10 V DC signals. Connecting 5A AC directly to a PLC analog card will destroy the sensitive analog-to-digital converter (ADC) channels.</li>'
         '<li><strong>Integrated Conditioning Solution:</strong> Instead of installing a bulky CT plus an external signal conditioning DIN-rail amplifier module '
         'and messy inter-wiring, the YOMIN ACT series combines the inductive sensing core and the precision true-RMS 4–20mA transmitter circuit '
         'into a single, compact, pre-calibrated housing.</li>'
         '</ul>'),
        ('Why is a 4–20 mA DC Current Loop preferred over a 0–10 V DC signal in industrial plants?',
         'While voltage signals (0–10 V DC) are simple, current loops (4–20 mA DC) dominate industrial automation for two critical engineering reasons: '
         '<ul>'
         '<li><strong>Zero Voltage-Drop Signal Degradation:</strong> Electrical cables have intrinsic resistance ($R$). Over cable runs exceeding 50 to 300 meters '
         'between factory floor motor drives and central PLC control rooms, voltage signals suffer significant $I \times R$ voltage drop, distorting measurement accuracy. '
         'A 4–20 mA current loop delivers identical current regardless of cable length or loop resistance (up to $500\,\Omega$).</li>'
         '<li><strong>Live Zero (4 mA) Wire-Break Fault Detection:</strong> A 0–10 V signal cannot distinguish between zero measured current and a severed/disconnected sensor wire. '
         'In a 4–20 mA loop, <strong>4 mA represents 0% current</strong>, while <strong>0 mA instantly alerts the PLC to a broken wire, blown fuse, or damaged sensor</strong>.</li>'
         '</ul>'),
        ('What is the difference between Average-Responding and True-RMS AC Current Transducers?',
         'Basic low-cost transducers utilize simple average-rectifying circuits calibrated to the root-mean-square value of a pure sine wave ($RMS = 1.11 \times \text{Average}$). '
         'However, in modern industrial plants with Variable Frequency Drives (VFDs), solar inverters, LED power supplies, and DC rectifiers, '
         'AC currents contain severe harmonic distortion and non-sinusoidal chopped waveforms. '
         'Average-sensing transducers produce measurement errors exceeding 20% to 40% under harmonic distortion. '
         'YOMIN ACT transducers incorporate <strong>True-RMS (TRMS) analog computation chips</strong> that mathematically calculate the exact root-mean-square '
         'heating value of the waveform, delivering accurate &plusmn;0.5% measurements on distorted and chopped inverter currents.')
    ],
    cta='Designing industrial automation control panels, motor control centers (MCC), building management systems (BMS), or SCADA telemetry enclosures requiring certified Class 0.5 True-RMS AC current transducers (0-10A to 0-500A, 4-20mA / 0-10V DC analog output, 3kV isolation)? YOMIN manufactures precision ACT series transducers.',
    body='''
<h2>The Precision Translation Bridge Between High-Power AC Equipment and Microelectronic PLCs</h2>
<p>Inside modern industrial manufacturing facilities, chemical process plants, water treatment stations, and automated machinery, Programmable Logic Controllers (PLCs) and Distributed Control Systems (DCS) orchestrate thousands of pumps, fans, conveyors, and compressors.</p>
<p>To prevent motor overloads, detect mechanical pump jams, monitor conveyor belt slip, and calculate factory energy consumption, the automation PLC must know the precise electrical current drawn by each three-phase motor.</p>
<p>However, industrial motors operate on <strong>380V, 480V, or 690V AC</strong> with phase currents of dozens or hundreds of amperes. Traditional current transformers scale this down to 5A AC, but PLC analog input modules are strictly low-voltage DC electronic devices that cannot accept alternating current directly.</p>
<p>The <strong>AC Current Transducer (Model YM-ACT Series)</strong> serves as the indispensable translation interface: a solid-state instrument sensor that measures AC conductor current and converts it into a clean, linear, electrically isolated 4–20 mA DC or 0–10 V DC analog signal that wires directly into any standard PLC analog card.</p>

<h2>Engineering Anatomy: Inside a Model YM-ACT True-RMS AC Current Transducer</h2>
<ol>
  <li><strong>Magnetic Induction Sensing Core (Solid or Split-Core):</strong> High-permeability silicon steel or permalloy toroidal core with precision secondary winding. Split-core models feature a spring-loaded hinge and latch for rapid clamp-on installation around existing live conductors without disconnecting power cables.</li>
  <li><strong>Integrated True-RMS Signal Processing Circuitry:</strong> On-board precision analog computation IC continuously samples the induced AC waveform, executing instantaneous squaring, averaging, and square-root calculations to output true-RMS current values even on distorted VFD inverter outputs.</li>
  <li><strong>3000V AC Galvanic Dielectric Isolation Barrier:</strong> High-voltage optocoupler and magnetic isolation barrier separating the high-voltage primary conductor aperture from the low-voltage DC output terminals, protecting delicate PLC microelectronics from destructive power surges.</li>
  <li><strong>Precision 4–20 mA DC Loop-Powered Transmitter:</strong> Regulated constant-current output driver that powers itself directly from the PLC\'s 24V DC loop supply (2-wire configuration), eliminating the need for a separate auxiliary power supply brick.</li>
  <li><strong>Flame-Retardant DIN-Rail Mounting Enclosure:</strong> Compact UL 94 V-0 rated polycarbonate housing that snaps directly onto standard 35mm DIN-rails, saving valuable horizontal space in crowded control cabinets.</li>
</ol>

<h2>Comparison: Integrated AC Current Transducer vs. Traditional CT + Signal Conditioner vs. Digital Power Meter</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Parameter</th>
      <th>Digital Panel Power Meter</th>
      <th>Traditional 5A CT + Separate DIN Converter</th>
      <th>YOMIN Integrated AC Current Transducer (ACT Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>System Complexity &amp; Component Count</strong></td>
      <td>Bulky meter body + 3 external CTs + external power supply.</td>
      <td>2 separate components: 5A CT + DIN-rail signal conditioner module.</td>
      <td><strong>1 Single Integrated Unit: Sensor core and 4-20mA transmitter in one compact housing.</strong></td>
    </tr>
    <tr>
      <td><strong>Cabinet Space &amp; Wiring Connections</strong></td>
      <td>Takes up front door cutout and extensive multi-wire harnesses.</td>
      <td>Consumes double DIN-rail space and requires 4 extra inter-wiring terminations.</td>
      <td><strong>Ultra-Compact: Mounts directly over conductor; requires only 2 wires to the PLC.</strong></td>
    </tr>
    <tr>
      <td><strong>Auxiliary Power Supply Requirements</strong></td>
      <td>Requires dedicated 110V/230V AC or 24V DC auxiliary power supply.</td>
      <td>Requires dedicated 24V DC auxiliary power wiring to the converter module.</td>
      <td><strong>Loop-Powered (2-Wire): Powers itself directly from the PLC\'s 24V DC analog loop.</strong></td>
    </tr>
    <tr>
      <td><strong>Non-Sinusoidal VFD Harmonic Accuracy</strong></td>
      <td>Accurate; but expensive and complex Modbus programming required.</td>
      <td>Often limited: Inexpensive conditioners use average-sensing with 30%+ VFD errors.</td>
      <td><strong>True-RMS Performance: True-RMS chip delivers &plusmn;0.5% precision on chopped inverter currents.</strong></td>
    </tr>
    <tr>
      <td><strong>Installation &amp; Commissioning Labor</strong></td>
      <td>High: Cutting panel doors, parameter programming, baud rate configuration.</td>
      <td>Moderate: Mounting CT, mounting converter, running intermediate secondary wires.</td>
      <td><strong>Instant Installation: Pass cable through aperture, connect 2 wires to PLC, done in 2 minutes.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

ACT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='industrial-automation-what-is-an-ac-current-transducer-fr',
    title="Automatismes Industriels & Télégestion : Qu'est-ce qu'un Transducteur de Courant AC (4-20mA) ?",
    breadcrumb='Capteurs de Courant &amp; Transducteurs Industriels',
    read='10 min de lecture',
    alt='Transducteur de courant alternatif compact pour rail DIN (Série YM-ACT) avec câblage de signal analogique 4-20mA raccordé à un automate programmable PLC',
    desc=('Armoires d\'automatismes industriels, entrées analogiques PLC, contrôle des moteurs et télégestion SCADA : Qu\'est-ce qu\'un transducteur de courant AC ? '
          'Conversion efficace True-RMS, signal de sortie analogique 4-20mA deux fils alimenté par la boucle, isolement galvanique 3kV et modèles ouvrants faciles à poser.'),
    model='Série YM-ACT / ACT : Transducteurs de Courant Alternatif True-RMS Ouvrants et Fixes (Entrée 0-10A à 0-500A AC, Sortie Analogique 4-20mA / 0-10V DC, Isolement 3kV, Classe 0.5)',
    category='Capteurs de Courant & Transducteurs Industriels / Transducteurs de Courant Alternatif',
    kw='transducteur de courant ac &middot; transmetteur de courant 4 20ma &middot; capteur de courant ouvrant plc &middot; convertisseur ct 4 20ma &middot; transducteur true rms &middot; ym-act',
    specs=[
        ('Plage de Mesure du Courant Primaire AC', 'Calibres primaires standard : 0–10A, 0–20A, 0–50A, 0–100A, 0–200A, 0–300A jusqu\'à 0–500A AC (50/60 Hz sinus ou déformé)'),
        ('Signaux Normalisés de Sortie Analogique DC', 'Standard industriel de télémesure : boucle de courant 4–20 mA DC (Option : sorties tension 0–5 V DC ou 0–10 V DC)'),
        ('Technologie de Traitement et Conversion', 'Conversion électronique True-RMS (valeur efficace vraie, exacte même sur variateurs de vitesse et signaux hachés)'),
        ('Classe de Précision et Linéarité de Mesure', 'Haute précision métrologique : Classe 0.5 (&plusmn;0,5% de la pleine échelle, linéarité &lt; 0,2% sur toute la plage)'),
        ('Barrière d\'Isolement Galvanique Diélectrique', 'Séparation optocoupleur et magnétique : tenue diélectrique testée à 3000 V AC pendant 1 min (primaire vers sortie)'),
        ('Alimentation et Charge Maximale de Boucle', 'Boucle 2 fils auto-alimentée : +24V DC nominal (plage 12V à 30V DC ; résistance maximale de boucle $R_L \le 500\,\Omega$)'),
        ('Temps de Réponse et Bande Passante Signal', 'Réponse analogique ultra-rapide : temps de montée &le; 200 ms (bande passante fréquentielle : 20 Hz à 1 kHz)'),
        ('Boîtier Mécanique et Fixation sur Rail DIN', 'Boîtier thermoplastique ignifugé auto-extinguible (UL 94 V-0) ; montage direct sur rail DIN 35 mm ou fixation par vis')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un Transducteur de Courant AC et pourquoi un automate ne lit-il pas un TC classique ?',
         'Un Transducteur de Courant Alternatif—souvent appelé transmetteur de courant 4-20mA ou convertisseur intensité-tension—est '
         'un capteur électronique qui mesure le courant alternatif circulant dans un conducteur de puissance '
         'et le transforme en un signal analogique continu basse tension normalisé (généralement 4–20 mA DC ou 0–10 V DC). '
         'Dans les armoires d\'automatisme industriel : '
         '<ul>'
         '<li><strong>L\'Incompatibilité des TC Standards :</strong> Les transformateurs de courant classiques délivrent un signal alternatif 0–5 A AC. '
         'Les cartes d\'entrées analogiques des automates programmables (Siemens, Schneider, Rockwell) ne traitent que des signaux continus basse tension. '
         'Raccorder du 5A AC directement sur une carte analogique PLC détruirait instantanément les convertisseurs analogique-numérique.</li>'
         '<li><strong>Solution Tout-en-Un :</strong> Au lieu d\'installer un TC classique encombrant associé à un convertisseur rail DIN externe '
         'avec de multiples câbles intermédiaires, le transducteur YOMIN ACT intègre le circuit de mesure inductif et le transmetteur 4-20mA '
         'dans un boîtier unique compact.</li>'
         '</ul>'),
        ('Pourquoi la boucle de courant 4–20 mA est-elle préférée au signal 0–10 V dans l\'industrie ?',
         'Dans les usines et sites de production, la boucle de courant 4–20 mA s\'impose pour deux raisons majeures : '
         '<ul>'
         '<li><strong>Insensibilité aux Longueurs de Câble :</strong> Un signal en tension (0–10 V) subit une chute ohmique ($U = R \times I$) '
         'sur les longues distances (plus de 50 à 300 mètres), faussant la mesure à l\'automate. Une boucle 4–20 mA transporte un courant constant '
         'rigoureusement identique quel que soit la résistance du câble.</li>'
         '<li><strong>Détection Immédiate de Rupture de Câble (Zéro Vivant) :</strong> En 0–10 V, un signal nul (0 V) peut signifier une intensité nulle '
         'ou un fil sectionné. En boucle 4–20 mA, <strong>4 mA correspond à 0% de charge</strong>, tandis qu\'un courant de <strong>0 mA signale instantanément '
         'à l\'automate une coupure de câble ou un capteur défaillant</strong>.</li>'
         '</ul>'),
        ('Quelle est la différence entre un transducteur moyenne redressée et un modèle True-RMS ?',
         'Les transducteurs d\'entrée de gamme utilisent un redressement moyen calibré uniquement pour une onde sinusoïdale pure. '
         'Sur des moteurs pilotés par des variateurs de fréquence (VFD) ou des charges non linéaires, ces appareils affichent des erreurs de 20% à 40%. '
         'Les transducteurs YOMIN ACT intègrent un <strong>processeur analogique True-RMS (valeur efficace vraie)</strong> qui calcule mathématiquement '
         'la véritable énergie calorifique du signal, assurant une précision métrologique de &plusmn;0,5% même sur des signaux fortement déformés.')
    ],
    cta='Vous concevez des armoires d\'automatismes industriels, des tiroirs de contrôle moteur MCC ou des systèmes de supervision SCADA nécessitant des transducteurs de courant alternatif True-RMS certifiés Classe 0.5 (0-10A à 0-500A, sortie analogique 4-20mA, isolement 3kV) ? YOMIN fabrique des transducteurs série ACT de haute fiabilité.',
    body='''
<h2>Le Pont de Mesure Indispensable entre la Puissance Électrique et les Automates PLC</h2>
<p>Dans les usines de fabrication automatisées, les stations de pompage, les centres de traitement des eaux et les lignes de production robotisées, les automates programmables industriels (PLC) et systèmes SCADA supervisent en continu des centaines de moteurs, compresseurs et ventilateurs.</p>
<p>Pour prévenir la surcharge mécanique d\'un moteur, détecter l\'usure d\'un palier de pompe ou optimiser la consommation énergétique de l\'usine, l\'automate a besoin de connaître avec exactitude le courant électrique réel consommé par chaque machine.</p>
<p>Cependant, les moteurs industriels fonctionnent sous <strong>380V ou 400V AC</strong> avec des courants de plusieurs dizaines ou centaines d\'ampères. Les TC classiques fournissent du 5A AC, que les cartes d\'entrées analogiques des automates ne peuvent accepter sous peine de destruction immédiate.</p>
<p>Le <strong>Transducteur de Courant Alternatif (Série YM-ACT)</strong> assure cette passerelle d\'instrumentation : un capteur électronique autonome qui mesure le courant alternatif et le convertit en un signal analogique continu linéaire, normalisé et isolé (4–20 mA DC ou 0–10 V DC) directement raccordable aux entrées automates.</p>

<h2>Caractéristiques et Avantages Technologiques de la Série YM-ACT</h2>
<ol>
  <li><strong>Tore de Mesure Intégré (Modèles Fixes ou Ouvrants) :</strong> Circuit magnétique haute perméabilité. Les versions ouvrantes (Split-Core) se clipsent directement autour des câbles en service sans aucune interruption de l\'alimentation électrique.</li>
  <li><strong>Convertisseur Analogique True-RMS Haute Précision :</strong> Électronique de traitement calculant la valeur efficace réelle instantanée, éliminant les erreurs de mesure sur les départs alimentés par variateurs de vitesse.</li>
  <li><strong>Isolement Galvanique Renforcé de 3000 V AC :</strong> Séparation diélectrique totale entre le câble de puissance haute tension et les circuits de signal basse tension, protégeant l\'automate contre tout retour de surtension.</li>
  <li><strong>Technologie 2 Fils Auto-Alimentée par la Boucle :</strong> Le transducteur s\'alimente directement sur la tension 24V DC fournie par la carte automate, supprimant le besoin d\'une alimentation secteur auxiliaire.</li>
  <li><strong>Format Modulaire pour Rail DIN 35 mm :</strong> Boîtier thermoplastique ignifugé UL 94 V-0 s\'encliquetant instantanément sur rail DIN, réduisant l\'encombrement dans les armoires de contrôle.</li>
</ol>
'''
)

ACT_ES = dict(
    lang='es',
    dir='ltr',
    slug='industrial-automation-what-is-an-ac-current-transducer-es',
    title='Automatización Industrial y Control PLC: ¿Qué es un Transductor de Corriente Alterna (AC Current Transducer)?',
    breadcrumb='Sensores de Corriente y Transductores Industriales',
    read='10 min de lectura',
    alt='Transductor de corriente alterna compacto para riel DIN (Serie YM-ACT) con cableado de señal analógica 4-20mA conectado a un módulo de entradas analógicas de PLC',
    desc=('Tableros de control industrial, entradas analógicas de PLC, telemetría de motores y sistemas de supervisión SCADA: ¿Qué es un transductor de corriente alterna (AC Current Transducer)? '
          'Conversión True-RMS de alta precisión, salida analógica de 4-20mA DC de 2 hilos autoalimentada en bucle, aislamiento galvánico de 3kV y modelos de núcleo abierto.'),
    model='Serie YM-ACT / ACT: Transductores de Corriente Alterna True-RMS de Núcleo Sólido y Núcleo Abierto (Entrada 0-10A a 0-500A AC, Salida Analógica 4-20mA / 0-10V DC, Aislamiento 3kV)',
    category='Sensores de Corriente y Transductores Industriales / Transductores de Corriente Alterna',
    kw='transductor de corriente ac &middot; transmisor de corriente 4 20ma &middot; sensor de corriente nucleo abierto &middot; convertidor ct a 4 20ma &middot; transductor true rms &middot; ym-act plc',
    specs=[
        ('Rango de Medición de Corriente Primaria AC', 'Calibres primarios estándar: 0–10A, 0–20A, 0–50A, 0–100A, 0–200A, 0–300A hasta 0–500A AC (50/60 Hz senoidal o distorsionada)'),
        ('Señales Normalizadas de Salida Analógica DC', 'Estándar industrial de instrumentación: bucle de corriente 4–20 mA DC (Opcional: salidas de voltaje 0–5 V DC o 0–10 V DC)'),
        ('Tecnología de Conversión y Tratamiento', 'Conversión electrónica True-RMS (valor cuadrático medio real, exacto ante armónicos y variadores de frecuencia VFD)'),
        ('Clase de Exactitud y Linealidad Metrológica', 'Alta precisión industrial: Clase 0.5 (&plusmn;0.5% de fondo de escala, linealidad &lt; 0.2% en todo el rango de medida)'),
        ('Aislamiento Galvánico Dieléctrico de Seguridad', 'Barrera optoacoplada y magnética: rigidez dieléctrica ensayada de 3000 V AC durante 1 min (cable primario a bornes de salida)'),
        ('Alimentación y Resistencia de Carga Máxima', 'Bucle de 2 hilos autoalimentado: +24V DC nominal (rango 12V a 30V DC ; resistencia máxima de bucle $R_L \le 500\,\Omega$)'),
        ('Tiempo de Respuesta y Ancho de Banda', 'Respuesta analógica rápida: tiempo de subida &le; 200 ms (ancho de banda de frecuencia: 20 Hz a 1 kHz)'),
        ('Carcasa Mecánica y Montaje en Riel DIN', 'Gabinete termoplástico autoextinguible (UL 94 V-0) ; montaje directo en riel DIN de 35 mm o fijación por tornillos a placa')
    ],
    faqs=[
        ('¿Qué es un Transductor de Corriente AC y por qué un PLC no puede leer un transformador de corriente estándar?',
         'Un Transductor de Corriente Alterna—conocido como transmisor de corriente 4-20mA o transductor de corriente a voltaje continuo—es '
         'un sensor electrónico de precisión que mide la corriente alterna que fluye por un conductor eléctrico '
         'y la convierte en una señal analógica continua de bajo voltaje linealmente proporcional (típicamente 4–20 mA DC o 0–10 V DC). '
         'En tableros de control con PLC y sistemas SCADA : '
         '<ul>'
         '<li><strong>Incompatibilidad de los TCs Tradicionales:</strong> Los transformadores de corriente convencionales entregan 0–5 A AC. '
         'Las tarjetas de entradas analógicas de los PLCs (Siemens, Allen-Bradley, Schneider) solo admiten señales directas de corriente continua (DC). '
         'Conectar corriente alterna de 5A directamente en el PLC destruiría sus microcircuitos convertidores analógico-digitales.</li>'
         '<li><strong>Dispositivo Compacto Todo-en-Uno:</strong> En lugar de instalar un TC convencional voluminoso más un convertidor de señal externo '
         'con cables adicionales, el transductor YOMIN ACT integra el núcleo de sensado y el transmisor 4-20mA en un único cuerpo compacto.</li>'
         '</ul>'),
        ('¿Por qué se prefiere el lazo de corriente 4–20 mA sobre la señal 0–10 V en plantas industriales?',
         'En la automatización de fábricas, el bucle de corriente 4–20 mA es el estándar dominante por dos razones : '
         '<ul>'
         '<li><strong>Inmunidad a la Resistencia del Cable:</strong> Una señal de voltaje (0–10 V) sufre caídas de tensión ($V = I \times R$) '
         'en recorridos largos (de 50 a 300 metros), falseando la lectura en el PLC. Un bucle 4–20 mA mantiene la corriente exacta '
         'sin importar la longitud del cable ni la resistencia del circuito.</li>'
         '<li><strong>Detección Instantánea de Cable Cortado (Cero Vivo):</strong> En 0–10 V, un valor de 0 V puede ser corriente nula '
         'o un cable roto. En 4–20 mA, <strong>4 mA representa el 0% de corriente</strong>, mientras que <strong>0 mA advierte inmediatamente '
         'al PLC que el cable se cortó o el sensor falló</strong>.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre un transductor de promedio rectificado y uno True-RMS?',
         'Los transductores básicos utilizan circuitos de promedio calibrados para ondas senoidales puras. '
         'En plantas con variadores de frecuencia (VFD) y motores regulados, las ondas de corriente sufren graves distorsiones armónicas, '
         'provocando errores de lectura de más del 20% al 40%. Los transductores YOMIN ACT incorporan <strong>tecnología True-RMS (valor eficaz real)</strong> '
         'que calcula con precisión matemática el valor térmico de la señal, asegurando mediciones confiables con exactitud de &plusmn;0.5%.')
    ],
    cta='¿Diseña tableros de automatización con PLC, centros de control de motores MCC o sistemas SCADA que requieren transductores de corriente alterna True-RMS Clase 0.5 (0-10A a 0-500A, salida 4-20mA DC, aislamiento de 3kV)? YOMIN suministra transductores serie ACT de máxima precisión.',
    body='''
<h2>El Puente de Medición Indispensable entre la Potencia Eléctrica y los Autómatas PLC</h2>
<p>En plantas industriales automatizadas, estaciones de bombeo de agua, centros de control de procesos químicos y maquinaria de manufactura, los autómatas programables (PLC) y sistemas SCADA supervisan el funcionamiento continuo de cientos de motores, ventiladores y compresores.</p>
<p>Para prevenir la sobrecarga mecánica de un motor, detectar atascos mecánicos en bombas o registrar el consumo energético de la planta, el PLC necesita conocer con exactitud la corriente eléctrica real que consume cada máquina.</p>
<p>Sin embargo, los motores operan en <strong>380V o 440V AC</strong> con corrientes de decenas o cientos de amperios. Los transformadores de corriente entregan 5A AC, que las tarjetas de entradas analógicas de los PLCs no pueden procesar directamente.</p>
<p>El <strong>Transductor de Corriente Alterna (Serie YM-ACT)</strong> resuelve este desafío : un sensor electrónico de estado sólido que mide la corriente alterna y la transforma en una señal analógica continua de 4–20 mA DC o 0–10 V DC, lineal y con aislamiento galvánico de 3kV, lista para conectarse directamente a las entradas analógicas del autómata.</p>

<h2>Elementos Constructivos y Calidad de Ingeniería de la Serie YM-ACT</h2>
<ol>
  <li><strong>Núcleo Magnético de Inducción (Sólido o Núcleo Abierto):</strong> Fabricado con láminas de acero al silicio de alta permeabilidad. Los modelos de núcleo abierto (Split-Core) se instalan de forma rápida abrazando los cables sin necesidad de desconectar la instalación.</li>
  <li><strong>Circuito Integrado True-RMS de Alta Exactitud:</strong> Procesamiento analógico continuo que calcula el valor cuadrático medio real de la onda, garantizando mediciones exactas en motores controlados por variadores de frecuencia.</li>
  <li><strong>Barrera de Aislamiento Galvánico Dieléctrico de 3000 V AC:</strong> Separación óptica y magnética que aísla los cables de potencia de los circuitos secundarios de control, protegiendo al autómata contra sobretensiones peligrosas.</li>
  <li><strong>Tecnología de 2 Hilos Alimentada por el Lazo:</strong> El transductor toma su energía directamente de los 24V DC de la entrada analógica del PLC, eliminando fuentes de alimentación adicionales en el gabinete.</li>
  <li><strong>Montaje Modular en Riel DIN de 35 mm:</strong> Carcasa termoplástica autoextinguible (UL 94 V-0) que se acopla directamente al riel DIN, optimizando el espacio dentro de los gabinetes de control.</li>
</ol>
'''
)

ACT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='industrial-automation-what-is-an-ac-current-transducer-ar',
    title='الأتمتة الصناعية وأنظمة التحكم PLC: ما هو محول الإشارة لتيار التيار المتردد (AC Current Transducer)؟',
    breadcrumb='حساسات ومحولات الإشارة الصناعية للتيار',
    read='10 دقائق قراءة',
    alt='محول إشارة تيار متردد مدمج يركب على سكة DIN (موديل YM-ACT) مع أسلاك خرج تناظري 4-20mA متصلة بكارت المداخل التناظرية لوحدة PLC',
    desc=('لوحات التحكم في الأتمتة الصناعية، ومداخل PLC التناظرية، ومراقبة أحمال المحركات، وأنظمة المراقبة SCADA: ما هو محول إشارة التيار المتردد (AC Current Transducer)؟ '
          'حساب القيمة الفعالة الحقيقية True-RMS، والخرج التناظري المعياري 4-20mA بسلكين يتغذى من الحلقة، والعزل الكهربائي 3kV، وسهولة المحولات ذات القلب المشقوق.'),
    model='سلسلة YM-ACT / ACT: محولات إشارة التيار المتردد True-RMS ذات القلب المصمت والمشقوق (دخل من 0-10A إلى 0-500A AC، خرج تناظري 4-20mA / 0-10V DC، عزل 3kV، فئة دقة 0.5)',
    category='حساسات ومحولات الإشارة الصناعية للتيار / محولات إشارة التيار المتردد',
    kw='محول اشارة تيار متردد &middot; ac current transducer &middot; مرسل تيار 4 20ma &middot; حساس تيار للـ plc &middot; محول تيار مشقوق 4 20ma &middot; ترانسديوسر تيار true rms',
    specs=[
        ('نطاق قياس تيار الدخل المتردد الاسمي', 'سعات دخل معيارية: 0–10A و 0–20A و 0–50A و 0–100A و 0–200A و 0–300A وحتى 0–500A AC (تردد 50/60 هرتز جيبية أو مشوهة)'),
        ('إشارات الخرج التناظرية المستمرة المعيارية', 'المعيار الصناعي القياسي لأنظمة التحكم: حلقة تيار 4–20 mA DC (خيارات إضافية: خرج جهد 0–5 V DC أو 0–10 V DC)'),
        ('تقنية المعالجة والحساب الإلكتروني للإشارة', 'حساب إلكتروني تناظري للقيمة الفعالة الحقيقية True-RMS (دقة تامة مع تشوهات مغيرات السرعة والإنفرتر VFD)'),
        ('فئة الدقة المترولوجية والخطية للحساس', 'دقة قياس صناعية متناهية: فئة 0.5 (&plusmn;0.5% من كامل التدريج، خطية قياس &lt; 0.2% عبر كامل النطاق)'),
        ('حاجز العزل الجلفاني الديزلكتريكي المعتمد', 'فصل بصري ومغناطيسي: صمود عزل مختبر حتى 3000 V AC لمدة دقيقة واحدة (بين كابل الدخل وأطراف الخرج)'),
        ('طريقة التغذية الكهربائية ومقاومة الحلقة', 'تغذية بسلكين عبر حلقة التيار (Loop-Powered): جهد 24V DC اسمي (نطاق 12V إلى 30V DC؛ مقاومة حمل قصوى $R_L \le 500\,\Omega$)'),
        ('زمن الاستجابة التناظرية وعرض النطاق', 'استجابة تناظرية فائقة السرعة: زمن الصعود &le; 200 مللي ثانية (عرض نطاق التردد: من 20 هرتز إلى 1 كيلوهرتز)'),
        ('هيكل الغلاف والتثبيت على سكة DIN', 'غلاف بلاستيكي هندسي ذاتي الإطفاء (UL 94 V-0)؛ تثبيت فوري على سكة DIN 35 مم أو تثبيت بالمسامير على اللوح')
    ],
    faqs=[
        ('ما هو محول إشارة التيار المتردد (AC Current Transducer) ولماذا تعجز وحدات PLC عن قراءة محولات التيار العادية؟',
         'محول إشارة التيار المتردد—والمعروف في هندسة الأتمتة والتحكم باسم مرسل التيار 4-20mA أو ترانسديوسر التيار المتردد—هو '
         'جهاز قياس إلكتروني دقيق يقيس شدة التيار المتردد المار في كابل القدرة '
         'ويحوله إلى إشارة تناظرية مستمرة منخفضة الجهد ومعزولة كهربائياً (عادةً 4–20 mA DC أو 0–10 V DC). '
         'وفي لوحات التحكم الصناعي ووحدات PLC : '
         '<ul>'
         '<li><strong>عدم توافق محولات التيار العادية:</strong> تُخرج محولات التيار التقليدية (CTs) تياراً متردداً شدته 0–5 A AC. '
         'بينما تعمل كروت المداخل التناظرية لوحدات التحكم المبرمجة PLC (مثل Siemens و Schneider و Allen-Bradley) بجهد وإشارات تيار مستمر DC فقط. '
         'وتوصيل تيار متردد 5A مباشرة بوحدة PLC يؤدي لتدمير كروت الدخل فورياً.</li>'
         '<li><strong>حل هندسي مدمج متكامل:</strong> بدلاً من تركيب محول تيار ضخم مع مكبر إشارة خارجي على سكة DIN وأسلاك معقدة، '
         'يدمج محول يمين ACT قلب التحسس المغناطيسي ودائرة إرسال 4-20mA في غلاف واحد صغير ومعاير جاهز للتوصيل.</li>'
         '</ul>'),
        ('لماذا تفضل حلقة التيار 4–20 mA على إشارة الجهد 0–10 V في البيئات الصناعية؟',
         'تعتبر حلقة التيار 4–20 mA المعيار الذهبي في الأتمتة لسببين جوهريين : '
         '<ul>'
         '<li><strong>عدم التأثر بمقاومة وطول الكابلات:</strong> تعاني إشارات الجهد (0–10 V) من هبوط الجهد ($V = I \times R$) عبر المسافات الطويلة '
         '(أكثر من 50 إلى 300 متر)، مما يشوه دقة القراءة في الـ PLC. بينما تحافظ حلقة التيار 4–20 mA على دقتها التامة بصرف النظر عن طول الكابل.</li>'
         '<li><strong>كشف قطع الأسلاك فورياً (مبدأ الصفر الحي 4mA):</strong> في إشارات الجهد، تشير قراءة 0V إلى تيار منعدم أو سلك مقطوع دون تمييز. '
         'بينما في حلقة 4–20 mA، <strong>تمثل قيمة 4mA تياراً مقداره 0%</strong>، بينما <strong>تعني قراءة 0mA انقطاع السلك فورياً فيصدر الـ PLC إنذار عطل</strong>.</li>'
         '</ul>'),
        ('ما هو الفرق بين المحولات متوسطة التعديل ومحولات القيمة الفعالة الحقيقية True-RMS؟',
         'تعتمد المحولات الرخيصة على دوائر تقويم متوسطة مخصصة للموجات الجيبية النقية فقط. '
         'ومع انتشار مغيرات السرعة (VFDs) والمحركات الحديثة، تتشوه موجات التيار بالتوافقيات، مما يولد أخطاء في القراءة تتجاوز 20% إلى 40%. '
         'تتميز محولات يمين ACT بمعالجات <strong>True-RMS (القيمة الفعالة الحقيقية)</strong> التي تحسب بدقة متناهية الطاقة الحرارية للموجة '
         'محافظةً على دقة مترولوجية &plusmn;0.5% حتى مع أشد التيارات تشوهاً.')
    ],
    cta='هل تعمل على تصميم لوحات التحكم الآلي PLC، أو مراكز التحكم بالمحركات MCC، أو منظومات SCADA التي تتطلب محولات إشارة تيار متردد True-RMS فئة دقة 0.5 (دخل من 0-10A إلى 0-500A، خرج 4-20mA DC، عزل 3kV)؟ تصنع يمين (YOMIN) محولات سلسلة ACT بأعلى معايير الدقة.',
    body='''
<h2>جسر القياس الحيوي الفاصل بين قوى التيار المتردد العالية ومعالجات PLC الدقيقة</h2>
<p>في المصانع الحديثة المؤتمتة، ومحطات معالجة وضخ المياه، وخطوط الإنتاج الروبوتية، تدير وحدات التحكم المنطقي المبرمج (PLC) ومنظومات المراقبة والتحكم SCADA مئات المحركات والمضخات والمراوح الصناعية على مدار الساعة.</p>
<p>ولمنع احتراق المحركات عند زيادة الأحمال الميكانيكية، أو رصد انسداد المضخات، أو احتساب الطاقة الكهربائية المستهلكة، يحتاج عقل الـ PLC لمعرفة التيار اللحظي الحقيقي الذي يسحبه كل محرك بدقة تامة.</p>
<p>ومع ذلك، تعمل المحركات الصناعية بجهود <strong>380V أو 440V AC</strong> وتيارات تصل إلى عشرات أو مئات الأمبيرات. ومحولات التيار التقليدية تعطي 5A AC، وهو ما تعجز كروت المداخل التناظرية لوحدات الـ PLC عن استقباله مباشرة دون احتراق.</p>
<p>يقدم <strong>محول إشارة التيار المتردد (سلسلة YM-ACT)</strong> الحل التكنولوجي المعتمد: حساس إلكتروني متكامل يقيس تيار الموصل المتردد ويحوله إلى إشارة تيار مستمر تناظرية خطية ومعزولة كهربائياً بقوة 3000 فولت (4–20 mA DC أو 0–10 V DC) لتتصل مباشرة بكروت المداخل التناظرية لوحدة الـ PLC.</p>

<h2>المكونات الهندسية وميزات الأداء لسلسلة محولات YM-ACT</h2>
<ol>
  <li><strong>قلب تحسس مغناطيسي متطور (مصمت أو مشقوق):</strong> شرائح فولاذ سيليكوني عالية النفاذية. وتتميز النماذج المشقوقة (Split-Core) بإمكانية تركيبها بالكبس المباشر حول الكابلات الحية دون الحاجة لفصل التيار الكهربائي.</li>
  <li><strong>معالج إلكتروني تناظري للقيمة الفعالة الحقيقية True-RMS:</strong> دوائر متقدمة تحسب القيمة الفعالة الدقيقة للموجة المشوهة المنبعثة من مغيرات التردد والإنفرتر VFD.</li>
  <li><strong>حاجز عزل جلفاني فائق القوة 3000 V AC:</strong> فصل بصري ومغناطيسي تام يحمي الإلكترونيات الدقيقة الحساسة للـ PLC من أي صدمات أو قصر كهربي في دوائر الجهد العالي.</li>
  <li><strong>تقنية التغذية بسلكين من حلقة التيار (Loop-Powered):</strong> يستمد المحول طاقته التشغيلية مباشرة من جهد الـ 24V DC المزود من كارت الـ PLC، ملغياً الحاجة لمصادر تغذية خارجية باللوحة.</li>
  <li><strong>تصميم مدمج يركب على سكة DIN 35 مم:</strong> هيكل بلاستيكي متين ومقاوم للهب (UL 94 V-0) يوفر مساحات اللوحة الثمينة ويتصل بسلكين فقط إلى كارت التحكم.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1017 = [
    PLC_EN, PLC_FR, PLC_ES, PLC_AR,
    ACT_EN, ACT_FR, ACT_ES, ACT_AR
]
