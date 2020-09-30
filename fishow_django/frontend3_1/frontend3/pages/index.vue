<template>
  <div class="tile is-vertical is-8">
    <div class="media">
      <div class="media-left"><h4 class="title is-4">Последние записи</h4></div>
      <div class="media-right">
        <div class="field">
          <b-switch v-model="isSwitched" @input="showBlog">
            Скрывать блоги
          </b-switch>
        </div>
      </div>
    </div>
    <div
      v-infinite-scroll="loadMore"
      infinite-scroll-disabled="busy"
      infinite-scroll-distance="10"
      class="tile is-parent is-vertical space-left0"
    >
      <article
        v-for="blog in notRatedBlogs"
        :key="blog.id"
        class="tile is-child blog-page"
      >
        <BlogCard :blog="blog" />
      </article>
    </div>
    <div v-if="!next">
      <h2 class="title">Блоги закончились, поздравляю!</h2>
    </div>
  </div>
</template>

<script>
import BlogCard from '@/components/BlogCard'

export default {
  layout: 'SideBarRight',
  components: {
    BlogCard,
  },
  data() {
    return {
      blogs: null,
      data: [],
      count: 0,
      busy: false,
      next: null,
      isSwitched: false,
    }
  },
  computed: {
    notRatedBlogs() {
      const result = []
      if (this.blogs) {
        const length = this.blogs.length
        for (let i = 0; i < length; i++) {
          if (
            !this.blogs[i].user_has_votedUp &&
            !this.blogs[i].user_has_votedDown
          ) {
            result.push(this.blogs[i])
          }
        }
      }
      return this.isSwitched ? result : this.blogs
    },
  },
  mounted() {
    if (process.browser && localStorage.getItem('hidden-blogs')) {
      this.isSwitched = JSON.parse(localStorage.getItem('hidden-blogs'))
    }
    this.$axios.get('/blogs/').then((res) => {
      this.blogs = res.data.results
      this.next = res.data.next
    })
  },
  methods: {
    loadMore() {
      this.busy = true

      setTimeout(() => {
        if (this.next) {
          const url = this.next.split('api/')[1]
          this.$axios.get(`/${url}`).then((res) => {
            this.blogs.push(...res.data.results)
            if (res.data.next) {
              this.next = res.data.next
            } else {
              this.next = null
            }
          })
        }
        this.busy = false
      }, 1000)
    },
    showBlog() {
      localStorage.setItem('hidden-blogs', this.isSwitched)
    },
  },

  head: {
    title: 'Прогноз клева рыбы, общение и новости | Fishow',
    meta: [
      {
        hid: 'description',
        name: 'description',
        content:
          'Прогноз клева рыбы. Рыболовный прогноз клёва рибы с учетом температуры води и воздуха, атмосферного давления, фаз луны и уровня воды, лучший прогноз на рыбалку.',
      },
    ],
  },
}
</script>

<style lang="scss" scoped>
@media screen and (max-width: 700px) {
  .space-left0 {
    padding-right: 0;
  }
}
.media {
  align-items: center;
}
.media-right .field {
  display: flex;
  flex-flow: row wrap;
  max-width: 100px;
  & > * {
    flex: 1 auto;
  }
}
</style>
