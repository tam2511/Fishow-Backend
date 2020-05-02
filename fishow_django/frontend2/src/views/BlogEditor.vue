<template>
  <div class="container">
    <div class="row row-50" v-if="username">
      <div class="col-lg-7 col-xl-8" v-if="blog_category !== 'Отчет'">
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
              <button
                class="button button-primary button-sm"
                type="button"
                @click="addText"
              >
                Текст
              </button>
              <button
                class="button button-primary button-sm"
                type="button"
                @click="addVideo"
              >
                Видео
              </button>
              <button
                class="button button-primary button-sm"
                type="button"
                @click="addImage"
              >
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
          <div class="col-md-12 error" v-if="error">
            {{ error }}
          </div>
        </form>
      </div>
      <div class="col-lg-7 col-xl-8" v-else>
        <article class="heading-component">
          <div class="heading-component-inner">
            <h5 class="heading-component-title">Добавить отчет</h5>
          </div>
        </article>
        <dynamic-form
          ref="dynamic-form"
          v-model="data"
          :descriptors="descriptors"
          :showOuterError="false"
        >
          <template slot="operations">
            <el-button @click="reset">Reset</el-button>
            <el-button type="primary" @click="validate" plain
              >Validate</el-button
            >
          </template>
        </dynamic-form>
      </div>
      <div class="col-lg-5 col-xl-4">
        <div>
          <label class="typo__label">Выберите категорию:</label>
          <multiselect
            v-model="blog_category"
            :options="optionsCategory"
            :searchable="false"
            :close-on-select="true"
            :show-labels="false"
            placeholder="Pick a value"
          ></multiselect>
        </div>
        <label class="typo__label">Теги:</label>
        <multiselect
          v-model="blog_tags"
          tag-placeholder="Add this as new tag"
          placeholder="Найдите или добавьте свой тег"
          label="name"
          track-by="code"
          :options="options"
          :multiple="true"
          :taggable="true"
          @tag="addTag"
        >
        </multiselect>
        <br />
      </div>
    </div>
    <div class="row row-50" v-else>
      Авторизуйтесь
    </div>
  </div>
</template>

<script>
import { apiService } from '@/common/api.service.js'
import TextField from '@/components/blog/textField'
import imageField from '@/components/blog/imageField'
import BlogContentField from '@/components/blog/blogContentField'
import videoField from '@/components/blog/videoField'
import Multiselect from 'vue-multiselect'
import { mapState } from 'vuex'

export default {
  name: 'BlogEditor',
  components: {
    TextField,
    BlogContentField,
    imageField,
    videoField,
    Multiselect,
  },
  props: {
    slug: {
      type: String,
      required: false,
    },
  },

  data() {
    return {
      picked: null,
      imageCounter: 0,
      textCounter: 1,
      articles: ['BlogContentField'],
      blog_body: '',
      blog_title: null,
      blog_category: 'Блоги',
      deafultTags: ['Удочки', 'Шутки', 'Ночь', 'История', 'Деньги'],
      result: [],
      error: null,
      field: 'textField',
      blog_json: null,
      valueCategory: '',
      blog_tags: [{ name: 'Текст', code: 'текст' }],
      options: [
        { name: 'Видео', code: 'ви' },
        { name: 'Картинки', code: 'os' },
        { name: 'Текст', code: 'текст' },
      ],
      optionsCategory: ['Новости', 'Блоги', 'Статьи', 'Отчет'],
      descriptors: {
        prop1: {
          type: 'string',
          label: 'Место рыбалки',
          required: true,
          message: 'Обязательно укажите место рыбалки',
        },
        prop2: {
          type: 'object',
          label: 'object label',
          fields: {
            prop1: { type: 'email', required: true },
            prop2: { type: 'number', required: true },
            prop3: [
              {
                type: 'string',
                required: true,
                message: 'object label.prop3 is required',
              },
              {
                pattern: /test/,
                message: 'object label.prop3 should include test',
              },
            ],
            prop4: {
              type: 'enum',
              enum: [0, 1],
              label: 'Рыба',
              placeholder: 'sadsad',
              options: [
                // { label: 'Лев', value: 0, disabled: true },
                { label: 'Лев', value: 0 },
                { label: 'Тигр', value: 1 },
              ],
            },
            prop5: { type: 'boolean', required: true },
          },
        },
      },
      data: {},
    }
  },
  computed: {
    ...mapState('user', ['username']),
  },
  methods: {
    // open2() {
    //   this.$message({
    //     message: 'Отлично, у вас получилсоь!',
    //     type: 'success',
    //   })
    // },
    // open3(text) {
    //   this.$message({
    //     message: text,
    //     type: 'warning',
    //   })
    // },
    reset() {
      this.$refs['dynamic-form'].resetFields()
    },
    validate() {
      this.$refs['dynamic-form'].validate()
    },
    addTag(newTag) {
      const tag = {
        name: newTag,
        code: newTag.substring(0, 2) + Math.floor(Math.random() * 10000000),
      }
      this.options.push(tag)
      this.blog_tags.push(tag)
    },
    convertBody() {
      const result = []
      const listBloks = document.querySelectorAll('textarea')

      listBloks.forEach((block) => {
        if (block.name === 'text') {
          result.push({ type: 'text', body: block.value })
        }
        if (block.name === 'image') {
          result.push({ type: 'image', url: block.value })
        }
        if (block.name === 'video') {
          result.push({ type: 'video', url: block.value })
        }
      })
      this.blog_body = JSON.stringify({
        blocks: [result],
      })
    },
    convertTags() {
      this.blog_tags = JSON.stringify(this.blog_tags)
    },
    onSubmit() {
      if (!this.blog_title) {
        // this.open3('Пустой заголовок!')
      } else {
        this.convertTags()
        this.convertBody()

        // this.open2()
        let endpoint = '/api/blogs/'
        let method = 'POST'
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`
          method = 'PUT'
        }
        const blog = {
          title: this.blog_title,
          content: this.blog_body,
          category: this.blog_category,
          tags: this.blog_tags,
        }
        console.log('blog = ', blog)
        apiService(endpoint, method, blog).then((blog_data) => {
          console.log('blog_data = ', blog_data)
          if (blog_data.detail) {
            this.error = 'Что то пошло не так, ошибка = ' + blog_data.detail
          } else {
            this.$router.push({
              name: 'blog',
              params: { slug: blog_data.slug },
            })
          }
        })
      }
    },
    addImage() {
      this.articles.push('imageField')
    },
    addText() {
      this.articles.push('BlogContentField')
    },
    addVideo() {
      this.articles.push('videoField')
    },
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.slug !== undefined) {
      const endpoint = `/api/blogs/${to.params.slug}/`
      const data = await apiService(endpoint)
      return next((vm) => (vm.blog_body = data.content))
    } else {
      return next()
    }
  },
  created() {
    document.title = 'Fishow - Создание блога'
  },
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
.form-wrap {
  display: flex;
  flex-flow: column;
  align-items: center;
  img,
  video {
    margin: 20px;
  }
}
@media screen and (max-width: 500px) {
  .fishow_container {
    justify-content: space-around;
    flex-flow: row;
    align-items: baseline;
  }
}

.fishow_action_btn {
  background-color: var(--background-color-primary);
}
.button.button-primary.button-sm {
  text-overflow: unset;
}
.button-block {
  width: auto;
}
.button {
  &:first-child {
    margin-top: 15px;
  }
  @media screen and (max-width: 840px) {
    width: 100%;
  }
}
.button_send_blog {
  flex-direction: row;
  flex-wrap: wrap;
  display: flex;
  align-items: baseline;
  justify-content: space-evenly;
}
.typo__label {
  color: #0f0f0f;
  font-size: 18px;
}
.dynamic-form {
  background: none !important;
}
</style>
