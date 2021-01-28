<template>
  <div>
    <multiselect
      :options="options"
      :custom-label="nameWithLang"
      placeholder="Выберите город"
      label="areal"
      track-by="city"
      @input="changePrediction"
    ></multiselect>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import city from '@/components/predictPage/Menu/city'
export default {
  props: {
    value: {
      type: Object,
      default() {
        return {
          city: '',
          areal: '',
        }
      },
    },
    passive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      options: city,
    }
  },
  computed: {
    ...mapState('prediction', ['multiPrediction']),
  },
  watch: {
    value(val) {
      this.selected = val
    },
    selected(val) {
      this.$emit('input', val)
    },
  },
  methods: {
    nameWithLang({ areal, city }) {
      return `${city} - ${areal}`
    },
    changePrediction(value) {
      this.setLocation([value.city, value.areal])
      if (this.passive) return
      const fish = this.$route.params.fish
      const date = this.$route.params.date
      const city = value.city
      this.$route.params.city = city
      const areal = value.areal
      let url
      if (this.multiPrediction) {
        url = encodeURI(
          `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
        )
      } else {
        url = encodeURI(
          `/prediction/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
        )
      }
      if (this.multiPrediction) {
        console.log('получить для 9 дней')
        this.getPrediction(url)
      } else {
        console.log('получить для одного дня url = ', url)
        this.getPredictionOne(url)
      }
    },
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
      getPredictionOne: 'getPredictionOne',
      setLocation: 'setLocation',
    }),
  },
}
</script>

<style scoped></style>
