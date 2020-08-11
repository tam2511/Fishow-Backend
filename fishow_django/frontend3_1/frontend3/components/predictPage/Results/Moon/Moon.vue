<template lang="pug">
  .moon-box.box
    h3.title Луна
    p.content(v-html="readyData.moon_desc")
    .columns
      MoonOne.column(v-for="(day, index) in readyData" :key="day.date + index" :day="day")
</template>

<script>
import readyData from '~/assets/mixins/prediction/readyData'
import MoonOne from '~/components/predictPage/Results/Moon/OneDay/MoonOne'
export default {
  components: {
    MoonOne,
  },
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
.moon-box {
  background: rgba(0, 0, 0, 0.89) !important;
  color: #fff;

  padding-bottom: 50px;
}
.title {
  color: #fff;
}
@media screen and (max-width: 768px) {
  div.columns {
    display: flex;
    overflow: scroll;
    min-height: 200px;
  }
}
div.column {
  display: flex;
  align-items: center;
  flex-flow: column;
}
</style>
