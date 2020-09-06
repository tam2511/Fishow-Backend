<template>
  <client-only>
    <div>
      <div class="legend">
        <span class="legend_max">Максимальное суточное давление</span>
        <span class="legend_min">Минимальное суточное давление</span>
      </div>
      <VueApexCharts
        width="100%"
        height="200px"
        type="bar"
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
          name: 'Максимальное суточное давление',
          data: JSON.parse(this.tempMax),
        },
        {
          name: 'Минимальное суточное давление',
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
        colors: ['#73a2a5', '#172a3b'],
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
          borderColor: 'rgba(231,231,231,0)',
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.0,
          },
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: getCalendarDay(this.days),
        },
        yaxis: {
          min: JSON.parse(this.tempMin).sort()[0] - 2,
          max: JSON.parse(this.tempMax).sort()[JSON.parse(this.tempMin).length],
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
  font-size: 14px;
  color: rgba(128, 128, 128, 0.8);
  span {
    position: relative;
  }
  &_max {
    color: #73a2a5;
    &:after {
      @extend %legend-flag;
      background-color: #73a2a5;
    }
  }
  &_min {
    color: #172a3b;
    &:after {
      @extend %legend-flag;
      background-color: #172a3b;
    }
  }
  @media screen and (max-width: 450px) {
    font-size: 10px;
  }
}
</style>
