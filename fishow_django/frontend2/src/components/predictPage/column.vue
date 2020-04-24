<template>
  <div>
    <div class="fishow_container">
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
          <chart
                  :optionsChart="{
                      type: 'bar',
                      probMin: data.temperature_min,
                      probMax: data.temperature_max,
                      max: 15,
                      min: 0
                  }"
          />
      </div>
      <div class="fishow_row">
        Среднесуточная температура
      </div>
      <div class="fishow_row">
          <chart
                  :optionsChart="{
                      type: 'bar',
                      probMin: data.prob_min,
                      probMax: data.prob_max,
                      max: 1,
                      min: 0
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
                      probMin: data.pressure_min,
                      probMax: data.pressure_max,
                      max: 740,
                      min: 650
                  }"/>

      </div>
      <div class="fishow_row">
        Давление, мм рт.ст.
      </div>
      <div class="fishow_row">
            <chart
                    :optionsChart="{
                      type: 'area',
                      probMin: data.wind_mean,
                      probMax: data.wind_mean,
                      max: 10,
                      min: 0
                  }"/>
      </div>
      <div class="fishow_row">
        Ветер, м/с
      </div>
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
  </div>
</template>

<script>
import OneColum from './oneColumn'
import IconPogoda from './IconPogoda'
import Temperatura from "./temperatura";
import Prob from "./prob";
import Chart from "./chart";
export default {
  name: 'colum',
  data() {
    return {
      data: {
        temperature_min: '[1,2,1,3,1,2,3,2,4]',
        temperature_mean: '[2,3,2,3,3,4,5,4,3]',
        temperature_max: '[4,5,4,5,5,4,6,7,8]',
        wind_mean: '[3,6,5,7,3,4,6,3,2]',
        wind_direction: '["СЗ","З","З","СЗ","С","В","Ю","ЮВ","В"]',
        gust_max: '[7,13,5,11,11,10,9,10,10]',
        phenomenon:
                '["[пасмурно]","[дождь,малооблачно]","[малооблачно]","[дождь,пасмурно]","[ясно]","[пасмурно]","[пасмурно]","[ясно]","[пасмурно]"]',
        pressure_min: '[733,734,733,735,735,733,738,735,733]',
        pressure_max: '[739,740,739,751,739,744,746,744,739]',
        humidity_mean: '[64,63,22,34,44,71,33,54,57]',
        uv_index_mean: '[3,3,3,3,5,4,3,2,1]',
        moon: '[1,4,7,14,21,28,33,40]',
        moon_direction: '[1,1,1,1,1,1,1,1,1]',
        date: '04.04.2020',
        areal: 'московскаяобласть',
        city: 'москва',
        fish: 'щука',
        prob_min: '[0.1,0.2,0.1,0.5,0.3,0.5,0.2,0.3,0.2]',
        prob_max: '[0.2,0.5,0.3,0.8,0.6,0.8,0.5,0.7,0.6]',
      },

    }
  },
  methods: {
    getPrediction() {

    }
  },
  created() {
    Object.keys(this.data).forEach((key) => {
      if (this.data[key][0] === '[') {
        this.data[key] = this.data[key]
                .slice(1, this.data[key].length - 1)
                .split(',')
      }
    })
    console.log(this.data.temperature_min)
    console.log(this.data.temperature_max)
    console.log(this.data)
  },

  components: {Chart, Prob, Temperatura, IconPogoda, OneColum },
}
</script>

<style scoped lang="scss">
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

</style>
