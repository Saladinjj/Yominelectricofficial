# -*- coding: utf-8 -*-
"""Content for 2026-10-23 batch - Topic B: AC voltage stabilizer sizing."""

SLUG = 'air-conditioner-voltage-stabilizer-sizing'

B_EN = dict(
    slug=SLUG,
    lang='en',
    dir='ltr',
    title='Voltage Stabilizer for Air Conditioners: Sizing, Types and Installation',
    desc='How to size a voltage stabilizer for an air conditioner: reading the nameplate, compressor starting current, relay versus servo AVR, restart delay, wall mounting, wiring and the mistakes that trip a unit on start-up.',
    breadcrumb='Air conditioner voltage stabilizer',
    category='Selection Guide',
    read='10 min read',
    alt='Wall-mounted automatic voltage stabilizer installed beside a split air conditioning unit in a domestic installation',
    cta='Tell us the air conditioner nameplate data, the number of units and the typical grid voltage in your area. We will size the stabilizer, confirm the model and quote factory-direct quantities.',
    product_url='/products/voltage-stabilizer-regulator',
    body='''<h2>What a stabilizer actually protects</h2>
<p>An air conditioner compressor is an induction motor that expects a stable supply. When line voltage drops, the motor draws more current for the same output, windings run hotter, and the internal overload eventually opens. When voltage rises, control boards and capacitors see stresses they were not designed for. In both directions the failure is rarely immediate &mdash; it shows up as a compressor that trips on hot afternoons, then as a replacement.</p>
<p>A voltage stabilizer sits between the wall supply and the air conditioner and holds the output within a working band while the input moves. It does not replace surge protection, and it does not fix a supply that is simply too weak to start the compressor. It buys the motor a stable voltage so that the current stays where the designer intended.</p>
<p>The mistake buyers make is choosing by horsepower alone. A 1.5&nbsp;HP unit in a hot climate with a long cable run and 160&nbsp;V evenings needs a different stabilizer from the same unit on a stiff urban supply.</p>

<h2>Sizing in four numbers</h2>
<p>Everything you need is on the unit nameplate and a multimeter:</p>
<ul>
<li><strong>Running current (A):</strong> the rated current on the nameplate, not the cooling capacity in BTU.</li>
<li><strong>Supply voltage (V):</strong> single-phase 220&ndash;240&nbsp;V for most domestic splits, three-phase for larger cassette and ducted systems.</li>
<li><strong>Starting current:</strong> compressors draw several times running current for a second or two at start-up. A stabilizer that is only marginally larger than the running load will trip or sag on every compressor start.</li>
<li><strong>Worst-case input voltage:</strong> measure at the socket during the evening peak, not at midday. The stabilizer must cover the lowest voltage your area actually delivers, not the nominal value.</li>
</ul>
<p>A practical method: required capacity (VA) = running current &times; nominal voltage &times; a starting margin. A margin of 1.3 to 1.5 covers normal compressor starting and ageing; go higher where the supply is very weak or the cable run is long. Round up to the next standard size &mdash; never down.</p>
<p>Worked example: a single-phase split with a nameplate running current of 6&nbsp;A at 230&nbsp;V gives 6 &times; 230 = 1,380&nbsp;VA; with a 1.4 margin the requirement is about 1,930&nbsp;VA, so the next standard stabilizer size is chosen, not the 1,500&nbsp;VA unit that looks &ldquo;close enough&rdquo;.</p>

<h2>Relay type or servo type?</h2>
<p>Both are automatic voltage regulators; they correct in different ways.</p>
<table>
  <thead><tr><th>Characteristic</th><th>Relay (tap-switching) type</th><th>Servo (motor-driven) type</th></tr></thead>
  <tbody>
    <tr><td><strong>Correction</strong></td><td>Steps between transformer taps</td><td>Continuous, by moving a carbon brush over a winding</td></tr>
    <tr><td><strong>Output quality</strong></td><td>Small step changes as taps switch</td><td>Smooth output, better for sensitive electronics</td></tr>
    <tr><td><strong>Speed of correction</strong></td><td>Fast, stepwise</td><td>Smoother but mechanically slower on large swings</td></tr>
    <tr><td><strong>Input range</strong></td><td>Suited to moderate fluctuation</td><td>Better where the grid swings widely</td></tr>
    <tr><td><strong>Wear parts</strong></td><td>Relay contacts</td><td>Brush and motor</td></tr>
    <tr><td><strong>Typical use</strong></td><td>Domestic splits, budget installations</td><td>Large splits, clinics, shops, sensitive loads</td></tr>
  </tbody>
</table>
<p>For a house with two splits on a supply that moves between roughly 190&nbsp;V and 240&nbsp;V, a relay-type wall unit is usually the economical answer. For a clinic, a shop with refrigeration, or an area where voltage collapses in the evening, the servo type earns its price difference.</p>

<h2>Installation: where it goes and what it needs</h2>
<h3>Position</h3>
<p>Mount the stabilizer on a wall close to the air conditioner, in a ventilated position out of direct sun. It dissipates heat; a unit boxed into a closed cabinet will derate or trip. Keep at least the clearance stated in its manual around the ventilation slots, and mount it at a height where the display can be read and the breaker reached.</p>
<h3>Wiring</h3>
<p>Feed the stabilizer from a dedicated circuit with a breaker rated for the air conditioner, then take the output to the unit. Use a conductor size appropriate to the circuit current, connect the earth continuously, and do not use the stabilizer as a junction box for other loads. Every connection should be torqued and tug-tested; loose terminals at a stabilizer are a common cause of nuisance tripping.</p>
<h3>Restart delay</h3>
<p>Compressors must not be restarted immediately after stopping: the refrigerant pressures need time to equalise, and a short-cycling compressor overheats and fails. Many stabilizers include a restart delay of a few minutes for exactly this reason. Where the stabilizer does not provide one, the air conditioner&rsquo;s own control board usually does &mdash; but check, because stacking two long delays makes the unit feel unresponsive.</p>

<h2>Symptoms of an undersized or wrong unit</h2>
<table>
  <thead><tr><th>Symptom</th><th>Likely cause</th></tr></thead>
  <tbody>
    <tr><td><strong>Trips every time the compressor starts</strong></td><td>Capacity below starting demand, or the input voltage is under the unit&rsquo;s range</td></tr>
    <tr><td><strong>Output voltage still low under load</strong></td><td>Stabilizer at its correction limit; the supply is weaker than assumed</td></tr>
    <tr><td><strong>Audible buzzing and a warm case</strong></td><td>Operation at the edge of its range or an overloaded unit</td></tr>
    <tr><td><strong>Display flickers between values</strong></td><td>Unstable input or a loose incoming connection</td></tr>
    <tr><td><strong>Works in winter, trips in summer</strong></td><td>Thermal derating in a hot position, or demand above capacity at peak ambient</td></tr>
  </tbody>
</table>

<h2>What to specify when you buy</h2>
<p>For a distributor or contractor order, specify: phase, capacity in VA, input voltage range, output accuracy band, correction type, restart delay, mounting format (wall or floor), display, protection functions and the ambient temperature rating. Ask for the input range explicitly &mdash; capacity alone tells you nothing about whether the unit will hold output at 150&nbsp;V.</p>
<p>Our <a href="/products/voltage-stabilizer-regulator">voltage stabilizer and regulator range</a> includes single-phase wall-mounted relay units for domestic air conditioners and servo-motor units for larger and more sensitive loads. For a wider comparison of correction technologies, see the <a href="/blog/voltage-stabilizer-guide">voltage stabilizer guide</a> and, for capacity calculations across a whole installation, the <a href="/blog/voltage-stabilizer-sizing-guide">sizing guide</a>.</p>

<h2>A note on three-phase air conditioning</h2>
<p>Cassette and ducted systems in shops, offices and clinics are often three-phase. A three-phase stabilizer must correct all three phases and protect against phase loss and phase sequence faults, because a compressor running on two phases will fail quickly. Specify the phase-failure behaviour at order time; it is not something to discover on commissioning.</p>''',
    specs=[
        ('Sizing basis', 'Nameplate running current × nominal voltage × 1.3–1.5 starting margin, rounded up'),
        ('Input range', 'Must cover the lowest measured supply voltage at peak hours, not the nominal value'),
        ('Correction types', 'Relay tap-switching or servo motor driven, chosen by load sensitivity and grid swing'),
        ('Restart delay', 'Several minutes between compressor stops and restarts to allow pressure equalisation'),
        ('Installation', 'Ventilated wall position out of direct sun, dedicated circuit, continuous earth, torqued terminals'),
    ],
    faqs=[
        ('What size stabilizer do I need for a 1.5 HP air conditioner?',
         'Size from the nameplate running current, not the horsepower. Multiply the running current by the nominal voltage, apply a 1.3 to 1.5 margin for compressor starting, and round up to the next standard capacity. A unit that sits exactly at the calculated figure will trip on hot days.'),
        ('Is a relay-type stabilizer enough, or do I need a servo unit?',
         'A relay type is adequate for domestic splits on a supply that fluctuates moderately. Choose servo where the voltage swings widely, where the load includes refrigeration or medical equipment, or where the output must be smooth rather than stepped.'),
        ('Why does the stabilizer trip when the compressor starts?',
         'Almost always because the unit is sized to running current only, ignoring the starting surge. It can also be the input voltage falling below the stabilizer range at that moment, or a loose incoming terminal. Check the nameplate, the measured voltage at start-up and the terminal torque in that order.'),
        ('Can one stabilizer supply two air conditioners?',
         'Only if its capacity covers the combined running load plus the starting surge of the largest unit, and only if both units are unlikely to start together. Separate units per air conditioner are easier to protect and to diagnose.'),
    ],
)

B_FR = dict(
    slug=SLUG + '-fr',
    lang='fr',
    dir='ltr',
    title='Stabilisateur de tension pour climatiseur : dimensionnement, types et installation',
    desc='Comment dimensionner un stabilisateur de tension pour climatiseur : lecture de la plaque signalétique, courant de démarrage du compresseur, régulateur à relais ou à servo-moteur, temporisation, pose murale et erreurs de câblage.',
    breadcrumb='Stabilisateur pour climatiseur',
    category='Guide de choix',
    read='10 min de lecture',
    alt='Stabilisateur de tension mural installé à côté d\'un climatiseur split dans une installation domestique',
    cta='Indiquez-nous les données de plaque du climatiseur, le nombre d\'unités et la tension habituelle de votre réseau. Nous dimensionnons le stabilisateur, confirmons le modèle et chiffrons les quantités départ usine.',
    product_url='/products/voltage-stabilizer-regulator',
    body='''<h2>Ce qu&rsquo;un stabilisateur protège réellement</h2>
<p>Le compresseur d&rsquo;un climatiseur est un moteur asynchrone qui attend une alimentation stable. Lorsque la tension chute, le moteur absorbe davantage de courant pour le même travail, les enroulements chauffent et le protecteur interne finit par déclencher. Lorsque la tension monte, les cartes de commande et les condensateurs subissent des contraintes pour lesquelles ils ne sont pas dimensionnés. Dans les deux cas, la défaillance est rarement immédiate : elle se manifeste d&rsquo;abord par un compresseur qui déclenche les après-midi de forte chaleur, puis par un remplacement.</p>
<p>Un stabilisateur se place entre le réseau et le climatiseur et maintient la sortie dans une plage de travail pendant que l&rsquo;entrée varie. Il ne remplace pas une protection contre les surtensions et ne corrige pas un réseau trop faible pour démarrer le compresseur. Il offre au moteur une tension stable afin que le courant reste celui prévu par le concepteur.</p>
<p>L&rsquo;erreur d&rsquo;achat la plus fréquente consiste à choisir uniquement selon la puissance en chevaux. Un split de 1,5&nbsp;ch en climat chaud, avec une longue ligne et 160&nbsp;V le soir, n&rsquo;a pas besoin du même stabilisateur que le même appareil sur un réseau urbain robuste.</p>

<h2>Dimensionner avec quatre données</h2>
<p>Tout se lit sur la plaque signalétique et sur un multimètre :</p>
<ul>
<li><strong>Courant de service (A) :</strong> le courant assigné de la plaque, pas la puissance frigorifique en BTU.</li>
<li><strong>Tension d&rsquo;alimentation (V) :</strong> 220&ndash;240&nbsp;V monophasé pour la plupart des splits domestiques, triphasé pour les cassettes et gainables de forte puissance.</li>
<li><strong>Courant de démarrage :</strong> un compresseur absorbe plusieurs fois le courant de service pendant une à deux secondes au démarrage. Un stabilisateur à peine plus puissant que la charge permanente déclenchera ou s&rsquo;affaissera à chaque démarrage.</li>
<li><strong>Tension d&rsquo;entrée la plus basse :</strong> mesurez à la prise pendant la pointe du soir, pas à midi. Le stabilisateur doit couvrir la tension la plus basse réellement délivrée, pas la valeur nominale.</li>
</ul>
<p>Méthode pratique : puissance nécessaire (VA) = courant de service &times; tension nominale &times; marge de démarrage. Une marge de 1,3 à 1,5 couvre le démarrage normal du compresseur et le vieillissement ; augmentez-la si le réseau est très faible ou la ligne longue. Arrondissez toujours au calibre standard supérieur, jamais à l&rsquo;inférieur.</p>
<p>Exemple : un split monophasé dont la plaque indique 6&nbsp;A sous 230&nbsp;V donne 6 &times; 230 = 1&nbsp;380&nbsp;VA ; avec une marge de 1,4 le besoin est d&rsquo;environ 1&nbsp;930&nbsp;VA : on retient le calibre standard supérieur, pas l&rsquo;appareil de 1&nbsp;500&nbsp;VA qui semble «&nbsp;proche&nbsp;».</p>

<h2>Type relais ou type servo-moteur ?</h2>
<p>Les deux sont des régulateurs automatiques de tension ; leur mode de correction diffère.</p>
<table>
  <thead><tr><th>Caractéristique</th><th>Type relais (commutation de prises)</th><th>Type servo-moteur</th></tr></thead>
  <tbody>
    <tr><td><strong>Correction</strong></td><td>Par paliers entre prises du transformateur</td><td>Continue, par balayage d&rsquo;un balai sur l&rsquo;enroulement</td></tr>
    <tr><td><strong>Qualité de sortie</strong></td><td>Petits sauts lors des commutations</td><td>Sortie lissée, préférable pour l&rsquo;électronique sensible</td></tr>
    <tr><td><strong>Rapidité</strong></td><td>Rapide, par paliers</td><td>Plus progressive sur les grandes variations</td></tr>
    <tr><td><strong>Plage d&rsquo;entrée</strong></td><td>Adapté aux fluctuations modérées</td><td>Préférable lorsque le réseau varie fortement</td></tr>
    <tr><td><strong>Pièces d&rsquo;usure</strong></td><td>Contacts de relais</td><td>Balai et moteur</td></tr>
    <tr><td><strong>Usage typique</strong></td><td>Splits domestiques, installations économiques</td><td>Gros splits, cliniques, commerces, charges sensibles</td></tr>
  </tbody>
</table>
<p>Pour une maison équipée de deux splits sur un réseau qui oscille entre 190 et 240&nbsp;V, un modèle mural à relais est généralement le choix économique. Pour une clinique, un commerce avec froid commercial, ou une zone où la tension s&rsquo;effondre le soir, le servo-moteur justifie son écart de prix.</p>

<h2>Installation : emplacement et raccordement</h2>
<h3>Emplacement</h3>
<p>Fixez le stabilisateur au mur, près du climatiseur, dans une zone ventilée et à l&rsquo;abri du soleil direct. L&rsquo;appareil dissipe de la chaleur : enfermé dans un coffret fermé, il se déclassera ou déclenchera. Respectez le dégagement indiqué autour des grilles de ventilation et choisissez une hauteur permettant de lire l&rsquo;afficheur et d&rsquo;atteindre le disjoncteur.</p>
<h3>Câblage</h3>
<p>Alimentez le stabilisateur depuis un circuit dédié protégé par un disjoncteur calibré pour le climatiseur, puis repartez vers l&rsquo;unité. Utilisez une section adaptée au courant du circuit, assurez la continuité du conducteur de protection et n&rsquo;utilisez pas le stabilisateur comme boîte de dérivation pour d&rsquo;autres charges. Chaque borne doit être serrée au couple et testée en traction : une borne desserrée sur un stabilisateur provoque des déclenchements intempestifs.</p>
<h3>Temporisation</h3>
<p>Un compresseur ne doit pas redémarrer immédiatement après son arrêt : les pressions de fluide doivent s&rsquo;équilibrer, faute de quoi le compresseur surchauffe et casse. Beaucoup de stabilisateurs intègrent pour cette raison une temporisation de redémarrage de quelques minutes. Lorsque ce n&rsquo;est pas le cas, la carte du climatiseur s&rsquo;en charge généralement &mdash; vérifiez-le, car deux temporisations longues cumulées rendent l&rsquo;appareil peu réactif.</p>

<h2>Symptômes d&rsquo;un appareil sous-dimensionné ou inadapté</h2>
<table>
  <thead><tr><th>Symptôme</th><th>Cause probable</th></tr></thead>
  <tbody>
    <tr><td><strong>Déclenchement à chaque démarrage du compresseur</strong></td><td>Puissance inférieure au besoin au démarrage, ou tension d&rsquo;entrée hors plage</td></tr>
    <tr><td><strong>Tension de sortie encore basse en charge</strong></td><td>Stabilisateur en limite de correction ; réseau plus faible que prévu</td></tr>
    <tr><td><strong>Bourdonnement et boîtier chaud</strong></td><td>Fonctionnement en limite de plage ou surcharge</td></tr>
    <tr><td><strong>Afficheur qui clignote entre deux valeurs</strong></td><td>Entrée instable ou borne d&rsquo;arrivée desserrée</td></tr>
    <tr><td><strong>Fonctionne en hiver, déclenche en été</strong></td><td>Déclassement thermique en emplacement chaud ou demande supérieure en pointe</td></tr>
  </tbody>
</table>

<h2>Ce qu&rsquo;il faut spécifier à la commande</h2>
<p>Pour une commande distributeur ou installateur, précisez : phase, puissance en VA, plage de tension d&rsquo;entrée, bande de précision en sortie, type de correction, temporisation de redémarrage, format de pose (mural ou sur socle), affichage, fonctions de protection et température ambiante assignée. Demandez explicitement la plage d&rsquo;entrée : la puissance seule ne dit rien de la capacité à tenir la sortie à 150&nbsp;V.</p>
<p>Notre <a href="/products/voltage-stabilizer-regulator">gamme de stabilisateurs et régulateurs de tension</a> comprend des modèles muraux monophasés à relais pour climatiseurs domestiques et des modèles à servo-moteur pour charges plus importantes et sensibles. Pour comparer les technologies, consultez le <a href="/blog/voltage-stabilizer-guide">guide du stabilisateur de tension</a> et, pour un calcul sur l&rsquo;ensemble d&rsquo;une installation, le <a href="/blog/voltage-stabilizer-sizing-guide">guide de dimensionnement</a>.</p>

<h2>Précision sur le triphasé</h2>
<p>Les cassettes et gainables de commerce, bureau ou clinique sont souvent triphasés. Un stabilisateur triphasé doit corriger les trois phases et protéger contre la perte de phase et l&rsquo;inversion d&rsquo;ordre, car un compresseur alimenté sur deux phases tombe rapidement en panne. Précisez le comportement en défaut de phase dès la commande : ce n&rsquo;est pas un point à découvrir à la mise en service.</p>''',
    specs=[
        ('Base de dimensionnement', 'Courant de plaque × tension nominale × marge de démarrage 1,3–1,5, arrondie au calibre supérieur'),
        ('Plage d\'entrée', 'Doit couvrir la tension la plus basse mesurée en pointe, pas la valeur nominale'),
        ('Types de correction', 'Relais à commutation de prises ou servo-moteur, selon la sensibilité de la charge et l\'amplitude des variations'),
        ('Temporisation', 'Plusieurs minutes entre arrêt et redémarrage du compresseur pour équilibrer les pressions'),
        ('Installation', 'Pose murale ventilée à l\'abri du soleil, circuit dédié, terre continue, bornes serrées au couple'),
    ],
    faqs=[
        ('Quelle puissance de stabilisateur pour un climatiseur de 1,5 ch ?',
         'Dimensionnez à partir du courant de plaque, pas des chevaux. Multipliez le courant de service par la tension nominale, appliquez une marge de 1,3 à 1,5 pour le démarrage du compresseur, puis arrondissez au calibre supérieur. Un appareil exactement à la valeur calculée déclenchera les jours de forte chaleur.'),
        ('Un modèle à relais suffit-il, ou faut-il un servo-moteur ?',
         'Le type relais convient aux splits domestiques sur un réseau modérément fluctuant. Choisissez le servo-moteur lorsque la tension varie fortement, que la charge inclut du froid commercial ou du matériel médical, ou que la sortie doit être lissée plutôt que par paliers.'),
        ('Pourquoi le stabilisateur déclenche-t-il au démarrage du compresseur ?',
         'Presque toujours parce que l\'appareil est dimensionné sur le courant de service seul, sans l\'appel de démarrage. Cela peut aussi venir d\'une tension d\'entrée qui passe sous la plage à cet instant, ou d\'une borne d\'arrivée desserrée. Vérifiez dans cet ordre la plaque, la tension au démarrage et le serrage des bornes.'),
        ('Un seul stabilisateur peut-il alimenter deux climatiseurs ?',
         'Uniquement si sa puissance couvre la charge cumulée plus l\'appel de démarrage du plus gros appareil, et si les deux ne démarrent pas simultanément. Un appareil par climatiseur est plus simple à protéger et à diagnostiquer.'),
    ],
)

B_ES = dict(
    slug=SLUG + '-es',
    lang='es',
    dir='ltr',
    title='Estabilizador de tensión para aire acondicionado: cálculo, tipos e instalación',
    desc='Cómo dimensionar un estabilizador de tensión para aire acondicionado: lectura de la placa, corriente de arranque del compresor, regulador de relé o servo, retardo de reconexión, montaje en pared y errores de cableado.',
    breadcrumb='Estabilizador para aire acondicionado',
    category='Guía de selección',
    read='10 min de lectura',
    alt='Estabilizador de tensión de pared instalado junto a un equipo split de aire acondicionado en una vivienda',
    cta='Indíquenos los datos de placa del equipo, el número de unidades y la tensión habitual de su red. Calculamos el estabilizador, confirmamos el modelo y cotizamos cantidades desde fábrica.',
    product_url='/products/voltage-stabilizer-regulator',
    body='''<h2>Qué protege realmente un estabilizador</h2>
<p>El compresor de un aire acondicionado es un motor de inducción que espera una alimentación estable. Cuando la tensión baja, el motor consume más corriente para el mismo trabajo, los devanados se calientan y el protector térmico acaba abriendo. Cuando la tensión sube, las tarjetas de control y los condensadores soportan esfuerzos para los que no fueron diseñados. En ambos casos la avería rara vez es inmediata: aparece primero como un compresor que dispara en las tardes calurosas y después como un recambio.</p>
<p>Un estabilizador se instala entre la red y el equipo y mantiene la salida dentro de una banda de trabajo mientras la entrada varía. No sustituye a una protección contra sobretensiones y no arregla una red demasiado débil para arrancar el compresor. Lo que hace es dar al motor una tensión estable para que la corriente se mantenga en el valor previsto por el diseñador.</p>
<p>El error más común al comprar es elegir solo por caballos de potencia. Un split de 1,5&nbsp;HP en clima cálido, con línea larga y 160&nbsp;V por la noche, necesita un estabilizador distinto del mismo equipo conectado a una red urbana robusta.</p>

<h2>Dimensionar con cuatro datos</h2>
<p>Todo está en la placa de características y en un multímetro:</p>
<ul>
<li><strong>Corriente de servicio (A):</strong> la corriente nominal de la placa, no la capacidad frigorífica en BTU.</li>
<li><strong>Tensión de alimentación (V):</strong> 220&ndash;240&nbsp;V monofásica en la mayoría de splits domésticos, trifásica en cassettes y conductos de mayor tamaño.</li>
<li><strong>Corriente de arranque:</strong> el compresor absorbe varias veces la corriente de servicio durante uno o dos segundos al arrancar. Un estabilizador apenas mayor que la carga permanente disparará o caerá en cada arranque.</li>
<li><strong>Tensión de entrada más baja:</strong> mida en la toma durante la punta de la noche, no al mediodía. El equipo debe cubrir la tensión más baja que su zona entrega realmente, no el valor nominal.</li>
</ul>
<p>Método práctico: capacidad necesaria (VA) = corriente de servicio &times; tensión nominal &times; margen de arranque. Un margen de 1,3 a 1,5 cubre el arranque normal del compresor y el envejecimiento; súbalo si la red es muy débil o la línea es larga. Redondee siempre al calibre estándar superior, nunca al inferior.</p>
<p>Ejemplo: un split monofásico con 6&nbsp;A de placa a 230&nbsp;V da 6 &times; 230 = 1.380&nbsp;VA; con margen de 1,4 la necesidad ronda 1.930&nbsp;VA, así que se elige el calibre estándar siguiente y no el equipo de 1.500&nbsp;VA que parece &laquo;suficiente&raquo;.</p>

<h2>¿Tipo relé o tipo servo?</h2>
<p>Ambos son reguladores automáticos de tensión; corrigen de forma distinta.</p>
<table>
  <thead><tr><th>Característica</th><th>Tipo relé (conmutación de tomas)</th><th>Tipo servo motor</th></tr></thead>
  <tbody>
    <tr><td><strong>Corrección</strong></td><td>Por escalones entre tomas del transformador</td><td>Continua, desplazando una escobilla sobre el devanado</td></tr>
    <tr><td><strong>Calidad de salida</strong></td><td>Pequeños saltos al conmutar</td><td>Salida suave, preferible para electrónica sensible</td></tr>
    <tr><td><strong>Velocidad</strong></td><td>Rápida, por escalones</td><td>Más progresiva en variaciones grandes</td></tr>
    <tr><td><strong>Rango de entrada</strong></td><td>Adecuado a fluctuación moderada</td><td>Mejor donde la red oscila mucho</td></tr>
    <tr><td><strong>Piezas de desgaste</strong></td><td>Contactos de relé</td><td>Escobilla y motor</td></tr>
    <tr><td><strong>Uso típico</strong></td><td>Splits domésticos, instalaciones económicas</td><td>Splits grandes, clínicas, comercios, cargas sensibles</td></tr>
  </tbody>
</table>
<p>Para una vivienda con dos splits en una red que oscila entre 190 y 240&nbsp;V, un equipo de pared tipo relé suele ser la opción económica. Para una clínica, un comercio con refrigeración o una zona donde la tensión se hunde por la noche, el servo justifica la diferencia de precio.</p>

<h2>Instalación: ubicación y conexionado</h2>
<h3>Ubicación</h3>
<p>Fije el estabilizador en pared, cerca del equipo, en zona ventilada y sin sol directo. El aparato disipa calor: dentro de un gabinete cerrado se recalienta y reduce su capacidad o dispara. Respete la separación indicada alrededor de las rejillas y elija una altura que permita leer el display y alcanzar el interruptor.</p>
<h3>Cableado</h3>
<p>Alimente el estabilizador desde un circuito dedicado con interruptor dimensionado para el aire acondicionado y lleve la salida al equipo. Use una sección adecuada a la corriente del circuito, mantenga la continuidad del conductor de protección y no utilice el estabilizador como caja de derivación para otras cargas. Cada borne debe apretarse al par y comprobarse con tracción: un borne flojo en el estabilizador provoca disparos intermitentes.</p>
<h3>Retardo de reconexión</h3>
<p>Un compresor no debe rearrancar inmediatamente después de parar: las presiones del refrigerante necesitan igualarse y un compresor con ciclos cortos se sobrecalienta y falla. Por eso muchos estabilizadores incluyen un retardo de varios minutos. Cuando no lo incluyen, la tarjeta del equipo suele hacerlo; conviene verificarlo, porque acumular dos retardos largos hace que el equipo parezca no responder.</p>

<h2>Síntomas de un equipo mal dimensionado</h2>
<table>
  <thead><tr><th>Síntoma</th><th>Causa probable</th></tr></thead>
  <tbody>
    <tr><td><strong>Dispara en cada arranque del compresor</strong></td><td>Capacidad por debajo de la demanda de arranque o tensión de entrada fuera de rango</td></tr>
    <tr><td><strong>Salida todavía baja con carga</strong></td><td>Estabilizador en su límite de corrección; red más débil de lo supuesto</td></tr>
    <tr><td><strong>Zumbido y carcasa caliente</strong></td><td>Trabajo al límite de rango o sobrecarga</td></tr>
    <tr><td><strong>Display que parpadea entre valores</strong></td><td>Entrada inestable o borne de llegada flojo</td></tr>
    <tr><td><strong>Funciona en invierno y dispara en verano</strong></td><td>Derrateo térmico por ubicación calurosa o demanda superior en punta</td></tr>
  </tbody>
</table>

<h2>Qué especificar al comprar</h2>
<p>Para un pedido de distribuidor o instalador, precise: fase, capacidad en VA, rango de tensión de entrada, banda de precisión de salida, tipo de corrección, retardo de reconexión, formato de montaje (pared o piso), display, funciones de protección y temperatura ambiente asignada. Pida el rango de entrada de forma explícita: la capacidad sola no dice nada sobre si el equipo sostendrá la salida a 150&nbsp;V.</p>
<p>Nuestra <a href="/products/voltage-stabilizer-regulator">gama de estabilizadores y reguladores de tensión</a> incluye modelos monofásicos de pared tipo relé para aire acondicionado doméstico y modelos con servo motor para cargas mayores y sensibles. Para comparar tecnologías, consulte la <a href="/blog/voltage-stabilizer-guide">guía del estabilizador de tensión</a> y, para calcular una instalación completa, la <a href="/blog/voltage-stabilizer-sizing-guide">guía de dimensionamiento</a>.</p>

<h2>Nota sobre trifásica</h2>
<p>Los equipos cassette y conducto de comercios, oficinas y clínicas suelen ser trifásicos. Un estabilizador trifásico debe corregir las tres fases y proteger frente a pérdida de fase e inversión de secuencia, porque un compresor alimentado con dos fases falla rápidamente. Especifique el comportamiento ante fallo de fase al hacer el pedido: no es algo que convenga descubrir en la puesta en marcha.</p>''',
    specs=[
        ('Base de cálculo', 'Corriente de placa × tensión nominal × margen de arranque 1,3–1,5, redondeado al calibre superior'),
        ('Rango de entrada', 'Debe cubrir la tensión más baja medida en horas punta, no el valor nominal'),
        ('Tipos de corrección', 'Relé con conmutación de tomas o servo motor, según sensibilidad de la carga y oscilación de la red'),
        ('Retardo', 'Varios minutos entre parada y rearranque del compresor para igualar presiones'),
        ('Instalación', 'Pared ventilada sin sol directo, circuito dedicado, tierra continua, bornes apretados al par'),
    ],
    faqs=[
        ('¿Qué estabilizador necesito para un aire acondicionado de 1,5 HP?',
         'Dimensione por la corriente de placa, no por los caballos. Multiplique la corriente de servicio por la tensión nominal, aplique un margen de 1,3 a 1,5 por el arranque del compresor y redondee al calibre superior. Un equipo justo en el valor calculado disparará en los días de calor.'),
        ('¿Basta un estabilizador de relé o hace falta servo?',
         'El tipo relé es adecuado para splits domésticos con fluctuación moderada. Elija servo cuando la tensión varíe mucho, cuando la carga incluya refrigeración comercial o equipos médicos, o cuando la salida deba ser suave y no escalonada.'),
        ('¿Por qué dispara el estabilizador al arrancar el compresor?',
         'Casi siempre porque está dimensionado solo para la corriente de servicio, sin el pico de arranque. También puede ser que la tensión de entrada caiga fuera de rango en ese instante o que un borne de llegada esté flojo. Revise en ese orden la placa, la tensión en el arranque y el apriete de bornes.'),
        ('¿Puede un solo estabilizador alimentar dos aires acondicionados?',
         'Solo si su capacidad cubre la carga conjunta más el arranque del equipo mayor, y si ambos no arrancan a la vez. Un equipo por aire acondicionado es más fácil de proteger y de diagnosticar.'),
    ],
)

B_AR = dict(
    slug=SLUG + '-ar',
    lang='ar',
    dir='rtl',
    title='مثبت الجهد للمكيفات: حساب السعة والأنواع والتركيب',
    desc='كيفية اختيار سعة مثبت الجهد للمكيف: قراءة لوحة البيانات، تيار إقلاع الضاغط، مثبت المرحل مقابل مثبت السيرفو، مؤقت إعادة التشغيل، التثبيت على الحائط وأخطاء التوصيل.',
    breadcrumb='مثبت الجهد للمكيفات',
    category='دليل الاختيار',
    read='10 دقائق قراءة',
    alt='مثبت جهد مثبت على الحائط بجوار وحدة تكييف سبليت في تركيب منزلي',
    cta='أرسل لنا بيانات لوحة المكيف وعدد الوحدات والجهد المعتاد في منطقتك. سنحدد السعة ونؤكد الطراز ونقدم عرض سعر بكميات المصنع.',
    product_url='/products/voltage-stabilizer-regulator',
    body='''<h2>ما يحميه مثبت الجهد فعليًا</h2>
<p>ضاغط المكيف محرك حثّي يحتاج تغذية مستقرة. وعندما ينخفض جهد الشبكة يسحب المحرك تيارًا أكبر للعمل نفسه، فتسخن الملفات ويفتح الحماية الحرارية الداخلية في النهاية. وعندما يرتفع الجهد تتعرض لوحات التحكم والمكثفات لإجهادات لم تُصمم لها. وفي الحالتين لا تكون الانهيارات فورية عادة: تظهر أولًا على شكل ضاغط يفصل في ساعات الحر، ثم على شكل استبدال.</p>
<p>يوضع مثبت الجهد بين الشبكة والمكيف ويحافظ على خرج داخل نطاق عمل مع تغيّر الدخل. وهو لا يغني عن حماية الطفرة، ولا يعالج شبكة أضعف من أن تُقلع الضاغط. ما يفعله هو منح المحرك جهدًا مستقرًا ليبقى التيار عند القيمة التي صممها المهندس.</p>
<p>الخطأ الشائع عند الشراء هو الاختيار على أساس القدرة بالحصان فقط. فوحدة 1,5 حصان في مناخ حار وكابل طويل و160&nbsp;فولت مساءً تحتاج مثبتًا مختلفًا عن الوحدة نفسها على شبكة حضرية قوية.</p>

<h2>حساب السعة بأربعة أرقام</h2>
<p>كل ما تحتاجه موجود على لوحة البيانات ومع جهاز قياس:</p>
<ul>
<li><strong>تيار التشغيل (أمبير):</strong> التيار الاسمي على اللوحة، وليس سعة التبريد بالـ BTU.</li>
<li><strong>جهد التغذية (فولت):</strong> 220&ndash;240 فولت أحادي الطور لمعظم وحدات السبليت المنزلية، وثلاثي الطور للوحدات الكاسيت والقنوات الكبيرة.</li>
<li><strong>تيار الإقلاع:</strong> يسحب الضاغط أضعاف تيار التشغيل لثانية أو ثانيتين عند الإقلاع. والمثبت الأكبر بقليل من الحمل المستمر سيفصل أو يهبط جهده عند كل إقلاع.</li>
<li><strong>أدنى جهد دخل:</strong> قِس عند المقبس في ذروة المساء لا في منتصف النهار. يجب أن يغطي المثبت أدنى جهد تقدمه منطقتك فعليًا لا القيمة الاسمية.</li>
</ul>
<p>الطريقة العملية: السعة المطلوبة (فولت أمبير) = تيار التشغيل &times; الجهد الاسمي &times; هامش الإقلاع. وهامش من 1,3 إلى 1,5 يغطي إقلاع الضاغط الطبيعي وتقادم المعدات؛ وارفعه إذا كانت الشبكة ضعيفة جدًا أو الكابل طويلًا. قرّب دائمًا إلى السعة القياسية الأعلى ولا إلى الأدنى.</p>
<p>مثال: سبليت أحادي الطور بتيار 6 أمبير عند 230 فولت يعطي 6 &times; 230 = 1380 فولت أمبير؛ ومع هامش 1,4 تصبح الحاجة نحو 1930 فولت أمبير، فتُختار السعة القياسية التالية وليس وحدة 1500 فولت أمبير التي تبدو «قريبة كفاية».</p>

<h2>نوع المرحل أم نوع السيرفو؟</h2>
<p>كلاهما منظم جهد تلقائي، لكن طريقة التصحيح تختلف.</p>
<table>
  <thead><tr><th>الخاصية</th><th>نوع المرحل (تبديل الصنابير)</th><th>نوع السيرفو (محرك)</th></tr></thead>
  <tbody>
    <tr><td><strong>التصحيح</strong></td><td>على درجات بين صنابير المحول</td><td>مستمر بتحريك فرشاة على الملف</td></tr>
    <tr><td><strong>جودة الخرج</strong></td><td>قفزات صغيرة عند التبديل</td><td>خرج ناعم، أفضل للإلكترونيات الحساسة</td></tr>
    <tr><td><strong>سرعة التصحيح</strong></td><td>سريعة وعلى درجات</td><td>أكثر تدرجًا في التغيرات الكبيرة</td></tr>
    <tr><td><strong>نطاق الدخل</strong></td><td>مناسب للتذبذب المعتدل</td><td>أفضل حين تتأرجح الشبكة بقوة</td></tr>
    <tr><td><strong>أجزاء التآكل</strong></td><td>ملامسات المرحل</td><td>الفرشاة والمحرك</td></tr>
    <tr><td><strong>الاستخدام المعتاد</strong></td><td>سبليت منزلي وتركيبات اقتصادية</td><td>وحدات كبيرة وعيادات ومحال وأحمال حساسة</td></tr>
  </tbody>
</table>
<p>لمنزل بوحدتي سبليت على شبكة تتذبذب بين 190 و240 فولت، يكون المثبت الحائطي نوع المرحل هو الخيار الاقتصادي عادة. أما العيادة أو المحل الذي يحتوي تبريدًا تجاريًا، أو منطقة ينهار فيها الجهد مساءً، فيستحق فيها السيرفو فرق السعر.</p>

<h2>التركيب: المكان والتوصيل</h2>
<h3>المكان</h3>
<p>ثبّت المثبت على الحائط قريبًا من المكيف، في موضع جيد التهوية وبعيدًا عن الشمس المباشرة. فالجهاز يبدد حرارة، وإدخاله في صندوق مغلق يقلل سعته أو يجعله يفصل. احترم المسافة المذكورة حول فتحات التهوية، واختر ارتفاعًا يسمح بقراءة الشاشة والوصول إلى القاطع.</p>
<h3>التوصيل</h3>
<p>غذّ المثبت من دائرة مستقلة بقاطع مناسب للمكيف، ثم أوصل الخرج إلى الوحدة. استخدم مقطع موصلًا مناسبًا لتيار الدائرة، وحافظ على استمرارية موصل الحماية، ولا تستخدم المثبت كصندوق توزيع لأحمال أخرى. ويجب ربط كل طرف بالعزم المحدد واختباره بالسحب؛ فالطرف المرتخي في المثبت سبب شائع للفصل المتكرر.</p>
<h3>مؤقت إعادة التشغيل</h3>
<p>لا يجوز إعادة إقلاع الضاغط فورًا بعد توقفه: فضواغط مادة التبريد تحتاج وقتًا لتتعادل، والضاغط الذي يعمل بدورات قصيرة يسخن ويتلف. ولهذا تتضمن كثير من المثبتات مؤقت إعادة تشغيل لبضع دقائق. وحين لا يتوفر، تتولاه عادة لوحة تحكم المكيف؛ ويُستحسن التحقق من ذلك لأن تراكم مؤقتين طويلين يجعل الوحدة تبدو بطيئة الاستجابة.</p>

<h2>أعراض مثبت غير مناسب أو ناقص السعة</h2>
<table>
  <thead><tr><th>العراض</th><th>السبب المرجح</th></tr></thead>
  <tbody>
    <tr><td><strong>فصل عند كل إقلاع للضاغط</strong></td><td>السعة أقل من طلب الإقلاع أو جهد الدخل خارج النطاق</td></tr>
    <tr><td><strong>خرج منخفض رغم وجود المثبت</strong></td><td>المثبت عند حد التصحيح؛ الشبكة أضعف مما افتُرض</td></tr>
    <tr><td><strong>طنين وصندوق ساخن</strong></td><td>عمل عند حد النطاق أو حمل زائد</td></tr>
    <tr><td><strong>شاشة تتذبذب بين قيمتين</strong></td><td>دخل غير مستقر أو طرف دخول مرتخي</td></tr>
    <tr><td><strong>يعمل شتاءً ويفصل صيفًا</strong></td><td>انخفاض سعة بسبب الحرارة أو طلب أعلى في الذروة</td></tr>
  </tbody>
</table>

<h2>ما يجب تحديده عند الشراء</h2>
<p>لطلب الموزع أو المقاول، حدد: عدد الأطوار، والسعة بالفولت أمبير، ونطاق جهد الدخل، ونطاق دقة الخرج، ونوع التصحيح، ومؤقت إعادة التشغيل، وشكل التثبيت (حائطي أو أرضي)، والشاشة، ووظائف الحماية، ودرجة الحرارة المحيطة الاسمية. واطلب نطاق الدخل صراحةً؛ فالسعة وحدها لا تخبرك إن كان الجهاز سيحافظ على الخرج عند 150 فولت.</p>
<p>يشمل <a href="/products/voltage-stabilizer-regulator">نطاق مثبتات ومنظمات الجهد</a> لدينا وحدات حائطية أحادية الطور بنوع المرحل لمكيفات المنازل، ووحدات بمحرك سيرفو للأحمال الأكبر والأكثر حساسية. ولمقارنة التقنيات راجع <a href="/blog/voltage-stabilizer-guide">دليل مثبت الجهد</a>، ولحساب سعة تركيب كامل راجع <a href="/blog/voltage-stabilizer-sizing-guide">دليل تحديد السعة</a>.</p>

<h2>ملاحظة حول التيار الثلاثي</h2>
<p>وحدات الكاسيت والقنوات في المحال والمكاتب والعيادات ثلاثية الطور غالبًا. ويجب أن يصحح المثبت الثلاثي الأطوار الثلاثة وأن يحمي من فقدان الطور وتعاقب الأطوار، لأن ضاغطًا يعمل على طورين يتلف سريعًا. حدد سلوك الجهاز عند فقدان الطور عند الطلب؛ فالأمر ليس مما يُكتشف عند التشغيل.</p>''',
    specs=[
        ('أساس الحساب', 'تيار اللوحة × الجهد الاسمي × هامش إقلاع 1,3–1,5 ثم التقريب للسعة الأعلى'),
        ('نطاق الدخل', 'يجب أن يغطي أدنى جهد مقيس في ساعات الذروة لا القيمة الاسمية'),
        ('أنواع التصحيح', 'مرحل بتبديل الصنابير أو محرك سيرفو بحسب حساسية الحمل وتذبذب الشبكة'),
        ('المؤقت', 'عدة دقائق بين توقف الضاغط وإعادة إقلاعه لتعادل الضغوط'),
        ('التركيب', 'حائط جيد التهوية بعيد عن الشمس، دائرة مستقلة، أرضي مستمر، أطراف مربوطة بالعزم'),
    ],
    faqs=[
        ('ما سعة المثبت المناسبة لمكيف 1,5 حصان؟',
         'احسب من تيار لوحة البيانات لا من الحصان. اضرب تيار التشغيل في الجهد الاسمي، ثم طبّق هامش 1,3 إلى 1,5 لإقلاع الضاغط، ثم قرّب إلى السعة الأعلى. والوحدة المساوية تمامًا للقيمة المحسوبة ستفصل في الأيام الحارة.'),
        ('هل يكفي مثبت نوع المرحل أم يلزم سيرفو؟',
         'نوع المرحل مناسب للسبليت المنزلي على شبكة معتدلة التذبذب. اختر السيرفو حين يتغير الجهد بشدة، أو حين يشمل الحمل تبريدًا تجاريًا أو أجهزة طبية، أو حين يجب أن يكون الخرج ناعمًا لا متدرجًا.'),
        ('لماذا يفصل المثبت عند إقلاع الضاغط؟',
         'غالبًا لأن الوحدة محسوبة على تيار التشغيل فقط دون تيار الإقلاع. وقد يكون السبب هبوط جهد الدخل تحت النطاق في تلك اللحظة، أو طرف دخول مرتخيًا. افحص بهذا الترتيب: اللوحة، ثم الجهد عند الإقلاع، ثم عزم الأطراف.'),
        ('هل يمكن لمثبت واحد تغذية مكيفين؟',
         'فقط إذا كانت سعته تغطي الحمل المشترك إضافة إلى إقلاع الوحدة الأكبر، وكان احتمال إقلاعهما معًا ضعيفًا. والوحدة المستقلة لكل مكيف أسهل في الحماية والتشخيص.'),
    ],
)
