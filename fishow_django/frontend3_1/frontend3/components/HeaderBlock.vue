<template>
  <b-navbar :fixed-top="true" :shadow="true">
    <template slot="brand">
      <b-navbar-item tag="a" to="#">
        Fishow
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item tag="nuxt-link" :to="{ name: 'index' }">
        Главная
      </b-navbar-item>
      <b-navbar-item tag="nuxt-link" :to="{ path: '/PredictionPage' }">
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
          <a class="button is-light" @click="toggleLoginYandex">
            Войти через Яндекс
          </a>
        </div>
        <div v-else class="buttons">
          <nuxt-link to="/UserPage" class="button ip-primary">
            {{ $auth.user.login || $auth.user }}</nuxt-link
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
        console.log('e = ', e)
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

<style scoped>
.nuxt-link-active {
  background-color: #fafafa;
  color: #7957d5;
}
</style>
