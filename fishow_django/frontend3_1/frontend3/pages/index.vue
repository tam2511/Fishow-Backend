<template>
  <div class="container">
    <div class="row row-50">
      <div class="col-lg-8">
        <div class="main-component">
          <!-- Heading Component-->
          <article class="heading-component">
            <div class="heading-component-inner">
              <h5 class="heading-component-title">Лучшие блоги</h5>
              <div class="buttons-nav">
                <!--                <router-link-->
                <!--                  class="button button-xs button-primary"-->
                <!--                  :to="{ name: 'blog-editor' }"-->
                <!--                >-->
                <!--                  Добавить блог-->
                <!--                </router-link>-->
                <!--                <router-link-->
                <!--                  class="button button-xs button-gray-outline"-->
                <!--                  to="/article"-->
                <!--                  style="margin-top: 0;"-->
                <!--                >-->
                <!--                  Читать все-->
                <!--                </router-link>-->
              </div>
            </div>
          </article>
          <!--          <transition-group name="slide-fade" appear tag="div">-->
          <!--          <blog-card v-for="(blog, index) in blogs" :key="index" :blog="blog" />-->
          {{ blogs }}
          <!--          </transition-group>-->

          <!--          <button-->
          <!--            v-show="next"-->
          <!--            class="button button-primary button-lg"-->
          <!--            @click="checkNext"-->
          <!--          >-->
          <!--            Загрузить больше-->
          <!--          </button>-->
        </div>
      </div>
      <!-- Aside Block-->
      <div class="col-lg-4">
        <aside class="aside-components">
          <!-- Мини блок поста -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">
                  <span class="icon material-icons-whatshot text-red"></span>
                  Горячие блоги
                </h5>
              </div>
            </article>
            <!--            <HotPostMinimal-->
            <!--              v-for="blog in minPost"-->
            <!--              :key="blog.pk"-->
            <!--              :blog="blog"-->
            <!--            />-->
          </div>
          <!-- Мини прогнозы -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">Прогнозы</h5>
              </div>
            </article>
            <!--            <MiniPrognos />-->
          </div>
          <!-- Статистика -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">Статистика</h5>
              </div>
            </article>
            <!--            <Statistic />-->
          </div>
          <!-- Пользователи -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">Рейтинг</h5>
                <a class="button button-xs button-gray-outline" href="#">
                  Все пользователи
                </a>
              </div>
            </article>
            <!-- Table team-->
            <!--            <UserRate />-->
          </div>
          <!-- List Comments Classic-->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">
                  Последние комментарии
                </h5>
              </div>
            </article>
            <!--            <last-comments />-->
          </div>
        </aside>
      </div>
    </div>
  </div>
</template>

<script>
// import { mapState, mapActions } from 'vuex'
// import HotPostMinimal from '@/components/HotPostMinimal'
// import MiniPrognos from '@/components/MiniPrognos'
// import Statistic from '@/components/Statistic'
// import UserRate from '@/components/UserRate'
// import LastComments from '@/components/LastComments'
// import BlogCard from '@/components/Home/BlogCard'
// import axios from '~/.nuxt/axios'
export default {
  components: {
    // BlogCard
    // LastComments,
    // UserRate,
    // Statistic,
    // MiniPrognos,
    // HotPostMinimal
  },
  // computed: {
  //   minPost() {
  //     return this.blogs.filter((blog, index) => index < 3)
  //   },
  //   ...mapState('blogs', ['blogs', 'next'])
  // },
  head() {
    return {
      title: 'Fishow - Главная'
    }
  },
  async asyncData({ $axios }) {
    try {
      const blogs = await $axios.$get('/blogs/')
      return { blogs }
    } catch (e) {
      return { blogs: [] }
    }
  },
  fetchOnServer: false,
  data() {
    return {
      blogs: []
    }
  },
  created() {
    console.log('privey')
  }
  // methods: {
  //   checkNext() {
  //     this.$store.dispatch('blogs/fetchBlogs')
  //   },
  //   ...mapActions('blogs', ['fetchBlogs'])
  // }
}
</script>

<style lang="scss" scoped>
.buttons-nav a {
  margin-left: 10px;
}
.col-lg-4 {
  @media screen and (min-width: 1024px) {
    .aside-components__sticky {
      position: fixed;
      width: 30%;
    }
  }
}
</style>
