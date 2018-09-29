// Copyright 2016 Google Inc.
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//      http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

const PRECACHE = 'cv-v1';
const RUNTIME = 'cv-final-1';

const PRECACHE_URLS = [
    '/',
    '/main.html',
    '/info.html',
    '/experiences.html',
    '/passions.html',
    '/assets/css/font-awesome.min.css',
    '/assets/css/ie8.css',
    '/assets/css/ie9.css',
    '/assets/css/main.css',
    '/assets/fonts/FontAwesome.otf',
    '/assets/fonts/fontawesome-webfont.eot',
    '/assets/fonts/fontawesome-webfont.svg',
    '/assets/fonts/fontawesome-webfont.ttf',
    '/assets/fonts/fontawesome-webfont.woff',
    '/assets/fonts/fontawesome-webfont.woff2',
    '/assets/js/ie/html5shiv.js',
    '/assets/js/ie/respond.min.js',
    '/assets/js/jquery.min.js',
    '/assets/js/main.js',
    '/assets/js/skel.min.js',
    '/assets/js/util.js',
    '/assets/sass/ie8.scss',
    '/assets/sass/ie9.scss',
    '/assets/sass/main.scss',
    '/assets/sass/base/_page.scss',
    '/assets/sass/base/_typography.scss',
    '/assets/sass/components/_box.scss',
    '/assets/sass/components/_button.scss',
    '/assets/sass/components/_form.scss',
    '/assets/sass/components/_icon.scss',
    '/assets/sass/components/_image.scss',
    '/assets/sass/components/_list.scss',
    '/assets/sass/components/_section.scss',
    '/assets/sass/components/_table.scss',
    '/assets/sass/components/_tiles.scss',
    '/assets/sass/layout/_footer.scss',
    '/assets/sass/layout/_header.scss',
    '/assets/sass/layout/_main.scss',
    '/assets/sass/layout/_menu.scss',
    '/assets/sass/layout/_wrapper.scss',
    '/assets/sass/libs/_functions.scss',
    '/assets/sass/libs/_mixins.scss',
    '/assets/sass/libs/_skel.scss',
    '/assets/sass/libs/_vars.scss',
    '/images/mindef.jpg',
    '/images/mountain.jpg',
    '/images/obs.jpg',
    '/images/computer.jpg',
    '/images/desk.jpg',
    '/images/epiphone.jpg',
    '/images/piano.jpg',
    '/scripts/app.js',
    '/styles/inline.css'
];

// The install handler takes care of precaching the resources we always need.
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(PRECACHE)
            .then(cache => cache.addAll(PRECACHE_URLS))
            .then(self.skipWaiting())
    );
});

// The activate handler takes care of cleaning up old caches.
self.addEventListener('activate', event => {
    const currentCaches = [PRECACHE, RUNTIME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return cacheNames.filter(cacheName => !currentCaches.includes(cacheName));
        }).then(cachesToDelete => {
            return Promise.all(cachesToDelete.map(cacheToDelete => {
                return caches.delete(cacheToDelete);
            }));
        }).then(() => self.clients.claim())
    );
});

// The fetch handler serves responses for same-origin resources from a cache.
// If no response is found, it populates the runtime cache with the response
// from the network before returning it to the page.
self.addEventListener('fetch', event => {
    // Skip cross-origin requests, like those for Google Analytics.
    if (event.request.url.startsWith(self.location.origin)) {
        event.respondWith(
            caches.match(event.request).then(cachedResponse => {
                if (cachedResponse) {
                    return cachedResponse;
                }

                return caches.open(RUNTIME).then(cache => {
                    return fetch(event.request).then(response => {
                        // Put a copy of the response in the runtime cache.
                        return cache.put(event.request, response.clone()).then(() => {
                            return response;
                        });
                    });
                });
            })
        );
    }
});