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
                <nuxt-link
                  class="button button-xs button-primary"
                  to="/blog-editor"
                >
                  Добавить блог
                </nuxt-link>
                <nuxt-link
                  class="button button-xs button-gray-outline"
                  to="/Article"
                  style="margin-top: 0;"
                >
                  Читать все
                </nuxt-link>
              </div>
            </div>
          </article>
          <!--          <transition-group name="slide-fade" appear tag="div">-->
          <!--          {{ blogs }}-->
          <BlogCard v-for="blog in blogs" :key="blog.id" :blog="blog" />
          <!--          {{ blogs }}-->
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
            <HotPostMinimal
              v-for="blog in minPost"
              :key="blog.id"
              :blog="blog"
            />
          </div>
          <!-- Мини прогнозы -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">Прогнозы</h5>
              </div>
            </article>
            <MiniPrognos />
          </div>
          <!-- Статистика -->
          <div class="aside-component">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">Статистика</h5>
              </div>
            </article>
            <Statistic />
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
            <UserRate />
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
            <last-comments />
          </div>
        </aside>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import HotPostMinimal from '@/components/HotPostMinimal'
import MiniPrognos from '@/components/MiniPrognos'
import Statistic from '@/components/Statistic'
import UserRate from '@/components/UserRate'
import LastComments from '@/components/LastComments'
import BlogCard from '@/components/BlogCard'
export default {
  middleware: 'auth',
  components: {
    BlogCard,
    LastComments,
    UserRate,
    Statistic,
    MiniPrognos,
    HotPostMinimal,
  },
  async fetch({ store, error }) {
    try {
      await store.dispatch('blogs/getBlogs')
    } catch (e) {
      error({
        statusCode: 503,
        message: 'Unable to fetch events at this time. Please try again.',
      })
    }
  },
  computed: {
    minPost() {
      return this.blogs.filter((blog, index) => index < 3)
    },
    ...mapState('blogs', ['blogs']),
  },
  created() {},
  head() {
    return {
      title: 'Fishow - Главная',
    }
  },
}
</script>

<style lang="scss">
@import '~/assets/scss/custom-styles/style.scss';
@import '~/assets/scss/fishowStyles.scss';
@import '~/assets/scss/custom-styles/fonts.scss';
</style>
