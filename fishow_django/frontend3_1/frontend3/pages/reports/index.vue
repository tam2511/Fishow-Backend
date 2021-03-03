<template>
  <div class="tile is-vertical is-8">
    <div class="media">
      <div class="media-left"><h4 class="title is-4">Последние отчеты</h4></div>
      <div class="media-right">
        <div class="field">
          <b-switch v-model="isSwitched" @input="showBlog">
            Скрывать отчеты
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
        v-for="report in notRatedReports"
        :key="report.id"
        class="tile is-child blog-page"
      >
        <report-card :report="report" />
      </article>
    </div>
    <div v-if="!next">
      <h2 class="title title-blogs-end">Отчеты закончились</h2>
    </div>
  </div>
</template>

<script>
import ReportCard from '@/components/ReportCard'
import catchError from '~/assets/mixins/catchError'
import { reportPage } from '~/assets/descriptions'

export default {
  name: 'Reports',
  components: {
    ReportCard,
  },
  mixins: [catchError],
  layout: 'sideBarRight',
  data() {
    return {
      reports: null,
      data: [],
      count: 0,
      busy: false,
      next: null,
      isSwitched: false,
    }
  },

  head: {
    title: reportPage.title,
    meta: [
      {
        hid: 'description',
        name: 'description',
        content: reportPage.description,
      },
    ],
  },
  computed: {
    notRatedReports() {
      const result = []
      if (this.reports) {
        const length = this.reports.length
        for (let i = 0; i < length; i++) {
          if (
            !this.reports[i].user_has_votedUp &&
            !this.reports[i].user_has_votedDown
          ) {
            result.push(this.reports[i])
          }
        }
      }
      return this.isSwitched ? result : this.reports
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
        const response = await this.$axios.get('/report/')

        this.reports = response.data.results
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
            this.reports.push(...response.data.results)
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
