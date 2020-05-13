<template>
  <div>
    <apexchart
      v-if="active"
      type="area"
      height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'Prob',
  components: {
    apexchart: VueApexCharts
  },
  props: {
    info: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      active: false,
      series: [
        {
          name: 'min',
          data: null
        },
        {
          name: 'max',
          data: null
        }
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: 'line'
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 2,
          curve: 'smooth'
        },
        colors: ['#260f4b', '#66DA26', '#546E7A', '#e9e001', '#FF9800'],
        sparkline: {
          enabled: true
        },
        fill: {
          type: 'solid'
        },
        xaxis: {
          type: 'datetime',
          categories: [
            '2018-09-19T00:00:00.000Z',
            '2018-09-19T01:30:00.000Z',
            '2018-09-19T02:30:00.000Z',
            '2018-09-19T03:30:00.000Z',
            '2018-09-19T04:30:00.000Z',
            '2018-09-19T05:30:00.000Z',
            '2018-09-19T06:30:00.000Z'
          ]
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      }
    }
  },
  computed: {},
  created() {
    this.calculateMax()
  },
  methods: {
    calculateMax() {
      this.series[0].data = this.info.prob_min
      this.series[1].data = this.info.prob_max
      this.active = true
    }
  }
}
</script>

<style scoped lang="scss">
.icon-pogoda {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: baseline;
  justify-content: center;
  text-align: center;
  position: relative;
  span {
    position: absolute;
  }
}
</style>
