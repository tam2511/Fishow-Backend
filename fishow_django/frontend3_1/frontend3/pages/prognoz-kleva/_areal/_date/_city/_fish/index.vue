<template lang="pug">
  div.main-content
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

      Temperature

      result-container(
        title="Ветер, м/с",
        type-of-result="wind",
        :content="readyData.wind_desc"
      )
        Wind
      PressureContainer(:readyData="readyData")
        pressure-chart(
          :days="days"
          :pressureMax="predictions['pressure_max']"
          :pressureMin="predictions['pressure_min']"
        )
      Moon
      Uvindexfull
    EmptyPrediction(v-else)
</template>

<script>
// vuex
import { mapState, mapActions } from 'vuex'

// menu items
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
import FPBreadCrumbs from '@/components/predictPage/Menu/FPBreadCrumbs'
import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
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
import Uvindexfull from '~/components/predictPage/Results/UVindex/uvindexfull'
import ResultContainer from '~/components/predictPage/Results/resultContainer'
export default {
  components: {
    ResultContainer,
    Uvindexfull,
    PressureChart,
    OneDayProbe,
    ChartTemperature,
    PProbe,
    Temperature,
    FishowPredictionHeader,
    FishSelectPrediction,
    EmptyPrediction,
    PressureContainer,
    DaysPicker,
    FPBreadCrumbs,
    Wind,
    Moon,
  },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
    readyData() {
      const data = convertDataFromServer(this.predictions)
      this.setReady(data)
      this.setDays(this.days)
      return data
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
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
  head() {
    return {
      title:
        'Fishow - Прогноз клева на 9 дней, вероятность клева рыбы, погодные условия',
    }
  },
}
</script>

<style lang="scss">
.fixed-top {
  position: fixed;
  top: 135px;
  right: 0;
  width: 26%;
  @media screen and (max-width: 768px) {
    display: none;
  }
}
.main-content {
  margin-top: 1rem;
}
.box {
  font-weight: 300;
}
</style>
