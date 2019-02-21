<template>
    <b-nav>
        <b-nav-item exact to="/secret">Pagina secreta</b-nav-item>
        <b-nav-item exact to="/secret/notes">Notas secretas</b-nav-item>
        <b-nav-item @click="_logout">Cerrar sesion</b-nav-item>
    </b-nav>
</template>

<script>
import {mapMutations} from 'vuex';
export default {
    methods: {
        ...mapMutations('auth', ['logout']),
        _logout() {
            this.logout();
            this.$router.push('/login');
        }
    }
}
</script>