export default {
  method: {
    showErrorNotification() {
      this.$buefy.toast.open({
        duration: 5000,
        message: 'Что то пошло не так при загрузке.',
        type: 'is-danger',
      })
      this.$router.push({ name: 'index' })
    },
  },
}
