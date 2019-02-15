<template>
    <empresa-form
        :empresa="selectedEmpresa"
        @processEmpresa="updateEmpresa"
        empresaSubmit="Actualizar Empresa"
        >
        </empresa-form>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import EmpresaForm from'@/components/EmpresaForm';
export default {
    components:{
        EmpresaForm
    },
    data(){
        return {
            empresa: null
        }
    },
    computed: {
        ...mapState('empresas', ['selectedEmpresa'])
    },
    methods: {
        ...mapActions({
            _updateEmpresa: 'empresas/updateEmpresa'
        }),
        updateEmpresa(empresa){
            this._updateEmpresa(empresa)
            .then(() => {
                this.$router.push('/empresas')
            })
        }
    }
}
</script>