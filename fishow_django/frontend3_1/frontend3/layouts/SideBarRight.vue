<template>
  <div id="app">
    <HeaderBlock />
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
    <transition name="fade" mode="out-in">
      <section class="section">
        <div class="container">
          <div class="tile">
            <nuxt />
            <div class="tile is-vertical is-4">
              <div>
                <article class="tile is-parent is-vertical">
                  <p class="title is-4">Популярные блоги</p>
                  <div class="tile is-child">
                    <div v-if="minPost">
                      <HotPostMinimal
                        v-for="blog in minPost"
                        :key="blog.id"
                        :blog="blog"
                      />
                    </div>
                    <div v-else>
                      <SkeletonHotPost />
                    </div>
                  </div>
                </article>
                <article class="tile is-parent is-vertical">
                  <p class="title is-4">Прогнозы</p>
                  <div class="tile is-child">
                    <MiniPrediction />
                  </div>
                </article>
                <article class="tile is-parent is-vertical">
                  <p class="title is-4">Статистика</p>
                  <div class="tile is-child card">
                    <UserRate />
                  </div>
                </article>
                <article class="tile is-parent is-vertical">
                  <p class="title is-4">Последние комментарии</p>
                  <div class="tile is-child box"></div>
                </article>
              </div>
            </div>
          </div>
        </div>
      </section>
    </transition>
    <TheFooter />
    <banner />
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
import TheFooter from '~/components/TheFooter'
import SkeletonHotPost from '~/components/Sidebar/skeleton/SkeletonHotPost'
import banner from '~/components/banner/banner'

export default {
  components: {
    SkeletonHotPost,
    HeaderBlock,
    LoginModal,
    RegModal,
    UserRate,
    MiniPrediction,
    HotPostMinimal,
    TheFooter,
    banner,
  },
  middleware: 'auth',
  data() {
    return {
      theme: '',
      minPost: null,
    }
  },
  mounted() {
    this.$axios.get('/blogs/').then((res) => {
      this.minPost = res.data.results.slice(0, 3)
    })
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
.tile.is-parent.is-vertical {
  flex-grow: initial;
}
.nav {
  max-width: 1200px;
}
.tile.is-parent.is-vertical.space-left0 {
  padding-left: 0;
}
.blog-page .content {
  max-height: 800px;
  overflow: hidden;
  position: relative;
}
</style>
