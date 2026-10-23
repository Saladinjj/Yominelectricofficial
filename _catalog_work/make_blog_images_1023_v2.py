# -*- coding: utf-8 -*-
"""Photo-led covers (v2) for the 2026-10-23 articles.

Style matches the site's existing photographic covers: full-bleed installation
photograph, white logo chip, headline over a left gradient, blue caption band.
Only authentic assets: real site photography + the YOMIN logo file.
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_WORD = os.path.join(BASE, 'Yomin logo website.png')
FONT_B = r'C:\Windows\Fonts\arialbd.ttf'
FONT_R = r'C:\Windows\Fonts\arial.ttf'

GOLD = (214, 178, 116)
BAND = (22, 45, 78)
WHITE = (255, 255, 255)


def cover_crop(src, size, focus_y=0.5, focus_x=0.5, zoom=1.0):
    """Resize-and-centre-crop src to fill size, honouring focus points and a zoom factor."""
    W, H = size
    im = src.convert('RGB')
    s = max(W / im.width, H / im.height) * zoom
    im = im.resize((max(W, int(im.width * s + 0.5)), max(H, int(im.height * s + 0.5))), Image.LANCZOS)
    left = int((im.width - W) * focus_x)
    top = int((im.height - H) * focus_y)
    return im.crop((left, top, left + W, top + H))


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


def build(size, photo, headline, kicker, subline, out_dir, name, focus_y=0.5, focus_x=0.5, zoom=1.0):
    W, H = size
    sc = W / 1536.0
    canvas = cover_crop(Image.open(photo), size, focus_y, focus_x, zoom).convert('RGBA')

    # left gradient for legibility
    grad = Image.new('L', (W, 1), 0)
    gd = ImageDraw.Draw(grad)
    for x in range(W):
        t = x / (W * 0.58)
        gd.point((x, 0), int(246 * max(0.0, 1 - t) ** 1.30))
    grad = grad.resize((W, H))
    shade = Image.new('RGBA', (W, H), (6, 10, 16, 255))
    shade.putalpha(grad)
    canvas.alpha_composite(shade)

    # bottom band
    band_h = int(78 * sc)
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, H - band_h, W, H], fill=BAND)

    # logo chip
    pad = int(52 * sc)
    if os.path.exists(LOGO_WORD):
        logo = Image.open(LOGO_WORD).convert('RGBA')
        lh = int(46 * sc)
        lw = int(logo.width * lh / logo.height)
        logo = logo.resize((lw, lh), Image.LANCZOS)
        cw, ch = int(lw + 34 * sc), int(lh + 26 * sc)
        cy = int(38 * sc)
        d.rounded_rectangle([pad, cy, pad + cw, cy + ch], radius=int(10 * sc), fill=(255, 255, 255, 246))
        canvas.alpha_composite(logo, (pad + int(17 * sc), cy + int(13 * sc)))

    f_kick = ImageFont.truetype(FONT_B, int(20 * sc))
    f_head = ImageFont.truetype(FONT_B, int(52 * sc))
    f_sub = ImageFont.truetype(FONT_R, int(24 * sc))

    x = pad
    y = int(236 * sc)
    d.text((x, y), kicker.upper(), font=f_kick, fill=GOLD)

    y += int(42 * sc)
    lines = wrap(d, headline, f_head, int(W * 0.46))
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for i, ln in enumerate(lines):
        sd.text((x, y + i * int(64 * sc)), ln, font=f_head, fill=(0, 0, 0, 190))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(int(7 * sc))))
    d = ImageDraw.Draw(canvas)
    for i, ln in enumerate(lines):
        d.text((x, y + i * int(64 * sc)), ln, font=f_head, fill=WHITE)
    y += len(lines) * int(64 * sc)

    d.rectangle([x, y + int(16 * sc), x + int(92 * sc), y + int(21 * sc)], fill=GOLD)
    y += int(46 * sc)
    for ln in wrap(d, subline, f_sub, int(W * 0.40)):
        d.text((x, y), ln, font=f_sub, fill=(232, 237, 243))
        y += int(32 * sc)

    # bottom band text
    f_band = ImageFont.truetype(FONT_B, int(21 * sc))
    ty = H - band_h + int(28 * sc)
    d.text((pad, ty), 'YOMIN ELECTRIC CO., LTD', font=f_band, fill=WHITE)
    rt = 'WWW.YOMINELECTRIC.COM'
    d.text((W - pad - d.textlength(rt, font=f_band), ty), rt, font=f_band, fill=(206, 216, 228))

    os.makedirs(out_dir, exist_ok=True)
    png = os.path.join(out_dir, name + '.png')
    canvas.convert('RGB').save(png, 'PNG', optimize=True)
    canvas.convert('RGB').save(os.path.join(out_dir, name + '.webp'), 'WEBP', quality=84, method=6)
    print('wrote', png, os.path.getsize(png) // 1024, 'KB')


JOBS = [
    dict(
        slug='din-rail-terminal-block-wiring-how-to',
        photo=os.path.join(BASE, 'assets/images/blog/din-rail-vs-panel-meters/hero.jpg'),
        headline='DIN Rail Terminal Block Wiring',
        kicker='Step-by-step installation',
        subline='Ferrules · torque · jumpers · testing',
        focus_y=0.45, focus_x=0.42, zoom=1.08,
    ),
    dict(
        slug='air-conditioner-voltage-stabilizer-sizing',
        photo=os.path.join(BASE, 'assets/images/blog/blog-voltage-stabilizer-guide/hero.jpg'),
        headline='Voltage Stabilizers for Air Conditioners',
        kicker='Sizing · types · installation',
        subline='Nameplate sizing · relay vs servo · delay',
        focus_y=0.30, focus_x=0.55, zoom=1.02,
    ),
]

for j in JOBS:
    out = os.path.join(BASE, 'assets/images/blog', j['slug'])
    build((1536, 864), j['photo'], j['headline'], j['kicker'], j['subline'], out, 'hero', j['focus_y'], j['focus_x'], j['zoom'])
    build((960, 540), j['photo'], j['headline'], j['kicker'], j['subline'], out, 'card', j['focus_y'], j['focus_x'], j['zoom'])
