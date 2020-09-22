<template>
  <div class="miniPrediction card">
    <!--    {{ readyData }}-->
    <div v-if="readyData">
      <div class="media">
        <div class="media-left">
          {{ readyData.fish }}
        </div>
        <div class="media-right">
          <ul>
            <li>
              {{ readyData.areal }}
            </li>
            <li>
              {{ readyData.city }}
            </li>
            <li>
              {{ predictions.date }}
            </li>
          </ul>
        </div>
      </div>
      <div class="body">
        <div class="">Сред. температура воздуха: {{ temperature }}°C</div>
      </div>
      <div class="progressbar-footer">
        <div class="progressbar-main">
          <div
            class="progressbar-value"
            :style="'width:' + readyData[0].prob_max * 100 + '%'"
          >
            {{ readyData[0].prob_max * 100 }}%
          </div>
        </div>
        <div class="progressbar-values"></div>
      </div>
    </div>
    <div v-else class="if-lostdata">
      <SkeletonPrediction />
    </div>
    <nuxt-link to="/prognoz-kleva">
      <div class="placeholder">
        Посмотреть другие прогнозы
      </div>
    </nuxt-link>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { convertDataFromServer } from '@/assets/js/convertDataFromServer'
import SkeletonPrediction from '@/components/Sidebar/skeleton/SkeletonPrediction'
export default {
  components: {
    SkeletonPrediction,
  },
  computed: {
    readyData() {
      return convertDataFromServer(this.predictions)
    },
    rightDate() {
      const d = new Date()
      let month = '' + (d.getMonth() + 1)
      let day = '' + d.getDate()
      const year = d.getFullYear()

      if (month.length < 2) month = '0' + month
      if (day.length < 2) day = '0' + day

      return [year, month, day].join('-')
    },
    temperature() {
      return Math.floor(this.readyData[0].temperature_mean)
    },
    ...mapState('prediction', ['predictions']),
  },
  created() {
    const url = encodeURI(
      `/predictionten/?areal=Брянская область&date=${this.rightDate}&city=Брянск&fish=Щука`
    )
    // const url = encodeURI(
    //   '/predictionten/?areal=Московская область&date=2020-07-18&city=Москва&fish=Щука'
    // )
    this.getPrediction(url)
    // console.log('this.readyData = ', this.readyData)
  },
  methods: {
    ...mapActions('prediction', { getPrediction: 'getPrediction' }),
  },
}
</script>

<style lang="scss">
.miniPrediction {
  position: relative;
  .media-right {
    flex-grow: 1;
    text-align: right;
  }
  .media-left {
    text-transform: capitalize;
  }
  .media {
    padding: 1.25rem;
  }
  .footer {
    background: #363636;
    border-radius: 6px;
  }
  div.box {
    padding: 0;
    position: relative;
  }
  .body {
    padding: 0 1.25rem;
  }
  .progressbar-footer {
    padding: 1.25rem;
    border-radius: 6px;
  }
  .progressbar-main {
    background-color: #ababab;
    height: 44px;
  }
  .progressbar-value {
    width: 50%;
    height: 100%;
    background-color: #c8e5bc;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 0 10px;
  }
  .placeholder {
    opacity: 0;
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.3s;
    font-size: 20px;
  }
  .placeholder a {
    color: white;
  }
  .placeholder:hover {
    background-color: rgba(15, 21, 119, 0.73);
    color: white;
    opacity: 1;
    cursor: pointer;
  }
}
</style>
