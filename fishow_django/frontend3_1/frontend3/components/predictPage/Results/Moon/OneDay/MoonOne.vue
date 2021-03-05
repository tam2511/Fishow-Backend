<template>
  <div>
    <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
    <figure class="image is-48x48">
      <img :src="moonPic" />
      <p class="content">{{ day.moon.toFixed() }}%</p>
    </figure>
  </div>
</template>

<script>
import convertFromObjectToDate from '~/assets/js/convertFromObjectToDate'
import DayBlock from '~/components/predictPage/helpers/dayBlock'
import helper from '~/assets/js/helper'

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
    moonPic() {
      const pic = {
        1: {
          0: '/assets/moon/1.png',
          10: '/assets/moon/2.png',
          20: '/assets/moon/3.png',
          30: '/assets/moon/4.png',
          40: '/assets/moon/5.png',
          50: '/assets/moon/6.png',
          60: '/assets/moon/7.png',
          70: '/assets/moon/8.png',
          80: '/assets/moon/9.png',
          90: '/assets/moon/10.png',
          100: '/assets/moon/11.png',
        },
        '-1': {
          0: '/assets/moon/23.png',
          10: '/assets/moon/22.png',
          20: '/assets/moon/21.png',
          30: '/assets/moon/20.png',
          40: '/assets/moon/19.png',
          50: '/assets/moon/18.png',
          60: '/assets/moon/17.png',
          70: '/assets/moon/16.png',
          80: '/assets/moon/15.png',
          90: '/assets/moon/14.png',
          100: '/assets/moon/13.png',
        },
      }
      let result = 0
      result = pic[this.day.moon_direction]
      for (const one in result) {
        if (this.day.moon >= one) {
          result = one
        }
      }
      return (
        (pic[this.day.moon_direction] &&
          pic[this.day.moon_direction][result]) ||
        '/assets/moon/23.png'
      )
    },
  },
  created() {},
}
</script>

<style scoped>
.column {
  text-align: center;
}
.content {
  padding-top: 10px;
}
</style>
