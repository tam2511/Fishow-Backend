<template>
  <div id="app" :class="'theme ' + theme">
    <settings />
    <new-nav-bar />
    <section class="section section-md section-view">
      <transition name="fade" mode="out-in">
        <router-view />
      </transition>
    </section>
    <FIshow_Footer />
  </div>
</template>

<script>
import FIshow_Footer from './components/FIshow_Footer'
import NewNavBar from './components/navbar/new-nav-bar'
import Settings from './components/Home/Settings'
export default {
  name: 'App',
  data() {
    return {
      theme: 'theme_color_fishow_esoteric',
    }
  },
  methods: {
    checkTheme() {
      if (localStorage.getItem('theme')) {
        this.theme = localStorage.getItem('theme')
      }
    },
  },
  components: {
    Settings,
    NewNavBar,
    FIshow_Footer,
  },
  mounted() {
    this.checkTheme()
  },
  created() {},
}
</script>

<style lang="scss">
@import 'assets/scss/custom-styles/style.scss';
@import 'assets/scss/customStyles.scss';
@import 'assets/scss/fishowStyles.scss';
@import 'assets/scss/custom-styles/fonts.scss';
#app {
  height: 100%;
  transition-duration: 0.2s;
}
@media (min-width: 1023px) {
  .section-md {
    padding: 20px 0 90px;
  }
}
html, body {
  margin: 0px;
  padding: 0px;
  height: 100%;
}
/*** TRANSITIONS ***/
.fade-enter {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}

.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.2s ease;
}

.slide-fade-leave-to {
  transform: translateX(-10px);
  opacity: 0;
}

.slide-up-enter {
  transform: translateY(10px);
  opacity: 0;
}

.slide-up-enter-active {
  transition: all 0.2s ease;
}

.slide-up-move {
  transition: transform 0.8s ease-in;
}
</style>
