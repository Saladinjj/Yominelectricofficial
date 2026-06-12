/**
 * YOMIN ELECTRIC — Backend Server
 * Node.js + Express API server
 *
 * Run: node backend/server.js
 * API: http://localhost:3000/api
 */

'use strict';

const express = require('express');
const cors = require('cors');
const path = require('path');

const config = require('./config/config');
const productRoutes = require('./routes/products');
const contactRoutes = require('./routes/contact');

const app = express();

// ─── MIDDLEWARE ───
app.use(cors({
  origin: config.corsOrigin,
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true, limit: '1mb' }));

// ─── SERVE STATIC FILES (dev only — Vercel handles this in production) ───
if (config.isDev) {
  app.use(express.static(path.join(__dirname, '..')));
}

// ─── API ROUTES ───
app.use('/api/products', productRoutes);
app.use('/api/contact', contactRoutes);
app.use('/api/quote', contactRoutes);

// ─── HEALTH CHECK ───
app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    version: '1.0.0',
    service: 'Yomin Electric API'
  });
});

// ─── CLEAN URL ROUTING (dev only — Vercel routing handles this in production) ───
const cleanRoutes = {
  '/': 'index.html',
  '/index': 'index.html',
  '/about': 'about.html',
  '/contact': 'contact.html',
  '/products': 'products.html',
  '/product-details': 'product-details.html',
  '/process': 'process.html',
  '/solutions': 'solutions.html',
  '/products/energy-meter': 'energy-meter.html',
  '/products/voltage-stabilizer-regulator': 'voltage-stabilizer-regulator.html',
  '/products/current-transformer': 'current-transformer.html',
  '/products/variac-transformer': 'variac-transformer.html',
  '/products/screw-machine': 'screw-machine.html',
  '/products/fuse-protection': 'fuse-protection.html',
  '/products/voltage-protector': 'voltage-protector.html',
  '/products/socket-wiring': 'socket-wiring.html',
  '/products/terminal-connector': 'terminal-connector.html',
  '/products/solar-pv-products': 'solar-pv-products.html',
  '/products/tools-hardware': 'tools-hardware.html',
  '/products/security-seal': 'security-seal.html',
  '/products/other': 'other.html',
  '/products/busbar': 'busbar.html',
};

if (config.isDev) {
  Object.entries(cleanRoutes).forEach(([url, file]) => {
    app.get(url, (req, res) => {
      res.sendFile(path.join(__dirname, '..', file));
    });
  });

  app.get('/video/company-overview', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'video', 'company-overview.html'));
  });

  // Redirect .html to clean URLs
  app.get('/*.html', (req, res) => {
    const clean = req.path.replace(/\.html$/, '');
    res.redirect(301, clean || '/');
  });
}

// ─── ERROR HANDLER ───
app.use((err, req, res, next) => {
  console.error('[ERROR]', err.message);
  res.status(err.status || 500).json({
    success: false,
    message: config.isDev ? err.message : 'An error occurred. Please try again.'
  });
});

// ─── START ───
if (config.isDev) {
  app.listen(config.port, () => {
    console.log(`\n🔌 Yomin Electric API running`);
    console.log(`   ➜ http://localhost:${config.port}`);
    console.log(`   ➜ API: http://localhost:${config.port}/api`);
    console.log(`   ➜ Env: development\n`);
  });
}

module.exports = app;
