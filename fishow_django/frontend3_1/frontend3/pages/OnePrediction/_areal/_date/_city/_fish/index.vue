<template>
  <div>
    <FPBreadCrumbs :areal="areal" :city="city" :fish="fish" :date="date" />
    <div v-for="predict in prediction" :key="predict.id">
      {{ predict.id }}
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import FPBreadCrumbs from '~/components/predictPage/Menu/FPBreadCrumbs'
import urlData from '~/assets/mixins/prediction/urlData'
export default {
  components: { FPBreadCrumbs },
  mixins: [urlData],
  layout: 'prediction',
  computed: {
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
      title: 'Fishow - Прогноз на один день',
    }
  },
}
</script>

<style scoped></style>
