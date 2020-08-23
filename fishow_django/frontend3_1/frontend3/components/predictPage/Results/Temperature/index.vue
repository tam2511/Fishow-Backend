<template lang="pug">
  .temperature-box.box
    h3.title Погодные условия
    p.content(v-html="readyData.temperature_brief")
    .columns.bg-white
      TempOneDay.column(v-for="day in readyData" :key="day.idc" :day="day")
    .columns.bg-white(style="margin-bottom: 1rem")
      .column(v-for="day in readyData" :key="day.idc" :day="day")
        Humidity(:day="day")
    .columns
      .column
        Thermo(:day="readyData.temperature_desc.day" :night="readyData.temperature_desc.night")
      .column.text-justify
        p.content(v-html="readyData.temperature_fish")
        p.content(v-html="readyData.temperature_desc.desc")
    report(:message="readyData.phenomenon_warning")
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'

import readyData from '~/assets/mixins/prediction/readyData'
import Humidity from '~/components/predictPage/Results/Temperature/OneDay/humidity'
import Thermo from '~/components/predictPage/Results/Temperature/thermo'
import Report from '~/components/predictPage/helpers/report'

export default {
  components: { Report, Humidity, TempOneDay, Thermo },
  mixins: [readyData],
}
</script>

<style scoped lang="scss">
.columns.bg-white {
}
.text-justify {
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
