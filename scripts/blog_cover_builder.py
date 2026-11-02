#!/usr/bin/env python3
"""Build YOMIN blog cover images (card + hero) from real brand + product assets.

Design contract
---------------
* Brand: real YOMIN lockup (mark + wordmark), cropped from the existing brand
  banner ``Yomin_LinkedIn_Banner_Final.png`` and saved once as
  ``assets/images/logo-lockup.png``. It is never redrawn, recoloured or
  approximated. ``logo.png`` in the repo root is only 240 px and its wordmark is
  light grey, so it is unusable on the light cover.
* Products: real photos from ``assets/images/products/`` only. Never synthetic
  art, never a stock render posing as a YOMIN product.
* Backdrops are normalised to pure white, then multiply-composited onto the warm
  canvas so studio shots blend with no grey box and no cut-out halo.
* No text is baked in, so one image serves en / fr / es / ar.

Usage
-----
    python scripts/blog_cover_builder.py --slug types-of-busbar \
        --photos <path> [<path> ...]

    python scripts/blog_cover_builder.py --batch scripts/blog_cover_map.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "images" / "logo-lockup.png"
BANNER = ROOT / "temp" / "e072tree" / "Yomin_LinkedIn_Banner_Final.png"

CANVAS = (244, 241, 236)          # warm paper, close to site --bgc2 light
CANVAS_EDGE = (236, 231, 223)
GRID = (226, 220, 210)
ACCENT = (198, 120, 52)           # --ac darkened for contrast on light paper
INK = (26, 26, 26)

CARD = (960, 540)
HERO = (1280, 720)


# --------------------------------------------------------------------------- #
# brand asset
# --------------------------------------------------------------------------- #
def ensure_logo() -> Path:
    """Crop the real lockup out of the brand banner once (source pixels only)."""
    if LOGO.exists():
        return LOGO
    if not BANNER.exists():
        raise SystemExit(f"brand lockup missing and banner not found: {BANNER}")
    im = Image.open(BANNER).convert("RGB")
    arr = np.asarray(im)
    strip = arr[:, int(im.width * 0.65):, :]
    mask = (strip < 235).any(axis=2)
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    x0 = int(im.width * 0.65) + int(cols[0]) - 6
    box = (x0, int(rows[0]) - 6, x0 + int(cols[-1] - cols[0]) + 13,
           int(rows[-1]) + 7)
    LOGO.parent.mkdir(parents=True, exist_ok=True)
    im.crop(box).save(LOGO, "PNG", optimize=True)
    print(f"brand lockup extracted -> {LOGO.relative_to(ROOT)}")
    return LOGO


# --------------------------------------------------------------------------- #
# photo preparation
# --------------------------------------------------------------------------- #
def _trim_uniform(im: Image.Image, tol: int = 14) -> Image.Image:
    arr = np.asarray(im.convert("RGB")).astype(np.int16)
    h, w, _ = arr.shape
    corners = np.array([arr[0, 0], arr[0, w - 1], arr[h - 1, 0], arr[h - 1, w - 1]])
    bg = np.median(corners, axis=0)
    mask = np.abs(arr - bg).max(axis=2) > tol
    if not mask.any():
        return im
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    pad = 4
    return im.crop((
        max(int(cols[0]) - pad, 0),
        max(int(rows[0]) - pad, 0),
        min(int(cols[-1]) + 1 + pad, w),
        min(int(rows[-1]) + 1 + pad, h),
    ))


def _normalise_backdrop(im: Image.Image, pad: int = 26) -> Image.Image:
    """Flatten the studio backdrop to pure white so the photo can be multiplied
    onto the tinted canvas without a visible grey rectangle.

    Studio shots often carry a soft vignette, so a single global scale leaves
    grey patches. We estimate the low-frequency backdrop surface (product masked
    out, then heavily blurred) and divide by it per pixel.
    """
    arr = np.asarray(im.convert("RGB")).astype(np.float32)
    h, w, _ = arr.shape

    corners = np.array([arr[0, 0], arr[0, w - 1], arr[h - 1, 0], arr[h - 1, -1]])
    bg0 = np.clip(np.median(corners, axis=0), 150.0, 255.0)

    lum = arr.mean(axis=2)
    # Product pixels are clearly darker than the backdrop.
    product = lum < float(bg0.mean()) - 18.0

    # Fill product areas with the backdrop colour, then blur to get the surface.
    filled = arr.copy()
    filled[product] = bg0
    radius = max(8, min(h, w) // 12)
    surface = np.asarray(
        Image.fromarray(filled.astype(np.uint8)).filter(
            ImageFilter.GaussianBlur(radius)
        )
    ).astype(np.float32)
    surface = np.clip(surface, 200.0, 255.0)

    corrected = np.clip(arr * (255.0 / surface), 0, 255)
    # Only push backdrop-class pixels to pure white; keep product edges intact.
    backdrop = corrected.mean(axis=2) >= 246
    corrected[backdrop] = 255
    corrected[corrected >= 252] = 255

    out = Image.fromarray(corrected.astype(np.uint8))
    if pad:
        out = ImageOps.expand(out, border=pad, fill=(255, 255, 255))
    return out


def prep_photo(path: Path, box: tuple[int, int]) -> Image.Image | None:
    try:
        im = Image.open(path)
    except Exception as exc:  # noqa: BLE001
        print(f"  ! cannot open {path.name}: {exc}", file=sys.stderr)
        return None
    im = ImageOps.exif_transpose(im).convert("RGB")
    if min(im.size) < 140:
        print(f"  ! too small, skipped: {path.name} ({im.size})", file=sys.stderr)
        return None
    im = _trim_uniform(im)
    im = _normalise_backdrop(im)
    im.thumbnail(box, Image.LANCZOS)
    return im


# --------------------------------------------------------------------------- #
# canvas pieces
# --------------------------------------------------------------------------- #
def _paper(size: tuple[int, int]) -> Image.Image:
    w, h = size
    base = Image.new("RGBA", size, (*CANVAS, 255))

    # faint vignette so the paper is not dead flat
    vig = Image.new("L", size, 0)
    d = ImageDraw.Draw(vig)
    d.ellipse([-w * 0.3, -h * 0.5, w * 1.3, h * 1.5], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(w * 0.12))
    tint = Image.new("RGBA", size, (*CANVAS_EDGE, 255))
    base = Image.composite(base, tint, vig)

    # engineering grid
    grid = Image.new("RGBA", size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    step = max(40, w // 20)
    for x in range(0, w, step):
        gd.line([(x, 0), (x, h)], fill=(*GRID, 120), width=1)
    for y in range(0, h, step):
        gd.line([(0, y), (w, y)], fill=(*GRID, 120), width=1)
    base.alpha_composite(grid)

    # soft accent wash bottom-right
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse(
        [w * 0.45, h * 0.55, w * 1.25, h * 1.45], fill=(*ACCENT, 26)
    )
    glow = glow.filter(ImageFilter.GaussianBlur(w * 0.08))
    base.alpha_composite(glow)
    return base


def _grid_index(canvas: Image.Image) -> int:
    return max(40, canvas.width // 20)


def _multiply_paste(
    canvas: Image.Image, img: Image.Image, xy: tuple[int, int], feather: int = 14
) -> None:
    """Multiply a white-background image onto the canvas so it blends, with a
    feathered edge so the photo's own backdrop never shows a straight seam."""
    x, y = xy
    region = canvas.crop((x, y, x + img.width, y + img.height)).convert("RGB")
    merged = ImageChops.multiply(region, img.convert("RGB"))
    if feather > 0:
        mask = Image.new("L", img.size, 0)
        ImageDraw.Draw(mask).rectangle(
            [feather, feather, img.width - feather, img.height - feather], fill=255
        )
        mask = mask.filter(ImageFilter.GaussianBlur(feather / 2))
        merged = Image.composite(merged, region, mask)
    canvas.paste(merged, (x, y))


def _brand_mark(canvas: Image.Image, height: int, xy: tuple[int, int]) -> None:
    logo = Image.open(LOGO).convert("RGB")
    ratio = height / logo.height
    logo = logo.resize((max(1, int(logo.width * ratio)), height), Image.LANCZOS)
    _multiply_paste(canvas, logo, xy, feather=0)
    # accent hairline under the lockup
    d = ImageDraw.Draw(canvas)
    d.line(
        [(xy[0], xy[1] + height + max(8, height // 6)),
         (xy[0] + int(logo.width * 0.62), xy[1] + height + max(8, height // 6))],
        fill=(*ACCENT, 220), width=3,
    )


def _corner_brackets(canvas: Image.Image, inset: int, length: int) -> None:
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    w, h = canvas.size
    col = (*ACCENT, 120)
    for cx, cy, dx, dy in (
        (inset, inset, 1, 1),
        (w - inset, inset, -1, 1),
        (inset, h - inset, 1, -1),
        (w - inset, h - inset, -1, -1),
    ):
        d.line([(cx, cy), (cx + dx * length, cy)], fill=col, width=2)
        d.line([(cx, cy), (cx, cy + dy * length)], fill=col, width=2)
    canvas.alpha_composite(overlay)


def build(
    photos: list[Path],
    out_dir: Path,
    size: tuple[int, int],
    side: int,
    top: int,
    logo_h: int,
    gap: int,
) -> tuple[Path, Path]:
    ensure_logo()
    canvas = _paper(size).convert("RGBA")
    _corner_brackets(canvas, inset=max(12, side // 3), length=int(min(size) * 0.07))
    _brand_mark(canvas, logo_h, (side, top))

    area_top = top + logo_h + gap
    area_bottom = size[1] - int(side * 0.85)
    area = (side, area_top, size[0] - side, area_bottom)

    n = max(1, len(photos))
    gutter = int((area[2] - area[0]) * 0.03) if n > 1 else 0
    cell_w = (area[2] - area[0] - gutter * (n - 1)) // n
    cell_h = area[3] - area[1]

    prepared = []
    for p in photos:
        img = prep_photo(p, (int(cell_w * 0.88), int(cell_h * 0.88)))
        if img is not None:
            prepared.append(img)
    if not prepared:
        raise SystemExit("no usable photos")

    # re-centre the row if some photos were dropped
    n = len(prepared)
    gutter = int((area[2] - area[0]) * 0.03) if n > 1 else 0
    cell_w = (area[2] - area[0] - gutter * (n - 1)) // n
    for i, ph in enumerate(prepared):
        cx = area[0] + i * (cell_w + gutter) + (cell_w - ph.width) // 2
        cy = area[1] + (cell_h - ph.height) // 2
        _multiply_paste(canvas, ph, (cx, cy))

    # baseline rule anchoring the product row
    d = ImageDraw.Draw(canvas)
    d.line([(side, area_bottom + 6), (size[0] - side, area_bottom + 6)],
           fill=(*CANVAS_EDGE, 255), width=2)
    d.line([(side, area_bottom + 6), (side + int((size[0] - 2 * side) * 0.18), area_bottom + 6)],
           fill=(*ACCENT, 235), width=3)

    out_dir.mkdir(parents=True, exist_ok=True)
    rgb = canvas.convert("RGB")
    stem = "card" if size == CARD else "hero"
    png = out_dir / f"{stem}.png"
    webp = out_dir / f"{stem}.webp"
    rgb.save(png, "PNG", optimize=True)
    rgb.save(webp, "WEBP", quality=88, method=6)
    return png, webp


def build_slug(slug: str, photo_paths: list[str], out_root: Path = ROOT) -> None:
    photos = [Path(p) if Path(p).is_absolute() else ROOT / p for p in photo_paths]
    for m in [p for p in photos if not p.exists()]:
        print(f"  ! missing photo: {m}", file=sys.stderr)
    photos = [p for p in photos if p.exists()]
    if not photos:
        raise SystemExit(f"no usable photos for {slug}")

    out_dir = out_root / "assets" / "images" / "blog" / slug
    build(photos, out_dir, CARD, side=42, top=30, logo_h=64, gap=18)
    build(photos, out_dir, HERO, side=54, top=38, logo_h=84, gap=24)
    print(f"{slug}: {len(photos)} photo(s) -> card + hero")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--photos", nargs="+")
    ap.add_argument("--batch", help="JSON file: {slug: [photo, ...]}")
    ap.add_argument("--out-root", default=str(ROOT))
    args = ap.parse_args()
    out_root = Path(args.out_root)

    if args.batch:
        data = json.loads(Path(args.batch).read_text(encoding="utf-8"))
        for slug, paths in data.items():
            build_slug(slug, paths, out_root)
        return

    if not args.slug or not args.photos:
        ap.error("need --slug and --photos, or --batch")
    build_slug(args.slug, args.photos, out_root)


if __name__ == "__main__":
    main()



