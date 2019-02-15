import Vue from 'vue';

export async function traerUsers ({commit}) {
    try {
        const {data} = await Vue.axios({
            url: '/users/'
        })        
        //si creo una const response tengo que agregar la linea de abajo sino mandon un const {data}
        //const payload = response && response.data        
        commit('users/setUsers', data, { root: true})
    } catch (error) {
        commit('usersError', error.message)
    } finally {
        console.log("La peticion traer users ha finalizado");
    }
}
