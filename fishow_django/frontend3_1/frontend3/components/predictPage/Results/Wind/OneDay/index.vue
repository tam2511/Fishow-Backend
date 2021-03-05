<template>
  <div>
    <div v-if="gustOnly">
      <div class="block gust" :style="colorGust">
        {{ day.gust_max || day.gust }}
      </div>
    </div>
    <div v-else>
      <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
      <div class="block" :style="colorWind">
        {{ Math.round(day.wind_mean) || Math.round(day.wind) }}
      </div>
      <!--    {{ color }}-->
      <div class="block">
        <b-icon
          pack="fas"
          icon="location-arrow"
          size="is-medium"
          :style="direction"
        />
      </div>
      <div class="block">{{ wind }}</div>
    </div>
  </div>
</template>

<script>
import helper from '~/assets/js/helper'
import convertFromObjectToDate from '~/assets/js/convertFromObjectToDate'
import DayBlock from '~/components/predictPage/helpers/dayBlock'
export default {
  components: { DayBlock },
  props: {
    gustOnly: {
      type: Boolean,
      default: false,
    },
    day: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      colorOfValue: null,
    }
  },
  computed: {
    normDay() {
      return this.day.wind_mean ? helper(this.day) : null
    },
    dayCalendar() {
      return this.day.wind_mean
        ? convertFromObjectToDate(this.day)
        : this.day.date
    },
    wind() {
      return this.day.wind_direction
    },
    direction() {
      const deg = {
        С: -45,
        СВ: 0,
        В: 45,
        ЮВ: 90,
        Ю: 135,
        ЮЗ: 180,
        З: 225,
        СЗ: 270,
      }
      return `transform: rotate(${deg[this.wind]}deg)`
    },
    colorWind() {
      let result = 'null'
      const colors = [
        [0, 'rgba(176,228,232,0.15)'],
        [1, 'rgba(176,228,232,0.3)'],
        [2, 'rgba(176,228,232,0.5)'],
        [3, 'rgba(176,228,232,0.7)'],
        [4, 'rgba(247,255,0,0.64)'],
        [5, '#ffe800'],
        [6, '#ffa700'],
        [7, '#ff8c00'],
        [8, '#ff3500'],
        [9, '#ff1300'],
      ]
      const wind = this.day.wind_mean ? this.day.wind_mean : this.day.wind
      for (let i = 0; i < colors.length; i++) {
        if (wind > colors[i][0]) {
          result = colors[i][1]
        }
      }
      return 'background-color:' + result
    },
    colorGust() {
      let result = 'null'
      const colors = [
        [1, 'rgba(176,228,232,0.05)'],
        [2, 'rgba(176,228,232,0.15)'],
        [3, 'rgba(176,228,232,0.25)'],
        [4, 'rgba(176,228,232,0.35)'],
        [5, 'rgba(176,228,232,0.45)'],
        [6, 'rgba(247,255,0,0.64)'],
        [7, '#ffe800'],
        [8, '#ffa700'],
        [13, '#ff8c00'],
        [15, '#ff3500'],
        [20, '#ff1300'],
      ]
      const gust = this.day.gust_max ? this.day.gust_max : this.day.gust
      for (let i = 0; i < colors.length; i++) {
        if (gust > colors[i][0]) {
          result = colors[i][1]
        }
      }
      return 'background-color:' + result
    },
  },
}
</script>

<style scoped lang="scss">
.chart {
  display: flex;
  flex-flow: column;
  justify-content: center;
}
.block {
  text-align: center;
}
.date {
  &-second {
    color: #a8a8a8;
  }
}
</style>
