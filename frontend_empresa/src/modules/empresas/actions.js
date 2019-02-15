import Vue from 'vue';

export async function traerEmpresas ({commit}) {
    try {
        const {data} = await Vue.axios({
            url: '/empresas/'
        })        
        //si creo una const response tengo que agregar la linea de abajo sino mandon un const {data}
        //const payload = response && response.data        
        commit('empresas/setEmpresas', data, { root: true})
    } catch (error) {
        commit('empresasError', error.message)
    } finally {
        console.log("La peticion traer empresas ha finalizado");
    }
}

export async function addEmpresa ({commit}, empresa){
    try {
        await Vue.axios({
            method: 'POST',
            url: '/empresas/',
            data: {
                nombre: empresa.nombre,
                cuit: empresa.cuit
            }
        })
    } catch (error) {
        commit('empresasError', error.message)
    } finally {
        console.log("La peticion para crear ha finalizado");
    }
}

export async function updateEmpresa ({commit}, empresa){
    try {
        await Vue.axios({
            method: 'PUT',
            url: `/empresas/${empresa.id}/`,
            data: {
                nombre: empresa.nombre,
                cuit: empresa.cuit
            }
        })
    } catch (error) {
        commit('empresasError', error.message)
    } finally {
        console.log("La peticion actualizar ha finalizado");
    }
}

export async function updateEmpresaStatus ({commit}, empresa){
    try {
        await Vue.axios({
            method: 'PUT',
            url: `/empresas/${empresa.id}/`,
            data: {
                nombre: empresa.nombre,
                cuit: empresa.cuit
            }
        })
    
    } catch (error) {
        commit('empresasError', error.message)
    } finally {
        console.log("La peticion actualizar el estado ha finalizado");
    }
}

export async function deleteEmpresa ({commit, dispatch}, id){
    try {
        await Vue.axios({
            method: 'DELETE',
            url: `/empresas/${id}/`,
        })
        dispatch('traerEmpresas')
    } catch (error) {
        commit('empresasError', error.message)
    } finally {
        console.log("La peticion actualizar el estado ha finalizado");
    }
}