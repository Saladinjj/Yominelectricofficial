"""Apply Pinterest chrome to the 2026-09-23 realistic on-site in-use images.
Generates:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/linkedin-2026-09-23/{slug}.png (1080x1350, 4:5 vertical)
"""
import os
from PIL import Image

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
LIDIR = os.path.join(BASE, 'media-output', 'linkedin-2026-09-23')
os.makedirs(LIDIR, exist_ok=True)

# Load chrome functions from gen_pinterest_style.py
src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='grounding-busbar-guide',
        scene='media-output/img-mudtpoc8-c0e7ca21.png',
        title='Grounding Busbar | Low-Impedance Earthing Terminal Bar',
        chips=['Solid Electrolytic Copper Bar', 'Multi-Terminal Lug Connections', 'Substation & Switchboard Duty']
    ),
    dict(
        slug='high-voltage-current-transformer-guide',
        scene='media-output/img-mudtqsre-2a2de082.png',
        title='10kV Current Transformer | Outdoor Epoxy Cast HV CT',
        chips=['10kV / 35kV Medium-Voltage', 'Cycloaliphatic Resin Sheds', 'Class 0.2S / 0.5S Metering']
    ),
    dict(
        slug='multifunction-energy-meter-guide',
        scene='media-output/img-mudtrkm3-75c42bd9.png',
        title='Multifunction Energy Meter | 3-Phase Digital Power Analyzer',
        chips=['Real-Time V, A, kW, PF, THD', 'RS485 Modbus RTU Protocol', 'Panel Mount 96x96mm Format']
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
