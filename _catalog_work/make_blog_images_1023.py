# -*- coding: utf-8 -*-
"""Build hero (1280x720) and card (960x540) images for the 2026-10-23 articles.

Uses only authentic assets: the YOMIN emblem (logo_transparent.png) and real
product photographs from the catalogue. No generated or retouched product shapes.
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, 'logo_transparent.png')
FONT_B = r'C:\Windows\Fonts\arialbd.ttf'
FONT_R = r'C:\Windows\Fonts\arial.ttf'

BG_TOP = (247, 248, 250)
BG_BOT = (228, 232, 238)
INK = (18, 24, 31)
MUTED = (90, 100, 112)
GOLD = (200, 169, 110)
BAND = (23, 46, 78)


def trim_white(im, tol=8):
    im = im.convert('RGB')
    bg = Image.new('RGB', im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.point(lambda p: 255 if p > tol else 0).getbbox()
    return im.crop(bbox) if bbox else im


def gradient(size):
    w, h = size
    g = Image.new('RGB', (1, h))
    d = ImageDraw.Draw(g)
    for y in range(h):
        t = y / max(h - 1, 1)
        d.point((0, y), tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)))
    return g.resize((w, h))


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if draw.textlength(test, font=font) <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build(size, product_path, headline, kicker, out_dir, name):
    W, H = size
    scale = W / 1280.0
    canvas = gradient(size).convert('RGBA')
    d = ImageDraw.Draw(canvas)

    pad = int(64 * scale)
    band_h = int(74 * scale)

    # emblem top-left
    if os.path.exists(LOGO):
        logo = Image.open(LOGO).convert('RGBA')
        lh = int(58 * scale)
        lw = int(logo.width * lh / logo.height)
        logo = logo.resize((lw, lh), Image.LANCZOS)
        canvas.alpha_composite(logo, (pad, int(46 * scale)))

    # kicker
    f_kick = ImageFont.truetype(FONT_B, int(17 * scale))
    d.text((pad, int(134 * scale)), kicker.upper(), font=f_kick, fill=GOLD)

    # headline
    f_head = ImageFont.truetype(FONT_B, int(52 * scale))
    text_w = int(W * 0.50)
    lines = wrap(d, headline, f_head, text_w)
    y = int(168 * scale)
    for ln in lines:
        d.text((pad, y), ln, font=f_head, fill=INK)
        y += int(64 * scale)

    # gold rule under headline
    d.rectangle([pad, y + int(14 * scale), pad + int(96 * scale), y + int(20 * scale)], fill=GOLD)

    # product card on the right
    if os.path.exists(product_path):
        prod = trim_white(Image.open(product_path))
        card_w = int(W * 0.40)
        card_h = int(H * 0.60)
        cx = W - pad - card_w
        cy = int((H - band_h - card_h) / 2) + int(10 * scale)

        shadow = Image.new('RGBA', (card_w + 40, card_h + 40), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        sd.rounded_rectangle([20, 26, card_w + 20, card_h + 20], radius=int(18 * scale), fill=(20, 30, 45, 60))
        shadow = shadow.filter(ImageFilter.GaussianBlur(int(14 * scale)))
        canvas.alpha_composite(shadow, (cx - 20, cy - 20))

        d.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=int(16 * scale),
                            fill=(255, 255, 255, 255), outline=(226, 230, 236, 255), width=max(1, int(scale)))
        inner = int(card_w * 0.86)
        sc = min(inner / prod.width, (card_h * 0.86) / prod.height)
        p = prod.resize((max(1, int(prod.width * sc)), max(1, int(prod.height * sc))), Image.LANCZOS)
        canvas.alpha_composite(p.convert('RGBA'),
                               (cx + (card_w - p.width) // 2, cy + (card_h - p.height) // 2))

    # bottom band
    d.rectangle([0, H - band_h, W, H], fill=BAND)
    f_band = ImageFont.truetype(FONT_B, int(19 * scale))
    d.text((pad, H - band_h + int(26 * scale)), 'YOMIN ELECTRIC CO., LTD', font=f_band, fill=(255, 255, 255))
    right = 'WWW.YOMINELECTRIC.COM'
    d.text((W - pad - d.textlength(right, font=f_band), H - band_h + int(26 * scale)),
           right, font=f_band, fill=(214, 222, 232))

    os.makedirs(out_dir, exist_ok=True)
    png = os.path.join(out_dir, name + '.png')
    canvas.convert('RGB').save(png, 'PNG', optimize=True)
    canvas.convert('RGB').save(os.path.join(out_dir, name + '.webp'), 'WEBP', quality=86, method=6)
    print('wrote', png, canvas.size)


JOBS = [
    dict(
        slug='din-rail-terminal-block-wiring-how-to',
        product=os.path.join(BASE, 'assets/images/products/high-quality-durable-brass-plastic-and-pa-electric-copper-din-rail-terminal-block-with-copper-inlet-outlet.jpg'),
        headline='DIN Rail Terminal Block Wiring',
        kicker='Panel building guide',
    ),
    dict(
        slug='air-conditioner-voltage-stabilizer-sizing',
        product=os.path.join(BASE, 'assets/images/products/cpu-control-relay-type-wps3000va-series-air-conditioning-wall-mount-plastic-panel-power-stabilizer-voltage-regulator-for-home.jpg'),
        headline='Voltage Stabilizers for Air Conditioners',
        kicker='Sizing, types, installation',
    ),
]

for j in JOBS:
    out = os.path.join(BASE, 'assets/images/blog', j['slug'])
    build((1280, 720), j['product'], j['headline'], j['kicker'], out, 'hero')
    build((960, 540), j['product'], j['headline'], j['kicker'], out, 'card')
