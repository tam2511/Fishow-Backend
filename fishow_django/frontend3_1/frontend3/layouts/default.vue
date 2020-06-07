<template>
  <div id="app" :class="'theme ' + theme">
    <!--    <TheHeader />-->
    <HeaderBlock />
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
    <transition name="fade" mode="out-in">
      <section class="section">
        <nuxt />
      </section>
    </transition>
    <!--    <theLogin />-->
    <!--    <TheFooter />-->
  </div>
</template>
<script>
import { mapState } from 'vuex'
import LoginModal from '@/components/Header/LoginModal'
import RegModal from '@/components/Header/RegModal'
import HeaderBlock from '@/components/HeaderBlock'
// import TheFooter from '~/components/TheFooter'

export default {
  components: {
    // TheHeader,
    HeaderBlock,
    LoginModal,
    RegModal,
    // TheFooter,
    // TheLogin,
  },
  data() {
    return {
      theme: '',
    }
  },
  computed: {
    ...mapState('login', ['showStateLogin', 'showStateReg']),
  },
  mounted() {
    this.checkTheme()
  },
  methods: {
    checkTheme() {
      if (process.browser) {
        this.theme =
          localStorage.getItem('theme') || 'theme_color_fishow_default'
      }
    },
  },
}
</script>
<style lang="scss">
.section {
  background-color: #edeff4;
}
a {
  color: #0d0a0a;
  transition: color 0.3s;
  &:hover {
    color: rgba(0, 0, 0, 0.55);
  }
}
</style>
