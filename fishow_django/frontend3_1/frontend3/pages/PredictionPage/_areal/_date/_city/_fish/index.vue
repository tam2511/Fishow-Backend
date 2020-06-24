<template lang="pug">
  .columns
    .column.is-three-quarters
      FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
      FishowPredictionHeader
        PDataPicker(:date2="date")
      FishSelectPrediction(:areal="areal" :city="city" :date="date")
      .box(v-if='predictions')
        PProbe(
          :days="days"
          :probMaxProp="predictions['prob_max']"
          :probMinProp="predictions['prob_min']"
        )
        Temperature(
          :phenomenon="predictions['phenomenon']"
          :days="days"
          :tempMin="predictions['temperature_min']"
          :tempMean="predictions['temperature_mean']"
          :tempMax="predictions['temperature_max']"
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
import { mapState, mapActions } from 'vuex'
import FishowPredictionHeader from '@/components/predictPage/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/FishSelectPrediction'
import FPBreadCrumbs from '@/components/predictPage/FPBreadCrumbs'
import Wind from '@/components/predictPage/Wind'
import EmptyPrediction from '@/components/predictPage/EmptyPrediction'
import getData from '@/pages/PredictionPage/_areal/_date/_city/_fish/getData'
import ListParams from '~/components/predictPage/ListParams'
import PDataPicker from '@/components/predictPage/PDataPicker'
import Temperature from '~/components/predictPage/Temperature'
import SideBar from '~/components/predictPage/SideBar'
import PProbe from '~/components/predictPage/PProbe'

export default {
  components: {
    PProbe,
    SideBar,
    Temperature,
    ListParams,
    FishowPredictionHeader,
    FishSelectPrediction,
    EmptyPrediction,
    PDataPicker,
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
    setTimeout(() => {
      console.log('this.result = ', this.predictions)
      try {
      } catch (e) {
        console.error(e)
      }
    }, 2000)
  },
  methods: {
    doScroll(event) {
      const list = [...document.querySelectorAll('.fishow-prediction li')]
      const newList = []
      list.forEach((item) => newList.push(item.getBoundingClientRect().y))
      console.log('event = ', event.target.id)
      window.scrollBy({
        top: newList[event.target.id] - 70,
        behavior: 'smooth',
      })
    },
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
