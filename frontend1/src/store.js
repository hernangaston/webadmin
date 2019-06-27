import Vue from 'vue';
import Vuex from 'vuex';
import cartas from './modules/cartas';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    cartas
  }
});
