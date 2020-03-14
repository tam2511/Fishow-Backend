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
                              <!--                                {% if Hot_blogs is not none %} {% for Hot_blog in Hot_blogs %}-->
                              <!-- List Post minimal-->
                              <div class="list-post-minimal">
                                  <!-- Post Minimal-->
                                  <article class="post-minimal">
                                      <div class="post-classic-main">
                                          <p class="post-classic-title">
                                              <a href="#"> Hot_blog.title </a>
                                          </p>
                                          <div class="post-minimal_comments">
                                              <div class="badge badge-primary">Категория</div>
                                              <div class="post-corporate-author">Имя автора тут</div>
                                              <time class="post-classic-time">
                                                  <!--                                                     Hot_blog.data_add|date:'d.m.Y' -->
                                              </time>
                                          </div>
                                      </div>
                                  </article>
                              </div>
                              <!--                                {% endfor %} {% endif %}-->
                          </div>
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Прогнозы</h5>
                                  </div>
                              </article>
                              <!-- Game Result Classic-->
                              <article class="game-result game-result-classic">
                                  <div class="game-result-main">
                                      <div class="game-result-team game-result-team-first">
                                          <div style="font-size: 35px">2%</div>
                                          <div class="game-result-team-name">Прогноз клева</div>
                                      </div>
                                      <div class="game-result-team game-result-team-second">
                                          <span>Скорость ветра: 10м/с</span>
                                          <span>Темп. воздуха: -16 C</span>
                                          <div class="game-result-team-name">Погодные условия</div>
                                      </div>
                                  </div>
                                  <div class="game-result-footer">
                                      <ul class="game-result-details" style="font-weight: 800">
                                          <li>Сом</li>
                                          <li>р.Кама</li>
                                          <li><time datetime="2018-04-14">16-02-2020</time></li>
                                      </ul>
                                  </div>
                              </article>
                              <!-- Game Result Classic-->
                              <article class="game-result game-result-classic">
                                  <div class="game-result-main">
                                      <div class="game-result-team game-result-team-first">
                                          <div style="font-size: 35px">65%</div>
                                          <div class="game-result-team-name">Прогноз клева</div>
                                      </div>
                                      <div class="game-result-team game-result-team-second">
                                          <span>Скорость ветра: 10м/с</span>
                                          <span>Темп. воздуха: -16 C</span>
                                          <div class="game-result-team-name">Погодные условия</div>
                                      </div>
                                  </div>
                                  <div class="game-result-footer">
                                      <ul class="game-result-details" style="font-weight: 800">
                                          <li>Лещ</li>
                                          <li>р.Кама</li>
                                          <li><time datetime="2018-04-14">16-02-2020</time></li>
                                      </ul>
                                  </div>
                              </article>
                              <!-- Game Result Classic-->
                              <article class="game-result game-result-classic">
                                  <div class="game-result-main">
                                      <div class="game-result-team game-result-team-first">
                                          <div style="font-size: 35px">74%</div>
                                          <div class="game-result-team-name">Прогноз клева</div>
                                      </div>
                                      <div class="game-result-team game-result-team-second">
                                          <span>Скорость ветра: 3 м/с</span>
                                          <span>Темп. воздуха: 3 C</span>
                                          <div class="game-result-team-name">Погодные условия</div>
                                      </div>
                                  </div>
                                  <div class="game-result-footer">
                                      <ul class="game-result-details" style="font-weight: 800">
                                          <li>Лещ</li>
                                          <li>р.Кама</li>
                                          <li><time datetime="2018-04-14">16-02-2020</time></li>
                                      </ul>
                                  </div>
                              </article>
                          </div>
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Статистика</h5>
                                  </div>
                              </article>
                              <div class="table-custom-responsive">
                                  <table
                                          class="table-custom table-custom-bordered table-team-statistic"
                                  >
                                      <tbody>
                                      <tr>
                                          <td>
                                              <p class="team-statistic-counter">109</p>
                                              <p class="team-statistic-title">Points Per Game</p>
                                          </td>
                                          <td>
                                              <p class="team-statistic-counter">65</p>
                                              <p class="team-statistic-title">Rebounds Per Game</p>
                                          </td>
                                      </tr>
                                      <tr>
                                          <td>
                                              <p class="team-statistic-counter">23.6</p>
                                              <p class="team-statistic-title">Assists Per Game</p>
                                          </td>
                                          <td>
                                              <p class="team-statistic-counter">102</p>
                                              <p class="team-statistic-title">Points Allowed</p>
                                          </td>
                                      </tr>
                                      </tbody>
                                  </table>
                              </div>
                          </div>
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
                              <div class="table-custom-responsive">
                                  <table class="table-custom table-standings table-classic">
                                      <thead>
                                      <tr>
                                          <th colspan="2">Пользователи</th>
                                          <th>Сообщ.</th>
                                          <th>Блогов</th>
                                      </tr>
                                      </thead>
                                      <tbody>
                                      <tr>
                                          <td><span>1</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="42"
                                                          height="26"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>153</td>
                                          <td>30</td>
                                      </tr>
                                      <tr>
                                          <td><span>2</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="35"
                                                          height="35"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>120</td>
                                          <td>30</td>
                                      </tr>
                                      <tr>
                                          <td><span>3</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="39"
                                                          height="30"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>100</td>
                                          <td>30</td>
                                      </tr>
                                      <tr>
                                          <td><span>4</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="38"
                                                          height="30"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>98</td>
                                          <td>30</td>
                                      </tr>
                                      <tr>
                                          <td><span>5</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="35"
                                                          height="35"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>98</td>
                                          <td>30</td>
                                      </tr>
                                      <tr>
                                          <td><span>6</span></td>
                                          <td class="team-inline">
                                              <div class="team-figure">
                                                  <img
                                                          src=""
                                                          alt=""
                                                          width="35"
                                                          height="36"
                                                  />
                                              </div>
                                              <div class="team-title">
                                                  <div class="team-name">Имя</div>
                                                  <div class="team-country">Фамилия</div>
                                              </div>
                                          </td>
                                          <td>98</td>
                                          <td>30</td>
                                      </tr>
                                      </tbody>
                                  </table>
                              </div>
                          </div>
                          <div class="aside-component">
                              <!-- Heading Component-->
                              <article class="heading-component">
                                  <div class="heading-component-inner">
                                      <h5 class="heading-component-title">Последние комментарии</h5>
                                  </div>
                              </article>
                          </div>
                          <!-- List Comments Classic-->
                          <div class="list-comments-classic">
                              <!-- Comment Classic-->
                              <div class="comment-classic">
                                  <svg
                                          version="1.1"
                                          x="0px"
                                          y="0px"
                                          width="6.888px"
                                          height="4.68px"
                                          viewBox="0 0 6.888 4.68"
                                          enable-background="new 0 0 6.888 4.68"
                                          xml:space="preserve"
                                  >
                <path
                        fill="#171617"
                        d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"
                ></path>
              </svg>
                                  <div class="comment-classic-header">
                                      <div class="comment-classic-header-aside">
                                          <img
                                                  src=""
                                                  alt=""
                                                  width="63"
                                                  height="63"
                                          />
                                      </div>
                                      <div class="comment-classic-header-main">
                                          <p class="comment-classic-title">Amanda Norton</p>
                                          <time class="comment-classic-time" datetime="2018">
                                              4 hours ago
                                          </time>
                                      </div>
                                  </div>
                                  <div class="comment-classic-body">
                                      <div class="comment-classic-text">
                                          <p>
                                              I am not really a big fan of basketball but even I am sure
                                              that Rockets are going to make it this time just like they
                                              did 3 years...
                                          </p>
                                      </div>
                                      <div class="comment-classic-post-title">
                                          <a href="">
                                              Six Big Questions for the Spurs-Rockets Heavyweight Clash
                                          </a>
                                      </div>
                                  </div>
                              </div>
                              <!-- Comment Classic-->
                              <div class="comment-classic">
                                  <svg
                                          version="1.1"
                                          x="0px"
                                          y="0px"
                                          width="6.888px"
                                          height="4.68px"
                                          viewBox="0 0 6.888 4.68"
                                          enable-background="new 0 0 6.888 4.68"
                                          xml:space="preserve"
                                  >
                <path
                        fill="#171617"
                        d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"
                ></path>
              </svg>
                                  <div class="comment-classic-header">
                                      <div class="comment-classic-header-aside">
                                          <img
                                                  src=""
                                                  alt=""
                                                  width="63"
                                                  height="63"
                                          />
                                      </div>
                                      <div class="comment-classic-header-main">
                                          <p class="comment-classic-title">Robert Norton</p>
                                          <time class="comment-classic-time" datetime="2018">
                                              14 hours ago
                                          </time>
                                      </div>
                                  </div>
                                  <div class="comment-classic-body">
                                      <div class="comment-classic-text">
                                          <p>Bulls are my personal favorites, and I don’t...</p>
                                      </div>
                                      <div class="comment-classic-post-title">
                                          <a href="">
                                              Which Team will Win the World Championship Series This Year
                                              ?
                                          </a>
                                      </div>
                                  </div>
                              </div>
                              <!-- Comment Classic-->
                              <div class="comment-classic">
                                  <svg
                                          version="1.1"
                                          x="0px"
                                          y="0px"
                                          width="6.888px"
                                          height="4.68px"
                                          viewBox="0 0 6.888 4.68"
                                          enable-background="new 0 0 6.888 4.68"
                                          xml:space="preserve"
                                  >
                <path
                        fill="#171617"
                        d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"
                ></path>
              </svg>
                                  <div class="comment-classic-header">
                                      <div class="comment-classic-header-aside">
                                          <img
                                                  src=""
                                                  alt=""
                                                  width="63"
                                                  height="63"
                                          />
                                      </div>
                                      <div class="comment-classic-header-main">
                                          <p class="comment-classic-title">Rebecca Smith</p>
                                          <time class="comment-classic-time" datetime="2018">
                                              20 hours ago
                                          </time>
                                      </div>
                                  </div>
                                  <div class="comment-classic-body">
                                      <div class="comment-classic-text">
                                          <p>
                                              My opinion on the topic is that Spurs don’t have enough
                                              chances to withstand the...
                                          </p>
                                      </div>
                                      <div class="comment-classic-post-title">
                                          <a href="">
                                              Six Big Questions for the Spurs-Rockets Heavyweight Clash
                                          </a>
                                      </div>
                                  </div>
                              </div>
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
// import HelloWorld from '@/components/HelloWorld.vue'
import { apiService } from "@/common/api.service";

export default {
  name: 'home',
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
