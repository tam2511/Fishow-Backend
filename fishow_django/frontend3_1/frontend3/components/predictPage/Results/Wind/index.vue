<template lang="pug">
  .wind-box.box
    p.title Ветер, м/с
    p.content {{ text }}
    .columns
      WindOneDay.column(v-for="(day, index) in readyData" :key="day.id + index" :day="day")
    p.title.has-text-weight-light Порывы, м/с
    .columns
      WindOneDay.column.gust-column(v-for="(day,index) in readyData" :key="day.id + index" :day="day" :gustOnly="true")
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
      text: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.`,
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
@media screen and (max-width: 768px) {
  div.column {
    display: inline-block;
    padding: 0;
    border-right: 6px solid #fff;
  }
  div.columns {
    margin: 0 auto;
    display: inline-flex;
    width: 100%;
    overflow: scroll;
  }
  .gust-column {
    padding: 0;
  }
}
</style>
