<template lang="pug">
  div.main-content
    FPBreadCrumbs(:areal="areal" :city="city" :fish="fish" :date="date")
    FishowPredictionHeader
      DaysPicker(:days="date")
    FishSelectPrediction(:areal="areal" :city="city" :date="date")
    .columns.is-2(v-if='readyData')
      div(v-for="predict in prediction" :key="predict.id" class="column")
        .box.card
          .card-content {{ predict.date }}
    EmptyPrediction(v-else)
</template>

<script>
import { mapState, mapActions } from 'vuex'
import FPBreadCrumbs from '~/components/predictPage/Menu/FPBreadCrumbs'
import FishowPredictionHeader from '@/components/predictPage/Menu/FishowPredictionHeader'
import FishSelectPrediction from '@/components/predictPage/Menu/FishSelectPrediction'
import SideBar from '~/components/predictPage/Menu/SideBar'
import DaysPicker from '~/components/predictPage/Menu/DaysPicker'
import EmptyPrediction from '@/components/predictPage/EmptyPrediction'
import urlData from '~/assets/mixins/prediction/urlData'

import { convertDataFromServer } from '@/assets/js/convertDataFromServer'

export default {
  components: {
    FPBreadCrumbs,
    EmptyPrediction,
    DaysPicker,
    SideBar,
    FishSelectPrediction,
    FishowPredictionHeader,
  },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
    readyData() {
      return convertDataFromServer(this.predictions)
    },
    ...mapState('prediction', ['prediction']),
  },
  created() {
    const fish = this.$route.params.fish
    const date = this.$route.params.date
    const city = this.$route.params.city
    const areal = this.$route.params.areal
    const url = encodeURI(
      `/prediction/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
    )
    this.getPredictionOne(url)
  },
  methods: {
    ...mapActions('prediction', { getPredictionOne: 'getPredictionOne' }),
  },
  head() {
    return {
      title:
        'Fishow - Прогноз клева рыбы на один день, вероятность клева, прогноз рыбалки на день',
    }
  },
}
</script>

<style scoped></style>
