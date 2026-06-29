const fs = require('fs');
const path = require('path');
const projRoot = 'C:\\Users\\Saladin\\Desktop\\yominelectric-main';
const jsonPath = path.join(projRoot, 'data', 'products.json');
const products = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const prod = products.find(p => p.id === 'ym-sm-001');

function fixEncoding(s) {
  if (typeof s !== 'string') return s;
  return s.replace(/\u00e2\u20ac\u201d/g, '\u2014')  // â€" → —
          .replace(/\u00e2\u20ac\u201c/g, '\u2013')  // â€" → –
          .replace(/\u00e2\u2020\u2019/g, '\u2192')  // â†' → →
          .replace(/\u00c3\u2014/g, '\u00d7')         // Ã— → ×
          .replace(/\u00c2\u00b1/g, '\u00b1');        // Â± → ±
}

// Fix main description
prod.description = fixEncoding(prod.description);

// Fix main specs
const fixedSpecs = {};
for (const [k, v] of Object.entries(prod.specs)) {
  fixedSpecs[k] = fixEncoding(v);
}
prod.specs = fixedSpecs;

// Fix processes
prod.processes.forEach(proc => {
  proc.description = fixEncoding(proc.description);
  
  // Convert specs from @{...} string to proper object
  if (typeof proc.specs === 'string' && proc.specs.startsWith('@{')) {
    const specStr = proc.specs.slice(2, -1);
    const specObj = {};
    const pairs = specStr.split(';').map(s => s.trim()).filter(Boolean);
    pairs.forEach(pair => {
      const eqIdx = pair.indexOf('=');
      if (eqIdx > 0) {
        const key = fixEncoding(pair.substring(0, eqIdx).trim());
        const val = fixEncoding(pair.substring(eqIdx + 1).trim());
        specObj[key] = val;
      }
    });
    proc.specs = specObj;
  } else if (typeof proc.specs === 'object' && proc.specs !== null) {
    const fixed = {};
    for (const [k, v] of Object.entries(proc.specs)) {
      fixed[fixEncoding(k)] = fixEncoding(v);
    }
    proc.specs = fixed;
  }
});

fs.writeFileSync(jsonPath, JSON.stringify(products, null, 2));
console.log('Fixed ym-sm-001 encoding and specs');
