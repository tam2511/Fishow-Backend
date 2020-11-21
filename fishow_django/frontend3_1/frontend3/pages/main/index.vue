<template>
  <section>
    <div class="container">
      <div class="head-banner">
        <div class="banner-body">
          <div class="banner_title-wrapper">
            <h1 class="banner_title">
              Вместе мы улучшаем качество прогноза клева
            </h1>
            <h3 class="banner_title">
              Ваши отчеты помогают спрогнозировать результаты рыбалки
            </h3>
            <button>Оставить отчет</button>
          </div>
          <div class="banner_picture">
            <img src="/5ccef214ee61b_o_rybalke.png" width="400px" alt="" />
          </div>
        </div>
        <div class="banner-statistic">
          <div class="banner-statistic__item">
            <div class="banner-statistic__title">Точность прогноза</div>
            <div class="banner-statistic__value">75%</div>
          </div>
          <div class="banner-statistic__item">
            <div class="banner-statistic__title">Статей и блогов</div>
            <div class="banner-statistic__value">26 641</div>
          </div>
          <div class="banner-statistic__item">
            <div class="banner-statistic__title">Количество прогнозов</div>
            <div class="banner-statistic__value">{{ predictions_counter }}</div>
          </div>
          <div class="banner-statistic__item">
            <div class="banner-statistic__title">Точность прогноза</div>
            <div class="banner-statistic__value">75%</div>
          </div>
        </div>
      </div>
      <div class="prediction-section">
        <div class="prediction-title">
          <h2 class="title">Прогноз клева</h2>
        </div>
        <div v-if="readyData" class="prediction-chart">
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
          <b-field label="Выберите место рыбалки">
            <CitySearch />
          </b-field>
          <b-field label="Выберите рыбу">
            <fish-select-prediction :passive="true" />
          </b-field>
          <button>Составить прогноз</button>
          <span>Подробнее > </span>
        </div>
      </div>
      <div class="actions-grid">
        <div class="actions-grid__item">
          <div class="grid__item_title">Создать свою статью</div>
          <div class="grid__item_body">
            Опишите свои впечатления о рыбалке и поделитесь опытом!
          </div>
        </div>
        <div class="actions-grid__item">
          <div class="grid__item_title">Отчеты о рыбалке</div>
          <div class="grid__item_body">
            Опишите свои впечатления о рыбалке и поделитесь опытом!
          </div>
        </div>
        <div class="actions-grid__item">
          <div class="grid__item_title">Статьи и блоги других авторов</div>
          <div class="grid__item_body">
            Читайте интересные истории товарищей по рыбалке
          </div>
        </div>
        <div class="actions-grid__item">
          <div class="grid__item_title">База знаний рыбалова</div>
          <div class="grid__item_body">
            Крупнейшее вики рыбаловного сообщества
          </div>
        </div>
      </div>
      <div class="site-news">
        <div class="site-news__title">
          <h2 class="title">Новости</h2>
        </div>
        <div class="site-news__container">
          <div class="site-news__item-container">
            <div class="site-news__header">30 октября 2020</div>
            <div class="site-news__body">
              Рыбхоз “Двенди” выпустл на волю 300 кг форели
            </div>
          </div>
          <div class="site-news__item-container">
            <div class="site-news__header">30 октября 2020</div>
            <div class="site-news__body">
              Открыт новый Рыбхоз “Рыбные пальчики”
            </div>
          </div>
          <div class="site-news__item-container">
            <div class="site-news__header">29 октября 2020</div>
            <div class="site-news__body">
              Компания “Шимана” выпустила новую линейку спинингов
            </div>
          </div>
        </div>
        <div class="site-news__footer">
          <a href="#">Все новости ></a>
        </div>
      </div>
      <div class="activity-rating">
        <div class="activity-container">
          <div class="activity-title"></div>
          <div class="activity-description"></div>
          <div class="activity-select"></div>
          <div class="activity-chart"></div>
        </div>
        <div class="rating-container">
          <div class="activity-title"></div>
          <div class="activity-description"></div>
          <div class="activity-select"></div>
          <div class="activity-chart"></div>
        </div>
      </div>
    </div>
  </section>
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
      predictions_counter: 26610,
    }
  },
  computed: {
    readyData() {
      const data = convertDataFromServer(this.predictions)
      this.setReady(data)
      this.setDays(this.days)
      return data
    },
    ...mapState('prediction', ['predictions']),
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
    const getRandomTimerTime = () => {
      return Math.floor(Math.random() * Math.floor(3000))
    }
    const timer = () => {
      this.predictions_counter += Math.floor(Math.random() * Math.floor(20))
      setTimeout(timer, getRandomTimerTime())
    }

    timer()
    console.log('this.predictions = ', this.predictions)
  },
  methods: {
    ...mapActions('prediction', {
      getPrediction: 'getPrediction',
      setReady: 'setReady',
      setDays: 'setDays',
    }),
  },
}
</script>

<style lang="scss">
.section {
  background-color: #fff;
}
.site-news {
  display: flex;
  flex-flow: column;
  margin: 40px 0;
  &__container {
    display: flex;
    flex-flow: row wrap;
  }
  &__item-container {
    margin: 20px 0;
    width: 33%;
    padding: 10px 10px 0 0;
  }
  &__header {
    color: #878b90;
  }
  &__footer {
    padding: 10px 0;
  }
  @media screen and (max-width: 768px) {
    &__item-container {
      width: 100%;
    }
    margin: 40px 10px;
  }
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
.actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 15px;
  row-gap: 15px;
  @media screen and (max-width: 768px) {
    grid-template-columns: 1fr;
  }
  &__item {
    min-height: 220px;
    background-image: url('/Rectangle.png');
    background-position: right;
    background-repeat: no-repeat;
    background-size: cover;
    padding: 20px;

    border: 1px solid rgba(206, 209, 213, 0.4);
    box-sizing: border-box;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
  }
}
.grid__item_title {
  font-size: 19px;
  line-height: 32px;
  width: 50%;
}
.grid__item_body {
  text-align: left;
  width: 70%;
}
.head-banner,
.banner-body {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  align-items: center;
}
.banner-body {
  width: 100%;
}
.banner_title {
  font-family: Open Sans, fantasy;
  font-style: normal;
  font-weight: normal;

  &-wrapper {
    width: 50%;
    max-height: 500px;
    & > * {
      margin: 10px 0;
    }
    button {
      background: #018cac;
      border: 2px solid #018cac;
      box-sizing: border-box;
      border-radius: 4px;
      padding: 10px 30px;
      font-size: 16px;
      line-height: 26px;
      color: #fff;
      text-align: center;
      margin-top: 50px;
    }
  }
  @media screen and (max-width: 768px) {
    &-wrapper {
      width: 100%;
      margin: 0 10px;
    }
  }
}
h1.banner_title {
  font-size: 36px;
  line-height: 48px;
}
h3.banner_title {
  font-size: 20px;
  line-height: 32px;
}

.banner-statistic {
  width: 100%;
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  margin: 40px 0;
  &__title {
  }
  &__value {
    font-size: 46px;
    line-height: 62px;
  }
  &__item {
    margin: 0 10px;
  }
}
</style>
