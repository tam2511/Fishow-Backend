<template>
  <div>
    <ul>
      <li>{{ currentDate }}</li>
      <li>{{ currentPhe }}</li>
      <li>{{ maxTemp }}</li>
      <li>{{ minTemp }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    currentDate: {
      type: String,
      required: true,
    },
    currentPhe: {
      type: String,
      required: true,
    },
    maxTemp: {
      type: String,
      required: true,
    },
    minTemp: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped></style>
