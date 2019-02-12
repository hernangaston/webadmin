<template>
<div class="container">
  <div class="empresas">
    <h1>Listado de empresas</h1>   
    <router-link :to="{name:'empresa-crear'}">Nueva empresa</router-link>
    <table class="table table-striped">
        <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">Usuario</th>
            <th scope="col">Nombre</th>
            <th scope="col">Cuit</th>
            <th scope="col">Opciones</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="empresa in empresas">
                <th scope="row">{{ empresa.id }}</th>
                <td>{{ empresa.nombreUser }}</td>
                <td>{{ empresa.nombre }}</td>
                <td>{{ empresa.cuit }}</td>
                <td>
                    <router-link :to="{name:'empresa-editar', params: {id: empresa.id}}">Editar</router-link>
                </td>
                <td>
                    <a class="btn btn-danger" @click.prevent="eliminarEmpresa(empresa.id)" href="">Eliminar</a>
                </td>
            </tr>
        </tbody>
    </table>     
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'empresas',
    mounted() {
        this.cargarEmpresas();
    },
    data () {
        return {
            empresas: []
        }
    },
    methods: {
        cargarEmpresas(){
             axios.get('http://localhost:8000/api/empresas/')
            .then((response) => {
                this.empresas = response.data;
            })
            .catch((error) => {
                console.log(error);
            })
        },
        eliminarEmpresa(id){
            var consulta = window.confirm("Seguro que desea realizar esta operacion??")
            if(consulta){

            }
            axios.delete('http://localhost:8000/api/empresas/'+id+'/')
            .then((response) => {
                if(response.status === 204){
                    console.log("EMPRESA ELIMINADA");
                    this.cargarEmpresas();
                }
            })
        }
    },
}

</script>

<style>

</style>
