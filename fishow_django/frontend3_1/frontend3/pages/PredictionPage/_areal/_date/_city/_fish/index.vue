<template lang="pug">
  div
    FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
    FishowPredictionHeader
      DaysPicker(:days="date")
    FishSelectPrediction(:areal="areal" :city="city" :date="date")
    .result-container(v-if='readyData')
      PProbe(
        :readyData="readyData"
      )
        one-day-probe(
          ref="pprobe"
          :days="days"
          :probMax="predictions['prob_max']"
          :probMin="predictions['prob_min']"
        )
      Temperature(:readyData="readyData")
      Wind(:readyData="readyData"
        :days="days")
      PressureContainer(:readyData="readyData")
        pressure-chart(
          :days="days"
          :tempMax="predictions['pressure_max']"
          :tempMin="predictions['pressure_min']"
        )
      Moon(:readyData="readyData" :days="days")
    EmptyPrediction(v-else)
</template>

<script>
// vuex
import { mapState, mapActions } from 'vuex'

// menu items
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
import FPBreadCrumbs from '@/components/predictPage/Menu/FPBreadCrumbs'
import SideBar from '~/components/predictPage/Menu/SideBar'
import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
import PDataPicker from '@/components/predictPage/Menu/PDataPicker'

// if empty
import EmptyPrediction from '@/components/predictPage/EmptyPrediction'

// results
import Wind from '@/components/predictPage/Results/Wind/index'
import Temperature from '~/components/predictPage/Results/Temperature/index'
import PProbe from '~/components/predictPage/Results/PProbe/index'
import PressureContainer from '~/components/predictPage/Results/Pressure/PressureContainer'
import Moon from '~/components/predictPage/Results/Moon/Moon'

// helpers

import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import ChartTemperature from '~/components/predictPage/chart/ChartTemperature'
import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'
import PressureChart from '~/components/predictPage/Results/Pressure/PressureChart'
import urlData from '~/assets/mixins/prediction/urlData'
export default {
  components: {
    PressureChart,
    OneDayProbe,
    ChartTemperature,
    PProbe,
    SideBar,
    Temperature,
    FishowPredictionHeader,
    FishSelectPrediction,
    EmptyPrediction,
    PressureContainer,
    PDataPicker,
    DaysPicker,
    FPBreadCrumbs,
    Wind,
    Moon,
  },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
    readyData() {
      return convertDataFromServer(this.predictions)
    },
    ...mapState('prediction', ['predictions']),
  },
  created() {
    const fish = this.$route.params.fish
    const date = this.$route.params.date
    const city = this.$route.params.city
    const areal = this.$route.params.areal
    const url = encodeURI(
      `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
    )
    this.getPrediction(url)
  },
  methods: {
    ...mapActions('prediction', { getPrediction: 'getPrediction' }),
  },
  head() {
    return {
      title: 'Fishow - Прогноз',
    }
  },
}
</script>

<style scoped lang="scss">
.fixed-top {
  position: fixed;
  top: 135px;
  right: 0;
  width: 26%;
  @media screen and (max-width: 768px) {
    display: none;
  }
}
.result-container > .box {
  background: radial-gradient(circle, #eff2ff 0%, #cac7c8 100%);
}
</style>
