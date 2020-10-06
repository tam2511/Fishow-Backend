<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">Максимальная суточная температура</span>
        <span class="legend_mean">Среднесуточная температура</span>
        <span class="legend_min">Минимальная суточная температура</span>
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
      type: Array,
      required: true,
    },
    tempMean: {
      type: Array,
      required: true,
    },
    tempMin: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Максимальная суточная температура',
          data: this.tempMax,
        },
        {
          name: 'Среднесуточная температура',
          data: this.tempMean,
        },
        {
          name: 'Минимальная суточная температура',
          data: this.tempMin,
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
        colors: ['#b0e4e8', 'rgba(173,121,30,0.29)', '#172a3b'],
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
          min: this.tempMin.sort()[0] - 2,
          max: this.tempMax.sort()[this.tempMin.length],
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
        responsive: [
          {
            breakpoint: 768,
            options: {
              chart: {
                height: 350,
                type: 'bar',
              },
              yaxis: {
                labels: {
                  show: false,
                },
              },
              plotOptions: {
                bar: {
                  horizontal: false,
                },
              },
              legend: {
                position: 'bottom',
              },
            },
          },
        ],
      },
    }
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/scss/legend';

@include legend;
</style>
