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
          <h3 class="activity-field-title">Ваш регион</h3>
          <regions-search
            v-if="regionsDone"
            v-model="selectedRegion"
            :options="regions"
            @select="selectRegion"
          />
        </div>
        <div v-if="fish.length">
          <h3 class="activity-field-title">Рыба</h3>
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
        На основе отчетов и оценках пользователей Вы можете наблюдать за
        распределением общего улова в течении года
      </div>
      <water-places-rating />
      <div class="activity-chart"></div>
    </div>
  </div>
</template>

<script>
import Http from '~/services/Http'
import FishSelect from '~/components/predictPage/Menu/FishSelect'
import RegionsSearch from '~/components/mainPage/components/Regions/regions-search'
import ChartsRegions from '~/components/Charts/ChartsRegions'
import WaterPlacesRating from '~/components/mainPage/components/WaterPlaces/WaterPlacesRating'
export default {
  name: 'ActivityRating',
  components: { WaterPlacesRating, ChartsRegions, RegionsSearch, FishSelect },
  data() {
    return {
      selectedRegion: null,
      selectedFish: '',
      waterPlaces: [],
      fish: [],
      stats: null,
      next: null,
      chartData: null,
      regions: [],
      regionsNext: null,
      regionsDone: false,
    }
  },
  mounted() {
    this.fetchRegions()
  },
  watch: {
    selectedRegion(val) {
      try {
        this.stats = JSON.parse(val.stat).main

        this.selectFish('щука')
      } catch (e) {
        this.stats = {
          error: true,
        }
        console.error(e)
      }
    },
    stats(val) {
      for (const key in val) {
        this.fish.push(key)
      }

      this.fish = this.fish.map((item) => {
        return {
          title: item,
        }
      })
    },
  },
  methods: {
    async fetchRegions(params = '') {
      try {
        const cache = sessionStorage.getItem('cache-regions')
        if (cache) {
          this.regions = JSON.parse(cache)
          this.selectRegion(this.regions[this.regions.length - 1])
          this.regionsDone = true
          return
        }
        const { data } = await Http.getRegions(params)
        this.regionsNext = data.next
        this.regions.push(...data.results)
        //
        if (this.regionsNext) {
          const next = this.regionsNext.split('/region/')[1]
          await this.fetchRegions(next)
        } else {
          this.selectRegion(this.regions[this.regions.length - 1])
          this.regionsDone = true
          sessionStorage.setItem('cache-regions', JSON.stringify(this.regions))
        }
      } catch (e) {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Что то пошло не так при загрузке регионов.',
          type: 'is-danger',
        })
      }
    },
    selectRegion(val) {
      console.log(val)
      this.selectedRegion = val
      // if (this.selectedFish) {
      //   this.selectFish(this.selectedFish)
      // }
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
  &-field-title {
    padding-bottom: 10px;
  }
  &-rating {
    display: flex;
    flex-flow: row;
    flex-wrap: wrap;
    border-radius: 20px;
    border: 1px solid rgba(206, 209, 213, 0.4);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
    & > div {
      width: 50%;
      padding: 20px;
      @media screen and (max-width: 500px) {
        width: 100%;
      }
    }
  }
  &-description {
    height: 70px;
    color: rgba(30, 30, 30, 0.66);
  }
  &-select {
    display: flex;
    min-height: 110px;
    & > div {
      width: 50%;
      margin: 20px;
    }
  }
  &-container {
    border-right: 1px solid #e7e7e7;
    @media screen and (max-width: 500px) {
      border-right: none;
      border-bottom: 1px solid #e7e7e7;
    }
  }
  &-title {
    font-weight: 500;
    font-size: 20px;
    line-height: 42px;
  }
}
</style>
