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
      type: String,
      required: true,
    },
    tempMean: {
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
          name: 'Максимальная суточная температура',
          data: JSON.parse(this.tempMax),
        },
        {
          name: 'Среднесуточная температура',
          data: JSON.parse(this.tempMean),
        },
        {
          name: 'Минимальная суточная температура',
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
        colors: ['#ba5f3d', 'rgba(173,121,30,0.29)', '#1e47ad'],
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
            breakpoint: 450,
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

  color: rgba(128, 128, 128, 0.8);
  span {
    position: relative;
  }
  &_max {
    color: #ba5f3d;
    &:after {
      @extend %legend-flag;
      background-color: #ba5f3d;
    }
  }
  &_mean {
    color: rgba(173, 121, 30, 1);
    &:after {
      @extend %legend-flag;
      background-color: rgba(173, 121, 30, 0.29);
    }
  }
  &_min {
    color: #1e47ad;
    &:after {
      @extend %legend-flag;
      background-color: #1e47ad;
    }
  }
  @media screen and (max-width: 450px) {
    font-size: 10px;
  }
}
</style>
