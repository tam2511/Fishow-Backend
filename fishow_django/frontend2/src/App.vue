<template>
  <div id="app" class="theme" :class="theme">
    <settings/>
    <new-nav-bar   />
    <router-view />
    <FIshow_Footer />
  </div>
</template>

<script>
import FIshow_Footer from './components/FIshow_Footer'
import NewNavBar from './components/navbar/new-nav-bar'
import Settings from "./components/Home/Settings";
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
    Settings,
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
@media (min-width: 1023px) {
  .section-md {
    padding: 30px 0 90px;
  }
}
</style>
