import json, os, urllib.request, re, time

data = json.load(open('data/products.json', encoding='utf-8'))
fuse = [p for p in data if p.get('category','') == 'Fuse & Protection']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.alibaba.com/',
}

def safe_name(title, pid):
    s = re.sub(r'[^a-z0-9]+', '-', title.lower())[:40].strip('-')
    return f"{pid}-{s}"

updated = 0
for p in fuse:
    img = p.get('image', '')
    if not img or img.startswith('/'):
        continue  # already local

    pid = p['id']
    folder_name = safe_name(p.get('title', pid), pid)
    folder = f"assets/images/products/fuse-protection/{folder_name}"
    os.makedirs(folder, exist_ok=True)

    # Determine extension
    ext = '.jpg'
    if '.png' in img.lower():
        ext = '.png'
    elif '.webp' in img.lower():
        ext = '.webp'

    local_path = f"{folder}/main{ext}"
    web_path = f"/assets/images/products/fuse-protection/{folder_name}/main{ext}"

    if os.path.exists(local_path):
        print(f"  SKIP (exists): {local_path}")
        p['image'] = web_path
        updated += 1
        continue

    try:
        req = urllib.request.Request(img, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
        with open(local_path, 'wb') as f:
            f.write(content)
        p['image'] = web_path
        print(f"  OK: {pid} -> {local_path} ({len(content)//1024}KB)")
        updated += 1
        time.sleep(0.3)
    except Exception as e:
        print(f"  FAIL: {pid} {img[:60]} -> {e}")

# Save updated products.json
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

print(f"\nDone. Updated {updated} fuse products with local images.")
