<template lang="pug">
    .temperature-box.box
      p.title Погодные условия
      p.content(v-html="readyData.temperature_brief")
      .columns
        TempOneDay.column(v-for="day in readyData" :key="day.idc" :day="day")
      p.title.has-text-weight-light.is-4 Влажность, %
      .columns(style="margin-bottom: 1rem")
        .column(v-for="day in readyData" :key="day.idc" :day="day")
          Humidity(:day="day")

      p.content(v-html="readyData.temperature_fish")
      p.content(v-html="readyData.temperature_desc")
      p.content(v-html="readyData.phenomenon_warning")
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'
import readyData from '~/assets/mixins/prediction/readyData'
import Humidity from '~/components/predictPage/Results/Temperature/OneDay/humidity'

export default {
  components: { Humidity, TempOneDay },
  mixins: [readyData],
}
</script>

<style scoped lang="scss">
.temperature-box {
  background-color: #5292e30d;
}
.columns {
  background-color: white;
  margin: 0 -1.3rem;
}
.title {
  margin-top: 1.5rem;
}
@media screen and (max-width: 768px) {
  div.columns {
    display: flex;
    overflow: scroll;
  }
  p.content {
    text-align: justify;
  }
}
.temperature-box {
}
.title.has-text-weight-light {
  margin: 0 -1.3rem;
  background-color: white;
  padding: 1rem;
}
</style>
