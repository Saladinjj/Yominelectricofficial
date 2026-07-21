import os
import re

root_dir = r'C:\Users\Saladin\Desktop\yominelectric-main'
skip_dirs = {'node_modules', '.git', 'scripts', 'temp', 'yominelectric-main', 'LibreChat'}

count = 0

# 1. Add product translation script tags to all HTML files
# 2. Modify the product title rendering to use translations

for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    for f in filenames:
        if not f.endswith('.html'):
            continue
        path = os.path.join(dirpath, f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        original = content
        
        # --- CHANGE 1: Add product i18n script tags before main.js ---
        # Find the main.js script tag and add product translation files before it
        old_js_load = '<script defer src="assets/js/main.js"></script>'
        new_js_load = '''<script defer src="assets/js/i18n-products-fr.js"></script>
<script defer src="assets/js/i18n-products-es.js"></script>
<script defer src="assets/js/i18n-products-ar.js"></script>
<script defer src="assets/js/main.js"></script>'''
        
        if old_js_load in content and 'i18n-products-fr.js' not in content:
            content = content.replace(old_js_load, new_js_load)
        
        # --- CHANGE 2: Translate product titles in card rendering ---
        # In product cards: ${esc(p.title)} and ${p.title} need to become translated
        # We add a function call: ${esc(T[currentLang]?.[p.id] || p.title)}
        # But we can't modify the template literal trivially. Instead, we modify the 
        # applyTranslations function in main.js to also handle product titles post-render.
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            count += 1
            print(f"Added i18n scripts to: {os.path.relpath(path, root_dir)}")

print(f"\nScript tags added to {count} files.")

# --- CHANGE 3: Modify main.js to translate product titles after rendering ---
main_js_path = os.path.join(root_dir, 'assets', 'js', 'main.js')
with open(main_js_path, 'r', encoding='utf-8') as f:
    main_js = f.read()

# Add product title translation to applyTranslations
old_apply = '''  // Support both data-t (inner pages) and data-i18n (index.html) attributes
  document.querySelectorAll('[data-t],[data-i18n]').forEach(el => {'''
new_apply = '''  // Support both data-t (inner pages) and data-i18n (index.html) attributes
  document.querySelectorAll('[data-t],[data-i18n]').forEach(el => {
  // Also translate product cards that have data-pid attribute
  document.querySelectorAll('[data-pid]').forEach(el => {
    const pid = el.dataset.pid;
    if (pid && d[pid]) el.textContent = d[pid];
  });'''

if old_apply in main_js and 'data-pid' not in main_js:
    main_js = main_js.replace(old_apply, new_apply)

# Also update setLang to re-render product list after language change
old_setLang = '''function setLang(l) {
  if (!T[l]) return;
  currentLang = l;
  localStorage.setItem('ym_lang', l);
  const isRTL = l === 'ar';
  document.documentElement.lang = l;
  document.documentElement.dir = isRTL ? 'rtl' : 'ltr';
  document.body.dir = isRTL ? 'rtl' : 'ltr';
  document.body.classList.toggle('ar', isRTL);
  applyTranslations();
  updateLangUI();
}'''

new_setLang = '''function setLang(l) {
  if (!T[l]) return;
  currentLang = l;
  localStorage.setItem('ym_lang', l);
  const isRTL = l === 'ar';
  document.documentElement.lang = l;
  document.documentElement.dir = isRTL ? 'rtl' : 'ltr';
  document.body.dir = isRTL ? 'rtl' : 'ltr';
  document.body.classList.toggle('ar', isRTL);
  applyTranslations();
  updateLangUI();
  // Re-render product list with new language
  if (typeof renderProductList === 'function') renderProductList(currentPage || 1);
}'''

if old_setLang in main_js:
    main_js = main_js.replace(old_setLang, new_setLang)

with open(main_js_path, 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Updated main.js with product title translation support")

# --- CHANGE 4: Modify product card rendering to add data-pid attribute ---
# In all category pages, add data-pid to product title spans
for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    for f in filenames:
        if not f.endswith('.html'):
            continue
        path = os.path.join(dirpath, f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        original = content
        
        # Add data-pid="${p.id}" to product card titles
        # Pattern: ${esc(p.title)} in product cards
        content = content.replace(
            '${esc(p.title)}',
            '${esc(T[currentLang]?.[p.id] || p.title)}'
        )
        
        # Also for the WhatsApp text
        content = content.replace(
            "Hi Yomin Electric, I am interested in: '+p.title+'",
            "Hi Yomin Electric, I am interested in: '+(T[currentLang]?.[p.id] || p.title)+'"
        )
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated product titles in: {os.path.relpath(path, root_dir)}")

print("Done - product title translation fully integrated.")
