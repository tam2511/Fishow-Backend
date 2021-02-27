<template>
  <div id="app">
    <HeaderBlock />
    <LoginModal v-if="showStateLogin" />
    <RegModal v-if="showStateReg" />
    <section class="section">
      <div class="container">
        <div class="tile">
          <nuxt />
          <div class="tile is-vertical is-4 tile-sidebar">
            <article class="tile is-parent is-vertical">
              <p class="title is-4">Прогнозы</p>
              <div class="tile is-child">
                <MiniPrediction />
              </div>
            </article>
            <div class="buttons">
              <nuxt-link
                class="button is-primary is-fullwidth"
                :to="{ path: '/prognoz-kleva' }"
                >Прогноз</nuxt-link
              >
              <nuxt-link
                :to="{ path: '/blog-editor' }"
                class="button is-success is-fullwidth"
              >
                Создать пост
              </nuxt-link>
              <nuxt-link
                :to="{ path: '/report-editor' }"
                class="button is-danger is-fullwidth"
              >
                Создать отчет
              </nuxt-link>
            </div>
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

            <article v-if="$auth.user" class="tile is-parent is-vertical">
              <p class="title is-4">Статистика</p>
              <div class="tile is-child card">
                <UserRate />
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
    <TheFooter />
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
  },
  middleware: 'auth',
  data() {
    return {
      theme: '',
      minPost: null,
    }
  },
  computed: {
    ...mapState('login', ['showStateLogin', 'showStateReg']),
  },
  async mounted() {
    const { data } = await this.$axios.get('/blogs/')
    this.minPost = data.results.slice(0, 3)
  },
}
</script>
<style lang="scss"></style>
