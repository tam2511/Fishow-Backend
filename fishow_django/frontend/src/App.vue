<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
    <FIshow_Footer/>
  </div>
</template>

<script>
  // import script from "./components/script";
  import NavbarComponent from "./components/Navbar.vue";
  import FIshow_Footer from "./components/FIshow_Footer";
  export default {
    name: 'App',
    components: {
      FIshow_Footer,
      NavbarComponent
    },
    mounted() {
      console.log('mounted');
      // script();
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
