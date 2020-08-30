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
      .column
        p(v-html="readyData.pressure_desc.min_date")
        p(v-html="readyData.pressure_desc.min")
        span мм рт.ст.
      .column
        p(v-html="readyData.pressure_desc.max_date")
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

<style scoped></style>
