import json

data = json.load(open('data/products.json', encoding='utf-8'))
fuse = [p for p in data if p.get('category','') == 'Fuse & Protection']

print(f'Writing {len(fuse)} fuse products to data/fuse-protection.json')
with open('data/fuse-protection.json', 'w', encoding='utf-8') as f:
    json.dump(fuse, f, ensure_ascii=False, indent=2)
print('Done.')
