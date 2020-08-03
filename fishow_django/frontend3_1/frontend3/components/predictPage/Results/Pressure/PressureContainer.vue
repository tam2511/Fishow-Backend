<template lang="pug">
  .pressure-box.box
    p.title Давление
    p.content(v-html="readyData.pressure_fish")
    p.content(v-html="readyData.pressure_desc")
    .columns
    slot
</template>

<script>
import readyData from '~/assets/mixins/prediction/readyData'

export default {
  mixins: [readyData],
}
</script>

<style scoped></style>
