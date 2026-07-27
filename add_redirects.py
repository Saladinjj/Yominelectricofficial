import json

with open("vercel.json", "r", encoding="utf-8") as f:
    config = json.load(f)

redirects = config["redirects"]

# Redirects to add (source -> destination)
new_redirects = [
    ("/energy-meter.html", "/products?category=energy-meter"),
    ("/voltage-stabilizer-regulator.html", "/products?category=voltage-stabilizer-regulator"),
    ("/current-transformer.html", "/products?category=current-transformer"),
    ("/variac-transformer.html", "/products?category=variac-transformer"),
    ("/screw-machine.html", "/products?category=screw-machine"),
    ("/terminal-connector.html", "/products?category=terminal-connector"),
    ("/solar-pv-products.html", "/products?category=solar-pv-products"),
    ("/fuse-protection.html", "/products?category=fuse-protection"),
    ("/voltage-protector.html", "/products?category=voltage-protector"),
    ("/socket-wiring.html", "/products?category=socket-wiring"),
    ("/tools-hardware.html", "/products?category=tools-hardware"),
    ("/security-seal.html", "/products?category=security-seal"),
    ("/other.html", "/products?category=other"),
    ("/product-details.html", "/products"),
]

# Check which ones already exist
existing = set(r["source"] for r in redirects)
added = 0
for src, dst in new_redirects:
    if src not in existing:
        # Insert after the busbar.html entry
        for i, r in enumerate(redirects):
            if r.get("source") == "/busbar.html":
                redirects.insert(i + 1, {"source": src, "destination": dst, "statusCode": 301})
                added += 1
                print("  Added: " + src + " -> " + dst)
                break

with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("\nAdded " + str(added) + " redirects")
