/* ═══════════════════════════════════════════════
   GRAMLINGO — Service Worker (Offline + Cache)
   Cache-first for static assets, network-first otherwise.
   Versioned — changes to CACHE_VERSION trigger re-cache.
   ═══════════════════════════════════════════════ */

const CACHE_VERSION = 'gramlingo-v9';
const STATIC_CACHE = `${CACHE_VERSION}-static`;
const DATA_CACHE = `${CACHE_VERSION}-data`;

// Patterns that are cache-first (app shell + assets)
// NOTE: origin-agnostic on purpose — the app runs at /gramlingo/ on
// github.io AND at / on the custom domain gramlingo.online.
const STATIC_PATTERNS = [
  /\.(js|css|svg|png|jpg|jpeg|webp|woff2?|ttf)$/i,
  /\/assets\//,
  /\/data\//,
  /\/favicon\.svg/,
  /\/icons\.svg/,
  /\/manifest\.json/,
  /fonts\.googleapis\.com/,
  /fonts\.gstatic\.com/,
];

// Patterns that are network-first (API, auth callbacks)
const NETWORK_FIRST_PATTERNS = [
  /supabase\.co/,
  /\/auth\//,
];

function isStatic(url) {
  return STATIC_PATTERNS.some(p => p.test(url));
}

function isNetworkFirst(url) {
  return NETWORK_FIRST_PATTERNS.some(p => p.test(url));
}

// ── Install: pre-cache the app shell ──
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      // Cache the root page (navigational pre-cache)
      return cache.add(new URL('./', self.location.href).href).catch(() => {});
    })
  );
  self.skipWaiting();
});

// ── Activate: clean old caches ──
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys
          .filter(k => k !== STATIC_CACHE && k !== DATA_CACHE)
          .map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

// ── Fetch ──
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = request.url;

  // Only handle GET requests
  if (request.method !== 'GET') return;

  // Don't cache Supabase API calls or auth requests
  if (isNetworkFirst(url)) return;

  // Static assets: cache-first with network fallback
  if (isStatic(url)) {
    event.respondWith(
      caches.match(request).then((cached) => {
        if (cached) {
          // Stale-while-revalidate: update cache in background
          fetch(request).then((response) => {
            if (response.ok) {
              caches.open(STATIC_CACHE).then((cache) => {
                cache.put(request, response);
              });
            }
          }).catch(() => {});
          return cached;
        }
        // Not in cache — fetch and cache
        return fetch(request).then((response) => {
          if (!response.ok) return response;
          const clone = response.clone();
          caches.open(STATIC_CACHE).then((cache) => {
            cache.put(request, clone);
          });
          return response;
        });
      })
    );
    return;
  }

  // Everything else: network-first with cache fallback
  event.respondWith(
    fetch(request)
      .then((response) => {
        if (response.ok) {
          const clone = response.clone();
          caches.open(DATA_CACHE).then((cache) => {
            cache.put(request, clone);
          });
        }
        return response;
      })
      .catch(() => {
        return caches.match(request);
      })
  );
});
