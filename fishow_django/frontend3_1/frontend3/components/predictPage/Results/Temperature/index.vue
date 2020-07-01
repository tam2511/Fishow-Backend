<template lang="pug">
    .temperature-box.box
      p.title Температура
      .columns
        .column(v-for="day in readyData" :key="day.idc")
          TempOneDay(:day="day")
      slot
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'
// import getCalendarDay from '~/assets/js/getCalendarDay'
export default {
  components: { TempOneDay },
  props: {
    readyData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      niceDays: null,
    }
  },
  computed: {},
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
