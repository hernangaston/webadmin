<template>
    <div>
       <div class="mt-5">
           <b-row>
               <b-col>
                   <h2 class="mb-3">Listado de Empresas</h2>
                   <hr>
                   <empresas-list :empresas="done"></empresas-list>
               </b-col>
           </b-row>
       </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import EmpresasList from '@/components/EmpresasList';

export default {
    components: {
        EmpresasList
    },
    mounted(){
        this.traerEmpresas()
    },
    methods:{
        ...mapActions('empresas', ['traerEmpresas'])
    },
    computed: {
        ...mapGetters('empresas', ['done'])
    }
}
</script>

<style>

</style>
