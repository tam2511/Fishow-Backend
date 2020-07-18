<template>
  <div class="prediction-box box">
    <p class="title">Прогноз клева</p>
    <p class="content">
      {{ readyData[0].prediction_text }}
    </p>
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
