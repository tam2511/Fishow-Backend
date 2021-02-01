<template>
  <div class="container"></div>
</template>

<script>
export default {
  layout: 'emptyPage',
  props: {
    error: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.$buefy.toast.open({
      duration: 2000,
      message: 'Такой страницы пока что нету.',
      type: 'is-danger',
    })
    setTimeout(() => {
      this.$router.push({ name: 'index' })
    }, 1000)
  },
}
</script>
