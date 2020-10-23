<template lang="pug">
  div
    .columns-container
      .columns.bg-white
        TempOneDay.column(v-for="day in readyDataStorage" :key="day.idc" :day="day")
      .columns.bg-white(style="margin-bottom: 1rem")
        .column(v-for="day in readyDataStorage" :key="day.idc" :day="day")
          Humidity(:day="day")
    .columns.temp-desc
      .column
        Thermo(
          v-if="readyDataStorage.temperature_desc.day"
          :day="readyDataStorage.temperature_desc.day"
          :night="readyDataStorage.temperature_desc.night"
          )
      .column.text-readyData
        p.content(v-html="readyDataStorage.temperature_fish")
        p.content(
          v-if="readyDataStorage.temperature_desc.desc",
          v-html="readyDataStorage.temperature_desc.desc"
          )
    report(:message="readyDataStorage.phenomenon_warning")
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'

import readyDataStorage from '~/assets/mixins/prediction/readyDataStorage'
import Humidity from '~/components/predictPage/Results/Temperature/OneDay/humidity'
import Thermo from '~/components/predictPage/Results/Temperature/thermo'
import Report from '~/components/predictPage/helpers/report'

export default {
  components: { Report, Humidity, TempOneDay, Thermo },
  mixins: [readyDataStorage],
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
  div.columns-container {
    display: flex;
    flex-flow: column;
    overflow: scroll;
  }
  div.columns {
    display: flex;
  }
  p.content {
    text-align: justify;
  }
  .temp-desc {
    flex-flow: column;
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
