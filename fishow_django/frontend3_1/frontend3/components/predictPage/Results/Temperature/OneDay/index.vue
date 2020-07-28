<template>
  <div class="tem-container">
    <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
    <figure class="image is-48x48">
      <img :src="image" alt="" :title="day.phenomenon" />
    </figure>
    {{ day.temperature_max }}
    <div class="svg-container">
      <temp-box :radius="day.temperature_max"></temp-box>
      <temp-box :radius="day.temperature_min" :up="false"></temp-box>
    </div>
    {{ day.temperature_min }}
    <!--    {{ day.phenomenon }}-->
  </div>
</template>

<script>
import { pogoda } from '~/assets/js/convertPogodaToUrlImage'
import helper from '~/assets/js/helper'
import convertFromObjectToDate from '~/assets/js/convertFromObjectToDate'
import DayBlock from '~/components/predictPage/helpers/dayBlock'
import TempBox from '~/components/predictPage/icon/tempBox'

export default {
  components: { TempBox, DayBlock },
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
.tem-container {
  text-align: center;
}
figure {
  margin: 0 auto;
  margin-bottom: 15px;
}
.svg-container {
  height: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.svg-container svg {
  display: block;
}
</style>
