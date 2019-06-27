<template>
    <div class="mt-5">
        <h2>Listado de cartas de porte</h2>        
        <b-row>
            <b-col cols="6">
                <h3>No conformes</h3>
                <cartas-list :cartas="noconforme"></cartas-list>               
            </b-col>
            <b-col cols="6">
                <h3>Conformes</h3>
                <cartas-list :cartas="conforme"></cartas-list>
            </b-col>            
        </b-row>
    </div>
</template>

<script>
    import { mapActions, mapGetters } from 'vuex';
    import CartasList from '@/components/CartasList';

    export default {
        components: {
            CartasList
        },
        mounted () {
            return this.fetchCartas()
        },
        methods: {
            ...mapActions('cartas', ['fetchCartas'])
        },
        computed: {
            ...mapGetters('cartas', ['conforme', 'noconforme'])
        }
    }
</script>