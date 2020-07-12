<template>
  <div id="app">
    <!--    <TheHeader />-->
    <div class="columns">
      <div class="column is-three-quarters">
        <div class="container">
          <HeaderBlock class="header" />
          <nuxt />
          <TheFooter />
        </div>
      </div>
      <div class="column pSideBar">
        <SideBar />
      </div>
    </div>
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
  </div>
</template>
<script>
import { mapState } from 'vuex'
import LoginModal from '@/components/Header/LoginModal'
import RegModal from '@/components/Header/RegModal'
import HeaderBlock from '@/components/HeaderBlock'
import TheFooter from '~/components/TheFooter'
import SideBar from '~/components/predictPage/Menu/SideBar'
export default {
  components: {
    // TheHeader,
    SideBar,
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
section.section {
  background-color: #edeff4;
  @media (max-width: 450px) {
    padding: 10px;
  }
}
a {
  color: #0d0a0a;
  transition: color 0.3s;
  &:hover {
    color: rgba(0, 0, 0, 0.55);
  }
}
.column.pSideBar {
  position: fixed;
  right: 0;
  width: 25%;
  top: 0;
  height: 100%;
  @media screen and (max-width: 450px) {
    display: none;
  }
}
.header {
  width: 75%;
  padding-left: 20px;
  @media screen and (max-width: 450px) {
    width: 100%;
  }
}
div.container {
  padding-left: 20px;
  @media screen and (max-width: 450px) {
    padding-right: 20px;
  }
}
</style>
