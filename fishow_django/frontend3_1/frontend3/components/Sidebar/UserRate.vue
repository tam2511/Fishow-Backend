<template>
  <section>
    <b-table :data="userRating" :columns="columns"> </b-table>
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
    // this.getUserList()
  },
  methods: {
    // async getUserList() {
    // console.log('this.auth_type = ', this.$auth)
    // try {
    //   if (this.$auth.user) {
    //     if (this.$auth.$state.strategy !== 'social') {
    // const response = await this.$axios.get('/user_all/')
    // this.userList.push(...response.data)
    // } else {
    // const token = this.$auth.$storage.$_token.social.split('Bearer ')[1]
    // console.log('token = ', token)
    // const response = await this.$axios.get({
    //   url: 'https://login.yandex.ru/info?',
    //   headers: {
    //     Authorization: 'OAuth ' + token,
    //   },
    // })
    // console.log('response  111 = ', response)
    // }
    // }
    // } catch (e) {
    // console.log('error userlist = ', e.response)
    // }
    // },
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
