<template>
  <div>
    <div v-if="gustOnly">
      <div class="block gust" :style="colorGust">
        {{ day.gust_max }}
      </div>
    </div>
    <div v-else>
      <day-block :norm-day="normDay" :day-calendar="dayCalendar" />
      <div class="block" :style="colorWind">
        {{ Math.round(day.wind_mean) }}
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
      return helper(this.day)
    },
    wind() {
      return this.day.wind_direction.split("'")[1]
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
        [1, 'rgba(0,33,244,0.05)'],
        [2, 'rgba(0,33,244,0.10)'],
        [3, 'rgba(0,33,244,0.15)'],
        [4, 'rgba(247,255,0,0.64)'],
        [5, '#ffe800'],
        [6, '#ffa700'],
        [7, '#ff8c00'],
        [8, '#ff3500'],
        [9, '#ff1300'],
      ]
      for (let i = 0; i < colors.length; i++) {
        if (this.day.wind_mean > colors[i][0]) {
          result = colors[i][1]
        }
      }
      return 'background-color:' + result
    },
    colorGust() {
      let result = 'null'
      const colors = [
        [5, 'rgba(0,33,244,0.19)'],
        [6, 'rgba(247,255,0,0.64)'],
        [7, '#ffe800'],
        [8, '#ffa700'],
        [13, '#ff8c00'],
        [15, '#ff3500'],
        [20, '#ff1300'],
      ]
      for (let i = 0; i < colors.length; i++) {
        if (this.day.gust_max > colors[i][0]) {
          result = colors[i][1]
        }
      }
      return 'background-color:' + result
    },
    dayCalendar() {
      return convertFromObjectToDate(this.day)
    },
  },
  mounted() {},
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
  &-fisrt {
  }
  &-second {
    color: #a8a8a8;
  }
}
.gust {
}
.moon {
  width: 200px;
  margin: 2rem auto;
}
#phase {
  width: 200px;
  margin: 25px 0;
}

.moon-left,
.moon-right {
  display: inline-block;
  width: 100px;
  position: relative;
  margin: 0;
}
.moon-left .bg,
.moon-right .bg {
  stroke-width: 2px;
}

.moon-right .fg {
  stroke-width: 2px;
}
.moon-left .bg {
  fill: black;
}
.moon-left .fg {
  fill: white;
  transform-origin: 0% 0%;
}

.moon-right .fg {
  transform: scaleX(1);
}
.moon-left .fg {
  transform: scaleX(0) translateX(0);
}
</style>
