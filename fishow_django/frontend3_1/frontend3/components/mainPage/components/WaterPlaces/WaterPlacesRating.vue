<template>
  <div class="water-places-container">
    <div>
      <h3>Водоем</h3>
      <div>
        <water-places-search @selected="showSelected" />
      </div>
    </div>
    <div>
      <h3>Рейтинг водоема</h3>
      <div v-if="waterPlace">
        <code>
          {{ waterPlace }}
        </code>
        <span class="rating">{{ waterPlace.fish_rating }}</span> Составлен по
        оценке пользователей
      </div>
    </div>
  </div>
</template>

<script>
import WaterPlacesSearch from '~/components/mainPage/components/WaterPlaces/WaterPlacesSearch'
export default {
  name: 'WaterPlacesRating',
  components: {
    WaterPlacesSearch,
  },
  data() {
    return {
      waterPlace: null,
    }
  },
  methods: {
    showSelected(val) {
      this.waterPlace = val
    },
  },
}
</script>

<style lang="scss" scoped>
.water-places-container {
  display: flex;
  & > div {
    width: 50%;
    margin: 20px;
  }
}
</style>
