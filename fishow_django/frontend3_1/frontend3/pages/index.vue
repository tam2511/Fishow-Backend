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
        v-for="blog in blogs"
        :key="blog.id"
        class="tile is-child blog-page"
      >
        <BlogCard
          v-if="
            !((blog.user_has_votedUp || blog.user_has_votedDown) && isSwitched)
          "
          :blog="blog"
        />
      </article>
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
