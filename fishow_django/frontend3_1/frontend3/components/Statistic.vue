<template>
  <div class="table-custom-responsive">
    <table class="table-custom table-custom-bordered table-team-statistic">
      <tbody>
        <tr>
          <td>
            <p class="team-statistic-counter">{{ counterBlogs }}</p>
            <p class="team-statistic-title">Всего блогов</p>
          </td>
          <td>
            <p class="team-statistic-counter">{{ counterComments }}</p>
            <p class="team-statistic-title">Количество комментариев</p>
          </td>
        </tr>
        <tr>
          <td>
            <p class="team-statistic-counter">0</p>
            <p class="team-statistic-title">Assists Per Game</p>
          </td>
          <td>
            <p class="team-statistic-counter">0</p>
            <p class="team-statistic-title">Points Allowed</p>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import { apiService } from '@/plugins/api.service'

export default {
  name: 'Statistic',
  data() {
    return {
      counterBlogs: null,
      counterComments: 0,
    }
  },
  created() {
    this.getBlogData()
  },
  methods: {
    getBlogData() {
      // const endpoint = '/api/blogs/'
      // apiService(endpoint).then(data => {
      //   this.counterBlogs = data.count
      //   // TODO: це хуйня
      //   data.results.forEach(
      //     item => (this.counterComments += item.comments_count)
      //   )
      // })
    },
  },
}
</script>

<style scoped></style>
