
var staticCacheName = 'OMMCSL-V1';

const assets = [
  "/",
  "../static/assets/css/main.css",
  "../static/assets/css/passcode.css",
  "../static/assets/css/shares.css",
  "../static/assets/css/style.css",
  "../static/assets/js/main.js",
  "../static/assets/js/offline.js",
  "../static/assets/js/news.js",
  "../static/assets/img/omsbackground.png",
  "../static/assets/img/omslogo.png",
  "../static/assets/img/hero-bg2.png"
]

const FALLBACK_HTML_URL = '/offline/'

var staticCacheName = 'OMMCSL-V1';
 
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        assets,
        new Request(FALLBACK_HTML_URL, { cache: "reload" }),
      ]);
    })
  );
    // Force the waiting service worker to become the active service worker.
    self.skipWaiting();
});

self.addEventListener('activate', function(event) {
    // Tell the active service worker to take control of the page immediately.
    self.clients.claim();
});
 
self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
      .catch(() => {
        return caches.match(FALLBACK_HTML_URL);
      })
    );
});

/* const HTML_CACHE = "html";
const JS_CACHE = "javascript";
const STYLE_CACHE = "stylesheets";
const IMAGE_CACHE = "images";
const FONT_CACHE = "fonts";
const CACHE_NAME = 'offline-html';
const FALLBACK_HTML_URL = '/offline/';

self.addEventListener('install',  (event) => {
  event.waitUntil(
    // Setting {cache: 'reload'} in the new request will ensure that the
    // response isn't fulfilled from the HTTP cache; i.e., it will be from
    // the network.
    cashes.open(staticCacheName).then(cache => {
      cache.addAll(assets)
    }),
    caches.open(CACHE_NAME)
      .then((cache) => cache.add(
        new Request(FALLBACK_HTML_URL, { cache: "reload" })
      ))
  );

  // Force the waiting service worker to become the active service worker.
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  // Tell the active service worker to take control of the page immediately.
  self.clients.claim();
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
      .catch(() => {
        return caches.match(FALLBACK_HTML_URL);
      })
  );
});

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
}); */

/* workbox.routing.registerRoute(
  ({event}) => event.request.destination === 'document',
  new workbox.strategies.NetworkFirst({
    cacheName: HTML_CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 10,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  ({event}) => event.request.destination === 'script',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: JS_CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 15,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  ({event}) => event.request.destination === 'style',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: STYLE_CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 15,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  ({event}) => event.request.destination === 'image',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: IMAGE_CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 15,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  ({event}) => event.request.destination === 'font',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: FONT_CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 15,
      }),
    ],
  })
);
 */


/* 
var staticCacheName = 'OMMCSL-V1';
 
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '',
        new Request(FALLBACK_HTML_URL, { cache: "reload" }),
      ]);
    })
  );
    // Force the waiting service worker to become the active service worker.
    self.skipWaiting();
});

self.addEventListener('activate', function(event) {
    // Tell the active service worker to take control of the page immediately.
    self.clients.claim();
});
 
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match(''));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
      .catch(() => {
        return caches.match(FALLBACK_HTML_URL);
      })
    );
}); */

//This is the service worker with the Advanced caching

/* importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');
 */
/* const manifest = self.__WB_MANIFEST;
if (manifest) {
  // do nothing
} */
