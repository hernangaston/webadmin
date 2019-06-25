import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

const baseURL = 'http://localhost:8000/';
axios.defaults.baseURL = baseURL;

Vue.use(VueAxios, axios);
