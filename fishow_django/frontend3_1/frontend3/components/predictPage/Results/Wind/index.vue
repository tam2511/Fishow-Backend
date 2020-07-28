<template lang="pug">
  .wind-box.box
    p.title Ветер, м/с
    p.content {{ readyData.wind_text }}
    .columns
      WindOneDay.column(v-for="(day, index) in readyData" :key="day.date + index" :day="day")
    p.title.has-text-weight-light Порывы, м/с
    .columns
      WindOneDay.column.gust-column(v-for="(day,index) in readyData" :key="day.date + index" :day="day" :gustOnly="true")
    slot
</template>

<script>
import WindOneDay from '@/components/predictPage/Results/Wind/OneDay/index'
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  components: { WindOneDay },
  mixins: [readyData],
  props: {
    days: {
      type: Array,
      required: true,
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
