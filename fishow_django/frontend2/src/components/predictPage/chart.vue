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
      <button type="button" @click="setArea" class="button button-fifth">
        area
      </button>
      <button type="button" @click="setBar" class="button button-fifth">
        bar
      </button>
      <button type="button" @click="setLines" class="button button-fifth">
        lines
      </button>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'chart',
  props: {
    optionsChart: {
      type: Object,
      required: true,
    },
  },
  computed: {
    getWidth() {
      let screen = document.body.offsetWidth
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
    console.log('result = ', result)

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
          formatter: function (val) {
            return val
          },
          offsetY: -10,
          style: {
            fontSize: '12px',
            colors: ['#304758'],
          },
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
            formatter: function (val) {
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
  components: {
    apexchart: VueApexCharts,
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
</style>
