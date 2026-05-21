/* ═══════════════════════════════════════════════════
   YOMIN ELECTRIC — API.JS
   Centralized API interaction layer
   ═══════════════════════════════════════════════════ */

'use strict';

const API = {
  base: '/api',

  async get(endpoint) {
    const res = await fetch(`${this.base}${endpoint}`, {
      headers: { 'Accept': 'application/json' }
    });
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  },

  async post(endpoint, data) {
    const res = await fetch(`${this.base}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(data)
    });
    const body = await res.json().catch(() => ({}));
    if (!res.ok) {
      const err = new Error(body.message || `API error: ${res.status}`);
      err.status = res.status;
      err.errors = body.errors;
      throw err;
    }
    return body;
  },

  // Product API calls
  products: {
    getAll(params = {}) {
      const q = new URLSearchParams(params).toString();
      return API.get(`/products${q ? '?' + q : ''}`);
    },
    getById(id) {
      return API.get(`/products/${id}`);
    }
  },

    // Contact API calls
    contact: {
      async submit(formData) {
        try {
          return await API.post('/contact', formData);
        } catch (err) {
          // Validation / server errors — surface to the form (no mailto)
          if (err.status && err.status !== 0) throw err;
          // Network failure only — mailto fallback
          console.warn('API unreachable, falling back to mailto:', err.message);
          return { success: true, fallback: 'mailto', formData };
        }
      }
    },

  // Quote API calls
  quote: {
    request(quoteData) {
      return API.post('/quote', quoteData);
    }
  }
};

// Fallback: load from local products.json if backend not available
async function loadProductsLocal() {
  try {
    const res = await fetch('/data/products.json');
    if (!res.ok) throw new Error('Local data not found');
    return res.json();
  } catch (err) {
    console.warn('Could not load products.json:', err);
    return [];
  }
}

window.API = API;
window.loadProductsLocal = loadProductsLocal;
