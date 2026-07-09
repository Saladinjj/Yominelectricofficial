import json

data = json.load(open('data/products.json', encoding='utf-8'))
fuse = [p for p in data if p.get('category','') == 'Fuse & Protection']
print('Total fuse products:', len(fuse))

cdn = [p for p in fuse if not p.get('image','').startswith('/')]
local = [p for p in fuse if p.get('image','').startswith('/')]
print('CDN images:', len(cdn))
print('Local images:', len(local))
print()
for p in cdn:
    img = p.get('image','')
    print(p['id'], img[:100])
