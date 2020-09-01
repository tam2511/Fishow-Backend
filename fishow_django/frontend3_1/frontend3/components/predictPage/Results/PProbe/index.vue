<template>
  <div class="prediction-box box">
    <p class="title">Прогноз клева</p>
    <p class="content" v-html="readyData.prediction_brief"></p>
    <div class="columns">
      <div class="column">
        <div class="columns minmax_columns">
          <div class="column">
            <div class="minmax_container">
              <span class="minmax" data-value="min">MIN</span>
              <p>{{ readyData.prediction_desc.min }}</p>
            </div>
            <p>{{ readyData.prediction_desc.min_date }}</p>
          </div>
          <div class="column">
            <div class="minmax_container">
              <span class="minmax" data-value="max">MAX</span>
              <p>{{ readyData.prediction_desc.max }}</p>
            </div>
            <p>{{ readyData.prediction_desc.max_date }}</p>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="legend">
          <span class="legend_max"
            >Максимальная суточная вероятность клёва</span
          >
          <span class="legend_min">Минимальная суточная вероятность клёва</span>
          <span class="legend_area">Высокий шанс клева рыбы</span>
        </div>
      </div>
    </div>
    <!--    <p class="content" v-html="readyData.prediction_desc"></p>-->
    <slot></slot>
  </div>
</template>
<script>
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  mixins: [readyData],
}
</script>

<style scoped lang="scss">
.minmax_container {
  display: flex;
  font-size: 4vh;
  align-items: center;
  white-space: nowrap;
  p {
    padding: 0 1rem;
  }
}
[data-value='min'] {
  color: #64888a;
}
[data-value='max'] {
  color: #77866c;
}
%legend-flag {
  content: '';
  height: 10px;
  width: 10px;
  display: block;
  position: absolute;
  left: -15px;
  top: 7px;
}
.legend {
  display: flex;
  flex-flow: column;
  align-items: flex-end;

  color: rgba(128, 128, 128, 0.8);
  span {
    position: relative;
  }
  &_area {
    color: #1a5105;
    &:after {
      @extend %legend-flag;
      background-color: #1a5105;
    }
  }
  &_min {
    color: #172a3b;
    &:after {
      @extend %legend-flag;
      background-color: #172a3b;
    }
  }
  &_max {
    color: #51686a;
    &:after {
      @extend %legend-flag;
      background-color: #b0e4e8;
    }
  }

  @media screen and (max-width: 450px) {
    font-size: 10px;
  }
}
</style>
