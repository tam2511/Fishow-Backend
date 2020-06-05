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
          label: 'Username',
          width: '160',
          'cell-class': 'column-username',
        },
        {
          field: 'blogs',
          label: 'Blogs',
        },
        {
          field: 'comments',
          label: 'Comments',
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
        console.log('responce = ', responce)
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
