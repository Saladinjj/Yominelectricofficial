const fs = require('fs');
const path = require('path');
const root = 'C:\\Users\\Saladin\\Desktop\\yominelectric-main';
const files = [
  'index.html','about.html','blog.html','blog-nepal-loading.html','contact.html','products.html','product-details.html',
  'process.html','solutions.html','energy-meter.html','current-transformer.html','voltage-stabilizer-regulator.html',
  'fuse-protection.html','voltage-protector.html','variac-transformer.html','terminal-connector.html',
  'socket-wiring.html','solar-pv-products.html','security-seal.html','screw-machine.html','tools-hardware.html','other.html'
];
const tag = '<meta name="p:domain_verify" content="744fec106751115b25bc974541f1541a"/>';
files.forEach(f => {
  const fp = path.join(root, f);
  if (!fs.existsSync(fp)) return console.log('MISSING:', f);
  let html = fs.readFileSync(fp, 'utf8');
  if (html.includes('p:domain_verify')) return console.log('SKIP:', f);
  html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + tag);
  fs.writeFileSync(fp, html);
  console.log('DONE:', f);
});
