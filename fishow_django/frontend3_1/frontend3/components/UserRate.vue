<template>
  <section>
    <b-table v-if="$auth.user" :data="userRating" :columns="columns"> </b-table>
    <div v-else>Авторизуйтесь что бы увидеть список пользователей</div>
  </section>
</template>

<script>
export default {
  name: 'UserRate',
  data() {
    return {
      userList: [],
      lengthOfList: 5,
      columns: [
        {
          field: 'username',
          label: 'Пользователь',
          width: '160',
          'cell-class': 'column-username',
        },
        {
          field: 'blogs',
          label: 'Блогов',
        },
        {
          field: 'comments',
          label: 'Комм-ев',
        },
      ],
    }
  },
  computed: {
    userRating() {
      return this.userList.filter((user, index) => index < this.lengthOfList)
    },
  },
  created() {
    this.getUserList()
  },
  methods: {
    async getUserList() {
      try {
        const responce = await this.$axios.get('/user_all/')
        this.userList.push(...responce.data)
      } catch (e) {
        console.log('error userlist = ', e.responce)
      }
    },
  },
}
</script>

<style>
section [data-label='Username'],
td {
  max-width: 160px;
  overflow: hidden;
}
.column-username {
  max-width: 160px;
  overflow: hidden;
}
</style>
