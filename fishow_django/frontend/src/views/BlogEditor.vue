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
                <div class="form-wrap">
                                        <textarea
                                                v-model="blog_title"
                                                name="blog_body"
                                                class="form-control"
                                                placeholder="Write here text of your blog"
                                                cols="30"
                                                rows="4">
                                        </textarea>
                  <textarea
                          v-model="blog_body"
                          name="blog_body"
                          class="form-control"
                          placeholder="Write here text of your blog"
                          cols="30"
                          rows="4">
                                        </textarea>
                </div>
<!--                <template v-for="(article, index) in articles">-->
<!--                  <component-->
<!--                    :is="article"-->
<!--                    :key="article[index]"-->
<!--                    :counter="article + articles.length"-->
<!--                  ></component>-->
<!--                </template>-->
              </div>
              <div class="col-md-12 fishow_container">
                <div class="fishow_button_text">
                  <button class="fishow_action_btn" @click="addText">Текст</button>
                </div>
                <div class="fishow_button_video">
                  <button class="fishow_action_btn" @click="addVideo">Видео</button>
                </div>
                <div class="fishow_button_picture">
                  <button class="fishow_action_btn" @click="addImage">Картинка</button>
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <button
                class="button button-lg button-google button-block"
                type="submit"
                name="send_blog"
              >
                Опубликовать
              </button>
            </div>
            <div class="col-md-12">
              <button
                class="button button-lg button-primary button-block"
                type="submit"
                name="save_blog"
                onclick=""
              >
                Сохранить как черновик
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
  <!--    </div>-->
</template>

<script>
import { apiService } from "@/common/api.service.js";
// import TextField from "../components/blog/textField";
// import imageField from "../components/blog/imageField";
// import BlogContentField from "../components/blog/blogContentField";
// import videoField from "../components/blog/videoField";
export default {
  name: "BlogEditor",
  components: {  },
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      imageCounter: 0,
      textCounter: 1,
      articles: ["TextField", "BlogContentField", "imageField", "videoField"],
      blog_body: null,
      blog_title: null,
      error: null,
      field: "textField"
    };
  },
  methods: {
    onSubmit() {
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
          content: this.blog_body
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
</style>