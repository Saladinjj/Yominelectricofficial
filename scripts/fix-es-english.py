"""Re-translate i18n-es.js keys that were left in English."""
import json
import re
import time
from pathlib import Path
from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "assets/js/main.js"
ES_FILE = ROOT / "assets/js/i18n-es.js"
CACHE = ROOT / "data/i18n-es-cache.json"

translator = GoogleTranslator(source="en", target="es")


def extract_en():
    text = MAIN.read_text(encoding="utf-8")
    m = re.search(r"en:\s*\{([\s\S]*?)\},\s*fr:", text)
    pairs = {}
    for km in re.finditer(r"(?:^|,\s*)([a-z][a-z0-9_]*):'((?:\\'|[^'])*)'", m.group(1)):
        pairs[km.group(1)] = km.group(2).replace("\\'", "'")
    return pairs


def extract_es():
    text = ES_FILE.read_text(encoding="utf-8")
    m = re.search(r"const _esInner = \{([\s\S]*?)\n  \};", text)
    pairs = {}
    for km in re.finditer(r"(?:^|,\s*)([a-z][a-z0-9_]*):'((?:\\'|[^'])*)'", m.group(1)):
        pairs[km.group(1)] = km.group(2).replace("\\'", "'")
    return pairs, text


def main():
    en = extract_en()
    es, raw = extract_es()
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    fix = []
    for k, ev in en.items():
        sv = es.get(k, "")
        if sv == ev or (len(ev) > 20 and sv == ev):
            fix.append((k, ev))
    print(f"Fixing {len(fix)} keys…")
    for k, ev in fix:
        try:
            if "<" in ev and ">" in ev:
                parts = re.split(r"(<[^>]+>)", ev)
                out = []
                for p in parts:
                    if p.startswith("<"):
                        out.append(p)
                    elif p.strip():
                        out.append(translator.translate(p))
                        time.sleep(0.05)
                    else:
                        out.append(p)
                es[k] = "".join(out)
            else:
                es[k] = translator.translate(ev)
                time.sleep(0.05)
            cache[ev] = es[k]
        except Exception:
            es[k] = ev
    CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

    lines = []
    items = list(es.items())
    i = 0
    while i < len(items):
        chunk = []
        for _ in range(3):
            if i >= len(items):
                break
            k, v = items[i]
            v = v.replace("'", "\\'")
            chunk.append(f"{k}:'{v}'")
            i += 1
        lines.append("    " + ",".join(chunk) + ",")
    if lines:
        lines[-1] = lines[-1].rstrip(",")
    inner = "\n".join(lines)
    new_raw = re.sub(
        r"const _esInner = \{[\s\S]*?\n  \};",
        f"const _esInner = {{\n{inner}\n  }};",
        raw,
        count=1,
    )
    ES_FILE.write_text(new_raw, encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()
