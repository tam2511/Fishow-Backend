<template lang="pug">
  .fish-select-body
    button(v-if="first - 10 > 0" @click="first -= 10") <<
    .fish-container
      nuxt-link.fish-container-item(v-for="fish in list" :key="fish" :to="{ name: 'PredictionPage-areal-date-city-fish', params: { areal, date, city, fish}}")
        .fish-container-item_value {{ fish }}
    button(v-if="first <= fishList.length" @click="first += 10") >>

</template>
js

<script>
export default {
  props: {
    areal: {
      type: String,
      required: true,
    },
    city: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      fishList: [
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
      first: 10,
    }
  },
  computed: {
    list() {
      return this.fishList.filter(
        (fish, index) => index > this.first - 9 && index < this.first
      )
    },
  },
}
</script>

<style scoped lang="scss">
.fish-select-body {
  display: flex;
  flex-flow: row;
  max-width: 640px;
  margin: auto;
}
.fish-container {
  min-height: 250px;
  display: flex;
  padding: 0 50px;
  flex-wrap: wrap;
  &-item {
    width: 80px;
    height: 80px;
    cursor: pointer;
    transition: 0.3s;
    margin: 20px;
    border-radius: 25px;
    position: relative;
    background-color: rgba(0, 0, 0, 0.3);
    &_value {
      position: absolute;
      transform: translate(-50%, -50%);
      left: 50%;
      top: 50%;
      margin: 0;
      text-align: center;
    }
    &:hover {
      color: #ffffff;
      background-color: cadetblue;
    }
  }
}
</style>
