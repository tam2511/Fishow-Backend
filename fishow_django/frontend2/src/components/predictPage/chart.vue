<template>
  <div>
    <apexchart
      :type="this.options.chart.type"
      height="350"
      width="850"
      :options="options"
      :series="options.series"
    ></apexchart>
    <button type="button" @click="setArea">area</button>
    <button type="button" @click="setBar">bar</button>
    <button type="button" @click="setLines">lines</button>
  </div>
</template>

<script>
// import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'chart',
  props: {
    optionsChart: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      options: {
        series: [
          {
            name: 'High - 2013',
            data: this.optionsChart.probMin,
          },
          {
            name: 'Low - 2013',
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
          categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec',
          ],
          position: 'top',
          axisBorder: {
            show: false,
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
  // components: {
  //   apexchart: VueApexCharts
  // },
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

<style scoped></style>
