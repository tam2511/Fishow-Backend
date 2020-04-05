<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
    <FIshow_Footer/>
  </div>
</template>

<script>
  import NavbarComponent from './components/Navbar.vue'
  import FIshow_Footer from './components/FIshow_Footer'
  export default {
    name: 'App',
    components: {
      FIshow_Footer,
      NavbarComponent
    },
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
      color: #ffd851 !important;
    }
  }
  @media (min-width: 1023px) {
    .section-md {
      padding: 30px 0 90px;
    }
  }

</style>
