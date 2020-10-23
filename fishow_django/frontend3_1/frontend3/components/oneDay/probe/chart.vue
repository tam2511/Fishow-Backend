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
export default {
  components: {
    VueApexCharts: () => import('vue-apexcharts'),
  },
  props: {
    prob: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Cуточная вероятность клёва',
          data: this.prob,
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
          categories: [
            '0:00',
            '3:00',
            '6:00',
            '9:00',
            '12:00',
            '15:00',
            '18:00',
            '21:00',
          ],
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
      this.series = [
        {
          name: 'Cуточная вероятность клёва',
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
