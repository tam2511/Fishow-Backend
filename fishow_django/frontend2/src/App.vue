<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
    <FIshow_Footer/>
  </div>
</template>

<script>

  import { apiService } from './common/api.service'
  import NavbarComponent from './components/Navbar.vue'
  import FIshow_Footer from './components/FIshow_Footer'
  export default {
    name: 'App',
    components: {
      FIshow_Footer,
      NavbarComponent
    },
    methods: {
      async setUserInfo () {
        // add the username of the logged in user to localStorage
        const data = await apiService('/api/user/')
        const requestUser = data.username
        window.localStorage.setItem('username', requestUser)
      }
    },
    created () {
      this.setUserInfo()
    }
  }

</script>

<style lang="scss">
  @import "assets/scss/custom-styles/style.scss";
  @import "assets/scss/customStyles.scss";
  @import "assets/scss/fishowStyles.scss";
  @import "assets/scss/custom-styles/fonts.scss";
  html {
    background-color: #edeff4;
  }
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
</style>
