<template>
  <div class="tile container">
    <div class="tile is-vertical is-12">
      <h1 class="title">Написать статью</h1>
      <div class="tile is-parent is-vertical box">
        <b-field>
          <b-input v-model="blog_title" placeholder="Заголовок"></b-input>
        </b-field>
        <template v-for="(article, index) in articles">
          <component
            :is="article"
            :key="article[index] + index"
            :counter="article + index"
            @input.passive="fillBlog"
            @remove="removeElement"
          ></component>
        </template>
        <div class="buttons">
          <button
            v-for="button in buttons"
            :key="button.type"
            class="button button-primary button-sm"
            type="button"
            @click="addBlock(button.field)"
          >
            {{ button.type }}
          </button>
          <multiselect
            v-model="blog_tags"
            tag-placeholder="Добавьте новый тег"
            placeholder="Найдите или добавьте свой тег"
            :options="options"
            :multiple="true"
            :taggable="true"
            @input="clearError"
            @tag="addTag"
          ></multiselect>
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
import Warning from '@/components/Warning'
import imageField from '@/components/blog/imageField'
import textField from '@/components/blog/textField'
import videoField from '@/components/blog/videoField'
import { blogEditor } from '~/assets/descriptions'

export default {
  components: {
    Warning,
    textField,
    imageField,
    videoField,
  },
  data() {
    return {
      buttons: [
        {
          type: 'Текст',
          field: 'textField',
        },
        {
          type: 'Изображение',
          field: 'imageField',
        },
        {
          type: 'Видео',
          field: 'videoField',
        },
      ],
      articles: ['textField'],
      blog_body: [],
      blog_title: null,
      blog_category: 'Блоги',
      blog_tags: ['Текст'],
      options: ['Видео', 'Картинки', 'Текст'],
      errorTags: '',
    }
  },
  head() {
    return {
      title: blogEditor.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: blogEditor.description,
        },
      ],
    }
  },
  methods: {
    removeElement(id) {
      this.blog_body = this.blog_body.filter((item) => {
        return item.name !== id
      })
    },
    fillBlog(val) {
      const block = this.blog_body.find((item) => item.name === val.name)
      if (block) {
        block.body = val.body
      } else {
        this.blog_body.push(val)
      }
    },
    error(text) {
      this.$buefy.notification.open({
        duration: 5000,
        message: text,
        position: 'is-bottom-right',
        type: 'is-danger',
        hasIcon: true,
      })
    },
    addTag(newTag) {
      this.options.push(newTag)
      this.blog_tags.push(newTag)
    },
    clearError() {
      this.errorTags = null
    },
    convertBody() {
      return JSON.stringify({
        blocks: [this.blog_body],
      })
    },
    addBlock(field) {
      this.articles.push(field)
    },
    async onSubmit() {
      try {
        if (!this.blog_title) return this.error('Нужно заполнить поля')

        const blogBody = this.convertBody()

        if (!blogBody) return this.error('Нужно заполнить поля')

        const tags = JSON.stringify(this.blog_tags)

        const blog = {
          title: this.blog_title,
          content: blogBody,
          category: this.blog_category,
          tags,
        }
        const response = await this.$axios.$post('/blogs/', blog)

        this.$router.push({
          name: 'blog-slug',
          params: { slug: response.slug },
        })
      } catch (e) {
        if (e.response && e.response.data && e.response.data.tags) {
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
        this.blog_tags = ['Текст']
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.warning-overlay {
  z-index: 2;
}
@media screen and (max-width: 450px) {
  .title {
    padding: 15px;
    text-align: center;
    margin: 0;
  }
}
</style>
