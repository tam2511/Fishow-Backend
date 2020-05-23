<template lang="pug">
  div.container
    div.row.row-50
      div.col-lg-8
        div.fishow-prediction
          ul
            li(v-for="prediciton in predictions" :key="prediciton.id") {{prediciton}}
      div.col-lg-4
        div.fishow-sidebar
          ul
            li(v-for="i in 25" :key="i") {{ i }}
</template>

<script>
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
  data() {
    return {
      fish: this.$route.params.fish,
      date: this.$route.params.date,
      city: this.$route.params.city,
      areal: this.$route.params.areal,
    }
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
}
.fishow-prediction {
  min-height: 2000px;
  position: relative;
  li {
    min-height: 100px;
  }
}
</style>
