# -*- coding: utf-8 -*-
"""Content module for Central Asia electrical engineering guides:
Current Transformers, Single-Phase Meters, Three-Phase Meters, and Prepaid Meters.
Excludes India/Bangladesh/Pakistan keywords; focuses on Central Asian power grids
(Kazakhstan, Uzbekistan, Kyrgyzstan, Tajikistan, ASKUE/AMR automation, IEC 62053, DLMS/COSEM).
Titles end with "What Is a [Product]?" and URLs end with "what-is-a-[product]".
"""

CT_BLOG = dict(
    slug='substation-measurement-what-is-a-current-transformer',
    title='Substation & Industrial Power Measurement: What Is a Current Transformer?',
    breadcrumb='Current Transformer',
    read='10 min read',
    alt='Epoxy-resin measuring current transformers actively installed over heavy copper busbars inside an industrial substation switchgear cabinet',
    desc=('Substation and industrial electrical measurement in Central Asia: What is a current transformer (CT)? '
          'How window-type, split-core, and cast-resin CTs scale primary current, prevent saturation, and interface with ASKUE energy meters.'),
    model='MSQ / RCT / BH-0.66 Series Low-Voltage Measuring & Protection Current Transformers',
    category='Current Transformer / Substation Measurement',
    kw='what is a current transformer &middot; current transformer working principle &middot; substation current transformer &middot; class 0.5s ct &middot; askue metering ct',
    specs=[
        ('Rated Primary Currents', '30A, 50A, 100A, 200A, 400A, 600A, 800A, 1000A up to 5000A AC Through-Window'),
        ('Rated Secondary Outputs', '5A standard (switchgear meters) or 1A low-burden (long telemetry runs in distributed substations)'),
        ('Measurement Accuracy Classes', 'Class 0.2, Class 0.2S (Revenue Grid Billing), Class 0.5, Class 0.5S (Industrial Feeders), Class 1.0, 5P10 / 10P10 (Protection)'),
        ('Insulation Voltage Rating', '0.66kV / 0.72kV Rated Insulation Voltage; 3kV 50Hz 1-minute power frequency dielectric test withstand'),
        ('Operating Temperature Range', '-40&deg;C to +70&deg;C (Heavy-duty extreme continental winter and arid summer resilience for Central Asian switchrooms)'),
        ('Enclosure & Core Material', 'Self-extinguishing flame-retardant ABS / epoxy resin casting with high-permeability grain-oriented silicon steel toroidal core'),
        ('Mounting Configurations', 'Busbar direct clamping with insulated tightening bolts, surface baseplate mounting, and 35mm DIN-rail snap-fit'),
        ('Applicable International Standards', 'IEC 61869-1, IEC 61869-2, GOST 7746 compliance for Central Asian power grid interconnection')
    ],
    faqs=[
        ('What is a current transformer and why is it essential in industrial substations?',
         'A current transformer (CT) is an instrument transformer designed to produce an alternating current in its secondary winding '
         'proportional to the high AC current flowing in its primary conductor. In heavy industrial substations and distribution switchboards, '
         'primary busbars carry hundreds or thousands of amperes at elevated voltages. Direct connection of measuring instruments or protective '
         'relays is physically impossible and extremely hazardous. The current transformer steps down the massive primary current to a standardized, '
         'safe secondary level (typically 5A or 1A) and provides vital galvanic isolation between high-voltage power circuits and sensitive low-voltage digital meters.'),
        ('What is the difference between Class 0.5 and Class 0.5S current transformers in grid metering?',
         'Standard Class 0.5 current transformers maintain their certified accuracy (&plusmn;0.5% ratio error) between 100% and 120% of rated current, '
         'but experience widening error margins when loads drop below 20%. In contrast, Class 0.5S ("Special") current transformers are engineered '
         'with premium grain-oriented magnetic cores that maintain high permeability down to 1% of rated current. For modern automated metering infrastructure '
         '(ASKUE / AMR) in commercial facilities where load fluctuates widely throughout the 24-hour cycle, Class 0.5S CTs prevent unmetered energy loss during light-load operating periods.'),
        ('Why is an open-circuit secondary condition extremely dangerous in a live current transformer?',
         'Under normal operation, the secondary current produces an opposing demagnetizing flux that counteracts the strong primary magnetomotive force, '
         'leaving only a small resultant core flux. If the secondary circuit is accidentally opened while primary current flows, the opposing secondary '
         'flux collapses to zero. The entire primary current becomes magnetizing current, driving the magnetic core into extreme saturation. '
         'This produces dangerously sharp voltage spikes reaching several thousand volts across the open secondary terminals, presenting a severe risk '
         'of fatal electric shock, dielectric breakdown, and catastrophic CT explosion. Shorting terminal blocks must always be used when disconnecting meters.')
    ],
    cta='Specifying Class 0.2S or 0.5S measuring current transformers for substation switchgear, motor control centers, or Central Asian ASKUE power accounting projects? YOMIN manufactures precision busbar and split-core CTs tested to IEC 61869 standards.',
    body='''
<h2>Current Measurement Challenges in Central Asian Grid Modernization</h2>
<p>Across the high-voltage transmission networks and industrial distribution hubs of Kazakhstan, Uzbekistan, and Central Asia, power utilities are executing large-scale retrofits of Soviet-era distribution substations. A central pillar of this modernization is the transition to <strong>Automated Systems for Commercial Electricity Metering (ASKUE / AMR)</strong>. Central Asian industrial switchgear operates under punishing continental climate extremes—winter ambient temperatures dropping below -40&deg;C in northern mining sectors and summer temperatures exceeding +50&deg;C in desert processing plants.</p>
<p>Accurate electrical monitoring in these environments requires instrument transformers that maintain strict magnetic linearity without thermal drift. The <strong>low-voltage measuring current transformer (CT)</strong> serves as the fundamental sensing gateway, translating primary busbar currents into precision telemetry for digital energy meters and programmable logic controllers.</p>

<h2>Electromagnetic Working Principle of Current Transformers</h2>
<p>Unlike standard power transformers designed to supply voltage to a variable impedance load, a current transformer operates under essentially short-circuited secondary conditions:</p>
<ol>
  <li><strong>Primary Current Conduction:</strong> The primary winding typically consists of the actual power cable or copper busbar passed straight through the central window aperture of the CT (constituting a single primary turn, $N_p = 1$).</li>
  <li><strong>Magnetic Flux Generation:</strong> As alternating current ($I_p$) flows through the primary conductor, it induces an alternating magnetic flux in the circular toroidal core of grain-oriented silicon steel.</li>
  <li><strong>Secondary Current Step-Down:</strong> A high number of secondary turns ($N_s$) wound uniformly around the core generates an induced secondary current ($I_s$) inversely proportional to the turns ratio:
  $$I_s = I_p \times \frac{N_p}{N_s}$$
  For an 800/5A current transformer, $N_s = 160$ turns, stepping 800A down to a manageable 5A for panel instruments.</li>
</ol>

<h2>Comparison of Current Transformer Construction Types</h2>
<p>Industrial panel builders select CT architectures based on retrofit convenience, busbar physical dimensions, and seismic stability:</p>

<table>
  <thead>
    <tr>
      <th>Construction Architecture</th>
      <th>Mechanical Design</th>
      <th>Key Advantages</th>
      <th>Best Application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Window / Busbar Type (MSQ/RCT)</strong></td>
      <td>One-piece molded plastic or resin housing with central rectangular/circular aperture.</td>
      <td>High mechanical strength, compact footprint, lowest cost, excellent thermal dissipation.</td>
      <td>New switchgear assemblies, motor control centers, distribution cubicles.</td>
    </tr>
    <tr>
      <td><strong>Split-Core Type (DP/KCT)</strong></td>
      <td>Two-piece separable magnetic core held together by mechanical clamps.</td>
      <td><strong>Zero power interruption:</strong> clamps around existing live cables without disconnecting busbars.</td>
      <td>Substation retrofits, energy audit logging, temporary power monitoring.</td>
    </tr>
    <tr>
      <td><strong>Cast-Resin Block Type (LZZBJ)</strong></td>
      <td>Solid epoxy resin casting completely encapsulating primary and secondary windings.</td>
      <td>Superior moisture resistance, high dielectric strength, high short-time thermal rating ($I_{th}$).</td>
      <td>Medium-voltage (6kV–35kV) switchgear, outdoor mining substations.</td>
    </tr>
  </tbody>
</table>
'''
)

SP_METER_BLOG = dict(
    slug='din-rail-sub-metering-what-is-a-single-phase-energy-meter',
    title='DIN Rail Electrical Sub-Metering: What Is a Single Phase Energy Meter?',
    breadcrumb='Energy Meter',
    read='9 min read',
    alt='Modular single-phase digital DIN rail kWh energy meter installed in a commercial distribution sub-panel with illuminated LCD display',
    desc=('Commercial and residential sub-metering in modern building infrastructure: What is a single-phase energy meter? '
          'How digital DIN rail kWh meters measure active power, log consumption, and communicate via RS485 Modbus RTU.'),
    model='DDS / SDM Series Modular Single-Phase DIN Rail Electronic Electricity Meters',
    category='Energy Meter / Single-Phase Sub-Metering',
    kw='what is a single phase energy meter &middot; din rail energy meter &middot; single phase kwh meter &middot; modbus energy meter &middot; sub metering electrical panel',
    specs=[
        ('Nominal Operating Voltage (Un)', '220V, 230V, 240V AC Single-Phase 2-Wire (Operating Range: 0.8Un to 1.15Un)'),
        ('Current Ratings (Ib/Imax)', '5(30)A, 5(60)A, 10(100)A Direct Connection; or 1.5(6)A CT Operated for larger commercial loads'),
        ('Accuracy Measurement Class', 'Class 1.0 (Active Energy conforming to IEC 62053-21); Class 0.5 available on precision models'),
        ('Starting Current Threshold', '0.4% Ib (0.02A for 5A base current), capturing ultra-low standby electronics consumption'),
        ('Digital Communication Port', 'RS485 2-Wire Half-Duplex, Modbus RTU Protocol, selectable baud rates from 1200bps up to 9600bps'),
        ('Display & Memory Interface', '6+1 or 7+1 digit blue-backlit high-contrast LCD; non-volatile EEPROM retaining data > 10 years without power'),
        ('Pulse Output Constant', '1000 imp/kWh, 1600 imp/kWh, or 2000 imp/kWh flashing optical LED and passive optocoupler SO terminals'),
        ('Mounting Enclosure Standard', 'Standard 35mm DIN-Rail mounting (1-Module 18mm or 2-Module 35mm widths), IP51 front dust protection')
    ],
    faqs=[
        ('What is a single-phase energy meter and where is it used in electrical installations?',
         'A single-phase energy meter is an electronic instrument designed to measure total active electrical energy consumption '
         '(measured in kilowatt-hours, kWh) in single-phase alternating current circuits. In modern commercial buildings, '
         'residential high-rises, shopping centers, and telecommunication shelters, single-phase meters are installed on modular DIN rails '
         'to sub-meter individual rental units, data server racks, electric vehicle chargers, and branch lighting circuits for precise billing and tenant allocation.'),
        ('How does an electronic digital energy meter calculate kilowatt-hours compared to old induction disc meters?',
         'Traditional electromechanical meters relied on an aluminum rotor disc turned by the eddy currents of magnetic coils, '
         'which suffered from mechanical friction wear, calibration drift, and vulnerability to external magnetic tampering. '
         'Modern digital electronic meters utilize high-precision micro-shunt resistors or internal current transformers paired with a specialized '
         'Application-Specific Integrated Circuit (ASIC). The ASIC samples instantaneous voltage and current waveforms at thousands of hertz, '
         'computes true instantaneous power (P = V &times; I &times; cos &phi;), integrates power over time, and stores digitized energy data into non-volatile EEPROM.'),
        ('Why is RS485 Modbus RTU communication essential in modern sub-metering systems?',
         'Manual meter reading across hundreds of tenant distribution boards is labor-intensive, error-prone, and provides no real-time load visibility. '
         'Single-phase DIN rail meters equipped with an RS485 serial communication port allow up to 32 meters to be daisy-chained along a single twisted-pair cable. '
         'Connected to an IoT data gateway or building management system (BMS), the meters automatically report live voltage, current, active power, '
         'power factor, and cumulative kWh every few seconds, enabling automated tenant billing and peak-demand management.')
    ],
    cta='Looking to deploy compact 1-module or 2-module single-phase DIN rail energy meters with RS485 Modbus for building sub-metering, solar arrays, or smart automation panels? YOMIN supplies certified Class 1.0 digital meters engineered to IEC 62053 standards.',
    body='''
<h2>The Rise of Electrical Sub-Metering in Modern Infrastructure</h2>
<p>Across commercial real estate, multi-tenant residential complexes, and light industrial facilities, electrical power costs represent one of the largest operational expenditures. Historically, utilities provided a single bulk master meter at the building service entrance, forcing facility managers to divide electricity bills arbitrarily by square footage. This practice penalized energy-conscious tenants and concealed equipment inefficiencies.</p>
<p>Modern electrical distribution designs mandate <strong>tenant sub-metering</strong>. Compact modular <strong>single-phase DIN-rail energy meters</strong> install directly inside branch circuit breaker panels, occupying minimal space alongside standard miniature circuit breakers (MCBs) while providing revenue-grade consumption records.</p>

<h2>Internal Architecture of an Electronic Single-Phase Meter</h2>
<p>Modern digital kWh meters achieve high reliability through solid-state microelectronics:</p>
<ul>
  <li><strong>Precision Analog Front End (AFE):</strong> High-accuracy manganin shunt resistors measure current flow with negligible thermal coefficient drift, while precision resistive divider networks step down the 230V line voltage.</li>
  <li><strong>Digital Signal Processing (DSP) Core:</strong> High-speed 16-bit or 24-bit analog-to-digital converters (ADCs) continuously sample line voltage and current. The integrated DSP calculates root-mean-square (RMS) voltage, RMS current, instantaneous active power ($P$), reactive power ($Q$), and line frequency ($Hz$).</li>
  <li><strong>Time-Integration & Pulse Output:</strong> Power calculations are integrated with respect to time to calculate cumulative energy consumption. The meter pulses an optical calibration LED (e.g. 1600 impulses per kWh) and updates the digital LCD display.</li>
</ul>

<h2>Single-Phase Meter Direct Connection vs. CT Connection</h2>
<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Direct Connection (Direct Insert)</th>
      <th>CT Operated Connection</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Current Rating</strong></td>
      <td>Standard 5(60)A or 10(100)A continuous load.</td>
      <td>1.5(6)A secondary rating paired with external CTs.</td>
    </tr>
    <tr>
      <td><strong>Wiring Mechanism</strong></td>
      <td>Phase and neutral line cables pass directly through internal heavy screw clamps.</td>
      <td>Main power cables stay outside; only thin 2.5mm&sup2; measuring leads connect to meter terminals.</td>
    </tr>
    <tr>
      <td><strong>Installation Complexity</strong></td>
      <td>Simple, plug-and-play wiring directly on DIN rail.</td>
      <td>Requires mounting external current transformers and configuring CT turns ratios.</td>
    </tr>
    <tr>
      <td><strong>Target Application</strong></td>
      <td>Individual apartments, offices, server racks, EV charging stations.</td>
      <td>Main feeder lines, heavy single-phase air conditioning chillers exceeding 100A.</td>
    </tr>
  </tbody>
</table>
'''
)

TP_METER_BLOG = dict(
    slug='commercial-grid-metering-what-is-a-three-phase-energy-meter',
    title='Commercial Grid Power Metering: What Is a Three Phase Energy Meter?',
    breadcrumb='Energy Meter',
    read='10 min read',
    alt='Three-phase commercial smart electronic energy meter actively installed in an industrial metering panel cabinet',
    desc=('Commercial and industrial grid metering in Central Asian utility distribution: What is a three-phase energy meter? '
          'How multi-function smart meters record 4-quadrant active and reactive energy, harmonics, and integrate with DLMS / Modbus networks.'),
    model='DTS / DTZ Series Three-Phase Four-Wire Smart Multi-Function Energy Meters',
    category='Energy Meter / Three-Phase Grid Metering',
    kw='what is a three phase energy meter &middot; three phase smart meter &middot; commercial energy meter &middot; 3 phase kwh meter &middot; dlms cosem energy meter',
    specs=[
        ('Nominal Rated Voltages', '3&times;220/380V, 3&times;230/400V, 3&times;57.7/100V Three-Phase 4-Wire or 3-Wire Systems'),
        ('Current Measurement Ranges', 'Direct Connection: 3&times;5(100)A; CT-Operated Secondary: 3&times;1.5(6)A (supporting CT ratios up to 10,000/5A)'),
        ('Accuracy Measurement Classes', 'Class 0.5S / Class 0.2S (Revenue Substation Metering); Class 1.0 (Industrial Sub-Distribution)'),
        ('Energy Measurement Modes', 'Bi-Directional Active Energy (Import/Export kWh), 4-Quadrant Reactive Energy (kvarh), Apparent Energy (kVAh)'),
        ('Multi-Tariff (TOU) Capability', 'Up to 8 daily tariffs, 14 seasonal tables, 100 holiday schedules, and maximum demand register (kW / kVA)'),
        ('Communication Ports', 'Dual RS485 Modbus RTU, Optical IEC 62056-21 maintenance port, optional plug-and-play 4G LTE / NB-IoT / GPRS modems'),
        ('Communication Protocols', 'DLMS / COSEM open utility protocol and Modbus RTU for integration with SCADA, BMS, and ASKUE systems'),
        ('Power Quality Diagnostics', 'Total Harmonic Distortion (THD up to 31st harmonic), phase voltage unbalance, power factor per phase, sag/swell logging')
    ],
    faqs=[
        ('What is a three-phase energy meter and where is it installed?',
         'A three-phase energy meter is an advanced electrical instrument engineered to measure electrical energy and power quality parameters '
         'in three-phase AC distribution systems (typically 380V to 415V line-to-line). It is deployed at the electrical intake of industrial factories, '
         'commercial office towers, shopping plazas, water treatment plants, and utility transmission substations. Because three-phase circuits '
         'power heavy commercial loads, these meters measure multi-parameter telemetry including voltage, current, frequency, active power, reactive power, and power factor across all three phases.'),
        ('What is bi-directional 4-quadrant energy measurement and why is it required for solar and grid interconnections?',
         'In modern electrical networks featuring commercial solar PV installations or industrial cogeneration, power can flow in both directions: '
         'from the utility grid into the factory (Import Energy), or from rooftop solar arrays back into the grid (Export Energy). '
         'A 4-quadrant energy meter measures both active power (Watts) and reactive power (VARS) in forward and reverse directions. '
         'This enables utilities to execute accurate net-metering billing, identify inductive vs. capacitive power factor penalties, '
         'and optimize reactive power compensation across the distribution grid.'),
        ('What is the difference between direct-connected and CT-connected three-phase meters?',
         'Direct-connected three-phase meters (typically rated up to 100A continuous current) have internal heavy-duty copper bus terminals '
         'where primary power conductors connect directly to the meter. They are ideal for commercial workshops and light retail units. '
         'For industrial facilities with currents exceeding 100A (e.g. 400A, 800A, or 2500A), CT-connected meters (rated 1.5(6)A secondary) '
         'are used in combination with external current transformers. The meter receives stepped-down 5A secondary currents and multiplies '
         'measured readings by the programmed CT turns ratio, providing unlimited current measuring capacity while ensuring installer safety.')
    ],
    cta='Need high-accuracy Class 0.5S or 0.2S three-phase multi-function smart energy meters with DLMS/COSEM, RS485 Modbus, or 4G IoT connectivity for Central Asian industrial switchboards or ASKUE projects? YOMIN supplies fully certified grid meters.',
    body='''
<h2>Central Asian Grid Standards & ASKUE Industrial Power Accounting</h2>
<p>Across the industrial centers of Central Asia—including metallurgical plants in Kazakhstan, agricultural irrigation grids in Uzbekistan, and hydropower distribution networks in Kyrgyzstan and Tajikistan—energy efficiency is strictly enforced through <strong>Automated Systems for Commercial Electricity Metering (ASKUE)</strong>. Industrial facilities are billed not merely on raw active energy consumption (kWh), but also face heavy utility penalties for poor power factor, excessive reactive energy consumption (kvarh), and peak demand violations during restricted grid hours.</p>
<p>Managing these commercial obligations requires intelligent <strong>three-phase multi-function smart energy meters</strong> capable of high-precision multi-tariff scheduling and high-frequency communication with central dispatch servers.</p>

<h2>Multi-Tariff (Time-of-Use) Scheduling and Demand Management</h2>
<p>Modern three-phase smart meters feature advanced firmware designed for automated tariff management:</p>
<ul>
  <li><strong>Time-Use (TOU) Registers:</strong> Power utilities charge varying kilowatt-hour rates depending on the time of day (Peak, Normal, and Valley/Off-Peak periods). YOMIN three-phase meters support up to 8 configurable tariff rates, automatically switching registers based on internal high-precision real-time clocks (RTC) backed by lithium battery backup (drift under 0.5 seconds per day).</li>
  <li><strong>Maximum Demand Profiling:</strong> To prevent industrial consumers from overloading substation distribution transformers, meters calculate sliding-window or block-interval maximum demand (typically over 15-minute intervals). If a factory starts heavy induction furnaces simultaneously, the demand register records the peak kW spike for utility capacity billing.</li>
  <li><strong>Power Quality & Harmonics Monitoring:</strong> Non-linear industrial loads—such as variable frequency drives (VFDs) and arc furnaces—inject destructive harmonics into the power grid. YOMIN smart meters analyze Total Harmonic Distortion (THD) up to the 31st harmonic order on both voltage and current channels.</li>
</ul>

<h2>Communication Protocols: Modbus RTU vs. DLMS / COSEM</h2>
<table>
  <thead>
    <tr>
      <th>Protocol</th>
      <th>Standard Definition</th>
      <th>Best Application</th>
      <th>Key Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Modbus RTU</strong></td>
      <td>Open industrial master-slave protocol over RS485.</td>
      <td>Building Automation, SCADA, factory PLC networks.</td>
      <td>Simple register mapping, low overhead, universal hardware compatibility.</td>
    </tr>
    <tr>
      <td><strong>DLMS / COSEM</strong></td>
      <td>IEC 62056 international utility metering suite.</td>
      <td>National power utilities, ASKUE/AMR centralized metering.</td>
      <td>Cryptographic data security, standardized OBIS codes, interoperable across multi-vendor grid platforms.</td>
    </tr>
  </tbody>
</table>
'''
)

PREPAID_BLOG = dict(
    slug='utility-revenue-protection-what-is-a-prepaid-energy-meter',
    title='Utility Revenue Protection & Smart Prepayment: What Is a Prepaid Energy Meter?',
    breadcrumb='Energy Meter',
    read='10 min read',
    alt='Split-type STS keypad prepaid electricity meter actively mounted on residential utility corridor wall with security seal',
    desc=('Utility revenue protection and smart prepayment in residential and commercial grids: What is a prepaid energy meter? '
          'How 20-digit STS token keypad systems prevent non-technical losses, enforce revenue collection, and disconnect delinquent loads.'),
    model='STE / YM-STS Series Single-Phase and Three-Phase STS Keypad Prepayment Electricity Meters',
    category='Energy Meter / Prepayment Systems',
    kw='what is a prepaid energy meter &middot; sts prepaid meter &middot; keypad electricity meter &middot; revenue protection meter &middot; token energy meter',
    specs=[
        ('Standard Transfer Specification', 'STS compliant (IEC 62055-41, IEC 62055-51) 20-digit encrypted numeric token input via keypad'),
        ('Nominal Operating Voltages', 'Single-Phase 230V AC or Three-Phase 3&times;230/400V AC 50Hz/60Hz Utility Grid Systems'),
        ('Current Carrying Ratings', '5(60)A, 5(80)A, 10(100)A Direct Connection with internal high-power magnetic latching relay switch'),
        ('Measurement Accuracy Class', 'Class 1.0 (IEC 62053-21 compliant active energy recording) with microsecond sampling'),
        ('Internal Disconnect Contactor', 'Bistable magnetic latching relay rated for 100A switching; 10,000+ mechanical open/close operations under full load'),
        ('Anti-Tamper Security Suite', 'Terminal cover open sensor, top cover open detector, strong magnetic field shield (500mT), neutral line bypass detection'),
        ('Customer Interface Options', 'Integrated keypad on meter body, or Split-Unit architecture with remote Customer Interface Unit (CIU) via PLC / RF / M-Bus'),
        ('Environmental Protection', 'Robust IP54 polycarbonate UV-stabilized housing with ultrasonic welding and galvanized security seal provisions')
    ],
    faqs=[
        ('What is a prepaid energy meter and how does it protect utility revenue?',
         'A prepaid energy meter (commonly termed a prepayment electricity meter or STS meter) is an intelligent electricity meter '
         'that requires consumers to pay for electrical energy in advance before power is consumed. The consumer purchases an encrypted '
         '20-digit numerical token from a vending station, bank, or mobile payment application, and inputs the code into the meter keypad. '
         'The meter credits the purchased kilowatt-hours to its internal balance register. As appliances run, the meter decrements the balance. '
         'If the credit reaches zero without replenishment, an internal motorized magnetic latching relay automatically disconnects the power supply, '
         'completely eliminating utility unpaid bad debt, manual meter-reading billing costs, and customer payment defaults.'),
        ('What is the Standard Transfer Specification (STS) and how does token encryption work?',
         'The Standard Transfer Specification (STS) is the globally recognized international open standard (IEC 62055) for secure transfer '
         'of prepayment tokens between utility vending systems and smart electricity meters. When a customer purchases electricity, the utility vending '
         'server generates a 20-digit numerical token using advanced 112-bit Triple-DES or 128-bit AES cryptographic algorithms, keyed to the unique '
         'factory serial number of that specific meter. This ensures that a token generated for one meter cannot be entered into any other meter. '
         'The algorithm also embeds a unique Tariff ID and Token Identifier (TID) to prevent replay tampering or re-use of old voucher codes.'),
        ('What is a split-type prepayment meter and why do utilities prefer it over integrated keypad meters?',
         'In an integrated prepaid meter, the keypad, display, and disconnect relay are all housed in a single enclosure mounted inside the customer residence, '
         'where dishonest consumers can attempt physical tampering or wire bypasses. In a split-type prepayment meter architecture, '
         'the robust Metering and Control Unit (MCU) containing the measuring shunt and disconnect contactor is locked away high on a utility pole '
         'or inside a tamper-proof street cabinet outside the property. The customer is provided only with a lightweight Customer Interface Unit (CIU) '
         'placed inside their kitchen or hallway. The CIU communicates with the pole-mounted MCU via Power Line Carrier (PLC) or wireless Radio Frequency (RF), '
         'rendering physical tampering virtually impossible.')
    ],
    cta='Planning utility electrification, municipal revenue protection, or residential prepayment deployments with STS-certified keypad meters and vending software? YOMIN supplies certified single-phase and three-phase STS split prepayment meters.',
    body='''
<h2>The Global Imperative for Utility Revenue Protection</h2>
<p>For municipal power utilities and private distribution concessionaires across emerging economies, commercial viability is continuously threatened by <strong>non-technical losses (electricity theft)</strong> and <strong>chronic billing payment defaults</strong>. In conventional postpaid utility frameworks, power is delivered first and billed 30 to 60 days later. Utilities face crippling overhead costs employing armies of meter readers, printing paper bills, and resolving customer billing disputes, often writing off millions of dollars in uncollectible debt.</p>
<p>The <strong>STS Prepaid Energy Meter</strong> re-engineers utility cash flow, converting receivables into upfront liquidity while empowering consumers to monitor and manage their own daily electricity usage in real time.</p>

<h2>How the 20-Digit STS Cryptographic Token Operates</h2>
<p>The Standard Transfer Specification (IEC 62055) governs the automated vending and decryption lifecycle:</p>
<ol>
  <li><strong>Vending Station Token Generation:</strong> The consumer purchases electricity at a vendor terminal or mobile app. The vending system takes the purchase value (e.g. 200 kWh), the unique 11-digit Meter ID, and a sequential Token Identifier (TID), encrypting them with a secure Vending Key into a standardized <strong>20-digit numeric token</strong>.</li>
  <li><strong>Keypad Decryption & Validation:</strong> The consumer types the 20 digits on the meter keypad. The meter internal processor decrypts the token using its stored secret device key. If the decryption verifies that the token was minted specifically for this meter and has not been used previously, the purchased kWh is added to the active credit register.</li>
  <li><strong>Credit Depletion & Automatic Disconnection:</strong> As the consumer draws power, the active credit decreases. When credit drops below a pre-programmed threshold (e.g. 10 kWh), an audible buzzer sounds and an LED warns the tenant to recharge. If credit reaches zero, the microcomputer fires a pulse to an internal <strong>heavy-duty magnetic latching relay</strong>, physically opening the contact points and disconnecting the load until a new token is input.</li>
</ol>

<h2>Integrated Keypad vs. Split Prepayment Meter Architecture</h2>
<table>
  <thead>
    <tr>
      <th>System Architecture</th>
      <th>Hardware Layout</th>
      <th>Anti-Tamper Security Level</th>
      <th>Installation Environment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Integrated Keypad Meter</strong></td>
      <td>Keypad, LCD display, MCU, and latching relay housed in one wall-mounted unit.</td>
      <td>Standard: protected by terminal seal wire and optical case-open sensors.</td>
      <td>Secure residential apartments, managed estates, commercial shopping stalls.</td>
    </tr>
    <tr>
      <td><strong>Split Prepayment Meter (MCU + CIU)</strong></td>
      <td>Measuring Unit (MCU) locked in outdoor pole cabinet; Customer Interface Unit (CIU) placed inside home.</td>
      <td><strong>Maximum:</strong> consumer has zero physical access to measurement shunt or disconnect relay.</td>
      <td>Utility residential electrification, high-theft urban zones, rural village grids.</td>
    </tr>
  </tbody>
</table>
'''
)

CA_BLOGS = [CT_BLOG, SP_METER_BLOG, TP_METER_BLOG, PREPAID_BLOG]
