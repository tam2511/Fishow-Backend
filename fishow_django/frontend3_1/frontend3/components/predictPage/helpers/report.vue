<template lang="pug">
  .columns.report
    .column.is-three-quarters
      p.content(v-html="message")
    .column.report-icon
      b-icon(pack="fas"
        icon="exclamation-triangle"
        size="is-large"
        type="is-primary")
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped>
.report {
  background-color: #b0e4e8;
  text-align: justify;
  display: flex;
  align-items: center;
  min-height: 120px;
}
</style>
