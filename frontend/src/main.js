import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';


import router from './router';
import store from './store';

//require('./plugins');

new Vue({
  el: '#app',
  router,
  store,
  beforeCreate(){
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  render: h => h(App)
})
