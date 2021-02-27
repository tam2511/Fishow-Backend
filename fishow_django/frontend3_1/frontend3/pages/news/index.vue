<template>
  <div class="tile is-vertical is-8">
    <div class="media">
      <div class="media-left">
        <h4 class="title is-4">Последние новости</h4>
      </div>
    </div>
    <div
      v-infinite-scroll="loadMore"
      infinite-scroll-disabled="busy"
      infinite-scroll-distance="10"
      class="tile is-parent is-vertical space-left0"
    >
      <article
        v-for="news in newsList"
        :key="news.id"
        class="tile is-child blog-page"
      >
        <CardItem :liked="false" :item="news" />
      </article>
    </div>
  </div>
</template>

<script>
import { mainPage } from '~/assets/descriptions'
import CardItem from '~/components/Card/CardItem'

export default {
  components: {
    CardItem,
  },
  layout: 'SideBarRight',
  data() {
    return {
      newsList: null,
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
    notRatedNews() {
      const result = []
      if (this.newsList) {
        const length = this.newsList.length
        for (let i = 0; i < length; i++) {
          if (
            !this.newsList[i].user_has_votedUp &&
            !this.newsList[i].user_has_votedDown
          ) {
            result.push(this.newsList[i])
          }
        }
      }
      return this.isSwitched ? result : this.newsList
    },
  },
  async mounted() {
    if (process.browser && localStorage.getItem('hidden-news')) {
      this.isSwitched = JSON.parse(localStorage.getItem('hidden-news'))
    }
    await this.$axios.get('/news/').then((res) => {
      this.newsList = res.data.results
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
            this.newsList.push(...res.data.results)
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
      localStorage.setItem('hidden-news', this.isSwitched)
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
