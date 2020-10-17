<template>
  <div class="humidity" :style="color">
    {{ Math.floor(day.humidity_mean) || Math.floor(day.humidity) }}%
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
      const day = this.day.humidity_mean
        ? this.day.humidity_mean
        : this.day.humidity
      let varStyle = ''
      if (day < 40) {
        varStyle = 'color: #000;'
      }
      return `${varStyle} background-color: rgba(68, 137, 196, ${day});`
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
