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
                                  <div class="">
                                      <router-link
                                              class="button button-xs button-primary"
                                              :to="{ name: 'blog-editor'}"
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


                          <article class="post-corporate"  v-for="blog in blogs"
                                   :key="blog.pk">
                              <div class="post-corporate-content">
                                  <div class="fishow-votes_container">
                                      <div class="fishow_votes" data-vote-status="" >
                                          <svg class="fishow-votes_up" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                                               width="284.929px" height="284.929px" viewBox="0 0 284.929 284.929"
                                               xml:space="preserve">
	<path d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"/>
</svg>
                                          <svg class="fishow-votes_down" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                                               width="284.929px" height="284.929px" viewBox="0 0 284.929 284.929"
                                               xml:space="preserve" >
	<path d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"/>
</svg>
                                      </div>
                                      <span data-votes-counter></span>
                                      <div class="post-corporate-header">
                                          <!-- Badge-->
                                          <div class="badge badge-primary">Категория</div>
                                          <time class="post-corporate-time">

                                          </time>
                                          <div class="post-corporate-author">
                                              Автор:
                                              <span>{{ blog.author }}</span>
                                          </div>
                                          <div class="post-corporate-view">
                                              <span class="icon fl-justicons-visible6"></span>
                                              0
                                          </div>
                                      </div>
                                  </div>

                                  <h4 class="post-corporate-title">
                                      <router-link :to="{ name: 'blog', params: { slug: blog.slug } }">{{ blog.title }}</router-link>
                                  </h4>
                                  <div class="post-corporate-text">
                                      <p>{{ blog.content }}</p>
                                  </div>
                              </div>
                              <a class="post-corporate-figure" href="">

                                  <img src="" alt='' width='769' height='416'>
                              </a>
                              <div class="post-corporate-footer">
                                  <div class="post-corporate-comment">
                                      <span class="icon mdi mdi-comment-outline"></span>
                                      <router-link :to="{ name: 'blog', params: { slug: blog.slug } }">{{ blog.comments_count }} Комментариев</router-link>
                                  </div>
                                  <div class="post-corporate-share">
                                      <ul class="group">
                                          <li>Share</li>
                                          <li><a class="icon fa-facebook" href="#"></a></li>
                                          <li><a class="icon fa-twitter" href="#"></a></li>
                                          <li><a class="icon fa-google-plus" href="#"></a></li>
                                          <li><a class="icon fa-instagram" href="#"></a></li>
                                      </ul>
                                  </div>
                              </div>
                          </article>



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
                                <HotPostMinimal/>
                          </div>
                          <!-- Мини прогнозы -->
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Прогнозы</h5>
                                  </div>
                              </article>
                              <MiniPrognos/>
                          </div>
                          <!-- Статистика -->
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Статистика</h5>
                                  </div>
                              </article>
                              <Statistic/>
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
                              <UserRate/>
                          </div>
                          <!-- List Comments Classic-->
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Последние комментарии</h5>
                                  </div>
                              </article>
                              <last-comments/>
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
import { apiService } from "@/common/api.service";
import HotPostMinimal from "../components/HotPostMinimal";
import MiniPrognos from "../components/MiniPrognos";
import Statistic from "../components/Statistic";
import UserRate from "../components/UserRate";
import LastComments from "../components/LastComments";

export default {
  name: 'home',
    components: {LastComments, UserRate, Statistic, MiniPrognos, HotPostMinimal},
    data() {
      return {
          blogs: [],
          next: null,
          loadingBlogs: false
      }
  },
  methods: {
      setPageTitle(title) {
          document.title = title;
      },
      getBlogs() {
          let endpoint = "/api/blogs/";
          if (this.next) {
              endpoint = this.next;
          }
          this.loadingBlogs = true;
          apiService(endpoint)
            .then(data => {
                this.blogs.push(...data.results);
                if (data.next) {
                    this.next = data.next;
                } else {
                    this.next = null;
                }
            })
      }
  },
    created() {
        this.getBlogs();
        this.setPageTitle("Fishow - Главная")
    }
}
</script>
