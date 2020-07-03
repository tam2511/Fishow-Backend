<template>
  <div class="prediction-box box">
    <p class="title">Прогноз клева</p>
    <div class="colums">
      <!--      <div v-for="day in readyData" :key="day.idc" class="column">-->
      <!--        <one-day-probe :day="day"></one-day-probe>-->
      <!--      </div>-->
    </div>
    <slot></slot>
  </div>
</template>
<script>
// import OneDayProbe from '~/components/predictPage/Results/PProbe/OneDay/oneDayProbe'
export default {
  // components: { OneDayProbe },
  props: {
    readyData: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped lang="scss"></style>
