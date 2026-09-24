"""Apply Pinterest chrome to the 'What Is' realistic on-site in-use images.
Generates:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/linkedin-what-is/{slug}.png (1080x1350, 4:5 vertical)
"""
import os
from PIL import Image

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
LIDIR = os.path.join(BASE, 'media-output', 'linkedin-what-is')
os.makedirs(LIDIR, exist_ok=True)

# Load chrome functions from gen_pinterest_style.py
src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='what-is-a-voltage-stabilizer',
        scene='media-output/img-muflfpci-e84c4fc6.png',
        title='Automatic Voltage Stabilizer | Constant Voltage Regulation',
        chips=['Servo Motor & Relay Drive', 'Brownout & Surge Protection', 'Single & 3-Phase AC Ratings']
    ),
    dict(
        slug='what-is-a-surge-protective-device',
        scene='media-output/img-mufliabe-40452eea.png',
        title='Surge Protective Device (SPD) | Transient Voltage Suppressor',
        chips=['Type 1, Type 2 & Type 3', 'High-Energy MOV Suppression', 'DIN Rail Panelboard Mount']
    ),
    dict(
        slug='what-is-a-fuse-cutout',
        scene='media-output/img-muflja0d-99db58ef.png',
        title='Distribution Fuse Cutout | Pole-Mounted Transformer Cutout',
        chips=['10kV–35kV Expulsion Drop-Out', 'Transformer Fault Clearance', 'Weatherproof Porcelain Body']
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
