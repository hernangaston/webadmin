<template>
  <div id="app">
    <loading :active.sync="loading"></loading>
    <b-container>
      <navigation-gest v-if="!isLogged"></navigation-gest>
      <navigation-logged v-else ></navigation-logged>
      <router-view/>
    </b-container>
  </div>
</template>

<script>

import NavigationLogged from '@/components/Navigations/Logged';
import NavigationGest from '@/components/Navigations/Gest';
import {mapState} from 'vuex';
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

export default {
  components: {
    NavigationLogged, NavigationGest, Loading
  },
  computed:{
    ...mapState('auth', ['isLogged']),
    ...mapState(['loading'])
  }
}

</script>