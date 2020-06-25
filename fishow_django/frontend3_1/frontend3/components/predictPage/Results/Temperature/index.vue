<template lang="pug">
    .temperature-box.box
      p.title Температура
      .columns
        .column(v-for="day in days" :key="day.id")
          TempOneDay(:day="day")
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'
export default {
  components: { TempOneDay },
  props: {
    days: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      niceDays: null,
    }
  },
  methods: {
    // convertDays() {
    //   const whatMonth = {
    //     '01': 'Января',
    //     '02': 'Февраля',
    //     '03': 'Марта',
    //     '04': 'Апреля',
    //     '05': 'Мая',
    //     '06': 'Июня',
    //     '07': 'Июля',
    //     '08': 'Августа',
    //     '09': 'Сентября',
    //     '10': 'Октября',
    //     '11': 'Ноября',
    //     '12': 'Декабря',
    //   }
    //   const days = this.days
    //   const result = []
    //   days.forEach((item) => {
    //     const arrayFromItem = item.split('/')
    //     result.push(arrayFromItem[0] + ' ' + whatMonth[arrayFromItem[1]])
    //   })
    //   this.niceDays = result
    // },
  },
}
</script>

<style scoped lang="scss">
.date {
  padding-bottom: 20px;
}
.temperature-list {
  display: flex;
  justify-content: space-around;
  &__start {
    align-items: flex-start;
  }
  &__end {
    align-items: flex-end;
  }
  &__p_t {
    padding-top: 70px;
  }
  &__p_b {
    padding-bottom: 10px;
  }
}
.phenomenon {
  position: relative;
}
.temperature-max_item {
  background-color: #fee187;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    top: -30px;
    left: 0;
    text-align: center;
    color: #000;
    font-size: 20px;
  }
}
.temperature-min_item {
  background-color: #7957d582;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    bottom: -30px;
    left: 0;
    text-align: center;
    color: #4e4e4e;
    font-size: 20px;
  }
}
.value {
  position: absolute;
  color: #000;
  bottom: -50px;
  left: -25px;
  width: 50px;
}
.date_item {
  font-weight: 300;
  font-size: 15px;
}
</style>
