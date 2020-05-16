<template>
  <div class="theme_color_fishow_default">
    <!--    <settings />-->
    <TheHeader />
    <section class="section section-md section-view">
      <transition name="fade" mode="out-in">
        <nuxt />
      </transition>
    </section>
    <theLogin />
    <TheFooter />
  </div>
</template>
<script>
import TheLogin from '~/components/TheLogin'
import TheHeader from '~/components/TheHeader.vue'
import TheFooter from '~/components/TheFooter.vue'

export default {
  components: {
    TheHeader,
    TheFooter,
    TheLogin,
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
.section-md {
  position: relative;
  min-height: 500px;
}
</style>
