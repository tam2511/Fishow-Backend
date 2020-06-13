<template lang="pug">
    .temperature-box.box
      p.title Температура
      .date.temperature-list
        .date_item(v-for="day in days" :key="day.id") {{ day }}
      .temperature-max.temperature-list.temperature-list__end
        .phenomenon(v-for="phe in dataJSON.phenomen" :key="phe.id")
          .value
            weather(:day="phe")
      .temperature-max.temperature-list.temperature-list__end.temperature-list__p_t
        .temperature-max_item(v-for="max in dataJSON.maxTemp"
          :key="max.id" :style="'padding-bottom:' + max * 3 + 'px'")
          .value +{{ max }}
      .temperature-min.temperature-list.temperature-list__start.temperature-list__p_b
        .temperature-min_item(v-for="min in dataJSON.minTemp"
          :key="min.id" :style="'padding-top:' + (50 - min * 3) + 'px'")
          .value {{ min >= 0 ? '+' : '' }}{{ min }}
</template>

<script>
import Weather from '~/components/predictPage/icon/weather'
export default {
  components: { Weather },
  props: {
    phenomenon: {
      type: String,
      required: true,
    },
    days: {
      type: Array,
      required: true,
    },
    tempMin: {
      type: String,
      required: true,
    },
    tempMean: {
      type: String,
      required: true,
    },
    tempMax: {
      type: String,
      required: true,
    },
  },
  computed: {
    dataJSON() {
      try {
        return {
          phenomen: JSON.parse(this.phenomenon),
          minTemp: JSON.parse(this.tempMin),
          meanTemp: JSON.parse(this.tempMean),
          maxTemp: JSON.parse(this.tempMax),
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
    padding-top: 70px;
  }
  &__p_b {
    padding-bottom: 10px;
  }
}
.phenomenon {
  position: relative;
}
.temperature-max_item {
  background-color: #fee187;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    top: -25px;
    left: 10px;
    color: #000;
  }
}
.temperature-min_item {
  background-color: #7957d582;
  color: white;
  width: 5%;
  position: relative;
  .value {
    position: absolute;
    bottom: -25px;
    left: 10px;
    color: #000;
  }
}
.value {
  position: absolute;
  color: #000;
  bottom: -50px;
  left: -25px;
  width: 50px;
}
.date_item {
  font-weight: 700;
  font-size: 20px;
}
</style>
