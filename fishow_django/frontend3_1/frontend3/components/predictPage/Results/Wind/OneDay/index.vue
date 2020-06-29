<template>
  <div>
    <div class="block">
      <p>{{ normDay }}</p>
    </div>
    <div class="block">{{ Math.round(day.wind_mean) }}</div>
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
    <div class="block gust" :style="'background-color:' + color">
      {{ day.gust_max }}
    </div>
  </div>
</template>

<script>
import helper from '~/assets/js/helper'

export default {
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
    wind() {
      return this.day.wind_direction.split("'")[1]
    },
    direction() {
      const deg = {
        С: 0,
        СВ: 45,
        В: 90,
        ЮВ: 135,
        Ю: 180,
        ЮЗ: 225,
        З: 270,
        СЗ: 315,
      }
      return `transform: rotate(${deg[this.wind]}deg)`
    },
    color() {
      const percentColors = [
        { pct: 0, color: { r: '0xff', g: '0x00', b: 0 } },
        { pct: 50, color: { r: '0xff', g: '0xff', b: 0 } },
        { pct: 100, color: { r: '0x00', g: '0xff', b: 0 } },
      ]
      let result = null
      const getColorForPercentage = function (pct) {
        for (let i = 1; i < percentColors.length - 1; i++) {
          if (pct < percentColors[i].pct) {
            const lower = percentColors[i - 1]
            const upper = percentColors[i]
            const range = upper.pct - lower.pct
            const rangePct = (pct - lower.pct) / range
            const pctLower = 1 - rangePct
            const pctUpper = rangePct
            const color = {
              r: Math.floor(
                lower.color.r * pctLower + upper.color.r * pctUpper
              ),
              g: Math.floor(
                lower.color.g * pctLower + upper.color.g * pctUpper
              ),
              b: Math.floor(
                lower.color.b * pctLower + upper.color.b * pctUpper
              ),
            }
            result = 'rgb(' + [color.r, color.g, color.b].join(',') + ')'
            break
          }
        }

        // or output as hex if preferred
      }
      getColorForPercentage(this.day.wind_mean)
      console.log('result = ', result)

      return result
    },
  },
  mounted() {},
}
</script>

<style scoped>
.chart {
  display: flex;
  flex-flow: column;
  justify-content: center;
}
.block {
  text-align: center;
}
.gust {
  background-color: #0d0a0a;
}
html,
body {
  width: 100%;
  background-color: #333;
  margin: 0;
  position: relative;
  font: 1em sans-serif;
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
