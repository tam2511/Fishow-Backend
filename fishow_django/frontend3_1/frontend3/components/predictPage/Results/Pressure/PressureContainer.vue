<template lang="pug">
  .pressure-box.box
    p.title Давление
    p.content(v-html="readyData.pressure_fish")
    slot
    .columns
      .column
        p(v-html="readyData.pressure_desc.up_text")
      .column
        p(v-html="readyData.pressure_desc.low_text")
      .column.container-minmax
        div
          div(data-value="min") MIN
          p(v-html="readyData.pressure_desc.min_date")
        div
          p(v-html="readyData.pressure_desc.min")
          span мм рт.ст.
      .column.container-minmax
        div
          div(data-value="max") MAX
          p(v-html="readyData.pressure_desc.max_date")
        div
          p(v-html="readyData.pressure_desc.max")
          span мм рт.ст.


    report(:message="message")
</template>

<script>
import readyData from '~/assets/mixins/prediction/readyData'
import Report from '~/components/predictPage/helpers/report'

export default {
  components: {
    Report,
  },
  mixins: [readyData],
  data() {
    return {
      message:
        'На данный момент недостаточно изучено, как именно влияет изменения атмосферного давления на клев окуня. Вы можете оставить отчет о рыбалке и помочь выявить закономерности нашему алгоритму.',
    }
  },
}
</script>

<style scoped>
.container-minmax {
  display: flex;
}
[data-value] {
  font-size: 4vh;
}
[data-value='min'] {
  color: #64888a;
}
[data-value='max'] {
  color: #77866c;
}
</style>
