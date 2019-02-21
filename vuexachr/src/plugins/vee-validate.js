import Vue from 'vue';
import VeeValidate, {Validator} from 'vee-validate';
import validatorEs from 'vee-validate/dist/locale/es';//idioma con traducciones

Vue.use(VeeValidate, {
    fieldsBagName: 'veeFields'
});

Validator.localize('es', validatorEs);

Validator.extend('strength_password', {
    getMessage: field => `El campo ${field} debe contener al menos: 1 letra mayusc, 1 letra minusc, 1 numero 
    y un caracter especial (por ej.: ._&? etc.)`,
    validate: value => {
        let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
        return strongRegex.test(value);
    }
})