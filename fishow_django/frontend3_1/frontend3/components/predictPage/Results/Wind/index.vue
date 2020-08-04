<template lang="pug">
  .wind-box.box
    p.title Ветер, м/с
    p.content(v-html="readyData.wind_fish")
    p.content(v-html="readyData.wind_desc")
    .columns
      WindOneDay.column(v-for="(day, index) in readyData" :key="day.date + index" :day="day")
    p.title.has-text-weight-light Порывы, м/с
    .columns
      WindOneDay.column.gust-column(v-for="(day,index) in readyData" :key="day.date + index" :day="day" :gustOnly="true")
    slot
</template>

<script>
import WindOneDay from '@/components/predictPage/Results/Wind/OneDay/index'
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  components: { WindOneDay },
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
}
.wind-box {
  background: radial-gradient(
    circle,
    rgb(239, 242, 255) 0%,
    rgb(202, 199, 200) 100%
  );
}
div.columns {
  background-color: white;
  margin: 0 -1.3rem;
  margin-bottom: 1.5rem;
}
</style>
