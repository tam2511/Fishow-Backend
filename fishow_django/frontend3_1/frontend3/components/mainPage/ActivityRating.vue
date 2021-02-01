<template>
  <div class="activity-rating">
    <div class="activity-container">
      <div class="activity-title">Активность клева в регионе</div>
      <div class="activity-description">
        Динамика активности клева за месяц по отчетам рабыловов и историческим
        данным
      </div>
      <div class="activity-select">
        <div>
          <h3>Выберите регион</h3>
          <fetch-data endpoint="/region/">
            <template slot-scope="{ response: regions }">
              <div>
                <regions-search
                  v-if="regions.results"
                  :options="regions.results"
                  @select="selectRegion"
                />
              </div>
            </template>
          </fetch-data>
        </div>
        <div v-if="fish.length">
          <h3>Выберите рыбу</h3>
          <fish-select :options="fish" @select="selectFish" />
        </div>
      </div>
      <div v-if="selectedFish" class="activity-chart">
        <charts-regions :value="chartData" />
      </div>
    </div>
    <div class="rating-container">
      <div class="activity-title">Рейтинг водоемов</div>
      <div class="activity-description">
        Как много различных товаров и услуг оплачивают жители России?
      </div>
      <div class="activity-select">
        <div>
          <h3>Выберите водоём</h3>
        </div>
      </div>
      <div class="activity-chart"></div>
    </div>
  </div>
</template>

<script>
import FishSelect from '~/components/predictPage/Menu/FishSelect'
import RegionsSearch from '~/components/mainPage/components/Regions/regions-search'
import FetchData from '~/components/renderless/fetchData'
import ChartsRegions from '~/components/Charts/ChartsRegions'
export default {
  name: 'ActivityRating',
  components: { ChartsRegions, FetchData, RegionsSearch, FishSelect },
  data() {
    return {
      selectedRegion: null,
      selectedFish: null,
      waterPlaces: [],
      fish: [],
      stats: null,
      next: null,
      chartData: null,
    }
  },
  watch: {
    selectedRegion(val) {
      try {
        this.stats = JSON.parse(val.stat).main
        console.log('set stats')
      } catch (e) {
        this.stats = {
          error: true,
        }
        console.log('error!')
        console.error(e)
      }
    },
    stats(val) {
      for (const key in val) {
        this.fish.push(key)
      }
      console.log('fish done')

      this.fish = this.fish.map((item) => {
        return {
          title: item,
        }
      })
    },
  },
  methods: {
    selectRegion(val) {
      this.selectedRegion = val
      if (this.selectedFish) {
        this.selectFish(this.selectedFish)
      }
    },
    selectFish(val) {
      this.selectedFish = val
      this.chartData = this.stats[this.selectedFish]
    },
  },
}
</script>

<style lang="scss" scoped>
.activity {
  &-rating {
    display: flex;
    flex-flow: row;
    border-radius: 20px;
    border: 1px solid rgba(206, 209, 213, 0.4);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
    padding: 20px;
    & > div {
      width: 50%;
    }
  }
  &-description {
    height: 70px;
  }
  &-select {
    display: flex;
    & > div {
      width: 50%;
      margin: 20px;
    }
  }

  &-title {
    font-weight: 700;
    font-size: 20px;
    line-height: 42px;
  }
}
</style>
