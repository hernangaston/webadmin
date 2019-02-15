export function done (state){
    return state.empresas.filter( empresa => empresa.nombre )
}
