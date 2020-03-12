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
@import "assets/css/style.css";
@import "assets/css/customStyles.css";
@import "assets/css/bootstrap.css";
@import "assets/css/fishowStyles.css";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
