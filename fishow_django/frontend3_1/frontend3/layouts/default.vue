<template>
  <div id="app">
    <HeaderBlock />
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
    <transition name="fade" mode="out-in">
      <section class="section">
        <div class="container">
          <nuxt />
        </div>
      </section>
    </transition>
    <TheFooter />
  </div>
</template>
<script>
import { mapState } from 'vuex'
import LoginModal from '@/components/Header/LoginModal'
import RegModal from '@/components/Header/RegModal'
import HeaderBlock from '@/components/HeaderBlock'
import TheFooter from '~/components/TheFooter'

export default {
  components: {
    HeaderBlock,
    LoginModal,
    RegModal,
    TheFooter,
  },
  computed: {
    ...mapState('login', ['showStateLogin', 'showStateReg']),
  },
}
</script>
<style lang="scss">
@import '~bulma/sass/utilities/_all';

// Set your colors
:root {
  --color-type-primary: #018cac;
  --color-type-hover: #003d4b;
  --size-typo-legend: 14px;
  --main-color: #018cac;
}
$primary: #018cac;
$primary-invert: findColorInvert($primary);
$twitter: #4099ff;
$twitter-invert: findColorInvert($twitter);

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: (
  'white': (
    $white,
    $black,
  ),
  'black': (
    $black,
    $white,
  ),
  'light': (
    $light,
    $light-invert,
  ),
  'dark': (
    $dark,
    $dark-invert,
  ),
  'primary': (
    $primary,
    $primary-invert,
  ),
  'info': (
    $info,
    $info-invert,
  ),
  'success': (
    $success,
    $success-invert,
  ),
  'warning': (
    $warning,
    $warning-invert,
  ),
  'danger': (
    $danger,
    $danger-invert,
  ),
  'twitter': (
    $twitter,
    $twitter-invert,
  ),
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import '~bulma';
@import '~buefy/src/scss/buefy';

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');

a {
  color: #0d0a0a;
  transition: color 0.3s;
  &:hover {
    color: rgba(0, 0, 0, 0.55);
  }
}
.errors {
  color: #b10909;
}
#app > section.section {
  padding-top: 10px;
  /*@media screen and (max-width: 450px) {*/
  /*  padding: 20px 0 0;*/
  /*}*/
}
#app {
  overflow: hidden;
  font-family: 'Roboto', sans-serif;
}
.card {
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}
.prediction-section label {
  font-weight: 400;
}
</style>
