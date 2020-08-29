<template lang="pug">
  .wind-box.box
    p.title Ветер, м/с
    p.content(v-html="readyData.wind_desc")
    .columns
      WindOneDay.column(v-for="(day, index) in readyData" :key="day.date + index" :day="day")
    p.title.has-text-weight-light Порывы, м/с
    .columns
      WindOneDay.column.gust-column(v-for="(day,index) in readyData" :key="day.date + index" :day="day" :gustOnly="true")
    .columns.roza-columns
      .column
        p.content(v-html="readyData.wind_fish")
      .column.roza
        roza(:windRoza="readyData.wind_roza")
    slot
</template>

<script>
import WindOneDay from '@/components/predictPage/Results/Wind/OneDay/index'
import readyData from '~/assets/mixins/prediction/readyData'
import Roza from '~/components/predictPage/Results/Wind/roza'

export default {
  components: { Roza, WindOneDay },
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
  .roza-columns {
    flex-flow: column;
  }
  .roza {
    min-width: 300px;
  }
}
</style>
