<template lang="pug">
  .wind-box.box
    p.title Ветер
    .columns
      .column(v-for="day in readyData" :key="day.id")
        WindOneDay(:day="day" )
    slot
</template>

<script>
import WindOneDay from '@/components/predictPage/Results/Wind/OneDay/index'
import getCalendarDay from '~/assets/js/getCalendarDay'

export default {
  components: { WindOneDay },
  props: {
    readyData: {
      type: Array,
      required: true,
    },
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
  computed: {
    calendarDay() {
      return getCalendarDay(this.days)
    },
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
    top: -25px;
    left: 10px;
    color: #000;
  }
}
.temperature-min_item {
  background-color: #7957d582;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    bottom: -25px;
    left: 10px;
    color: #000;
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
  font-weight: 700;
  font-size: 20px;
}
</style>
