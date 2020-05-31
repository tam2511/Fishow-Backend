<template lang="pug">
  div.container
    div.fishow-prediction
      Temperature(
        :phenomenon="predictions['phenomenon']"
        :days="days"
        :tempMin="predictions['temperature_min']"
        :tempMean="predictions['temperature_mean']"
        :tempMax="predictions['temperature_max']"
        )
    SideBar
</template>

<script>
// import HeaderPrediction from '@/components/predictPage/HeaderPrediction'
// import FishSelectPrediction from '@/components/predictPage/FishSelectPrediction'
// import FishSelectCarousel from '@/components/predictPage/FishSelectCarousel'
import getData from '@/pages/PredictionPage/_areal/_date/_city/_fish/getData'
import ListParams from '~/components/predictPage/ListParams'
import Temperature from '~/components/predictPage/Temperature'
import SideBar from '~/components/predictPage/SideBar'
export default {
  components: {
    SideBar,
    Temperature,
    ListParams,
    // HeaderPrediction,
    // FishSelectPrediction,
    // FishSelectCarousel,
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
      days: getData(this.$route.params.date, 9),
      fish: this.$route.params.fish,
      date: this.$route.params.date,
      city: this.$route.params.city,
      areal: this.$route.params.areal,
    }
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
.fish {
  display: flex;
  flex-flow: row;
}
.fishow-sidebar {
  position: fixed;
  margin: 70px 70px 0 70px;
  padding: 10px;
  min-width: 200px;
  right: 0;
  top: 0;
  background: var(--background-color-primary);
  border: 1px solid var(--background-color-border);
  li {
    cursor: pointer;
    &:hover {
      background-color: #1e347b;
      color: #fff;
    }
  }
}
.fishow-prediction {
  min-height: 2000px;
  position: relative;
  li {
    padding: 20px;
  }
}
</style>
