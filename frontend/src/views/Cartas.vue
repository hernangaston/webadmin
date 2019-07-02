<template>
    <div class="mt-5">
        <h2>Listado de cartas de porte</h2>        
        <b-row>            
            <h3>Cartas</h3>
            <cartas-list :cartas="cartas"></cartas-list>                 
        </b-row>
    </div>
</template>

<script>
   
    import CartasList from '@/components/CartasList';

    export default {
        components: {
            CartasList
        }
    }
</script>