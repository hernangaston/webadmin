<template>
    <div>
        <b-row class="mb-3">
            <b-col cols=2>
                {{ empresa.id }})
            </b-col>
            <b-col cols=3>
                {{ empresa.nombre }}
            </b-col>
            <b-col cols=3>
                {{ empresa.cuit }}
            </b-col>
            
            <b-col cols=2>
                <b-button variant="primary" @click="goToUpdateEmpresa">Editar</b-button>
            </b-col>
            <b-col cols=2>
                <b-button class="ml-2" variant="danger" @click="deleteEmpresa">Eliminar</b-button>
            </b-col>
        </b-row>        
    </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';

export default {
    props: {
        empresa: {
            type: Object,
            required: true
        }
    },
    methods: {
        ...mapActions({
            _deleteEmpresa: 'empresas/deleteEmpresa'
        }),
        ...mapMutations('empresas', ['setEmpresa']),
        goToUpdateEmpresa(){
            this.setEmpresa(this.empresa);
            this.$router.push({
                name: 'empresa-edit',
                params: {id: this.empresa.id}
            })
        },
        deleteEmpresa(){
            this._deleteEmpresa(this.empresa.id);
        }
    }
}
</script>