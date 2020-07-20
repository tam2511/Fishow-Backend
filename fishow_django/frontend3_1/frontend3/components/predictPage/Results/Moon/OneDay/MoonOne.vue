<template>
  <div>
    <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
    {{ day.moon }}
  </div>
</template>

<script>
import convertFromObjectToDate from '~/assets/js/convertFromObjectToDate'
import DayBlock from '~/components/predictPage/helpers/dayBlock'
import helper from '~/assets/js/helper'
// import { planet } from '~/assets/js/planet'
export default {
  components: { DayBlock },
  props: {
    day: {
      type: Object,
      required: true,
    },
  },
  computed: {
    normDay() {
      return helper(this.day)
    },
    dayCalendar() {
      return convertFromObjectToDate(this.day)
    },
  },
  created() {},
}
</script>

<style scoped></style>
