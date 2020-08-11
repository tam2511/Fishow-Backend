<template lang="pug">
  .temperature-box.box
    h3.title Погодные условия
    p.content(v-html="readyData.temperature_brief")
    .columns.bg-white
      TempOneDay.column(v-for="day in readyData" :key="day.idc" :day="day")
    p.title.has-text-weight-light.is-4 Влажность, %
    .columns.bg-white(style="margin-bottom: 1rem")
      .column(v-for="day in readyData" :key="day.idc" :day="day")
        Humidity(:day="day")
    .columns
      .column
        Thermo
      .column.text-justify
        p.content(v-html="readyData.temperature_fish")
        p.content(v-html="readyData.temperature_desc")
    .columns.report
      .column.is-three-quarters
        p.content(v-html="readyData.phenomenon_warning")
      .column.report-icon
        b-icon(pack="fas"
          icon="exclamation-triangle"
          size="is-large"
          type="is-primary")

</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'

import readyData from '~/assets/mixins/prediction/readyData'
import Humidity from '~/components/predictPage/Results/Temperature/OneDay/humidity'
import Thermo from '~/components/predictPage/Results/Temperature/thermo'

export default {
  components: { Humidity, TempOneDay, Thermo },
  mixins: [readyData],
}
</script>

<style scoped lang="scss">
.columns.bg-white {
}
.text-justify {
  text-align: justify;
}
.report {
  background-color: #cbe8f791;
  text-align: justify;
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
  /*margin: 0 -1.3rem*/
  /*background-color: white;*/
  /*padding: 1rem;*/
}
</style>
