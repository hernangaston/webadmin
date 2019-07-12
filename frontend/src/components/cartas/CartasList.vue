<template>  
  <div v-if="cartas.length">
    <ol>
      <carta-item v-for="carta in cartas" :key="carta.id" :carta="carta"></carta-item>
    </ol>
  </div>  
</template>
<script>

import CartaItem from './CartaItem'

export default {
  components: {
    CartaItem
  },
  props: {
    cartas: {
      type: Array,
      required: true
    }
  }
}
</script>
