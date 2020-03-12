<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
  </div>
</template>

<script>
  // import script from "./components/script";
  import NavbarComponent from "./components/Navbar.vue";
  export default {
    name: 'App',
    components: {
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
@import "assets/css/customStyles.css";
@import "assets/css/bootstrap.css";
@import "assets/css/fishowStyles.css";
@import "localFIles/assest/scss/custom-styles/fonts.scss";
</style>
