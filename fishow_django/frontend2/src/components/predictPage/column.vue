<template>
  <div>
    <div class="fishow_container">
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          Пн
          {{ index + 1}}
        </div>
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index"><one-colum/></div>
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element  fishow_row_temp" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
          Среднесуточная температура
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element  fishow_row_temp" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
        Прогноз аналогично температуре
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
        Ветер, м/с
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
        Давление, мм рт.ст.
      </div>

      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
        Относительная влажность, %
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index"> {{ index + 1}}</div>
      </div>
      <div class="fishow_row">
        Ультрафиолетовый индекс, баллы
      </div>
    </div>
  </div>
</template>

<script>
import OneColum from './oneColumn'
export default {
  name: 'colum',
  data() {
    return {}
  },
  components: { OneColum },
}
</script>

<style scoped lang="scss">
  .fishow_row {
    height: 50px;

    width: 100%;
    display: flex;
    flex-flow: row;
    justify-content: space-around;
    align-items: center;
    &_temp {
      background: linear-gradient(0deg, var(--blue) 55%, rgba(0,212,255,0) 56%);
    }
  }
  .fishow_row_element {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
</style>
