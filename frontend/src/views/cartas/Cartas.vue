<template>
  <div>
    <br>
    <h2 class="text-center">Listado de cartas de porte</h2>
    <br>
    <cartas-list :cartas="cartas"></cartas-list>
  </div>
</template>

<script>
import CartasList from '@/components/cartas/CartasList'
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
