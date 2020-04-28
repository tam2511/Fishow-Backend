<template>
  <nav class="fishow_navbar">
    <router-link class="fishow_navbar-brand" to="/">Fishow</router-link>
    <div id="fishow_navbarNav">
      <div class="fishow_navbar-nav">
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/">Главная</router-link>
        </span>
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/predict-page"
            >Прогноз</router-link
          >
        </span>
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/blog-editor"
            >Создать блог</router-link
          >
        </span>
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/article"
            >Все блоги</router-link
          >
        </span>
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/wiki">Вики</router-link>
        </span>
        <span class="fishow_nav-item">
          <router-link class="fishow_nav-link" to="/forum">Форум</router-link>
        </span>
      </div>
    </div>
    <div class="fishow_navbar_menu">
      <div>
        <router-link to="/login">
          <img src="./user.png" alt="" />
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  computed: {
    ...mapState('user', ['username']),
  },
  methods: {
    ...mapActions('user', ['setUserInfo']),
  },
  created() {
    this.setUserInfo()
    console.log('this.username when created = ', this.username)
    if (this.username) {
      this.navbarOptions.menuOptionsRight[0] = {
        type: 'button',
        text: 'Личный кабинет',
        path: '/user-page',
      }
    }
  },
}
</script>

<style lang="scss" scoped>
.fishow_navbar {
  font-size: 16px;
  text-transform: uppercase;
  display: flex;
  flex-flow: row;
  align-items: center;
  justify-content: center;
  position: fixed;
  font-weight: 700;
  top: 0;
  left: 0;
  height: 70px;
  z-index: 100;
  width: 100%;
  background-color: var(--background-color-brand);
  @media screen and (max-width: 600px) {
    font-size: 14px;
    justify-content: flex-start;
    overflow: auto;
  }
  a {
    color: var(--color-link);
  }
  .fishow_navbar-nav {
    dispaly: flex;
    flex-flow: row;
    flex-wrap: nowrap;
    min-width: 700px;
  }
  .fishow_nav-item {
    padding: 15px;
  }
  .fishow_navbar-brand {
    justify-self: flex-start;
    padding-right: 30px;
    font-size: 30px;
  }
}
.fishow_navbar_menu {
  height: 70px;
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
