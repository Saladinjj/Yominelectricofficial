# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-09-28:
1. Four-Quadrant Bi-Directional Smart Energy Meter (EN, FR, ES, AR)
2. Split-Type STS Prepaid Electricity Meter with CIU (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. FOUR-QUADRANT SMART ENERGY METER (EN, FR, ES, AR)
# ==============================================================================

FOUR_QUADRANT_EN = dict(
    lang='en',
    dir='ltr',
    slug='industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter',
    title='Industrial Grid Interconnection & Reactive Power: What Is a Four-Quadrant Energy Meter?',
    breadcrumb='Energy Meters',
    read='10 min read',
    alt='Three-phase four-quadrant bi-directional smart energy meter actively operating inside an industrial facility substation switchgear panel',
    desc=('Commercial solar grid interconnection and industrial reactive power billing: What is a four-quadrant energy meter? '
          'How multi-vector electronic smart meters measure active energy import/export (+P / -P), inductive/capacitive reactive energy (+Q / -Q), and power factor to eliminate utility penalties.'),
    model='Model DTS / DTZ Series Three-Phase 4-Quadrant Bi-Directional Smart Energy Meters',
    category='Energy Meters / Bi-Directional Grid Meters',
    kw='what is a four quadrant energy meter &middot; four quadrant meter &middot; bidirectional energy meter &middot; net metering solar meter &middot; reactive power billing',
    specs=[
        ('Measurement Architecture', 'Full 4-Quadrant true RMS vector measurement: Active Import (+P), Active Export (-P), Reactive Inductive (+Q), Reactive Capacitive (-Q)'),
        ('Rated Voltage & Current', '3&times;230/400V AC 3-phase 4-wire (or 3&times;100V 3-phase 3-wire); CT-operated 1.5(6)A / 5(10)A or direct-connect 5(100)A frame sizes'),
        ('Metrological Accuracy Class', 'Active energy Class 0.5S or Class 0.2S (IEC 62053-22); Reactive energy Class 1.0 or Class 2.0 (IEC 62053-23)'),
        ('Harmonic & Power Quality Profiling', 'Total Harmonic Distortion (THD) and individual harmonics up to the 31st order; voltage sag/swell and phase angle imbalance logging'),
        ('Multi-Tariff Time-of-Use (TOU)', 'Up to 8 configurable tariff rates, 14 seasonal zones, and 8 daily billing profiles managed via battery-backed real-time clock'),
        ('Communication Interfaces', 'Dual RS485 Modbus RTU ports, optical IEC 62056-21 port, and pluggable 4G/GPRS or Ethernet DLMS/COSEM smart grid module'),
        ('Data Logging & Load Profiling', 'Non-volatile flash memory recording 15-minute load profiles for up to 180 days; tamper event recording with real-time timestamps'),
        ('Applicable International Standards', 'IEC 62052-11, IEC 62053-22, IEC 62053-23, EN 50470-3 (MID Class C), DLMS/COSEM certified for utility AMI systems')
    ],
    faqs=[
        ('What is a four-quadrant energy meter and how does it differ from a standard bi-directional meter?',
         'A standard bi-directional net-meter only measures active power flow in two directions: energy imported from the utility grid (+kWh) and energy exported '
         'back to the grid from rooftop solar panels (-kWh). However, industrial manufacturing plants and commercial buildings also draw massive inductive '
         'loads from electric motors, transformers, and compressors, creating reactive power (kvarh). '
         'A **Four-Quadrant Energy Meter** measures both active power (P) and reactive power (Q) simultaneously across all four operating quadrants of the complex power plane: '
         'Quadrant I (+P, +Q: Import Active, Inductive Lagging), Quadrant II (-P, +Q: Export Active, Inductive Leading), '
         'Quadrant III (-P, -Q: Export Active, Capacitive Lagging), and Quadrant IV (+P, -Q: Import Active, Capacitive Leading). '
         'This comprehensive 4-vector monitoring enables electric utilities to bill accurately for power factor degradation and grid stability impacts.'),
        ('Why do electric utilities mandate four-quadrant metering for commercial solar and industrial grid interconnections?',
         'When industrial factories install multi-megawatt rooftop solar photovoltaic systems or grid-tied battery storage, they transform from passive consumers '
         'into active grid participants (prosumers). While the solar inverter feeds active kilowatt-hours into the grid during peak sunshine, the factory\'s '
         'heavy conveyor motors and chillers continue demanding magnetizing reactive power (kvar) from the utility lines. '
         'Without a four-quadrant meter, standard metering cannot distinguish whether reactive energy is being absorbed by the plant or injected by over-excited inverters. '
         'Utilities mandate 4-quadrant DLMS/COSEM meters to enforce grid codes (such as IEEE 1547 and EN 50549), monitor power factor in real time, and levy statutory '
         'low-power-factor surcharges whenever power factor drops below 0.90 or 0.95.'),
        ('How does four-quadrant metering help industrial facility managers eliminate power factor penalty charges?',
         'Electric utility bills for commercial and industrial consumers include punitive maximum demand charges and low-power-factor penalties based on reactive energy consumption. '
         'A four-quadrant meter provides detailed 15-minute load profiles breaking down inductive versus capacitive kvarh across peak, shoulder, and off-peak tariff periods. '
         'Plant energy managers use this granular quadrant telemetry to properly size and tune automatic power factor correction (APFC) capacitor banks, '
         'prevent harmonic resonance, and program inverter power factor settings, completely eliminating utility surcharge penalties.')
    ],
    cta='Specifying Class 0.5S four-quadrant bi-directional smart energy meters for industrial solar grid interconnections, utility substations, or commercial microgrids? YOMIN manufactures DLMS/COSEM and Modbus smart meters engineered to IEC 62053.',
    body='''
<h2>Complex Power Dynamics in the Distributed Generation Era</h2>
<p>The global transition toward distributed renewable generation has fundamentally transformed commercial and industrial power distribution. Manufacturing facilities, logistics parks, and commercial data centers are no longer simple unidirectional power consumers. With multi-megawatt rooftop solar PV arrays, cogeneration plants, and battery energy storage systems (BESS), modern facilities constantly import and export electricity simultaneously.</p>
<p>However, power flow in alternating current (AC) networks involves both <strong>Active Power (Watts)</strong> that performs physical mechanical work and <strong>Reactive Power (VARs)</strong> required to sustain magnetic fields in industrial motors, transformers, and inverters.</p>
<p>The <strong>Four-Quadrant Energy Meter</strong> is the foundational metrological instrument that provides complete 360-degree vector accounting of active and reactive energy across modern smart grid interconnections.</p>

<h2>The Four Operating Quadrants Explained</h2>
<p>In electrical power engineering, alternating current power flow is mapped onto a two-dimensional Cartesian coordinate system where the horizontal axis represents Active Power (P) and the vertical axis represents Reactive Power (Q):</p>
<table>
  <thead>
    <tr>
      <th>Quadrant</th>
      <th>Power Vector</th>
      <th>Operating Condition</th>
      <th>Typical Industrial Equipment State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Quadrant I (Q1)</strong></td>
      <td><strong>+P, +Q</strong></td>
      <td><strong>Import Active, Inductive (Lagging)</strong></td>
      <td>Standard factory consumption: importing grid electricity to drive induction motors, machine tools, and transformers.</td>
    </tr>
    <tr>
      <td><strong>Quadrant II (Q2)</strong></td>
      <td><strong>-P, +Q</strong></td>
      <td><strong>Export Active, Inductive (Leading)</strong></td>
      <td>Solar PV array or generator exporting active power to the grid while absorbing magnetizing reactive power.</td>
    </tr>
    <tr>
      <td><strong>Quadrant III (Q3)</strong></td>
      <td><strong>-P, -Q</strong></td>
      <td><strong>Export Active, Capacitive (Lagging)</strong></td>
      <td>Over-excited synchronous generator or smart solar inverter generating active electricity while injecting reactive VAR support into the grid.</td>
    </tr>
    <tr>
      <td><strong>Quadrant IV (Q4)</strong></td>
      <td><strong>+P, -Q</strong></td>
      <td><strong>Import Active, Capacitive (Leading)</strong></td>
      <td>Facility importing grid power with over-compensated power factor correction capacitor banks or lightly loaded underground cables.</td>
    </tr>
  </tbody>
</table>
'''
)

FOUR_QUADRANT_FR = dict(
    lang='fr',
    dir='ltr',
    slug='industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-fr',
    title="Raccordement au Réseau Industriel & Énergie Réactive : Qu'est-ce qu'un Compteur d'Énergie Quatre Quadrants ?",
    breadcrumb='Compteurs d\'Énergie',
    read='10 min de lecture',
    alt='Compteur d\'énergie intelligent bidirectionnel triphasé à quatre quadrants en service dans un tableau de sous-station industrielle',
    desc=('Raccordement solaire industriel et facturation de la puissance réactive : Qu\'est-ce qu\'un compteur d\'énergie quatre quadrants ? '
          'Comment les compteurs intelligents mesurent l\'énergie active (+P / -P), l\'énergie réactive (+Q / -Q) et le facteur de puissance pour éliminer les pénalités.'),
    model='Série DTS / DTZ : Compteurs d\'Énergie Intelligents Triphasés Bidirectionnels 4 Quadrants',
    category='Compteurs d\'Énergie / Réseau Bidirectionnel',
    kw='compteur quatre quadrants &middot; compteur d\'énergie 4 quadrants &middot; compteur bidirectionnel &middot; comptage d\'énergie réactive &middot; raccordement photovoltaïque',
    specs=[
        ('Architecture de Mesure', 'Mesure vectorielle RMS vraie sur 4 quadrants : Énergie active importée (+P), exportée (-P), réactive inductive (+Q) et capacitive (-Q)'),
        ('Tension et Courant Nominaux', '3&times;230/400V AC triphasé 4 fils (ou 3&times;100V 3 fils) ; raccordement sur TC 1,5(6)A / 5(10)A ou direct 5(100)A'),
        ('Classe de Précision Métrologique', 'Énergie active Classe 0,5S ou Classe 0,2S (CEI 62053-22) ; Énergie réactive Classe 1,0 ou Classe 2,0 (CEI 62053-23)'),
        ('Analyse des Harmoniques', 'Taux de distorsion harmonique global (THD) et rangs harmoniques individuels jusqu\'au 31ème rang ; journal des creux et surtensions'),
        ('Tarification Multi-Tarif (TOU)', 'Jusqu\'à 8 tarifs configurables, 14 saisons et 8 profils journaliers gérés par horloge temps réel (RTC) secourue par pile'),
        ('Interfaces de Communication', 'Deux ports RS485 Modbus RTU, port optique CEI 62056-21, et module enfichable 4G/GPRS ou Ethernet DLMS/COSEM pour réseaux intelligents'),
        ('Enregistrement des Profils de Charge', 'Mémoire flash non volatile enregistrant les courbes de charge 15 minutes sur 180 jours ; horodatage des événements de fraude'),
        ('Normes Internationales Applicables', 'CEI 62052-11, CEI 62053-22, CEI 62053-23, EN 50470-3 (MID Classe C), certifié DLMS/COSEM pour systèmes AMI')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un compteur d\'énergie quatre quadrants et en quoi diffère-t-il d\'un compteur bidirectionnel classique ?',
         'Un compteur bidirectionnel standard mesure uniquement le flux d\'énergie active dans deux directions : l\'électricité importée du réseau (+kWh) et l\'électricité '
         'solaire réinjectée (-kWh). Cependant, les usines et bâtiments tertiaires alimentent des moteurs et transformateurs qui consomment de la puissance réactive (kvarh). '
         'Un **Compteur Quatre Quadrants** mesure simultanément la puissance active (P) et la puissance réactive (Q) dans les quatre quadrants du plan complexe : '
         'Quadrant I (+P, +Q : Import Actif, Inductif Arrière), Quadrant II (-P, +Q : Export Actif, Inductif Avant), '
         'Quadrant III (-P, -Q : Export Actif, Capacitif Arrière) et Quadrant IV (+P, -Q : Import Actif, Capacitif Avant). '
         'Cette analyse vectorielle complète permet aux gestionnaires de réseau de facturer précisément l\'impact sur la stabilité du réseau.'),
        ('Pourquoi les distributeurs d\'électricité imposent-ils le comptage 4 quadrants pour le solaire industriel ?',
         'Lorsqu\'une usine installe une centrale solaire photovoltaïque en toiture, elle devient un acteur actif du réseau (prosommateur). Tandis que l\'onduleur '
         'injecte des kilowattheures actifs sur le réseau à midi, les compresseurs et moteurs de l\'usine continuent d\'absorber de la puissance réactive magnétisante. '
         'Sans compteur 4 quadrants, le distributeur ne peut pas distinguer si l\'énergie réactive est absorbée par l\'installation ou fournie par les onduleurs. '
         'Les distributeurs imposent ces compteurs DLMS/COSEM pour appliquer les codes de réseau (comme la norme EN 50549) et facturer les pénalités de mauvais facteur de puissance.'),
        ('Comment le comptage 4 quadrants permet-il d\'éliminer les pénalités de dépassement de puissance réactive ?',
         'Les factures d\'électricité des sites industriels intègrent des pénalités financières lourdes lorsque le facteur de puissance (cos phi) descend sous 0,90 ou 0,93. '
         'Un compteur 4 quadrants fournit des courbes de charge détaillées au pas de 10 ou 15 minutes dissociant les kvarh inductifs et capacitifs. '
         'Ces données permettent aux directeurs d\'usine de dimensionner précisément leurs batteries de condensateurs automatiques (batteries de compensation), '
         'évitant ainsi les pénalités de dépassement.')
    ],
    cta='Vous concevez des sous-stations industrielles, des raccordements solaires haute puissance ou des micro-réseaux nécessitant des compteurs intelligents Classe 0,5S quatre quadrants ? YOMIN fabrique des compteurs communicants conformes CEI 62053 et DLMS/COSEM.',
    body='''
<h2>La Gestion de la Puissance Complexe à l'Ère des Énergies Renouvelables</h2>
<p>L'intégration massive de la production photovoltaïque sur les toitures industrielles a transformé les consommateurs en prosommateurs. Une usine moderne ne se contente plus de consommer passivement de l'électricité : elle en injecte régulièrement sur le réseau de distribution moyenne ou basse tension.</p>
<p>Cependant, le courant alternatif transporte à la fois de la <strong>Puissance Active (Watts)</strong> qui produit un travail mécanique ou thermique utile, et de la <strong>Puissance Réactive (VARs)</strong> nécessaire à la magnétisation des moteurs, transformateurs et inductances.</p>
<p>Le <strong>Compteur d'Énergie Quatre Quadrants</strong> est l'équipement de métrologie fondamental permettant de mesurer avec une précision absolue les flux d'énergie active et réactive sur les points d'interconnexion au réseau.</p>

<h2>Explication des Quatre Quadrants de Fonctionnement</h2>
<p>En électrotechnique, les flux de puissance s'inscrivent sur un repère cartésien où l'axe horizontal représente la puissance active (P) et l'axe vertical la puissance réactive (Q) :</p>
<table>
  <thead>
    <tr>
      <th>Quadrant</th>
      <th>Vecteur Puissance</th>
      <th>Sens de Circulation</th>
      <th>État de l'Installation Industrielle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Quadrant I (Q1)</strong></td>
      <td><strong>+P, +Q</strong></td>
      <td><strong>Import Actif, Inductif (Arrière)</strong></td>
      <td>Consommation industrielle classique : prélèvement d'énergie active et réactive pour alimenter moteurs et transformateurs.</td>
    </tr>
    <tr>
      <td><strong>Quadrant II (Q2)</strong></td>
      <td><strong>-P, +Q</strong></td>
      <td><strong>Export Actif, Inductif (Avant)</strong></td>
      <td>Centrale solaire ou cogénération injectant de la puissance active sur le réseau tout en consommant de la puissance réactive.</td>
    </tr>
    <tr>
      <td><strong>Quadrant III (Q3)</strong></td>
      <td><strong>-P, -Q</strong></td>
      <td><strong>Export Actif, Capacitif (Arrière)</strong></td>
      <td>Générateur synchrone ou onduleur intelligent injectant à la fois puissance active et puissance réactive de soutien au réseau.</td>
    </tr>
    <tr>
      <td><strong>Quadrant IV (Q4)</strong></td>
      <td><strong>+P, -Q</strong></td>
      <td><strong>Import Actif, Capacitif (Avant)</strong></td>
      <td>Usine prélevant de l'énergie active avec une batterie de condensateurs surcompensée ou de longs câbles souterrains à vide.</td>
    </tr>
  </tbody>
</table>
'''
)

FOUR_QUADRANT_ES = dict(
    lang='es',
    dir='ltr',
    slug='industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-es',
    title='Interconexión a la Red Industrial y Potencia Reactiva: ¿Qué es un Medidor de Energía de Cuatro Cuadrantes?',
    breadcrumb='Medidores de Energía',
    read='10 min de lectura',
    alt='Medidor de energía inteligente bidireccional trifásico de cuatro cuadrantes en funcionamiento en un panel de subestación industrial',
    desc=('Interconexión de red solar industrial y facturación de energía reactiva: ¿Qué es un medidor de energía de cuatro cuadrantes? '
          'Cómo los medidores inteligentes miden la energía activa (+P / -P), la energía reactiva (+Q / -Q) y el factor de potencia para evitar penalizaciones.'),
    model='Serie DTS / DTZ: Medidores Inteligentes Trifásicos Bidireccionales de 4 Cuadrantes',
    category='Medidores de Energía / Red Bidireccional',
    kw='medidor cuatro cuadrantes &middot; medidor de energía 4 cuadrantes &middot; medidor bidireccional &middot; medición energía reactiva &middot; interconexión solar fotovoltaica',
    specs=[
        ('Arquitectura de Medición', 'Medición vectorial RMS real en 4 cuadrantes: Energía activa importada (+P), exportada (-P), reactiva inductiva (+Q) y capacitiva (-Q)'),
        ('Tensión y Corriente Nominal', '3&times;230/400V AC trifásico 4 hilos (o 3&times;100V 3 hilos); conexión por TC 1,5(6)A / 5(10)A o conexión directa 5(100)A'),
        ('Clase de Precisión Metrológica', 'Energía activa Clase 0,5S o Clase 0,2S (IEC 62053-22); Energía reactiva Clase 1,0 o Clase 2,0 (IEC 62053-23)'),
        ('Monitoreo de Calidad de Energía', 'Distorsión armónica total (THD) y armónicos individuales hasta el orden 31; registro de caídas, sobretensiones y desbalance'),
        ('Tarificación Horaria (TOU)', 'Hasta 8 tarifas configurables, 14 temporadas y 8 perfiles diarios mediante reloj en tiempo real con respaldo de batería'),
        ('Interfaces de Comunicación', 'Doble puerto RS485 Modbus RTU, puerto óptico IEC 62056-21, y módulo enchufable 4G/GPRS o Ethernet DLMS/COSEM'),
        ('Registro de Curvas de Carga', 'Memoria flash no volátil con perfiles de carga cada 15 minutos durante 180 días; registro de eventos de fraude'),
        ('Normas Internacionales Aplicables', 'IEC 62052-11, IEC 62053-22, IEC 62053-23, EN 50470-3 (MID Clase C), certificado DLMS/COSEM para redes AMI')
    ],
    faqs=[
        ('¿Qué es un medidor de energía de cuatro cuadrantes y en qué se diferencia de un medidor bidireccional convencional?',
         'Un medidor bidireccional estándar solo registra el flujo de energía activa en dos sentidos: energía importada de la red eléctrica (+kWh) y energía exportada '
         'hacia la red desde paneles solares (-kWh). Sin embargo, las fábricas y centros comerciales operan motores, transformadores y compresores que consumen '
         'potencia reactiva (kvarh). '
         'Un **Medidor de Cuatro Cuadrantes** mide simultáneamente la potencia activa (P) y la potencia reactiva (Q) en los cuatro cuadrantes del plano complejo: '
         'Cuadrante I (+P, +Q: Importación Activa, Inductiva en Atraso), Cuadrante II (-P, +Q: Exportación Activa, Inductiva en Adelanto), '
         'Cuadrante III (-P, -Q: Exportación Activa, Capacitiva en Atraso) y Cuadrante IV (+P, -Q: Importación Activa, Capacitiva en Adelanto). '
         'Esto permite a las empresas de energía facturar con precisión las penalizaciones por bajo factor de potencia.'),
        ('¿Por qué las empresas eléctricas exigen medidores de cuatro cuadrantes para plantas solares industriales?',
         'Cuando una industria instala sistemas fotovoltaicos en sus cubiertas, se convierte en un prosumidor activo. Mientras los inversores solares '
         'inyectan energía activa a la red a mediodía, los motores de la fábrica continúan demandando potencia reactiva magnetizante de la red. '
         'Sin un medidor de 4 cuadrantes, la distribuidora no puede distinguir si la energía reactiva es absorbida por la fábrica o inyectada por los inversores. '
         'Las empresas exigen estos medidores DLMS/COSEM para cumplir el código de red y cobrar los recargos por factor de potencia inferior a 0,90 o 0,95.'),
        ('¿Cómo ayuda la medición en 4 cuadrantes a eliminar los recargos por energía reactiva?',
         'Las facturas eléctricas industriales penalizan severamente el consumo excesivo de energía reactiva. Un medidor de 4 cuadrantes registra curvas '
         'de carga detalladas cada 15 minutos desglosando los kvarh inductivos y capacitivos. '
         'Esta información permite a los ingenieros de planta dimensionar con exactitud los bancos automáticos de condensadores, evitando sobrecompensaciones '
         'y eliminando por completo las multas en el recibo de luz.')
    ],
    cta='¿Diseña subestaciones industriales, proyectos de generación distribuida o plantas comerciales que requieren medidores inteligentes Clase 0,5S de 4 cuadrantes? YOMIN fabrica medidores certificados bajo normas IEC 62053 y DLMS/COSEM.',
    body='''
<h2>La Medición de Potencia Compleja en la Era Solar Distribuida</h2>
<p>La adopción masiva de energía solar fotovoltaica en techos industriales ha transformado por completo el flujo de energía eléctrica en las redes de distribución. Las fábricas ya no son receptores pasivos de energía, sino nodos activos capaces de generar, exportar e importar electricidad de manera continua.</p>
<p>En los circuitos de corriente alterna, la energía total transportada se compone de <strong>Potencia Activa (Vatios)</strong>, que realiza trabajo útil, y <strong>Potencia Reactiva (VARs)</strong>, necesaria para crear los campos magnéticos indispensables en motores y transformadores.</p>
<p>El <strong>Medidor de Energía de Cuatro Cuadrantes</strong> es el instrumento metrológico esencial para registrar con máxima precisión todos los vectores de potencia en puntos de interconexión industrial.</p>

<h2>Definición y Funcionamiento de los Cuatro Cuadrantes</h2>
<p>En ingeniería eléctrica, los vectores de potencia se representan en un plano cartesiano bidimensional donde el eje horizontal indica la Potencia Activa (P) y el eje vertical representa la Potencia Reactiva (Q):</p>
<table>
  <thead>
    <tr>
      <th>Cuadrante</th>
      <th>Vector de Potencia</th>
      <th>Sentido de Flujo</th>
      <th>Estado Operativo de la Planta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Cuadrante I (Q1)</strong></td>
      <td><strong>+P, +Q</strong></td>
      <td><strong>Importación Activa, Inductiva (Atraso)</strong></td>
      <td>Consumo industrial estándar: la planta absorbe energía activa y reactiva de la red para alimentar motores e iluminación.</td>
    </tr>
    <tr>
      <td><strong>Cuadrante II (Q2)</strong></td>
      <td><strong>-P, +Q</strong></td>
      <td><strong>Exportación Activa, Inductiva (Adelanto)</strong></td>
      <td>Planta fotovoltaica inyectando energía activa a la red mientras sus cargas auxiliares consumen potencia reactiva.</td>
    </tr>
    <tr>
      <td><strong>Cuadrante III (Q3)</strong></td>
      <td><strong>-P, -Q</strong></td>
      <td><strong>Exportación Activa, Capacitiva (Atraso)</strong></td>
      <td>Generador síncrono o inversor inteligente inyectando activamente potencia activa y soporte de potencia reactiva a la red.</td>
    </tr>
    <tr>
      <td><strong>Cuadrante IV (Q4)</strong></td>
      <td><strong>+P, -Q</strong></td>
      <td><strong>Importación Activa, Capacitiva (Adelanto)</strong></td>
      <td>La fábrica consume energía activa con bancos de condensadores sobrecompensados o cables subterráneos en vacío.</td>
    </tr>
  </tbody>
</table>
'''
)

FOUR_QUADRANT_AR = dict(
    lang='ar',
    dir='rtl',
    slug='industrial-grid-interconnection-what-is-a-four-quadrant-energy-meter-ar',
    title='ربط الشبكة الصناعية والقدرة غير الفعالة: ما هو عداد الطاقة رباعي الأرباع؟',
    breadcrumb='عدادات الطاقة',
    read='10 دقائق قراءة',
    alt='عداد طاقة ذكي ثلاثي الأطوار رباعي الأرباع ثنائي الاتجاه يعمل داخل لوحة توزيع فرعية صناعية',
    desc=('ربط شبكات الطاقة الشمسية الصناعية وفواتير القدرة غير الفعالة: ما هو عداد الطاقة رباعي الأرباع؟ '
          'كيف تقيس العدادات الذكية الطاقة الفعالة (+P / -P) وغير الفعالة (+Q / -Q) ومعامل القدرة للتخلص من غرامات شركات الكهرباء.'),
    model='سلسلة DTS / DTZ: عدادات ذكية ثلاثية الأطوار رباعية الأرباع وثنائية الاتجاه',
    category='عدادات الطاقة / العدادات الشبكية ثنائية الاتجاه',
    kw='عداد أربعة أرباع &middot; عداد طاقة 4 أرباع &middot; عداد ثنائي الاتجاه &middot; قياس القدرة غير الفعالة &middot; ربط الطاقة الشمسية بالشبكة',
    specs=[
        ('هندسة القياس الكهربائي', 'قياس اتجاهي حقيقي RMS في 4 أرباع: الطاقة الفعالة المستوردة (+P)، المصدرة (-P)، غير الفعالة الحثية (+Q) والسعوية (-Q)'),
        ('الجهد والتيار الاسمي', '3&times;230/400V تيار متردد ثلاثي الأطوار 4 أسلاك؛ توصيل عبر محولات تيار 1.5(6)A / 5(10)A أو توصيل مباشر 5(100)A'),
        ('فئة الدقة المترولوجية', 'الطاقة الفعالة فئة 0.5S أو فئة 0.2S (IEC 62053-22)؛ الطاقة غير الفعالة فئة 1.0 أو فئة 2.0 (IEC 62053-23)'),
        ('مراقبة جودة القدرة والتوافقيات', 'قياس التشوه التوافقي الكلي (THD) والتوافقيات الفردية حتى الرتبة 31؛ تسجيل هبوط وارتفاع الجهد وعدم اتزان الأطوار'),
        ('نظام التعرفة متعدد الأوقات (TOU)', 'حتى 8 فئات تعرفة قابلة للضبط، 14 موسماً، و8 ملفات تشغيل يومية عبر ساعة داخلية عالية الدقة مدعومة ببطارية ليثيوم'),
        ('منافذ وبروتوكولات الاتصال', 'منفذا RS485 Modbus RTU، منفذ ضوئي IEC 62056-21، ووحدة اتصالات قابلة للتبديل 4G/GPRS أو Ethernet DLMS/COSEM للشبكات الذكية'),
        ('تسجيل منحنيات الحمل الكهربائي', 'ذاكرة فلاش دائمة تسجل منحنيات الأحمال كل 15 دقيقة لمدة تصل إلى 180 يوماً؛ توثيق كامل لمحاولات العبث مع الوقت والتاريخ'),
        ('المعايير الدولية المعتمدة', 'IEC 62052-11، IEC 62053-22، IEC 62053-23، EN 50470-3 (MID)، معتمد رسمياً ببروتوكول DLMS/COSEM لأنظمة AMI')
    ],
    faqs=[
        ('ما هو عداد الطاقة رباعي الأرباع وما الفرق بينه وبين العداد ثنائي الاتجاه التقليدي؟',
         'يقيس العداد ثنائي الاتجاه التقليدي تدفق الطاقة الفعالة في اتجاهين فقط: الكهرباء المستوردة من الشبكة العامة (+kWh) والكهرباء المصدرة من الألواح الشمسية '
         'إلى الشبكة (-kWh). لكن المنشآت الصناعية والمباني التجارية تشغل محركات ومحولات ومكيفات ضخمة تستهلك قدراً هائلاً من القدرة غير الفعالة (kvarh). '
         'يقيس **عداد الطاقة رباعي الأرباع** كلاً من القدرة الفعالة (P) والقدرة غير الفعالة (Q) في آن واحد عبر الأرباع الأربعة للمستوى الإحداثي الكهربائي: '
         'الربع الأول (+P, +Q: استيراد قدرة فعالة، حمل حثي متأخر)، الربع الثاني (-P, +Q: تصدير قدرة فعالة، حمل حثي متقدم)، '
         'الربع الثالث (-P, -Q: تصدير قدرة فعالة، حمل سعوي متأخر)، والربع الرابع (+P, -Q: استيراد قدرة فعالة، حمل سعوي متقدم). '
         'يتيح هذا التوثيق الشامل لشركات توزيع الكهرباء احتساب فواتير معامل القدرة بدقة متناهية.'),
        ('لماذا تلزم شركات الكهرباء المصانع ومشاريع الطاقة الشمسية بتركيب عدادات رباعية الأرباع؟',
         'عندما يركب مصنع محطة طاقة شمسية كهروضوئية على أسطحه، يتحول من مستهلك عادي إلى مشارك نشط في الشبكة. فبينما يضخ العاكس الشمسي الطاقة الفعالة إلى الشبكة '
         'في ساعات الظهيرة، تظل محركات المصنع تسحب تياراً مغناطيسياً حثياً من خطوط الشبكة. '
         'بدون عداد رباعي الأرباع، تعجز الشركة عن معرفة ما إذا كانت القدرة غير الفعالة مسحوبة بواسطة المصنع أو محقونة عبر العواكس الشمسية. '
         'تلزم شركات الكهرباء بهذه العدادات الذكية المعتمدة ببروتوكول DLMS/COSEM لتطبيق لوائح ربط الشبكة وتطبيق غرامات انخفاض معامل القدرة عن 0.90.'),
        ('كيف يساعد العداد رباعي الأرباع مديري الصيانة على إلغاء غرامات معامل القدرة في الفواتير؟',
         'تتضمن فواتير الكهرباء الصناعية والتجارية غرامات مالية باهظة تُعرف بغرامات انخفاض معامل القدرة (Power Factor Penalties) الناتجة عن استهلاك الطاقة غير الفعالة. '
         'يوفر العداد رباعي الأرباع منحنيات حمل مفصلة كل 15 دقيقة توضح حجم الطاقة غير الفعالة الحثية والسعوية في أوقات الذروة وخارجها. '
         'تمكن هذه البيانات مهندسي المصانع من ضبط وتحديد سعات بنوك مكثفات تحسين معامل القدرة الأوتوماتيكية بدقة متناهية، مما يلغي هذه الغرامات تماماً.')
    ],
    cta='هل تخطط لمشاريع ربط محطات الطاقة الشمسية الصناعية بالشبكة أو تصميم لوحات التوزيع الذكية التي تتطلب عدادات رباعية الأرباع فئة 0.5S؟ تصنع يمين (YOMIN) عدادات طاقة ذكية معتمدة بمعايير IEC 62053 وDLMS/COSEM.',
    body='''
<h2>ديناميكيات القدرة الكهربائية المعقدة في عصر التوليد الموزع</h2>
<p>أحدث التوسع الهائل في مشاريع الطاقة الشمسية الكهروضوئية الموزعة على أسطح المنشآت الصناعية والمستودعات التجارية تحولاً جذرياً في مسارات الطاقة الكهربائية. لم تعد المصانع مجرد مستهلك سلبي للكهرباء، بل باتت مراكز إنتاج نشطة تستورد وتصدر الطاقة باستمرار.</p>
<p>ومع ذلك، فإن سريان التيار المتردد لا يقتصر على <strong>القدرة الفعالة (واط)</strong> التي تنجز الشغل الميكانيكي والحراري، بل يتطلب أيضاً <strong>القدرة غير الفعالة (فار)</strong> اللازمة لبناء المجالات المغناطيسية في المحركات والمحولات.</p>
<p>يعد <strong>عداد الطاقة رباعي الأرباع</strong> أداة القياس المترولوجية الحاسمة التي توفر محاسبة اتجاهية كاملة بزاوية 360 درجة لجميع تدفقات القدرة الفعالة وغير الفعالة عبر نقاط الربط الكهربائي.</p>

<h2>شرح أرباع التشغيل الأربعة للقدرة الكهربائية</h2>
<p>في الهندسة الكهربائية، تُمثّل متجهات تدفق القدرة في نظام إحداثي ديكارتي ثنائي الأبعاد، حيث يمثل المحور الأفقي القدرة الفعالة (P) ويمثل المحور الرأسي القدرة غير الفعالة (Q):</p>
<table>
  <thead>
    <tr>
      <th>الربع الكهربائي</th>
      <th>متجه القدرة</th>
      <th>اتجاه سريان الطاقة</th>
      <th>حالة التشغيل الفعلية في المنشأة الصناعية</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>الربع الأول (Q1)</strong></td>
      <td><strong>+P, +Q</strong></td>
      <td><strong>استيراد قدرة فعالة، حمل حثي (متأخر)</strong></td>
      <td>الاستهلاك الصناعي المعتاد: سحب الطاقة الفعالة وغير الفعالة من الشبكة لتشغيل المحركات الحثية والمحولات.</td>
    </tr>
    <tr>
      <td><strong>الربع الثاني (Q2)</strong></td>
      <td><strong>-P, +Q</strong></td>
      <td><strong>تصدير قدرة فعالة، حمل حثي (متقدم)</strong></td>
      <td>محطة طاقة شمسية تصدر الكهرباء الفعالة للشبكة بينما تسحب الأحمال المساعدة طاقة غير فعالة لبناء المغناطيسية.</td>
    </tr>
    <tr>
      <td><strong>الربع الثالث (Q3)</strong></td>
      <td><strong>-P, -Q</strong></td>
      <td><strong>تصدير قدرة فعالة، حمل سعوي (متأخر)</strong></td>
      <td>مولد تزامني أو عاكس شمسي ذكي يولد الطاقة الفعالة ويضخ في الوقت نفسه دعماً من القدرة غير الفعالة لتثبيت جهد الشبكة.</td>
    </tr>
    <tr>
      <td><strong>الربع الرابع (Q4)</strong></td>
      <td><strong>+P, -Q</strong></td>
      <td><strong>استيراد قدرة فعالة، حمل سعوي (متقدم)</strong></td>
      <td>المنشأة تستورد الطاقة الفعالة مع وجود فائض تعويض سعوي ناتج عن بنوك مكثفات زائدة أو كابلات أرضية مفرغة.</td>
    </tr>
  </tbody>
</table>
'''
)

# ==============================================================================
# 2. SPLIT-TYPE STS PREPAID ENERGY METER (EN, FR, ES, AR)
# ==============================================================================

SPLIT_PREPAID_EN = dict(
    lang='en',
    dir='ltr',
    slug='anti-tamper-revenue-protection-what-is-a-split-prepaid-meter',
    title='Utility Revenue Protection & Anti-Tamper: What Is a Split Prepaid Meter?',
    breadcrumb='Energy Meters',
    read='10 min read',
    alt='Split-type STS prepaid electricity meter showing outdoor pole-mounted MCU and indoor wireless CIU customer keypad unit',
    desc=('Utility non-technical loss reduction and anti-tamper revenue protection: What is a split prepaid meter? '
          'How split-architecture STS electricity meters separate the outdoor Measurement & Control Unit (MCU) from the indoor Customer Interface Unit (CIU) to eliminate power theft.'),
    model='Model STE / YM-STS Series Single-Phase & Three-Phase Split Prepayment Electricity Meters',
    category='Energy Meters / STS Prepayment Systems',
    kw='what is a split prepaid meter &middot; split prepayment meter &middot; sts prepaid meter &middot; anti tamper electric meter &middot; customer interface unit ciu',
    specs=[
        ('System Architecture', 'Split two-part architecture: Outdoor Measurement and Control Unit (MCU) paired with Indoor Customer Interface Unit (CIU) keypad'),
        ('Communication Medium', 'Power Line Carrier (PLC), Wireless Radio Frequency (RF 433/868 MHz), or M-Bus cable communicating up to 150m between MCU and CIU'),
        ('Token Encryption Standard', 'Standard Transfer Specification (STS) compliant; 20-digit encrypted numeric tokens adhering to IEC 62055-41 and IEC 62055-51'),
        ('Rated Voltage & Current', 'Single-Phase 230V AC (5(60)A or 5(80)A) and Three-Phase 3&times;230/400V AC (5(100)A frame sizes); 50Hz / 60Hz frequency'),
        ('Disconnection Mechanism', 'Internal heavy-duty bi-stable magnetic latching relay (100A rated contact) disconnecting load automatically at zero credit'),
        ('Multi-Sensor Anti-Tamper Protection', 'Dual current sensors (Phase and Neutral current measurement), terminal cover open sensor, magnetic field detector (&ge; 0.4T), reverse energy trip'),
        ('Enclosure & Ingress Protection', 'Outdoor MCU: IP54/IP65 UV-resistant polycarbonate enclosure for pole-top or boundary wall mounting; Indoor CIU: IP51 wall/tabletop mount'),
        ('Applicable International Standards', 'IEC 62052-11, IEC 62053-21 (Class 1.0), IEC 62055-31, IEC 62055-41, STS Association certified')
    ],
    faqs=[
        ('What is a split prepaid meter and how does its physical architecture prevent electricity theft?',
         'A split prepaid meter divides the traditional all-in-one electricity meter into two physically separated components: '
         '1. **Measurement and Control Unit (MCU):** The actual metering computer and 100A disconnect relay, mounted high up on an outdoor utility distribution pole '
         'or locked inside a secure street boundary enclosure beyond the consumer\'s physical reach. '
         '2. **Customer Interface Unit (CIU):** A convenient indoor keypad device placed inside the consumer\'s home or apartment, equipped with an LCD display and numeric keys. '
         'The consumer enters their 20-digit STS recharge token on the indoor CIU keypad. The token is transmitted wirelessly (via RF) or through existing power wiring (PLC) '
         'to the outdoor MCU, which credits the account. Because the actual metering unit and power lines are physically inaccessible to the consumer, '
         'illegal line bridging, meter shunting, and physical tampering are eliminated.'),
        ('How does the dual-sensor measurement technology inside the MCU detect neutral bypass tampering?',
         'A common method of electricity theft involves disconnecting the meter\'s neutral wire and grounding the home circuits locally, or introducing an illegal bypass '
         'wire across the live terminals so current bypasses the measuring element. '
         'YOMIN split prepaid MCUs incorporate **dual current sensors** measuring current independently in both the active phase wire and the neutral wire. '
         'Under normal conditions, phase current matches neutral current exactly. If an unbalanced bypass or earth leakage is detected exceeding a preset threshold (e.g. 6.25%), '
         'the MCU firmware immediately logs a tamper event, lights a tamper warning LED, continues billing on whichever conductor carries higher current, '
         'or trips the internal relay, completely thwarting bypass theft.'),
        ('What is the Standard Transfer Specification (STS) and how does token encryption protect utility revenue?',
         'The Standard Transfer Specification (STS) is the globally recognized open international standard (IEC 62055) for secure prepayment vending systems. '
         'When a consumer purchases electricity at a vending station or mobile banking app, the central vending software generates a unique **20-digit encrypted numeric token**. '
         'This token contains encrypted instructions including the exact kilowatt-hour value, a unique transaction sequence number, and the specific meter serial number. '
         'The token cannot be decoded by any other meter, cannot be reused twice, and cannot be counterfeited, guaranteeing absolute revenue security for the power utility.')
    ],
    cta='Combating non-technical losses, unauthorized bypasses, and metering tampering across municipal, rural, or commercial utility networks? YOMIN manufactures STS-certified split prepayment electricity meters engineered to IEC 62055 standards.',
    body='''
<h2>Eliminating Non-Technical Losses in Modern Power Utilities</h2>
<p>For electric distribution utilities across developing economies, non-technical losses (electricity theft, meter tampering, unbilled consumption, and non-payment) represent an existential financial crisis. In many regional power networks, non-technical losses exceed 20% to 35% of total generated electricity, starving utilities of the capital required to maintain power plants and expand grid infrastructure.</p>
<p>Traditional integrated prepayment meters—where the keypad and measurement electronics reside in a single box installed inside the customer\'s hallway—remain vulnerable to physical assault. Determined fraudsters drill enclosure walls, insert foreign objects to jam relays, place powerful neodymium magnets over current coils, or tap incoming service drop cables before the meter.</p>
<p>The <strong>Split-Type STS Prepaid Electricity Meter</strong> solves this vulnerability through physical segregation, relocating the metering core beyond the reach of consumers while preserving an effortless indoor recharging experience.</p>

<h2>Split Architecture: MCU vs. CIU Integration</h2>
<p>A certified split prepayment system operates across two discrete functional nodes communicating via Power Line Carrier (PLC) or wireless Radio Frequency (RF):</p>
<table>
  <thead>
    <tr>
      <th>System Component</th>
      <th>Physical Location</th>
      <th>Core Functional Hardware</th>
      <th>Security Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Measurement & Control Unit (MCU)</strong></td>
      <td>Outdoor utility pole crossarm, secure boundary meter kiosk, or locked multi-meter riser cabinet.</td>
      <td>Class 1.0 metering microchip, dual phase/neutral current sensors, 100A bi-stable latching relay, tamper-proof terminal block.</td>
      <td>Performs all legal metrology and automated power disconnection. Completely physically inaccessible to building occupants.</td>
    </tr>
    <tr>
      <td><strong>Customer Interface Unit (CIU)</strong></td>
      <td>Indoor kitchen or living room wall, plugged into a standard electrical outlet or battery operated.</td>
      <td>Tactile 12-key numeric keypad, high-contrast backlit LCD screen, audible low-credit buzzer alarm.</td>
      <td>Allows consumers to enter 20-digit STS tokens, check remaining kWh credit balance, view instantaneous load, and track consumption history.</td>
    </tr>
  </tbody>
</table>
'''
)

SPLIT_PREPAID_FR = dict(
    lang='fr',
    dir='ltr',
    slug='anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-fr',
    title='Protection des Recettes Énergétiques & Anti-Fraude : Qu\'est-ce qu\'un Compteur Prépaiement Split ?',
    breadcrumb='Compteurs d\'Énergie',
    read='10 min de lecture',
    alt='Système de comptage prépayé STS de type split montrant l\'unité de mesure extérieure MCU sur poteau et le clavier intérieur CIU',
    desc=('Réduction des pertes non techniques et protection des recettes des distributeurs : Qu\'est-ce qu\'un compteur prépayé split ? '
          'Comment l\'architecture séparée (MCU extérieure et clavier CIU intérieur) élimine les fraudes et le vol d\'électricité.'),
    model='Série STE / YM-STS : Compteurs d\'Électricité Prépaiement Split Monophasés et Triphasés STS',
    category='Compteurs d\'Énergie / Systèmes de Prépaiement STS',
    kw='compteur prépayé split &middot; compteur prépaiement sts &middot; unité d\'interface client ciu &middot; protection des recettes &middot; compteur anti fraude',
    specs=[
        ('Architecture du Système', 'Architecture séparée en deux parties : Unité de Mesure et de Contrôle (MCU) extérieure et Unité d\'Interface Client (CIU) intérieure'),
        ('Support de Communication', 'Courants Porteurs en Ligne (CPL / PLC), Radiofréquence sans fil (RF 433/868 MHz), ou câble M-Bus jusqu\'à 150 mètres'),
        ('Norme de Cryptage des Tokens', 'Conforme à la spécification Standard Transfer Specification (STS) ; tokens numériques cryptés à 20 chiffres (CEI 62055-41/51)'),
        ('Tension et Courant Nominaux', 'Monophasé 230V AC (5(60)A ou 5(80)A) et Triphasé 3&times;230/400V AC (5(100)A) ; fréquence 50Hz / 60Hz'),
        ('Mécanisme de Coupure', 'Relais bistable magnétique interne haute puissance (contact 100A) coupant la charge automatiquement à crédit nul'),
        ('Protection Anti-Fraude Multi-Capteurs', 'Double capteur de courant (mesure de phase et de neutre), détection d\'ouverture de capot, blindage magnétique (&ge; 0,4T)'),
        ('Boîtier et Indice de Protection', 'MCU extérieure : IP54/IP65 en polycarbonate résistant aux UV pour montage sur poteau ; CIU intérieure : boîtier IP51 mural ou sur table'),
        ('Normes Internationales Applicables', 'CEI 62052-11, CEI 62053-21 (Classe 1.0), CEI 62055-31, CEI 62055-41, certifié par l\'Association STS')
    ],
    faqs=[
        ('Qu\'est-ce qu\'un compteur prépayé split et comment son architecture physique empêche-t-elle le vol d\'électricité ?',
         'Un compteur prépayé de type "split" divise le compteur d\'électricité traditionnel en deux composants physiquement séparés : '
         '1. **L\'Unité de Mesure et de Contrôle (MCU) :** Le véritable compteur électronique équipé du relais de coupure de 100A, installé en hauteur sur un poteau '
         'électrique extérieur ou verrouillé dans une armoire de distribution en limite de propriété, hors de portée de l\'abonné. '
         '2. **L\'Unité d\'Interface Client (CIU) :** Un boîtier à clavier ergonomique placé à l\'intérieur du logement de l\'usager, doté d\'un écran LCD et de touches numériques. '
         'L\'abonné saisit son code de recharge STS à 20 chiffres sur le clavier intérieur du CIU. Le code est transmis sans fil (RF) ou par le réseau électrique (CPL) '
         'à l\'unité MCU extérieure qui crédite le compte. Comme le compteur réel et les câbles d\'arrivée sont physiquement inaccessibles au consommateur, '
         'les dérivations frauduleuses et les altérations mécaniques sont totalement éliminées.'),
        ('Comment la technologie de mesure à double capteur de la MCU détecte-t-elle la fraude par dérivation du neutre ?',
         'Une méthode classique de fraude consiste à déconnecter le câble de neutre du compteur pour le relier à une terre locale, ou à shunter la phase '
         'pour qu\'une partie du courant ne soit pas mesurée. '
         'Les unités MCU split YOMIN intègrent un **double capteur de courant** mesurant indépendamment le courant dans la phase et dans le neutre. '
         'En régime normal, le courant de phase équilibre parfaitement le courant de neutre. Dès qu\'une dérivation ou fuite anormale dépasse un seuil de 6,25%, '
         'le compteur enregistre immédiatement une alerte de fraude, allume un voyant d\'avertissement et continue de facturer sur le conducteur transportant '
         'le courant le plus élevé, voire coupe le relais d\'alimentation.'),
        ('Qu\'est-ce que la norme STS (Standard Transfer Specification) et comment protège-t-elle les revenus des distributeurs ?',
         'La spécification STS est la norme internationale ouverte (CEI 62055) de référence pour les systèmes de prépaiement sécurisés. '
         'Lorsqu\'un usager achète de l\'électricité au guichet, sur une borne ou via une application mobile, le logiciel d\'émission génère un code crypté unique '
         'de **20 chiffres (Token STS)**. Ce code contient les kilowattheures achetés, un numéro de séquence et le numéro de série spécifique du compteur. '
         'Le code ne peut être utilisé que sur ce seul compteur, ne peut jamais être réutilisé une seconde fois et ne peut pas être contrefait, garantissant '
         'une sécurité financière totale pour la compagnie d\'électricité.')
    ],
    cta='Vous luttez contre les pertes non techniques, le vol d\'électricité et les fraudes sur vos réseaux de distribution électrique ? YOMIN fabrique des compteurs communicants prépayés split certifiés STS selon les normes CEI 62055.',
    body='''
<h2>Éliminer les Pertes Non Techniques des Compagnies d'Électricité</h2>
<p>Pour les distributeurs d'énergie, les pertes non techniques (fraude, raccordements clandestins, compteurs trafiqués et impayés) représentent un fardeau financier majeur. Dans de nombreux pays, ces pertes dépassent 20 à 30 % de l'énergie injectée sur le réseau, privant les opérateurs des ressources nécessaires pour entretenir les infrastructures.</p>
<p>Les compteurs prépayés monoblocs traditionnels—dont le clavier et l'unité de mesure sont réunis dans un même boîtier installé dans l'entrée du domicile—restent très vulnérables aux manipulations malveillantes : perçage du boîtier, aimants puissants perturbant les bobines ou pontage direct des câbles d'arrivée.</p>
<p>Le <strong>Compteur d'Électricité Prépaiement Split STS</strong> résout définitivement ce problème en délocalisant le cœur de comptage hors de portée des usagers, tout en offrant une interface de recharge intérieure simple et conviviale.</p>

<h2>Architecture Split : Séparation Fonctionnelle entre MCU et CIU</h2>
<p>Un système de prépaiement split certifié repose sur deux unités distinctes communiquant par Courants Porteurs en Ligne (CPL) ou par liaison Radiofréquence (RF) :</p>
<table>
  <thead>
    <tr>
      <th>Composant du Système</th>
      <th>Emplacement Physique</th>
      <th>Éléments Matériels Intégrés</th>
      <th>Fonction de Sécurité</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Unité de Mesure et de Contrôle (MCU)</strong></td>
      <td>Sur poteau électrique en hauteur, armoire de coupure extérieure cadenassée ou gaine technique fermée.</td>
      <td>Puce de métrologie Classe 1.0, double capteur phase/neutre, relais de coupure bistable 100A, bornier scellé.</td>
      <td>Exécute la mesure légale et la coupure automatique. Totalement inaccessible physiquement aux occupants du bâtiment.</td>
    </tr>
    <tr>
      <td><strong>Unité d'Interface Client (CIU)</strong></td>
      <td>Dans la cuisine ou le salon de l'usager, posée sur une table ou fixée au mur sur une prise standard.</td>
      <td>Clavier numérique tactile 12 touches, écran LCD rétroéclairé, avertisseur sonore de crédit faible.</td>
      <td>Permet à l'abonné de saisir les codes de recharge STS à 20 chiffres, de consulter son crédit restant en kWh et de surveiller sa consommation.</td>
    </tr>
  </tbody>
</table>
'''
)

SPLIT_PREPAID_ES = dict(
    lang='es',
    dir='ltr',
    slug='anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-es',
    title='Protección de Ingresos de Servicios Públicos y Antifraude: ¿Qué es un Medidor Prepago Dividido (Split)?',
    breadcrumb='Medidores de Energía',
    read='10 min de lectura',
    alt='Sistema de medición prepago STS tipo split que muestra la unidad de medición exterior MCU en poste y el teclado de usuario interior CIU',
    desc=('Reducción de pérdidas no técnicas y protección de ingresos para distribuidoras eléctricas: ¿Qué es un medidor prepago split? '
          'Cómo la arquitectura dividida (MCU exterior y teclado CIU interior) elimina el robo de electricidad y las conexiones fraudulentas.'),
    model='Serie STE / YM-STS: Medidores de Electricidad Prepago Split Monofásicos y Trifásicos STS',
    category='Medidores de Energía / Sistemas Prepago STS',
    kw='medidor prepago split &middot; medidor prepago sts &middot; unidad de interfaz de cliente ciu &middot; medidor antifraude &middot; protección de ingresos eléctricos',
    specs=[
        ('Arquitectura del Sistema', 'Arquitectura dividida en dos componentes: Unidad de Medición y Control (MCU) exterior y Teclado de Interfaz de Cliente (CIU) interior'),
        ('Medio de Comunicación', 'Corrientes Portadoras por Línea de Potencia (PLC), Radiofrecuencia inalámbrica (RF 433/868 MHz), o cable M-Bus hasta 150 metros'),
        ('Estándar de Encriptación de Tokens', 'Cumple con la especificación Standard Transfer Specification (STS); tokens numéricos encriptados de 20 dígitos (IEC 62055-41/51)'),
        ('Tensión y Corriente Nominal', 'Monofásico 230V AC (5(60)A o 5(80)A) y Trifásico 3&times;230/400V AC (5(100)A); frecuencia 50Hz / 60Hz'),
        ('Mecanismo de Desconexión', 'Relé magnético biestable de alta potencia (contacto de 100A) que desconecta la carga automáticamente al agotarse el saldo'),
        ('Protección Antifraude Multicontacto', 'Doble sensor de corriente (medición independiente en fase y neutro), detección de apertura de tapa y sensor de campo magnético (&ge; 0,4T)'),
        ('Gabinete y Grado de Protección', 'MCU exterior: gabinete IP54/IP65 de policarbonato con protección UV para montaje en poste; CIU interior: gabinete IP51 de pared o sobremesa'),
        ('Normas Internacionales Aplicables', 'IEC 62052-11, IEC 62053-21 (Clase 1.0), IEC 62055-31, IEC 62055-41, certificado por la Asociación STS')
    ],
    faqs=[
        ('¿Qué es un medidor prepago dividido (split) y cómo su arquitectura previene el hurto de energía?',
         'Un medidor prepago tipo split divide el medidor eléctrico tradicional en dos elementos físicamente separados: '
         '1. **Unidad de Medición y Control (MCU):** El verdadero equipo de medición y el relé de desconexión de 100A, instalados en lo alto de un poste de distribución '
         'o en una caja blindada en la vía pública, fuera del alcance físico del usuario. '
         '2. **Unidad de Interfaz de Cliente (CIU):** Un teclado colocado cómodamente en la sala o cocina del usuario, con pantalla LCD y teclas numéricas. '
         'El usuario ingresa su token de recarga STS de 20 dígitos en el teclado del CIU. El código se transmite por radiofrecuencia (RF) o por el cable eléctrico (PLC) '
         'hacia la MCU exterior, que acredita los kilovatios-hora. Al estar el medidor real fuera del alcance físico del usuario, se elimina el bypass y la manipulación ilícita.'),
        ('¿Cómo detecta la MCU las conexiones clandestinas y la manipulación del neutro?',
         'Un método habitual de fraude consiste en desconectar el neutro del medidor y conectarlo a una jabalina a tierra, o puentear la fase para que parte de la corriente '
         'no pase por el sensor. '
         'Las unidades MCU split de YOMIN incorporan **doble sensor de corriente** que mide simultáneamente la fase y el neutro. '
         'Si se detecta un desbalance superior al 6,25% entre ambos conductores, el firmware registra de inmediato una alarma de fraude y continúa facturando sobre el cable '
         'que registre mayor corriente, o bien activa la desconexión del relé.'),
        ('¿Qué es el estándar STS y cómo garantiza los ingresos de la empresa distribuidora?',
         'El estándar STS (Standard Transfer Specification) es la norma internacional abierta (IEC 62055) más segura para la venta prepaga de energía. '
         'Al recargar energía en un punto de venta o aplicación bancaria, el software genera un **token numérico encriptado de 20 dígitos**. '
         'Este código contiene los kWh adquiridos, el número de serie único del medidor y una secuencia irrepetible. '
         'El token solo puede ser leído por ese medidor específico, no puede duplicarse ni reutilizarse, garantizando la total seguridad de los ingresos de la empresa de servicios públicos.')
    ],
    cta='¿Busca reducir pérdidas no técnicas y erradicar el fraude en sus redes de distribución eléctrica? YOMIN fabrica medidores prepago split certificados bajo el estándar internacional STS e IEC 62055.',
    body='''
<h2>Reducción de Pérdidas No Técnicas en Empresas de Distribución Eléctrica</h2>
<p>Para las compañías eléctricas de distribución, las pérdidas no técnicas (robo de electricidad, alteraciones de medidores, conexiones clandestinas e impagos) generan un severo impacto financiero, reduciendo la capacidad de inversión en nuevas subestaciones y redes.</p>
<p>Los medidores prepago tradicionales integrados—donde el teclado y la unidad de corte comparten la misma caja instalada dentro del inmueble del cliente—son muy vulnerables a taladros, imanes de neodimio y puentes en los bornes de entrada.</p>
<p>El <strong>Medidor de Electricidad Prepago Tipo Split STS</strong> resuelve esta debilidad mediante la segregación física del equipo: ubica el núcleo de medición fuera del alcance del usuario y mantiene un teclado interior cómodo para la recarga de saldo.</p>

<h2>Arquitectura Dividida: Integración entre MCU y CIU</h2>
<p>Un sistema de medición prepaga split certificado opera mediante dos nodos complementarios que se comunican por Corrientes Portadoras (PLC) o Radiofrecuencia (RF):</p>
<table>
  <thead>
    <tr>
      <th>Componente del Sistema</th>
      <th>Ubicación Física</th>
      <th>Hardware Integrado</th>
      <th>Función de Seguridad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Unidad de Medición y Control (MCU)</strong></td>
      <td>En poste de distribución exterior en altura o armario concentrador bajo llave en fachada.</td>
      <td>Chip de medición Clase 1.0, doble sensor de corriente fase/neutro, relé biestable de 100A, bornera sellada.</td>
      <td>Realiza la medición legal y la desconexión automática. Completamente inaccesible físicamente para el usuario.</td>
    </tr>
    <tr>
      <td><strong>Unidad de Interfaz de Cliente (CIU)</strong></td>
      <td>En el interior de la vivienda (cocina o sala), conectada a un enchufe o con pilas.</td>
      <td>Teclado numérico táctil de 12 teclas, pantalla LCD retroiluminada, alarma sonora de saldo bajo.</td>
      <td>Permite ingresar los códigos STS de 20 dígitos, revisar el saldo disponible en kWh y monitorear el consumo en tiempo real.</td>
    </tr>
  </tbody>
</table>
'''
)

SPLIT_PREPAID_AR = dict(
    lang='ar',
    dir='rtl',
    slug='anti-tamper-revenue-protection-what-is-a-split-prepaid-meter-ar',
    title='حماية إيرادات المرافق ومكافحة التلاعب: ما هو عداد الدفع المسبق المنفصل (Split)؟',
    breadcrumb='عدادات الطاقة',
    read='10 دقائق قراءة',
    alt='نظام عداد كهرباء مسبق الدفع بنظام STS المنفصل يوضح وحدة القياس الخارجية على العمود ووحدة لوحة المفاتيح الداخلية للمستهلك',
    desc=('تقليل الفاقد غير الفني وحماية إيرادات شركات الكهرباء: ما هو عداد الدفع المسبق المنفصل (Split)؟ '
          'كيف يفصل هذا النظام وحدة القياس والتحكم الخارجية (MCU) عن لوحة مفاتيح المستهلك الداخلية (CIU) للقضاء التام على سرقة الكهرباء.'),
    model='سلسلة STE / YM-STS: عدادات الكهرباء مسبقة الدفع المنفصلة أحادية وثلاثية الأطوار STS',
    category='عدادات الطاقة / أنظمة الدفع المسبق STS',
    kw='عداد دفع مسبق منفصل &middot; عداد كهرباء split &middot; عداد sts &middot; وحدة واجهة المستهلك ciu &middot; مكافحة سرقة الكهرباء &middot; حماية الإيرادات',
    specs=[
        ('هندسة وبنية النظام', 'بنية منفصلة ثنائية الأجزاء: وحدة قياس وتحكم خارجية (MCU) مقترنة بوحدة واجهة للمستهلك داخلية (CIU) مزودة بلوحة مفاتيح'),
        ('وسط الاتصال ونقل البيانات', 'الاتصال عبر خطوط القدرة (PLC) أو الترددات اللاسلكية (RF 433/868 MHz) أو كابل M-Bus لمسافة تصل إلى 150 متراً'),
        ('معيار تشفير أكواد الشحن', 'متوافق تماماً مع مواصفات النقل القياسية (STS)؛ أكواد شحن رقمية مشفرة من 20 رقماً وفقاً لمعايير IEC 62055-41/51'),
        ('الجهد والتيار الاسمي', 'أحادي الطور 230V تيار متردد (5(60)A أو 5(80)A) وثلاثي الأطوار 3&times;230/400V (سعة 5(100)A)؛ تردد 50Hz / 60Hz'),
        ('آلية الفصل والتوصيل التلقائي', 'مرحل مغناطيسي ثنائي الاستقرار شديد التحمل (سعة 100A) يفصل التيار تلقائياً وبأمان فوري عند نفاد الرصيد'),
        ('حماية متعددة الحساسات ضد العبث', 'حساسات تيار مزدوجة (قياس مستقل لتيار الطور وتيار المحايد)، كاشف فتح الغطاء، وحماية ضد المجالات المغناطيسية (&ge; 0.4T)'),
        ('صندوق الحماية ومقاومة العوامل الجوية', 'الوحدة الخارجية MCU: حماية IP54/IP65 من البولي كربونات المقاوم للأشعة فوق البنفسجية للتركيب على الأعمدة؛ الوحدة الداخلية CIU: حماية IP51'),
        ('المعايير الدولية المعتمدة', 'IEC 62052-11، IEC 62053-21 (فئة 1.0)، IEC 62055-31، IEC 62055-41، معتمد رسمياً من منظمة STS')
    ],
    faqs=[
        ('ما هو عداد الدفع المسبق المنفصل (Split) وكيف تمنع بنيته الفيزيائية سرقة الكهرباء؟',
         'يقسم عداد الدفع المسبق المنفصل عداد الكهرباء التقليدي إلى جزأين منفصلين تماماً: '
         '1. **وحدة القياس والتحكم (MCU):** وهي العداد الحقيقي الذي يحتوي على شريحة القياس الدقيقة ومرحل الفصل سعة 100 أمبير، ويتم تركيبه في مكان مرتفع '
         'على أعمدة الكهرباء في الشارع أو داخل صندوق توزيع مصفح ومغلق خارج العقار تماماً بعيداً عن متناول المستهلك. '
         '2. **وحدة واجهة المستهلك (CIU):** جهاز مريح مزود بشاشة ولوحة مفاتيح يوضع داخل شقة أو منزل المستهلك على طاولة أو جدار داخلي. '
         'يقوم المستهلك بإدخال كود الشحن (Token) المكون من 20 رقماً عبر لوحة المفاتيح الداخلية. تُنقل الشفرة لاسلكياً (RF) أو عبر أسلاك الكهرباء (PLC) '
         'إلى وحدة القياس الخارجية التي تضيف الرصيد في ثوانٍ. وبما أن العداد وكابلات الخدمة تقع خارج المنزل تماماً، يتم القضاء على محاولات التوصيل المباشر أو التلاعب.'),
        ('كيف تكشف تقنية حساسات التيار المزدوجة داخل وحدة MCU التلاعب بسلك المحايد (Neutral)؟',
         'تعتمد إحدى الطرق الشائعة للسرقة على فصل سلك المحايد عن العداد وتوصيل أحمال المنزل بالأرضي، أو عمل جسر (Bypass) يتجاوز العداد جزئياً. '
         'تحتوي وحدات MCU المنفصلة من يمين (YOMIN) على **حساسي تيار مستقلين** لقياس التيار المار في خط الطور (الحار) وخط المحايد (البارد) بالتزامن. '
         'في الوضع الطبيعي، يتطابق التياران تماماً. فإذا رصد المعالج أي تفاوت يتجاوز 6.25%، يسجل العداد فوراً واقعة تلاعب، ويطلق إنذاراً ضوئياً، '
         'ويواصل احتساب الاستهلاك وفقاً للقيمة الأعلى بين السلكين أو يفصل التيار تماماً، مما يحبط محاولات السرقة فوراً.'),
        ('ما هو معيار STS العالمي وكيف يحمي نظام التشفير إيرادات شركات ومؤسسات الكهرباء؟',
         'معيار مواصفات النقل القياسية (STS) هو المعيار العالمي المفتوح (IEC 62055) المعتمد لأنظمة الدفع المسبق الآمنة للكهرباء والمياه. '
         'عندما يشتري المشترك رصيداً عبر منافذ الشحن أو التطبيقات البنكية، يولد برنامج نقاط البيع **رمزاً رقمياً مشفراً مكوناً من 20 رقماً**. '
         'يحتوي هذا الرمز على كمية الكيلوواط ساعة المشتراة ورقم تسلسلي فريد مرتبط برقم العداد الحصري. '
         'لا يمكن قراءة هذا الرمز أو قبوله إلا بواسطة العداد المخصص له فقط، ولا يمكن إعادة استخدامه، مما يضمن أماناً مالياً مطلقاً لشركات التوزيع.')
    ],
    cta='هل تسعى للقضاء على الفاقد التجاري غير الفني والتلاعب بالعدادات في شبكات التوزيع البلدية والريفية؟ تصنع يمين (YOMIN) عدادات دفع مسبق منفصلة معتمدة بمعايير STS وIEC 62055 العالمية.',
    body='''
<h2>القضاء على الفاقد غير الفني في شبكات توزيع الكهرباء الحديثة</h2>
<p>تشكل الخسائر غير الفنية (المتمثلة في سرقة الكهرباء، والتلاعب بالعدادات، والربط غير القانوني، وتراكم المستحقات غير المحصلة) أزمة مالية خانقة لشركات وهيئات توزيع الكهرباء في مختلف الأسواق النامية. إذ تتجاوز هذه الخسائر في بعض الشبكات 20% إلى 35% من إجمالي الطاقة المولدة، مما يحرم الشركات من الموارد اللازمة لتحديث محطات التحويل وتطوير البنية التحتية.</p>
<p>تظل عدادات الدفع المسبق التقليدية المدمجة—حيث تتواجد لوحة المفاتيح وشريحة القياس ومرحل الفصل داخل صندوق واحد مركب في مدخل منزل المستهلك—عرضة للاعتداءات الفيزيائية والحيل التقنية، كاستخدام مغناطيسات النيوديميوم القوية أو ثقب الصندوق أو عمل وصلات غير مشروعة قبل العداد.</p>
<p>يقدم <strong>عداد الكهرباء مسبق الدفع المنفصل بنظام STS (Split-Type Meter)</strong> الحل الهندسي الجذري لهذه المعضلة عبر الفصل المكاني التام، حيث يُنقل قلب القياس خارج نطاق وصول المشترك مع الحفاظ على تجربة شحن منزلية غاية في السلاسة والراحة.</p>

<h2>البنية المنفصلة: التكامل التشغيلي بين وحدة القياس MCU ووحدة المشترك CIU</h2>
<p>يعمل نظام الدفع المسبق المنفصل المعتمد عبر وحدتين مستقلتين وظيفياً تتواصلان بواسطة خطوط القدرة الكهربائية (PLC) أو عبر الترددات الراديوية اللاسلكية (RF):</p>
<table>
  <thead>
    <tr>
      <th>عنصر النظام</th>
      <th>موقع التركيب الفيزيائي</th>
      <th>المكونات الصلبة والعتاد المدمج</th>
      <th>الدور الأمني والوقائي</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>وحدة القياس والتحكم (MCU)</strong></td>
      <td>في أعلى أعمدة توزيع الكهرباء الخارجية بالشارع، أو داخل خزائن توزيع مصفحة مغلقة على جدران المبنى الخارجية.</td>
      <td>شريحة قياس دقيقة فئة 1.0، حسّاسا تيار مستقلان للطور والمحايد، مرحل فصل مغناطيسي 100A، أطراف توصيل محكمة الغلق.</td>
      <td>مسؤولة عن القياس المترولوجي القانوني والفصل الآلي للتيار. معزولة تماماً وغير قابلة للوصول الفيزيائي من قبل المشتركين.</td>
    </tr>
    <tr>
      <td><strong>وحدة واجهة المستهلك (CIU)</strong></td>
      <td>داخل مطبخ أو غرفة معيشة المشترك، مثبتة على جدار داخلي أو موضوعة على طاولة وموصلة بمقبس كهربائي قياسي.</td>
      <td>لوحة مفاتيح سيليكونية مرنة من 12 زراً، شاشة LCD واضحة بإضاءة خلفية، جرس إنذار صوتي عند انخفاض الرصيد.</td>
      <td>تتيح للمستهلك إدخال أكواد الشحن المكونة من 20 رقماً، ومتابعة الرصيد المتبقي بالكيلوواط ساعة، ومراقبة استهلاك الطاقة في أي وقت.</td>
    </tr>
  </tbody>
</table>
'''
)

ALL_MULTILINGUAL_POSTS = [
    FOUR_QUADRANT_EN, FOUR_QUADRANT_FR, FOUR_QUADRANT_ES, FOUR_QUADRANT_AR,
    SPLIT_PREPAID_EN, SPLIT_PREPAID_FR, SPLIT_PREPAID_ES, SPLIT_PREPAID_AR
]
