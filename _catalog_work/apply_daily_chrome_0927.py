"""Apply Pinterest chrome to the 2026-09-27 on-site scenes.
Generates:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/linkedin-2026-09-27/{slug}.png (1080x1350, 4:5 vertical)
"""
import os
from PIL import Image

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
LIDIR = os.path.join(BASE, 'media-output', 'linkedin-2026-09-27')
os.makedirs(LIDIR, exist_ok=True)

src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='solar-array-cable-connections-what-is-an-mc4-connector',
        scene='media-output/img-muj6l4es-eeb4b1e0.png',
        title='MC4 Solar Connector | Waterproof PV Cable Terminal',
        chips=['1000V / 1500V DC Rating', 'IP68 Waterproof Snap-Lock', 'Tinned Copper Contact Pin']
    ),
    dict(
        slug='commercial-grid-monitoring-what-is-a-smart-energy-meter',
        scene='media-output/img-muj6mcm9-97024686.png',
        title='Smart Energy Meter | 3-Phase Multi-Function Monitor',
        chips=['RS485 Modbus & IoT Ready', 'Bi-Directional Active/Reactive', 'Class 0.5S Precision']
    ),
    dict(
        slug='heavy-duty-power-distribution-what-is-an-industrial-plug-and-socket',
        scene='media-output/img-muj6n9d7-11207c32.png',
        title='CEE Industrial Plug & Socket | Heavy-Duty Power Coupling',
        chips=['16A–125A 3P+N+E 400V', 'IP44 / IP67 Weatherproof', 'IEC 60309 Pin & Sleeve']
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
