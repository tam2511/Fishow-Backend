<template lang="pug">
  .wind-box.box
    p.title Ветер
    .date.temperature-list
      .date_item(v-for="day in days" :key="day.id") {{ day }}
    .temperature-max.temperature-list.temperature-list__end
      .phenomenon(v-for="direction in dataJSON.direction" :key="direction.id")
        .value
          span {{direction}}
          WindDir(:dir="direction")
    .temperature-max.temperature-list.temperature-list__end.temperature-list__p_t
      .temperature-max_item(v-for="max in dataJSON.wind"
        :key="max.id")
        .value {{ Number(max).toFixed() }}
</template>

<script>
import WindDir from '@/components/predictPage/icon/windDir'
export default {
  components: { WindDir },
  props: {
    days: {
      type: Array,
      required: true,
    },
    windMean: {
      type: String,
      required: true,
    },
    windDirection: {
      type: String,
      required: true,
    },
  },
  computed: {
    dataJSON() {
      try {
        return {
          wind: this.windMean.substr(1, this.windMean.length - 2).split(', '),
          direction: this.windDirection
            .substr(1, this.windDirection.length - 2)
            .split(', '),
        }
      } catch (e) {
        console.log('this.wind = ', this.windMean)
        console.log('this.wind = ', this.windDirection)
        console.log('error = ', e)
        return {
          wind: 'null',
          direction: 'null',
        }
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
