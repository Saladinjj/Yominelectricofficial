"""Apply Pinterest chrome to the 2026-09-30 multilingual scenes.
Generates:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/visuals-2026-09-30/{slug}.png (1080x1350, 4:5 vertical)
"""
import os
from PIL import Image

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
VDIR = os.path.join(BASE, 'media-output', 'visuals-2026-09-30')
os.makedirs(VDIR, exist_ok=True)

src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='smart-metering-infrastructure-what-is-a-data-concentrator-unit',
        scene='media-output/img-munl0i6f-aeae9941.png',
        title='Smart Meter Data Concentrator | Substation AMI DCU Gateway',
        chips=['G3-PLC / RS485 / 4G LTE', 'DLMS / COSEM IEC 62056', 'Up to 1024 Smart Meters']
    ),
    dict(
        slug='feeder-automation-what-is-an-auto-recloser',
        scene='media-output/img-munl206s-feb49503.png',
        title='Automatic Circuit Recloser | 11kV–36kV Vacuum ACR',
        chips=['ANSI 79 Reclosing Sequence', 'Microprocessor FTU Control', 'Up to 20kA Fault Clearance']
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

    # Vertical chrome (4:5 visual)
    scene = Image.open(scene_path).convert('RGB')
    W, H = scene.size
    tw = int(H * 4 / 5)
    left = max(0, (W - tw) // 2)
    crop = scene.crop((left, 0, left + min(tw, W), H))
    cpath = os.path.join(BASE, 'media-output', f'_crop_{slug}.png')
    crop.save(cpath, 'PNG')

    v_chrome_job = dict(scene=cpath, title=job['title'], chips=job['chips'])
    v_img = chrome_vertical(v_chrome_job)
    vis_path = os.path.join(VDIR, f"{slug}.png")
    v_img.save(vis_path, 'PNG', optimize=True)
    print(f"Built images for {slug}: hero.png, hero.webp, card.png, card.webp, and {vis_path}")
