import Vue from 'vue';

export async function signIn(context, user) {
    try {
        context.commit('setLoading', true, {root: true})
        await Vue.axios({
            method: 'POST',
            url: '/auth/',
            data: user
        })
        context.commit('setUser', user)
    } catch(e) {
        context.commit('authError', e.message)
    } finally {
        context.commit('setLoading', false, {root: true})
    }
}