<template>
  <div>
    <multiselect
      v-model="selected"
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
import { mapActions } from 'vuex'
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
      selected: null,
      options: city,
    }
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
    changePrediction() {
      this.setLocation([this.value.city, this.value.areal])
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
      setLocation: 'setLocation',
    }),
  },
}
</script>

<style scoped></style>
