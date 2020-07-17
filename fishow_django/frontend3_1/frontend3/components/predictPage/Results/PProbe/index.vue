<template>
  <div class="prediction-box box">
    <p class="title">Прогноз клева</p>
    <p class="content">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat.
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
