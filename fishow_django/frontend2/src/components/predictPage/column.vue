<template>
  <div>
    <div class="fishow_container">
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          Пн
          {{ index + 1 }}
        </div>
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <one-colum />
        </div>
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="20"
            :minValue="12"
            color="--red"
            :height="4"
            :margin-text="0.99"
          />
        </div>
      </div>
      <div class="fishow_row">
        Среднесуточная температура
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="15"
            :minValue="10"
            color="--orange"
            :height="5"
            :margin-text="1"
          />
        </div>
      </div>
      <div class="fishow_row">
        Прогноз аналогично температуре
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="15"
            :minValue="10"
            color="--yellow"
            :height="5"
            :margin-text="1"
          />
        </div>
      </div>
      <div class="fishow_row">
        Ветер, м/с
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="700"
            :minValue="650"
            color="--green"
            :height="0.08"
            :margin-text="30"
          />
        </div>
      </div>
      <div class="fishow_row">
        Давление, мм рт.ст.
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="90"
            :minValue="80"
            color="--teal"
            :height="1.5"
            :margin-text="3"
          />
        </div>
      </div>
      <div class="fishow_row">
        Относительная влажность, %
      </div>
      <div class="fishow_row">
        <div class="fishow_row_element" v-for="(n, index) in 9" :key="index">
          <icon-pogoda
            :maxValue="5"
            :minValue="3"
            color="--cyan"
            :height="10"
            :margin-text="0.5"
          />
        </div>
      </div>
      <div class="fishow_row">
        Ультрафиолетовый индекс, баллы
      </div>
    </div>
  </div>
</template>

<script>
import OneColum from './oneColumn'
import IconPogoda from './IconPogoda'
export default {
  name: 'colum',
  data() {
    return {}
  },

  components: { IconPogoda, OneColum },
}
</script>

<style scoped lang="scss">
.fishow_row {
  margin-top: 10px;
  color: var(--color-typo-primary);
  height: 50px;
  width: 100%;
  display: flex;
  font-size: 20px;
  flex-flow: row;
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
