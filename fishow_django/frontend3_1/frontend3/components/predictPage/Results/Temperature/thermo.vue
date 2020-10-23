<template>
  <div>
    <div class="columns">
      <div class="column">
        <span>Средняя {{ Math.floor(day.mean) }}&#8451;</span>
        <span>Макс {{ day.max }}&#8451; - {{ day.max_date }} августа</span>
        <span>Мин {{ day.min }}&#8451; - {{ day.min_date }} августа</span>
      </div>
      <div class="column">
        <span>Средняя {{ Math.floor(night.mean) }}&#8451;</span>
        <span>Макс {{ night.max }}&#8451; - {{ night.max_date }} августа</span>
        <span>Мин {{ night.min }}&#8451; - {{ night.min_date }} августа</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    day: {
      type: Object,
      required: true,
    },
    night: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.column {
  display: flex;
  flex-flow: column;
}
</style>
