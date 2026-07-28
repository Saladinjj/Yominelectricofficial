import json

with open("vercel.json", "r", encoding="utf-8") as f:
    config = json.load(f)

routes = config["routes"]

# Find insertion point (before the (.*) catch-all)
insert_at = None
for i, r in enumerate(routes):
    if r.get("src") == "/(.*)" and r.get("check"):
        insert_at = i
        break

if insert_at is None:
    insert_at = max(len(routes) - 2, 0)

new_routes = [
    {"src": "/guide/energy-meter-types", "dest": "/guide/energy-meter-types.html"},
    {"src": "/guide/current-transformer-selection", "dest": "/guide/current-transformer-selection.html"},
    {"src": "/guide/voltage-stabilizer-buying-guide", "dest": "/guide/voltage-stabilizer-buying-guide.html"},
    {"src": "/compare/single-phase-vs-three-phase-meter", "dest": "/compare/single-phase-vs-three-phase-meter.html"},
    {"src": "/compare/prepaid-vs-postpaid-meter", "dest": "/compare/prepaid-vs-postpaid-meter.html"},
    {"src": "/guide", "dest": "/guide/energy-meter-types.html"},
    {"src": "/compare", "dest": "/compare/single-phase-vs-three-phase-meter.html"},
]

existing = set(r["src"] for r in routes)
for nr in new_routes:
    if nr["src"] not in existing:
        routes.insert(insert_at, nr)
        insert_at += 1
        print("  Added: " + nr["src"] + " -> " + nr["dest"])

with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Routes updated")
