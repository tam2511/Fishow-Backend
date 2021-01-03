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
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
}
</style>
