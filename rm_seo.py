import re, os

cats = ["energy-meter","voltage-stabilizer-regulator","current-transformer","variac-transformer",
        "screw-machine","terminal-connector","solar-pv-products","fuse-protection","voltage-protector",
        "socket-wiring","tools-hardware","security-seal","other","aluminum-busbar","flexible-busbar",
        "rigid-busbar","energy-storage-busbar","busbar-protection","composite-laminated-busbar",
        "ccs-integrated-busbar","heavy-duty-busbar"]

fixed = 0
for c in cats:
    f = c + ".html"
    if not os.path.exists(f):
        continue
    with open(f, "r", encoding="utf-8") as fh:
        txt = fh.read()
    
    # Remove everything from cat-seo div through to (but not including) FOOTER
    before = len(txt)
    new_txt = re.sub(
        r'\n\s*<div class="cat-seo" style="margin-top:48px.*?\n\s*</div>\n\s*</div>\n\s*</div>\n\s*\n\s*<!-- FOOTER -->',
        r'\n\n  <!-- FOOTER -->',
        txt,
        flags=re.DOTALL
    )
    
    if len(new_txt) < before - 500:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new_txt)
        fixed += 1
        print("  Removed SEO block: " + c + " (" + str(before-len(new_txt)) + " bytes)")

print("\nRemoved from " + str(fixed) + " files")
