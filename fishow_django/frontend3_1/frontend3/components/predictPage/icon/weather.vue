<template>
  <div>
    <b-tooltip :label="day" multilined>
      <img
        class="weather-icon"
        :src="'/png/' + result + '.png'"
        width="50"
        height="50"
        alt="пасмурно"
      />
    </b-tooltip>
  </div>
</template>

<script>
export default {
  props: {
    day: {
      type: String,
      required: true,
    },
  },
  computed: {
    result() {
      let result
      switch (this.day) {
        case "['пасмурно', ' небольшой дождь', ' осадки']":
          result = 'rainy'
          break
        case "['пасмурно', 'малооблачно', 'ясно']":
          result = 'cloud'
          break
        case "['облачно', 'ясно', 'малооблачно']":
          result = 'cloud'
          break
        case "['пасмурно', 'облачно', ' небольшой дождь']":
          result = 'rainy'
          break
        case "['пасмурно', 'малооблачно', ' небольшой дождь']":
          result = 'rainy'
          break
        case "['ясно']":
          result = 'sun'
          break
        case "['пасмурно', ' небольшой дождь', 'облачно']":
          result = 'rainy'
          break
        case "['пасмурно', ' дождь', ' небольшой дождь']":
          result = 'rain'
          break
        case "['ясно', 'пасмурно', 'малооблачно']":
          result = 'cloud'
          break
      }
      return result
    },
  },
}
</script>

<style scoped>
.weather-icon {
  height: 50px;
  width: 50px;
}
</style>
