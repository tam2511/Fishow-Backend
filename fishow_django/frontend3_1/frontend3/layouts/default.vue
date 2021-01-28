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
@import '@/src/styles/main';
</style>
