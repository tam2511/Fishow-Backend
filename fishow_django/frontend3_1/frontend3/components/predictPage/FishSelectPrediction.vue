<template lang="pug">
  .fishow-prediction_fish-select
    div.fishow-prediction_fish-select-item(v-for="fish in fishs" :key="fish") {{ fish }}
</template>

<script>
export default {
  data() {
    return {
      fishs: [
        'щука',
        'судак',
        'окунь',
        'берш',
        'речная форель',
        'озерная форель',
        'елец',
        'чехонь',
        'сом',
        'голавль',
        'язь',
        'карп',
        'жерех',
        'лещ',
        'карась',
        'линь',
        'пескарь',
        'ротан',
        'плотва',
        'красноперка',
        'налим',
        'густера',
        'амур',
        'ерш',
        'сазан',
        'подуст',
        'толстолобик',
        'вобла',
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.fishow-prediction_fish-select {
  border: 3px solid #00b3ee;
  min-height: 250px;
  display: flex;
  flex-wrap: wrap;
  &-item {
    padding: 20px;
    cursor: pointer;
    transition: 0.3s;
    background: url('/static/fish.svg') center;
    &:hover {
      color: #ffffff;
      background-color: cadetblue;
    }
  }
}
</style>
