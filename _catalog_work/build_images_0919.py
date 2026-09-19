"""Build Pinterest-style images for the 2026-09-19 blog production run.
Composites real catalogue products onto authentic project scenes with brand chrome.
Produces:
  * assets/images/blog/{slug}/hero.png + hero.webp (1280x720)
  * assets/images/blog/{slug}/card.png + card.webp (960x540)
  * media-output/linkedin-2026-09-19/{slug}.png (4:5 vertical)
"""
import os
from collections import deque
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BASE = r'C:\Users\Saladin\Desktop\yominelectric-main'
LIDIR = os.path.join(BASE, 'media-output', 'linkedin-2026-09-19')
os.makedirs(LIDIR, exist_ok=True)

# Load chrome functions from gen_pinterest_style.py
src = open(os.path.join(BASE, '_catalog_work', 'gen_pinterest_style.py'), encoding='utf-8').read()
src = src.split("if __name__")[0]
ns = {}
exec(compile(src, 'gen_pinterest_style.py', 'exec'), ns)
chrome_wide, chrome_vertical = ns['chrome_wide'], ns['chrome_vertical']

JOBS = [
    dict(
        slug='fuse-cutout-guide',
        src='assets/images/products/7edc35982a7d50e1.jpg',
        bg='media-output/img-mu83z3v6-603c5acc.png',
        thr=240,
        target_h=480,
        pos_y=270,
        title='J-Type Fuse Cutout | Heavy-Duty Feeder Disconnector',
        chips=['Up to 400A / 415V Rating', '82mm & 92mm Slotted Centers', 'Distribution Pole & LV Duty']
    ),
    dict(
        slug='electric-meter-seal-guide',
        src='assets/images/products/20dd6d59d60cf684.png',
        bg='media-output/img-mu8401a5-b3a713be.png',
        thr=245,
        target_h=490,
        pos_y=260,
        title='Electric Meter Security Seal | Anti-Tamper Revenue Lock',
        chips=['Polycarbonate Twist Body', 'Stainless Steel Sealing Wire', 'Custom Barcode & Serial ID']
    ),
    dict(
        slug='bimetallic-lug-guide',
        src='assets/images/products/17a14fa3e6aae8ea.jpg',
        bg='media-output/img-mu8410nf-cd951465.png',
        thr=240,
        target_h=470,
        pos_y=280,
        title='DTL Bimetallic Cable Lug | Cu-Al Transition Terminal',
        chips=['Friction-Welded Solid Joint', 'Prevents Galvanic Corrosion', 'Heavy Aluminium Cable Duty']
    ),
]

def key_product(src_path, thr=240):
    im = Image.open(os.path.join(BASE, src_path)).convert('RGB')
    arr = np.asarray(im).astype(np.int16)
    nw = (arr[:, :, 0] >= thr) & (arr[:, :, 1] >= thr) & (arr[:, :, 2] >= thr)
    h, w = nw.shape
    bg = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if nw[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if nw[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and nw[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))

    mask = (~bg).astype(np.uint8) * 255
    mask_im = Image.fromarray(mask, mode='L')
    mask_im = mask_im.filter(ImageFilter.BoxBlur(0.8))

    rgba = Image.new('RGBA', (w, h))
    rgba.paste(im, (0, 0))
    rgba.putalpha(mask_im)

    bbox = rgba.getbbox()
    if bbox:
        rgba = rgba.crop(bbox)
    return rgba

for job in JOBS:
    slug = job['slug']
    print(f"Building assets for: {slug}")
    out_dir = os.path.join(BASE, 'assets', 'images', 'blog', slug)
    os.makedirs(out_dir, exist_ok=True)

    cutout = key_product(job['src'], job['thr'])
    bg_wide = Image.open(os.path.join(BASE, job['bg'])).convert('RGBA').resize((1280, 720), Image.Resampling.LANCZOS)

    # Scale cutout proportionally
    cw, ch = cutout.size
    scale = job['target_h'] / float(ch)
    new_w = max(10, int(cw * scale))
    new_h = job['target_h']
    cutout_scaled = cutout.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Center horizontally on wide scene
    paste_x = (1280 - new_w) // 2
    paste_y = job['pos_y']

    # Soft contact shadow
    shadow = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sh_box = [paste_x - 15, paste_y + new_h - 18, paste_x + new_w + 15, paste_y + new_h + 16]
    sdraw.ellipse(sh_box, fill=(15, 20, 25, 130))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))

    wide_scene = Image.alpha_composite(bg_wide, shadow)
    wide_scene.paste(cutout_scaled, (paste_x, paste_y), cutout_scaled)
    scene_path = os.path.join(BASE, 'media-output', f'_scene_{slug}.png')
    wide_scene.convert('RGB').save(scene_path, 'PNG')

    # Apply Pinterest wide chrome
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

    # 4:5 LinkedIn vertical asset (1080x1350)
    bg_vert = Image.open(os.path.join(BASE, job['bg'])).convert('RGBA')
    bw, bh = bg_vert.size
    target_vw = int(bh * 4 / 5)
    left = max(0, (bw - target_vw) // 2)
    bg_vert_cropped = bg_vert.crop((left, 0, left + target_vw, bh)).resize((1080, 1350), Image.Resampling.LANCZOS)

    v_scale = 680 / float(ch)
    v_new_w = max(10, int(cw * v_scale))
    v_new_h = 680
    v_cutout = cutout.resize((v_new_w, v_new_h), Image.Resampling.LANCZOS)
    v_x = (1080 - v_new_w) // 2
    v_y = 420

    v_shadow = Image.new('RGBA', (1080, 1350), (0, 0, 0, 0))
    v_sdraw = ImageDraw.Draw(v_shadow)
    v_sh_box = [v_x - 20, v_y + v_new_h - 22, v_x + v_new_w + 20, v_y + v_new_h + 20]
    v_sdraw.ellipse(v_sh_box, fill=(15, 20, 25, 140))
    v_shadow = v_shadow.filter(ImageFilter.GaussianBlur(18))

    vert_scene = Image.alpha_composite(bg_vert_cropped, v_shadow)
    vert_scene.paste(v_cutout, (v_x, v_y), v_cutout)
    vert_scene_path = os.path.join(BASE, 'media-output', f'_vert_scene_{slug}.png')
    vert_scene.convert('RGB').save(vert_scene_path, 'PNG')

    li_chrome_job = dict(scene=vert_scene_path, title=job['title'], chips=job['chips'])
    li_img = chrome_vertical(li_chrome_job)
    li_png_path = os.path.join(LIDIR, f"{slug}.png")
    li_img.save(li_png_path, 'PNG', optimize=True)
    print(f"  Saved hero: {os.path.getsize(hero_png_path)} bytes, card: {os.path.getsize(card_png_path)} bytes, LI: {os.path.getsize(li_png_path)} bytes")

print("All Phase 3 images generated successfully!")
