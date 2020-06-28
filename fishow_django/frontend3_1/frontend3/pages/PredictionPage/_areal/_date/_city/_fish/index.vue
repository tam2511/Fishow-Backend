<template lang="pug">
  .columns
    .column.is-three-quarters
      FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
      FishowPredictionHeader
        DaysPicker(:days="date")
      FishSelectPrediction(:areal="areal" :city="city" :date="date")
      .box.result-container(v-if='readyData')
        PProbe(
          :days="days"
          :probMaxProp="predictions['prob_max']"
          :probMinProp="predictions['prob_min']"
        )
        Temperature(:readyData="readyData")
          ChartTemperature(
            :days="days"
            :tempMax="predictions['temperature_max']"
            :tempMin="predictions['temperature_min']"
          )
        Wind(
          :days="days"
          :windMean="predictions['wind_mean']"
          :windDirection="predictions['wind_direction']")
      EmptyPrediction(v-else)
    .column.fixed-top
      SideBar
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

// helpers
import getData from '@/pages/PredictionPage/_areal/_date/_city/_fish/getData'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import ChartTemperature from '~/components/predictPage/chart/ChartTemperature'

export default {
  components: {
    ChartTemperature,
    PProbe,
    SideBar,
    Temperature,
    FishowPredictionHeader,
    FishSelectPrediction,
    EmptyPrediction,
    PDataPicker,
    DaysPicker,
    FPBreadCrumbs,
    Wind,
  },
  data() {
    return {
      days: getData(this.$route.params.date, 9),
      fish: this.$route.params.fish,
      date: this.$route.params.date,
      city: this.$route.params.city,
      areal: this.$route.params.areal,
    }
  },
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
</style>
