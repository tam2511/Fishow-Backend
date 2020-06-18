<template>
  <div id="app">
    <!--    <TheHeader />-->
    <HeaderBlock />
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
    <transition name="fade" mode="out-in">
      <section class="section">
        <div class="tile">
          <nuxt />
          <div class="tile is-vertical is-4">
            <article class="tile is-parent is-vertical">
              <p class="title">Горячие блоги</p>
              <div class="tile is-child">
                <HotPostMinimal
                  v-for="blog in minPost"
                  :key="blog.id"
                  :blog="blog"
                />
              </div>
            </article>
            <article class="tile is-parent is-vertical">
              <p class="title">Прогнозы</p>
              <div class="tile is-child box">
                <MiniPrediction />
              </div>
            </article>
            <article class="tile is-parent is-vertical">
              <p class="title">Статистика</p>
              <div class="tile is-child box">
                <UserRate />
              </div>
            </article>
            <article class="tile is-parent is-vertical">
              <p class="title">Последние комментарии</p>
              <div class="tile is-child box"></div>
            </article>
          </div>
        </div>
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
import UserRate from '@/components/Sidebar/UserRate'
import MiniPrediction from '@/components/Sidebar/MiniPrediction'
import HeaderBlock from '@/components/HeaderBlock'
import HotPostMinimal from '~/components/Sidebar/HotPostMinimal'
// import TheFooter from '~/components/TheFooter'

export default {
  components: {
    // TheHeader,
    HeaderBlock,
    LoginModal,
    RegModal,
    UserRate,
    MiniPrediction,
    HotPostMinimal,

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
    ...mapState('blogs', ['minPost']),
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
.tile.is-parent.is-vertical {
  flex-grow: initial;
}
</style>
