<template>
  <!--  <div class="container" id="login" v-if="!username">-->
  <!--    <div class="note note&#45;&#45;down">-->
  <!--      <p>{{ note }}</p>-->
  <!--    </div>-->
  <!--    <div class="login">-->
  <!--      <header class="login&#45;&#45;header">-->
  <!--        <span>Личный кабинет</span>-->
  <!--      </header>-->
  <!--      <section class="login&#45;&#45;section">-->
  <!--        <form class="login&#45;&#45;form" @submit.prevent="makeAuth">-->
  <!--          <fieldset>-->
  <!--            <input-->
  <!--              type="email"-->
  <!--              placeholder="email"-->
  <!--              v-model="email"-->
  <!--              required-->
  <!--              @focus="inputFocus"-->
  <!--            />-->
  <!--          </fieldset>-->
  <!--          <div class="error" v-if="errorEmail">-->
  <!--            Укажите правильную почту-->
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
  <!--            <button type="submit" class="button button-default">Вход</button>-->
  <!--            <router-link class="button button-default" to="/registration"-->
  <!--              >Регистрация</router-link-->
  <!--            >-->
  <!--          </fieldset>-->
  <!--        </form>-->
  <!--      </section>-->
  <!--    </div>-->
  <!--  </div>-->
  <transition name="fade">
    <div v-if="show" class="logmod">
      <div class="logmod__wrapper">
        <div class="logmod__close" @click="setShow">X</div>
        <div class="logmod__container">
          <ul class="logmod__tabs">
            <li data-tabtar="lgm-2" :class="{ current: stepReg }">
              <a tabindex="0" @click="setStep">Вход</a>
            </li>
            <li data-tabtar="lgm-1" :class="{ current: !stepReg }">
              <a tabindex="0" @click="setStep">Регистрация</a>
            </li>
          </ul>
          <div class="logmod__tab-wrapper">
            <div v-if="!stepReg" class="logmod__tab lgm-1 show">
              <div class="logmod__heading">
                <span class="logmod__heading-subtitle"
                  >Введите свои данные
                  <strong>для создания аккаунта</strong></span
                >
              </div>
              <div class="logmod__form">
                <form accept-charset="utf-8" action="#" class="simform">
                  <div class="sminputs">
                    <div class="input full">
                      <label class="string optional" for="user-email"
                        >Email*</label
                      >
                      <input
                        id="user-email"
                        class="string optional"
                        maxlength="255"
                        placeholder="Email"
                        type="email"
                        size="50"
                      />
                    </div>
                  </div>
                  <div class="sminputs">
                    <div class="input string optional">
                      <label class="string optional" for="user-pw"
                        >Пароль *</label
                      >
                      <input
                        id="user-pw"
                        class="string optional"
                        maxlength="255"
                        placeholder="Password"
                        type="text"
                        size="50"
                      />
                    </div>
                    <div class="input string optional">
                      <label class="string optional" for="user-pw-repeat"
                        >Повторите пароль *</label
                      >
                      <input
                        id="user-pw-repeat"
                        class="string optional"
                        maxlength="255"
                        placeholder="Repeat password"
                        type="text"
                        size="50"
                      />
                    </div>
                  </div>
                  <div class="simform__actions">
                    <button class="sumbit" name="commit" type="sumbit">
                      Создать аккаунт
                    </button>
                    <span class="simform__actions-sidetext"
                      >Создавая аккаунт вы соглашаетесь с
                      <a class="special" href="#" target="_blank" role="link"
                        >Terms &amp; Privacy</a
                      ></span
                    >
                  </div>
                </form>
              </div>
              <div class="logmod__alter">
                <div class="logmod__alter-container">
                  <a href="#" class="connect facebook">
                    <div class="connect__icon">
                      <i class="fa fa-facebook"></i>
                    </div>
                    <div class="connect__context">
                      <span
                        >Создать аккаунт с помощью
                        <strong>Facebook</strong></span
                      >
                    </div>
                  </a>
                  <a href="#" class="connect googleplus">
                    <div class="connect__icon">
                      <i class="fa fa-google-plus"></i>
                    </div>
                    <div class="connect__context">
                      <span
                        >Создать аккаунт с помощью
                        <strong>Google+</strong></span
                      >
                    </div>
                  </a>
                </div>
              </div>
            </div>
            <div v-else class="logmod__tab lgm-2 show">
              <div class="logmod__heading">
                <span class="logmod__heading-subtitle"
                  >Введите свою почту и пароль</span
                >
              </div>
              <div class="logmod__form">
                <form
                  accept-charset="utf-8"
                  action="#"
                  class="simform"
                  @submit.prevent="makeAuth"
                >
                  <div class="sminputs">
                    <div class="input full">
                      <label class="string optional" for="user-email"
                        >Почта*</label
                      >
                      <input
                        id="user-email"
                        v-model="email"
                        class="string optional"
                        maxlength="255"
                        placeholder="example@mail.ru"
                        type="email"
                        size="50"
                      />
                    </div>
                  </div>
                  <div class="sminputs">
                    <div class="input full">
                      <label class="string optional" for="user-pw"
                        >Пароль *</label
                      >
                      <input
                        id="user-pw"
                        v-model="password"
                        class="string optional"
                        maxlength="255"
                        placeholder="Пароль"
                        type="password"
                        size="50"
                      />
                      <span class="hide-password">Показать</span>
                    </div>
                  </div>
                  <div class="simform__actions">
                    <button class="sumbit" name="commit" type="sumbit">
                      Войти
                    </button>
                    <span class="simform__actions-sidetext"
                      ><a class="special" role="link" href="#"
                        >Забыли ваш пароль?<br />Нажмите здесь</a
                      ></span
                    >
                  </div>
                </form>
              </div>
              <div class="logmod__alter">
                <div class="logmod__alter-container">
                  <a href="#" class="connect facebook">
                    <div class="connect__icon">
                      <i class="fa fa-facebook"></i>
                    </div>
                    <div class="connect__context">
                      <span>Войти с помощью <strong>Facebook</strong></span>
                    </div>
                  </a>
                  <a href="#" class="connect googleplus">
                    <div class="connect__icon">
                      <i class="fa fa-google-plus"></i>
                    </div>
                    <div class="connect__context">
                      <span>Войти с помощью <strong>Google+</strong></span>
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'LoginPage',
  data() {
    return {
      note: '',
      login: '',
      password: '',
      email: ''
    }
  },
  head() {
    return {
      title: 'Fishow - Вход'
    }
  },
  computed: {
    ...mapState('user', ['username']),
    ...mapState('login', ['show', 'stepReg', 'error'])
  },
  methods: {
    makeAuth(e) {
      this.sendUserData(e)
    },
    inputFocus() {
      this.note = ''
    },
    closeModal() {
      console.log('close from login')
      this.$emit('actiLog', false)
    },
    ...mapActions('login', ['setShow', 'setStep', 'sendUserData'])
  }
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
