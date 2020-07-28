<template>
  <div class="miniPrediction">
    {{ readyData }}
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
export default {
  computed: {
    readyData() {
      return convertDataFromServer(this.predictions)
    },
    ...mapState('prediction', ['predictions']),
  },
  created() {
    const date = '2020-07-18'
    const url = encodeURI(
      `/predictionten/?areal=Московская область&date=${date}&city=Москва&fish=Щука`
    )
    this.getPrediction(url)
    console.log('this.readyData = ', this.readyData)
  },
  methods: {
    ...mapActions('prediction', { getPrediction: 'getPrediction' }),
  },
}
</script>

<style scoped></style>
