<template>
    <div>
        <div class="text-center text-muted mt-4">
            Iniciar Sesion
        </div>
        <b-alert v-if="error" show variant="danger">
            {{ errorMessage }}
        </b-alert>
        <login-form :user="user" @login="submit"></login-form>
    </div>
    
</template>

<script>
import LoginForm from '@/components/Authentication/LoginForm';
import { mapState, mapActions} from 'vuex';

export default {
    components: {
        LoginForm
    },
    data () {
        return {
            user: {
                username: '',
                email: '',
                password: ''
            }
        }
    },
    computed: {
        ...mapState('auth', ['error', 'errorMessage'])
    },
    methods: {
        ...mapActions('auth', ['signIn']),
        async submit () {
            const validate = await this.$validator.validateAll()
            if(! validate) {
                return false
            }
            await this.signIn(this.user)
            this.$router.push('/secret')

        }
    }
}
</script>