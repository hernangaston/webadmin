import Vue from 'vue';
import Router from 'vue-router';

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
      component: () => import(/* webpackChunkName: "cartas" */ './views/Cartas.vue')
    },
    {
      path: '/cartas/create',
      name: 'cartas-create',
      component: () => import(/* webpackChunkName: "cartas-create" */ './views/CartaCreate.vue')
    },
    {
      path: '/cartas/:id/update',
      name: 'cartas-update',
      component: () => import(/* webpackChunkName: "cartas-update" */ './views/CartaUpdate.vue')
    }
  ],
  mode: 'history'
})
