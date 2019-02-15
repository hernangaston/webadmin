export function setEmpresas (state, empresas) {
    state.empresas = empresas;
}

export function setEmpresa (state, empresa) {
    state.selectedEmpresa = empresa;
}

export function empresasError (state, pyload) {
    state.error = true;
    state.errorMessage = payload;
    state.empresas = [];
}