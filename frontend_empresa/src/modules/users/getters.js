export function traer (state){
    return state.users.filter( user => user.nombre )
}