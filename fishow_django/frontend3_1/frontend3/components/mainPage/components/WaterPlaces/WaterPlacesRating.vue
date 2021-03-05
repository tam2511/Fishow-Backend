<template>
  <div class="water-places-container">
    <div>
      <div>
        <h3 class="rating-title">Водоем</h3>
        <div>
          <water-places-search @selected="showSelected" />
        </div>
      </div>
      <div class="rating-container">
        <h3 class="rating-title">Рейтинг водоема</h3>
        <div>
          <div class="rating-value">0</div>
          <div>
            <span v-if="waterPlace" class="rating">{{
              waterPlace.fish_rating
            }}</span>
            Составлен по оценке пользователей
          </div>
        </div>
      </div>
    </div>
    <div>
      <div v-if="waterPlace">
        <charts-regions :value="chartData" chart-type="bar" />
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
.rating-container {
  display: flex;

  flex-flow: wrap;
  & > div {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
}
.rating-title {
  width: 100%;
  padding-bottom: 10px;
  color: #878b90;
}
.rating-value {
  width: 40px;
  height: 40px;
  background-color: #44c77f;
  display: flex;
  justify-content: center;
  font-size: 21px;
  align-items: center;
  border-radius: 5px;
  margin-right: 10px;
  color: #fff;
}
</style>
