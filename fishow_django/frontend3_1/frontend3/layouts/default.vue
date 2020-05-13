<template>
  <div>
    <!--    <settings />-->
    <new-nav-bar />
    <section class="section section-md section-view">
      <transition name="fade" mode="out-in">
        <nuxt />
      </transition>
    </section>
    <!--    <FIshow_Footer />-->
  </div>
</template>
<script>
import newNavBar from '@/components/new-nav-bar.vue'

export default {
  components: {
    newNavBar
  }
}
</script>
<style lang="scss">
@import '~/assets/scss/custom-styles/style.scss';
@import '~/assets/scss/customStyles.scss';
@import '~/assets/scss/fishowStyles.scss';
@import '~/assets/scss/custom-styles/fonts.scss';
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
</style>
