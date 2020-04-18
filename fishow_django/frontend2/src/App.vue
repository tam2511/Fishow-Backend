<template>
  <div id="app" class="theme_color_megafon-brand">
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
  components: {
    NewNavBar,
    FIshow_Footer,
  },
}
</script>

<style lang="scss">
@import 'assets/scss/custom-styles/style.scss';
@import 'assets/scss/customStyles.scss';
@import 'assets/scss/fishowStyles.scss';
@import 'assets/scss/custom-styles/fonts.scss';
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
