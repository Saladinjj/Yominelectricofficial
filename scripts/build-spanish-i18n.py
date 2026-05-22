"""Build Spanish i18n from English keys in main.js and index.html."""
import json
import re
import time
from pathlib import Path
from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "assets/js/main.js"
INDEX = ROOT / "index.html"
OUT_MAIN = ROOT / "assets/js/i18n-es.js"
OUT_INDEX = ROOT / "assets/js/i18n-index-es.js"
CACHE = ROOT / "data/i18n-es-cache.json"

translator = GoogleTranslator(source="en", target="es")
BATCH = 40


def extract_main_pairs(text):
    m = re.search(r"en:\s*\{([\s\S]*?)\},\s*fr:", text)
    if not m:
        return {}
    block = m.group(1)
    pairs = {}
    for km in re.finditer(r"(?:^|,\s*)([a-z][a-z0-9_]*):'((?:\\'|[^'])*)'", block):
        key, val = km.group(1), km.group(2).replace("\\'", "'")
        pairs[key] = val
    return pairs


def extract_index_pairs(text):
    m = re.search(r'en:\s*\{([\s\S]*?)\},\s*fr:', text)
    if not m:
        return {}
    block = m.group(1)
    pairs = {}
    for km in re.finditer(r'(\w+):"((?:\\"|[^"])*)"', block):
        key, val = km.group(1), km.group(2).replace('\\"', '"')
        pairs[key] = val
    for km in re.finditer(r"(\w+):'((?:\\'|[^'])*)'", block):
        key, val = km.group(1), km.group(2).replace("\\'", "'")
        pairs[key] = val
    return pairs


def should_skip(val):
    if not val.strip():
        return True
    if re.fullmatch(r"[\d\s+°%./\-–—,;:()&+]+", val):
        return True
    if val.startswith("+86"):
        return True
    return False


def translate_batch(values, cache):
    out = []
    todo_idx = []
    todo_vals = []
    for i, v in enumerate(values):
        if v in cache:
            out.append(cache[v])
        elif should_skip(v):
            cache[v] = v
            out.append(v)
        else:
            out.append(None)
            todo_idx.append(i)
            todo_vals.append(v)

    for start in range(0, len(todo_vals), BATCH):
        chunk = todo_vals[start : start + BATCH]
        try:
            translated = translator.translate_batch(chunk)
            time.sleep(0.15)
        except Exception:
            translated = chunk
        for orig, es in zip(chunk, translated):
            cache[orig] = es or orig
        for j, orig in enumerate(chunk):
            out[todo_idx[start + j]] = cache[orig]

    return out


def pairs_to_js(pairs, quote="'"):
    lines = []
    items = list(pairs.items())
    i = 0
    while i < len(items):
        chunk = []
        for _ in range(3):
            if i >= len(items):
                break
            k, v = items[i]
            if quote == "'":
                v = v.replace("'", "\\'")
                chunk.append(f"{k}:'{v}'")
            else:
                v = v.replace("\\", "\\\\").replace('"', '\\"')
                chunk.append(f'{k}:"{v}"')
            i += 1
        lines.append("    " + ",".join(chunk) + ",")
    if lines:
        lines[-1] = lines[-1].rstrip(",")
    return "\n".join(lines)


def main():
    print("Reading sources…")
    main_src = MAIN.read_text(encoding="utf-8")
    index_src = INDEX.read_text(encoding="utf-8")
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}

    en_main = extract_main_pairs(main_src)
    en_index = extract_index_pairs(index_src)
    print(f"  main.js: {len(en_main)} keys, index.html: {len(en_index)} keys")

    keys_main = list(en_main.keys())
    vals_main = [en_main[k] for k in keys_main]
    print("Translating main.js keys…")
    es_vals_main = translate_batch(vals_main, cache)
    es_main = dict(zip(keys_main, es_vals_main))

    keys_index = list(en_index.keys())
    vals_index = [en_index[k] for k in keys_index]
    print("Translating index.html keys…")
    es_vals_index = translate_batch(vals_index, cache)
    es_index = dict(zip(keys_index, es_vals_index))

    CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

    js_main = (
        "/* Spanish translations for inner pages (loaded after main.js) */\n"
        "'use strict';\n"
        "if (typeof T !== 'undefined') {\n"
        "  T.es = {\n"
        + pairs_to_js(es_main, "'")
        + "\n  };\n}\n"
    )
    OUT_MAIN.write_text(js_main, encoding="utf-8")

    js_index = (
        "/* Spanish translations for homepage (loaded after inline T) */\n"
        "'use strict';\n"
        "if (typeof T !== 'undefined') {\n"
        "  T.es = {\n"
        + pairs_to_js(es_index, '"')
        + "\n  };\n}\n"
    )
    OUT_INDEX.write_text(js_index, encoding="utf-8")

    print(f"Wrote {OUT_MAIN}")
    print(f"Wrote {OUT_INDEX}")


if __name__ == "__main__":
    main()
