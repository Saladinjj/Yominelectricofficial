const fs = require('fs');
const path = require('path');
const jsonPath = path.join(__dirname, '..', 'data', 'products.json');
const products = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Category-specific base keywords
const CAT_KW = {
  'Energy Meter': ['energy meter','kwh meter','electric meter','power meter','din rail meter','single phase meter','three phase meter','digital meter','smart meter','electricity meter'],
  'Current Transformer': ['current transformer','split core ct','low voltage ct','metering ct','protection ct','toroidal transformer','busbar ct','ct manufacturer'],
  'Voltage Stabilizer/Regulator': ['voltage stabilizer','voltage regulator','avr','automatic voltage regulator','servo stabilizer','ac stabilizer','power stabilizer'],
  'Fuse & Protection': ['fuse','circuit breaker','disconnect switch','isolating switch','protection device','surge protector','overcurrent protection'],
  'Voltage Protector': ['voltage protector','over voltage protection','under voltage protection','surge protector','voltage monitor'],
  'Variac/Transformer': ['variac','variable transformer','voltage transformer','ac transformer','auto transformer','step up transformer','step down transformer'],
  'Screw Machine': ['screw machine','terminal machine','brass machine','metal processing','drilling machine','tapping machine','assembly machine','busbar machine'],
  'Terminal & Connector': ['terminal block','connector','cable lug','terminal lug','brass terminal','copper terminal','screw terminal','electrical connector'],
  'Solar/PV Products': ['solar','pv','photovoltaic','combiner box','dc breaker','solar panel','solar system','renewable energy'],
  'Socket & Wiring': ['socket','smart socket','wifi socket','outlet','wall plug','power socket','usb socket'],
  'Tools & Hardware': ['electrical tool','hardware','transformer','control transformer','isolation transformer','machine tool'],
  'Security Seal': ['security seal','meter seal','tamper seal','plastic seal','wire seal','utility seal'],
  'Other': ['electrical product','electrical component','electrical equipment','industrial electrical','china manufacturer'],
};

// Flexible Busbar sub-categories
const BUSBAR_KW = {
  'Flexible Busbar': ['flexible busbar','braided busbar','copper busbar','battery busbar','laminated busbar'],
  'Rigid Busbar': ['rigid busbar','copper bar','bus bar','power busbar','insulated busbar'],
  'Aluminum Busbar': ['aluminum busbar','aluminium busbar','aluminum bar','lightweight busbar'],
  'Composite Laminated Busbar': ['laminated busbar','composite busbar','multilayer busbar','hybrid busbar'],
  'CCS Integrated Busbar': ['ccs busbar','cell contact system','battery busbar','integrated busbar'],
  'Heavy Duty Busbar': ['heavy duty busbar','high current busbar','industrial busbar','welded busbar'],
  'Energy Storage Busbar': ['energy storage busbar','ess busbar','battery storage busbar','container busbar'],
  'Busbar Protection': ['busbar protection','busbar insulation','busbar cover','safety cover'],
};

function extractTitleWords(title) {
  const words = title.toLowerCase()
    .replace(/[^a-z0-9\s\/\-]/g, '')
    .split(/\s+/)
    .filter(w => w.length > 2 && !['the','and','for','with','use','new','type','high','low','made','used','from','that','this','into','over','has','can','its','not','but','all','are','was'].includes(w));
  return [...new Set(words)];
}

function generateKeywords(product) {
  const cat = product.category;
  const base = [...(CAT_KW[cat] || CAT_KW['Other']), ...(BUSBAR_KW[cat] || [])];
  const titleWords = extractTitleWords(product.title);
  const specWords = Object.values(product.specs || {})
    .filter(v => typeof v === 'string')
    .flatMap(v => extractTitleWords(v));
  
  // Combine and deduplicate
  const all = [...new Set([...titleWords, ...specWords, ...base])];
  // Take up to 25 keywords, prioritize title words first
  const combined = [...titleWords.slice(0, 10), ...specWords.slice(0, 5), ...base];
  return [...new Set(combined)].slice(0, 25);
}

let added = 0;
products.forEach(p => {
  if (!p.keywords || p.keywords.length === 0) {
    p.keywords = generateKeywords(p);
    added++;
  }
});

fs.writeFileSync(jsonPath, JSON.stringify(products, null, 2));
console.log(`Added keywords to ${added} products`);
