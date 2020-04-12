<template>
  <el-col :span="6">
    <div class="grid-content">
      <h4>Ночь</h4>
      <span>{{ randomDpogoda }}</span>
      <h4>Температура воздуха:</h4>
      <span>{{ getRandom25 }} &#8451;</span>
      <h4>температура воды:</h4>
      <span>{{ getRandom15 }} &#8451;</span>
      <h4>поверхность</h4>
      <span>{{ getRandom10 }} &#8451;</span>
      <h4>глубина</h4>
      <span>{{ getRandom8 }} &#8451;</span>
      <h4>ветер</h4>
      <span>западно-юго-западный, 5м/с</span>
      <h4>влажность</h4>
      <span>64%</span>
      <h4>давление</h4>
      <span> 760 мм рт.ст.</span>
      <h4>восход солнца</h4>
    </div>
  </el-col>
</template>

<script>
export default {
  name: 'oneColum',
  data() {
    return {
      value: '',
      pogoda: ['Ясно', 'Пасурно', 'Облачно', 'Гроза'],
    }
  },
  computed: {
    randomDpogoda() {
      let value = Math.floor(Math.random() * Math.floor(3))
      return this.pogoda[value]
    },
    getRandom25() {
      return Math.floor(Math.random() * Math.floor(25))
    },
    getRandom15() {
      return Math.floor(Math.random() * Math.floor(25))
    },
    getRandom10() {
      return Math.floor(Math.random() * Math.floor(25))
    },
    getRandom8() {
      return Math.floor(Math.random() * Math.floor(25))
    },
  },
}
</script>

<style lang="scss">
.grid-content {
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  span {
    width: 100%;
    /*background-color: rgba(53, 121, 185, 0.28);*/
    font-size: 20px;
    padding: 5px 0;
    /*color: rgba(60, 60, 60, 0.87);*/
  }
  h4 {
    /*color: #fff;*/
    width: 100%;
    /*background-color: rgba(24, 99, 107, 0.61);*/
  }
}
.el-col {
  /*border-right: 3px solid rgba(24, 99, 107, 0.61);*/
}
</style>
