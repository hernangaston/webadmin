<template>
  <div id="app">
    <b-container>
      <b-nav tabs>
        <b-nav-item exact to="/empresas">Listado de empresas</b-nav-item>
        <b-nav-item exact to="/empresas/create">Crear Empresa</b-nav-item>
      </b-nav>    
     <router-view/>
    </b-container>
  </div>
</template>