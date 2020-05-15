<template>
  <div>
    <apexchart
      :type="this.options.chart.type"
      height="350"
      :width="this.getWidth"
      :options="options"
      :series="options.series"
    ></apexchart>
    <div class="button-container">
      <button type="button" class="button button-gray-outline" @click="setArea">
        area
      </button>
      <button type="button" class="button button-gray-outline" @click="setBar">
        bar
      </button>
      <button
        type="button"
        class="button button-gray-outline"
        @click="setLines"
      >
        lines
      </button>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'Chart',
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    optionsChart: {
      type: Object,
      required: true,
    },
  },
  data() {
    const getData = (days) => {
      const someDate = new Date()
      const numberOfDaysToAdd = days
      someDate.setDate(someDate.getDate() + numberOfDaysToAdd)
      const dd = someDate.getDate()
      const mm = someDate.getMonth() + 1
      const newmm = mm.length > 1 ? mm : '0' + mm
      const someFormattedDate = dd + '/' + newmm
      return someFormattedDate
    }
    const result = []
    for (let i = 0; i < 9; i++) {
      result.push(getData(i))
    }

    return {
      options: {
        series: [
          {
            name: 'минимальное',
            data: this.optionsChart.probMin,
          },
          {
            name: 'максимальное',
            data: this.optionsChart.probMax,
          },
        ],
        chart: {
          height: 350,
          type: this.optionsChart.type,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            dataLabels: {
              position: 'top', // top, center, bottom
            },
          },
        },
        // colors: ['#ea5d55', '#299431'],
        // dataLabels: {
        //     enabled: true,
        // },
        dataLabels: {
          enabled: true,
          formatter(val) {
            return val
          },
          offsetY: -10,
          style: {
            fontSize: '12px',
            colors: ['var(--color-typo-primary)'],
          },
        },
        grid: {
          borderColor: 'var(--background-color-border)',
          row: {
            colors: ['var(--background-color-default)', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.2,
          },
        },
        markers: {
          size: 1,
        },
        // xaxis: {
        //     categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        //     title: {
        //         text: 'Month'
        //     }
        // },
        // xaxis: {
        //   type: 'datatime'
        // },
        // yaxis: {
        //     title: {
        //         text: ''
        //     },
        //     min: this.minMax.min,
        //     max: this.minMax.max
        // },
        xaxis: {
          categories: result,
          position: 'top',
          axisBorder: {
            show: true,
          },
          axisTicks: {
            show: false,
          },
          crosshairs: {
            fill: {
              type: 'gradient',
              gradient: {
                colorFrom: '#D8E3F0',
                colorTo: '#BED1E6',
                stops: [0, 100],
                opacityFrom: 0.4,
                opacityTo: 0.5,
              },
            },
          },
          tooltip: {
            enabled: true,
          },
        },
        yaxis: {
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: false,
            formatter(val) {
              return val + '%'
            },
          },
        },
        legend: {
          position: 'bottom',
          horizontalAlign: 'right',
          floating: true,
          offsetY: 0,
          offsetX: 0,
        },
      },
    }
  },
  computed: {
    getWidth() {
      const screen = document.body.offsetWidth
      let value
      if (screen > 1200) {
        value = 1000
      } else if (screen > 600 && screen < 1200) {
        value = screen - 150
      } else {
        value = screen - 40
      }
      return value
    },
  },
  methods: {
    setArea() {
      this.options.chart.type = 'area'
    },
    setBar() {
      this.options.chart.type = 'bar'
    },
    setLines() {
      this.options.chart.type = 'line'
    },
  },
}
</script>

<style scoped lang="scss">
//#5697ec
.button-container {
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  padding-left: 20px;
  button {
    margin-right: 20px;
    padding: 3px 14px;
  }
}
.apexcharts-text tspan {
  fill: var(--color-typo-primary);
}
</style>
