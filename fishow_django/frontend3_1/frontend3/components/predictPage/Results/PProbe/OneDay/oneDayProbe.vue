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
      type: String,
      required: true,
    },
    probMax: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Максимальная суточная вероятность клёва',
          data: JSON.parse(this.probMax),
        },
        {
          name: 'Минимальная суточная вероятность клёва',
          data: JSON.parse(this.probMin),
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
            return Math.round(value * 100)
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
              y: 1,
              y2: 0.74,
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
          max: 1,
          labels: {
            formatter(value) {
              return Math.round(value * 100) + '%'
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
          name: 'Максимальная суточная температура',
          data: JSON.parse(this.probMax),
        },
        {
          name: 'Минимальная суточная температура',
          data: JSON.parse(this.probMin),
        },
      ]
    },
  },
}
</script>

<style scoped lang="scss">
%legend-flag {
  content: '';
  height: 10px;
  width: 10px;
  display: block;
  position: absolute;
  left: -15px;
  top: 7px;
}
.legend {
  display: flex;
  flex-flow: column;
  align-items: flex-end;

  color: rgba(128, 128, 128, 0.8);
  span {
    position: relative;
  }
  &_area {
    color: #1a5105;
    &:after {
      @extend %legend-flag;
      background-color: #1a5105;
    }
  }
  &_min {
    color: #172a3b;
    &:after {
      @extend %legend-flag;
      background-color: #172a3b;
    }
  }
  &_max {
    color: #51686a;
    &:after {
      @extend %legend-flag;
      background-color: #b0e4e8;
    }
  }

  @media screen and (max-width: 450px) {
    font-size: 10px;
  }
}
</style>
