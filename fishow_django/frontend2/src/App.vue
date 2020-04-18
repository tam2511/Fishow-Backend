<template>
  <div id="app" :class="theme">
    <new-nav-bar />
    <router-view />
    <FIshow_Footer />
  </div>
</template>

<script>
import FIshow_Footer from './components/FIshow_Footer'
import NewNavBar from './components/navbar/new-nav-bar'
export default {
  name: 'App',
  data() {
    return {
      theme : 'theme_color_fishow_esoteric'
    }
  },
  methods: {
    checkTheme() {
      if (localStorage.getItem('theme')) {
        this.theme = localStorage.getItem('theme')
      }
    }
  },
  components: {
    NewNavBar,
    FIshow_Footer,
  },
  mounted() {
    this.checkTheme();
  }
}
</script>

<style lang="scss">
@import 'assets/scss/custom-styles/style.scss';
@import 'assets/scss/customStyles.scss';
@import 'assets/scss/fishowStyles.scss';
@import 'assets/scss/custom-styles/fonts.scss';
#app {
  transition-duration: 0.2s;
}
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
