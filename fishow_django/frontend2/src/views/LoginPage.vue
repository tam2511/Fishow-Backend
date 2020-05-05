<template>
  <div class="container" id="login" v-if="!username">
    <div class="note note--down">
      <p>{{ note }}</p>
    </div>
    <div class="login">
      <header class="login--header">
        <span>Личный кабинет</span>
      </header>
      <section class="login--section">
        <form class="login--form" @submit.prevent="makeAuth">
          <fieldset>
            <input
              type="email"
              placeholder="email"
              v-model="email"
              required
              @focus="inputFocus"
            />
          </fieldset>
          <div class="error" v-if="errorEmail">
            Укажите правильную почту
          </div>
          <fieldset>
            <input
              type="password"
              placeholder="Пароль"
              v-model="password"
              @focus="inputFocus"
              required
            />
          </fieldset>
          <div class="error" v-if="error">
            Неверно указана почта или пароль
          </div>
          <fieldset>
            <button type="submit" class="button button-default">Вход</button>
            <router-link class="button button-default" to="/registration"
              >Регистрация</router-link
            >
          </fieldset>
        </form>
      </section>
    </div>
  </div>
</template>

<script>
import { apiService } from '@/common/api.service'
import { mapState } from 'vuex'

export default {
  name: 'LoginPage',
  data() {
    return {
      note: '',
      login: '',
      password: '',
      email: '',
      error: null,
      errorEmail: null,
    }
  },
  computed: {
    ...mapState('user', ['username']),
  },
  methods: {
    makeAuth(e) {
      this.note = 'Login failed'
      const endpoint = 'api/rest-auth/login/'
      apiService(endpoint, 'POST', {
        email: this.email,
        password: this.password,
      }).then((date) => {
        if (date['non_field_errors']) {
          this.error = true
        } else if (
          date['email'] &&
          date['email'][0] === 'Enter a valid email address.'
        ) {
          this.errorEmail = true
        } else {
          this.$router.push({
            name: 'home',
          })
          location.reload()
        }
      })
    },
    inputFocus() {
      this.note = ''
    },
  },
  created() {
    document.title = 'Fishow - Вход'
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
