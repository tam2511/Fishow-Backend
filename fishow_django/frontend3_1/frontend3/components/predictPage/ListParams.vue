<template>
  <div>
    <!--    {{ data }}-->
    <hr />
    <!--    {{ dataJSON }}-->
    <ul>
      <li v-for="item in dataJSON" :key="item.id">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    list: {
      type: String,
      required: true,
    },
  },
  computed: {
    dataJSON() {
      try {
        return JSON.parse(this.list)
      } catch (e) {
        return null
      }
    },
  },
}
</script>

<style scoped></style>
