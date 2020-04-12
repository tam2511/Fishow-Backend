<template>
  <header class="section page-header rd-navbar-darker">
    <div class="rd-navbar-wrap">
      <nav
        class="rd-navbar rd-navbar-modern"
        data-layout="rd-navbar-fixed"
        data-sm-layout="rd-navbar-fixed"
        data-md-layout="rd-navbar-fixed"
        data-md-device-layout="rd-navbar-fixed"
        data-lg-layout="rd-navbar-fixed"
        data-lg-device-layout="rd-navbar-fixed"
        data-xl-layout="rd-navbar-static"
        data-xl-device-layout="rd-navbar-static"
        data-xxl-layout="rd-navbar-static"
        data-xxl-device-layout="rd-navbar-static"
        data-lg-stick-up-offset="114px"
        data-xl-stick-up-offset="114px"
        data-xxl-stick-up-offset="114px"
        data-lg-stick-up="true"
        data-xl-stick-up="true"
        data-xxl-stick-up="true"
      >
        <rd-navbar-panel />
        <rd-navbar-main />
      </nav>
    </div>
  </header>
</template>

<script>
import RdNavbarPanel from './navbar/rd-navbar-panel'
import RdNavbarMain from './navbar/rd-navbar-main'
export default {
  name: 'navbar',
  components: { RdNavbarMain, RdNavbarPanel },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss"></style>
