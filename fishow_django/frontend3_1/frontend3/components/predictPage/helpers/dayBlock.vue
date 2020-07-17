<template>
  <div class="block">
    <p class="date-first">{{ dayCalendar }}</p>
    <p class="date-second">{{ normDay }}</p>
  </div>
</template>

<script>
export default {
  props: {
    dayCalendar: {
      type: String,
      required: true,
    },
    normDay: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped lang="scss">
.date {
  &-fisrt {
  }
  &-second {
    color: #a8a8a8;
  }
}
</style>
