<template>
  <div class="table-custom-responsive">
    <table class="table-custom table-standings table-classic">
      <thead>
        <tr>
          <th colspan="2">Пользователи</th>
          <th>Рейтинг</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in userRating" :key="user.username">
          <td>
            <span>{{ index + 1 }}</span>
          </td>
          <td class="team-inline">
            <div class="team-figure">
              <img
                src="/static/assets/images/user-1-63x63.jpg"
                alt=""
                width="42"
                height="26"
              />
            </div>
            <div class="team-title">
              <div class="team-name">{{ user.username }}</div>
              <div class="team-country">Ник или Фамилия</div>
            </div>
          </td>
          <td>{{ user.rating }}</td>
          <!--          <td>{{ user.blogs }}</td>-->
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { apiService } from '@/plugins/api.service'

export default {
  name: 'UserRate',
  data() {
    return {
      userList: [],
      lengthOfList: 5
    }
  },
  computed: {
    userRating() {
      return this.userList.filter((user, index) => index < this.lengthOfList)
    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    getUserList() {
      const endpoint = '/api/user_all/'

      apiService(endpoint).then((data) => {
        this.userList.push(...data)
      })
    }
  }
}
</script>

<style scoped>
thead {
  background-color: var(--background-color-brand);
}
.team-inline {
  max-width: 90px;
}
.team-title {
  font-size: 12px;
}
</style>
