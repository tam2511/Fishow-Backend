<template>
  <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
</template>

<script>
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
    normDay() {
      return helper(this.day)
    },
    dayCalendar() {
      return convertFromObjectToDate(this.day)
    },
  },
}
</script>
