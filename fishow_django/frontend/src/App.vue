<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
    <FIshow_Footer/>
  </div>
</template>

<script>
  import {apiService} from "./common/api.service";
  import NavbarComponent from "./components/Navbar.vue";
  import FIshow_Footer from "./components/FIshow_Footer";
  export default {
    name: 'App',
    components: {
      FIshow_Footer,
      NavbarComponent
    },
    methods: {
      async setUserInfo() {
        // add the username of the logged in user to localStorage
        const data = await apiService("/api/user/");
        const requestUser = data["username"];
        window.localStorage.setItem("username", requestUser);
      }
    },
    created() {
      this.setUserInfo()
    }
  }


</script>

<style lang="scss">
@import "localFIles/assest/scss/custom-styles/style.scss";
@import "localFIles/assest/scss/customStyles.scss";
@import "localFIles/assest/scss/fishowStyles.scss";
@import "assets/css/bootstrap.css";
@import "assets/css/fishowStyles.css";
@import "localFIles/assest/scss/custom-styles/fonts.scss";
</style>
