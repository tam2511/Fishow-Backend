<template lang="pug">
  transition(name="fade")
    .logmod(v-if="showState")
      .logmod__wrapper
        .logmod__close(@click="close") X
        .logmod__container
          button(@click="stepReg = !stepReg") {{ stepReg ? "Reg" : "Login" }}
          form(v-if="stepReg" @submit.prevent="submit")
            input(type="email" v-model="login.email" placeholder="email")
            input(type="password" v-model="login.password" placeholder="password")
            button Login
          form(v-else @submit.prevent="registration")
            input(type="login" v-model="register.username" placeholder="username")
            input(type="email" v-model="register.email" placeholder="email")
            input(type="password" v-model="register.password1" placeholder="password")
            input(type="password" v-model="register.password2" placeholder="password")
            button Register
          span {{ error }}
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  middleware: 'auth',
  data() {
    return {
      login: {
        email: '',
        password: '',
      },
      register: {
        password1: 'Damir461',
        password2: 'Damir461',
        email: 'sayava9429@whowlft.com',
        username: 'sayava9429',
      },
      note: '',
      password: '',
      email: '',
      show: true,
      stepReg: true,
      error: null,
    }
  },
  computed: {
    ...mapState('user', ['user']),
    ...mapState('login', ['showState']),
  },
  methods: {
    async submit() {
      try {
        await this.$auth.loginWith('local', { data: this.login })
        this.close()
        // }
      } catch (e) {
        this.error = 'Login failed.'
      }
    },
    async registration() {
      try {
        const data = this.register
        console.log('data = ', data)
        const response = await this.$axios.$post(
          '/rest-auth/registration/',
          data
        )
        console.log('response register = ', response)
        console.log('response register = ', response.response)
      } catch (e) {
        console.log('error = ', e.response)
        if (e.response.data.email) {
          this.error = e.response.data.email[0]
        }
        if (e.response.data.username) {
          this.error.push(e.response.data.username[0])
        }
      }
    },
    inputFocus() {
      this.note = ''
    },
    closeModal() {
      console.log('close from login')
      this.$emit('actiLog', false)
    },
    changeStep() {
      this.stepReg = !this.stepReg
    },
    // ...mapActions('login', { sendData: 'sendUserData' }),
    ...mapMutations('login', { close: 'SET_SHOW' }),
    // ...mapActions('login', ['setShow', 'setStep', 'sendUserData']),
  },
}
</script>

<style scoped lang="scss">
body,
input {
  color: var(--color-typo-primary);
  font-size: 1.2rem;
}

fieldset {
  border: none;
}

.note {
  background: var(--background-color-primary);
  padding: 0.75rem 1.5rem;
  box-sizing: border-box;
  position: absolute;
  bottom: 100%;
  width: 100%;
  z-index: 0;
  transition: all 0.2s ease-out;
}

.login {
  color: var(--color-typo-primary);
  z-index: 1;
  position: relative;
  background: var(--background-color-primary);
  padding: 0.75rem 1.5rem 1.5rem;
  box-sizing: border-box;
  margin: auto;
  @media screen and (min-width: 600px) {
    width: 450px;
  }
}

.login--header {
  margin-bottom: 1rem;
  text-align: center;
}

.login--header span {
  font-size: 2rem;
}
.button-default {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 20px 0 20px 0;
  background-color: var(--background-color-brand);
  border-color: var(--background-color-brand);
}
input {
  width: 100%;
  border: none;
  border-bottom: 1px solid;
  text-align: center;
  outline: none;
  padding: 0.5rem 1rem;
  box-sizing: border-box;
  background: none;
}
input:focus + svg > .line--default {
  stroke: #3f51b5;
}

input:focus:invalid + svg > .line--default {
  stroke: #ff5722;
}
.error {
  text-align: center;
  padding: 10px 0 10px 0;
  color: #a30000;
}
</style>
