<template>
  <client-only>
    <div>
      <VueApexCharts
        width="100%"
        height="300px"
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
    probMin: {
      type: Array,
      required: true,
    },
    probMax: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Максимальная суточная вероятность клёва',
          data: this.probMax,
        },
        {
          name: 'Минимальная суточная вероятность клёва',
          data: this.probMin,
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
        colors: ['#8ebbbf', '#172a3b'],
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
        annotations: {
          yaxis: [
            {
              y: 100,
              y2: 74,
              borderColor: '#4fbb26',
              fillColor: 'rgba(109,180,61,0.83)',
              label: {
                borderColor: '#4fbb26',
                style: {
                  color: '#fff',
                  background: '#4fbb26',
                },
              },
            },
          ],
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: getCalendarDay(this.days),
        },
        yaxis: {
          min: 0,
          max: 100,
          labels: {
            formatter(value) {
              return Math.round(value) + '%'
            },
          },
        },
        legend: {
          show: false,
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
  watch: {
    probMin() {
      this.updateData()
    },
  },
  methods: {
    updateData() {
      console.log('update data multi')
      this.series = [
        {
          name: 'Максимальная суточная вероятность клёва',
          data: this.probMax,
        },
        {
          name: 'Минимальная суточная вероятность клёва',
          data: this.probMin,
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
