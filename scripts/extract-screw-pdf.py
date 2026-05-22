"""Extract screw machine catalogue from PDF into JSON + images."""
import json
import re
import sys
from pathlib import Path

try:
    import fitz  # pymupdf
except ImportError:
    print("pymupdf required")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "yomin screw machines.pdf"
OUT_IMG = ROOT / "assets" / "images" / "screw-machines"
OUT_JSON = ROOT / "data" / "screw-machines-raw.json"

OUT_IMG.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
pages_meta = []

for i, page in enumerate(doc):
    text = page.get_text("text") or ""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # render page image
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    img_name = f"page-{i+1:03d}.jpg"
    img_path = OUT_IMG / img_name
    pix.save(str(img_path))
    pages_meta.append({
        "page": i + 1,
        "image": f"/assets/images/screw-machines/{img_name}",
        "lines": lines,
        "text": text[:4000],
    })

doc.close()

# Heuristic: group pages into products by title-like lines
products = []
current = None
skip_words = re.compile(r"^(yomin|yueqing|catalog|catalogue|page|\d+$|www\.|http)", re.I)

for pm in pages_meta:
    title = None
    body_lines = []
    for ln in pm["lines"]:
        if len(ln) < 4 or len(ln) > 120:
            continue
        if skip_words.match(ln):
            continue
        # likely title: short, has machine/screw/model or all caps chunk
        if not title and (
            re.search(r"screw|machine|tapping|drilling|thread|bolt|nut|assembly", ln, re.I)
            or (ln.isupper() and len(ln) < 60)
            or re.match(r"^[A-Z]{1,5}[-\s]?\d", ln)
        ):
            title = ln
        else:
            body_lines.append(ln)

    if not title and pm["lines"]:
        # use longest meaningful line
        candidates = [ln for ln in pm["lines"] if 8 < len(ln) < 80 and not skip_words.match(ln)]
        if candidates:
            title = max(candidates, key=len)

    if not title:
        title = f"Screw Machine — Page {pm['page']}"

    specs = {}
    keywords = []
    for ln in body_lines:
        if re.search(r"[:：]", ln):
            parts = re.split(r"[:：]", ln, 1)
            if len(parts) == 2:
                specs[parts[0].strip()] = parts[1].strip()
        elif re.search(r"\d+\s*(mm|kW|V|A|rpm|pcs|Hz)", ln, re.I):
            specs.setdefault("Technical", specs.get("Technical", "") + ("; " if specs.get("Technical") else "") + ln)
        else:
            keywords.append(ln)

    products.append({
        "page": pm["page"],
        "title": title,
        "description": " ".join(body_lines[:6])[:500] if body_lines else f"Yomin screw machine from catalogue page {pm['page']}.",
        "specs": specs,
        "keywords": keywords[:12],
        "image": pm["image"],
    })

OUT_JSON.write_text(json.dumps({"page_count": len(pages_meta), "products": products}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"pages={len(pages_meta)} products={len(products)}")
print(f"written {OUT_JSON}")
