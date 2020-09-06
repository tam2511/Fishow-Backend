import getData from '@/pages/prognoz-kleva/_areal/_date/_city/_fish/getData'

export default {
  data() {
    return {
      days: getData(this.$route.params.date, 9),
      fish: this.$route.params.fish,
      date: this.$route.params.date,
      city: this.$route.params.city,
      areal: this.$route.params.areal,
    }
  },
}
