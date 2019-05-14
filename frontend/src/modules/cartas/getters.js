export function conforme(state){
    return state.cartas.filter(carta => carta.conforme)
}

export function noconforme(state){
    return state.cartas.filter(carta => !carta.conforme)
}

export function listInter(state){
    return state.intermediarios
}