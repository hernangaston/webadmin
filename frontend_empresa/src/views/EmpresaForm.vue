<template>
<div class="container">
  <div class="empresas">
    <h1 v-if="empresa.id!=null">Editar empresa</h1>
    <h1 v-else>Ingresar empresa</h1>
    <form action="">
        <p>
        <label for="">Nombre: </label>
        <input type="text" v-model="empresa.nombre">
        </p>
        <p>
        <label for="">Cuit: </label>
        <input type="text" v-model="empresa.cuit">
        </p>
        <p>
        <select name="" id="" v-model="empresa.user">
            <option v-for="user in users" :value="user.id">{{ user.nombre }}</option>
        </select>
        </p>
        <button v-if="empresa.id!=null" @click.prevent="guardarDatos">Modificar</button>
        <button v-else @click.prevent="guardarDatos">Guardar</button>
    </form>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'empresa-crear',
    mounted() {
        var id = this.$route.params.id;

        if(id!=null){
            axios.get('http://localhost:8000/api/empresas/'+ id)
            .then((response) => {
                this.empresa = response.data;
            })
        }

        axios.get('http://localhost:8000/api/users/')
        .then((response) => {
            this.users = response.data;
        })
        .catch((error) => {
            console.log(error);
        })
    },
    data () {
        return {
            users: [],
            errors: [],
            empresa: {
                nombre: '',
                cuit: '',
                user: null
            }
        }
    },
    methods: {
        guardarDatos(){
            var router = this.$router;

            if(this.empresa.id!=null){
                axios.put('http://localhost:8000/api/empresas/'+this.empresa.id+'/', this.empresa)
                .then((response) => {
                    if(response.status === 200){
                        console.log(response.statusText);
                        router.push('/empresas');
                    }else{
                        console.log("Error al editar");
                    }
                })
                .catch((error) => {
                    console.log(error);
                })

            }else{
                axios.post('http://localhost:8000/api/empresas/', this.empresa)
                .then((response) => {
                    if(response.status === 201){
                        console.log(response.statusText);
                        router.push('/empresas');
                    }else{
                        console.log("Error al crear");
                    }
                })
                .catch((error) => {
                    console.log(error);
                })
            }
        }
    }
}

</script>

<style>

</style>
