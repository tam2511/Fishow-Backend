<template lang="pug">
  nav.fishow_navbar
    nuxt-link.fishow_navbar-brand(to='/') Fishow
    .fishow_navbar-nav
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/') Главная
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/PredictionPage') Прогноз
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/blog-editor') Создать блог
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/article') Все блоги
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/wiki') Вики
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/forum') Форум
      span.fishow_nav-item
        nuxt-link.fishow_nav-link(to='/UserPage') Пользователь
    nuxt-link(v-if='$auth.loggedIn', to='/UserPage')
      .fishow_navbar_menu
        | {{ $auth.user }}
    a(v-else='', @click='modalToggle')
      .fishow_navbar_menu
        | Вход / Регистрация
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  async fetch({ store, error }) {
    try {
      await store.dispatch('user/getUser')
    } catch (e) {
      error({
        statusCode: 503,
        message: 'Unable to fetch events at this time. Please try again.',
      })
    }
  },
  data() {
    return {
      active: false,
      step: false,
    }
  },
  computed: {
    ...mapState('user', ['user', 'userBlogs', 'userRating', 'userComments']),
    // ...mapState('login', ['show','stepReg','error'])
  },
  created() {
    // this.setUserInfo()
  },
  methods: {
    ...mapMutations('login', { modalToggle: 'SET_SHOW' }),
    // actiLog() {
    //     this.active = !this.active
    // },
    // changeStep() {
    // },
    // ...mapActions('user', ['setUserInfo']),
    // ...mapActions('login', ['setShow', 'setStep'])
  },
}
</script>

<style scoped lang="scss">
.fishow_navbar {
  font-size: 16px;
  display: flex;
  flex-flow: row;
  align-items: center;
  position: sticky;
  top: 0;
  left: 0;
  height: 65px;
  z-index: 100;
  width: 100%;
  box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
  background-color: var(--background-color-default);
  @media screen and (max-width: 600px) {
    font-size: 14px;
    justify-content: flex-start;
    overflow: auto;
  }
  a {
    color: var(--color-typo-primary);
    &:hover {
      color: var(--color-typo-brand);
    }
  }
}
.fishow_nav-item {
  padding: 15px;
  &:last-child {
    padding-right: 70px;
  }
}
.fishow_navbar-nav {
  display: contents;
  white-space: nowrap;
}
.fishow_navbar-brand {
  justify-self: flex-start;
  padding-left: 30px;
  padding-right: 30px;
  font-size: 30px;
}
.fishow_navbar_menu {
  height: 65px;
  position: fixed;
  cursor: pointer;
  padding: 0 10px;
  right: 0;
  top: 0;
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: space-evenly;
  background-color: #fff;
  box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
  transition-duration: 0.3s;
  &:hover {
    background-color: var(--background-color-default);
  }
}
</style>
