# -*- coding: utf-8 -*-
"""Multilingual content module for 2026-10-21:
1. Cable Terminations: What Is a Bimetallic Cable Lug? (EN, FR, ES, AR)
2. Solar PV Systems: What Is a Solar DC Isolator Switch? (EN, FR, ES, AR)
High-level international B2B electrical engineering guides.
"""

# ==============================================================================
# 1. BIMETALLIC CABLE LUG (EN, FR, ES, AR)
# ==============================================================================

BIMETAL_EN = dict(
    lang='en',
    dir='ltr',
    slug='cable-terminations-what-is-a-bimetallic-cable-lug',
    title='Cable Terminations: What Is a Bimetallic Cable Lug?',
    breadcrumb='Cable Terminations &amp; Bimetallic Lugs',
    read='10 min read',
    alt='Industrial switchgear panel interior showing friction-welded bimetallic cable lugs terminating heavy aluminum cables onto tinned copper busbars',
    desc=('Electrical switchboard assembly, solar PV balance of system, and utility power distribution: What is a bimetallic cable lug? '
          'How friction welding joins high-purity copper palms (Cu ≥ 99.95%) with aluminum barrels (Al ≥ 99.5%), eliminates galvanic corrosion, prevents thermal runaway, '
          'and ensures permanent low contact resistance under IEC 61238-1 Class A and DIN 46267.'),
    model='Model DTL-1 and DTL-2 Series Friction-Welded Bi-Metallic Cable Lugs (Electrolytic Copper Cu ≥ 99.95%, EC Grade Aluminum Al ≥ 99.5%, Pre-Filled with Neutral Antioxidant Grease, Certified IEC 61238-1 Class A)',
    category='Cable Terminations & Bimetallic Lugs / Terminal Connectors & Lugs',
    kw='what is a bimetallic cable lug &middot; bimetallic cable lug &middot; copper aluminum cable lug &middot; bimetal lug &middot; dtl bimetallic lug &middot; galvanic corrosion cable &middot; iec 61238-1',
    specs=[
        ('Palm Material Composition', 'High-conductivity electrolytic forged copper ($Cu \ge 99.95\%$, IACS conductivity $> 100\%$) for low-resistance bolting to copper busbars'),
        ('Barrel Material Composition', 'High-purity electrical grade aluminum ($Al \ge 99.5\%$) designed for compression crimping onto stranded aluminum conductors'),
        ('Metallurgical Joining Technology', 'Solid-state rotary friction welding: Generates molecular inter-diffusion without melting, yielding 100% molecular bonding without brittle intermetallic phases'),
        ('Internal Corrosion Protection', 'Factory pre-filled with neutral zinc-loaded antioxidant contact grease and sealed with a protective plastic end-cap to prevent aluminum oxidation'),
        ('Operating Temperature Rating', 'Continuous operation up to $105^\circ\text{C}$; Short-circuit maximum withstand temperature $250^\circ\text{C}$ without joint failure under IEC 61238-1'),
        ('Electrochemical Voltage Isolation', 'Completely eliminates the $0.78\,\text{V}$ electrochemical potential difference between copper and aluminum inside the electrical contact zone'),
        ('Applicable Conductor Cross-Sections', 'Standard sizes from $16\,\text{mm}^2$ up to $630\,\text{mm}^2$ (AWG 6 to 1000 kcmil) matching metric and imperial cable gauges'),
        ('International Manufacturing Standards', 'Fully certified and tested to IEC 61238-1 Class A (heavy-duty through-fault electrical and mechanical cycling) and DIN 46267 Part 2')
    ],
    faqs=[
        ('What is a bimetallic cable lug and why is it essential in electrical engineering?',
         'A bimetallic cable lug (often designated as Model DTL or bi-metal terminal) is an engineered electrical connector comprising a high-purity '
         'aluminum barrel joined seamlessly via solid-state friction welding to an electrolytic copper palm. '
         'It is mandatory whenever an <strong>aluminum conductor</strong> must be bolted to a <strong>copper busbar, circuit breaker terminal, or transformer stud</strong>. '
         'Directly connecting aluminum wire to copper terminals causes rapid <strong>galvanic corrosion</strong> due to their $0.78\,\text{V}$ electrochemical potential difference, '
         'forming non-conductive aluminum oxide films that increase contact resistance ($R_{\text{contact}}$), overheat, and ignite switchgear fires. '
         'A bimetallic lug keeps the copper-to-aluminum transition hermetically sealed inside the molecular friction weld, completely eliminating galvanic degradation.'),
        ('How does friction welding guarantee zero failure at the copper-aluminum interface?',
         'Friction welding is a solid-state joining process where the aluminum rod is rotated at high speed under immense axial pressure against the stationary copper palm. '
         'Frictional heat plasticizes the interface without melting the metals. When rotation stops, forge pressure forces out surface contaminants and creates '
         'a true <strong>atomic-level crystalline bond</strong> between copper and aluminum atoms. '
         'Because melting is avoided, the formation of brittle intermetallic compounds ($\text{CuAl}_2$) is strictly prevented. '
         'Tensile testing under IEC 61238-1 proves that the friction weld is stronger than the parent aluminum metal—the cable or barrel will yield before the friction weld shears.'),
        ('What is the correct crimping procedure for installing bimetallic cable lugs?',
         'To achieve a certified Class A electrical termination, follow these engineering steps: '
         '<ol>'
         '<li><strong>Cable Stripping:</strong> Strip the cable insulation to the exact depth of the aluminum barrel without nicking the aluminum strands.</li>'
         '<li><strong>Oxide Removal:</strong> Wire-brush the bare aluminum strands immediately prior to insertion to break up any invisible aluminum oxide ($\text{Al}_2\text{O}_3$) layer.</li>'
         '<li><strong>Antioxidant Verification:</strong> Ensure the factory-injected neutral antioxidant grease inside the barrel is retained; do not wipe it out. The grease seals out atmospheric moisture and breaks surface oxides during compression.</li>'
         '<li><strong>Hexagonal Die Compression:</strong> Use calibrated hydraulic crimping tools with standard DIN hexagonal dies. Crimp starting from the palm end and move progressively toward the cable entry, ensuring complete die closure on each bite.</li>'
         '<li><strong>Insulation Sealing:</strong> Install a heavy-wall polyolefin heat-shrink sleeve over the barrel-to-cable transition to provide IP67 environmental moisture protection.</li>'
         '</ol>')
    ],
    cta='Engineering electrical power distribution switchgear, utility transformer connections, or commercial solar balance-of-system infrastructure requiring certified, heavy-duty bimetallic cable lugs? YOMIN manufactures friction-welded copper-aluminum lugs from 16mm² to 630mm² certified under IEC 61238-1 Class A.',
    body='''
<h2>The Critical Role of Bimetallic Connectors in Modern Power Systems</h2>
<p>In electrical power distribution, substation engineering, and renewable energy infrastructure, engineers frequently face an unavoidable material dilemma: while aluminum cables are widely chosen for underground transmission and feeder runs due to their lightweight properties and significant cost savings, switchgear busbars, circuit breaker terminals, and transformer connection studs are almost exclusively manufactured from high-conductivity electrolytic copper.</p>
<p>Attempting to bolt an aluminum cable lug directly to a copper busbar, or crimping a copper lug directly onto an aluminum conductor, creates an immediate engineering catastrophe known as <strong>galvanic corrosion</strong>:</p>
<ul>
  <li><strong>The Galvanic Battery Effect:</strong> Copper and aluminum possess a massive electrochemical potential difference of approximately $0.78\,\text{V}$. In the presence of ambient humidity or industrial atmospheric moisture, a microscopic galvanic cell forms. Aluminum, being the more anodic metal, sacrifices itself and corrodes aggressively.</li>
  <li><strong>Thermal Expansion Differential:</strong> Aluminum expands at approximately $23 \times 10^{-6}/\text{K}$, while copper expands at only $17 \times 10^{-6}/\text{K}$. Thermal cycling during daily peak loads causes mechanical loosening, air ingress, oxidation, elevated contact resistance, and ultimate thermal runaway.</li>
</ul>
<p>The <strong>bimetallic cable lug</strong> completely solves this dilemma through solid-state friction welding, providing an imperishable molecular bridge between copper switchgear and aluminum cables.</p>

<h2>Engineering Anatomy: Friction Welding vs. Mechanical Cladding</h2>
<table>
  <thead>
    <tr>
      <th>Design Characteristic</th>
      <th>YOMIN Friction-Welded Bimetallic Lug (DTL Series)</th>
      <th>Inferior Cladded / Soldered Lugs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Transition Joint Strength</strong></td>
      <td><strong>100% Solid-State Molecular Bond:</strong> Joint tensile strength exceeds the yield strength of the parent aluminum barrel.</td>
      <td>Weak mechanical crimp or brazed joint prone to delamination under electrodynamic short-circuit forces.</td>
    </tr>
    <tr>
      <td><strong>Intermetallic Compound Formation</strong></td>
      <td><strong>Zero Brittle $\text{CuAl}_2$ Phases:</strong> Solid-state process avoids melting temperatures, maintaining ductile crystalline continuity.</td>
      <td>High heat during soldering or brazing generates brittle copper-aluminum alloys that crack under thermal shock.</td>
    </tr>
    <tr>
      <td><strong>Internal Corrosion Protection</strong></td>
      <td>Pre-filled with zinc-loaded antioxidant paste and capped at the factory to block moisture during storage and transit.</td>
      <td>Dry barrel; requires manual on-site paste application that technicians frequently forget.</td>
    </tr>
    <tr>
      <td><strong>Short-Circuit Thermal Endurance</strong></td>
      <td>Tested to withstand $250^\circ\text{C}$ short-circuit conditions under IEC 61238-1 Class A without degradation.</td>
      <td>Solder melts or softens at temperatures above $180^\circ\text{C}$, causing catastrophic terminal detachment.</td>
    </tr>
  </tbody>
</table>
'''
)

BIMETAL_FR = dict(
    lang='fr',
    dir='ltr',
    slug='cable-terminations-what-is-a-bimetallic-cable-lug-fr',
    title='Raccordement de Câbles : Qu\'est-ce qu\'une Cosse Bimétallique Cuivre-Aluminium ?',
    breadcrumb='Raccordement &amp; Cosses Bimétalliques',
    read='10 min de lecture',
    alt='Intérieur d\'armoire électrique industrielle montrant des cosses bimétalliques cuivre-aluminium raccordant des câbles d\'aluminium sur des barres de cuivre',
    desc=('Tableaux électriques industriels, distribution d\'énergie et raccordement solaire : Qu\'est-ce qu\'une cosse bimétallique cuivre-aluminium ? '
          'Soudage par friction de la plage cuivre (Cu ≥ 99,95%) et du fût aluminium (Al ≥ 99,5%), élimination de la corrosion galvanique et certification CEI 61238-1 Classe A.'),
    model='Séries DTL-1 et DTL-2 : Cosses Bimétalliques Cuivre-Aluminium Soudées par Friction (Cuivre Électrolytique Cu ≥ 99,95%, Aluminium Électrique Al ≥ 99,5%, Pré-graissées Antioxydant, Certifiées CEI 61238-1 Classe A)',
    category='Raccordement & Cosses Bimétalliques / Connectique & Cosses Électriques',
    kw='cosse bimetallique &middot; cosse cuivre aluminium &middot; cosse dtl &middot; raccordement cable aluminium &middot; corrosion galvanique cuivre alu &middot; soudage friction cosse &middot; cei 61238-1',
    specs=[
        ('Composition de la Plage de Raccordement', 'Cuivre électrolytique forgé haute conductivité ($Cu \ge 99,95\%$) pour boulonnage direct sur jeux de barres cuivre sans échauffement'),
        ('Composition du Fût de Sertissage', 'Aluminium de qualité électrique haute pureté ($Al \ge 99,5\%$) conçu pour le sertissage hexagonal sur conducteurs aluminium'),
        ('Technologie de Jonction Métallurgique', 'Soudage rotatif par friction à l\'état solide : Interdiffusion atomique parfaite sans fusion, éliminant tout composé intermétallique fragile'),
        ('Protection Interne Contre l\'Oxydation', 'Pré-rempli en usine avec une graisse de contact neutre antioxydante et obturé par un capuchon étanche de protection'),
        ('Tenue en Température de Service', 'Service continu jusqu\'à $105^\circ\text{C}$ ; Tenue thermique de court-circuit jusqu\'à $250^\circ\text{C}$ selon CEI 61238-1'),
        ('Suppression du Risque Électrochimique', 'Isole et neutralise totalement la différence de potentiel de $0,78\,\text{V}$ entre le cuivre et l\'aluminium au point de serrage'),
        ('Sections de Câbles Admissibles', 'Gamme standardisée de $16\,\text{mm}^2$ à $630\,\text{mm}^2$ conforme aux câbles normalisés BT et MT'),
        ('Normes Internationales et Essais', 'Conforme et certifié selon les normes CEI 61238-1 Classe A (cycles thermomécaniques et courts-circuits sévères) et DIN 46267')
    ],
    faqs=[
        ('Qu\'est-ce qu\'une cosse bimétallique et pourquoi est-elle obligatoire ?',
         'Une cosse bimétallique (série DTL) est un raccord électrique composé d\'un fût en aluminium et d\'une plage de contact en cuivre, '
         'soudés par friction rotative. '
         'Elle est indispensable pour raccorder un <strong>câble en aluminium</strong> sur un <strong>jeu de barres ou disjoncteur en cuivre</strong>. '
         'En contact direct, le couple cuivre-aluminium génère une <strong>corrosion galvanique</strong> dévastatrice due à leur différence de potentiel de $0,78\,\text{V}$. '
         'L\'aluminium s\'oxyde, la résistance de contact monte en flèche, et la jonction prend feu. La cosse bimétallique neutralise ce risque en confinant la transition métal-métal dans une soudure moléculaire étanche.')
    ],
    cta='Vous concevez des armoires de distribution électrique, des raccordements de transformateurs ou des parcs solaires nécessitant des cosses bimétalliques cuivre-aluminium certifiées CEI 61238-1 Classe A ? YOMIN fabrique la gamme complète de cosses DTL soudées par friction de 16 à 630 mm².',
    body='''
<h2>La Nécessité Technique des Raccordements Bimétalliques dans les Réseaux Modernes</h2>
<p>Dans la distribution d\'énergie électrique et les réseaux industriels, l\'utilisation de câbles en aluminium s\'est généralisée pour des raisons économiques et de poids. En revanche, les jeux de barres des armoires de distribution et les bornes des disjoncteurs sont presque exclusivement en cuivre électrolytique.</p>
<p>Le raccordement direct d\'un câble d\'aluminium sur du cuivre provoque deux phénomènes destructeurs :</p>
<ul>
  <li><strong>La corrosion galvanique :</strong> L\'aluminium et le cuivre présentent un écart électrochimique de 0,78 V. Avec l\'humidité ambiante, l\'aluminium s\'oxyde rapidement et se désagrège.</li>
  <li><strong>La dilatation thermique différentielle :</strong> L\'aluminium se dilate plus vite que le cuivre, provoquant le desserrage des boulons et des arcs électriques.</li>
</ul>
<p>La <strong>cosse bimétallique</strong> élimine ces défaillances grâce au soudage moléculaire par friction selon la norme <strong>CEI 61238-1 Classe A</strong>.</p>
'''
)

BIMETAL_ES = dict(
    lang='es',
    dir='ltr',
    slug='cable-terminations-what-is-a-bimetallic-cable-lug-es',
    title='Terminaciones de Cables: ¿Qué Es un Terminal Bimetálico Cobre-Aluminio?',
    breadcrumb='Terminaciones &amp; Terminales Bimetálicos',
    read='10 min de lectura',
    alt='Interior de cuadro de distribución industrial mostrando terminales bimetálicos cobre-aluminio conectando cables de aluminio en barras de cobre',
    desc=('Cuadros eléctricos de distribución, plantas solares fotovoltaicas y subestaciones: ¿Qué es un terminal bimetálico (cosse bimetálica)? '
          'Soldadura por fricción de pala de cobre (Cu ≥ 99.95%) y tubo de aluminio (Al ≥ 99.5%), eliminación de corrosión galvánica y ensayos bajo norma IEC 61238-1 Clase A.'),
    model='Series DTL-1 y DTL-2: Terminales Bimetálicos Cobre-Aluminio Soldados por Fricción (Cobre Electrolítico Cu ≥ 99.95%, Aluminio Conductor Al ≥ 99.5%, Pre-rellenos con Grasa Antioxidante, Certificados IEC 61238-1 Clase A)',
    category='Terminaciones & Terminales Bimetálicos / Terminales y Conectores de Cable',
    kw='terminal bimetalico &middot; terminal cobre aluminio &middot; terminal dtl &middot; conexion cable aluminio &middot; corrosion galvanica cobre aluminio &middot; soldadura por friccion &middot; iec 61238-1',
    specs=[
        ('Material de la Pala de Contacto', 'Cobre electrolítico forjado de alta conductividad ($Cu \ge 99.95\%$) para empernado seguro en pletinas de cobre'),
        ('Material del Tubo de Compresión', 'Aluminio de pureza eléctrica ($Al \ge 99.5\%$) calibrado para compresión hexagonal sobre conductores de aluminio'),
        ('Tecnología de Unión Metalúrgica', 'Soldadura rotativa por fricción en estado sólido: Genera unión molecular homogénea sin formación de fases frágiles'),
        ('Protección Interna Antioxidante', 'Pre-relleno en fábrica con pasta de contacto neutra con carga de zinc y precintado con tapón de plástico estanco'),
        ('Rango de Temperatura de Trabajo', 'Servicio continuo hasta $105^\circ\text{C}$ ; Temperatura de cortocircuito admisible hasta $250^\circ\text{C}$ según IEC 61238-1'),
        ('Eliminación del Par Galvánico', 'Aísla e inhibe la diferencia de potencial electroquímico de $0.78\,\text{V}$ entre cobre y aluminio en el punto de apriete'),
        ('Secciones Nominales de Conductor', 'Desde $16\,\text{mm}^2$ hasta $630\,\text{mm}^2$ adaptados a conductores milimétricos y calibres AWG / kcmil'),
        ('Normativas Internacionales de Ensayo', 'Certificado y probado conforme a IEC 61238-1 Clase A (ensayos de ciclado térmico y cortocircuito) y DIN 46267')
    ],
    faqs=[
        ('¿Qué es un terminal bimetálico y por qué es imprescindible en instalaciones eléctricas?',
         'Un terminal bimetálico (serie DTL) es una pieza de conexión compuesta por un tubo de aluminio unido mediante soldadura por fricción '
         'a una pala de cobre electrolítico. '
         'Es indispensable al conectar un <strong>cable de aluminio</strong> sobre una <strong>barra o borne de cobre</strong>. '
         'La unión directa entre cobre y aluminio desata una <strong>corrosión galvánica</strong> acelerada debido a su diferencia de potencial electroquímico de $0.78\,\text{V}$, '
         'provocando aumento de resistencia, sobrecalentamiento e incendios. El terminal bimetálico neutraliza este riesgo con su soldadura molecular estanca.')
    ],
    cta='¿Diseña cuadros eléctricos, centros de transformación o plantas solares que requieren terminales bimetálicos cobre-aluminio certificados bajo norma IEC 61238-1 Clase A? YOMIN fabrica la gama DTL soldada por fricción de 16 a 630 mm².',
    body='''
<h2>La Solución Técnica Definitiva para Conexiones de Aluminio y Cobre</h2>
<p>En la ingeniería eléctrica moderna, el uso de cables de aluminio para transporte subterráneo y acometidas principales es el estándar por su ligereza y rentabilidad. No obstante, las barras colectoras de los cuadros de distribución y los interruptores son invariablemente de cobre electrolítico.</p>
<p>El contacto directo entre aluminio y cobre produce dos fallos graves :</p>
<ul>
  <li><strong>Corrosión galvánica :</strong> La diferencia de potencial de 0.78 V oxida rápidamente el aluminio en presencia de humedad.</li>
  <li><strong>Diferencia de dilatación térmica :</strong> El aluminio se dilata un 35% más que el cobre, aflojando tornillos y generando falsos contactos.</li>
</ul>
<p>El <strong>terminal bimetálico soldado por fricción</strong> resuelve de forma permanente este problema cumpliendo la norma <strong>IEC 61238-1 Clase A</strong>.</p>
'''
)

BIMETAL_AR = dict(
    lang='ar',
    dir='rtl',
    slug='cable-terminations-what-is-a-bimetallic-cable-lug-ar',
    title='نهايات وتوصيل الكابلات: ما هي كابل لوج ثنائية المعدن (Bimetallic Cable Lug)؟',
    breadcrumb='نهايات الكابلات &amp; كابل لوج ثنائية المعدن',
    read='10 دقائق قراءة',
    alt='لوحة توزيع قواطع كهربائية صناعية توضح تركيب كابل لوج ثنائية المعدن نحاس ألومنيوم تربط كابلات ألومنيوم على قضبان نحاسية',
    desc=('لوحات التوزيع الكهربائية، ومحطات الطاقة الشمسية، وشبكات نقل القدرة: ما هي كابل لوج ثنائية المعدن نحاس ألومنيوم (Bimetallic Cable Lug)؟ '
          'كيف يمنع اللحام بالاحتكاك التآكل الكلفاني وارتفاع درجات الحرارة بين كابلات الألومنيوم وقضبان النحاس وفقاً للمواصفة القياسية الدولية IEC 61238-1 الفئة A.'),
    model='سلاسل DTL-1 و DTL-2: كابل لوج ثنائية المعدن نحاس ألومنيوم مصنعة باللحام الاحتكاكي (نحاس كهرلي نقي 99.95%، ألومنيوم نقي 99.5%، معبأة بشحم مضاد للأكسدة، معتمدة IEC 61238-1 Class A)',
    category='نهايات الكابلات & كابل لوج ثنائية المعدن / موصلات ونهايات الكابلات الكهربائية',
    kw='كابل لوج ثنائية المعدن &middot; bimetallic cable lug &middot; كابل لوج نحاس الومنيوم &middot; dtl bimetal lug &middot; التآكل الجلفاني للكابلات &middot; لحام الاحتكاك &middot; iec 61238-1',
    specs=[
        ('مادة كف التوصيل النحاسي', 'نحاس كهرلي نقي عالي التوصيل ($Cu \ge 99.95\%$) للتثبيت بالمسامير مباشرة على قضبان التوزيع النحاسية دون حرارة'),
        ('مادة أنبوب الكبس الألومنيوم', 'ألومنيوم نقي مخصص للأغراض الكهربائية ($Al \ge 99.5\%$) للكبس السداسي المحكم على موصلات الألومنيوم'),
        ('تكنولوجيا اللحام الميتالورجي', 'اللحام بالاحتكاك الدوراني في الحالة الصلبة: اندماج ذري كامل بين النحاس والألومنيوم يمنع تكوّن المركبات الهشة'),
        ('الحماية الداخلية من الأكسدة', 'معبأة مسبقاً في المصنع بشحم تلامس محايد محمل بالزنك ومغلقة بغطاء بلاستيكي لمنع تكوّن طبقة أكسيد الألومنيوم العازلة'),
        ('درجة حرارة التشغيل المقننة', 'تشغيل مستمر حتى $105^\circ\text{C}$؛ وتحمل تيار القصر المفاجئ حتى $250^\circ\text{C}$ وفقاً لمعيار IEC 61238-1'),
        ('منع التآكل الكلفاني الكهربائي', 'عزل تام لفرق الجهد الكهروكيميائي البالغ $0.78\,\text{V}$ بين النحاس والألومنيوم داخل منطقة اللحام الذري المحكمة'),
        ('المقاطع الاسمية المتوفرة', 'مقاسات قياسية من $16\,\text{mm}^2$ حتى $630\,\text{mm}^2$ متوافقة مع الكابلات المترية والقياسات الدولية'),
        ('المواصفات والشهادات الدولية', 'مختبر ومعتمد بالكامل وفق معايير IEC 61238-1 الفئة A لدورات الإجهاد الحراري والميكانيكي ومعيار DIN 46267')
    ],
    faqs=[
        ('ما هي كابل لوج ثنائية المعدن ولماذا تعتبر ضرورية في التوصيلات الكهربائية؟',
         'كابل لوج ثنائية المعدن (طراز DTL) هي وصلة كهربائية متطورة تتكون من أنبوب ألومنيوم مدمج بلحام الاحتكاك مع كف تثبيت من النحاس النقي. '
         'وتعتبر هذه الوصلة إلزامية تماماً عند الحاجة إلى توصيل <strong>كابل ألومنيوم</strong> على <strong>قضيب توزيع نحاسي أو قاطع تيار بنقاط توصيل نحاسية</strong>. '
         'إذا تم توصيل كابل الألومنيوم مباشرة بالنحاس، يحدث تفاعل <strong>تآكل كلفاني سريع</strong> بسبب فرق الجهد الكهروكيميائي البالغ $0.78\,\text{V}$، '
         'مما يؤدي إلى تآكل الألومنيوم وارتفاع مقاومة التلامس واشتعال الحرائق. تقوم اللوج ثنائية المعدن بالقضاء التام على هذه المشكلة بفضل اللحام الذري المحكم.')
    ],
    cta='هل تعمل على تنفيذ مشاريع محطات التحويل الكهربائية، أو لوحات التوزيع الصناعية، أو مزارع الطاقة الشمسية التي تتطلب كابل لوج ثنائية المعدن نحاس ألومنيوم معتمدة وفقاً لـ IEC 61238-1 Class A؟ تصنع يمين (YOMIN) تشكيلة DTL المتطورة بسعات من 16 إلى 630 مم².',
    body='''
<h2>الأهمية الهندسية القصوى لاستخدام الوصلات ثنائية المعدن في شبكات التوزيع الكهربائية</h2>
<p>في شبكات توزيع الطاقة ومشاريع محطات التحويل الكبرى، يفضل المهندسون استخدام كابلات الألومنيوم لخطوط التغذية الرئيسية تحت الأرض نظراً لوزنها الخفيف وتكلفتها الاقتصادية الممتازة. وفي المقابل، تصنع قضبان التوزيع داخل لوحات القواطع ونقاط ربط المحولات من النحاس الكهرلي عالي النقاوة والتوصيل.</p>
<p>ويؤدي ربط موصلات الألومنيوم مباشرة بالنحاس إلى حدوث كارثتين هندسيتين في منظومة التوزيع:</p>
<ul>
  <li><strong>التآكل الكلفاني الكهروكيميائي:</strong> يشكل النحاس والألومنيوم في وجود الرطوبة الجوية خلية جلفانية بفرق جهد كهروكيميائي قدره 0.78 فولت، مما يؤدي إلى تآكل معدن الألومنيوم وتفتته سريعاً.</li>
  <li><strong>اختلاف التمدد الحراري:</strong> يتمدد الألومنيوم بمعدل يفوق النحاس بأكثر من 35%، مما يسبب ارتخاء المسامير وتولّد شرر كهربائي خطير واحتراق لوحة التوزيع بالكامل.</li>
</ul>
<p>تمثل <strong>كابل لوج ثنائية المعدن المصنعة باللحام الاحتكاكي</strong> الحل الهندسي الجذري والدائم لهذه المشكلة، حيث تضمن توصيلاً آمناً طويل الأمد طبقاً للمواصفة القياسية الدولية <strong>IEC 61238-1 Class A</strong>.</p>

<h2>مزايا اللحام بالاحتكاك في كابل لوج ثنائية المعدن من يمين (YOMIN)</h2>
<p>يتميز اللحام بالاحتكاك الدوراني في الحالة الصلبة بتوليد اندماج ذري مباشر بين بلورات النحاس والألومنيوم تحت ضغط محوري هائل دون الوصول إلى درجة الانصهار. هذا الأسلوب يمنع منعاً باتاً تكوّن السبائك الهشة التي تتشقق أثناء تيار القصر، مما يمنح وصلة اللحام قوة ميكانيكية فائقة تفوق قوة معدن الألومنيوم الأصلي.</p>
'''
)

# ==============================================================================
# 2. SOLAR DC ISOLATOR SWITCH (EN, FR, ES, AR)
# ==============================================================================

SOLAR_ISO_EN = dict(
    lang='en',
    dir='ltr',
    slug='solar-pv-systems-what-is-a-solar-dc-isolator-switch',
    title='Solar PV Systems: What Is a Solar DC Isolator Switch?',
    breadcrumb='Solar PV Systems &amp; Solar DC Isolators',
    read='10 min read',
    alt='Exterior commercial building wall showing an IP66 outdoor waterproof rotary solar DC isolator switch mounted adjacent to a solar string inverter',
    desc=('Solar photovoltaic power systems, rooftop commercial solar installations, and balance of system electrical safety: What is a solar DC isolator switch? '
          'Why direct current arcs do not self-extinguish without a zero-crossing point, how rotary knife contacts and magnetic blowout chambers quench 1000V/1500V DC arcs in under 3ms, '
          'and mandatory compliance with IEC 60947-3 (DC-PV2) and NEC 690.'),
    model='Model ELR1 & SIS-32 Series 1000V/1500V DC 16A–32A 2-Pole & 4-Pole Outdoor Waterproof Rotary Solar DC Isolator Switches (IP66 UV-Resistant Enclosure, Class DC-PV2, Magnetic Arc Blowout, IEC 60947-3 Compliant)',
    category='Solar PV Systems & Solar DC Isolators / Solar PV Products & DC Protection',
    kw='what is a solar dc isolator switch &middot; solar dc isolator switch &middot; pv isolator switch &middot; dc isolator switch for solar &middot; solar dc disconnect switch &middot; iec 60947-3 dc-pv2 &middot; rooftop solar safety',
    specs=[
        ('Rated Operational Voltage ($U_e$)', 'Standard ratings of $1000\,\text{V DC}$ and $1500\,\text{V DC}$ specifically engineered for string inverters and utility solar arrays'),
        ('Rated Operational Current ($I_e$)', 'Continuous load-break currents of $16\,\text{A}$, $25\,\text{A}$, and $32\,\text{A}$ per pole; parallel wiring configurations up to $50\,\text{A}$'),
        ('Utilization Category Standard', 'Classified as **DC-PV2** under IEC 60947-3 (highest safety rating for connecting and disconnecting photovoltaic circuits under full electrical load)'),
        ('Arc Extinguishment Mechanism', 'Rotary double-break knife contacts with patented internal permanent magnet arc blowout chambers; extinguishes DC arcs in under $3\,\text{milliseconds}$'),
        ('Environmental Enclosure Protection', 'Heavy-duty UV-stabilized polycarbonate enclosure rated **IP66** water-jet proof with silicone sealing gaskets for harsh outdoor desert & coastal climates'),
        ('Safety Lockout Mechanism', 'Ergonomic high-visibility red/yellow rotary handle equipped with an integrated padlockable lockout hole in the OFF position for maintenance safety'),
        ('Cable Entry Connection Ports', 'Equipped with M20 / M25 IP68 compression cable glands or factory pre-wired genuine MC4 solar connectors for rapid installation'),
        ('International Manufacturing Standards', 'Fully certified to IEC 60947-3, AS/NZS 5033, UL 508I, and NEC Article 690 solar disconnect requirements')
    ],
    faqs=[
        ('What is a solar DC isolator switch and why can\'t you use a standard AC switch for solar panels?',
         'A solar DC isolator switch is a specially engineered load-break switch installed between the photovoltaic solar panels and the inverter '
         'to manually disconnect direct current power. '
         '<strong>You can NEVER use a standard AC switch for solar DC circuits:</strong> '
         '<ul>'
         '<li><strong>Alternating Current (AC):</strong> Crosses zero voltage 100 or 120 times every second (50Hz or 60Hz), naturally extinguishing electrical arcs as contacts open.</li>'
         '<li><strong>Direct Current (DC):</strong> Maintains a constant continuous voltage without any zero-crossing point. When contacts open under 1000V DC load, '
         'a ferocious continuous plasma arc exceeding $3,000^\circ\text{C}$ forms. In an AC switch, this arc bridges the open contacts, melts the plastic housing, '
         'and causes catastrophic rooftop fires!</li>'
         '</ul>'
         'A true solar DC isolator utilizes spring-loaded snap-action contacts and magnetic arc blowout chambers to stretch, cool, and extinguish DC arcs within milliseconds.'),
        ('Where should a solar DC isolator switch be located in a photovoltaic installation?',
         'According to international solar installation codes (such as IEC 60364-7-712 and NEC 690), DC isolation must be provided at two strategic locations: '
         '<ol>'
         '<li><strong>Adjacent to the Inverter:</strong> An isolator must be located within 1 to 2 meters of the inverter, within line of sight, '
         'allowing technicians to completely de-energize the DC input before opening the inverter for maintenance.</li>'
         '<li><strong>Near the Solar Array (Rooftop):</strong> In commercial and multi-string installations, a rooftop DC isolator allows firefighters '
         'and emergency crews to isolate the high-voltage DC conductors entering the building envelope, eliminating electrocution hazards during rooftop emergencies.</li>'
         '</ol>'),
        ('What does the IEC 60947-3 DC-PV2 utilization category signify?',
         'IEC 60947-3 defines specific utilization categories for low-voltage switchgear. In solar photovoltaic applications: '
         '<ul>'
         '<li><strong>DC-PV1:</strong> Rated for non-frequent switching of pure resistive or slightly inductive solar circuits under limited load.</li>'
         '<li><strong>DC-PV2:</strong> The highest, most rigorous international classification. It certifies that the switch is capable of repeatedly breaking '
         'and making full operational photovoltaic currents at maximum rated voltage (up to 1500V DC) during severe over-current and fault conditions without contact welding or enclosure rupture.</li>'
         '</ul>'
         'Always ensure your solar switch is certified to DC-PV2 for absolute balance-of-system safety.')
    ],
    cta='Designing rooftop commercial solar systems, utility-scale photovoltaic farms, or residential solar installations requiring certified 1000V/1500V IP66 DC isolator switches compliant with IEC 60947-3 DC-PV2? YOMIN manufactures rugged, weatherproof rotary DC disconnectors engineered for maximum firefighter and maintenance safety.',
    body='''
<h2>The Critical Role of Solar DC Isolator Switches in Photovoltaic Safety</h2>
<p>In modern solar photovoltaic (PV) power systems, solar panels silently convert solar irradiance into high-voltage direct current (DC). Unlike conventional alternating current (AC) power grids, solar modules cannot simply be turned "off" with a wall switch—as long as sunlight strikes the photovoltaic cells, live DC voltage up to 1000V or 1500V remains present on the solar string conductors.</p>
<p>To safely install, inspect, service, or decommission a solar string inverter—and to protect emergency firefighters during a building blaze—the electrical system mandates a dedicated <strong>Solar DC Isolator Switch</strong>.</p>

<h2>The Physics of DC Arcing vs. AC Switching</h2>
<p>The primary reason standard electrical switches fail catastrophically on solar arrays lies in the fundamental physics of electric arcs:</p>
<ul>
  <li><strong>AC Zero-Crossing Arc Extinction:</strong> In an alternating current circuit, the voltage wave naturally drops to zero volts twice per cycle (100 times per second in a 50Hz grid). When switch contacts part, the arc automatically extinguishes at the next zero crossing.</li>
  <li><strong>The Continuous DC Arc Hazard:</strong> Direct current has no natural zero crossing. When contacts open under 1000V DC load, an electric plasma arc forms instantly across the contact air gap. Reaching temperatures over $3000^\circ\text{C}$, a sustained DC arc acts like an electric welding torch, vaporizing metal terminals and igniting surrounding building materials unless aggressively quenched.</li>
</ul>

<h2>Engineered DC Arc Suppression Mechanisms</h2>
<p>YOMIN\'s ELR1 and SIS-32 series solar DC isolators incorporate advanced multi-stage arc extinguishing architectures:</p>
<ol>
  <li><strong>Rotary Knife Double-Break Contacts:</strong> Each pole utilizes two stationary contact points and a rotating copper blade that breaks the circuit at two separate points simultaneously, halving the arc voltage per gap.</li>
  <li><strong>Spring-Loaded Snap-Action Mechanism:</strong> The internal contact speed is completely independent of the operator\'s handle turning speed. Once the spring trip point is passed, the contacts snap open at high velocity ($< 3\,\text{ms}$), rapidly stretching the arc beyond its breakdown threshold.</li>
  <li><strong>Magnetic Arc Blowout Chambers:</strong> Powerful internal permanent magnets create a perpendicular magnetic field that deflects the ionizing arc into de-ionizing splitter plates, rapidly cooling and extinguishing the arc before contact damage occurs.</li>
</ol>
'''
)

SOLAR_ISO_FR = dict(
    lang='fr',
    dir='ltr',
    slug='solar-pv-systems-what-is-a-solar-dc-isolator-switch-fr',
    title='Systèmes Solaires Photovoltaïques : Qu\'est-ce qu\'un Sectionneur DC Solaire ?',
    breadcrumb='Solaire Photovoltaïque &amp; Sectionneurs DC',
    read='10 min de lecture',
    alt='Façade d\'un bâtiment industriel montrant un sectionneur DC solaire étanche rotatif IP66 installé à proximité d\'un onduleur solaire',
    desc=('Installations solaires photovoltaïques en toiture, sécurité électrique et parcs solaires : Qu\'est-ce qu\'un sectionneur DC solaire ? '
          'Pourquoi les arcs en courant continu ne s\'éteignent pas sans passage par zéro, coupure ultra-rapide (<3ms) sous 1000V/1500V et conformité CEI 60947-3 DC-PV2.'),
    model='Séries ELR1 et SIS-32 : Sectionneurs DC Solaires Rotatifs Étanche Extérieur 1000V/1500V 16A–32A (Coffret IP66 Anti-UV, Catégorie DC-PV2, Soufflage Magnétique d\'Arc, Conforme CEI 60947-3)',
    category='Solaire Photovoltaïque & Sectionneurs DC / Produits Solaires PV & Protection DC',
    kw='sectionneur dc solaire &middot; interrupteur sectionneur photovoltaique &middot; coupure dc solaire 1000v &middot; arc electrique courant continu &middot; coffret ip66 solaire &middot; cei 60947-3 dc-pv2',
    specs=[
        ('Tension Assignée d\'Emploi ($U_e$)', 'Tensions normalisées de $1000\,\text{V DC}$ et $1500\,\text{V DC}$ adaptées aux onduleurs de chaînes photovoltaïques'),
        ('Courant Assigné d\'Emploi ($I_e$)', 'Calibres de coupure en charge de $16\,\text{A}$, $25\,\text{A}$ et $32\,\text{A}$ par pôle (jusqu\'à $50\,\text{A}$ en couplage parallèle)'),
        ('Catégorie d\'Emploi Normalisée', 'Classé **DC-PV2** selon la norme CEI 60947-3 (le niveau de sécurité le plus élevé pour la coupure en charge des circuits PV)'),
        ('Dispositif d\'Extinction d\'Arc', 'Contacts rotatifs à double coupure avec chambres de soufflage magnétique éteignant les arcs DC en moins de $3\,\text{millisecondes}$'),
        ('Indice de Protection Environnementale', 'Boîtier étanche en polycarbonate traité anti-UV certifié **IP66** résistant aux intempéries extrêmes et embruns'),
        ('Système de Sécurité et Cadenassage', 'Poignée rotative ergonomique rouge/jaune cadenassable en position OUVERTE (OFF) pour la consignation des techniciens'),
        ('Raccordements et Presse-étoupes', 'Équipé d\'entrées M20/M25 avec presse-étoupes IP68 étanches ou connecteurs solaires MC4 pré-câblés'),
        ('Normes Internationales de Sécurité', 'Entièrement certifié CEI 60947-3, NFC 15-712-1, AS/NZS 5033 et exigences UTE C15-712')
    ],
    faqs=[
        ('Pourquoi ne peut-on jamais utiliser un disjoncteur ou interrupteur AC sur du courant continu solaire ?',
         'Le courant alternatif (AC) s\'annule naturellement 100 fois par seconde (50 Hz), ce qui permet à l\'arc électrique de s\'éteindre de lui-même à chaque passage par zéro. '
         'Le courant continu (DC) solaire ne s\'annule jamais. Lors de l\'ouverture des contacts sous 1000V DC, il se crée un <strong>arc plasma continu à plus de 3000°C</strong> '
         'qui vaporise les contacts d\'un interrupteur AC ordinaire et provoque un incendie immédiat en toiture. '
         'Un sectionneur DC solaire spécifique utilise un mécanisme à déclenchement brusque et des aimants de soufflage pour rompre l\'arc en moins de 3 millisecondes.')
    ],
    cta='Vous concevez des centrales solaires au sol, des ombrières ou des toitures photovoltaïques nécessitant des sectionneurs DC étanches 1000V/1500V certifiés CEI 60947-3 DC-PV2 ? YOMIN fabrique des sectionneurs rotatifs ultra-sécurisés pour onduleurs solaires.',
    body='''
<h2>Le Rôle Fondamental du Sectionneur DC dans la Sécurité Photovoltaïque</h2>
<p>Tant que le soleil éclaire les panneaux photovoltaïques, les chaînes de modules génèrent une tension continue pouvant atteindre 1000V ou 1500V. Il est impossible d\'éteindre un panneau solaire. Pour intervenir en toute sécurité sur l\'onduleur ou permettre l\'intervention des pompiers, l\'installation d\'un <strong>sectionneur DC solaire</strong> est strictement obligatoire.</p>
<p>Ce dossier technique détaille les contraintes physiques de l\'arc électrique en courant continu et les mécanismes de coupure certifiés selon la norme <strong>CEI 60947-3 DC-PV2</strong>.</p>
'''
)

SOLAR_ISO_ES = dict(
    lang='es',
    dir='ltr',
    slug='solar-pv-systems-what-is-a-solar-dc-isolator-switch-es',
    title='Sistemas Solares Fotovoltaicos: ¿Qué Es un Seccionador DC Solar?',
    breadcrumb='Sistemas Solares &amp; Seccionadores DC',
    read='10 min de lectura',
    alt='Pared exterior de edificio mostrando un seccionador rotativo DC solar estanco IP66 instalado junto a un inversor fotovoltaico de string',
    desc=('Sistemas solares fotovoltaicos sobre cubierta, seguridad eléctrica de balance de sistema e inversores solares: ¿Qué es un seccionador DC solar? '
          'Por qué los arcos de corriente continua no se autoextinguen, cámaras de soplado magnético para 1000V/1500V en menos de 3ms y norma IEC 60947-3 DC-PV2.'),
    model='Series ELR1 y SIS-32: Seccionadores DC Solares Rotativos Estancos para Exterior 1000V/1500V 16A–32A (Caja IP66 Resistente a Rayos UV, Categoría DC-PV2, Soplado Magnético de Arco, Conforme a IEC 60947-3)',
    category='Sistemas Solares & Seccionadores DC / Productos Solares PV & Protección DC',
    kw='seccionador dc solar &middot; interruptor seccionador fotovoltaico &middot; desconexion dc solar 1000v &middot; arco electrico corriente continua &middot; caja ip66 solar &middot; iec 60947-3 dc-pv2',
    specs=[
        ('Tensión Asignada de Empleo ($U_e$)', 'Tensiones normalizadas de $1000\,\text{V DC}$ y $1500\,\text{V DC}$ diseñadas para inversores solares y grandes parques'),
        ('Corriente Asignada de Empleo ($I_e$)', 'Capacidad de corte en carga de $16\,\text{A}$, $25\,\text{A}$ y $32\,\text{A}$ por polo (hasta $50\,\text{A}$ en conexionado paralelo)'),
        ('Categoría de Utilización Homologada', 'Clasificado **DC-PV2** bajo IEC 60947-3 (la máxima exigencia para maniobra y corte seguro de circuitos fotovoltaicos en carga)'),
        ('Mecanismo de Extinción de Arco Eléctrico', 'Contactos rotativos de doble ruptura con cámaras de soplado magnético que apagan el arco en menos de $3\,\text{milisegundos}$'),
        ('Protección Envolvente Intemperie', 'Carcasa de policarbonato estabilizado anti-UV con certificación **IP66** estanca contra lluvia torrencial y polvo'),
        ('Bloqueo de Seguridad para Mantenimiento', 'Maneta rotativa roja y amarilla de alta visibilidad con orificio para candado de consignación en posición OFF'),
        ('Prensacables y Conexiones de Entrada', 'Provisto de prensacables estancos M20/M25 con índice IP68 o conectores solares MC4 precableados de fábrica'),
        ('Normativas Internacionales Aplicables', 'Certificado conforme a IEC 60947-3, NEC 690, AS/NZS 5033 y normativas de seguridad de bomberos')
    ],
    faqs=[
        ('¿Por qué no se puede utilizar un interruptor normal de corriente alterna (AC) en paneles solares?',
         'La corriente alterna (AC) cambia de sentido y pasa por cero voltios 100 veces por segundo (a 50Hz), lo que extingue el arco de forma natural. '
         'La corriente continua (DC) de los paneles solares mantiene un voltaje constante sin paso por cero. '
         'Al abrir un interruptor convencional bajo 1000V DC se produce un <strong>arco de plasma continuo a más de 3000°C</strong> '
         'que funde la carcasa plástica y provoca incendios inmediatos en el tejado. Un seccionador solar DC específico '
         'utiliza cuchillas de accionamiento ultrarrápido e imanes de soplado que extinguen el arco en menos de 3 milisegundos.')
    ],
    cta='¿Diseña proyectos solares fotovoltaicos residenciales o plantas industriales que requieren seccionadores DC estancos de 1000V/1500V homologados según IEC 60947-3 DC-PV2? YOMIN fabrica seccionadores rotativos fiables para protección fotovoltaica.',
    body='''
<h2>La Importancia Vital del Seccionador DC en la Seguridad Solar Fotovoltaica</h2>
<p>Mientras haya luz solar sobre los paneles solares, los strings de módulos fotovoltaicos generan alta tensión de corriente continua que no se puede apagar con un interruptor común. Para realizar tareas de mantenimiento en el inversor o salvaguardar la vida de los bomberos en caso de emergencia, el uso de un <strong>seccionador DC solar</strong> es preceptivo.</p>
<p>Este artículo analiza la física del arco eléctrico de corriente continua y las características de los seccionadores certificados bajo la categoría <strong>DC-PV2 de la norma IEC 60947-3</strong>.</p>
'''
)

SOLAR_ISO_AR = dict(
    lang='ar',
    dir='rtl',
    slug='solar-pv-systems-what-is-a-solar-dc-isolator-switch-ar',
    title='أنظمة الطاقة الشمسية الكهروضوئية: ما هو قاطع العزل للتيار المستمر (Solar DC Isolator Switch)؟',
    breadcrumb='الطاقة الشمسية الكهروضوئية &amp; قواطع عزل التيار المستمر',
    read='10 دقائق قراءة',
    alt='واجهة مبنى تجاري توضح قاطع عزل التيار المستمر للطاقة الشمسية المقاوم للماء IP66 مثبت بجوار عاكس الطاقة الشمسية',
    desc=('أنظمة الطاقة الشمسية على أسطح المباني والمشاريع الكهروضوئية التجارية: ما هو قاطع العزل للتيار المستمر (Solar DC Isolator Switch)؟ '
          'لماذا لا ينطفئ القوس الكهربائي للتيار المستمر تلقائياً، وكيف تعمل غرف إخماد القوس المغناطيسي تحت جهود 1000V/1500V في أقل من 3 مللي ثانية وفقاً لـ IEC 60947-3 DC-PV2.'),
    model='سلاسل ELR1 و SIS-32: قواطع عزل التيار المستمر الدوارة المقاومة للماء 1000V/1500V 16A–32A (صندوق حماية IP66 مقاوم للأشعة فوق البنفسجية، فئة DC-PV2، إخماد مغناطيسي للقوس، معتمدة IEC 60947-3)',
    category='الطاقة الشمسية الكهروضوئية & قواطع عزل التيار المستمر / منتجات الطاقة الشمسية وحماية التيار المستمر',
    kw='قاطع عزل التيار المستمر للطاقة الشمسية &middot; solar dc isolator switch &middot; مفتاح عزل الطاقة الشمسية &middot; قوس التيار المستمر &middot; صندوق مقاوم للماء ip66 &middot; iec 60947-3 dc-pv2',
    specs=[
        ('جهد التشغيل المقنن ($U_e$)', 'جهود قياسية معتمدة $1000\,\text{V DC}$ و $1500\,\text{V DC}$ مصممة خصيصاً لسلاسل الألواح ومحولات الطاقة الشمسية'),
        ('تيار التشغيل الاسمي المقنن ($I_e$)', 'سعات قطع الحمل المستمر $16\,\text{A}$ و $25\,\text{A}$ و $32\,\text{A}$ لكل قطب (وحتى $50\,\text{A}$ عند التوصيل على التوازي)'),
        ('فئة الاستخدام القياسية المعتمدة', 'مصنف كفئة **DC-PV2** وفقاً لمعيار IEC 60947-3 (أعلى تصنيف أمان عالمي لقطع وتوصيل الدوائر الكهروضوئية تحت كامل الحمل)'),
        ('آلية إخماد القوس الكهربائي المستمر', 'ملامسات سكين دوارة مزدوجة القطع مع غرف إخماد مغناطيسية تطفئ القوس الكهربائي المستمر في أقل من $3\,\text{مللي ثانية}$'),
        ('مستوى الحماية البيئية للصندوق', 'صندوق متين من مادة البولي كربونات المقاومة للأشعة فوق البنفسجية معتمد بمعيار **IP66** ضد تدفق المياه والأتربة الصحراوية'),
        ('آلية الإغلاق والأمان للصيانة', 'مقبض دوار عالي الوضوح باللونين الأحمر والأصفر مزود بفتحة قفل مدمجة في وضعية الفصل (OFF) لضمان سلامة الفنيين'),
        ('مداخل ومخارج كابلات الطاقة الشمسية', 'مزود بمداخل كابلات M20/M25 وجلب مانعة لتسرب المياه IP68 أو وصلات طاقة شمسية MC4 قياسية مسبقة التوصيل'),
        ('المواصفات القياسية الدولية', 'معتمد ومختبر بالكامل وفق معايير IEC 60947-3 و NEC 690 و AS/NZS 5033 واشتراطات هيئات الدفاع المدني')
    ],
    faqs=[
        ('ما هو قاطع عزل التيار المستمر ولماذا لا يمكن استخدام قاطع تيار متردد عادي مع الألواح الشمسية؟',
         'قاطع عزل التيار المستمر (Solar DC Isolator) هو جهاز فصل كهربائي ميكانيكي يتم تركيبه بين الألواح الشمسية ومحول التيار (Inverter) '
         'لفصل التيار المستمر يدوياً عند الصيانة أو الطوارئ. '
         '<strong>لا يمكن إطلاقاً استخدام قاطع تيار متردد (AC) عادي مع الألواح الشمسية:</strong> '
         '<ul>'
         '<li><strong>التيار المتردد (AC):</strong> ينخفض الجهد إلى الصفر 100 مرة في الثانية (عند تردد 50 هرتز)، مما يساعد على انطفاء القوس الكهربائي تلقائياً عند فتح القاطع.</li>'
         '<li><strong>التيار المستمر (DC):</strong> يحتفظ بجهد ثابت مستمر دون أي نقطة عبور للصفر. عند فتح الملامسات تحت جهد 1000 فولت، '
         'يتولد <strong>قوس كهربائي بلازمي مستمر تتجاوز حرارته 3000 درجة مئوية</strong>، مما يؤدي إلى صهر القاطع العادي واشتعال الحرائق فوق أسطح المباني!</li>'
         '</ul>'
         'يستخدم قاطع التيار المستمر المخصص ملامسات سريعة الارتداد ومغانط إخماد توجه القوس الكهربائي وتطفئه في أقل من 3 مللي ثانية بأمان تام.')
    ],
    cta='هل تعمل على تصميم وتركيب محطات الطاقة الشمسية على أسطح المصانع والمباني التجارية التي تتطلب قواطع عزل تيار مستمر 1000V/1500V بمعيار IP66 ومطابقة للمواصفة IEC 60947-3 DC-PV2؟ تصنع يمين (YOMIN) قواطع عزل دوارة متطورة تضمن أعلى درجات السلامة لمنظومات الطاقة المتجددة.',
    body='''
<h2>الأهمية الحيوية لقواطع عزل التيار المستمر في منظومات الطاقة الشمسية الكهروضوئية</h2>
<p>في محطات الطاقة الشمسية الكهروضوئية، تقوم الألواح الشمسية بتحويل الإشعاع الشمسي مباشرة إلى تيار كهربائي مستمر بجهود عالية تصل إلى 1000 أو 1500 فولت. ولا يمكن إيقاف الألواح الشمسية عن توليد الكهرباء طالما سقط عليها ضوء النهار، مما يعني بقاء الكابلات حاملة لجهود كهربائية قاتلة على مدار ساعات النهار.</p>
<p>لذلك، تفرض الأكواد والمواصفات الكهربائية العالمية تركيب <strong>قاطع عزل التيار المستمر (Solar DC Isolator Switch)</strong> لفصل سلاسل الألواح عن العاكس بأمان تام أثناء أعمال الصيانة الدورية أو في حالات الطوارئ ومكافحة الحرائق.</p>

<h2>فيزياء القوس الكهربائي المستمر وآليات الإخماد المتقدمة</h2>
<p>يكمن الخطر الأكبر في التيار المستمر في عدم وجود نقطة عبور للصفر، مما يجعل القوس الكهربائي مستمراً ومدمراً. تعتمد قواطع التيار المستمر من يمين (YOMIN) على تكنولوجيا إخماد ثلاثية الأبعاد:</p>
<ol>
  <li><strong>ملامسات سكين دوارة مزدوجة القطع:</strong> تقوم بكسر الدائرة في نقطتين منفصلتين في نفس اللحظة، مما يقسم جهد القوس الكهربائي إلى النصف.</li>
  <li><strong>آلية نابضية سريعة الارتداد:</strong> تنفصل الملامسات بسرعة فائقة مستقلة تماماً عن سرعة يد المشغل، مما يقطع القوس في زمن قياسي يقل عن 3 مللي ثانية.</li>
  <li><strong>غرف النفخ المغناطيسي:</strong> تعمل مغانط دائمة قوية على سحب وتشتيت القوس البلازمي نحو صفائح تبريد معدنية متدرجة تطفئه على الفور قبل أن يلحق أي ضرر بالملامسات.</li>
</ol>
'''
)

ALL_MULTILINGUAL_POSTS_1021 = [
    BIMETAL_EN, BIMETAL_FR, BIMETAL_ES, BIMETAL_AR,
    SOLAR_ISO_EN, SOLAR_ISO_FR, SOLAR_ISO_ES, SOLAR_ISO_AR
]
