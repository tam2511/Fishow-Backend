<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">Авторизация</header>
      <section class="modal-card-body">
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <label for="email">Email:</label>
            <input
              id="email"
              v-model="login.email"
              class="input"
              type="email"
              placeholder="Email"
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
          <p class="control has-icons-left">
            <label for="password">Пароль:</label>
            <input
              id="password"
              v-model="login.password"
              class="input"
              type="password"
              placeholder="Password"
            />
            <span class="icon is-small is-left">
              <i class="fas fa-lock"></i>
            </span>
          </p>
          <p v-if="error.password" class="help is-danger">
            {{ error.password }}
          </p>
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
        console.log(e.response)
        if (e.response.data.non_field_errors) {
          if (
            e.response.data.non_field_errors[0] ===
            'Unable to log in with provided credentials.'
          ) {
            this.error.email = 'Неверно введена почта или пароль'
          } else {
            this.error.email = 'Поле не может быть пустым'
            this.error.password = 'Поле не может быть пустым'
          }
        }
      }
    },
    ...mapMutations('login', { toggle: 'TOGGLE_LOGIN' }),
  },
}
</script>

<style scoped></style>
