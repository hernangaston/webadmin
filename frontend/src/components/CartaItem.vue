<template>
    <li>
    <b-row class="mb-2">              
        <b-col>{{ carta }}</b-col>
    </b-row>    
    <b-row class="mb-2">              
        <b-col cols="2">{{ carta.fecha }}</b-col>
        <b-col cols="2">{{ carta.numero }}</b-col>
        <b-col cols="1" class="ml-1">{{ carta.conforme }}</b-col>
        <b-col>
            <b-button
                variant="primary"
                @click="goToUpdateCarta"
            >
            Editar
            </b-button>
            <b-button
                variant="warning"
                class="ml-2"
                @click="removeCarta"
            >
            Eliminar
            </b-button>
            <b-link
                :href="'http://localhost:8000/cp/cartaslist/generarpdf/'+ carta.numero"
                class="ml-2"
            >
            Download
            </b-link>
        </b-col>        
    </b-row>
    </li>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';

export default {
    props: {
        carta: {
            type: Object,
            required: true
        }
    }
    ,
    data () {
       return {
           url: ''
       }
    },
    methods: {
        ...mapActions({
            _removeCarta: 'cartas/removeCarta'
        }),
        ...mapMutations('cartas', ['setCarta']),
        goToUpdateCarta(){
            this.setCarta(this.carta);
            this.$router.push({
                name: 'cartas-update',
                params: {id: this.carta.id}
            })
        },
        removeCarta(){
            this._removeCarta(this.carta.id)
        }
    }
}
</script>