<template lang="pug">
  div.container
    div.row.row-50
      div.col-lg-8
        div.fishow-prediction
          HeaderPrediction
          FishSelectPrediction(:date="date" :city="city" :areal="areal")
          .result {{ areal }} {{ city }} {{ date }} {{ fish }}
          ul
            li(v-for="(prediciton, key) in predictions" :key="prediciton.id") {{ key}}: {{prediciton}}
      div.col-lg-4
        div.fishow-sidebar
          ul
            li(v-for="(prediciton, key, index) in predictions" :key="prediciton.id" @click="doScroll" :id="index") {{ key}}
</template>

<script>
import HeaderPrediction from '@/components/predictPage/HeaderPrediction'
import FishSelectPrediction from '@/components/predictPage/FishSelectPrediction'
export default {
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
  components: {
    HeaderPrediction,
    FishSelectPrediction,
  },
  data() {
    return {
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
  ul {
    background-color: var(--background-color-primary);
  }
  li {
    padding: 20px;
  }
}
</style>
