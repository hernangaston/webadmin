<template>
    <div v-if="selectedCarta">
        <carta-form
            :carta="selectedCarta"
            @processCarta="updateCarta"
            cartaSubmit="Actualizar">
        </carta-form>
    </div>
    <div v-else>No hay resultados</div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import CartaForm from '@/components/CartaForm';

export default {
    components: {
        CartaForm
    },
    computed: {
        ...mapState('cartas', ['selectedCarta'])
    },
    methods: {
        ...mapActions({
            _updateCarta: 'cartas/updateCarta'
        }),
        updateCarta(carta){
            this._updateCarta(carta).then(() => {
                this.$router.push('/cartas')
            })
        }
    }
}
</script>