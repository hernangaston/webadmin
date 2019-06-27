export function setCartas(state, cartas){
    state.cartas = cartas;
}

export function setCarta(state, carta){
    state.selectedCarta = carta;
}

//para cambiar una estado de cartas de porte por ejemplo (pagadas o pendientes de pago)
//la parte de abajo es a modo de ejemplo tengo que probar
/*export function updateCartaDePorteStatus(state, payload){
    //primero buscamos la carta de porte
    const cartadeporte = state.cartas.find(cp => cp.id === payload.id)
    //si esta la carta de porte 
    if (cartadeporte) {
        //le decimos que si esta paga pase a impaga o si no esta pagada pase a pagada
        cartadeporte.pagada = !cartadeporte.pagada;
    }
}*/

export function cartasError(state, payload){
    state.error = true;
    state.errorMessage = payload;
    state.cartas = [];
}