import Vue from 'vue';
import Vuex from 'vuex';

import auth from '@/modules/authentication';
import VuexPersistence from 'vuex-persist';

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  modules: ['auth']
})

export default new Vuex.Store({
  state: {
    loading: false
  },
  mutations: {
    setLoading (state, bool) {
      state.loading = bool;
    }
  },
  modules: {
    auth
  },
  plugins: [vuexLocal.plugin]
})
