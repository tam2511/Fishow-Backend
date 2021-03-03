<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">{{ value.Y.name }}</span>
        <span class="legend_min">{{ value.X.name }}</span>
      </div>
      <vue-apex-charts
        v-if="chartX"
        width="100%"
        :type="chartType"
        :options="chartOptions"
        :series="series"
      ></vue-apex-charts>
    </div>
  </client-only>
</template>

<script>
export default {
  components: {
    VueApexCharts: () => import('vue-apexcharts'),
  },
  props: {
    value: {
      type: Object,
      required: true,
    },
    chartType: {
      type: String,
      default() {
        return 'area'
      },
    },
  },
  data() {
    return {
      series: [
        {
          type: 'column',
          name: this.value.Y.name,
          data: this.chartY,
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
        colors: ['#018cac', '#172a3b'],
        dataLabels: {
          enabled: true,
          formatter(value) {
            return Math.floor(value)
          },
        },
        stroke: {
          curve: 'smooth',
        },
        grid: {
          borderColor: '#e7e7e7',
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5,
          },
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: [],
          labels: {
            formatter(value) {
              return Math.round(value)
            },
          },
        },
        yaxis: {
          categories: this.value.X.name,
          min: 0,
          max: 100,
          labels: {
            formatter(value) {
              return Math.floor(value)
            },
          },
        },
        legend: {
          position: 'top',
          horizontalAlign: 'right',
          show: true,
        },
      },
    }
  },
  computed: {
    chartY() {
      return (this.value && this.value.Y && this.value.Y.values) || []
    },
    chartX() {
      return (this.value && this.value.X && this.value.X.values) || []
    },
  },
  watch: {
    value: {
      deep: true,
      immediate: true,
      handler(val) {
        this.series = [
          {
            name: val.Y.name,
            data: this.chartY,
          },
        ]
      },
    },
  },
  methods: {
    convertData(data) {
      if (data && data.Y && data.Y.values) {
        return data.Y.values
      } else {
        return null
      }
    },
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/scss/legend';

@include legend;
</style>
