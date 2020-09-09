<template lang="pug">
  div.main-content
    FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
    FishowPredictionHeader
      DaysPicker(:days="date")
    FishSelectPrediction(:areal="areal" :city="city" :date="date")
    .result-container(v-if='prediction')
      PProbe(
        :readyData="prediction[0]"
      )
        div(v-for="predict in prediction" :key="predict.id" class="column")
          .box.card {{ predict.prob }}
      result-container(
        title="Погодные условия"
        type-of-result="temperature"
        :content="prediction[0].temperature_brief"
        )
      result-container(
        title="Ветер, м/с"
        type-of-result="wind"
        :content="prediction[0].wind_fish"
        )
      result-container(
        title="Давление"
        type-of-result="pressure"
        :content="prediction[0].pressure_fish"
        )
      result-container(title="Луна" type-of-result="moon")
      result-container(title="Солнечная активность" type-of-result="uvindex")
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

import PProbe from '~/components/predictPage/Results/PProbe/index'
import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'

import transformForChart from '~/pages/OnePrediction/_areal/_date/_city/_fish/transformForChart'
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
    PProbe,
  },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
    dataForChart() {
      return transformForChart(this.prediction)
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
    this.getPredictionOne(url)
  },
  methods: {
    ...mapActions('prediction', { getPredictionOne: 'getPredictionOne' }),
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
