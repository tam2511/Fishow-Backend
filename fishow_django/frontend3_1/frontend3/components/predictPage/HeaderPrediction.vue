<template lang="pug">
  .fishow-prediction_description
    .fishow-prediction_name
      .fishow-prediction_name-heading Прогноз на 9 дней
      .fishow-prediction_name-sub Наслаждайтесь максимально хорошо спланированной рыбалкой экспедиции в Бунтаус
    .fishow-prediction_nav
      .fishow-prediction_nav-item
        .fishow-prediction_nav-text Вероятность клева
      .fishow-prediction_nav-item
        .fishow-prediction_nav-text Погодные условия
      .fishow-prediction_nav-item
        .fishow-prediction_nav-text Влажность
      .fishow-prediction_nav-item
        .fishow-prediction_nav-text Луна
</template>

<script></script>

<style scoped lang="scss">
.fishow-prediction_description {
  padding: 10px;
  min-height: 200px;
  background: url('/assets/beach-blue-bouy.jpg');
  color: white;
  display: flex;
  flex-flow: row;
  align-items: center;
}
.fishow-prediction_nav {
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
  &-item {
    width: 100px;
    height: 100px;
    border: 2px solid #000000;
    position: relative;
    background-color: rgba(13, 10, 10, 0.8);
    transition: 0.3s;
    &:hover {
      background-color: rgba(13, 10, 10, 0.6);
    }
  }
  &-text {
    position: absolute;
    transform: translate(-50%, -50%);
    margin: 0;
    left: 50%;
    top: 50%;
    text-align: center;
  }
}
</style>
