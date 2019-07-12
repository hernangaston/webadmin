<template>
    <div>
        <carta-form :carta="carta" @processCarta="addCarta"></carta-form>
    </div>
</template>

<script>

import CartaForm from '@/components/cartas/CartaForm'
import Vue from 'vue'

export default {
    components: {
        CartaForm
    },
    data () {
        return {
            carta: {
                numero: '',
                fecha: '',
                intermediario: '',
                remitente_comercial: '',
                ctg: '',
                renspa: '',
                conforme: false,
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
        addCarta () {
            console.log('Add carta')
            let full =  this.carta.fecha.getFullYear().toString() + 
            "-" + (this.carta.fecha.getMonth()+1).toString() + "-"
            + this.carta.fecha.getDate().toString();  
            
            var data = new FormData()
            data.append('numero', this.carta.numero)
            data.append('fecha', full)
            data.append('ctg', this.carta.ctg)
            data.append('renspa', this.carta.renspa)
            data.append('conforme', this.carta.conforme)
            data.append('intermediario', this.carta.intermediario)
            data.append('remitente_comercial', this.carta.remitente_comercial)
            data.append('corredor_comprador', this.carta.corredor_comprador)
            data.append('mercado_a_termino', this.carta.mercado_a_termino)
            data.append('corredor_vendedor', this.carta.corredor_vendedor)
            data.append('entregador', this.carta.entregador)
            data.append('destinatario', this.carta.destinatario)
            data.append('destino', this.carta.destino)
            data.append('intermediario_flete', this.carta.intermediario_flete)
            data.append('transportista', this.carta.transportista)
            data.append('chofer', this.carta.chofer)
            data.append('grano', this.carta.grano)
            data.append('tipo', this.carta.tipo)
            data.append('cosecha', this.carta.cosecha)
            data.append('contrato', this.carta.contrato)
            data.append('pesada_en_destino', this.carta.pesada_en_destino)
            data.append('kgs_estimados', this.carta.kgs_estimados)
            data.append('declaracion_calidad', this.carta.declaracion_calidad)
            data.append('condicional', this.carta.condicional)
            data.append('peso_bruto', this.carta.peso_bruto)
            data.append('peso_tara', this.carta.peso_tara)
            data.append('peso_neto', this.carta.peso_neto)
            data.append('observaciones', this.carta.observaciones)
            data.append('direccion_procedencia', this.carta.direccion_procedencia)
            data.append('localidad_procedencia', this.carta.localidad_procedencia)
            data.append('provincia_procedencia', this.carta.provincia_procedencia)
            data.append('kilometros', this.carta.kilometros)
            data.append('tarifa', this.carta.tarifa)
            data.append('tarifa_referencia', this.carta.tarifa_referencia)
            data.append('declaracion_juarada_nombre', this.carta.declaracion_juarada_nombre)
            data.append('declaracion_juarada_dni', this.carta.declaracion_juarada_dni)
            data.append('docfile', this.carta.docfile)
            Vue.axios({
                method: 'POST',
                url: 'cp/fileupload/' + this.carta.docfile.name,
                data
            })
            .then( res => {
                console.log(res.status)
                this.$router.push('/')
            })
            .catch(error => console.log(error))
        }
    }
}
</script>
