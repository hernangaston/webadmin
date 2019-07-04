<template>
    <div>
        <carta-form :carta="carta" @processCarta="addCarta"></carta-form>
    </div>
</template>

<script>

import CartaForm from '@/components/CartaForm'
import Vue from 'vue'

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
            }
        }
    },
    methods: {
        addCarta () {
            console.log('Add carta')
            let full =  this.carta.fecha.getFullYear().toString() + 
            "-" + (this.carta.fecha.getMonth()+1).toString() + "-"
            + this.carta.fecha.getDate().toString();  
            //var csrftoken = Cookies.get("csrftoken");
            //var fd = new FormData()
            //fd.append('data', this.this.carta)
            Vue.axios({
                method: 'POST',
                url: '/cp/api/cartas/',
                data: {
                    'fecha': full,
                    'numero': this.carta.numero,
                    'ctg': this.carta.ctg,
                    'renspa': this.carta.renspa,
                    'conforme': this.carta.conforme,
                    'intermediario': this.carta.intermediario,
                    'corredor_comprador': this.carta.corredor_comprador,
                    'mercado_a_termino': this.carta.mercado_a_termino,
                    'corredor_vendedor': this.carta.corredor_vendedor,
                    'entregador': this.carta.entregador,
                    'destinatario': this.carta.destinatario,
                    'destino': this.carta.destino,
                    'intermediario_flete': this.carta.intermediario_flete,
                    'transportista': this.carta.transportista,
                    'chofer': this.carta.chofer,
                    'grano': this.carta.grano,
                    'tipo': this.carta.tipo,
                    'cosecha': this.carta.cosecha,
                    'contrato': this.carta.contrato,
                    'pesada_en_destino': this.carta.pesada_en_destino,
                    'kgs_estimados': this.carta.kgs_estimados,
                    'declaracion_calidad': this.carta.declaracion_calidad,
                    'condicional': this.carta.condicional,
                    'peso_bruto': this.carta.peso_bruto,
                    'peso_tara': this.carta.peso_tara,
                    'peso_neto': this.carta.peso_neto,
                    'observaciones': this.carta.observaciones,
                    'direccion_procedencia': this.carta.direccion_procedencia,
                    'localidad_procedencia': this.carta.localidad_procedencia,
                    'provincia_procedencia': this.carta.provincia_procedencia,
                    'kilometros': this.carta.kilometros,
                    'tarifa': this.carta.tarifa,
                    'tarifa_referencia': this.carta.tarifa,
                    'declaracion_juarada_nombre': this.carta.declaracion_juarada_nombre,
                    'declaracion_juarada_dni': this.carta.declaracion_juarada_dni,
                }
            })
            .then( res => console.log(res.status))
            .catch(error => console.log(error))
        }
    }
}
</script>
