<!--<template>-->
<!--  <div class="container">-->
<!--    <div class="row row-50">-->
<!--      <div class="col-lg-8">-->
<!--        <div class="main-component">-->
<!--          &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--          <article class="heading-component">-->
<!--            <div class="heading-component-inner">-->
<!--              <h5 class="heading-component-title">Лучшие блоги</h5>-->
<!--              <div class="buttons-nav">-->
<!--                <nuxt-link-->
<!--                  class="button button-xs button-primary"-->
<!--                  to="/blog-editor"-->
<!--                >-->
<!--                  Добавить блог-->
<!--                </nuxt-link>-->
<!--                <nuxt-link-->
<!--                  class="button button-xs button-gray-outline"-->
<!--                  to="/Article"-->
<!--                  style="margin-top: 0;"-->
<!--                >-->
<!--                  Читать все-->
<!--                </nuxt-link>-->
<!--              </div>-->
<!--            </div>-->
<!--          </article>-->
<!--          &lt;!&ndash;          <transition-group name="slide-fade" appear tag="div">&ndash;&gt;-->
<!--          &lt;!&ndash;          {{ blogs }}&ndash;&gt;-->
<!--          <BlogCard v-for="blog in blogs" :key="blog.id" :blog="blog" />-->
<!--          &lt;!&ndash;          {{ blogs }}&ndash;&gt;-->
<!--          &lt;!&ndash;          </transition-group>&ndash;&gt;-->

<!--          &lt;!&ndash;          <button&ndash;&gt;-->
<!--          &lt;!&ndash;            v-show="next"&ndash;&gt;-->
<!--          &lt;!&ndash;            class="button button-primary button-lg"&ndash;&gt;-->
<!--          &lt;!&ndash;            @click="checkNext"&ndash;&gt;-->
<!--          &lt;!&ndash;          >&ndash;&gt;-->
<!--          &lt;!&ndash;            Загрузить больше&ndash;&gt;-->
<!--          &lt;!&ndash;          </button>&ndash;&gt;-->
<!--        </div>-->
<!--      </div>-->
<!--      &lt;!&ndash; Aside Block&ndash;&gt;-->
<!--      <div class="col-lg-4">-->
<!--        <aside class="aside-components">-->
<!--          &lt;!&ndash; Мини блок поста &ndash;&gt;-->
<!--          <div class="aside-component">-->
<!--            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--            <article class="heading-component">-->
<!--              <div class="heading-component-inner">-->
<!--                <h5 class="heading-component-title">-->
<!--                  <span class="icon material-icons-whatshot text-red"></span>-->
<!--                  Горячие блоги-->
<!--                </h5>-->
<!--              </div>-->
<!--            </article>-->
<!--            <HotPostMinimal-->
<!--              v-for="blog in minPost"-->
<!--              :key="blog.id"-->
<!--              :blog="blog"-->
<!--            />-->
<!--          </div>-->
<!--          &lt;!&ndash; Мини прогнозы &ndash;&gt;-->
<!--          <div class="aside-component">-->
<!--            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--            <article class="heading-component">-->
<!--              <div class="heading-component-inner">-->
<!--                <h5 class="heading-component-title">Прогнозы</h5>-->
<!--              </div>-->
<!--            </article>-->
<!--            <MiniPrognos />-->
<!--          </div>-->
<!--          &lt;!&ndash; Статистика &ndash;&gt;-->
<!--          <div class="aside-component">-->
<!--            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--            <article class="heading-component">-->
<!--              <div class="heading-component-inner">-->
<!--                <h5 class="heading-component-title">Статистика</h5>-->
<!--              </div>-->
<!--            </article>-->
<!--            <Statistic />-->
<!--          </div>-->
<!--          &lt;!&ndash; Пользователи &ndash;&gt;-->
<!--          <div class="aside-component">-->
<!--            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--            <article class="heading-component">-->
<!--              <div class="heading-component-inner">-->
<!--                <h5 class="heading-component-title">Рейтинг</h5>-->
<!--                <a class="button button-xs button-gray-outline" href="#">-->
<!--                  Все пользователи-->
<!--                </a>-->
<!--              </div>-->
<!--            </article>-->
<!--            &lt;!&ndash; Table team&ndash;&gt;-->
<!--            <UserRate />-->
<!--          </div>-->
<!--          &lt;!&ndash; List Comments Classic&ndash;&gt;-->
<!--          <div class="aside-component">-->
<!--            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--            <article class="heading-component">-->
<!--              <div class="heading-component-inner">-->
<!--                <h5 class="heading-component-title">-->
<!--                  Последние комментарии-->
<!--                </h5>-->
<!--              </div>-->
<!--            </article>-->
<!--            <last-comments />-->
<!--          </div>-->
<!--        </aside>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<template>
  <div class="tile">
    <div class="tile is-vertical is-8">
      <p class="title">Последние записи</p>
      <div class="tile is-parent is-vertical">
        <article v-for="blog in blogs" :key="blog.id" class="tile is-child">
          <BlogCard :blog="blog" />
        </article>
      </div>
    </div>
    <div class="tile is-vertical is-4">
      <article class="tile is-parent is-vertical">
        <p class="title">Горячие блоги</p>
        <div class="tile is-child">
          <HotPostMinimal v-for="blog in minPost" :key="blog.id" :blog="blog" />
        </div>
      </article>
      <article class="tile is-parent is-vertical">
        <p class="title">Прогнозы</p>
        <div class="tile is-child box"></div>
      </article>
      <article class="tile is-parent is-vertical">
        <p class="title">Статистика</p>
        <div class="tile is-child box"></div>
      </article>
      <article class="tile is-parent is-vertical">
        <p class="title">Последние комментарии</p>
        <div class="tile is-child box"></div>
      </article>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import HotPostMinimal from '@/components/HotPostMinimal'
// import MiniPrognos from '@/components/MiniPrognos'
// import Statistic from '@/components/Statistic'
// import UserRate from '@/components/UserRate'
// import LastComments from '@/components/LastComments'
import BlogCard from '@/components/BlogCard'
export default {
  middleware: 'auth',
  components: {
    BlogCard,
    // LastComments,
    // UserRate,
    // Statistic,
    // MiniPrognos,
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

<style lang="scss" scoped>
.tile.is-parent.is-vertical {
  flex-grow: initial;
}
</style>
