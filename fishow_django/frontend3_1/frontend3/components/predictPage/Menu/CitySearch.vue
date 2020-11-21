<template>
  <div>
    <!--    {{ list }}-->
    <!--    <label class="typo__label">Select with search</label>-->
    <multiselect
      v-model="value"
      :options="options"
      :custom-label="nameWithLang"
      placeholder="Выберите город"
      label="areal"
      track-by="city"
      @input="changePrediction"
    ></multiselect>
    <!--    {{ value }}-->
    <!--    <pre class="language-json"><code>{{ value  }}</code></pre>-->
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import city from '@/components/predictPage/Menu/city'
export default {
  props: {
    passive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      value: '',
      options: city,
    }
  },
  methods: {
    nameWithLang({ areal, city }) {
      return `${areal} - ${city}`
    },
    changePrediction() {
      if (this.passive) return
      const fish = this.$route.params.fish
      const date = this.$route.params.date
      const city = this.value.city
      this.$route.params.city = city
      const areal = this.value.areal
      const url = encodeURI(
        `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
      )
      this.getPrediction(url)
    },
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
    }),
  },
}
</script>

<style scoped></style>
