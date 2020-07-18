<template lang="pug">
    .temperature-box.box
      p.title Погодные условия
      p.content {{ readyData[0].temperature_text }}
      .columns
        TempOneDay.column(v-for="day in readyData" :key="day.idc" :day="day")
      slot
</template>

<script>
import TempOneDay from '@/components/predictPage/Results/Temperature/OneDay/index'
// import getCalendarDay from '~/assets/js/getCalendarDay'
export default {
  components: { TempOneDay },
  props: {
    readyData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      text: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.`,
    }
  },
  computed: {},
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 768px) {
  div.column {
    display: inline-block;
  }
}
</style>
