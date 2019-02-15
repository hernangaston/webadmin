<template>
    <div v-if="empresas.length">
        <empresa-item v-for="empresa in empresas" :key="empresa.id" :empresa="empresa"></empresa-item>
    </div>
    <b-alert show variant="info" v-else>No hay empresas</b-alert>
</template>

<script>
import EmpresaItem from './EmpresaItem'

export default {
    components: {
        EmpresaItem
    },
    props: {
        empresas:{
            type: Array,
            required: true
        }
    }
}
</script>