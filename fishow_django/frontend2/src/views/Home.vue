<template>
  <div class="home">
    <section class="section section-md bg-gray-100">
      <div class="container">
        <div class="row row-50">
          <div class="col-lg-8">
            <div class="main-component">
              <!-- Heading Component-->
              <article class="heading-component">
                <div class="heading-component-inner">
                  <h5 class="heading-component-title">Лучшие блоги</h5>
                  <div class="buttons-nav">
                    <router-link
                            class="button button-xs button-primary"
                            :to="{ name: 'blog-editor' }"
                    >
                      Добавить блог
                    </router-link>
                    <router-link
                            class="button button-xs button-gray-outline"
                            to=""
                            style="margin-top: 0"
                    >
                      Читать все
                    </router-link>
                  </div>
                </div>
              </article>

              <blog-card v-for="blog in blogs"
                         :blog="blog"
                         :key="blog.pk"/>
              <button class="button button-primary button-lg"
                      v-show="next"
                      @click="getBlogs">Load more</button>
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
                      <span
                              class="icon material-icons-whatshot text-red"
                      ></span>
                      Горячие блоги
                    </h5>
                  </div>
                </article>
                <HotPostMinimal
                        v-for="blog in blogs"
                        :blog="blog"
                        :key="blog.pk"
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
    </section>
  </div>
</template>

<script>
  // @ is an alias to /src
import { apiService } from '@/common/api.service'
import HotPostMinimal from '../components/HotPostMinimal'
import MiniPrognos from '../components/MiniPrognos'
import Statistic from '../components/Statistic'
import UserRate from '../components/UserRate'
import LastComments from '../components/LastComments'
import BlogCard from '../components/Home/BlogCard'

export default {
  name: 'home',
  components: {
    BlogCard,
    LastComments,
    UserRate,
    Statistic,
    MiniPrognos,
    HotPostMinimal
  },
  data () {
    return {
      blogs: [],
      next: null,
      loadingBlogs: false
    }
  },
  methods: {
    setPageTitle (title) {
      document.title = title
    },
    getBlogs () {
      let endpoint = '/api/blogs/'
      if (this.next) {
        endpoint = this.next
      }
      this.loadingBlogs = true
      apiService(endpoint).then(data => {
        this.blogs.push(...data.results)
        this.loadingBlogs = false
        if (data.next) {
          this.next = data.next
        } else {
          this.next = null
        }
      })
    }

},
created () {
  this.getBlogs()
  this.setPageTitle('Fishow - Главная')
}
}
</script>
<style>
  .buttons-nav a {
    margin-left: 10px;
  }
</style>
