import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/empresas'
    },
    {
      path: '/empresas',
      name: 'empresas',
      component: () => import(/* webpackChunkName: "empresas" */ './views/Empresas.vue')
    },
    {
      path: '/empresas/create',
      name: 'empresas-create',
      component: () => import(/* webpackChunkName: "crear" */ './views/EmpresaCreate.vue')
    },
    {
      path: '/empresas/:id/edit',
      name: 'empresa-edit',
      component: () => import(/* webpackChunkName: "update" */ './views/EmpresaUpdate.vue')
    }
  ]
})
