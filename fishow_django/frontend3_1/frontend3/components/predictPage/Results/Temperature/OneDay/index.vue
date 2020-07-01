<template>
  <div>
    <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
    <figure class="image is-48x48">
      <img :src="image" alt="" :title="day.phenomenon" />
    </figure>
    <!--    {{ day.phenomenon }}-->
  </div>
</template>

<script>
import { pogoda } from '~/assets/js/convertPogodaToUrlImage'
import helper from '~/assets/js/helper'
import convertFromObjectToDate from '~/assets/js/convertFromObjectToDate'
import DayBlock from '~/components/predictPage/helpers/dayBlock'

export default {
  components: { DayBlock },
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
    normDay() {
      return helper(this.day)
    },
    dayCalendar() {
      return convertFromObjectToDate(this.day)
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
