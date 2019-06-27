import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/cartas'
    }/*,
    {
      path: '/cartas',
      name: 'cartas',
      component: () => import('./views/Cartas.vue')
    },
    {
      path: '/cartas/create',
      name: 'cartas-create',
      component: () => import( './views/CartaCreate.vue')
    },
    {
      path: '/cartas/:id/update',
      name: 'cartas-update',
      component: () => import('./views/CartaUpdate.vue')
    }*/
  ],
  mode: 'history'
})
