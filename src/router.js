import Vue from 'vue';
import Router from 'vue-router';
import Cartas from './views/Cartas.vue'
import CartaCreate from './views/CartaCreate.vue'
import CartaUpdate from './views/CartaUpdate.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/cartas'
    },
    {
      path: '/cartas',
      name: 'cartas',
      component: Cartas
    },
    {
      path: '/cartas/create',
      name: 'cartas-create',
      component: CartaCreate
    },
    {
      path: '/cartas/:id/update',
      name: 'cartas-update',
      component: CartaUpdate
    }
  ],
  mode: 'history'
})
