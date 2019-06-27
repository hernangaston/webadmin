<template>
  <div id="app">    
    <b-container>
      <b-nav tabs>
        <b-nav-item exact to="/cartas">Listado de cartas de porte</b-nav-item>
        <b-nav-item exact to="/cartas/create">Crear nueva carta de porte</b-nav-item>
      </b-nav>
      <router-view/>
    </b-container>
   <form @submit.prevent="submitCp">
     <label for="">Fecha</label>
     <input type="date" v-model="formData.fecha">
     <br />
     <label for="">Numero cp</label>
     <input type="text" v-model="formData.numero">
     <br />
     <button type="submit">Submit</button>
     <h1>{{ msg }}</h1>
   </form>
    <br />
    <h1>Todas las cp</h1>
    <ol>
      <li v-for="(cp, index) in cps" :key="index"> Fecha: {{ cp.fecha }} - Numero: {{ cp.numero }}</li>
    </ol>  
  </div>
</template>

<script>
import api from '../api/index'
export default {
  name: 'app',
  data () {
    return {
      msg: '',
      formData: {
        numero: '',
        fecha: ''
      },
      cps: []
    }
  },
  methods: {
    submitCp(){
      api.fetchCartas('post', null, this.formData).then(
        res => { this.msg = "Saved"}
      ).catch( err => {
        this.msg = err.response
      })
    },
    fetchCp(){
      api.fetchCartas('get', null, null).then(
        res => { 
          this.cps = res.data;
          //check if exists data
          console.log(this.cps);
        }
      ).catch( err => {
        console.log(err);
      })
    }
  },
  mounted () {
    //fetch all notes once the component is mounted
    this.fetchCp();
  }
}
</script>

<style>
#app {
  margin: 50px;
  text-align: center;
  font-size: xx-large;
}
</style>