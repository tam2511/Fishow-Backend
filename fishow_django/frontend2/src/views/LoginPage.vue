<template>
  <div class="container" id="login">
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
              type="text"
              placeholder="Логин"
              v-model="login"
              required
              @focus="inputFocus"
            />
          </fieldset>
          <fieldset>
            <input
              type="password"
              placeholder="Пароль"
              v-model="password"
              @focus="inputFocus"
              required
            />
          </fieldset>
          <fieldset>
            <button type="submit" class="button button-default">Вход</button>
            <router-link class="button button-default" to="/register"
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

export default {
  name: 'LoginPage',
  data() {
    return {
      note: '',
      login: '',
      password: '',
    }
  },
  methods: {
    makeAuth(e) {
      console.log('submit')
      // write you own auth logic here
      this.note = 'Login failed'
      const data = {
        username: this.login,
        password: this.password,
      }
      console.log('data = ', data)
      const endpoint = 'api/rest-auth/login/'
      apiService(endpoint, 'POST', data).then((date) => {
        console.log('date ', date)
        this.$router.push({
          name: 'home',
        })
      })
    },
    inputFocus() {
      this.note = ''
    },
  },
}
</script>

<style scoped lang="scss">
body,
input {
  font-size: 1.2rem;
}

fieldset {
  border: none;
}

.note {
  background: #ff9e80;
  padding: 0.75rem 1.5rem;
  box-sizing: border-box;
  position: absolute;
  bottom: 100%;
  width: 100%;
  z-index: 0;
  transition: all 0.2s ease-out;
}

.login {
  z-index: 1;
  position: relative;
  background: white;
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
</style>
