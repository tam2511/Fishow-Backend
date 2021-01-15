<template>
  <div class="tem-container">
    <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
    <figure class="image is-48x48">
      <img :src="image" alt="" :title="day.phenomenon" />
    </figure>
    {{ max }}
    <div class="svg-container">
      <temp-box :radius="max + 10"></temp-box>
      <temp-box :radius="min + 10" :up="false"></temp-box>
    </div>
    {{ min }}
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
      // console.log('this.day.phenomenon = ', this.day.phenomenon)
      const image = pogoda[this.day.phenomenon]
      // console.log('image = ', image)
      return image
    },
    max() {
      return this.day.temperature_max
        ? this.day.temperature_max
        : this.day.temperature + 3
    },
    min() {
      return this.day.temperature_min
        ? this.day.temperature_min
        : this.day.temperature - 3
    },
    normDay() {
      return this.day.temperature_max ? helper(this.day) : null
    },
    dayCalendar() {
      return this.day.temperature_max
        ? convertFromObjectToDate(this.day)
        : this.day.date
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
  background-color: #b0e4e8;
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
