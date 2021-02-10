<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">X</span>
        <span class="legend_mean">Y</span>
      </div>
      <VueApexCharts
        width="100%"
        type="line"
        :options="chartOptions"
        :series="series"
      ></VueApexCharts>
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
  },
  data() {
    return {
      series: [
        {
          name: 'Y',
          data: this.value.y.map((item) => item * 100),
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
          categories: this.value.x,
          labels: {
            formatter(value) {
              return Math.round(value)
            },
          },
        },
        yaxis: {
          min: 0,
          max: 100,
          labels: {
            formatter(value) {
              return Math.floor(value)
            },
          },
        },
        legend: {
          show: false,
        },
      },
    }
  },
  watch: {
    value(val) {
      this.series = [
        {
          name: 'ачевсмысле',
          data: val.y.map((item) => item * 100),
        },
      ]
    },
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/scss/legend';

@include legend;
</style>
