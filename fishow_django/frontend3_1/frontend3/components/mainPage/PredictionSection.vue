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
        <CitySearch v-model="selectedLocation" :passive="true" />
      </b-field>
      <b-field label="Выберите рыбу">
        <fish-select @select="selectFish" :fish-list="fishList" />
      </b-field>
      <button class="button is-primary" @click="createPrediction">
        Составить прогноз
      </button>
      <nuxt-link class="button" outlined :to="{ path: '/prognoz-kleva' }"
        >Подробнее</nuxt-link
      >
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import getData from '@/assets/js/getData2'
import fishList from '~/assets/data/fishList'

import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'
import PProbe from '~/components/predictPage/Results/PProbe/index'
import CitySearch from '~/components/predictPage/Menu/CitySearch'
import rightDate from '~/assets/mixins/prediction/rightDate'
import FishSelect from '~/components/predictPage/Menu/FishSelect'
export default {
  components: {
    FishSelect,
    CitySearch,
    PProbe,
    OneDayProbe,
  },
  mixins: [rightDate],
  data() {
    return {
      fishList,
      selectedFish: null,
      selectedLocation: { areal: 'Московская область', city: 'Москва' },
      typeLocation: '',
      errorEmptySelect: '',
      position: null,
    }
  },
  computed: {
    days() {
      return getData(this.rightDate, 9)
    },
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
  mounted() {
    this.createPrediction()
  },
  methods: {
    selectFish(val) {
      this.selectedFish = val
    },
    createPrediction() {
      this.errorEmptySelect = ''
      this.typeLocation = ''

      const fish = this.selectedFish || 'щука'
      const date = this.rightDate
      const city = this.location.city
      const areal = this.location.areal

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
  z-index: 2;
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
    h2 {
      font-weight: 500;
    }
  }
  .prediction-chart {
    width: 70%;
    &.template {
      position: relative;
    }
    & > div:not(:first-child) {
      filter: blur(3px);
      position: relative;
      pointer-events: none;
      &:after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(238, 238, 238, 0.3);
      }
    }
  }
  .prediction-select {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-flow: column;

    width: 270px;

    label {
      font-weight: 300;
    }
    .box.fish {
      padding: 0;
    }
    & > * {
      margin: 10px 0;
      width: 100%;
    }
    button {
      width: 100%;

      background: var(--main-color);
      border: 2px solid var(--main-color);
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
