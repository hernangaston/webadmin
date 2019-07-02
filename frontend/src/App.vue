<template>
  <b-container>
      <b-nav tabs>
        <b-nav-item exact to="/">Home</b-nav-item>
        <b-nav-item exact to="/cartas">Listado de cartas de porte</b-nav-item>
        <b-nav-item exact to="/cartas/create">Crear nueva carta de porte</b-nav-item>
      </b-nav>
      <router-view/>
  </b-container>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
