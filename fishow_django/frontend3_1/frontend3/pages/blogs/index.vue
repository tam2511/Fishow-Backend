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
      <h2 class="title title-blogs-end">Блоги закончились, поздравляю!</h2>
    </div>
  </div>
</template>

<script>
import BlogCard from '@/components/BlogCard'
import catchError from '~/assets/mixins/catchError'
import { mainPage } from '~/assets/descriptions'

export default {
  components: {
    BlogCard,
  },
  mixins: [catchError],
  layout: 'SideBarRight',
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

  head: {
    title: mainPage.title,
    meta: [
      {
        hid: 'description',
        name: 'description',
        content: mainPage.description,
      },
    ],
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
    this.getBlogs()
  },
  methods: {
    async getBlogs() {
      try {
        const response = await this.$axios.get('/blogs/')

        this.blogs = response.data.results
        this.next = response.data.next
      } catch (e) {
        this.showErrorNotification()
      }
    },
    loadMore() {
      this.busy = true

      setTimeout(async () => {
        if (this.next) {
          const url = this.next.split('api/')[1]
          try {
            const response = await this.$axios.get(`/${url}`)
            this.blogs.push(...response.data.results)
            if (response.data.next) {
              this.next = response.data.next
            } else {
              this.next = null
            }
          } catch (e) {
            this.showErrorNotification()
          }
        }
        this.busy = false
      }, 1000)
    },
    showBlog() {
      localStorage.setItem('hidden-blogs', this.isSwitched)
    },
  },
}
</script>

<style lang="scss" scoped>
.title-blogs-end {
  color: #247d21;
  font-size: 1rem;
  padding: 1rem;
  background: #fff;
}
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
