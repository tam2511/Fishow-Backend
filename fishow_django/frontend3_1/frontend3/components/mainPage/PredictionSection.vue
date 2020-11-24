<template>
  <div class="prediction-section">
    <div class="prediction-title">
      <h2 class="title">Прогноз клева</h2>
    </div>
    <div v-if="readyData" :class="classOfChart">
      <div v-if="predictions.template" class="template-message">
        Данный прогноз временно недоступен
      </div>
      <PProbe :ready-data="readyData" :main-page="true">
        <one-day-probe
          ref="pprobe"
          :days="days"
          :prob-max="predictions && predictions['prob_max']"
          :prob-min="predictions && predictions['prob_min']"
        ></one-day-probe>
      </PProbe>
    </div>
    <div class="prediction-select">
      <b-field
        label="Выберите место рыбалки"
        :type="typeLocation"
        :message="errorEmptySelect"
      >
        <CitySearch :passive="true" />
      </b-field>
      <b-field label="Выберите рыбу">
        <fish-select-prediction :passive="true" />
      </b-field>
      <!--      <div>position: {{ position }}</div>-->
      <button @click="createPrediction" class="button is-primary">
        Составить прогноз
      </button>
      <nuxt-link class="button is-text" :to="{ path: '/prognoz-kleva' }"
        >Подробнее</nuxt-link
      >
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import getData from '@/pages/prognoz-kleva/_areal/_date/_city/_fish/getData'

import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'
import PProbe from '~/components/predictPage/Results/PProbe/index'
import CitySearch from '~/components/predictPage/Menu/CitySearch'
import FishSelectPrediction from '~/components/predictPage/Menu/FishSelectPrediction'
export default {
  components: {
    FishSelectPrediction,
    CitySearch,
    PProbe,
    OneDayProbe,
  },
  data() {
    return {
      days: getData('2020-10-02', 9),
      typeLocation: '',
      errorEmptySelect: '',
      position: null,
    }
  },
  computed: {
    readyData() {
      const data = convertDataFromServer(this.predictions)
      this.setReady(data)
      this.setDays(this.days)
      return data
    },
    classOfChart() {
      return this.predictions.template
        ? ' prediction-chart template'
        : 'prediction-chart'
    },
    ...mapState('prediction', ['predictions', 'fishId', 'location']),
  },
  created() {
    const fish = 'щука'
    // const fish = this.$route.params.fish
    const date = '2020-10-02'
    // const date = this.$route.params.date
    const city = 'Белово'
    // const city = this.$route.params.city
    const areal = 'Кемеровская область'
    // const areal = this.$route.params.areal
    const url = encodeURI(
      `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
    )
    this.getPrediction(url)
  },
  // mounted() {
  //   this.getPosition()
  // },
  methods: {
    getPosition() {
      const positionCB = (position) => {
        this.position = [position.coords.latitude, position.coords.longitude]
      }
      if (navigator && navigator.geolocation) {
        console.log('start search position')
        navigator.geolocation.getCurrentPosition(positionCB, this.showError)
      }
    },
    showError(error) {
      switch (error.code) {
        case error.PERMISSION_DENIED:
          this.position = 'User denied the request for Geolocation.'
          break
        case error.POSITION_UNAVAILABLE:
          this.position = 'Location information is unavailable.'
          break
        case error.TIMEOUT:
          this.position = 'The request to get user location timed out.'
          break
        case error.UNKNOWN_ERROR:
          this.position = 'An unknown error occurred.'
          break
      }
    },
    createPrediction() {
      if (!this.location) {
        this.errorEmptySelect = 'Выберите место рыбалки'
        this.typeLocation = 'is-danger'
        return
      }
      this.errorEmptySelect = ''
      this.typeLocation = ''

      const fish = this.fishId || 'щука'
      // const fish = this.$route.params.fish
      const date = '2020-10-02'
      // const date = this.$route.params.date
      const city = (this.location && this.location[0]) || 'Москва'
      // const city = this.$route.params.city
      const areal = (this.location && this.location[1]) || 'Московская область'
      // const areal = this.$route.params.areal

      const url = encodeURI(
        `/predictionten/?areal=${areal}&date=${date}&city=${city}&fish=${fish}`
      )
      this.getPrediction(url)
    },
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
}
</script>

<style scoped lang="scss">
.template-message {
  position: absolute;
  transform: translate(-50%, -50%);
  left: 50%;
  top: 50%;

  font-size: 20px;
}
.prediction-section {
  display: flex;
  flex-flow: row wrap;
  margin: 40px 0;
  justify-content: space-between;
  .prediction-box {
    border: 1px solid rgba(206, 209, 213, 0.4);
    box-sizing: border-box;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
  }
  .prediction-title {
    width: 100%;
    margin: 25px 0;
  }
  .prediction-chart {
    width: 70%;
    &.template {
      position: relative;
    }
    & > div:not(:first-child) {
      filter: blur(3px);
      opacity: 0.3;
      pointer-events: none;
    }
  }
  .prediction-select {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-flow: column;

    width: 270px;
    .box.fish {
      padding: 0;
    }
    & > * {
      margin: 10px 0;
      width: 100%;
    }
    button {
      width: 100%;

      background: #018cac;
      border: 2px solid #018cac;
      box-sizing: border-box;
      border-radius: 4px;
      padding: 10px 30px;
      font-size: 16px;
      line-height: 26px;
      color: #fff;
      text-align: center;
    }
  }
  @media screen and (max-width: 768px) {
    justify-content: center;
    .prediction-chart {
      width: 100%;
    }
    .prediction-title {
      margin: 25px 10px;
    }
  }
}
</style>
