<template>
  <div class="fish">
    <ul>
      {{
        predictions
      }}
      <!--      <li v-for="prediction in predictions" :key="prediction.id"></li>-->
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, route }) {
    try {
      const fish = route.params.fish
      const date = route.params.date
      const city = route.params.city
      const areal = route.params.areal
      const response = await $axios.get(
        `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
      )
      return { predictions: response.data }
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

<style scoped></style>
