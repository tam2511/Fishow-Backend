<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">Суточное давление</span>
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
const time = [
  '0:00',
  '3:00',
  '6:00',
  '9:00',
  '12:00',
  '15:00',
  '18:00',
  '21:00',
]
export default {
  components: {
    VueApexCharts: () => import('vue-apexcharts'),
  },
  props: {
    pressureValue: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Суточное давление',
          data: this.pressureValue,
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
          categories: time,
        },
        yaxis: {
          min: 730,
          max: this.max,
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
      const cached = this.pressureValue
      return cached.sort()[0] - 2
    },
    min() {
      const cached = this.pressureValue
      return cached.sort()[this.pressureValue.length]
    },
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/scss/legend';

@include legend;
</style>
