<template lang="pug">
  .columns
    .column.is-three-quarters
      FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
      FishowPredictionHeader
      FishSelectPrediction(:areal="areal" :city="city" :date="date")
      Temperature(
        :phenomenon="predictions['phenomenon']"
        :days="days"
        :tempMin="predictions['temperature_min']"
        :tempMean="predictions['temperature_mean']"
        :tempMax="predictions['temperature_max']"
        )
    .column.fixed-top
      SideBar
    b-loading(:is-full-page="true" :active.sync="isLoading" :can-cancel="true")
</template>

<script>
import FishowPredictionHeader from '@/components/predictPage/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/FishSelectPrediction'
import FPBreadCrumbs from '@/components/predictPage/FPBreadCrumbs'
import getData from '@/pages/PredictionPage/_areal/_date/_city/_fish/getData'
import ListParams from '~/components/predictPage/ListParams'
import Temperature from '~/components/predictPage/Temperature'
import SideBar from '~/components/predictPage/SideBar'

export default {
  components: {
    SideBar,
    Temperature,
    ListParams,
    FishowPredictionHeader,
    FishSelectPrediction,
    FPBreadCrumbs,
  },
  async asyncData({ $axios, route }) {
    try {
      const fish = route.params.fish
      const date = route.params.date
      const city = route.params.city
      const areal = route.params.areal
      const url = encodeURI(
        `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
      )
      const response = await $axios.get(url)
      return { predictions: response.data.results[0] }
    } catch (e) {
      console.log('e =', e)
    }
  },
  data() {
    return {
      isLoading: true,
      days: getData(this.$route.params.date, 9),
      fish: this.$route.params.fish,
      date: this.$route.params.date,
      city: this.$route.params.city,
      areal: this.$route.params.areal,
    }
  },
  created() {
    setTimeout(() => {
      this.isLoading = false
    }, 500)
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
