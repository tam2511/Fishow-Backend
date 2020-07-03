<template>
  <div id="app">
    <!--    <TheHeader />-->
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
    <!--    <theLogin />-->
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
    // TheHeader,
    HeaderBlock,
    LoginModal,
    RegModal,
    TheFooter,
    // TheLogin,
  },
  computed: {
    ...mapState('login', ['showStateLogin', 'showStateReg']),
  },
}
</script>
<style lang="scss">
.section {
  background-color: #edeff4;
  @media (max-width: 450px) {
    padding: 0;
  }
}
a {
  color: #0d0a0a;
  transition: color 0.3s;
  &:hover {
    color: rgba(0, 0, 0, 0.55);
  }
}
</style>
