<!--<template>-->
<!--  <div class="container">-->
<!--    <div class="row row-50" :style="$auth.loggedIn ? '' : 'filter:blur(5px)'">-->
<!--      <div v-if="blog_category !== 'Отчет'" class="col-lg-7 col-xl-8">-->
<!--        <article class="heading-component">-->
<!--          <div class="heading-component-inner">-->
<!--            <h5 class="heading-component-title">Написать блог</h5>-->
<!--          </div>-->
<!--        </article>-->

<!--      </div>-->
<!--      &lt;!&ndash;      <div class="col-lg-7 col-xl-8">&ndash;&gt;-->
<!--      <div v-else class="col-lg-7 col-xl-8">-->
<!--        <article class="heading-component">-->
<!--          <div class="heading-component-inner">-->
<!--            <h5 class="heading-component-title">Добавить отчет</h5>-->
<!--          </div>-->
<!--        </article>-->
<!--      </div>-->
<!--      <div class="col-lg-5 col-xl-4">-->
<!--        <div>-->
<!--          <label class="typo__label">Выберите категорию:</label>-->
<!--          <multiselect-->
<!--            v-model="blog_category"-->
<!--            :options="optionsCategory"-->
<!--            :searchable="false"-->
<!--            :close-on-select="true"-->
<!--            :show-labels="false"-->
<!--            placeholder="Pick a value"-->
<!--          ></multiselect>-->
<!--        </div>-->
<!--        <label class="typo__label">Теги:</label>-->
<!--        <multiselect-->
<!--          v-model="blog_tags"-->
<!--          tag-placeholder="Add this as new tag"-->
<!--          placeholder="Найдите или добавьте свой тег"-->
<!--          label="name"-->
<!--          track-by="code"-->
<!--          :options="options"-->
<!--          :multiple="true"-->
<!--          :taggable="true"-->
<!--          @tag="addTag"-->
<!--        >-->
<!--        </multiselect>-->
<!--        <br />-->
<!--      </div>-->
<!--    </div>-->
<!--    <div v-if="!$auth.loggedIn" class="warning-overlay">-->
<!--      <warning-->
<!--        class="warning-popin"-->
<!--        title="Оповещение"-->
<!--        body="Для возможности создания блога вам необходимо авторизоваться"-->
<!--        button="Войти"-->
<!--        redirect="/login"-->
<!--      />-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<template>
  <div class="tile">
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
      blog_body {{ blog_body }}
      <hr />
      blog_title {{ blog_title }}
      <hr />
      blog_category {{ blog_category }}
      <hr />
      blog_tags {{ blog_tags }}
    </div>
  </div>
</template>

<script>
// import { mapState } from 'vuex'
// import Warning from '@/components/Warning'
// import TextField from '@/components/blog/textField'
import imageField from '@/components/blog/imageField'
import BlogContentField from '@/components/blog/blogContentField'
import videoField from '@/components/blog/videoField'

export default {
  components: {
    // Warning,
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
      //     deafultTags: ['Удочки', 'Шутки', 'Ночь', 'История', 'Деньги'],

      //     error: null,

      //     valueCategory: '',
      blog_tags: [{ name: 'Текст', code: 'текст' }],
      options: [
        { name: 'Видео', code: 'ви' },
        { name: 'Картинки', code: 'os' },
        { name: 'Текст', code: 'текст' },
      ],
      optionsCategory: ['Новости', 'Блоги', 'Статьи', 'Отчет'],
      //     descriptors: {
      //       prop1: {
      //         type: 'string',
      //         label: 'Место рыбалки',
      //         required: true,
      //         message: 'Обязательно укажите место рыбалки'
      //       },
      //       prop2: {
      //         type: 'object',
      //         label: 'object label',
      //         fields: {
      //           prop1: { type: 'email', required: true },
      //           prop2: { type: 'number', required: true },
      //           prop3: [
      //             {
      //               type: 'string',
      //               required: true,
      //               message: 'object label.prop3 is required'
      //             },
      //             {
      //               pattern: /test/,
      //               message: 'object label.prop3 should include test'
      //             }
      //           ],
      //           prop4: {
      //             type: 'enum',
      //             enum: [0, 1],
      //             label: 'Рыба',
      //             placeholder: 'sadsad',
      //             options: [
      //               // { label: 'Лев', value: 0, disabled: true },
      //               { label: 'Лев', value: 0 },
      //               { label: 'Тигр', value: 1 }
      //             ]
      //           },
      //           prop5: { type: 'boolean', required: true }
      //         }
      //       }
      //     },
      //     data: {}
    }
  },
  // computed: {
  //   loading() {
  //     return this.username !== null
  //   },
  //   ...mapState('user', ['username'])
  // },
  // created() {
  //   // document.title = 'Fishow - Создание блога'
  // },
  methods: {
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
    // async submitRecipe() {
    //   const config = {
    //     headers: { 'content-type': 'multipart/form-data' },
    //   }
    //   const formData = new FormData()
    //   /* eslint-disable */
    //   for (let data in this.recipe) {
    //     formData.append(data, this.recipe[data])
    //   }
    //   try {
    //     const response = await this.$axios.$post('/blogs/', formData, config)
    //     console.log('response = ', response)
    //     this.$router.push('/blogs/')
    //   } catch (e) {
    //     console.log(e)
    //   }
    // },
    async onSubmit() {
      try {
        this.convertTags()
        this.convertBody()
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
        console.log('error = ', e)
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
<style lang="scss" scoped></style>
