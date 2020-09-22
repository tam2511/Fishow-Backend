<template lang="pug">
  .box(:class="typeOfResult + '-box'")
    h2.title {{ title }}
    p.content(v-if="content" v-html="content")
    slot
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    typeOfResult: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      default: null,
    },
  },
}
</script>

<style scoped>
.box {
  min-height: 300px;
}
</style>
