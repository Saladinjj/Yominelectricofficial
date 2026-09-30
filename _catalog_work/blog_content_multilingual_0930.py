# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-09-30:
1. Smart Metering Data Concentrator Unit (DCU) (EN, FR, ES, AR)
2. Medium-Voltage Automatic Circuit Recloser (ACR) (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. SMART METERING DATA CONCENTRATOR UNIT (DCU) (EN, FR, ES, AR)
# ==============================================================================

DCU_EN = dict(
    lang='en',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-data-concentrator-unit',
    title='Smart Metering Infrastructure & AMI: What Is a Data Concentrator Unit (DCU)?',
    breadcrumb='Energy Meter',
    read='10 min read',
    alt='Industrial smart meter Data Concentrator Unit (DCU) actively operating inside an outdoor distribution transformer kiosk',
    desc=('Advanced Metering Infrastructure (AMI/AMR/ASKUE) and smart grid automation: What is a Data Concentrator Unit (DCU)? '
          'How utility DCUs aggregate smart meter data over G3-PLC, RS485, and LoRaWAN, executing automated billing and power loss analytics.'),
    model='Model YM-DCU Series Smart Automated Meter Reading (AMI/AMR/ASKUE) Data Concentrator Units',
    category='Energy Meter / Data Concentrator Units',
    kw='what is a data concentrator unit &middot; data concentrator unit &middot; smart meter data concentrator &middot; dcu smart meter &middot; ami data concentrator',
    specs=[
        ('Processor Architecture & Operating System', '32-bit high-performance industrial ARM Cortex-A7/A9 core (800MHz) running embedded Linux OS with secure cryptographic root of trust'),
        ('Meter Management Capacity', 'Manages up to 1,024 single-phase smart electricity meters or 256 three-phase commercial smart meters per transformer node'),
        ('Downstream Local Area Network (LAN)', 'G3-PLC (OFDM Power Line Communication), PRIME PLC, RS485 (dual isolated channels, 1200–115200 bps), and Sub-1GHz RF / LoRaWAN wireless mesh'),
        ('Upstream Wide Area Network (WAN)', '4G LTE (Cat 4 / Cat 1 with fallback to 2G/3G), 10/100 Mbps RJ45 Ethernet port, supporting dual-SIM card automatic failover'),
        ('Standard Industrial Protocols', 'DLMS/COSEM (IEC 62056-5-3/6-1/6-2), IEC 60870-5-104, Modbus RTU/TCP, MQTT, and secure TLS 1.3 encrypted data transmission to HES/MDMS'),
        ('Memory Storage & Data Retention', '512MB DDR3 RAM, 8GB eMMC flash memory; stores up to 180 days of hourly load profile data and tamper event logs; non-volatile retention &ge; 10 years'),
        ('Power Supply & Outage Backup', 'Wide 3x220V/380V AC &plusmn;20% input; integrated supercapacitor or rechargeable lithium battery providing &ge; 5 minutes Last Gasp power outage transmission'),
        ('Environmental & Mechanical Protection', 'IP54/IP65 sealed UV-resistant polycarbonate enclosure; operating temperature range &minus;40&deg;C to +70&deg;C; 6kV impulse surge immunity per IEC 61000-4-5')
    ],
    faqs=[
        ('What is a Data Concentrator Unit (DCU) and what role does it serve in Advanced Metering Infrastructure (AMI)?',
         'A Data Concentrator Unit (DCU) is an intelligent, edge-computing gateway installed at distribution transformer kiosks or residential riser shafts '
         'that acts as the vital bridge between individual smart electricity meters and the utility Head-End System (HES). '
         'In an AMI or ASKUE network, thousands of smart meters record cumulative kilowatt-hours, instantaneous voltage, current, load profiles, and tamper events. '
         'Connecting every meter directly to cellular networks via individual SIM cards is cost-prohibitive and creates massive network congestion. '
         'The DCU solves this by managing downstream communications (Neighborhood Area Network / NAN) across hundreds of local meters using cost-free media '
         'such as Power Line Carrier (PLC) or RS485. The DCU collects, buffers, and validates meter readings automatically, compresses the data, and transmits it '
         'upstream via a single secure 4G LTE or Ethernet connection to utility billing servers.'),
        ('How does Power Line Communication (PLC) allow a DCU to communicate over existing electrical wires without extra cabling?',
         'Power Line Communication (PLC)—specifically modern OFDM standards like G3-PLC and PRIME—modulates high-frequency digital signals directly onto energized '
         '50Hz or 60Hz power distribution cables. '
         'Because every customer meter is already physically wired to the low-voltage side of the local distribution transformer, the power cable itself serves as the data conduit. '
         'The DCU injects modulated carrier signals through a capacitive coupling unit into the transformer busbars. Smart meters listening on the same phase receive the packets '
         'and reply with energy registers. Advanced G3-PLC utilizes adaptive frequency hopping and dynamic mesh routing, allowing meters acting as repeaters to forward signals '
         'past cable splices and electrical noise, completely eliminating civil excavation and communication cabling costs.'),
        ('What is the difference between automated meter reading (AMR) and advanced metering infrastructure (AMI)?',
         'The critical distinction lies in communication directionality and real-time control: '
         '<ul>'
         '<li><strong>AMR (Automated Meter Reading):</strong> A one-way communication architecture where meters broadcast energy consumption data periodically to a walk-by/drive-by '
         'receiver or simple concentrator for monthly billing. AMR cannot execute remote disconnect commands, modify tariffs, or report power outages instantly.</li>'
         '<li><strong>AMI (Advanced Metering Infrastructure):</strong> A fully automated, secure, two-way communication network powered by intelligent DCUs and cloud MDMS platforms. '
         'AMI enables real-time dynamic pricing, remote over-the-air firmware upgrades, instant power outage detection ("Last Gasp" distress signals), automated credit replenishment '
         'for STS prepayment systems, and remote load disconnect/reconnect control.</li>'
         '</ul>')
    ],
    cta='Designing utility Advanced Metering Infrastructure (AMI), automated commercial power accounting (ASKUE), or distribution transformer monitoring projects requiring certified DLMS/COSEM data concentrators? YOMIN manufactures industrial DCUs engineered to IEC 62056 standards.',
    body='''
<h2>The Critical Communications Nerve Center for Modern Smart Grids</h2>
<p>Modern electrical power utilities across Central Asia, the Middle East, Europe, and the Americas are undergoing a massive transition from manual meter reading to automated smart grids. However, deploying millions of smart electricity meters introduces a staggering data management challenge: aggregating time-of-use tariffs, reactive energy vectors, maximum demand intervals, and power quality waveforms across thousands of disparate distribution substations.</p>
<p>Deploying dedicated cellular modems in every residential meter is economically unfeasible and introduces severe SIM management vulnerabilities. The solution is the <strong>Data Concentrator Unit (DCU)</strong>—the rugged, substation-grade microcomputer that aggregates, validates, and routes meter telemetry across the distribution network.</p>

<h2>AMI Network Topology: Where the DCU Fits</h2>
<p>In a standard Advanced Metering Infrastructure (AMI) architecture, the network is organized into three distinct tiers:</p>
<ol>
  <li><strong>Home Area Network (HAN):</strong> The customer interface, connecting energy meters to in-home displays (CIU) or smart home energy management systems.</li>
  <li><strong>Neighborhood Area Network (NAN / Downstream):</strong> The local data collection loop managed by the DCU. Connecting between 100 and 1,024 smart meters to the local transformer substation via G3-PLC, RS485 shielded buses, or Sub-1GHz RF mesh.</li>
  <li><strong>Wide Area Network (WAN / Upstream):</strong> The long-distance backhaul link. The DCU encrypts batched meter data and transmits it via 4G LTE, optical fiber, or industrial Ethernet directly to the utility Head-End System (HES) and Meter Data Management System (MDMS).</li>
</ol>

<h2>Core Architecture: DCU Hardware Capabilities</h2>
<table>
  <thead>
    <tr>
      <th>System Component</th>
      <th>Legacy Concentrator Limitation</th>
      <th>YOMIN Modern Industrial AMI DCU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Processing Core</strong></td>
      <td>8-bit / 16-bit low-speed microcontroller.</td>
      <td><strong>32-bit ARM Cortex-A7 (800MHz) running Embedded Linux.</strong></td>
    </tr>
    <tr>
      <td><strong>Local Network Protocols</strong></td>
      <td>Proprietary vendor-locked serial protocols.</td>
      <td><strong>Standardized DLMS/COSEM (IEC 62056), G3-PLC, Modbus RTU.</strong></td>
    </tr>
    <tr>
      <td><strong>Upstream Backhaul</strong></td>
      <td>2G GPRS with frequent dropouts.</td>
      <td><strong>4G LTE Cat 4 with Dual-SIM auto-failover & Ethernet RJ45.</strong></td>
    </tr>
    <tr>
      <td><strong>Local Storage Capacity</strong></td>
      <td>Stores only 24 hours of daily totals.</td>
      <td><strong>8GB eMMC Flash (up to 180 days of 15-min load curves).</strong></td>
    </tr>
    <tr>
      <td><strong>Outage Alerting ("Last Gasp")</strong></td>
      <td>Powers down instantly on line outage.</td>
      <td><strong>Supercapacitor backup transmits power outage alarm to HES.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

DCU_FR = dict(
    lang='fr',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-data-concentrator-unit-fr',
    title="Infrastructure de Comptage Intelligent & AMI : Qu'est-ce qu'un Concentrateur de Données (DCU) ?",
    breadcrumb='Compteur d\'Énergie',
    read='10 min de lecture',
    alt='Concentrateur de données industriel pour compteurs communicants (DCU) en service dans un poste de transformation de distribution',
    desc=('Infrastructure de comptage avancé (AMI/AMR/ASKUE) et réseaux intelligents : Qu\'est-ce qu\'un concentrateur de données (DCU) ? '
          'Comment les concentrateurs de données agrègent les relevés des compteurs communicants via CPL G3, RS485 et LoRaWAN pour la facturation automatisée.'),
    model='Série YM-DCU : Concentrateurs de Données Intelligents pour Télé-relève et Réseaux Communicants AMI',
    category='Compteur d\'Énergie / Concentrateurs de Données',
    kw='concentrateur de données dcu &middot; concentrateur compteur communicant &middot; dcu smart meter &middot; télérelève ami &middot; concentrateur cpl g3',
    specs=[
        ('Architecture Processeur & Système d\'Exploitation', 'Cœur industriel ARM Cortex-A7/A9 32 bits (800MHz) sous Linux embarqué avec racine de confiance cryptographique'),
        ('Capacité de Gestion de Compteurs', 'Gère jusqu\'à 1 024 compteurs communicants monophasés ou 256 compteurs industriels triphasés par nœud de transformateur'),
        ('Réseau Local Aval (NAN - Local Area Network)', 'CPL G3 (Courant Porteur en Ligne OFDM), PRIME, RS485 (double canal isolé 1200–115200 bps) et radio maillée Sub-1GHz / LoRaWAN'),
        ('Réseau Étendu Amont (WAN - Wide Area Network)', '4G LTE (Cat 4 / Cat 1 avec basculement automatique 2G/3G), port Ethernet RJ45 10/100 Mbps, double emplacement carte SIM'),
        ('Protocoles Industriels Pris en Charge', 'DLMS/COSEM (CEI 62056-5-3/6-1/6-2), CEI 60870-5-104, Modbus RTU/TCP, MQTT et transmission sécurisée chiffrée TLS 1.3 vers le HES/MDMS'),
        ('Mémoire et Conservation des Données', '512 Mo RAM DDR3, 8 Go Flash eMMC ; enregistre jusqu\'à 180 jours de profils de charge horaires et journaux d\'alertes ; rétention &ge; 10 ans'),
        ('Alimentation et Secours en Cas de Coupure', 'Large plage 3x220V/380V AC &plusmn;20% ; supercondensateur intégré fournissant &ge; 5 minutes pour l\'émission de l\'alerte de panne'),
        ('Protection Environnementale et Mécanique', 'Boîtier polycarbonate étanche IP54/IP65 résistant aux UV ; plage de température &minus;40&deg;C à +70&deg;C ; immunité aux chocs 6kV (CEI 61000-4-5)')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un concentrateur de données (DCU) et quel est son rôle dans un réseau de comptage communicant (AMI) ?',
         'Un concentrateur de données (DCU - Data Concentrator Unit) est une passerelle informatique industrielle installée au niveau des postes de transformation '
         'de quartier ou des colonnes montantes d\'immeubles. Il constitue le pont de communication stratégique entre les compteurs communicants d\'abonnés et le système central de gestion de la compagnie électrique (HES/MDMS). '
         'Dans un réseau de comptage intelligent (AMI/ASKUE), des milliers de compteurs enregistrent les index de consommation, profils de charge, tensions et tentatives de fraude. '
         'Équiper chaque compteur individuel d\'une carte SIM 4G serait excessivement coûteux et saturerait le réseau cellulaire. '
         'Le DCU résout ce problème en collectant localement les données de centaines de compteurs via des médias sans coût de télécommunication, '
         'tels que le Courant Porteur en Ligne (CPL) ou le bus RS485. Le DCU valide, compresse et transmet ces index en un flux unique et sécurisé 4G ou fibre vers les serveurs de facturation.'),
        ('Comment le Courant Porteur en Ligne (CPL) permet-il au DCU de communiquer sur les câbles électriques sans câblage supplémentaire ?',
         'Le Courant Porteur en Ligne (CPL G3 ou PRIME) module des signaux numériques haute fréquence directement sur les câbles d\'énergie 50Hz/60Hz existants. '
         'Chaque compteur électrique étant déjà relié physiquement au réseau basse tension du transformateur, le câble électrique devient le vecteur de données. '
         'Le DCU injecte ses trames de données modulées dans les jeux de barres du transformateur. Les compteurs raccordés sur les mêmes phases reçoivent les paquets '
         'et renvoient leurs index de consommation. Le protocole CPL G3 gère le maillage dynamique : si un compteur distant est affaibli par le bruit électrique, '
         'les compteurs intermédiaires relaient automatiquement le signal, éliminant totalement les tranchées de génie civil et le câblage de communication.'),
        ('Quelle est la différence fondamentale entre la télé-relève (AMR) et le comptage intelligent (AMI) ?',
         'La différence réside dans la bidirectionnalité et la capacité de télécommande en temps réel : '
         '<ul>'
         '<li><strong>AMR (Automated Meter Reading) :</strong> Architecture de télé-relève unidirectionnelle où le compteur émet ses index mensuels vers un récepteur mobile '
         'ou un concentrateur simple. L\'AMR ne permet pas d\'actionner à distance le disjoncteur du compteur ni de modifier les grilles tarifaires.</li>'
         '<li><strong>AMI (Advanced Metering Infrastructure) :</strong> Réseau de comptage communicant bidirectionnel complet supervisé par des concentrateurs DCU intelligents. '
         'L\'AMI permet la tarification dynamique en temps réel, la mise à jour à distance des microprogrammes, la détection immédiate des pannes réseau (alertes "Last Gasp"), '
         'la recharge de crédit pour compteurs prépayés et la coupure/rétablissement à distance de l\'alimentation.</li>'
         '</ul>')
    ],
    cta='Vous déployez un réseau de comptage communicant (AMI), des projets de télé-relève de distribution (ASKUE) ou de monitoring de sous-stations nécessitant des concentrateurs certifiés DLMS/COSEM ? YOMIN fabrique des DCU industriels haute performance conformes aux normes CEI 62056.',
    body='''
<h2>Le Nœud Stratégique de Communication des Réseaux Électriques Modernes</h2>
<p>Les compagnies d'électricité à travers l'Asie centrale, le Moyen-Orient, l'Europe et les Amériques modernisent leurs réseaux de distribution pour éliminer les relèves manuelles et maîtriser les pertes non techniques. Cependant, le déploiement de millions de compteurs communicants soulève un défi massif : comment collecter de manière fiable les courbes de charge, puissances réactives et alarmes de fraude de centaines de milliers de points de livraison ?</p>
<p>Équiper chaque compteur individuel d'un modem cellulaire est économiquement insoutenable. La solution réside dans le <strong>Concentrateur de Données (DCU)</strong>—une passerelle industrielle durcie qui gère intelligemment la collecte locale et l'acheminement sécurisé des données vers le système central.</p>

<h2>Architecture Réseau AMI : Le Positionnement Clé du DCU</h2>
<p>Dans un réseau de comptage communicant (AMI), l'architecture s'articule en trois niveaux :</p>
<ol>
  <li><strong>Réseau Domestique (HAN) :</strong> Liaison entre le compteur communicant et l'afficheur déporté du client ou le système domotique.</li>
  <li><strong>Réseau de Quartier (NAN - Downstream) :</strong> La boucle de collecte locale gérée par le DCU. Il relie 100 à 1 024 compteurs au poste transformateur via CPL G3, bus RS485 ou réseau radio maillé LoRaWAN.</li>
  <li><strong>Réseau Métropolitain (WAN - Upstream) :</strong> La liaison longue distance. Le DCU compresse et chiffre les données pour les transmettre en 4G LTE ou Ethernet vers le système central HES/MDMS de la compagnie électrique.</li>
</ol>
'''
)

DCU_ES = dict(
    lang='es',
    dir='ltr',
    slug='smart-metering-infrastructure-what-is-a-data-concentrator-unit-es',
    title='Infraestructura de Medición Inteligente y AMI: ¿Qué es una Unidad Concentradora de Datos (DCU)?',
    breadcrumb='Medidor de Energía',
    read='10 min de lectura',
    alt='Unidad concentradora de datos industrial para medidores inteligentes (DCU) operando dentro de un centro de transformación de distribución',
    desc=('Infraestructura de medición avanzada (AMI/AMR/ASKUE) y redes inteligentes: ¿Qué es una unidad concentradora de datos (DCU)? '
          'Cómo los concentradores DCU agregan datos de medidores inteligentes mediante PLC G3, RS485 y LoRaWAN, permitiendo facturación automática.'),
    model='Serie YM-DCU: Unidades Concentradoras de Datos Inteligentes para Redes de Telemedición AMI',
    category='Medidor de Energía / Unidades Concentradoras de Datos',
    kw='unidad concentradora de datos &middot; dcu medidor inteligente &middot; concentrador ami &middot; telemedición eléctrica &middot; concentrador plc g3',
    specs=[
        ('Arquitectura de Procesamiento y Sistema Operativo', 'Núcleo industrial ARM Cortex-A7/A9 de 32 bits (800MHz) con sistema operativo Linux embebido y cifrado criptográfico'),
        ('Capacidad de Gestión de Medidores', 'Gestiona hasta 1.024 medidores inteligentes monofásicos o 256 medidores comerciales trifásicos por nodo de transformador'),
        ('Red de Área Local de Medición (NAN - Downstream)', 'PLC G3 (Comunicación por Línea Eléctrica OFDM), PRIME, RS485 (doble canal aislado 1200–115200 bps) y radio mallada Sub-1GHz / LoRaWAN'),
        ('Red de Área Amplia de Retransmisión (WAN - Upstream)', '4G LTE (Cat 4 / Cat 1 con conmutación automática a 2G/3G), puerto Ethernet RJ45 10/100 Mbps, doble ranura para tarjeta SIM'),
        ('Protocolos Estándar Compatibles', 'DLMS/COSEM (IEC 62056-5-3/6-1/6-2), IEC 60870-5-104, Modbus RTU/TCP, MQTT y transmisión segura cifrada TLS 1.3 hacia HES/MDMS'),
        ('Capacidad de Almacenamiento y Registro', '512MB RAM DDR3, 8GB Flash eMMC; almacena hasta 180 días de curvas de carga horarias y registros de fraude; retención no volátil &ge; 10 años'),
        ('Fuente de Alimentación y Respaldo por Falla', 'Rango amplio 3x220V/380V AC &plusmn;20%; supercondensador integrado que provee &ge; 5 minutos para emitir alarma de corte de energía'),
        ('Protección Mecánica y Ambiental', 'Gabinete hermético de policarbonato IP54/IP65 resistente a radiación UV; temperatura &minus;40&deg;C a +70&deg;C; inmunidad al impulso 6kV (IEC 61000-4-5)')
    ],
    faqs=[
        ('¿Qué es una Unidad Concentradora de Datos (DCU) y qué función cumple en la medición avanzada (AMI)?',
         'Una Unidad Concentradora de Datos (DCU - Data Concentrator Unit) es una pasarela informática industrial instalada en transformadores de distribución '
         'o cuartos de medidores en edificios. Actúa como el puente de enlace fundamental entre los medidores inteligentes de los usuarios y el sistema central de la empresa eléctrica (HES/MDMS). '
         'En una red AMI o de telemedición automática, miles de medidores registran consumos, voltajes, perfiles de carga y alarmas de manipulación. '
         'Dotar a cada medidor de un módem celular individual resultaría prohibitivo en costos operativos y saturaría las redes móviles. '
         'La DCU soluciona este cuello de botella administrando la red local de medidores a través de tecnologías sin costo recurrente de comunicación, '
         'como la Comunicación por Línea de Potencia (PLC) o bus RS485. La DCU recopila, valida y comprime las lecturas, enviándolas en un paquete único y seguro por 4G o fibra.'),
        ('¿Cómo funciona la Comunicación por Línea Eléctrica (PLC) para transmitir datos sin cables adicionales?',
         'La tecnología PLC (especialmente protocolos OFDM avanzados como G3-PLC o PRIME) modula señales digitales de alta frecuencia directamente sobre los conductores '
         'de distribución de energía de 50Hz o 60Hz existentes. '
         'Dado que cada medidor ya está físicamente conectado a la red eléctrica del transformador, el cable de potencia funciona como canal de datos. '
         'La DCU inyecta los paquetes de datos a través de un acoplador capacitivo en las barras del transformador. Los medidores conectados reciben las tramas y responden con sus indexaciones. '
         'El protocolo G3-PLC implementa enrutamiento mallado dinámico: si un medidor lejano sufre atenuación, los medidores intermedios actúan como repetidores automáticos.'),
        ('¿Cuál es la diferencia entre la telemedición básica (AMR) y la infraestructura avanzada (AMI)?',
         'La diferencia radica en la bidireccionalidad de las comunicaciones y el control remoto en tiempo real: '
         '<ul>'
         '<li><strong>AMR (Automated Meter Reading):</strong> Sistema unidireccional donde los medidores transmiten lecturas acumuladas a un receptor móvil (drive-by) '
         'o concentrador simple exclusivamente para facturación mensual. No permite enviar comandos remotos de corte o cambio de tarifas.</li>'
         '<li><strong>AMI (Advanced Metering Infrastructure):</strong> Red bidireccional inteligente de ciclo completo gestionada por concentradores DCU. '
         'Permite aplicar tarifas horarias dinámicas, actualizar firmware de manera remota, detectar cortes de suministro en tiempo real (alertas "Last Gasp"), '
         'recargar crédito en medidores prepagos STS y desconectar/reconectar el suministro eléctrico a distancia.</li>'
         '</ul>')
    ],
    cta='¿Diseña proyectos de Infraestructura de Medición Avanzada (AMI), balance de energía en transformadores o telemetría de distribución eléctrica que requieren concentradores certificados DLMS/COSEM? YOMIN fabrica DCUs industriales de alta confiabilidad bajo normas IEC 62056.',
    body='''
<h2>El Centro Neurálgico de Comunicaciones en las Redes Eléctricas Inteligentes</h2>
<p>Las empresas distribuidoras de electricidad en América Latina, Asia Central, Europa y Oriente Medio están reemplazando masivamente los medidores electromagnéticos tradicionales por redes inteligentes de telemedición. Sin embargo, la gestión de millones de puntos de medida introduce un inmenso desafío: ¿cómo recolectar curvas de carga horarias, balance de energía por transformador y alarmas de fraude de forma confiable y económica?</p>
<p>Instalar tarjetas SIM celulares individuales en cada medidor residencial no es viable financieramente. La solución de ingeniería estándar es la <strong>Unidad Concentradora de Datos (DCU)</strong>—un equipo industrial robusto que administra la red local de medidores y consolida la información para enviarla a los servidores centrales.</p>

<h2>Arquitectura de Red AMI: El Rol Clave de la DCU</h2>
<p>En una infraestructura de medición avanzada (AMI), los sistemas se estructuran en tres niveles:</p>
<ol>
  <li><strong>Red de Área Hogar (HAN):</strong> Conecta el medidor con monitores para el usuario o sistemas de gestión energética domiciliaria.</li>
  <li><strong>Red de Área Vecinal (NAN - Downstream):</strong> La red de recolección local administrada por la DCU. Agrupa entre 100 y 1.024 medidores en torno al transformador mediante PLC G3, bus RS485 o radioenlace LoRaWAN.</li>
  <li><strong>Red de Área Amplia (WAN - Upstream):</strong> El enlace de retorno hacia la nube. La DCU cifra los paquetes de datos y los envía por 4G LTE o Ethernet directamente al sistema HES/MDMS de la distribuidora eléctrica.</li>
</ol>
'''
)

DCU_AR = dict(
    lang='ar',
    dir='rtl',
    slug='smart-metering-infrastructure-what-is-a-data-concentrator-unit-ar',
    title='البنية التحتية للعدادات الذكية وأنظمة AMI: ما هي وحدة تجميع البيانات (DCU)؟',
    breadcrumb='عداد الطاقة الكهربائية',
    read='10 دقائق قراءة',
    alt='وحدة تجميع بيانات صناعية للعدادات الذكية تعمل داخل كشك محول توزيع كهربائي خارجي',
    desc=('البنية التحتية المتقدمة للعدادات (AMI/AMR/ASKUE) وشبكات الكهرباء الذكية: ما هي وحدة تجميع البيانات (DCU)؟ '
          'كيف تجمع وحدات DCU بيانات العدادات الذكية عبر كابلات القدرة (G3-PLC) و RS485 و LoRaWAN لتحقيق الفوترة الآلية ومكافحة الفاقد.'),
    model='سلسلة YM-DCU: وحدات تجميع البيانات الذكية لأنظمة القراءة الآلية والشبكات المتقدمة AMI',
    category='عدادات الطاقة / وحدات تجميع البيانات DCU',
    kw='وحدة تجميع البيانات dcu &middot; مجمع العدادات الذكية &middot; dcu smart meter &middot; قراءة العدادات عن بعد ami &middot; كابلات القدرة g3-plc',
    specs=[
        ('معمارية المعالج ونظام التشغيل', 'معالج صناعي عالي الأداء 32 بت ARM Cortex-A7 (تردد 800 ميجاهرتز) يعمل بنظام Linux مدمج مع تشفير متكامل'),
        ('سعة إدارة العدادات التابعة', 'إدارة ما يصل إلى 1,024 عداداً أحادي الطور أو 256 عداداً تجارياً ثلاثي الطور لكل محول توزيع كهربائي'),
        ('شبكة الجمع المحلية (NAN - Downstream)', 'تقنية نقل البيانات عبر كابلات الكهرباء G3-PLC، PRIME، ومنفذ RS485 مزدوج معزول، وشبكة راديو لاسلكية LoRaWAN'),
        ('شبكة النقل المركزية (WAN - Upstream)', 'اتصال خلوي 4G LTE مع التبديل التلقائي لشبكات 2G/3G، ومنفذ إيثرنت RJ45، ودعم شريحتي اتصال Dual-SIM للنسخ الاحتياطي'),
        ('البروتوكولات القياسية المعتمدة', 'بروتوكول DLMS/COSEM (معايير IEC 62056)، IEC 60870-5-104، Modbus RTU/TCP، ونقل بيانات مشفر وفق معيار TLS 1.3'),
        ('الذاكرة وسعة تسجيل البيانات', 'ذاكرة رام 512MB DDR3، وسعة تخزين فلاش 8GB eMMC؛ تخزين منحنيات الأحمال اليومية وسجلات العبث لمدة 180 يوماً متواصلة'),
        ('تغذية القدرة والاحتياطي عند انقطاع التيار', 'نطاق واسع 3x220V/380V AC &plusmn;20%؛ مكثف فائق سعة (Supercapacitor) مدمج يوفر &ge; 5 دقائق لإرسال إشارة انقطاع التغذية'),
        ('الحماية البيئية والميكانيكية', 'هيكل بولي كربونات محكم ومقاوم للأشعة فوق البنفسجية بدرجة حماية IP54/IP65؛ حرارة تشغيل من &minus;40 إلى +70 مئوية؛ مناعة صواعق 6kV')
    ],
    faqs=[
        ('ما هي وحدة تجميع البيانات (DCU) وما هو دورها الحيوي في منظومة العدادات الذكية المتقدمة (AMI)؟',
         'وحدة تجميع البيانات (Data Concentrator Unit - DCU) هي بوابة حاسوبية صناعية متطورة تُثبت عند محولات التوزيع الفرعية أو غرف الكهرباء الرئيسية. '
         'تمثل هذه الوحدة همزة الوصل الاستراتيجية بين آلاف العدادات الذكية المنتشرة لدى المستهلكين والمنظومة المركزية لإدارة العدادات (HES/MDMS) لدى شركة الكهرباء. '
         'في شبكات العدادات الذكية (AMI/ASKUE)، تسجل العدادات استهلاك الكيلوواط ساعي، وتغيرات الجهد، ومنحنيات الأحمال، ومحاولات التلاعب. '
         'إن تزويد كل عداد فردي بشريحة اتصال خلوية 4G يتطلب تكاليف اشتراك شهرية باهظة ويسبب ازدحاماً هائلاً في شبكات الاتصالات. '
         'تحل وحدة DCU هذه المشكلة عبر إدارة الاتصالات المحلية مع مئات العدادات مجاناً باستخدام كابلات الكهرباء ذاتها (G3-PLC) أو خطوط RS485. '
         'تقوم الوحدة بجمع القراءات محلياً، والتأكد من صحتها، وضغطها، ثم إرسالها بحزمة موحدة وآمنة عبر اتصال 4G واحد إلى خوادم الفوترة المركزية.'),
        ('كيف تعمل تقنية الاتصال عبر كابلات الكهرباء (PLC) لنقل القراءات دون الحاجة لأي كابلات إضافية؟',
         'تعتمد تقنية نقل البيانات عبر كابلات القدرة (مثل G3-PLC أو PRIME) على تضمين إشارات رقمية عالية التردد مباشرة فوق موجة التيار الكهربائي الأساسية (50/60 هرتز). '
         'وبما أن كل عداد كهربائي متصل بالفعل بأسلاك المحول المحلي المغذي للمبنى، فإن كابل الكهرباء نفسه يعمل كخط نقل بيانات عالي السرعة. '
         'تقوم وحدة DCU بحقن الإشارات المعدلة في قضبان المحول، لتستقبلها العدادات المرتبطة على نفس الأطوار وتجيب بإرسال سجلات الاستهلاك. '
         'تتميز أنظمة G3-PLC الحديثة بالتوجيه الشبكي الذكي (Mesh Routing)؛ فإذا تعذر وصول الإشارة لعداد بعيد، تقوم العدادات الوسيطة بإعادة إرسال الإشارة تلقائياً.'),
        ('ما هو الفرق الأساسي بين القراءة الآلية التقليدية (AMR) والبنية التحتية المتقدمة (AMI)؟',
         'يكمن الفارق الجوهري في اتجاه الاتصال والقدرة على التحكم والتشغيل الفوري عن بُعد: '
         '<ul>'
         '<li><strong>القراءة الآلية (AMR):</strong> شبكة اتصالات أحادية الاتجاه يقتصر دورها على إرسال بيانات الاستهلاك من العداد إلى قارئ متنقل أو مجمع بسيط '
         'لإصدار الفاتورة الشهرية، دون القدرة على إرسال أوامر عكسية أو رصد انقطاعات الشبكة فوراً.</li>'
         '<li><strong>البنية التحتية المتقدمة (AMI):</strong> شبكة اتصالات ثنائية الاتجاه فائقة الذكاء تديرها وحدات DCU المركزية. '
         'تتيح تطبيق تسعيرات استهلاك متغيرة حسب الوقت (TOU)، وتحديث برمجيات العدادات عن بُعد، ورصد الانقطاعات الكهربائية لحظياً (إنذارات "Last Gasp")، '
         'وشحن رصيد عدادات الدفع المسبق، وفصل وإعادة توصيل الخدمة كهربائياً بنقرة زر من مركز التحكم.</li>'
         '</ul>')
    ],
    cta='هل تخطط لتنفيذ مشروعات البنية التحتية المتقدمة للعدادات الذكية (AMI)، أو أنظمة القراءة الآلية (ASKUE)، أو مراقبة محولات التوزيع الفرعية وتتطلب مجمعات بيانات معتمدة وفق معيار DLMS/COSEM؟ تصنع يمين (YOMIN) وحدات DCU صناعية متوافقة مع معايير IEC 62056.',
    body='''
<h2>العصب المركزي للاتصالات في شبكات الطاقة الكهربائية الذكية</h2>
<p>تتسابق شركات ومؤسسات توزيع الكهرباء في آسيا الوسطى والشرق الأوسط وأوروبا والأمريكتين لتحديث شبكاتها والتحول نحو العدادات الذكية للقضاء التام على القراءات اليدوية والحد من الفواقد غير الفنية الناتجة عن التلاعب والسرقات. غير أن نشر ملايين العدادات الذكية يفرض تحدياً لوجستياً هائلاً: كيف يمكن جمع آلاف منحنيات الأحمال، وسجلات الطاقة غير الفعالة، والإنذارات الفورية بكفاءة وتكلفة اقتصادية؟</p>
<p>إن تزويد كل عداد بشريحة اتصال هاتفية يمثل عبئاً مالياً وإدارياً غير مستدام. وتكمن الإجابة الهندسية المعتمدة عالمياً في <strong>وحدة تجميع البيانات (Data Concentrator Unit - DCU)</strong>—البوابة الذكية الصلبة التي تدير حلقة جمع البيانات المحلية وتنظم تدفقها الآمن إلى خوادم الإدارة المركزية.</p>

<h2>موقع وحدة DCU في طوبولوجيا شبكات العدادات الذكية (AMI)</h2>
<p>في الشبكات الذكية المتقدمة، تنتظم الاتصالات في ثلاثة مستويات رئيسية:</p>
<ol>
  <li><strong>شبكة النطاق المنزلي (HAN):</strong> ربط العداد الذكي بشاشة العرض الداخلية للعميل (CIU) أو أنظمة إدارة الطاقة المنزلية.</li>
  <li><strong>شبكة الجمع المحلية (NAN - Downstream):</strong> الحلقة المحلية التي تديرها وحدة DCU، حيث تربط بين 100 و 1,024 عداداً بمحول التوزيع عبر كابلات الكهرباء G3-PLC أو خطوط RS485 أو موجات الراديو اللاسلكية LoRaWAN.</li>
  <li><strong>الشبكة المركزية الموسعة (WAN - Upstream):</strong> خط الاتصال البعيد الذي تنقل عبره وحدة DCU البيانات المجمعة والمشفرة عبر تقنية 4G LTE أو الإيثرنت إلى المنظومة المركزية لشركة الكهرباء (HES/MDMS).</li>
</ol>
'''
)

# ==============================================================================
# 2. MEDIUM-VOLTAGE AUTOMATIC CIRCUIT RECLOSER (ACR) (EN, FR, ES, AR)
# ==============================================================================

ACR_EN = dict(
    lang='en',
    dir='ltr',
    slug='feeder-automation-what-is-an-auto-recloser',
    title='Distribution Feeder Grid Automation: What Is an Auto Recloser?',
    breadcrumb='Fuse &amp; Protection',
    read='10 min read',
    alt='Pole-mounted medium-voltage vacuum automatic circuit recloser (ACR) operating on an overhead distribution power line',
    desc=('Medium-voltage overhead distribution feeder automation and reliability: What is an auto recloser (ACR)? '
          'How vacuum automatic circuit reclosers clear transient faults (ANSI 79), prevent extended blackouts, and reduce SAIDI/SAIFI indices.'),
    model='Model ZW32 / ZW20 Series 11kV, 24kV & 36kV Outdoor Vacuum Automatic Circuit Reclosers (ACR)',
    category='Fuse & Protection / Automatic Circuit Reclosers',
    kw='what is an auto recloser &middot; auto recloser &middot; automatic circuit recloser &middot; 11kv auto recloser &middot; pole mounted recloser &middot; feeder automation',
    specs=[
        ('Rated Voltage & System Frequency', 'Rated nominal voltage 12kV, 24kV, and 36kV; maximum continuous operating voltage up to 40.5kV; system frequency 50Hz / 60Hz'),
        ('Insulation & Impulse Levels', 'Power frequency withstand voltage (dry/wet) 42kV/34kV (12kV) and 95kV/80kV (36kV); lightning impulse withstand (BIL) 75kV / 125kV / 170kV'),
        ('Rated Continuous Current & Breaking Capacity', 'Continuous current 630A and 1250A; rated short-circuit interrupting current 12.5 kA, 16 kA, and 20 kA (tested up to 25 kA at 12kV)'),
        ('Arc Quenching Technology & Bushings', 'High-vacuum ceramic interrupters housed within outdoor weather-sealed solid dielectric epoxy resin or cycloaliphatic silicone rubber poles'),
        ('Operating Mechanism & Actuator', 'Permanent magnetic actuator (PMA) or heavy-duty motor-charged spring mechanism with manual trip handle and emergency mechanical lockout'),
        ('Reclosing Sequence & Timings (ANSI 79)', 'Configurable up to 4 reclosing operations; standard operating cycle: O &minus; 0.3s &minus; CO &minus; 2s &minus; CO &minus; 2s &minus; CO &minus; Lockout'),
        ('Intelligent Controller & Telemetry (FTU/RTU)', 'Microprocessor-based Feeder Terminal Unit (FTU) supporting DNP3.0, IEC 60870-5-101/104, Modbus RTU, directional overcurrent, and sensitive earth fault (SEF)'),
        ('Mechanical & Electrical Durability', 'Class M2 mechanical endurance (&ge; 10,000 operations without maintenance); Class E2 electrical endurance at full short-circuit current; IP65 controller')
    ],
    faqs=[
        ('What is an Auto Recloser (Automatic Circuit Recloser) and how does it prevent prolonged power outages?',
         'An Auto Recloser—formally termed an Automatic Circuit Recloser (ACR)—is a medium-voltage, pole-mounted electrical switchgear apparatus '
         'engineered to detect and interrupt short-circuit fault currents and automatically reclose the distribution circuit after a programmed delay. '
         'Electrical engineering field studies reveal that **over 80% to 90% of overhead distribution line faults are transient in nature**, '
         'caused by wind-blown tree branches brushing conductors, lightning flashovers across insulators, bird or animal contacts, or wind-induced line gallops. '
         'When a conventional circuit breaker or fuse operates during a transient fault, the entire distribution feeder remains blacked out until a utility line crew '
         'drives out to manually inspect the line and replace the fuse. '
         'An auto recloser trips within 30 to 45 milliseconds to extinguish the fault arc, waits a fraction of a second (e.g. 300ms) for the ionized air to deionize and the branch to drop away, '
         'and automatically restores power. Customers experience only a momentary light flicker instead of an hours-long outage.'),
        ('How does the ANSI 79 reclosing operating sequence (O &minus; 0.3s &minus; CO &minus; 2s &minus; CO) clear temporary faults while isolating permanent failures?',
         'The intelligent controller follows a precise multi-shot reclosing sequence configured per utility protection philosophy: '
         '<ul>'
         '<li><strong>First Trip (Fast Operation - 30ms):</strong> The recloser opens instantly to clear the fault current before downstream line fuses can melt. '
         'It pauses for an initial "dead time" (typically 0.3 seconds / 300ms) to allow the temporary arc channel to disperse.</li>'
         '<li><strong>First Reclose (0.3s):</strong> The vacuum contacts reclose. If the fault was temporary (e.g. tree branch fell clear), the feeder remains energized and normal service resumes.</li>'
         '<li><strong>Subsequent Delayed Shots (e.g. 2s pause):</strong> If the fault persists, the controller trips and recloses 1 to 3 more times using time-overcurrent curves '
         'to coordinate with downstream sectionalizers and fuses.</li>'
         '<li><strong>Lockout:</strong> If the fault remains energized after the programmed attempts (indicating a permanent failure like a downed conductor or broken pole), '
         'the recloser locks open (Lockout), isolating the faulted section and sending an automated SCADA alert to dispatch crews.</li>'
         '</ul>'),
        ('What is the difference between an Auto Recloser (ACR) and a Sectionalizer on overhead lines?',
         'The critical distinction lies in fault breaking capacity: '
         'An **Auto Recloser** is a fully rated circuit breaker capable of interrupting full short-circuit currents (e.g. 12.5kA–20kA) under high voltage. '
         'A **Sectionalizer** is a lighter switch that cannot interrupt fault currents; it counts the reclosing shots of an upstream recloser during the de-energized "dead time" '
         'and opens automatically while no current is flowing to isolate a specific branch spur before the main recloser executes its final lockout.')
    ],
    cta='Designing overhead medium-voltage distribution feeder automation, rural electrification reliability upgrades, or smart grid SCADA projects requiring 11kV–36kV vacuum auto reclosers? YOMIN manufactures intelligent ACRs tested to IEC 62271-111 and ANSI C37.60 standards.',
    body='''
<h2>Eliminating 80% of Overhead Power Outages with Intelligent Feeder Automation</h2>
<p>Medium-voltage overhead distribution networks—operating from 11kV to 36kV across rural, suburban, and industrial feeder lines—represent the front line of power grid vulnerability. Exposed to windstorms, lightning surges, ice loads, and wildlife, overhead power lines experience thousands of transient electrical faults every year.</p>
<p>Historically, when a temporary fault occurred, upstream substation breakers or pole-mounted expulsion fuse cutouts disconnected the entire feeder, stranding hospitals, manufacturing plants, and residential communities in hours-long blackouts until repair crews patrolled the line.</p>
<p>The <strong>Automatic Circuit Recloser (ACR / Auto Recloser)</strong> is the foundational apparatus of modern distribution feeder automation, combining high-speed vacuum interruption, intelligent microprocessor protection, and automated reclosing sequences to restore power in milliseconds.</p>

<h2>ANSI 79 Operating Mechanism: The Psychology of Fast vs. Delayed Reclosing</h2>
<p>The true genius of the auto recloser lies in its programmable multi-shot coordination sequence, standardized under ANSI device number 79:</p>
<ol>
  <li><strong>Shot 1 (Instantaneous Fast Trip):</strong> When current exceeds the pickup threshold, the vacuum interrupter contacts open within 35 milliseconds. The breaker holds open for 0.3 seconds ("dead time") to allow air deionization, then recloses. If the fault has cleared, power is restored instantly.</li>
  <li><strong>Shot 2 & 3 (Time-Delayed Trips):</strong> If current spikes again, the microprocessor switches to time-inverse overcurrent curves (e.g. IEEE Very Inverse). This intentional time delay allows downstream spur fuses to blow and isolate branch faults locally without tripping the entire feeder.</li>
  <li><strong>Lockout (Permanent Fault Isolation):</strong> If the fault persists after the final attempt (typically 3 or 4 operations), the mechanism locks open permanently, protecting distribution transformers from thermal destruction and transmitting real-time fault distance telemetry via SCADA to utility dispatchers.</li>
</ol>

<h2>Comparison: Fuse Cutout vs. Sectionalizer vs. Automatic Circuit Recloser</h2>
<table>
  <thead>
    <tr>
      <th>Engineering Feature</th>
      <th>Expulsion Drop-Out Fuse Cutout</th>
      <th>Loadbreak Sectionalizer</th>
      <th>Automatic Circuit Recloser (ACR)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Fault Breaking Capacity</strong></td>
      <td>Single-shot expulsion link melting.</td>
      <td>Cannot break fault current (zero Isc).</td>
      <td><strong>Full vacuum breaking capacity (12.5kA to 20kA).</strong></td>
    </tr>
    <tr>
      <td><strong>Post-Fault Operation</strong></td>
      <td>Drops open; requires manual replacement.</td>
      <td>Opens during upstream dead time.</td>
      <td><strong>Automatically recloses up to 4 times (ANSI 79).</strong></td>
    </tr>
    <tr>
      <td><strong>Response to Transient Faults</strong></td>
      <td>Causes prolonged customer blackout.</td>
      <td>Dependent on upstream recloser shots.</td>
      <td><strong>Clears fault in 300ms without customer outage.</strong></td>
    </tr>
    <tr>
      <td><strong>SCADA / Telemetry Integration</strong></td>
      <td>None (mechanical gravity drop-out).</td>
      <td>Basic contact status.</td>
      <td><strong>Full DNP3 / IEC 60870-5-104 smart grid telemetry.</strong></td>
    </tr>
    <tr>
      <td><strong>Impact on Utility SAIDI / SAIFI</strong></td>
      <td>High outage duration and frequency.</td>
      <td>Moderate sectionalizing improvement.</td>
      <td><strong>Reduces permanent customer outages by up to 80%.</strong></td>
    </tr>
  </tbody>
</table>
'''
)

ACR_FR = dict(
    lang='fr',
    dir='ltr',
    slug='feeder-automation-what-is-an-auto-recloser-fr',
    title="Automatisation des Réseaux Moyenne Tension : Qu'est-ce qu'un Réenclencheur Automatique ?",
    breadcrumb='Fusibles &amp; Protection',
    read='10 min de lecture',
    alt='Réenclencheur automatique à vide moyenne tension monté sur poteau en service sur une ligne aérienne de distribution',
    desc=('Automatisation des lignes aériennes moyenne tension et fiabilité du réseau : Qu\'est-ce qu\'un réenclencheur automatique (ACR) ? '
          'Comment les disjoncteurs réenclencheurs éliminent les défauts fugitifs (ANSI 79) et réduisent drastiquement les indices de coupure SAIDI/SAIFI.'),
    model='Série ZW32 / ZW20 : Disjoncteurs Réenclencheurs Automatiques Moyenne Tension à Vide (11kV–36kV)',
    category='Fusibles & Protection / Réenclencheurs Automatiques',
    kw='réenclencheur automatique &middot; disjoncteur réenclencheur &middot; réenclencheur 11kv 33kv &middot; réenclencheur sur poteau &middot; automatisation réseau aérien',
    specs=[
        ('Tension Nominale et Fréquence Réseau', 'Tension assignée 12kV, 24kV et 36kV ; tension maximale de service jusqu\'à 40,5kV ; fréquence industrielle 50Hz / 60Hz'),
        ('Niveaux d\'Isolement et Tenue aux Chocs', 'Tension de tenue à fréquence industrielle 42kV/54kV/95kV ; onde de choc de foudre (BIL) 75kV / 125kV / 170kV'),
        ('Courant Assigné et Pouvoir de Coupure', 'Courant de service continu 630A et 1250A ; pouvoir de coupure en court-circuit 12,5 kA, 16 kA et 20 kA (testé jusqu\'à 25 kA sous 12kV)'),
        ('Technologie de Coupure & Isolateurs', 'Ampoules de coupure sous vide protégées dans des pôles en résine cycloaliphatique ou silicone résistant aux intempéries'),
        ('Actionneur et Mécanisme de Commande', 'Actionneur magnétique permanent (PMA) ou mécanisme à ressort motorisé avec commande mécanique d\'ouverture d\'urgence'),
        ('Cycles de Réenclenchement (Code ANSI 79)', 'Cycle paramétrable jusqu\'à 4 réenclenchements : O &minus; 0,3s &minus; FO &minus; 2s &minus; FO &minus; 2s &minus; FO &minus; Verrouillage'),
        ('Contrôleur Électronique Numérique (FTU)', 'Coffret de contrôle communicant sur microprocesseur supportant DNP3, CEI 60870-5-104, surintensité directionnelle et terre sensible (SEF)'),
        ('Endurance Mécanique et Électrique', 'Classe M2 pour l\'endurance mécanique (&ge; 10 000 manœuvres sans entretien) ; Classe E2 à pleine intensité de court-circuit')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un réenclencheur automatique (ACR) et comment évite-t-il les pannes de courant prolongées ?',
         'Un réenclencheur automatique—souvent appelé disjoncteur réenclencheur sur poteau—est un appareil de coupure moyenne tension extérieur '
         'capable d\'interrompre les courants de court-circuit et de refermer automatiquement le circuit après une temporisation programmée. '
         'Les statistiques des distributeurs d\'énergie démontrent que **plus de 80 % à 90 % des défauts sur les lignes aériennes sont fugitifs ou transitoires**, '
         'provoqués par des branches touchant momentanément les câbles sous l\'effet du vent, des amorçages de foudre ou des contacts d\'oiseaux. '
         'Avec un disjoncteur ou un fusible classique, la ligne reste coupée jusqu\'à l\'intervention d\'une équipe de dépannage. '
         'Le réenclencheur automatique ouvre le circuit en 30 millisecondes pour éteindre l\'arc, attend quelques fractions de seconde que l\'air se désionise, '
         'et referme le contact. Les usagers ne perçoivent qu\'un micro-clignotement au lieu d\'une panne de plusieurs heures.'),
        ('Comment fonctionne la séquence de réenclenchement ANSI 79 pour éliminer les défauts passagers sans risquer d\'aggraver les défauts permanents ?',
         'Le contrôleur numérique applique une séquence intelligente de plusieurs cycles d\'ouverture/fermeture : '
         '<ul>'
         '<li><strong>Premier déclenchement instantané (30ms) :</strong> Le réenclencheur coupe immédiatement le courant de défaut avant la fusion des fusibles avals. '
         'Il attend un "temps mort" de 0,3 seconde pour que la branche d\'arbre tombe ou que l\'arc s\'éteigne.</li>'
         '<li><strong>Premier réenclenchement (0,3s) :</strong> Les contacts sous vide se referment. Si le défaut a disparu, la distribution reprend normalement.</li>'
         '<li><strong>Déclenchements temporisés suivants (2s) :</strong> Si le défaut persiste, l\'appareil réenclenche encore 1 à 3 fois avec temporisation pour permettre '
         'aux fusibles de dérivation de ségréguer le défaut localement.</li>'
         '<li><strong>Verrouillage ouvert (Lockout) :</strong> Si le défaut subsiste (câble au sol, isolateur brisé), le réenclencheur se verrouille définitivement en position ouverte '
         'et envoie une alerte SCADA pour guider les équipes de maintenance.</li>'
         '</ul>'),
        ('Quelle est la différence entre un réenclencheur automatique et un interrupteur sectionnaliseur sur ligne aérienne ?',
         'La différence fondamentale réside dans le pouvoir de coupure en court-circuit : '
         'Le **réenclencheur automatique** est un véritable disjoncteur capable de couper un court-circuit franc de 12,5kA à 20kA sous haute tension. '
         'Le **sectionnaliseur** ne peut pas couper de courant de court-circuit : il compte les déclenchements du réenclencheur amont et s\'ouvre uniquement pendant '
         'le temps mort sans courant pour isoler une branche défaillante avant le verrouillage final.')
    ],
    cta='Vous modernisez des lignes aériennes de distribution rurale, des projets d\'automatisation moyenne tension 11kV–36kV ou des postes sources nécessitant des réenclencheurs communicants ? YOMIN fabrique des réenclencheurs automatiques sous vide certifiés CEI 62271-111.',
    body='''
<h2>Éliminer 80% des Coupures sur Réseaux Aériens grâce à l'Automatisation de Ligne</h2>
<p>Les réseaux de distribution aérienne moyenne tension—fonctionnant de 11kV à 36kV à travers les zones rurales et périurbaines—sont particulièrement vulnérables aux aléas climatiques : tempêtes, foudre, neige collante et végétation.</p>
<p>Historiquement, au moindre coup de vent rabattant une branche sur les conducteurs, les fusibles à expulsion fondaient ou le disjoncteur du poste source s'ouvrait, plongeant des cantons entiers dans le noir pendant plusieurs heures jusqu'au remplacement manuel des cartouches.</p>
<p>Le <strong>Réenclencheur Automatique à Vide (ACR)</strong> constitue l'appareil d'automatisation réseau par excellence : il détecte les surintensités, coupe le courant de court-circuit en quelques millisecondes et rétablit l'alimentation automatiquement dès disparition du défaut fugitif.</p>

<h2>La Séquence de Déclenchement ANSI 79 : Une Stratégie de Protection Éprouvée</h2>
<p>L'intelligence du réenclencheur repose sur son cycle d'ouverture et de refermeture coordonné :</p>
<ol>
  <li><strong>Déclenchement Rapide (30ms) :</strong> Dès dépassement du seuil de courant, l'ampoule à vide s'ouvre. La coupure intervient en 30ms, évitant la fusion des fusibles en aval. L'appareil observe un temps mort de 300ms pour dissiper l'arc, puis se referme.</li>
  <li><strong>Déclenchements Temporisés (2s) :</strong> Si le court-circuit persiste, le contrôleur bascule sur des courbes à temps inverse, laissant le temps aux protections secondaires de couper le départ défectueux.</li>
  <li><strong>Verrouillage Ouvert (Lockout) :</strong> En présence d'un défaut permanent (arbre couché sur la ligne), le réenclencheur se verrouille en position ouverte pour isoler le tronçon et transmet les coordonnées du défaut par liaison SCADA.</li>
</ol>
'''
)

ACR_ES = dict(
    lang='es',
    dir='ltr',
    slug='feeder-automation-what-is-an-auto-recloser-es',
    title='Automatización de Redes de Distribución Eléctrica: ¿Qué es un Reconectador Automático?',
    breadcrumb='Fusibles y Protección',
    read='10 min de lectura',
    alt='Reconectador automático en vacío de media tensión montado en poste operando en una línea aérea de distribución eléctrica',
    desc=('Automatización de alimentadores aéreos de media tensión y confiabilidad del suministro: ¿Qué es un reconectador automático (ACR)? '
          'Cómo los reconectadores en vacío despejan fallas transitorias (ANSI 79), previenen apagones y reducen los índices SAIDI/SAIFI.'),
    model='Serie ZW32 / ZW20: Reconectadores Automáticos de Media Tensión en Vacío para Intemperie (11kV–36kV)',
    category='Fusibles y Protección / Reconectadores Automáticos',
    kw='reconectador automático &middot; reconectador en vacío &middot; reconectador 11kv 33kv &middot; reconectador en poste &middot; automatización de alimentadores',
    specs=[
        ('Tensión Asignada y Frecuencia de Servicio', 'Tensión nominal 12kV, 24kV y 36kV; tensión máxima de operación continua hasta 40,5kV; frecuencia industrial 50Hz / 60Hz'),
        ('Niveles de Aislamiento e Impulso tipo Rayo', 'Tensión soportada a frecuencia industrial 42kV/54kV/95kV; tensión de impulso tipo rayo (BIL) 75kV / 125kV / 170kV'),
        ('Corriente Nominal y Capacidad de Ruptura', 'Corriente continua 630A y 1250A; corriente de ruptura en cortocircuito 12,5 kA, 16 kA y 20 kA (probado hasta 25 kA a 12kV)'),
        ('Tecnología de Interrupción y Aislamiento', 'Botellas de interrupción en vacío alojadas en polos encapsulados en resina epoxi sólida o caucho de silicona resistente a intemperie'),
        ('Mecanismo de Operación y Actuador', 'Actuador magnético permanente (PMA) o mecanismo de resortes motorizados con palanca manual de apertura y bloqueo mecánico'),
        ('Secuencia de Reconexión Programable (ANSI 79)', 'Ciclo configurable hasta 4 operaciones de reconexión: A &minus; 0,3s &minus; CA &minus; 2s &minus; CA &minus; 2s &minus; CA &minus; Bloqueo'),
        ('Controlador Electrónico Inteligente (FTU/RTU)', 'Gabinete de control por microprocesador con soporte de protocolos DNP3, IEC 60870-5-104, sobrecorriente direccional y falla a tierra sensible (SEF)'),
        ('Vida Útil Mecánica y Eléctrica', 'Clase M2 de alta endurancia mecánica (&ge; 10.000 operaciones sin mantenimiento); Clase E2 a plena corriente de cortocircuito')
    ],
    faqs=[
        ('¿Qué es un Reconectador Automático (ACR) y cómo evita cortes prolongados de energía en redes eléctricas?',
         'Un Reconectador Automático—conocido comúnmente como reconectador de distribución o restaurador de poste—es un interruptor de media tensión para intemperie '
         'diseñado para despejar corrientes de falla y reconectar automáticamente el circuito eléctrico tras un intervalo programado. '
         'Las estadísticas de las empresas eléctricas demuestran que **entre el 80% y el 90% de las fallas en líneas aéreas son transitorias o pasajeras**, '
         'originadas por ramas de árboles mecidas por el viento, descargas de rayos que ionizan aisladores o aves en contacto momentáneo con los conductores. '
         'Con un fusible o interruptor convencional, la línea queda desenergizada hasta que una brigada de mantenimiento acude físicamente al lugar. '
         'El reconectador automático abre sus contactos en menos de 35 milisegundos para extinguir el arco, espera una fracción de segundo a que el aire se desionice '
         'y vuelve a cerrar el circuito, restableciendo el servicio eléctrico de inmediato.'),
        ('¿Cómo funciona la secuencia de reconexión ANSI 79 para eliminar fallas temporales sin dañar transformadores en fallas permanentes?',
         'El controlador electrónico sigue una secuencia programada de disparos rápidos y temporizados: '
         '<ul>'
         '<li><strong>Primer disparo rápido (30ms):</strong> El reconectador abre instantáneamente antes de que los fusibles aguas abajo alcancen a fundirse. '
         'Aplica un "tiempo muerto" de 0,3 segundos para permitir que la rama caiga o el arco se extinga.</li>'
         '<li><strong>Primer cierre automático (0,3s):</strong> Los contactos en vacío se cierran. Si la falla desapareció, el suministro continúa con total normalidad.</li>'
         '<li><strong>Disparos temporizados subsiguientes (2s):</strong> Si la falla persiste, el equipo realiza de 1 a 3 intentos adicionales con curvas de tiempo inverso '
         'para permitir que los fusibles de ramal aíslen el tramo averiado.</li>'
         '<li><strong>Bloqueo definitivo (Lockout):</strong> Si la falla es permanente (un poste derribado o conductor roto en el suelo), el reconectador se abre definitivamente, '
         'quedando bloqueado y enviando una alarma SCADA con la distancia aproximada de la falla.</li>'
         '</ul>'),
        ('¿Cuál es la diferencia entre un Reconectador Automático y un Seccionalizador en líneas aéreas?',
         'La diferencia radica en su capacidad de interrumpir cortocircuitos: '
         'El **Reconectador Automático** es un disyuntor completo con cámaras de vacío capaz de extinguir arcos de cortocircuito severos de 12,5kA a 20kA. '
         'El **Seccionalizador** no tiene capacidad de corte de falla: cuenta los disparos del reconectador principal aguas arriba y se abre únicamente durante '
         'el tiempo muerto en que la línea está desenergizada para aislar un ramal averiado antes del bloqueo final.')
    ],
    cta='¿Moderniza líneas aéreas de distribución rural, proyectos de alimentadores inteligentes de 11kV–36kV o subestaciones eléctricas que requieren reconectadores automáticos certificados? YOMIN fabrica reconectadores en vacío bajo normas IEC 62271-111 y ANSI C37.60.',
    body='''
<h2>Eliminando el 80% de los Apagones Aéreos mediante Automatización de Redes</h2>
<p>Las líneas aéreas de media tensión—que operan entre 11kV y 36kV en zonas rurales, suburbanas e industriales—están expuestas constantemente a tormentas de viento, rayos, vegetación y fauna. Estas contingencias generan miles de fallas eléctricas temporales cada año.</p>
<p>Tradicionalmente, ante cualquier contacto accidental de una rama, los fusibles de expulsión caían o el interruptor de la subestación disparaba, dejando a miles de usuarios sin energía durante horas hasta que una cuadrilla técnica recorría la línea para reponer los cartuchos fusibles.</p>
<p>El <strong>Reconectador Automático de Media Tensión (ACR)</strong> constituye la solución por excelencia para la automatización de la red: despeja la corriente de cortocircuito en milisegundos y restablece el servicio automáticamente sin intervención humana.</p>

<h2>La Lógica de Protección ANSI 79: Disparos Rápidos y Temporizados</h2>
<p>La eficacia del reconectador radica en su capacidad de coordinar disparos rápidos y retardados:</p>
<ol>
  <li><strong>Disparo Rápido (30ms):</strong> Al detectar una sobrecorriente de falla, las cámaras de vacío abren los contactos en 30 milisegundos, evitando que los fusibles se quemen. Tras una pausa de 300ms ("tiempo muerto"), el equipo reconecta. Si el obstáculo cayó, el servicio queda restablecido.</li>
  <li><strong>Disparos Temporizados (2s):</strong> Si la falla continúa, el controlador conmuta a curvas de sobrecorriente retardadas, dando oportunidad a que los fusibles del ramal aíslen el tramo específico.</li>
  <li><strong>Bloqueo Definitivo (Lockout):</strong> Si la falla es permanente (un cable caído al suelo), el reconectador se bloquea en posición abierta para proteger los transformadores y envía telemetría SCADA a la central de control.</li>
</ol>
'''
)

ACR_AR = dict(
    lang='ar',
    dir='rtl',
    slug='feeder-automation-what-is-an-auto-recloser-ar',
    title='أتمتة شبكات التوزيع الكهربائي متوسطة الجهد: ما هو قاطع الإعادة التلقائي (Auto Recloser)؟',
    breadcrumb='المصهرات والحماية',
    read='10 دقائق قراءة',
    alt='قاطع إعادة تلقائي مفرغ من الهواء متوسط الجهد مثبت على عمود يعمل على خط هوائي لتوزيع الكهرباء',
    desc=('أتمتة خطوط التوزيع الهوائية متوسطة الجهد ورفع موثوقية التغذية: ما هو قاطع الإعادة التلقائي (Auto Recloser)؟ '
          'كيف تزيل قواطع الإعادة الأعطال العابرة المؤقتة (ANSI 79)، وتمنع انقطاعات الكهرباء الطويلة، وتخفض مؤشرات الانقطاع SAIDI/SAIFI.'),
    model='سلسلة ZW32 / ZW20: قواطع الإعادة التلقائية الهوائية المفرغة من الهواء متوسطة الجهد (11kV–36kV)',
    category='المصهرات والحماية / قواطع الإعادة التلقائية',
    kw='قاطع الإعادة التلقائي &middot; auto recloser &middot; قاطع هوائي متوسط الجهد &middot; ريكلوزر 11kv 33kv &middot; أتمتة خطوط التوزيع الهوائية',
    specs=[
        ('الجهد الاسمي وتردد النظام', 'الجهد المقنن 12kV و 24kV و 36kV؛ أقصى جهد تشغيل مستمر حتى 40.5kV؛ التردد الاسمي 50Hz / 60Hz'),
        ('مستويات العزل وصدمة الصواعق', 'جهد تحمل تردد الشبكة (جاف/مبلل) 42kV/34kV و 95kV/80kV؛ جهد نبضة الصاعقة الاسمي (BIL) 75kV / 125kV / 170kV'),
        ('التيار المستمر وسعة قطع تيار القصر', 'التيار المستمر 630A و 1250A؛ سعة قطع تيارات القصر 12.5 kA و 16 kA و 20 kA (مختبر حتى 25 kA عند 12kV)'),
        ('تكنولوجيا إخماد القوس والعوازل', 'غرف تفريغ سيراميكية فائقة العزل محمية داخل أقطاب صلبة من الراتنج الإيبوكسي أو مطاط السيليكون المقاوم للعوامل الجوية'),
        ('آلية التشغيل والمشغل المغناطيسي', 'مشغل مغناطيسي دائم (PMA) أو مشغل يايات محركية قوية مع ذراع فتح يدوي وآلية إغلاق ميكانيكي للأمان في الطوارئ'),
        ('تسلسل إعادة التوصيل الآلي (ANSI 79)', 'تسلسل تشغيل قابل للبرمجة حتى 4 دورات: فتح &minus; 0.3 ثانية &minus; غلق/فتح &minus; 2 ثانية &minus; غلق/فتح &minus; إقفال تام'),
        ('وحدة التحكم الذكية ونقل الإشارات (FTU)', 'وحدة تحكم رقمية معالجة دقيقة (FTU) تدعم بروتوكولات DNP3.0 و IEC 60870-5-104، والحماية الاتجاهية من زيادة التيار والتسرب الأرضي الحساس'),
        ('العمر الافتراضي الميكانيكي والكهربائي', 'فئة M2 للتحمل الميكانيكي (&ge; 10,000 عملية تشغيل بدون صيانة)؛ فئة E2 لتحمل تيارات القصر القصوى؛ كابينة تحكم IP65')
    ],
    faqs=[
        ('ما هو قاطع الإعادة التلقائي (Auto Recloser) وكيف يقضي على انقطاعات الكهرباء في الخطوط الهوائية؟',
         'قاطع الإعادة التلقائي (Automatic Circuit Recloser - ACR / Recloser) هو قاطع دائرة كهربائي متوسط الجهد يُثبت في الهواء الطلق على أعمدة التوزيع '
         'مصمم لاكتشاف وقطع تيارات القصر الكهربائي، ثم إعادة توصيل الدائرة تلقائياً بعد فترة تأخير زمنية محسوبة بالثواني. '
         'تثبت الدراسات الهندسية الميدانية أن **أكثر من 80% إلى 90% من أعطال خطوط التوزيع الهوائية هي أعطال عابرة أو مؤقتة**، '
         'تنشأ عن ملامسة عابرة لأغصان الأشجار بفعل الرياح، أو تفريغ عابر لصاعقة على العوازل، أو اصطدام طيور بأسلاك التوزيع. '
         'عند استخدام القواطع أو المصهرات التقليدية، تنقطع الكهرباء عن الخط بأكمله لساعات حتى تصل فرق الطوارئ لاستبدال المصهر المحترق. '
         'يقوم قاطع الإعادة التلقائي بفصل الدائرة في أقل من 35 جزءاً من الألف من الثانية لإخماد القوس، وينتظر 0.3 ثانية لزوال التأين وسقوط الغصن، '
         'ثم يعيد التوصيل تلقائياً، فلا يشعر المستهلك سوى بوميض لحظي في الإنارة بدلاً من انقطاع طويل.'),
        ('كيف يعمل تسلسل الإعادة التلقائي (ANSI 79) لإزالة الأعطال المؤقتة وعزل الأعطال الدائمة بأمان؟',
         'تنفذ وحدة التحكم الإلكترونية تسلسلاً دقيقاً من عمليات الفصل السريع والبطيء: '
         '<ul>'
         '<li><strong>الفصل الأول السريع (30ms):</strong> يفصل القاطع فوراً قبل أن تنصهر المصهرات الفرعية، وينتظر "زمن خمول" قدره 0.3 ثانية لإتاحة الفرصة للقوس كي ينطفئ.</li>'
         '<li><strong>الإعادة الأولى (0.3s):</strong> يغلق القاطع نقاط تلامسه المفرغة؛ فإذا زال العطل المؤقت، تستمر التغذية الكهربائية بصورة طبيعية تماماً.</li>'
         '<li><strong>الفصل المتأخر الإضافي (2s):</strong> إذا استمر العطل، يفصل القاطع ويعيد المحاولة 1 إلى 3 مرات بانتظار زمني مدروس، مما يتيح للمصهرات الفرعية '
         'فصل المسار المعطوب بمفرده دون قطع الخط الرئيسي.</li>'
         '<li><strong>الإقفال التام (Lockout):</strong> إذا استمر العطل (بسبب سقوط عمود أو انقطاع سلك على الأرض)، يقفل القاطع نهائياً في وضع الفتح '
         'ويرسل بلاغاً آلياً عبر نظام الإسكادا (SCADA) لتحديد موقع العطل الدقيق لفرق الصيانة.</li>'
         '</ul>'),
        ('ما الفرق بين قاطع الإعادة التلقائي (Recloser) والمفتاح الجزئي (Sectionalizer) على الخطوط الهوائية؟',
         'الفارق الجوهري يكمن في سعة قطع تيار القصر: '
         '**قاطع الإعادة التلقائي** هو قاطع تيار متكامل بغرف تفريغ قادر على كسر تيار قصر هائل يصل إلى 20 ألف أمبير تحت الجهد العالي. '
         'أما **المفتاح الجزئي (Sectionalizer)** فهو مجرد مفتاح فصل لا يملك سعة لإطفاء أقواس تيارات القصر؛ إذ يقوم بعد فترات فصل قاطع الإعادة التلقائي الرئيسي الواقع قبله، '
         'ويفتح نقاط تلامسه فقط أثناء "زمن الخمول" الذي تنعدم فيه الكهرباء تماماً على الخط، ليعزل الفرع المصاب قبل قفل القاطع الرئيسي نهائياً.')
    ],
    cta='هل تصمم شبكات توزيع كهربائية هوائية ذكية، أو مشروعات تغذية كهربية ريفية متوسطة الجهد بقدرات 11kV أو 24kV أو 36kV تتطلب قواطع إعادة توصيل تلقائية معتمدة؟ تصنع يمين (YOMIN) قواطع ريكلوزر ذكية مطابقة للمواصفات الدولية IEC 62271-111 و ANSI C37.60.',
    body='''
<h2>القضاء على 80% من انقطاعات الخطوط الهوائية عبر أتمتة شبكات التوزيع</h2>
<p>تمثل خطوط التوزيع الهوائية متوسطة الجهد—العاملة من 11 إلى 36 كيلو فولت عبر المناطق الريفية والصناعية المفتوحة—الخط الأمامي الأكثر عرضة للاضطرابات المناخية. وتتعرض هذه الخطوط سنوياً لآلاف الأعطال الكهربائية الناتجة عن الصواعق والرياح الشديدة وتداخل الأشجار والطيور.</p>
<p>تاريخياً، كان حدوث أي تماس مؤقت يؤدي إلى سقوط المصهرات الهوائية أو فصل قاطع المحطة الرئيسية، مما يترك مدناً ومصانع ومستشفيات بلا كهرباء لساعات طويلة حتى تصل فرق الطوارئ لاستبدال المصاهر يدوياً.</p>
<p>يمثل <strong>قاطع الإعادة التلقائي المفرغ من الهواء (Auto Recloser - ACR)</strong> حجر الزاوية في أتمتة مغذيات التوزيع الكهربائي، حيث يجمع بين سرعة الفصل الفائقة في الفراغ المطلق، والتحكم الرقمي الذكي، وإعادة التوصيل التلقائي لإعادة التيار في أجزاء من الثانية.</p>

<h2>فلسفة التشغيل ANSI 79: التناغم بين الفصل السريع والبطيء</h2>
<p>تعتمد عبقرية قاطع الإعادة على تسلسل ذكي مبرمج وفق معيار الحماية ANSI 79:</p>
<ol>
  <li><strong>الضربة السريعة الفورية (30ms):</strong> عند استشعار تيار القصر، تفتح غرف التفريغ في 30 مللي ثانية فقط، مما يمنع احتراق المصهرات الفرعية في الشبكة. يظل القاطع مفتوحاً لزمن 300 مللي ثانية لتبديد القوس ثم يعيد التوصيل. فإذا زال التماس المؤقت، تستقر الشبكة فوراً.</li>
  <li><strong>الضربات المتأخرة (2 ثانية):</strong> إذا تكرر تيار القصر، تبدأ وحدة التحكم بالاعتماد على منحنيات زمنية متأخرة، لمنح مصاهر الخطوط الفرعية فرصة كافية للانصهار وفصل العطل موضعياً.</li>
  <li><strong>الإقفال النهائي (Lockout):</strong> عند التأكد من أن العطل دائم (مثل سقوط كابل على الأرض)، يقفل القاطع نهائياً في وضع الفتح لمنع احتراق المحولات، ويبث إحداثيات العطل عبر الإسكادا لمركز التحكم.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_0930 = [
    DCU_EN, DCU_FR, DCU_ES, DCU_AR,
    ACR_EN, ACR_FR, ACR_ES, ACR_AR
]
