<template>
  <div class="humidity" :style="color">
    {{ Math.floor(day.humidity_mean * 100) }}%
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
      if (this.day.humidity_mean < 0.4) {
        varStyle = 'color: #000;'
      }
      return `${varStyle} background-color: rgba(30, 50, 120, ${this.day.humidity_mean});`
    },
  },
}
</script>

<style scoped>
.humidity {
  text-align: center;
  color: white;
}
</style>
