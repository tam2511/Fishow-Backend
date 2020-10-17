<template lang="pug">
  div
    .columns
      WindOneDay.column(
        v-for="(day, index) in readyDataStorage",
        :key="day.date + index",
        :day="day",
        )
    h2.title Порывы, м/с
    .columns
      WindOneDay.column.gust-column(
        v-for="(day,index) in readyDataStorage",
        :key="day.date + index",
        :day="day",
        :gustOnly="true"
        )
    .columns.roza-columns
      .column
        p.content(v-html="readyDataStorage.wind_fish")
      .column.roza
        roza(:windRoza="readyDataStorage.wind_roza")
    slot
</template>

<script>
import WindOneDay from '@/components/predictPage/Results/Wind/OneDay/index'
import readyDataStorage from '~/assets/mixins/prediction/readyDataStorage'
import Roza from '~/components/predictPage/Results/Wind/roza'

export default {
  components: { Roza, WindOneDay },
  mixins: [readyDataStorage],
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 768px) {
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
