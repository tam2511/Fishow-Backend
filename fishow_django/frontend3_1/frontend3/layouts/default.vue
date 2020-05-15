<template>
  <div class="theme_color_fishow_default">
    <!--    <settings />-->
    <new-nav-bar />
    <section class="section section-md section-view">
      <transition name="fade" mode="out-in">
        <nuxt />
      </transition>
    </section>
    <fishow-footer />
  </div>
</template>
<script>
import newNavBar from '@/components/new-nav-bar.vue'
import fishowFooter from '@/components/FIshow_Footer.vue'

export default {
  components: {
    newNavBar,
    fishowFooter,
  },
}
</script>
<style lang="scss">
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
