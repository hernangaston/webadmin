<template>
  <li>
    <b-row class="mb-2">
      <b-col cols="2">{{ carta.fecha }}</b-col>
      <b-col cols="2">{{ carta.numero }}</b-col>
      <b-col cols="1" class="ml-1">{{ carta.conforme }}</b-col>
      <b-col>
        <b-button variant="primary" @click="goToUpdateCarta">Editar</b-button>
        <b-button variant="warning" class="ml-2" @click="removeCarta(carta.id)">Eliminar</b-button>
        <b-link variant="secondary"
          :href="'http://localhost:8000/cp/cartaslist/generarpdf/'+ carta.id"
          class="ml-2"
        >Download</b-link>
      </b-col>
    </b-row>
  </li>
</template>

<script>
import Vue from 'vue'
export default {
  props: {
    carta: {
      type: Object,
      required: true
    }
  },
  methods: {
    removeCarta (id) {
      alert('Eliminar cp' + id);
      Vue.axios({ 
        method: 'DELETE',
        url: 'cp/api/cartas/'+ id })
        .then(res => {
          console.log(res.status);
          this.$router.push('/cartas');
        });
    }
  } 
}
</script>
