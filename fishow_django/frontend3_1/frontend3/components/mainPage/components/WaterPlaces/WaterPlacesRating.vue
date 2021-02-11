<template>
  <div class="water-places-container">
    <div>
      <div>
        <h3>Водоем</h3>
        <div>
          <water-places-search @selected="showSelected" />
        </div>
      </div>
      <div>
        <h3>Рейтинг водоема</h3>
        <span v-if="waterPlace" class="rating">{{
          waterPlace.fish_rating
        }}</span>
        Составлен по оценке пользователей
      </div>
    </div>
    <div>
      <div v-if="waterPlace">
        <charts-regions :value="chartData" />
      </div>
    </div>
  </div>
</template>

<script>
import WaterPlacesSearch from '~/components/mainPage/components/WaterPlaces/WaterPlacesSearch'
import ChartsRegions from '~/components/Charts/ChartsRegions'
export default {
  name: 'WaterPlacesRating',
  components: {
    ChartsRegions,
    WaterPlacesSearch,
  },
  data() {
    return {
      waterPlace: null,
      chartData: null,
    }
  },
  methods: {
    showSelected(val) {
      this.waterPlace = val
      this.chartData = this.getChartData(val)
    },
    getChartData(val) {
      try {
        return JSON.parse(val.stat).main
      } catch (e) {
        console.error(e)
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Что то пошло не так при создании графика водоёмов.',
          type: 'is-danger',
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.water-places-container {
  display: flex;
  flex-wrap: wrap;
  & > div:first-child {
    display: flex;
    margin-top: 10px;
    & > div {
      padding: 10px;
    }
  }
  & > div {
    width: 100%;
    margin: 20px;
    @media screen and (max-width: 500px) {
      margin: 0;
    }
  }
}
</style>
