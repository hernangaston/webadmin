import Vue from 'vue';
import Vuex from 'vuex';
import empresas from './modules/empresas';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    empresas
  }
})
