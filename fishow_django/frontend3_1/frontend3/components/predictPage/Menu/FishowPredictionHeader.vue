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
                  date: $route.params.date,
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
          Наслаждайтесь спланированной рыбалкой в {{ $route.params.city }} и
          отличным клевом
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      niceDays: null,
    }
  },
  computed: {
    day() {
      return this.niceDays[0] === '0'
        ? this.niceDays.split('0')[1]
        : this.niceDays
    },
  },
  created() {
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
      const result = whatMonth[day[1]]
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
