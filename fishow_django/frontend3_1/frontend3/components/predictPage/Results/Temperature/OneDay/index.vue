<template>
  <div>
    <p>{{ day.temperature_mean }}</p>
  </div>
</template>

<script>
export default {
  props: {
    day: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped></style>
