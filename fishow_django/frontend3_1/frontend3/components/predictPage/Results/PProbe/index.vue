<template>
  <div class="prediction-box box">
    <p class="title">Прогноз клева</p>
    <p class="content" v-html="readyData.prediction_brief"></p>
    <p class="content" v-html="readyData.prediction_desc"></p>
    <slot></slot>
  </div>
</template>
<script>
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  mixins: [readyData],
}
</script>

<style scoped lang="scss"></style>
