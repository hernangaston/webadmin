<template>
    <b-form @submit.prevent="$emit('login')">
        <b-form-group
            label="Username"
            description="Los datos son privados">
            <b-form-input
                type="text"
                autocomplete="off"
                v-model="user.username"
                name="username"
                placeholder="Introduce username"
                ></b-form-input>
            <b-form-invalid-feedback>{{ errors.first('username') }}</b-form-invalid-feedback>
        </b-form-group>        
        <b-form-group
            label="Email"
            description="Los datos son privados">
            <b-form-input
                type="email"
                autocomplete="off"
                v-model="user.email"
                v-validate="'required|email'"
                name="email"
                placeholder="Introduce email"
                ></b-form-input>
            <b-form-invalid-feedback>{{ errors.first('email') }}</b-form-invalid-feedback>
        </b-form-group>
        <b-form-group label="Password">
            <b-form-input
                type="password"
                autocomplete="off"
                v-model="user.password"
                v-validate="'required|min:6'"
                name="password"
                placeholder="Introduce password"
                >
            </b-form-input>
            <b-form-invalid-feedback>{{ errors.first('password') }}</b-form-invalid-feedback>
        </b-form-group>

        <b-button :disabled="errors.any() || ! user.password" type="submit" variant="primary">
            Iniciar sesion 
        </b-button>
    </b-form>
    
</template>

<script>
import validateMixin from '@/mixins/validation'
export default {
    props: {
        mixins: [validateMixin],
        user: {
            type: Object,
            required: true,
            validator: user => {
                if (!user.hasOwnProperty('email') || !user.hasOwnProperty('password')) {
                 console.warn("Usuario no valido");
                 return false;
                }
                return true;
            }
        }
    }
}
</script>