{%load static %}
(function() {
  'use strict';

  var app = {
    isLoading: true,
    visibleCards: {},
    selectedCities: [],
    spinner: document.querySelector('.loader'),
    // cardTemplate: document.querySelector('.cardTemplate'),
    // container: document.querySelector('.main'),
    // addDialog: document.querySelector('.dialog-container'),
    daysOfWeek: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  };


  if (app.isLoading) {
    app.spinner.setAttribute('hidden', true);
    // app.container.removeAttribute('hidden');
    app.isLoading = false;
  }

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
             .register("{% static 'scripts/service-worker.js'%}")
             .then(function() { console.log('Service Worker Registered'); });
  }
})();
