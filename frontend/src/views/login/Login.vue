<template>
    <div>
        <b-container fluid>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                <b-form-group id="input-group-1" label="Your Name:" label-for="input-1">    
                    <b-form-input id="input-1" v-model="form.email" type="email" placeholder="Enter your email">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                    <b-form-input id="input-2" v-model="form.password" type="password" placeholder="Enter your password">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="input-group-3" label="Password Confirmation:" label-for="input-3">
                    <b-form-input id="input-3" v-model="form.passwordConfirmation" type="password" placeholder="Confirm your password">
                    </b-form-input>
                </b-form-group>

                <b-form-group>
                    <b-button type="submit" variant="primary">Submit</b-button>
                    <b-button type="reset" variant="danger">Reset</b-button>
                </b-form-group>
            </b-form>
            
            <b-card>
                {{ form }}
            </b-card>
        </b-container>       
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                    email: '',
                    password: '',
                    passwordConfirmation:''
            },
            show: true
        }
    },
    methods: {
            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this.form))
            },
            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.form.email = ''
                this.form.password = ''
                this.form.passwordConfirmation = ''
                // Trick to reset/clear native browser form validation state
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                })
            }
        }
    }
</script>
