import Vue from 'vue';
import Cookies from 'js-cookie';

export async function fetchCartas({ commit }){
    try {
        const response = await Vue.axios({
            url:'cp/api/cartas/'
        });        
        const payload = response && response.data;
        commit('cartas/setCartas', payload, { root: true });
    } catch (error) {
        commit('cartasError', error.message);
    }finally{
        console.log("la peticion para obtener las cps ha finalizado");
    }
}

export async function addCarta({ commit }, carta){
    let full =  carta.fecha.getFullYear().toString() + 
    "-" + (carta.fecha.getMonth()+1).toString() + "-"
    + carta.fecha.getDate().toString();  
    carta.fetcha = full;  
    var csrftoken = Cookies.get("csrftoken");
    
    try {
       await Vue.axios({
            method: 'POST',
            url:'cp/api/cartas/',
            data:{
                'fecha': full,
                'numero': carta.numero,
                'ctg': carta.ctg,
                'renspa': carta.renspa,
                'conforme': carta.conforme,
                'intermediario': carta.intermediario,
                'corredor_comprador': carta.corredor_comprador,
                'mercado_a_termino': carta.mercado_a_termino,
                'corredor_vendedor': carta.corredor_vendedor,
                'entregador': carta.entregador,
                'destinatario': carta.destinatario,
                'destino': carta.destino,
                'intermediario_flete': carta.intermediario_flete,
                'transportista': carta.transportista,
                'chofer': carta.chofer,
                'grano': carta.grano,
                'tipo': carta.tipo,
                'cosecha': carta.cosecha,
                'contrato': carta.contrato,
                'pesada_en_destino': carta.pesada_en_destino,
                'kgs_estimados': carta.kgs_estimados,
                'declaracion_calidad': carta.declaracion_calidad,
                'condicional': carta.condicional,
                'peso_bruto': carta.peso_bruto,
                'peso_tara': carta.peso_tara,
                'peso_neto': carta.peso_neto,
                'observaciones': carta.observaciones,
                'direccion_procedencia': carta.direccion_procedencia,
                'localidad_procedencia': carta.localidad_procedencia,
                'provincia_procedencia': carta.provincia_procedencia,
                'kilometros': carta.kilometros,
                'tarifa': carta.tarifa,
                'tarifa_referencia': carta.tarifa,
                'declaracion_juarada_nombre': carta.declaracion_juarada_nombre,
                'declaracion_juarada_dni': carta.declaracion_juarada_dni,
             }
        });
    } catch (error) {        
        commit('cartasError', error.message);
    }finally{
        console.log("la peticion para crear una carta ha finalizado");
    }
}

export async function updateCarta({ commit }, carta){
    try {
        let full =  carta.fecha.getFullYear().toString() + "-" + (carta.fecha.getMonth()+1).toString() + "-" + carta.fecha.getDate().toString();
        await Vue.axios({
            method: 'PUT',
            url:`cp/api/cartas/${carta.id}/`,
            data: {
                'fecha': full,
                'numero': carta.numero,
                'ctg': carta.ctg,
                'renspa': carta.renspa,
                'conforme': carta.conforme,
                'intermediario': carta.intermediario,
                'corredor_comprador': carta.corredor_comprador,
                'mercado_a_termino': carta.mercado_a_termino,
                'corredor_vendedor': carta.corredor_vendedor,
                'entregador': carta.entregador,
                'destinatario': carta.destinatario,
                'destino': carta.destino,
                'intermediario_flete': carta.intermediario_flete,
                'transportista': carta.transportista,
                'chofer': carta.chofer,
                'grano': carta.grano,
                'tipo': carta.tipo,
                'cosecha': carta.cosecha,
                'contrato': carta.contrato,
                'pesada_en_destino': carta.pesada_en_destino,
                'kgs_estimados': carta.kgs_estimados,
                'declaracion_calidad': carta.declaracion_calidad,
                'condicional': carta.condicional,
                'peso_bruto': carta.peso_bruto,
                'peso_tara': carta.peso_tara,
                'peso_neto': carta.peso_neto,
                'observaciones': carta.observaciones,
                'direccion_procedencia': carta.direccion_procedencia,
                'localidad_procedencia': carta.localidad_procedencia,
                'provincia_procedencia': carta.provincia_procedencia,
                'kilometros': carta.kilometros,
                'tarifa': carta.tarifa,
                'tarifa_referencia': carta.tarifa,
                'declaracion_juarada_nombre': carta.declaracion_juarada_nombre,
                'declaracion_juarada_dni': carta.declaracion_juarada_dni
            }
        })
    } catch (error) {
        commit('cartasError', error.message);
    }finally{
        console.log("la peticion para actualizar una carta ha finalizado");
    }
}

export async function removeCarta({ commit, dispatch }, id){
    try {
        await Vue.axios({
            method: 'DELETE',
            url:`cp/api/cartas/${id}`,
        })
        dispatch('fetchCartas')
    } catch (error) {
        commit('cartasError', error.message);
    }finally{
        console.log("la peticion para eliminar una cp ha finalizado");
    }
}
