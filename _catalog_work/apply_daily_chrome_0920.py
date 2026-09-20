"""Apply Pinterest chrome to the 2026-09-20 realistic on-site in-use images.
Generates:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/linkedin-2026-09-20/{slug}.png (1080x1350, 4:5 vertical)
"""
import os
from PIL import Image

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
LIDIR = os.path.join(BASE, 'media-output', 'linkedin-2026-09-20')
os.makedirs(LIDIR, exist_ok=True)

# Load chrome functions from gen_pinterest_style.py
src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='mechanical-lug-guide',
        scene='media-output/img-mu9jjipy-bf2ef8f6.png',
        title='Mechanical Cable Lug | Dual-Rated Solderless Connector',
        chips=['Al9CU Dual Rated 600V', 'Hex Screw Clamp Termination', 'No Crimp Tool Required']
    ),
    dict(
        slug='test-terminal-block-guide',
        scene='media-output/img-mu9jkjv1-8d862980.png',
        title='Test Terminal Block | CT & PT Secondary Disconnect',
        chips=['3-Phase 4-Wire Meter Testing', 'Safe CT Current Shorting', 'Clear Polycarbonate Cover']
    ),
    dict(
        slug='central-battery-system-guide',
        scene='media-output/img-mu9jlt5s-ae786723.png',
        title='Central Battery System | Emergency Lighting EPS Cabinet',
        chips=['Centralized Power Backup', 'EN 50171 & NFPA 101 Standard', 'Touchscreen Circuit Monitor']
    ),
    dict(
        slug='dc-surge-protector-guide',
        scene='media-output/img-mu9jmsgr-cff149b9.png',
        title='DC Surge Protective Device | 1000V Solar PV SPD',
        chips=['Type 2 / Class II 40kA Protection', 'Pluggable Cartridge Modules', 'DIN Rail Combiner Box Mount']
    ),
]

for job in JOBS:
    slug = job['slug']
    out_dir = os.path.join(BASE, 'assets', 'images', 'blog', slug)
    os.makedirs(out_dir, exist_ok=True)
    scene_path = os.path.join(BASE, job['scene'])

    # Wide chrome (16:9 hero + card)
    chrome_job = dict(scene=scene_path, title=job['title'], chips=job['chips'])
    hero_img = chrome_wide(chrome_job, 1536, 864)
    hero_1280 = hero_img.resize((1280, 720), Image.Resampling.LANCZOS)
    hero_png_path = os.path.join(out_dir, 'hero.png')
    hero_webp_path = os.path.join(out_dir, 'hero.webp')
    hero_1280.save(hero_png_path, 'PNG', optimize=True)
    hero_1280.save(hero_webp_path, 'WEBP', quality=85)

    card_img = hero_img.resize((960, 540), Image.Resampling.LANCZOS)
    card_png_path = os.path.join(out_dir, 'card.png')
    card_webp_path = os.path.join(out_dir, 'card.webp')
    card_img.save(card_png_path, 'PNG', optimize=True)
    card_img.save(card_webp_path, 'WEBP', quality=85)

    # Vertical chrome (4:5 LinkedIn)
    scene = Image.open(scene_path).convert('RGB')
    W, H = scene.size
    tw = int(H * 4 / 5)
    left = max(0, (W - tw) // 2)
    crop = scene.crop((left, 0, left + min(tw, W), H))
    cpath = os.path.join(BASE, 'media-output', f'_li_crop_{slug}.png')
    crop.save(cpath, 'PNG')

    v_chrome_job = dict(scene=cpath, title=job['title'], chips=job['chips'])
    v_img = chrome_vertical(v_chrome_job)
    li_path = os.path.join(LIDIR, f"{slug}.png")
    v_img.save(li_path, 'PNG', optimize=True)
    print(f"Built images for {slug}: hero.png, hero.webp, card.png, card.webp, and {li_path}")
