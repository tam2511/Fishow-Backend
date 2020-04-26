<template>
  <div class="table-custom-responsive">
    <table class="table-custom table-standings table-classic">
      <thead>
        <tr>
          <th colspan="2">Пользователи</th>
          <th>Сообщ.</th>
          <th>Блогов</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in userList" :key="user.username">
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
          <td>{{ user.comments }}</td>
          <td>{{ user.blogs }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { apiService } from '../common/api.service'

export default {
  name: 'UserRate',
  data() {
    return {
      userList: [],
    }
  },
  methods: {
    getUserList() {
      let endpoint = '/api/user_all/'

      apiService(endpoint).then((data) => {
        this.userList.push(...data)
      })
    },
  },
  created() {
    this.getUserList()
  },
}
</script>

<style scoped>
thead,
tbody {
  display: block;
}
.team-inline {
  max-width: 90px;
}
.team-title {
  font-size: 12px;
}
</style>
