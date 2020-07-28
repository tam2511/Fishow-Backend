<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">Регистрация</header>
      <section class="modal-card-body">
        <div class="field">
          <b-field
            label="Логин"
            :type="{
              'is-danger': error.username,
              'is-success': !error.username && reg.username,
            }"
            :message="error.username"
          >
            <b-input
              v-model="reg.username"
              value=" "
              maxlength="30"
              @blur="error.username = null"
            ></b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field
            label="Почта"
            :type="{
              'is-danger': error.email,
              'is-success': !error.email && reg.email,
            }"
            :message="error.email"
          >
            <b-input
              v-model="reg.email"
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
            :type="{ 'is-danger': error.password1 }"
            :message="error.password1"
          >
            <b-input
              v-model="reg.password1"
              type="password"
              value=" "
              password-reveal
              @blur="error.password1 = null"
            >
            </b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field
            :type="{ 'is-danger': error.password2 }"
            :message="error.password2"
          >
            <b-input
              v-model="reg.password2"
              type="password"
              value=" "
              password-reveal
              @blur="error.password2 = null"
            >
            </b-input>
          </b-field>
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link" @click="registration">
              Подтвердить
            </button>
          </div>
          <div class="control">
            <button class="button is-link is-light" @click="toggle">
              Отмена
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
export default {
  data() {
    return {
      reg: {
        email: '',
        username: '',
        password1: '',
        password2: '',
      },
      error: {
        email: null,
        username: null,
        password1: null,
        password2: null,
      },
    }
  },
  methods: {
    async registration() {
      try {
        const data = this.reg
        // console.log('data = ', data)
        await this.$axios.$post('/rest-auth/registration/', data)
        this.toggle()
        this.success()
      } catch (e) {
        console.log('error = ', e.response)
        if (e.response.data.email) {
          this.error.email = this.message(e.response.data.email[0])
        }
        if (e.response.data.username) {
          this.error.login = this.message(e.response.data.username[0])
        }
        if (e.response.data.password1) {
          this.error.password1 = this.message(e.response.data.password1[0])
        }
        if (e.response.data.password2) {
          this.error.password2 = this.message(e.response.data.password2[0])
        }
      }
    },
    success() {
      this.$buefy.notification.open({
        message: 'Регистрация прошла успешна, письмо отправлено!',
        type: 'is-success',
        duration: 9000,
      })
    },
    message(data) {
      switch (data) {
        case 'This field may not be blank.':
          return 'Это поле не может быть пустым'
        case 'A user is already registered with this e-mail address.':
          return 'Это электронная почта уже используется'
        case 'This password is too short. It must contain at least 8 characters.':
          return 'Пароль слишком короткий, необходимо минимум 8 символов'
        case 'A user with that username already exists.':
          return 'Пользователь с таким логином уже зарегистрирован'
      }
    },
    ...mapMutations('login', { toggle: 'TOGGLE_REG' }),
  },
}
</script>

<style scoped></style>
