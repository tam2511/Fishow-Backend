<template>
  <div class="tile container">
    <div class="tile is-vertical is-8">
      <p class="title">Написать блог</p>
      <div class="tile is-parent is-vertical box">
        <div class="field">
          <label for="blog_title" class="label">Заголовок</label>
          <div class="control">
            <input
              id="blog_title"
              v-model="blog_title"
              type="text"
              class="input"
              placeholder="Заголовок"
            />
          </div>
        </div>
        <template v-for="(article, index) in articles">
          <component
            :is="article"
            :key="article[index]"
            :counter="article + index"
          ></component>
        </template>
        <div class="buttons">
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
        <div class="buttons">
          <button
            class="button is-success"
            type="button"
            name="send_blog"
            @click="onSubmit"
          >
            Опубликовать
          </button>
          <button
            class="button is-info"
            type="button"
            name="save_blog"
            disabled
          >
            Сохранить как черновик
          </button>
        </div>
      </div>
    </div>
    <div class="tile is-vertical is-4">
      <p class="title">Настройки</p>
      <div class="tile is-parent is-vertical box">
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
        <div>
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
            @input="clearError"
            @tag="addTag"
          >
          </multiselect>
          <div v-if="errorTags" class="errors">
            {{ errorTags }}
          </div>
        </div>
      </div>
    </div>
    <div v-if="!$auth.loggedIn" class="warning-overlay">
      <warning
        title="Оповещение"
        body="Для возможности создания блога вам необходимо авторизоваться"
        button="Войти"
        redirect="/login"
      />
    </div>
  </div>
</template>

<script>
// import { mapState } from 'vuex'
import Warning from '@/components/Warning'
// import TextField from '@/components/blog/textField'
import imageField from '@/components/blog/imageField'
import BlogContentField from '@/components/blog/blogContentField'
import videoField from '@/components/blog/videoField'

export default {
  components: {
    Warning,
    // TextField,
    BlogContentField,
    imageField,
    videoField,
  },
  // props: {
  //   slug: {
  //     type: String,
  //     required: false,
  //     default: null
  //   }
  // },

  data() {
    return {
      articles: ['BlogContentField'],
      blog_body: '',
      blog_title: null,
      blog_category: 'Блоги',
      blog_tags: [{ name: 'Текст', code: 'текст' }],
      options: [
        { name: 'Видео', code: 'ви' },
        { name: 'Картинки', code: 'os' },
        { name: 'Текст', code: 'текст' },
      ],
      optionsCategory: ['Новости', 'Блоги', 'Статьи', 'Отчет'],
      errorTags: '',
    }
  },
  methods: {
    error(text) {
      const notif = this.$buefy.notification.open({
        duration: 5000,
        message: text,
        position: 'is-bottom-right',
        type: 'is-danger',
        hasIcon: true,
      })
      notif.$on('close', () => {
        // this.$buefy.notification.open('Custom notification closed!')
      })
    },
    addTag(newTag) {
      const tag = {
        name: newTag,
        code: newTag.substring(0, 2) + Math.floor(Math.random() * 10000000),
      }
      this.options.push(tag)
      this.blog_tags.push(tag)
    },
    clearError() {
      if (this.errorTags) this.errorTags = null
    },
    convertBody() {
      const result = []
      const listBloks = [...document.querySelectorAll('textarea')]

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
    addImage() {
      this.articles.push('imageField')
    },
    addText() {
      this.articles.push('BlogContentField')
    },
    addVideo() {
      this.articles.push('videoField')
    },
    async onSubmit() {
      try {
        if (!this.blog_title) return this.error('Нужно заполнить поля')
        this.convertTags()
        this.convertBody()
        if (!this.blog_body) return this.error('Нужно заполнить поля')
        const blog = {
          title: this.blog_title,
          content: this.blog_body,
          category: this.blog_category,
          tags: this.blog_tags,
        }
        const response = await this.$axios.$post('/blogs/', blog)
        this.$router.push({
          name: 'blog-slug',
          params: { slug: response.slug },
        })
      } catch (e) {
        // console.log('error = ', e.response)
        if (e.response && e.response.data && e.response.data.tags) {
          this.blog_tags = [{ name: 'Текст', code: 'текст' }]
          this.errorTags = 'Слишком много тэгов'
        }
        if (e.response && e.response.data && e.response.data.content) {
          if (
            e.response.data.content[0] ===
            'Ensure this field has no more than 5000 characters.'
          ) {
            this.error('Максимум 5000 символов')
          }
        }
      }
    },
  },
  // async beforeRouteEnter(to, from, next) {
  // if the component will be used to update a question, then get the question's data from the REST API
  // if (to.params.slug !== undefined) {
  // const endpoint = `/api/blogs/${to.params.slug}/`
  // const data = await apiService(endpoint)
  // return next(vm => (vm.blog_body = data.content))
  // } else {
  //   return next()
  // }
  // }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
.tile.is-vertical.is-8 {
  padding-right: 20px;
}
</style>
