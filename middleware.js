/** Redirect /products?category=<slug> to clean /products/<slug> URLs */
const CAT_SLUG_MAP = {
  'energy-meter': true,
  'voltage-stabilizer-regulator': true,
  'current-transformer': true,
  'variac-transformer': true,
  'screw-machine': true,
  'solar-pv-products': true,
  'fuse-protection': true,
  'voltage-protector': true,
  'socket-wiring': true,
  'terminal-connector': true,
  'tools-hardware': true,
  'security-seal': true,
  'other': true,
  'busbar': true,
};

function slugFromParam(value) {
  if (!value) return null;
  const raw = decodeURIComponent(String(value).replace(/\+/g, ' ')).trim().toLowerCase();
  if (/^[a-z0-9]+(-[a-z0-9]+)*$/.test(raw) && CAT_SLUG_MAP[raw]) return raw;
  return null;
}

export default function middleware(request) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/$/, '') || '/';

  const isProductsPage = path === '/products' || path === '/products.html';
  if (!isProductsPage) return;

  const category = url.searchParams.get('category');
  const slug = slugFromParam(category);

  if (slug) {
    const target = new URL(`/products/${slug}`, url.origin);
    const idParam = url.searchParams.get('id');
    if (idParam) target.searchParams.set('id', idParam);
    return Response.redirect(target.href, 301);
  }

  if (path === '/products.html') {
    return Response.redirect(new URL('/products', url.origin), 301);
  }
}

export const config = {
  matcher: ['/products', '/products.html'],
};
