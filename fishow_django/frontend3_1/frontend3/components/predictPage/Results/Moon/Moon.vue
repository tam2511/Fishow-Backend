<template lang="pug">
  .moon-box.box
    h3.title Луна
    .columns.moons
      MoonOne.column(v-for="(day, index) in readyData" :key="day.date + index" :day="day")
    .columns.moon-columns
      .column.moon-pic
        figure.image
          img(src="/image 92.png" alt="a random image" ratio="6by4")
      .column.moon_desc
        p(v-html="readyData.moon_desc.bad")
        p(v-html="readyData.moon_desc.neutral")
        p(v-html="readyData.moon_desc.good")
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
  /*background: rgba(0, 0, 0, 0.89) !important;*/
  /*color: #fff;*/

  padding-bottom: 50px;
}
.moons {
  padding-bottom: 50px;
}
.title {
  /*color: #fff;*/
}
@media screen and (max-width: 768px) {
  div.columns {
    display: flex;
    overflow: scroll;
    min-height: 200px;
  }
  .moon-columns {
    flex-flow: column;
  }
  .moon-pic {
    min-width: 300px;
  }
}
div.column {
  display: flex;
  align-items: center;
  flex-flow: column;
}
.moon_desc {
  justify-content: center;
}
</style>
