# -*- coding: utf-8 -*-
"""Content for 2026-10-23 batch - Topic A: DIN rail terminal block wiring."""

SLUG = 'din-rail-terminal-block-wiring-how-to'

A_EN = dict(
    slug=SLUG,
    lang='en',
    dir='ltr',
    title='DIN Rail Terminal Block Wiring: A Step-by-Step Installation Guide',
    desc='How to wire DIN rail terminal blocks in a control panel: conductor preparation, ferrules, torque, jumpers, end stops, PE bonding, insulation testing and the faults that cause hot terminals.',
    breadcrumb='DIN rail terminal block wiring',
    category='Wiring Guide',
    read='11 min read',
    alt='Hands fitting a device onto a DIN rail and tightening a terminal screw inside a distribution panel',
    cta='Send us your terminal schedule, conductor sizes and panel drawing. Our engineers will confirm the terminal range, accessories and quantity breaks, and quote from the factory.',
    product_url='/products/terminal-connector',
    body='''<h2>Why terminal block wiring fails in the field</h2>
<p>A DIN rail terminal block is a simple part, and that is exactly why installation errors survive inspection. The connection looks tight, the panel closes, and eighteen months later a terminal at the bottom of a cabinet is running at 40&nbsp;&deg;C above ambient because the screw was tightened onto insulation instead of copper.</p>
<p>Most of the failures we see in returned panels and site reports come from five things: the wrong strip length, stranded wire terminated without a ferrule, a screwdriver that does not match the screw head, missing end stops, and no thermal check after energising. None of them are visible on a drawing.</p>
<p>This guide walks through the sequence our panel customers use when they wire DIN rail terminals, from rail preparation to the insulation test that closes the job. It applies to screw-clamp terminals; spring-cage and push-in terminals follow the same logic with a different tool.</p>

<h2>The short answer</h2>
<p>Wire DIN rail terminal blocks in this order: mount the rail and end stops, snap the terminals on in circuit order, fit partition plates and PE terminals, prepare each conductor to the manufacturer&rsquo;s strip length, crimp a ferrule on every stranded conductor, insert to the full depth, torque to the specified value, bridge with jumper bars where the drawing requires it, mark every circuit, then test continuity and insulation resistance before energising.</p>
<p>Every step has a measurable check. If you can&rsquo;t measure it, you are relying on feel.</p>

<h2>Before you start: rail, tools and the terminal schedule</h2>
<h3>Rail and mounting</h3>
<p>Most industrial terminals snap onto 35&nbsp;mm top-hat rail to EN&nbsp;60715. Check three things before you mount anything: the rail is the correct profile, it is fixed at both ends, and it is vertical or horizontal as the enclosure design requires. A rail that flexes when you push a terminal onto it will eventually crack a mounting foot.</p>
<p>Leave 30&ndash;50&nbsp;mm of free rail at each end. You will need it for end stops and for the extra terminals that commissioning always adds.</p>
<h3>Tools that matter</h3>
<ul>
<li><strong>Insulated screwdriver matched to the screw:</strong> a Pozidriv or slotted blade that fills the head. An undersized blade rounds the screw and reduces the torque you can actually apply.</li>
<li><strong>Torque screwdriver:</strong> the only way to guarantee the specified value. Hand torque varies by more than 40&nbsp;% between technicians.</li>
<li><strong>Crimping tool matched to the ferrule profile:</strong> square or hexagonal crimp, never pliers.</li>
<li><strong>Wire stripper with an adjustable stop:</strong> not a knife.</li>
<li><strong>Continuity and insulation tester:</strong> for the commissioning checks at the end.</li>
</ul>
<h3>Read the terminal schedule first</h3>
<p>Good panels are wired from a terminal schedule that lists, for every terminal: circuit reference, conductor size, core colour, destination, and whether it is a feed-through, earth, disconnect or fused terminal. If the schedule is missing, the wiring will be reworked. Our <a href="/blog/din-rail-terminal-block-guide">DIN rail terminal block sizing guide</a> covers how to choose the block type and pitch before this stage.</p>

<h2>Step 1 &mdash; Mount end stops and terminals in circuit order</h2>
<p>Fit the left end stop first, then snap terminals on from left to right in the order of the schedule. Terminals are removed by pressing the release slot with a screwdriver and tilting the block away from the rail; they are not levered off with pliers.</p>
<p>Group by function: feeds, control, signals, earth. Put a partition plate between groups that carry different voltages, and between terminals that are bridged and terminals that are not. Partition plates are not cosmetic &mdash; they maintain creepage distance and stop a stray strand from bridging two circuits.</p>
<p>Finish with the right end stop. A terminal stack without end stops will creep along the rail every time a conductor is pushed in, and the last block can walk off the rail entirely.</p>

<h2>Step 2 &mdash; Prepare the conductor correctly</h2>
<h3>Strip length</h3>
<p>Strip to the length marked on the terminal or in its datasheet, usually printed on the side of the block. Too short and the clamp bites insulation, which creeps under load and loosens. Too long and bare copper sits outside the clamp body, reducing creepage and exposing live metal.</p>
<h3>Ferrules on every stranded conductor</h3>
<p>Stranded wire without a ferrule spreads when the screw compresses it. Individual strands break, resistance rises, and the joint heats. Crimp a ferrule &mdash; twin ferrules where two conductors enter one clamp &mdash; and check the crimp by pulling it firmly before insertion.</p>
<p>Do not tin stranded conductors that go into a screw clamp. Solder cold-flows under sustained clamp pressure and the joint loosens over thermal cycles. Tinning belongs to soldered joints, not mechanical terminals.</p>
<h3>One conductor per clamp</h3>
<p>Two conductors of different sizes in one clamp is the most common cause of a loose terminal in a panel that otherwise tests fine. Where the drawing needs two conductors, use a twin ferrule of the correct size, or move to a terminal with two separate clamping points.</p>

<h2>Step 3 &mdash; Insert, torque and bridge</h2>
<p>Push the conductor in until the insulation stops against the clamp body, then tighten. Apply the torque stated by the terminal manufacturer with a torque screwdriver; typical values for modular terminals sit in the 0.4&ndash;1.2&nbsp;N&middot;m band depending on the frame size, but the datasheet governs, not a rule of thumb.</p>
<p>After torquing, tug each conductor. A joint that moves is not terminated.</p>
<p>Where the schedule calls for a common feed, bridge adjacent terminals with the manufacturer&rsquo;s jumper bar &mdash; not with a loop of wire. Jumper bars are rated for the full current of the terminal range; a wire loop is not, and it defeats the testability of the block. Insert the jumper fully so both prongs engage, and never bridge across a partition plate.</p>
<p>Earth terminals go on the rail with a direct bond to the enclosure earth bar. The PE conductor is green-yellow for its whole visible length, and the earth terminal is the one component in the stack that must never be bridged to a live circuit.</p>

<h2>Step 4 &mdash; Mark, dress and close</h2>
<p>Mark every terminal with the circuit reference from the schedule using the manufacturer&rsquo;s marker tags. Hand-written tape falls off in a warm cabinet, and the next technician loses an hour tracing circuits.</p>
<p>Dress conductors so they enter the clamp straight, with a service loop that allows the terminal to be removed without pulling adjacent wiring. Do not run line voltage and signal wiring in the same bundle. Leave the rail ends accessible.</p>

<h2>Step 5 &mdash; Test before you energise</h2>
<p>Three checks close the job:</p>
<ul>
<li><strong>Continuity:</strong> confirm each circuit against the schedule, including earth bonding between the terminal and the enclosure.</li>
<li><strong>Insulation resistance:</strong> test at 500&nbsp;V DC between live conductors and earth with the terminals disconnected from sensitive electronics; the usual acceptance value is at least 1&nbsp;M&Omega;.</li>
<li><strong>Thermal check under load:</strong> after the panel has run at working current for a period, scan the terminal stack with a thermal camera or check by touch with appropriate precautions. A terminal noticeably hotter than its neighbours is a loose or high-resistance joint.</li>
</ul>

<h2>Common faults and what they look like</h2>
<table>
  <thead><tr><th>Symptom</th><th>Usual cause</th><th>Corrective action</th></tr></thead>
  <tbody>
    <tr><td><strong>Terminal discoloured or browning</strong></td><td>Loose screw or conductor not fully inserted</td><td>Re-terminate with a new ferrule; inspect the clamp for damage</td></tr>
    <tr><td><strong>Intermittent signal on a control circuit</strong></td><td>Insulation caught in the clamp</td><td>Re-strip to the correct length and re-terminate</td></tr>
    <tr><td><strong>Terminal stack slides on the rail</strong></td><td>Missing end stops</td><td>Fit end stops at both ends of the stack</td></tr>
    <tr><td><strong>Heat at a bridged group</strong></td><td>Wire loop instead of a rated jumper bar</td><td>Replace with the manufacturer&rsquo;s jumper bar</td></tr>
    <tr><td><strong>Earth continuity failure at test</strong></td><td>PE terminal not bonded to the rail or earth bar</td><td>Fit the correct PE terminal and bond to the enclosure bar</td></tr>
  </tbody>
</table>

<h2>What to specify when you order</h2>
<p>For a procurement list, the terminal is only half the line item. Specify: terminal type and clamping method, conductor range, pitch, colour, rated voltage and current, plus end stops, end plates, partition plates, jumper bars, marker tags and test plugs. Panels that arrive short of accessories stall at commissioning.</p>
<p>Our <a href="/products/terminal-connector">terminal and connector range</a> covers modular DIN rail blocks with brass current bars and screw clamps, together with the accessories that go with them. If you are still choosing between identification styles, the <a href="/blog/terminal-blocks-connectors-identification-guide">terminal identification chart</a> maps the common families.</p>

<h2>Frequently asked: the questions buyers ask us</h2>
<p>The FAQ below covers the points that come up in almost every panel enquiry &mdash; torque, mixed conductor sizes, spring versus screw, and whether ferrules are mandatory.</p>''',
    specs=[
        ('Rail profile', '35 mm top-hat rail to EN 60715, fixed at both ends'),
        ('Conductor preparation', 'Strip to manufacturer length; ferrule on every stranded conductor'),
        ('Termination check', 'Tug test after torquing; one conductor per clamp unless a twin ferrule is used'),
        ('Bridging', 'Manufacturer-rated jumper bar, never a wire loop'),
        ('Commissioning test', 'Continuity, 500 V DC insulation resistance (≥ 1 MΩ), thermal check under load'),
    ],
    faqs=[
        ('What torque should I use on a DIN rail terminal block?',
         'Use the value stated by the terminal manufacturer for that frame size, applied with a torque screwdriver. Modular terminals commonly fall in the 0.4 to 1.2 N·m band, but the datasheet is the governing figure because frame size, screw head and clamp design all change the requirement.'),
        ('Can I put two conductors in one terminal clamp?',
         'Only where the terminal is designed for it and both conductors are the same size, using a twin ferrule of the correct profile. Mixing conductor sizes in one clamp is the most common cause of a joint that loosens under thermal cycling.'),
        ('Are ferrules required on stranded wire in screw-clamp terminals?',
         'Yes for reliable industrial work. Without a ferrule the strands spread under clamp pressure, some break, and resistance rises at the joint. Do not tin the conductor instead: solder cold-flows and the joint loosens over time.'),
        ('Do I need end stops and partition plates?',
         'Both. End stops prevent the stack from sliding along the rail when conductors are inserted, and partition plates maintain creepage distance between circuits at different voltages or between bridged and unbonded groups.'),
    ],
)

A_FR = dict(
    slug=SLUG + '-fr',
    lang='fr',
    dir='ltr',
    title='Câblage des bornes à rail DIN : guide d\'installation pas à pas',
    desc='Comment câbler des bornes à rail DIN dans une armoire électrique : préparation des conducteurs, embouts, couple de serrage, peignes, butées, liaison PE, essais d\'isolement et défauts responsables des bornes chaudes.',
    breadcrumb='Câblage des bornes à rail DIN',
    category='Guide de câblage',
    read='11 min de lecture',
    alt='Mains installant un appareil sur rail DIN et serrant une vis de borne dans un tableau de distribution',
    cta='Transmettez-nous votre tableau de bornes, les sections de conducteurs et le schéma d\'armoire. Nos ingénieurs confirment la gamme, les accessoires et les paliers de quantité, puis établissent le devis usine.',
    product_url='/products/terminal-connector',
    body='''<h2>Pourquoi les bornes à rail DIN chauffent en exploitation</h2>
<p>Une borne à rail DIN est une pièce simple, et c&rsquo;est précisément pour cela que les erreurs de pose passent inaperçues. Le serrage semble correct, l&rsquo;armoire se ferme, et dix-huit mois plus tard une borne en bas du coffret tourne à 40&nbsp;&deg;C au-dessus de l&rsquo;ambiance parce que la vis a été serrée sur l&rsquo;isolant et non sur le cuivre.</p>
<p>Dans les retours d&rsquo;armoires et les rapports de chantier que nous traitons, cinq causes reviennent : une longueur de dénudage incorrecte, un conducteur multibrins sans embout, un tournevis inadapté à la tête de vis, des butées absentes et l&rsquo;absence de contrôle thermique après mise sous tension. Aucune n&rsquo;apparaît sur un plan.</p>
<p>Ce guide reprend la séquence appliquée par nos clients installateurs, du montage du rail jusqu&rsquo;à l&rsquo;essai d&rsquo;isolement qui clôt le chantier. Il traite des bornes à serrage par vis ; les bornes à ressort et à enfichage suivent la même logique avec un outillage différent.</p>

<h2>La réponse courte</h2>
<p>Montez le rail et les butées, clipsez les bornes dans l&rsquo;ordre du schéma, posez les cloisons et les bornes de terre, dénudez chaque conducteur à la longueur prescrite, sertissez un embout sur tout conducteur souple, enfoncez à fond, serrez au couple spécifié, peignez les bornes concernées, repérez chaque circuit, puis réalisez les essais de continuité et d&rsquo;isolement avant la mise sous tension.</p>
<p>Chaque étape possède un contrôle mesurable. Sans mesure, on travaille au ressenti.</p>

<h2>Avant de commencer : rail, outillage et tableau de bornes</h2>
<h3>Rail et fixation</h3>
<p>La majorité des bornes industrielles se clipsent sur un rail profilé 35&nbsp;mm conforme à la norme EN&nbsp;60715. Vérifiez trois points avant tout montage : le profil du rail, sa fixation aux deux extrémités et son orientation, verticale ou horizontale, selon la conception de l&rsquo;enveloppe. Un rail qui fléchit lorsqu&rsquo;on clipse une borne finira par casser un pied de fixation.</p>
<p>Laissez 30 à 50&nbsp;mm de rail libre à chaque extrémité : cet espace reçoit les butées et les quelques bornes que la mise en service ajoute toujours.</p>
<h3>L&rsquo;outillage qui compte</h3>
<ul>
<li><strong>Tournevis isolé adapté à la vis :</strong> une lame Pozidriv ou plate qui remplit l&rsquo;empreinte. Une lame trop petite arrondit la vis et réduit le couple réellement appliqué.</li>
<li><strong>Tournevis dynamométrique :</strong> seule façon de garantir la valeur prescrite. Le couple appliqué à la main varie de plus de 40&nbsp;% d&rsquo;un technicien à l&rsquo;autre.</li>
<li><strong>Pince à sertir adaptée au profil de l&rsquo;embout :</strong> sertissage carré ou hexagonal, jamais une pince universelle.</li>
<li><strong>Pince à dénuder avec butée réglable :</strong> pas de lame de couteau.</li>
<li><strong>Contrôleur de continuité et d&rsquo;isolement :</strong> pour les essais finaux.</li>
</ul>
<h3>Lire le tableau de bornes</h3>
<p>Une armoire bien construite se câble à partir d&rsquo;un tableau de bornes qui indique, pour chaque borne : repère de circuit, section, couleur d&rsquo;âme, destination et type (traversante, terre, sectionnement, porte-fusible). Sans ce document, le câblage sera repris. Notre <a href="/blog/din-rail-terminal-block-guide">guide de dimensionnement des bornes à rail DIN</a> traite du choix du type et du pas en amont de cette étape.</p>

<h2>Étape 1 &mdash; Butées et bornes dans l&rsquo;ordre du schéma</h2>
<p>Posez d&rsquo;abord la butée de gauche, puis clipsez les bornes de gauche à droite selon le tableau. Une borne se dépose en appuyant sur la fente de déverrouillage avec un tournevis et en basculant le bloc hors du rail ; elle ne se démonte pas au levier.</p>
<p>Regroupez par fonction : alimentations, commande, signaux, terre. Intercalez une cloison entre deux groupes de tensions différentes, et entre bornes peignées et bornes non peignées. La cloison n&rsquo;est pas décorative : elle maintient la ligne de fuite et empêche un brin errant de ponter deux circuits.</p>
<p>Terminez par la butée de droite. Sans butées, l&rsquo;empilage migre sur le rail à chaque insertion de conducteur et la dernière borne peut sortir du rail.</p>

<h2>Étape 2 &mdash; Préparer correctement le conducteur</h2>
<h3>Longueur de dénudage</h3>
<p>Dénudez à la longueur indiquée sur la borne ou dans sa fiche technique, souvent imprimée sur le flanc du bloc. Trop courte, la pince mord l&rsquo;isolant, qui fluage sous charge et se desserre. Trop longue, du cuivre nu reste hors du corps de serrage, ce qui réduit la ligne de fuite et expose du métal sous tension.</p>
<h3>Un embout sur chaque conducteur souple</h3>
<p>Un conducteur multibrins sans embout s&rsquo;étale sous la pression de la vis : des brins cassent, la résistance augmente et le point chauffe. Sertissez un embout &mdash; double embout lorsque deux conducteurs entrent dans la même pince &mdash; et tirez fermement dessus avant insertion pour valider le sertissage.</p>
<p>Ne étamez pas un conducteur souple destiné à une borne à vis. L&rsquo;étain fluage sous la pression de serrage et le joint se desserre au fil des cycles thermiques. L&rsquo;étamage appartient aux jonctions soudées, pas aux bornes mécaniques.</p>
<h3>Un conducteur par pince</h3>
<p>Deux conducteurs de sections différentes dans une même pince constituent la première cause de borne desserrée dans une armoire par ailleurs conforme aux essais. Lorsque le schéma impose deux conducteurs, utilisez un double embout de calibre correct ou passez à une borne à deux points de serrage distincts.</p>

<h2>Étape 3 &mdash; Insérer, serrer, peigner</h2>
<p>Enfoncez le conducteur jusqu&rsquo;à ce que l&rsquo;isolant bute contre le corps de serrage, puis serrez. Appliquez le couple indiqué par le fabricant avec un tournevis dynamométrique ; les valeurs courantes des bornes modulaires se situent entre 0,4 et 1,2&nbsp;N&middot;m selon la taille du corps, mais c&rsquo;est la fiche technique qui fait foi, pas une règle empirique.</p>
<p>Après serrage, tirez sur chaque conducteur. Un joint qui bouge n&rsquo;est pas raccordé.</p>
<p>Lorsque le schéma prévoit une alimentation commune, peignez les bornes adjacentes avec le peigne du fabricant &mdash; pas avec une boucle de fil. Un peigne est dimensionné pour le courant de la gamme ; une boucle de fil ne l&rsquo;est pas et rend le bloc non testable. Enfoncez le peigne à fond pour que les deux griffes s&rsquo;engagent, et ne peignez jamais à travers une cloison.</p>
<p>Les bornes de terre se montent sur le rail avec une liaison directe à la barre de terre de l&rsquo;enveloppe. Le conducteur PE est vert-jaune sur toute sa longueur visible, et la borne de terre est le seul élément de l&rsquo;empilage qui ne doit jamais être peigné vers un circuit sous tension.</p>

<h2>Étape 4 &mdash; Repérer, habiller, fermer</h2>
<p>Repérez chaque borne avec l&rsquo;indication du tableau, à l&rsquo;aide des porte-étiquettes du fabricant. Une bande adhésive manuscrite se décolle dans une armoire chaude, et le technicien suivant perd une heure à repérer les circuits.</p>
<p>Habillez les conducteurs pour qu&rsquo;ils entrent droit dans la pince, avec une boucle de service permettant de déposer la borne sans tirer sur le câblage voisin. Ne faites pas cheminer puissance et signaux dans le même faisceau. Laissez les extrémités de rail accessibles.</p>

<h2>Étape 5 &mdash; Tester avant la mise sous tension</h2>
<p>Trois contrôles closent le chantier :</p>
<ul>
<li><strong>Continuité :</strong> vérifiez chaque circuit au regard du tableau, y compris la liaison de terre entre la borne et l&rsquo;enveloppe.</li>
<li><strong>Résistance d&rsquo;isolement :</strong> mesurez à 500&nbsp;V continu entre conducteurs actifs et terre, bornes déconnectées de l&rsquo;électronique sensible ; la valeur d&rsquo;acceptation usuelle est d&rsquo;au moins 1&nbsp;M&Omega;.</li>
<li><strong>Contrôle thermique en charge :</strong> après une période de fonctionnement au courant nominal, balayez l&rsquo;empilage à la caméra thermique ou vérifiez au toucher avec les précautions d&rsquo;usage. Une borne nettement plus chaude que ses voisines signale un serrage insuffisant ou une résistance de contact élevée.</li>
</ul>

<h2>Défauts fréquents et symptômes</h2>
<table>
  <thead><tr><th>Symptôme</th><th>Cause habituelle</th><th>Action corrective</th></tr></thead>
  <tbody>
    <tr><td><strong>Borne colorée ou brunie</strong></td><td>Vis desserrée ou conducteur mal enfoncé</td><td>Reprendre le raccordement avec un embout neuf ; inspecter la pince</td></tr>
    <tr><td><strong>Signal intermittent sur un circuit de commande</strong></td><td>Isolant coincé dans la pince</td><td>Dénuder à la bonne longueur et raccorder à nouveau</td></tr>
    <tr><td><strong>Empilage qui glisse sur le rail</strong></td><td>Butées absentes</td><td>Poser des butées aux deux extrémités</td></tr>
    <tr><td><strong>Échauffement d&rsquo;un groupe peigné</strong></td><td>Boucle de fil au lieu d&rsquo;un peigne dimensionné</td><td>Remplacer par le peigne du fabricant</td></tr>
    <tr><td><strong>Défaut de continuité de terre à l&rsquo;essai</strong></td><td>Borne PE non reliée au rail ou à la barre de terre</td><td>Poser la borne PE adaptée et la relier à la barre de l&rsquo;enveloppe</td></tr>
  </tbody>
</table>

<h2>Ce qu&rsquo;il faut spécifier à la commande</h2>
<p>Dans une liste d&rsquo;approvisionnement, la borne ne représente que la moitié de la ligne. Précisez : type et mode de serrage, plage de section, pas, couleur, tension et courant assignés, ainsi que butées, plaques d&rsquo;extrémité, cloisons, peignes, porte-étiquettes et fiches de test. Les armoires livrées sans accessoires s&rsquo;arrêtent à la mise en service.</p>
<p>Notre <a href="/products/terminal-connector">gamme de bornes et connecteurs</a> comprend des bornes modulaires à rail DIN avec barres de courant en laiton et serrages à vis, ainsi que les accessoires associés. Si vous hésitez encore entre familles, <a href="/blog/terminal-blocks-connectors-identification-guide">le tableau d&rsquo;identification des bornes</a> récapitule les grandes séries.</p>

<h2>En résumé</h2>
<p>La fiabilité d&rsquo;un raccordement à rail DIN ne dépend ni du prix de la borne ni de la marque de l&rsquo;armoire, mais de quatre gestes répétés avec méthode : dénuder juste, sertir systématiquement, serrer au couple et contrôler en charge. Ces quatre gestes coûtent quelques minutes par armoire et évitent la plupart des interventions de garantie.</p>''',
    specs=[
        ('Profil de rail', 'Rail profilé 35 mm selon EN 60715, fixé aux deux extrémités'),
        ('Préparation du conducteur', 'Dénudage à la longueur fabricant ; embout sur tout conducteur souple'),
        ('Contrôle du raccordement', 'Traction après serrage ; un conducteur par pince sauf double embout'),
        ('Peignage', 'Peigne dimensionné par le fabricant, jamais une boucle de fil'),
        ('Essais de réception', 'Continuité, isolement 500 V DC (≥ 1 MΩ), contrôle thermique en charge'),
    ],
    faqs=[
        ('Quel couple de serrage appliquer sur une borne à rail DIN ?',
         'Celui indiqué par le fabricant pour cette taille de corps, appliqué au tournevis dynamométrique. Les bornes modulaires se situent souvent entre 0,4 et 1,2 N·m, mais la fiche technique fait foi car la conception de la pince et de la vis modifie l\'exigence.'),
        ('Peut-on mettre deux conducteurs dans une même pince ?',
         'Uniquement si la borne est prévue pour cela, avec deux conducteurs de même section et un double embout adapté. Mélanger les sections dans une pince est la première cause de desserrage sous cycles thermiques.'),
        ('Les embouts sont-ils obligatoires sur conducteur souple ?',
         'Oui pour un raccordement industriel fiable. Sans embout, les brins s\'étalent sous la pression, certains cassent et la résistance du point augmente. Il ne faut pas non plus étamer le conducteur : l\'étain fluage et le joint se desserre.'),
        ('Faut-il des butées et des cloisons ?',
         'Les deux. Les butées empêchent l\'empilage de glisser lors de l\'insertion des conducteurs ; les cloisons maintiennent la ligne de fuite entre circuits de tensions différentes ou entre groupes peignés et non peignés.'),
    ],
)

A_ES = dict(
    slug=SLUG + '-es',
    lang='es',
    dir='ltr',
    title='Cableado de borneras de carril DIN: guía de instalación paso a paso',
    desc='Cómo cablear borneras de carril DIN en un tablero eléctrico: preparación del conductor, punteras, par de apriete, peines, topes, conexión de tierra, ensayos de aislamiento y fallos que provocan bornes calientes.',
    breadcrumb='Cableado de borneras de carril DIN',
    category='Guía de cableado',
    read='11 min de lectura',
    alt='Manos instalando un aparato sobre carril DIN y apretando un tornillo de borne dentro de un cuadro de distribución',
    cta='Envíenos su lista de borneras, las secciones de conductor y el esquema del tablero. Nuestros ingenieros confirman la gama, los accesorios y los tramos de cantidad, y cotizan desde fábrica.',
    product_url='/products/terminal-connector',
    body='''<h2>Por qué falla el cableado con borneras de carril DIN</h2>
<p>Una bornera de carril DIN es una pieza sencilla, y por eso mismo los errores de instalación sobreviven a la inspección. La conexión parece firme, el tablero se cierra y, dieciocho meses después, una bornera en la parte baja del gabinete trabaja a 40&nbsp;&deg;C por encima de la ambiente porque el tornillo apretó sobre el aislamiento y no sobre el cobre.</p>
<p>En los tableros devueltos y en los informes de obra que recibimos, cinco causas se repiten: longitud de pelado incorrecta, conductor flexible sin puntera, destornillador que no corresponde a la cabeza del tornillo, topes ausentes y falta de control térmico tras energizar. Ninguna aparece en un plano.</p>
<p>Esta guía sigue la secuencia que aplican nuestros clientes armadores, desde el montaje del riel hasta el ensayo de aislamiento que cierra el trabajo. Se refiere a borneras de apriete por tornillo; las de resorte y de inserción directa siguen la misma lógica con otra herramienta.</p>

<h2>La respuesta corta</h2>
<p>Monte el riel y los topes, encaje las borneras en el orden del esquema, coloque separadores y borneras de tierra, pele cada conductor a la longitud indicada, engaste una puntera en todo conductor flexible, inserte a fondo, apriete al par especificado, puentee con peine donde el plano lo exija, identifique cada circuito y realice los ensayos de continuidad y aislamiento antes de energizar.</p>
<p>Cada paso tiene una comprobación medible. Si no se puede medir, se está trabajando de memoria.</p>

<h2>Antes de empezar: riel, herramientas y lista de borneras</h2>
<h3>Riel y montaje</h3>
<p>La mayoría de las borneras industriales se encajan en riel perfilado de 35&nbsp;mm según EN&nbsp;60715. Verifique tres cosas antes de montar: el perfil del riel, su fijación en ambos extremos y su orientación, vertical u horizontal, según el diseño del gabinete. Un riel que flexiona al encajar una bornera terminará rompiendo un pie de fijación.</p>
<p>Deje 30 a 50&nbsp;mm de riel libre en cada extremo. Allí van los topes y las borneras que la puesta en marcha siempre agrega.</p>
<h3>Herramientas que importan</h3>
<ul>
<li><strong>Destornillador aislado ajustado al tornillo:</strong> una hoja Pozidriv o plana que llene la cabeza. Una hoja pequeña redondea el tornillo y reduce el par realmente aplicado.</li>
<li><strong>Destornillador dinamométrico:</strong> la única forma de garantizar el par especificado. El par aplicado a mano varía más de un 40&nbsp;% entre técnicos.</li>
<li><strong>Pinza de engaste adecuada al perfil de la puntera:</strong> engaste cuadrado o hexagonal, nunca alicates.</li>
<li><strong>Pelacables con tope ajustable:</strong> no un cuchillo.</li>
<li><strong>Equipo de continuidad y aislamiento:</strong> para las pruebas finales.</li>
</ul>
<h3>Lea primero la lista de borneras</h3>
<p>Un tablero bien construido se cablea desde una lista que indica, para cada bornera: referencia de circuito, sección, color del conductor, destino y tipo (pasante, tierra, seccionadora, portafusible). Sin ese documento el cableado se rehace. Nuestra <a href="/blog/din-rail-terminal-block-guide">guía de dimensionamiento de borneras de carril DIN</a> trata la elección de tipo y paso antes de esta etapa.</p>

<h2>Paso 1 &mdash; Topes y borneras en el orden del esquema</h2>
<p>Coloque primero el tope izquierdo y luego encaje las borneras de izquierda a derecha según la lista. Una bornera se retira presionando la ranura de liberación con un destornillador e inclinando el bloque fuera del riel; no se desmonta haciendo palanca.</p>
<p>Agrupe por función: alimentaciones, mando, señales, tierra. Intercale un separador entre grupos con tensiones distintas y entre borneras puenteadas y no puenteadas. El separador no es decorativo: mantiene la distancia de fuga e impide que un hilo suelto puentee dos circuitos.</p>
<p>Termine con el tope derecho. Sin topes, la pila se desplaza por el riel cada vez que se inserta un conductor y la última bornera puede salirse.</p>

<h2>Paso 2 &mdash; Preparar bien el conductor</h2>
<h3>Longitud de pelado</h3>
<p>Pele a la longitud marcada en la bornera o en su ficha técnica, habitualmente impresa en el lateral del bloque. Si es corta, la mordaza atrapa aislamiento, que fluye bajo carga y se afloja. Si es larga, queda cobre desnudo fuera del cuerpo de apriete, lo que reduce la distancia de fuga y expone metal con tensión.</p>
<h3>Puntera en todo conductor flexible</h3>
<p>Un conductor flexible sin puntera se abre al comprimirlo el tornillo: algunos hilos se rompen, la resistencia sube y la unión se calienta. Engaste una puntera &mdash; doble puntera cuando entran dos conductores en la misma mordaza &mdash; y tire con firmeza antes de insertar para validar el engaste.</p>
<p>No estañe el conductor flexible destinado a una bornera de tornillo. El estaño fluye bajo la presión del apriete y la unión se afloja con los ciclos térmicos. Estañar pertenece a las uniones soldadas, no a los bornes mecánicos.</p>
<h3>Un conductor por mordaza</h3>
<p>Dos conductores de secciones distintas en una misma mordaza son la causa más frecuente de una bornera floja en un tablero que por lo demás pasa las pruebas. Cuando el plano exige dos conductores, use una doble puntera del calibre correcto o pase a una bornera con dos puntos de apriete independientes.</p>

<h2>Paso 3 &mdash; Insertar, apretar y puentear</h2>
<p>Inserte el conductor hasta que el aislamiento tope con el cuerpo de apriete y apriete. Aplique el par indicado por el fabricante con destornillador dinamométrico; en borneras modulares los valores habituales están entre 0,4 y 1,2&nbsp;N&middot;m según el tamaño del cuerpo, pero manda la ficha técnica, no una regla empírica.</p>
<p>Después de apretar, tire de cada conductor. Una unión que se mueve no está conectada.</p>
<p>Cuando el esquema prevé una alimentación común, puentee borneras contiguas con el peine del fabricante &mdash; no con un lazo de cable. El peine está dimensionado para la corriente de la gama; un lazo de cable no lo está y además impide probar el bloque. Inserte el peine a fondo para que ambos dientes engranen y nunca puentee a través de un separador.</p>
<p>Las borneras de tierra se montan en el riel con unión directa a la barra de tierra del gabinete. El conductor de protección es verde-amarillo en toda su longitud visible, y la bornera de tierra es el único elemento de la pila que nunca debe puentearse a un circuito con tensión.</p>

<h2>Paso 4 &mdash; Identificar, ordenar y cerrar</h2>
<p>Identifique cada bornera con la referencia de la lista usando los portarótulos del fabricante. Una cinta escrita a mano se despega en un gabinete caliente y el siguiente técnico pierde una hora rastreando circuitos.</p>
<p>Acomode los conductores para que entren rectos en la mordaza, con una curva de servicio que permita retirar la bornera sin tirar del cableado vecino. No lleve fuerza y señal por el mismo mazo. Deje accesibles los extremos del riel.</p>

<h2>Paso 5 &mdash; Probar antes de energizar</h2>
<p>Tres comprobaciones cierran el trabajo:</p>
<ul>
<li><strong>Continuidad:</strong> verifique cada circuito contra la lista, incluida la unión de tierra entre la bornera y el gabinete.</li>
<li><strong>Resistencia de aislamiento:</strong> mida a 500&nbsp;V CC entre conductores activos y tierra, con las borneras desconectadas de la electrónica sensible; el valor de aceptación habitual es de al menos 1&nbsp;M&Omega;.</li>
<li><strong>Control térmico en carga:</strong> tras un periodo funcionando a corriente nominal, barra la pila con cámara termográfica o compruebe al tacto con las precauciones debidas. Una bornera claramente más caliente que sus vecinas indica apriete insuficiente o resistencia de contacto elevada.</li>
</ul>

<h2>Fallos frecuentes y cómo se ven</h2>
<table>
  <thead><tr><th>Síntoma</th><th>Causa habitual</th><th>Acción correctiva</th></tr></thead>
  <tbody>
    <tr><td><strong>Bornera decolorada o pardusca</strong></td><td>Tornillo flojo o conductor mal insertado</td><td>Rehacer la conexión con puntera nueva; revisar la mordaza</td></tr>
    <tr><td><strong>Señal intermitente en un circuito de mando</strong></td><td>Aislamiento atrapado en la mordaza</td><td>Pelar a la longitud correcta y reconectar</td></tr>
    <tr><td><strong>La pila se desplaza en el riel</strong></td><td>Faltan topes</td><td>Instalar topes en ambos extremos</td></tr>
    <tr><td><strong>Calor en un grupo puenteado</strong></td><td>Lazo de cable en lugar de peine dimensionado</td><td>Sustituir por el peine del fabricante</td></tr>
    <tr><td><strong>Falla de continuidad de tierra en el ensayo</strong></td><td>Bornera de protección no unida al riel o a la barra</td><td>Colocar la bornera adecuada y unir a la barra del gabinete</td></tr>
  </tbody>
</table>

<h2>Qué especificar al comprar</h2>
<p>En una lista de compra, la bornera es solo la mitad de la línea. Precise: tipo y método de apriete, rango de sección, paso, color, tensión y corriente asignadas, además de topes, placas de extremo, separadores, peines, portarótulos y fichas de prueba. Los tableros que llegan sin accesorios se detienen en la puesta en marcha.</p>
<p>Nuestra <a href="/products/terminal-connector">gama de bornes y conectores</a> incluye borneras modulares de carril DIN con barras de corriente de latón y apriete por tornillo, junto con sus accesorios. Si aún duda entre familias, <a href="/blog/terminal-blocks-connectors-identification-guide">la tabla de identificación de borneras</a> resume las series más comunes.</p>

<h2>En resumen</h2>
<p>La fiabilidad de una conexión en carril DIN no depende del precio de la bornera ni de la marca del tablero, sino de cuatro gestos repetidos con método: pelar justo, engastar siempre, apretar al par y comprobar en carga. Cuestan unos minutos por tablero y evitan la mayoría de las visitas de garantía.</p>''',
    specs=[
        ('Perfil de riel', 'Riel perfilado de 35 mm según EN 60715, fijado en ambos extremos'),
        ('Preparación del conductor', 'Pelado a la longitud del fabricante; puntera en todo conductor flexible'),
        ('Verificación de unión', 'Prueba de tracción tras apretar; un conductor por mordaza salvo doble puntera'),
        ('Puentado', 'Peine homologado por el fabricante, nunca un lazo de cable'),
        ('Ensayos de puesta en marcha', 'Continuidad, aislamiento a 500 V CC (≥ 1 MΩ) y control térmico en carga'),
    ],
    faqs=[
        ('¿Qué par de apriete debo aplicar en una bornera de carril DIN?',
         'El indicado por el fabricante para ese tamaño de cuerpo, aplicado con destornillador dinamométrico. En borneras modulares suele estar entre 0,4 y 1,2 N·m, pero manda la ficha técnica porque el diseño de la mordaza y del tornillo cambia el requisito.'),
        ('¿Se pueden poner dos conductores en una misma mordaza?',
         'Solo si la bornera está diseñada para ello, con conductores de la misma sección y una doble puntera adecuada. Mezclar secciones en una mordaza es la causa más común de aflojamiento por ciclos térmicos.'),
        ('¿Son obligatorias las punteras en conductor flexible?',
         'Sí para un trabajo industrial fiable. Sin puntera los hilos se abren bajo la presión del tornillo, algunos se rompen y la resistencia de la unión sube. Tampoco conviene estañar el conductor: el estaño fluye y la unión se afloja.'),
        ('¿Hacen falta topes y separadores?',
         'Los dos. Los topes impiden que la pila se desplace al insertar conductores; los separadores mantienen la distancia de fuga entre circuitos de distinta tensión o entre grupos puenteados y no puenteados.'),
    ],
)

A_AR = dict(
    slug=SLUG + '-ar',
    lang='ar',
    dir='rtl',
    title='توصيل أطراف سكة DIN: دليل تركيب خطوة بخطوة',
    desc='كيفية توصيل أطراف سكة DIN داخل لوحة التحكم: تحضير الموصل، الأطراف المضغوطة، عزم الربط، قضبان التوصيل، المصادر النهائية، ربط الأرضي، واختبار العزل والأخطاء التي تسبب سخونة الأطراف.',
    breadcrumb='توصيل أطراف سكة DIN',
    category='دليل التوصيل',
    read='11 دقيقة قراءة',
    alt='يدان تركبان جهازًا على سكة DIN وتشدان برغي طرف توصيل داخل لوحة توزيع',
    cta='أرسل لنا جدول الأطراف ومقاطع الموصلات ومخطط اللوحة. سيراجع مهندسونا النطاق والملحقات وشرائح الكميات، ثم يقدمون عرض سعر من المصنع.',
    product_url='/products/terminal-connector',
    body='''<h2>لماذا تفشل توصيلات سكة DIN في الموقع</h2>
<p>طرف سكة DIN قطعة بسيطة، ولهذا بالضبط تمر أخطاء التركيب دون أن يلاحظها أحد. يبدو الربط محكمًا، ويُغلق الصندوق، وبعد ثمانية عشر شهرًا يعمل طرف في أسفل اللوحة بحرارة تزيد 40&nbsp;&deg;C عن المحيط لأن البرغي أُحكم على العزل لا على النحاس.</p>
<p>في اللوحات المعادة وتقارير المواقع التي نستلمها تتكرر خمسة أسباب: طول تقشير غير صحيح، موصل مجدول دون طرف مضغوط، مفك لا يطابق رأس البرغي، غياب المصادر النهائية، وعدم إجراء فحص حراري بعد التغذية. لا يظهر أي منها على المخطط.</p>
<p>يتبع هذا الدليل التسلسل الذي يعتمده عملاؤنا من مصنّعي اللوحات، من تجهيز السكة حتى اختبار العزل الذي يُغلق العمل. وهو يخص الأطراف ذات الربط اللولبي؛ أما أطراف النابض والإدخال المباشر فتتبع المنطق نفسه بأداة مختلفة.</p>

<h2>الإجابة المختصرة</h2>
<p>ثبّت السكة والمصادر النهائية، ثم أدخل الأطراف بترتيب المخطط، وركّب الحواجز الفاصلة وأطراف الأرضي، وقشّر كل موصل بالطول المحدد، واضغط طرفًا على كل موصل مجدول، وأدخل حتى النهاية، وأحكم الربط بالعزم المحدد، ووصّل بقضبان التوصيل حيث يطلب المخطط، ورمّز كل دائرة، ثم نفّذ اختبار الاستمرارية والعزل قبل التغذية.</p>
<p>لكل خطوة فحص قابل للقياس. وما لا يمكن قياسه يعتمد على التقدير الشخصي.</p>

<h2>قبل البدء: السكة والعدد وجدول الأطراف</h2>
<h3>السكة والتثبيت</h3>
<p>تُثبّت معظم الأطراف الصناعية على سكة مقاس 35&nbsp;مم وفق EN&nbsp;60715. تحقق من ثلاثة أمور قبل التركيب: مقطع السكة، وتثبيتها من الطرفين، واتجاهها رأسيًا أو أفقيًا بحسب تصميم الصندوق. السكة التي تنثني عند إدخال طرف ستنكسر إحدى قوائم تثبيتها في النهاية.</p>
<p>اترك 30 إلى 50&nbsp;مم من السكة فارغة عند كل طرف؛ فهي مخصصة للمصادر النهائية وللأطراف التي يضيفها التشغيل دائمًا.</p>
<h3>العدد التي تهم</h3>
<ul>
<li><strong>مفك معزول مطابق للبرغي:</strong> رأس Pozidriv أو مسطح يملأ تجويف البرغي. الرأس الصغير يبرّد زوايا البرغي ويقلل العزم المطبق فعليًا.</li>
<li><strong>مفك عزم:</strong> الطريقة الوحيدة لضمان القيمة المحددة. العزم اليدوي يتفاوت بأكثر من 40&nbsp;% بين فني وآخر.</li>
<li><strong>كماشة ضغط مطابقة لشكل الطرف المضغوط:</strong> ضغط مربع أو سداسي، وليس كماشة عادية.</li>
<li><strong>قشارة أسلاك بصدادة قابلة للضبط:</strong> لا سكين.</li>
<li><strong>جهاز استمرارية وعزل:</strong> لاختبارات التسليم.</li>
</ul>
<h3>اقرأ جدول الأطراف أولًا</h3>
<p>اللوحة الجيدة تُوصَّل من جدول يحدد لكل طرف: مرجع الدائرة، المقطع، لون القلب، الوجهة، والنوع (عابر، أرضي، فصل، حامل مصهر). وبدون هذا المستند ستُعاد الأعمال. يشرح <a href="/blog/din-rail-terminal-block-guide">دليل اختيار أطراف سكة DIN</a> كيفية اختيار النوع والمسافة بين الأطراف قبل هذه المرحلة.</p>

<h2>الخطوة 1 &mdash; المصادر والأطراف بترتيب المخطط</h2>
<p>ركّب المصد الأيسر أولًا، ثم أدخل الأطراف من اليسار إلى اليمين وفق الجدول. يُفك الطرف بالضغط على فتحة التحرير بمفك وإمالة الجسم بعيدًا عن السكة، ولا يُخلع بالعتلة.</p>
<p>جمّع حسب الوظيفة: التغذية، التحكم، الإشارات، الأرضي. وضع حاجزًا فاصلًا بين مجموعات ذات جهود مختلفة، وبين أطراف موصولة بقضيب وأخرى غير موصولة. الحاجز ليس شكليًا: فهو يحافظ على مسافة الزحف الكهربائي ويمنع شعيرة سائبة من توصيل دائرتين.</p>
<p>أنهِ العمل بالمصد الأيمن. فبدون المصادر تنزلق المجموعة على السكة مع كل إدخال موصل، وقد يخرج الطرف الأخير من السكة تمامًا.</p>

<h2>الخطوة 2 &mdash; تحضير الموصل بشكل صحيح</h2>
<h3>طول التقشير</h3>
<p>قشّر بالطول المحدد على الطرف أو في ورقة بياناته، وغالبًا ما يكون مطبوعًا على جانب الجسم. التقشير الأقصر يجعل الملقط يعض العزل، والعزل يزحف تحت الحمل ويرتخي. والأطول يترك نحاسًا عاريًا خارج جسم الربط، ما يقلل مسافة الزحف ويكشف معدنًا مكهربًا.</p>
<h3>طرف مضغوط على كل موصل مجدول</h3>
<p>الموصل المجدول دون طرف مضغوط يتفتح تحت ضغط البرغي: تنكسر بعض الشعيرات، وترتفع المقاومة، وتسخن الوصلة. اضغط طرفًا — أو طرفًا مزدوجًا عند دخول موصلين في الملقط نفسه — واسحب بقوة قبل الإدخال للتأكد من الضغط.</p>
<p>لا تقم بقصدير الموصل المجدول المخصص لطرف لولبي. القصدير يزحف تحت ضغط الربط وترتخي الوصلة مع الدورات الحرارية. القصدير مكانه الوصلات الملحومة لا الأطراف الميكانيكية.</p>
<h3>موصل واحد لكل ملقط</h3>
<p>وجود موصلين بمقطعين مختلفين في ملقط واحد هو السبب الأكثر شيوعًا لارتخاء طرف في لوحة تجتاز بقية الاختبارات. وعندما يفرض المخطط موصلين، استخدم طرفًا مزدوجًا بالمقاس الصحيح أو انتقل إلى طرف بنقطتي ربط منفصلتين.</p>

<h2>الخطوة 3 &mdash; الإدخال والربط والتوصيل</h2>
<p>أدخل الموصل حتى يستقر العزل على جسم الربط ثم أحكم. طبّق العزم المحدد من الشركة المصنعة بمفك عزم؛ والقيم المعتادة للأطراف المعيارية تتراوح بين 0,4 و1,2&nbsp;نيوتن·متر بحسب حجم الجسم، لكن ورقة البيانات هي المرجع لا القاعدة التقريبية.</p>
<p>بعد الربط اسحب كل موصل. الوصلة التي تتحرك غير موصولة.</p>
<p>عندما يطلب المخطط تغذية مشتركة، وصّل الأطراف المتجاورة بقضيب التوصيل الخاص بالشركة المصنعة — لا بحلقة سلك. القضيب مصمم لتيار النطاق كاملًا، وحلقة السلك ليست كذلك، كما أنها تمنع اختبار الطرف. أدخل القضيب حتى النهاية لتتعشق السنّتان، ولا تعبر أبدًا عبر حاجز فاصل.</p>
<p>تُركّب أطراف الأرضي على السكة بربط مباشر بقضيب الأرضي في الصندوق. والموصل الأرضي أخضر-أصفر بطوله الظاهر كله، وطرف الأرضي هو العنصر الوحيد في المجموعة الذي لا يجوز توصيله بدائرة مكهربة.</p>

<h2>الخطوة 4 &mdash; الترميز والترتيب والإغلاق</h2>
<p>رمّز كل طرف بمرجع الدائرة من الجدول باستخدام حاملات البطاقات الخاصة بالشركة المصنعة. الشريط المكتوب بخط اليد يسقط داخل صندوق ساخن، ويضيع الفني التالي ساعة في تتبع الدوائر.</p>
<p>رتّب الموصلات لت دخل الملقط مستقيمة، مع انحناء خدمة يسمح بفك الطرف دون شد الأسلاك المجاورة. لا تمرر أسلاك الجهد العالي والإشارات في الحزمة نفسها. واترك طرفي السكة في متناول اليد.</p>

<h2>الخطوة 5 &mdash; الاختبار قبل التغذية</h2>
<p>ثلاثة فحوص تُغلق العمل:</p>
<ul>
<li><strong>الاستمرارية:</strong> تحقق من كل دائرة مقابل الجدول، بما في ذلك ربط الأرضي بين الطرف والصندوق.</li>
<li><strong>مقاومة العزل:</strong> قِس عند 500&nbsp;فولت تيار مستمر بين الموصلات الحاملة والأرضي مع فصل الأطراف عن الإلكترونيات الحساسة؛ والقيمة المقبولة عادة لا تقل عن 1&nbsp;ميغا أوم.</li>
<li><strong>الفحص الحراري تحت الحمل:</strong> بعد تشغيل اللوحة بالتيار الاسمي لفترة، امسح مجموعة الأطراف بكاميرا حرارية أو افحص باللمس مع الاحتياطات اللازمة. الطرف الأعلى حرارة بوضوح من جيرانه يعني ربطًا مرتخيًا أو مقاومة تلامس مرتفعة.</li>
</ul>

<h2>الأخطاء الشائعة وكيف تظهر</h2>
<table>
  <thead><tr><th>العراض</th><th>السبب المعتاد</th><th>الإجراء التصحيحي</th></tr></thead>
  <tbody>
    <tr><td><strong>تغيّر لون الطرف أو اسمرار</strong></td><td>برغي مرتخي أو موصل غير مدخل بالكامل</td><td>إعادة التوصيل بطرف مضغوط جديد وفحص الملقط</td></tr>
    <tr><td><strong>إشارة متقطعة في دائرة تحكم</strong></td><td>عزل محتجز داخل الملقط</td><td>إعادة التقشير بالطول الصحيح والتوصيل مجددًا</td></tr>
    <tr><td><strong>انزلاق المجموعة على السكة</strong></td><td>غياب المصادر النهائية</td><td>تركيب مصد عند كل طرف</td></tr>
    <tr><td><strong>سخونة في مجموعة موصولة بقضيب</strong></td><td>حلقة سلك بدل قضيب بالمقاس</td><td>الاستبدال بقضيب الشركة المصنعة</td></tr>
    <tr><td><strong>فشل استمرارية الأرضي في الاختبار</strong></td><td>طرف الحماية غير مربوط بالسكة أو القضيب</td><td>تركيب طرف الحماية الصحيح وربطه بقضيب الصندوق</td></tr>
  </tbody>
</table>

<h2>ما يجب تحديده عند الطلب</h2>
<p>في قائمة الشراء لا يمثل الطرف إلا نصف البند. حدد: نوع الطرف وطريقة الربط، ونطاق المقطع، والمسافة بين الأطراف، واللون، والجهد والتيار الاسميان، إضافة إلى المصادر ولوحات الأطراف والحواجز وقضبان التوصيل وحاملات البطاقات ومقابس الاختبار. اللوحات التي تصل ناقصة الملحقات تتوقف عند التشغيل.</p>
<p>يغطي <a href="/products/terminal-connector">نطاق الأطراف والموصلات</a> لدينا أطراف سكة DIN المعيارية بقضبان تيار نحاسية وملاقط لولبية مع ملحقاتها. وإذا كنت ما تزال تختار بين العائلات، يلخص <a href="/blog/terminal-blocks-connectors-identification-guide">جدول تعريف الأطراف</a> الفئات الشائعة.</p>

<h2>الخلاصة</h2>
<p>لا تعتمد موثوقية التوصيل على سكة DIN على سعر الطرف ولا على ماركة اللوحة، بل على أربع خطوات تُنفذ بانتظام: تقشير دقيق، وضغط دائم للطرف، وربط بالعزم المحدد، وفحص تحت الحمل. تكلّف دقائق لكل لوحة وتتفادى معظم زيارات الضمان.</p>''',
    specs=[
        ('مقطع السكة', 'سكة 35 مم وفق EN 60715 مثبتة من الطرفين'),
        ('تحضير الموصل', 'تقشير بالطول المحدد من المصنع وطرف مضغوط على كل موصل مجدول'),
        ('التحقق من الوصلة', 'اختبار سحب بعد الربط، وموصل واحد لكل ملقط إلا مع طرف مزدوج'),
        ('التوصيل المشترك', 'قضيب توصيل معتمد من المصنع وليس حلقة سلك'),
        ('اختبارات التسليم', 'الاستمرارية، والعزل عند 500 فولت مستمر (1 ميغا أوم على الأقل)، والفحص الحراري تحت الحمل'),
    ],
    faqs=[
        ('ما عزم الربط المناسب لطرف سكة DIN؟',
         'العزم الذي تحدده الشركة المصنعة لذلك الحجم، ويُطبق بمفك عزم. تقع القيم الشائعة للأطراف المعيارية بين 0,4 و1,2 نيوتن·متر، لكن ورقة البيانات هي المرجع لأن تصميم الملقط والبرغي يغيّر المتطلب.'),
        ('هل يمكن إدخال موصلين في ملقط واحد؟',
         'فقط إذا كان الطرف مصممًا لذلك، وبموصلين من المقطع نفسه وطرف مزدوج مناسب. خلط المقاطع في ملقط واحد هو السبب الأكثر شيوعًا لارتخاء الوصلة مع الدورات الحرارية.'),
        ('هل الأطراف المضغوطة إلزامية على الموصل المجدول؟',
         'نعم للعمل الصناعي الموثوق. فبدونها تتفتح الشعيرات تحت ضغط البرغي، وينكسر بعضها، وترتفع مقاومة الوصلة. ولا يُستبدل ذلك بالقصدير لأنه يزحف ويرتخي الربط.'),
        ('هل نحتاج إلى المصادر والحواجز الفاصلة؟',
         'كلاهما. المصادر تمنع انزلاق المجموعة عند إدخال الموصلات، والحواجز تحافظ على مسافة الزحف بين دوائر مختلفة الجهد أو بين مجموعات موصولة وأخرى غير موصولة.'),
    ],
)
