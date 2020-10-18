<template lang="pug">
  div.main-content
    FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
    FishowPredictionHeader
      DaysPicker(:days="date")
    FishSelectPrediction(
      :areal="areal"
      :city="city"
      :date="date"
      )
    .result-container(v-if='prediction')
      PProbe(
        :readyData="readyData"
      )
        OneDayProbe(
          ref="pprobe"
          :prob="prediction.prob")
      result-container(
        title="Погодные условия"
        type-of-result="temperature"
        :content="readyData.temperature_brief"
      )
        Temperature
      result-container(
        title="Ветер, м/с"
        type-of-result="wind"
        :content="prediction.wind_fish"
        )
        Wind
      result-container(
        title="Давление"
        type-of-result="pressure"
        :content="prediction.pressure_fish"
      )
        PressureContainer(:readyData="readyData")
          pressure-chart(
            :days="days"
            :pressureMax="prediction.pressure"
            :pressureMin="prediction.pressure"
            :one="true"
          )
      result-container(
        title="Луна"
        type-of-result="moon"
        )
        OneMoon(
          :moon="prediction.moon",
          :moon-desc="prediction.moon_desc",
          :moon-dir="prediction.moon_direction",
          :sun-down="prediction.sun_down",
          :sun-up="prediction.sun_up",
          :date="prediction.date"
        )
      result-container(
        title="Солнечная активность"
        type-of-result="uvindex"
        )
    EmptyPrediction(v-else)
</template>

<script>
import { mapState, mapActions } from 'vuex'
import FPBreadCrumbs from '~/components/predictPage/Menu/FPBreadCrumbs'
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
import EmptyPrediction from '@/components/predictPage/EmptyPrediction'
import urlData from '~/assets/mixins/prediction/urlData'
import Wind from '@/components/predictPage/Results/Wind/index'
import Temperature from '~/components/predictPage/Results/Temperature/index'
import PressureContainer from '~/components/predictPage/Results/Pressure/PressureContainer'
import PressureChart from '~/components/predictPage/Results/Pressure/PressureChart'

import PProbe from '~/components/predictPage/Results/PProbe/index'
import OneDayProbe from '~/components/oneDay/probe/chart'
import OneMoon from '~/components/oneDay/moon/OneMoon'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'

import ResultContainer from '~/components/predictPage/Results/resultContainer'

export default {
  components: {
    ResultContainer,
    FPBreadCrumbs,
    EmptyPrediction,
    DaysPicker,
    FishSelectPrediction,
    FishowPredictionHeader,
    OneDayProbe,
    OneMoon,
    PProbe,
    PressureChart,
    PressureContainer,
    Temperature,
    Wind,
  },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
    readyData() {
      console.log('this.prediction = ', this.prediction)
      const data = convertDataFromServer(this.prediction, true)
      console.log('before set = ', data)
      this.setReady(data)
      this.setDays(this.days)
      return data
    },
    ...mapState('prediction', ['prediction']),
  },
  created() {
    const fish = this.$route.params.fish
    const date = this.$route.params.date
    const city = this.$route.params.city
    const areal = this.$route.params.areal
    const url = encodeURI(
      `/prediction/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
    )
    console.log('url = ', url)
    console.log('start get prediction one ')
    this.getPredictionOne(url)
  },
  methods: {
    ...mapActions('prediction', {
      getPredictionOne: 'getPredictionOne',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
  head() {
    return {
      title:
        'Fishow - Прогноз клева рыбы на один день, вероятность клева, прогноз рыбалки на день',
    }
  },
}
</script>

<style scoped></style>
