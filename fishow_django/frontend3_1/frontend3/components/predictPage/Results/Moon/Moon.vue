<template lang="pug">
  .moon-box.box
    p.title Луна
    p.content {{ readyData[0].moon_text }}
    .columns
      MoonOne.column(v-for="(day, index) in readyData" :key="day.id + index" :day="day")
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

<style scoped></style>
