<template lang="pug">
    .temperature-box.box
      p.title Погодные условия
      p.content(v-html="readyData.temperature_brief")
      .columns
        TempOneDay.column(v-for="day in readyData" :key="day.idc" :day="day")
      slot
      p.content(v-html="readyData.temperature_fish")
      p.content(v-html="readyData.temperature_desc")

      p.content(v-html="readyData.phenomenon_warning")
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  components: { TempOneDay },
  mixins: [readyData],
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 768px) {
  div.column {
    display: inline-block;
  }
}
</style>
