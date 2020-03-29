<template>
  <section class="section section-variant-1 bg-gray-100">
    <div class="container">
      <div class="row row-50">
        <div class="col-lg-7 col-xl-8">
          <!-- Heading Component-->
          <article class="heading-component">
            <div class="heading-component-inner">
              <h5 class="heading-component-title">Написать блог</h5>


            </div>
          </article>
          <form @submit.prevent="onSubmit">
            <div class="row row-10 row-narrow">
              <div class="col-md-12 fishow-content_container">
                <div class="col-md-12 fishow-content">
                  <div class="form-wrap">
                    <textarea
                            v-model="blog_title"
                            class="form-input"
                            id="blog_title"
                            name="title"
                            placeholder="Заголовок"
                    ></textarea>
                  </div>
                </div>

                <template v-for="(article, index) in articles">
                  <component
                          :is="article"
                          :key="article[index]"
                          :counter="article + index"
                  ></component>
                </template>
              </div>

              <div class="col-md-12 fishow_container">
                <button class="button button-primary button-sm"
                        type="button"
                        @click="addText">
                  Текст
                </button>
                <button class="button button-primary button-sm"
                        type="button"
                        @click="addVideo">
                  Видео
                </button>
                <button class="button button-primary button-sm"
                        type="button"
                        @click="addImage">
                  Картинка
                </button>
              </div>
            </div>
            <div class="col-md-12 button_send_blog">
              <button
                      class="button button-lg button-primary button-block"
                      type="submit"
                      name="send_blog"
              >
                Опубликовать
              </button>
              <button
                      class="button button-lg button-gray-outline button-block"
                      type="button"
                      name="save_blog"
                      onclick=""
                      @click="convertBody"
              >
                Сохранить как черновик
              </button>
            </div>
            <div class="col-md-12">

            </div>
          </form>

        </div>
        <div class="col-lg-5 col-xl-4">
          <input type="radio" id="one" value="Новости" v-model="blog_category" checked>
          <label for="one">Новости</label>
          <input type="radio" id="two" value="Блоги" v-model="blog_category">
          <label for="two">Блоги</label>
          <input type="radio" id="three" value="Статьи" v-model="blog_category">
          <label for="three">Статьи</label>
          <br>
          <h4>Категория: {{ blog_category }}</h4>

          <select v-model="blog_tags" multiple>
            <option>Наука</option>
            <option>Картинки</option>
            <option>Юмор</option>
          </select>
          <br>
          <h5>Selected: {{ blog_tags }}</h5>
        </div>
      </div>
    </div>
  </section>
  <!--    </div>-->
</template>

<script>
  import { apiService } from "@/common/api.service.js";
  import TextField from "../components/blog/textField";
  import imageField from "../components/blog/imageField";
  import BlogContentField from "../components/blog/blogContentField";
  import videoField from "../components/blog/videoField";
  export default {
    name: "BlogEditor",
    components: {TextField,BlogContentField,imageField,videoField},
    props: {
      slug: {
        type: String,
        required: false
      }
    },

    data() {
      return {
        picked: null,
        imageCounter: 0,
        textCounter: 1,
        articles: ['BlogContentField'],
        blog_body: '',
        blog_title: null,
        blog_category: null,
        blog_tags:{},
        result: [],
        error: null,
        field: "textField",
        blog_json: null
      };
    },
    methods: {
      convertBody() {
        const result = [];
        const listBloks = document.querySelectorAll('textarea');

        listBloks.forEach((block) => {
          if (block.name === 'text') {
            result.push({'type':'text','body':block.value})
          }
          if (block.name === 'image') {
            result.push({'type':'image','url':block.value})
          }
          if (block.name === 'video') {
            result.push({'type':'video','url':block.value})
          }
        });
        this.blog_body = JSON.stringify({
          "tags":"Картинка с текстом,Картинки",
          "is_authors":false,
          "is_adult":false,
          "is_community":false,
          "blocks":[
            result
          ]
        });
      },
      convertTags() {
        this.blog_tags = JSON.stringify(this.blog_tags);
      },
      onSubmit() {
        this.convertTags();
        this.convertBody();

        if (!this.blog_body) {
          this.error = "You can't send an empty blog!";
        } else if (this.blog_body.length > 400) {
          this.error = "To much words in your blog";
        } else {
          let endpoint = "/api/blogs/";
          let method = "POST";
          if (this.slug !== undefined) {
            endpoint += `${this.slug}/`;
            method = "PUT";
          }
          apiService(endpoint, method, {
            title: this.blog_title,
            content: this.blog_body,
            category: this.blog_category,
            tags: this.blog_tags
          }).then(blog_data => {
            this.$router.push({
              name: "blog",
              params: { slug: blog_data.slug }
            });
          });
        }
      },
      addImage() {
        this.articles.push("imageField");
      },
      addText() {
        this.articles.push("BlogContentField");
      },
      addVideo() {
        this.articles.push("videoField");
      }
    },
    async beforeRouteEnter(to, from, next) {
      // if the component will be used to update a question, then get the question's data from the REST API
      if (to.params.slug !== undefined) {
        let endpoint = `/api/blogs/${to.params.slug}/`;
        let data = await apiService(endpoint);
        return next(vm => (vm.blog_body = data.content));
      } else {
        return next();
      }
    },
    created() {
      document.title = "Fishow - Создание блога";
    }
  };
</script>

<style lang="scss">
  .form-wrap {
    display: flex;
    flex-flow: column;
    align-items: center;
    img,
    video {
      margin: 20px;
    }
  }
  @media screen and (max-width: 500px){
    .fishow_container {
      justify-content: space-around;
      flex-flow: row;
      align-items: baseline;
    }
  }

  .fishow_action_btn {
    background-color: #18636b;
  }
  .button-block {
    width: auto;
  }
  .button_send_blog {
    flex-direction: row;
    flex-wrap: wrap;
    display: flex;
    align-items: baseline;
    justify-content: space-evenly;
  }
</style>