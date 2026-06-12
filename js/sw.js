const CACHE_NAME = 'zip-cache-v1';
const ASSETS = [
    '/',
    '/static/css/style.css',
    '/static/js/mobile.js',
    '/static/images/logo.png'
];

self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
)});