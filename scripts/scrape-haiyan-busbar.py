'use strict';
import json, re, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUGS = [
  ('flexible-busbar', 'Flexible Busbar'),
  ('rigid-busbar', 'Rigid Busbar'),
  ('aluminum-busbar', 'Aluminum Busbar'),
  ('soft-connection', 'Composite Laminated Busbar'),
  ('solid-connection', 'CCS Integrated Busbar'),
  ('heavy-duty-connectors', 'Heavy Duty Busbar'),
  ('energy-storage-connector', 'Energy Storage Busbar'),
  ('pvc-battery-terminal-covers', 'Busbar Protection'),
]
base = 'https://www.haiyannewenergy.com/'
out = {}
for slug, name in SLUGS:
    url = base + slug
    try:
        html = urllib.request.urlopen(url, timeout=30).read().decode('utf-8', 'replace')
    except Exception as e:
        print('fail', slug, e)
        continue
    desc = ''
    m = re.search(r'<div class="msg">\s*<p>(.*?)</p>', html, re.S)
    if m:
        desc = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    kw_m = re.search(r'<meta name="keywords" content="([^"]+)"', html)
    keywords = [k.strip() for k in (kw_m.group(1).split(',') if kw_m else []) if k.strip()]
    specs = {}
    for m in re.finditer(r'<li[^>]*>\s*<span[^>]*>(.*?)</span>\s*<span[^>]*>(.*?)</span>', html, re.S):
        k = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        v = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if k and v and len(k) < 50:
            specs[k] = v
    for row in re.findall(r'<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>', html, re.S):
        k = re.sub(r'<[^>]+>', '', row[0]).strip()
        v = re.sub(r'<[^>]+>', '', row[1]).strip()
        if k and v and len(k) < 50:
            specs[k] = v
    apps = re.findall(r'<div class="t1"[^>]*>([^<]+)</div>', html)
    out[name] = {
        'url': url,
        'description': desc,
        'keywords': keywords,
        'specs': specs,
        'applications': apps[:12],
    }
    print(name, 'kw', len(keywords), 'specs', len(specs))

(ROOT / 'data' / 'haiyan-busbar-meta.json').write_text(
    json.dumps(out, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'
)
