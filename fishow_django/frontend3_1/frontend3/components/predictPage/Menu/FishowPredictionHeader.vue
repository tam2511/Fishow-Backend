<template>
  <div class="card box">
    <div class="columns">
      <div class="column">
        <slot></slot>

        <!--        {{ $route }}-->
        <div class="buttons">
          <b-button>
            <nuxt-link
              :to="{
                name: 'prognoz-kleva-areal-date-city-fish',
                params: {
                  areal: $route.params.areal,
                  city: $route.params.city,
                  date: rightDate,
                  fish: $route.params.fish,
                },
              }"
            >
              Прогноз на 9 дней
            </nuxt-link>
          </b-button>
        </div>
      </div>
      <div class="column">
        <h1 class="title">Прогноз клева на {{ day }}</h1>
        <span>
          Наслаждайтесь спланированной рыбалкой в {{ city }} и отличным клевом
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import rightDate from '~/assets/mixins/prediction/rightDate'
export default {
  mixins: [rightDate],
  data() {
    return {
      niceDays: null,
    }
  },
  computed: {
    city() {
      let result = null
      if (this.multiPrediction) {
        if (this.predictions && this.predictions.city) {
          result = this.predictions.city
        }
      } else if (this.prediction && this.prediction.city) {
        result = this.prediction.city
      }
      return result
    },
    day() {
      return this.niceDays && this.niceDays[0] === '0'
        ? this.niceDays.split('0')[1]
        : this.niceDays
    },
    ...mapState('prediction', ['multiPrediction', 'prediction', 'predictions']),
  },
  mounted() {
    this.convertDays()
  },
  methods: {
    convertDays() {
      const whatMonth = {
        '01': 'Января',
        '02': 'Февраля',
        '03': 'Марта',
        '04': 'Апреля',
        '05': 'Мая',
        '06': 'Июня',
        '07': 'Июля',
        '08': 'Августа',
        '09': 'Сентября',
        10: 'Октября',
        11: 'Ноября',
        12: 'Декабря',
      }
      const day = this.$route.params.date.split('-')
      const month = day[1].length < 2 ? '0' + day[1] : day[1]
      const result = whatMonth[month]
      this.niceDays = day[2] + ' ' + result
    },
  },
}
</script>

<style scoped>
.card {
  min-height: 250px;

  background: url('/prediction_background.jpg') no-repeat center;
  background-size: cover;
}
.title,
.column span {
  color: #fff;
}

@media screen and (max-width: 1200px) {
  .columns {
    flex-flow: column;
  }
  .card {
    min-height: 450px;
  }
}
.column span {
  font-weight: initial;
}
</style>
