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
      data: [
        { username: 'Jesse Simmons', posts: 2, comments: 5 },
        { username: 'John Jacobs', posts: 11, comments: 42 },
        { username: 'Tina Gilbert', posts: 0, comments: 7 },
        { username: 'Clarence Flores', posts: 4, comments: 4 },
        { username: 'Anne Lee', posts: 1, comments: 2 },
      ],
      columns: [
        {
          field: 'username',
          label: 'Username',
          width: 160,
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

<style scoped>
section [data-label='Username'],
td {
  max-width: 160px;
  overflow: hidden;
}
.table td {
  max-width: 160px;
  overflow: hidden;
}
</style>
