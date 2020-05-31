<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">Регистрация</header>
      <section class="modal-card-body">
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <label for="email">Email:</label>
            <input
              id="email"
              v-model="reg.email"
              type="email"
              class="input"
              placeholder="Email"
              @blur="error.email = null"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-check"></i>
            </span>
          </p>
          <p v-if="error.email" class="help is-danger">
            {{ error.email }}
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <label for="username">Username:</label>
            <input
              id="username"
              v-model="reg.username"
              class="input"
              name="username"
              type="text"
              placeholder="Логин"
              @blur="error.login = null"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-check"></i>
            </span>
          </p>
          <p v-if="error.login" class="help is-danger">
            {{ error.login }}
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left">
            <label for="password">Пароль:</label>
            <input
              id="password"
              v-model="reg.password1"
              class="input"
              type="password"
              placeholder="Пароль"
              @blur="error.password1 = null"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-lock"></i>
            </span>
          </p>
          <p v-if="error.password1" class="help is-danger">
            {{ error.password1 }}
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left">
            <input
              v-model="reg.password2"
              class="input"
              type="password"
              placeholder="Повторите пароль"
              @blur="error.password2 = null"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-lock"></i>
            </span>
          </p>
          <p v-if="error.password2" class="help is-danger">
            {{ error.password2 }}
          </p>
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
        login: null,
        password1: null,
        password2: null,
      },
    }
  },
  methods: {
    async registration() {
      try {
        const data = this.reg
        console.log('data = ', data)
        await this.$axios.$post('/rest-auth/registration/', data)
        // console.log('response register = ', response)
        // console.log('response register = ', response.response)
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
