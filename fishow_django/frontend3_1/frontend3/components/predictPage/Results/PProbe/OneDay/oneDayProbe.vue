<template>
  <client-only>
    <div>
      {{ probMin }}
      <button @click="updateData">update</button>
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
          name: 'Максимальная суточная температура',
          data: JSON.parse(this.probMax),
        },
        {
          name: 'Минимальная суточная температура',
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
        colors: ['#ba5f3d', '#1e63ad'],
        dataLabels: {
          enabled: true,
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
          categories: '',
        },
        yaxis: {
          min: 0,
          max: 1,
        },
        legend: {
          position: 'top',
          show: true,
          horizontalAlign: 'right',
          floating: false,
          offsetY: -25,
          offsetX: -5,
        },
      },
    }
  },
  // watch: {
  //   series() {
  //     this.series = [
  //       {
  //         name: 'Максимальная суточная температура',
  //         data: JSON.parse(this.probMax),
  //       },
  //       {
  //         name: 'Минимальная суточная температура',
  //         data: JSON.parse(this.probMin),
  //       },
  //     ]
  //   },
  // },
  methods: {
    updateData() {
      console.log('update!')
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

<style scoped></style>
