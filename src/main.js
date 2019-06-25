import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

require('./plugins');

axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  components: {
    'django': App
  }
})

/*import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import BootstrapVue from 'bootstrap-vue'
//import store from './store'

Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// font awesome settings
import { library } from '@fortawesome/fontawesome-svg-core'
import {
        faFilePdf,
        faFileImage,
        faFileExcel,
        faFilePowerpoint,
        faFileWord,
        faFileVideo,
        faFileArchive,
        faFileAlt,
        faFile,
        faTrashAlt,
        faUpload,
        faTasks
       } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
            faFilePdf,
            faFileImage,
            faFileExcel,
            faFilePowerpoint,
            faFileWord,
            faFileVideo,
            faFileArchive,
            faFileAlt,
            faFile,
            faTrashAlt,
            faUpload,
            faTasks
          )

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

// axios settings
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

new Vue({
  el: '#app',
  components: {
    'django': App
  }
})*/