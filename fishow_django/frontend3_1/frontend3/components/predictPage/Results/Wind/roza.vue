<template>
  <client-only>
    <div id="chart">
      <VueApexCharts
        type="radar"
        height="350"
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
    windRoza: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      series: [
        {
          name: 'Series 1',
          data: [
            this.windRoza['С'],
            this.windRoza['СВ'],
            this.windRoza['В'],
            this.windRoza['ЮВ'],
            this.windRoza['Ю'],
            this.windRoza['ЮЗ'],
            this.windRoza['З'],
            this.windRoza['СЗ'],
          ],
        },
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: 'radar',
        },
        xaxis: {
          categories: ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ'],
        },
      },
    }
  },
}
</script>

<style scoped></style>
