<template lang="pug">
  div
    .result-container(v-if='readyData')
      PProbe(
        :readyData="readyData"
      )
        one-day-probe(
          ref="pprobe"
          :days="days"
          :probMax="predictions['prob_max']"
          :probMin="predictions['prob_min']"
        )

      result-container(
        title="Погодные условия"
        type-of-result="temperature"
        :content="readyData.temperature_brief"
      )
        Temperature

      result-container(
        title="Ветер, м/с",
        type-of-result="wind",
        :content="readyData.wind_desc"
      )
        Wind

      result-container(
        title="Давление"
        type-of-result="pressure"
        :content="readyData.pressure_fish"
      )
        PressureContainer(:readyData="readyData")
          pressure-chart(
            :days="days"
            :pressureMax="predictions['pressure_max']"
            :pressureMin="predictions['pressure_min']"
          )

      Moon
      Uvindexfull
    EmptyPrediction(v-else)
</template>

<script>
// vuex
import { mapState, mapActions } from 'vuex'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import { predictionTen } from '~/assets/descriptions'
// mixins
import urlData from '~/assets/mixins/prediction/urlData'
import predictionTemp from '~/assets/mixins/prediction/predictionTemp'
// results
import Moon from '~/components/predictPage/Results/Moon/Moon'
import ChartTemperature from '~/components/predictPage/chart/ChartTemperature'
import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'

export default {
  components: {
    OneDayProbe,
    ChartTemperature,
    Moon,
  },
  mixins: [urlData, predictionTemp],
  layout: 'prediction',
  computed: {
    readyData() {
      const data = convertDataFromServer(this.predictions)
      this.setReady(data)
      this.setDays(this.days)
      return data
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
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
  head() {
    return {
      title: predictionTen.title,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content: predictionTen.description,
        },
      ],
    }
  },
}
</script>

<style lang="scss">
.fixed-top {
  position: fixed;
  top: 135px;
  right: 0;
  width: 26%;
  @media screen and (max-width: 768px) {
    display: none;
  }
}
.main-content {
  margin-top: 1rem;
}
.box {
  font-weight: 300;
}
</style>
