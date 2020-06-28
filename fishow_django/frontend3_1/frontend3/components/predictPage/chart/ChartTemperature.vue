<template>
  <client-only>
    <VueApexCharts
      width="100%"
      type="line"
      :options="chartOptions"
      :series="series"
    ></VueApexCharts>
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
    tempMax: {
      type: String,
      required: true,
    },
    tempMin: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Максимальная среднесуточная температура',
          data: JSON.parse(this.tempMax),
        },
        {
          name: 'Минимальная среднесуточная температура',
          data: JSON.parse(this.tempMin),
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
        colors: ['#ba5f3d', '#1e63ad'],
        dataLabels: {
          enabled: true,
        },
        stroke: {
          // curve: 'smooth',
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
          categories: getCalendarDay(this.days),
        },
        yaxis: {
          min: 5,
          max: 30,
        },
        legend: {
          position: 'top',
          horizontalAlign: 'right',
          floating: false,
          offsetY: -25,
          offsetX: -5,
        },
      },
    }
  },
}
</script>

<style scoped></style>
