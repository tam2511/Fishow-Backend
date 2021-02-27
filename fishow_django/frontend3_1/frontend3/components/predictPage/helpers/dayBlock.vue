<template>
  <div class="block">
    <p v-if="dayCalendar" class="date-first">{{ dayCalendar }}</p>
    <p v-if="normDay" class="date-second">{{ normDay }}</p>
  </div>
</template>

<script>
export default {
  props: {
    dayCalendar: {
      type: String,
      required: false,
      default: null,
    },
    normDay: {
      type: String,
      required: false,
      default: null,
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
    height: 24px;
    white-space: nowrap;
  }
}
</style>
