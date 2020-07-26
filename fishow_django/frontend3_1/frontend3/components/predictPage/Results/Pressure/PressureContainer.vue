<template lang="pug">
  .pressure-box.box
    p.title Давление
    p.content {{ readyData.pressure_text }}
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
