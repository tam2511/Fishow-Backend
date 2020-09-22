<template>
  <b-navbar :fixed-top="true" :shadow="true" class="navbar-brand-container">
    <template slot="brand">
      <b-navbar-item tag="a" to="#" class="logo" data-word="FISHOW">
        FISHOW
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item tag="nuxt-link" :to="{ name: 'index' }">
        Главная
      </b-navbar-item>
      <b-navbar-item tag="nuxt-link" :to="{ path: '/prognoz-kleva' }">
        Прогноз
      </b-navbar-item>
      <b-navbar-dropdown label="Блоги">
        <b-navbar-item tag="nuxt-link" :to="{ path: '/blog-editor' }">
          Создать блог
        </b-navbar-item>
      </b-navbar-dropdown>
    </template>
    <template slot="end">
      <b-navbar-item tag="div">
        <div v-if="!$auth.user" class="buttons">
          <a class="button is-primary" @click="toggleReg">
            <strong>Регистрация</strong>
          </a>
          <a class="button is-light" @click="toggleLogin">
            Войти
          </a>
          <!--          <a class="button is-light" @click="toggleLoginYandex">-->
          <!--            Войти через Яндекс-->
          <!--          </a>-->
        </div>
        <div v-else class="buttons">
          <nuxt-link to="/UserPage" class="button ip-primary">
            {{ $auth.user.login || $auth.user.username }}</nuxt-link
          >
          <a class="button is-light" @click="logout">
            Выйти
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  computed: {
    ...mapState('user', ['user']),
  },
  methods: {
    async logout() {
      try {
        await this.$auth.logout()
      } catch (e) {
        // console.log('e = ', e)
      }
    },
    toggleLoginYandex() {
      this.$auth.loginWith('social')
    },
    ...mapMutations('login', {
      toggleLogin: 'TOGGLE_LOGIN',
      toggleReg: 'TOGGLE_REG',
    }),
  },
}
</script>

<style lang="scss">
.nuxt-link-active {
  color: var(--color-type-primary);
  &:not([href*='blog']) {
    background-color: #fafafa;
  }
}
.logo {
  padding: 0 !important;
  color: transparent !important;
  -webkit-text-stroke: 1px #fff;
  position: relative;
  &:after {
    content: attr(data-word);
    position: absolute;
    /*top: 0;*/
    left: 0;
    color: #fff;
    cursor: initial;
    animation: waves 2s ease-in-out infinite forwards;
  }
}
a.navbar-item:hover {
  color: white;
}
@keyframes waves {
  0%,
  100% {
    clip-path: polygon(
      0 66%,
      11% 59%,
      18% 51%,
      26% 46%,
      35% 41%,
      48% 44%,
      55% 54%,
      63% 63%,
      76% 60%,
      82% 50%,
      92% 48%,
      100% 53%,
      100% 100%,
      0% 100%
    );
  }
  50% {
    clip-path: polygon(
      0 66%,
      8% 74%,
      17% 77%,
      28% 70%,
      35% 57%,
      48% 44%,
      56% 39%,
      69% 41%,
      75% 47%,
      84% 60%,
      92% 61%,
      100% 53%,
      100% 100%,
      0% 100%
    );
  }
}
.navbar-brand {
  font-size: 20px;
  font-weight: bold;
  transition: all 200ms;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  background-position: 50% 50%;
  display: grid;
  place-items: center;
  z-index: 1;
  cursor: initial;
  position: relative;
  background: var(--color-type-primary);
  padding: 7px;
}
</style>
