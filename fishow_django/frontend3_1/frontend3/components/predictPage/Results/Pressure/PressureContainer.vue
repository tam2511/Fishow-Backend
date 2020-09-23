<template lang="pug">
  .pressure-box.box
    p.title Давление
    p.content(v-html="readyData.pressure_fish")
    slot
    .columns
      .column.container-minmax
        b-icon(
          pack="fas"
          icon="chevron-up"
          size="is-large"
          type="is-primary"
        )
        p(v-html="readyData.pressure_desc.up_text" class="right-box")
      .column.container-minmax
        b-icon(
          pack="fas"
          icon="chevron-down"
          size="is-large"
          type="is-primary"
        )
        p(v-html="readyData.pressure_desc.low_text" class="right-box")
      .column.container-minmax
        div
          div(data-value="min") MIN
          p(v-html="readyData.pressure_desc.min_date")
        div.right-box
          p(v-html="readyData.pressure_desc.min" data-value)
          span мм рт.ст.
      .column.container-minmax
        div
          div(data-value="max") MAX
          p(v-html="readyData.pressure_desc.max_date")
        div.right-box
          p(v-html="readyData.pressure_desc.max" data-value)
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

<style scoped lang="scss">
.container-minmax {
  display: flex;
  justify-content: center;
  align-items: center;
}
.content {
  font-size: 18px;
}
.right-box {
  padding: 0 1rem;
}
[data-value] {
  font-size: 3rem;
}
[data-value='min'] {
  color: #64888a;
}
[data-value='max'] {
  color: #77866c;
}
.columns {
  flex-wrap: wrap;
}
</style>
