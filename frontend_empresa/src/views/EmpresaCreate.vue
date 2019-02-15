<template>
    <empresa-form :empresa="empresa" @processEmpresa="addEmpresa"></empresa-form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import EmpresaForm from'@/components/EmpresaForm';
export default {
    components:{
        EmpresaForm
    },
    data(){
        return {
            empresa: {
                nombre: '',
                cuit: ''
            }
        }
    },
    methods: {
        ...mapActions({
            createEmpresa: 'empresas/addEmpresa'
        }),
        addEmpresa(empresa){
            this.createEmpresa(empresa)
            .then(() => {
                this.$router.push('/empresas')
            })
        }
    }
}
</script>