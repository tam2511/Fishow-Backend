<template>
  <div>
    <p>{{ day.date }}</p>
    <figure class="image is-48x48">
      <img :src="image" alt="" :title="day.phenomenon" />
    </figure>
    <!--    {{ day.phenomenon }}-->
  </div>
</template>

<script>
import { pogoda } from '~/assets/js/convertPogodaToUrlImage'

export default {
  props: {
    day: {
      type: Object,
      required: true,
    },
  },
  computed: {
    image() {
      return pogoda[this.day.phenomenon]
    },
  },
}
</script>

<style scoped>
.temperature-max {
  width: 100%;
  background-color: #dea40b;
}
.temperature-min {
  background-color: #00b3ee;
  width: 100%;
}
.chart {
  display: flex;
  flex-flow: column;
  justify-content: center;
}
</style>
