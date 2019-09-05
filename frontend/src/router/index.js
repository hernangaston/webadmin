import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Cartas from '@/views/cartas/Cartas'
import CartaCreate from '@/views/cartas/CartaCreate'

import Login from '@/views/login/Login'
import Registro from '@/views/registro/Registro'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cartas',
      name: 'lista',
      component: Cartas
    },
    {
      path: '/cartas/create',
      name: 'create',
      component: CartaCreate
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registro',
      name: 'registro',
      component: Registro
    }
  ]
})
