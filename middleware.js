/** 301 legacy product URLs to canonical /products?category=<slug> */
const CAT_TO_SLUG = {
  'energy meter': 'energy-meter',
  'voltage stabilizer/regulator': 'voltage-stabilizer-regulator',
  'current transformer': 'current-transformer',
  'variac/transformer': 'variac-transformer',
  'terminal & connector': 'terminal-connector',
  'solar/pv products': 'solar-pv-products',
  'fuse & protection': 'fuse-protection',
  'voltage protector': 'voltage-protector',
  'socket & wiring': 'socket-wiring',
  'tile leveling system': 'tile-leveling-system',
  'tools & hardware': 'tools-hardware',
  'security seal': 'security-seal',
  'other': 'other',
};

function slugFromParam(value) {
  if (!value) return null;
  const raw = decodeURIComponent(String(value).replace(/\+/g, ' ')).trim();
  const lower = raw.toLowerCase();
  if (/^[a-z0-9]+(-[a-z0-9]+)*$/.test(lower)) return lower;
  return CAT_TO_SLUG[lower] || null;
}

export default function middleware(request) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/$/, '') || '/';
  const isProductsPage = path === '/products' || path === '/products.html' || path === '/product' || path === '/product.html';
  if (!isProductsPage) return;

  const legacyCat = url.searchParams.get('cat');
  const category = url.searchParams.get('category');
  const slug = slugFromParam(legacyCat) || slugFromParam(category);

  if (!legacyCat && !category && (path === '/products' || path === '/products.html')) return;
  if (path === '/products' && category && slug === category.toLowerCase()) return;

  const target = new URL('/products', url.origin);
  if (slug) target.searchParams.set('category', slug);
  return Response.redirect(target.href, 301);
}

export const config = {
  matcher: ['/products', '/products.html', '/product', '/product.html'],
};
