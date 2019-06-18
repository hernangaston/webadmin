<template>
    <div>
        <carta-form :carta="carta" @processCarta="addCarta"></carta-form>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
import CartaForm from '@/components/CartaForm';

export default {
    components: {
        CartaForm
    },
    data () {
        return {
            carta: {
                numero: '',
                conforme: false,
                fecha: '',
                intermediario: null,
                ctg: '',
                renspa: '',
                conforme: false,
                intermediario: '',
                corredor_comprador: '',
                mercado_a_termino: '',
                corredor_vendedor: '',
                entregador: '',
                destinatario: '',
                destino: '',
                intermediario_flete: '',
                transportista: '',
                chofer: '',
                grano: '',
                tipo: '',
                cosecha: '',
                contrato: '',
                pesada_en_destino: false,
                kgs_estimados: false,
                declaracion_calidad: false,
                condicional: false,
                peso_bruto: '',
                peso_tara: '',
                peso_neto: '',
                observaciones: '',
                direccion_procedencia: '',
                localidad_procedencia: '',
                provincia_procedencia: '',
                kilometros: '',
                tarifa: '',
                tarifa_referencia: '',
                declaracion_juarada_nombre: '',
                declaracion_juarada_dni: '',
                docfile: ''
            }
        }
    },
    methods: {
        ...mapActions({
            createCarta: 'cartas/addCarta'
        }),
        addCarta(carta){
            this.createCarta(carta).then(() => {
                this.$router.push('/cartas')
            })
        }
    }
}
</script>