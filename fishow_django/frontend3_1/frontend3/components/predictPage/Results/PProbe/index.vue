<template lang="pug">
  .prediction-box.box
    p.title Прогноз клева
    .date.temperature-list
      .date_item(v-for="day in days" :key="day.id") {{ day }}
    .temperature-max.temperature-list.temperature-list__end.temperature-list__p_t
      .temperature-max_item(v-for="max in dataJSON.probMax"
        :key="max.id" :style="'padding-bottom:' + max * 100 + 'px'")
        .value {{ (max * 100).toFixed() }} %
    .temperature-min.temperature-list.temperature-list__start.temperature-list__p_b
      .temperature-min_item(v-for="min in dataJSON.probMin"
        :key="min.id" :style="'padding-top:' + (50 - min * 0) + 'px'")
        .value {{ (min * 100).toFixed() }} %
</template>
pi
<script>
export default {
  props: {
    days: {
      type: Array,
      required: true,
    },
    probMaxProp: {
      type: String,
      required: true,
    },
    probMinProp: {
      type: String,
      required: true,
    },
  },

  computed: {
    dataJSON() {
      try {
        return {
          probMax: JSON.parse(this.probMaxProp),
          probMin: JSON.parse(this.probMinProp),
        }
      } catch (e) {
        return null
      }
    },
  },
}
</script>

<style scoped lang="scss">
.date {
  padding-bottom: 20px;
}
.temperature-list {
  display: flex;
  justify-content: space-around;
  &__start {
    align-items: flex-start;
  }
  &__end {
    align-items: flex-end;
  }
  &__p_t {
    padding-top: 10px;
  }
  &__p_b {
    padding-bottom: 10px;
  }
}
.temperature-max_item {
  background-color: #1e347b;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    top: -25px;
    left: 10px;
    color: #000;
    width: 100%;
  }
}
.temperature-min_item {
  background-color: #7b1e6f;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    bottom: -25px;
    left: 10px;
    color: #000;
    width: 100%;
  }
}
.date_item {
  font-weight: 700;
  font-size: 20px;
}
</style>
