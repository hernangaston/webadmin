<template>
  <div class="mt-5">
    <h2>Listado de cartas de porte</h2>
    <b-row>
      <h3>Cartas</h3>
      <cartas-list :cartas="cartas"></cartas-list>
    </b-row>
  </div>
</template>

<script>
import CartasList from '@/components/CartasList'
import Vue from 'vue'
export default {
  components: {
    CartasList
  },
  data () {
    return {
      cartas: []
    }
  },
  mounted () {
    Vue.axios({
      url: 'cp/api/cartas/'
    }).then(res => {
      this.cartas = res.data
    }).catch(error => console.log(error))
  }
}
</script>
