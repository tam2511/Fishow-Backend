<template lang="pug">
  .pressure-box.box
    p.title Давление
    p.content {{ readyData[0].pressure_text }}
    .columns
    slot
</template>

<script>
export default {
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
}
</script>

<style scoped></style>
