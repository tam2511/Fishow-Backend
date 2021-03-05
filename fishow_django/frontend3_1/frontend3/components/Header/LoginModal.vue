<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">Авторизация</header>
      <section class="modal-card-body">
        <div class="field">
          <b-field
            label="Почта"
            :type="{ 'is-danger': error.email }"
            :message="error.email"
          >
            <b-input
              v-model="login.email"
              type="email"
              value=" "
              maxlength="30"
              @blur="error.email = null"
            >
            </b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field
            label="Пароль"
            :type="{ 'is-danger': error.password }"
            :message="error.password"
          >
            <b-input
              v-model="login.password"
              type="password"
              value="iwantmytreasure"
              password-reveal
              @blur="error.password = null"
            >
            </b-input>
          </b-field>
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button
              class="button is-link is-success"
              @keypress.enter="temlLogin"
              @click="temlLogin"
            >
              Подтвердить
            </button>
          </div>
          <div class="control">
            <button
              class="button is-link is-light"
              @keypress.esc="toggle"
              @click="toggle"
            >
              Отмена
            </button>
          </div>
          <div class="control">
            <button
              class="button is-primary"
              @keypress.esc="toggle"
              @click="toggleReg"
            >
              Регистрация
            </button>
          </div>
        </div>
      </section>
    </div>
    <button
      class="modal-close is-large"
      aria-label="close"
      @click="toggle"
    ></button>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Http from '~/services/Http'
import errors from '~/components/Header/errors'
export default {
  data() {
    return {
      login: {
        email: '',
        password: '',
      },
      error: {
        email: null,
        password: null,
      },
    }
  },
  methods: {
    async temlLogin() {
      try {
        const payload = {
          email: this.login.email,
          password: this.login.password,
        }
        const resp = await Http.login(payload)
        this.$auth.setToken('local', 'Bearer ' + resp.data.access_token)
        this.$auth.setRefreshToken('local', resp.data.refresh_token)
        this.$axios.setHeader()
        this.$auth.ctx.app.$axios.setHeader(
          'Authorization',
          'Bearer ' + resp.data.access_token
        )
        this.$axios.get('/dj-rest-auth/user/').then((resp) => {
          this.$auth.setUser(resp.data)
        })
        this.toggle()
        window.location.reload()
      } catch (e) {
        console.error(e)
        if (e.response.data.password) {
          const response = e.response.data.password[0]
          this.error.password = errors[response]
        }
        if (e.response.data.non_field_errors) {
          const response = e.response.data.non_field_errors[0]
          this.error.email = errors[response]
        }
      }
    },
    ...mapMutations('login', {
      toggle: 'TOGGLE_LOGIN',
      toggleReg: 'TOGGLE_REG',
    }),
  },
}
</script>

<style scoped></style>
