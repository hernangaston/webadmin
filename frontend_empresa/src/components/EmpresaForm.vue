<template>
    <b-form @submit.prevent="$emit('processEmpresa', empresa)">
        <b-form-group id="empresa" label="Empresa" label-for="empresa">
            <b-form-input class="mb-3"
                autocomplete="off"
                id="empresa"
                v-model="empresa.nombre"
                :state="!$v.empresa.nombre.$invalid"
                placeholder="Nombre de la empresa"
                @input="$v.empresa.$touch">
            </b-form-input>
            <b-form-invalid-feedback id="empresaInfo" v-if="$v.empresa.$dirty">
                Este campo es requerido y debe tener una logitud minima de 4
            </b-form-invalid-feedback>
            <b-form-input class="mb-3"
                autocomplete="off"
                id="empresa"
                v-model="empresa.cuit"
                :state="!$v.empresa.cuit.$invalid"
                placeholder="Cuit de la empresa"
                @input="$v.empresa.$touch">
            </b-form-input>
            <b-form-invalid-feedback id="empresaInfo" v-if="$v.empresa.$dirty">
                Este campo es requerido y debe tener una logitud minima de 13
            </b-form-invalid-feedback>
        </b-form-group>
        <b-button type="submit" variant="primary" :disabled="$v.empresa.$invalid">
            {{ empresaSubmit }}
        </b-button>
    </b-form>
</template>

<script>
import { validationMixin } from 'vuelidate';
import { required, minLength } from 'vuelidate/lib/validators'
export default {
    mixins: [validationMixin],
    props: {
        empresa: {
            type: Object,
            required: true
        },
        empresaSubmit: {
            type: String,
            default: 'Crear Empresa'
        }
    },
    validations: {
        empresa: {
            nombre: {
                required, minLength: minLength(4)
            },
            cuit: {
                required, minLength: minLength(11)
            }
        }
    }
}

</script>

<style>

</style>
