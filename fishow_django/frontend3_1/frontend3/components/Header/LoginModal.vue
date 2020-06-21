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
          <!--          <p class="control has-icons-left">-->
          <!--            <label for="password">Пароль:</label>-->
          <!--            <input-->
          <!--              id="password"-->
          <!--              v-model="login.password"-->
          <!--              class="input"-->
          <!--              type="password"-->
          <!--              placeholder="Password"-->
          <!--            />-->
          <!--            <span class="icon is-small is-left">-->
          <!--              <i class="fas fa-lock"></i>-->
          <!--            </span>-->
          <!--          </p>-->
          <!--          <p v-if="error.password" class="help is-danger">-->
          <!--            {{ error.password }}-->
          <!--          </p>-->
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button
              class="button is-link"
              @keypress.enter="submit"
              @click="submit"
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
    async submit() {
      try {
        await this.$auth.loginWith('local', {
          data: this.login,
        })
        this.toggle()
        window.location.reload()
        // }
      } catch (e) {
        console.log(e.response.data)
        if (e.response.data.password) {
          const response = e.response.data.password[0]
          console.log('responce = ', response)
          if (response === 'Unable to log in with provided credentials.') {
            this.error.email = 'Неверно введена почта или пароль'
          } else if (response === 'This field may not be blank.') {
            this.error.password = 'Поле не может быть пустым'
          }
        }
        if (e.response.data.non_field_errors) {
          const response = e.response.data.non_field_errors[0]
          if (response === 'Unable to log in with provided credentials.') {
            this.error.email = 'Неверно введена почта или пароль'
          } else if (response === 'This field may not be blank.') {
            this.error.email = 'Поле не может быть пустым'
          } else if (response === 'Must include "email" and "password".') {
            this.error.email = 'Должна быть указана почта и пароль'
          }
        }
      }
    },
    ...mapMutations('login', { toggle: 'TOGGLE_LOGIN' }),
  },
}
</script>

<style scoped></style>
