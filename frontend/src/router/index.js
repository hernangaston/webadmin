import Vue from 'vue'
import Router from 'vue-router'
import Cartas from '@/views/Cartas'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '',
      component: Cartas
    }
  ]
})
