import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

const baseURL = 'http://localhost:8000/'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

axios.defaults.baseURL = baseURL

Vue.use(VueAxios, axios)
