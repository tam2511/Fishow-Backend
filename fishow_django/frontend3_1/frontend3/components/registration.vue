<template>
  <!--  <div class="container" id="login">-->
  <!--    <div class="note note&#45;&#45;down">-->
  <!--      <p>{{ note }}</p>-->
  <!--    </div>-->
  <!--    <div class="login" v-if="!success">-->
  <!--      <header class="login&#45;&#45;header">-->
  <!--        <span>Регистрация</span>-->
  <!--      </header>-->
  <!--      <section class="login&#45;&#45;section">-->
  <!--        <form class="login&#45;&#45;form" @submit.prevent="makeAuth">-->
  <!--          <fieldset>-->
  <!--            <input-->
  <!--              type="login"-->
  <!--              placeholder="Логин"-->
  <!--              v-model="login"-->
  <!--              required-->
  <!--              @focus="inputFocus"-->
  <!--            />-->
  <!--          </fieldset>-->
  <!--          <div class="error" v-if="loginError">-->
  <!--            {{ loginError }}-->
  <!--          </div>-->
  <!--          <fieldset>-->
  <!--            <input-->
  <!--              type="email"-->
  <!--              placeholder="Почта"-->
  <!--              v-model="email"-->
  <!--              required-->
  <!--              @focus="inputFocus"-->
  <!--            />-->
  <!--          </fieldset>-->
  <!--          <div class="error" v-if="errorEmail">-->
  <!--            {{ errorEmail }}-->
  <!--          </div>-->
  <!--          <fieldset>-->
  <!--            <input-->
  <!--              type="password"-->
  <!--              placeholder="Пароль"-->
  <!--              v-model="password"-->
  <!--              @focus="inputFocus"-->
  <!--              required-->
  <!--            />-->
  <!--          </fieldset>-->
  <!--          <div class="error" v-if="error">-->
  <!--            Неверно указана почта или пароль-->
  <!--          </div>-->
  <!--          <fieldset>-->
  <!--            <button type="submit" class="button button-default">-->
  <!--              Подтвердить-->
  <!--            </button>-->
  <!--            <router-link class="button button-default" to="/login"-->
  <!--              >Уже зарегистрирован</router-link-->
  <!--            >-->
  <!--          </fieldset>-->
  <!--        </form>-->
  <!--      </section>-->
  <!--    </div>-->
  <!--    <div class="success" v-else>-->
  <!--      <h3>Регистрация прошла успешно</h3>-->
  <!--      <h4>Проверьте свою почту для активации аккаунта</h4>-->
  <!--      <img-->
  <!--        width="300"-->
  <!--        height="300"-->
  <!--        src="static/assets/images/source.gif"-->
  <!--        alt=""-->
  <!--      />-->
  <!--    </div>-->
  <!--  </div>-->
  <div class="container">
    <div class="logmod">
      <div class="logmod__wrapper">
        <div class="logmod__container">
          <ul class="logmod__tabs">
            <li data-tabtar="lgm-2" class="">
              <router-link to="/login" tabindex="0">Вход</router-link>
            </li>
            <li data-tabtar="lgm-1" class="current">
              <router-link to="/registration" tabindex="0"
                >Регистрация</router-link
              >
            </li>
          </ul>
          <div class="logmod__tab-wrapper"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { apiService } from '@/plugins/api.service'

export default {
  name: 'Registration',
  data() {
    return {
      note: '',
      login: '',
      password: '',
      email: '',
      error: null,
      errorEmail: null,
      loginError: null,
      success: false
    }
  },
  computed: {
    ...mapState('user', ['username'])
  },
  methods: {
    makeAuth(e) {
      this.note = 'Login failed'
      const endpoint = 'api/rest-auth/registration/'
      apiService(endpoint, 'POST', {
        username: this.login,
        email: this.email,
        password1: this.password,
        password2: this.password
      }).then((date) => {
        if (date.non_field_errors) {
          this.error = true
        } else if (date.email || date.username) {
          if (
            date.email[0] ===
            'A user is already registered with this e-mail address.'
          ) {
            this.errorEmail = 'Данная почта уже занята'
          }
          if (
            date.username &&
            date.username[0] === 'A user with that username already exists.'
          ) {
            this.loginError = 'Данный логин уже занят.'
          }
          // this.errorEmail = true
        } else {
          this.success = true
          // this.$router.push({
          //   name: 'home',
          // })
          // location.reload()
        }
      })
    },
    inputFocus() {
      this.note = ''
    }
  }
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
.error {
  text-align: center;
  padding: 10px 0 10px 0;
  color: #a30000;
}
.success {
  min-height: 600px;
  padding: 30px;
  text-align: center;
}
</style>
