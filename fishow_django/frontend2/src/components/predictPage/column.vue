<template>
  <div class="results-prediction">
    <section class="section section-variant-1 section-view">
      <div class="fishow_container container container__small" v-if="isLoading">
        <span
          >{{ this.areal }} / {{ this.city }} | Прогноз на близжайшие 10 дней -
          {{ this.fish }} - дата {{ this.date }}</span
        >
        <div class="fishow_row">
          <!--        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">-->
          <!--          Пн-->
          <!--          {{ index + 1 }}-->
          <!--        </div>-->
        </div>
        <div class="fishow_row">
          <!--          <one-colum />-->
        </div>
        <div class="fishow_row">
          Среднесуточная температура
        </div>
        <div class="fishow_row">
          <chart
            :optionsChart="{
              type: 'bar',
              probMin: predictions.temperature_min,
              probMax: predictions.temperature_max,
              max: 15,
              min: 0,
            }"
          />
        </div>
        <div class="fishow_row">
          Вероятность клева
        </div>
        <div class="fishow_row">
          <chart
            :optionsChart="{
              type: 'area',
              probMin: predictions.prob_min,
              probMax: predictions.prob_max,
              max: 1,
              min: 0,
            }"
          />
        </div>
        <div class="fishow_row">
          Давление, мм рт.ст.
        </div>
        <div class="fishow_row">
          <chart
            :optionsChart="{
              type: 'area',
              probMin: predictions.pressure_min,
              probMax: predictions.pressure_max,
              max: 740,
              min: 650,
            }"
          />
        </div>
        <div class="fishow_row">
          Ветер, м/с
        </div>
        <div class="fishow_row">
          <chart
            :optionsChart="{
              type: 'area',
              probMin: predictions.wind_mean,
              probMax: predictions.wind_mean,
              max: 10,
              min: 0,
            }"
          />
        </div>
        <!--        <div class="fishow_row">-->
        <!--          Погода-->
        <!--        </div>-->
        <!--        <div class="fishow_row">-->
        <!--          <span v-for="pog in predictions.phenomenon" :key="pog">{{-->
        <!--            pog[0]-->
        <!--          }}</span>-->
        <!--        </div>-->
        <!--      <div class="fishow_row">-->
        <!--        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">-->
        <!--          <icon-pogoda-->
        <!--            :maxValue="700"-->
        <!--            :minValue="650"-->
        <!--            color="&#45;&#45;green"-->
        <!--            :height="0.08"-->
        <!--            :margin-text="30"-->
        <!--          />-->
        <!--        </div>-->
        <!--      </div>-->
        <!--      <div class="fishow_row">-->
        <!--        Давление, мм рт.ст.-->
        <!--      </div>-->
        <!--      <div class="fishow_row">-->
        <!--        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">-->
        <!--          <icon-pogoda-->
        <!--            :maxValue="90"-->
        <!--            :minValue="80"-->
        <!--            color="&#45;&#45;teal"-->
        <!--            :height="1.5"-->
        <!--            :margin-text="3"-->
        <!--          />-->
        <!--        </div>-->
        <!--      </div>-->
        <!--      <div class="fishow_row">-->
        <!--        Относительная влажность, %-->
        <!--      </div>-->
        <!--      <div class="fishow_row">-->
        <!--        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">-->
        <!--          <icon-pogoda-->
        <!--            :maxValue="5"-->
        <!--            :minValue="3"-->
        <!--            color="&#45;&#45;cyan"-->
        <!--            :height="10"-->
        <!--            :margin-text="0.5"-->
        <!--          />-->
        <!--        </div>-->
        <!--      </div>-->
        <!--      <div class="fishow_row">-->
        <!--        Ультрафиолетовый индекс, баллы-->
        <!--      </div>-->
      </div>
      <div v-if="error !== ''" class="container container__small">
        <h2>{{ this.error }}</h2>
        <router-link
          :to="{ name: 'PredictPage' }"
          class="button button-xl badge-orange"
          >Назад</router-link
        >
      </div>
    </section>
  </div>
</template>

<script>
import Chart from './chart'
import { mapState } from 'vuex'
import { Loading } from 'element-ui'
export default {
  name: 'colum',
  props: ['areal', 'date', 'fish', 'city'],
  data() {
    return {
      error: '',
      isLoading: false,
    }
  },
  components: { Chart },
  computed: {
    ...mapState(['predictions']),
    // this.isLoading = true
  },
  methods: {
    loadingfunc() {
      const options = {
        target: document.querySelector('body'),
        fullscreen: true,
        lock: true,
        background: 'var(--background-color-default)',
      }
      let loadingInstance = Loading.service(options)
      setTimeout(() => {
        if (this.predictions) {
          this.isLoading = true
          loadingInstance.close()
        } else {
          this.error = 'Прогноз не найден, напишите Саньку'
          loadingInstance.close()
        }
      }, 2000)
    },
  },
  created() {
    const endpoint = `/api/predictionten/?areal=${this.areal}&date=${this.date}&city=${this.city}&fish=${this.fish}`
    this.$store.dispatch('fetchPredictionTen', endpoint)
    this.loadingfunc()
  },
}
</script>

<style scoped lang="scss">
.section-variant-1 {
  @media screen and (max-width: 600px) {
    padding: 0;
  }
}
tspan {
  fill: var(--color-typo-primary);
}
.results-prediction {
  min-height: 1500px;
}
.fishow_row {
  margin-top: 10px;
  color: var(--color-typo-primary);
  width: 100%;
  display: flex;
  font-size: 20px;
  flex-flow: column;
  justify-content: space-around;
  align-items: center;
  transition: 0.2s;
  &_temp {
    background: linear-gradient(
      0deg,
      var(--blue) 55%,
      rgba(0, 212, 255, 0) 56%
    );
  }
}
.fishow_row_element {
  padding-right: 4px;
  padding-left: 4px;
  color: var(--color-typo-primary);
  width: 100%;
  height: 100%;
  display: flex;
  align-items: baseline;
  justify-content: center;
  text-align: center;
}
.container__small {
  opacity: 1;
  /*max-width: 900px;*/
  padding: 40px;
  border: none;
  min-height: 500px;
  box-shadow: 0 7px 18px rgba(0, 0, 0, 0.13);
  background-color: var(--background-color-primary);
  &_menu {
    max-width: 500px;
  }
  transition: all 0.3s;

  @media screen and (max-width: 600px) {
    /*width: 1024px !important;*/
    max-height: 100% !important;
  }
}
</style>
