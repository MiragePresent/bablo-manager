import Vue from 'vue';
import Vuetify from 'vuetify';

import store from './store';
import router from './config/router';
import { sync } from 'vuex-router-sync';

import Root from './components/Root';
import 'vuetify/dist/vuetify.min.css';

sync(store, router);

Vue.use(Vuetify);

const app = new Vue({
  router,
  store,
  ...Root
});

export {app, router, store};
