<template>
  <div id="app">
    <HeaderBlock />
    <div class="columns">
      <div class="column is-three-quarters">
        <div class="container">
          <nuxt />
        </div>
      </div>
      <div class="column pSideBar">
        <SideBar />
      </div>
    </div>
    <TheFooter />
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
    SideBar,
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
body {
  background-color: #eee;
}
.results-container .columns {
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
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
  top: 55px;
  min-height: 500px;
  height: calc(100% - 250px);

  @media screen and (max-width: 768px) {
    display: none;
  }
}
.header {
  @media screen and (max-width: 450px) {
    width: 100%;
  }
}
div.container {
  @media screen and (max-width: 450px) {
    padding-right: 0;
  }
}
.blue {
  color: #09438e;
}
.red {
  color: #8a0000;
}
.green {
  color: green;
}
.strong {
  font-weight: 800;
}
.report-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  span {
    height: 6rem;
    width: 6rem;
    i {
      font-size: 6rem;
      color: #fff;
    }
  }
}
@media screen and (max-width: 450px) {
  .column.is-three-quarters {
    padding-left: 0;
    padding-right: 0;
  }
}
@media screen and (min-width: 769px) {
  .main-content {
    padding-left: 20px;
  }
}
</style>
