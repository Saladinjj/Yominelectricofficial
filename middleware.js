/** Canonical URL enforcement and legacy redirects for products page */
export default function middleware(request) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/$/, '') || '/';

  /* Redirect /products.html and /product.html to /products */
  if (path === '/products.html' || path === '/product.html') {
    const target = new URL('/products', url.origin);
    url.searchParams.forEach((v, k) => target.searchParams.set(k, v));
    if (target.search !== url.search || target.pathname !== path) {
      return Response.redirect(target.href, 301);
    }
  }

  /* Normalize trailing /products/ to /products */
  if (url.pathname === '/products/') {
    const target = new URL('/products', url.origin);
    url.searchParams.forEach((v, k) => target.searchParams.set(k, v));
    return Response.redirect(target.href, 301);
  }

  return;
}

export const config = {
  matcher: ['/products', '/products.html', '/product', '/product.html', '/products/'],
};
