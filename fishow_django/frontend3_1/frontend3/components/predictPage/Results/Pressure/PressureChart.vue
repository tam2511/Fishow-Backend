<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">Максимальное суточное давление</span>
        <span class="legend_min">Минимальное суточное давление</span>
      </div>
      <VueApexCharts
        width="100%"
        height="200px"
        type="bar"
        :options="chartOptions"
        :series="series"
      ></VueApexCharts>
    </div>
  </client-only>
</template>

<script>
import getCalendarDay from '~/assets/js/getCalendarDay'
export default {
  components: {
    VueApexCharts: () => import('vue-apexcharts'),
  },
  props: {
    days: {
      type: Array,
      required: true,
    },
    pressureMax: {
      type: Array,
      required: true,
    },
    pressureMin: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Максимальное суточное давление',
          data: this.pressureMax,
        },
        {
          name: 'Минимальное суточное давление',
          data: this.pressureMin,
        },
      ],
      chartOptions: {
        chart: {
          height: 250,
          type: 'line',
          dropShadow: {
            enabled: false,
            color: '#000',
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2,
          },
          toolbar: {
            show: false,
          },
        },
        colors: ['#73a2a5', '#172a3b'],
        dataLabels: {
          enabled: true,
          formatter(value) {
            return Math.round(value)
          },
        },
        stroke: {
          curve: 'smooth',
        },
        grid: {
          borderColor: 'rgba(231,231,231,0)',
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.0,
          },
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: getCalendarDay(this.days),
        },
        yaxis: {
          min: this.max,
          max: this.min,
          labels: {
            formatter(value) {
              return Math.round(value)
            },
          },
        },
        legend: {
          // position: 'top',
          show: false,
          // horizontalAlign: 'right',
          // floating: false,
          // offsetY: -25,
          // offsetX: -5,
        },
      },
    }
  },
  computed: {
    max() {
      const cached = this.pressureMax
      return cached.sort()[0] - 2
    },
    min() {
      const cached = this.pressureMin
      return cached.sort()[this.pressureMin.length]
    },
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/scss/legend';

@include legend;
</style>
