import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';
import localForage from "localforage";


import empresas from './modules/empresas';

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: localForage,
  modules: ['empresas'] //le digo el/los modulos que quiero guardar por defecto los guarda a todos
})


export default new Vuex.Store({
  state: {},
  modules: {
    empresas
  },
  plugins: [vuexLocal.plugin]
})
