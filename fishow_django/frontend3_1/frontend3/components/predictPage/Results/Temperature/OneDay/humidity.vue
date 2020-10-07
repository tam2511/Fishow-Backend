<template>
  <div class="humidity" :style="color">
    {{ Math.floor(day.humidity_mean) }}%
  </div>
</template>

<script>
export default {
  props: {
    day: {
      type: Object,
      required: true,
    },
  },
  computed: {
    color() {
      let varStyle = ''
      if (this.day.humidity_mean < 40) {
        varStyle = 'color: #000;'
      }
      return `${varStyle} background-color: rgba(68, 137, 196, ${this.day.humidity_mean});`
    },
  },
}
// rgba(176, 228, 232, 1)
</script>

<style scoped>
.humidity {
  text-align: center;
  color: white;
  padding: 0.2rem 0.75rem;
}
</style>
