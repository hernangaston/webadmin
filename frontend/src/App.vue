<template>
  <div>
    <b-navbar>
      <b-navbar-brand href="/cp">CP-WEB</b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-item exact to="/">Home</b-nav-item>
        <b-nav-item exact to="/cartas">Listado de cartas de porte</b-nav-item>
        <b-nav-item exact to="/cartas/create">Crear nueva carta de porte</b-nav-item>
        <b-nav-item exact to="/login">Login</b-nav-item>
        <b-nav-item exact to="/registro">Registro</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <br>
    <b-container>
        <router-view/>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
