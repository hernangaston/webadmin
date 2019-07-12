import Vue from 'vue'
import Router from 'vue-router'
import Cartas from '@/views/cartas/Cartas'
import CartaCreate from '@/views/cartas/CartaCreate'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/cartas',
      name: '',
      component: Cartas
    },
    {
      path: '/cartas/create',
      name: 'create',
      component: CartaCreate
    }
  ]
})
