<template>
  <div class="data-pick">
    <div v-for="day in tenDays" :key="day.id" class="tenDays">
      <nuxt-link
        :to="{
          name: 'OnePrediction-areal-date-city-fish',
          params: {
            areal: $route.params.areal,
            date: '2021-' + day.split('/')[1] + '-' + day.split('/')[0],
            city: $route.params.city,
            fish,
          },
        }"
        class="button"
      >
        {{ day }}
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import getData from '~/assets/js/getData'
export default {
  props: {
    days: {
      type: String,
      required: true,
    },
  },
  computed: {
    fish() {
      return (this.prediction && this.prediction.fish) || 'щука'
    },
    tenDays() {
      return getData(this.days, 9)
    },
    ...mapState('prediction', ['prediction']),
  },
}
</script>

<style scoped lang="scss">
.data-pick {
  display: flex;
  flex-flow: row;
  flex-wrap: nowrap;

  padding: 15px 0;

  overflow: auto;
}
.is-link {
  background-color: #204a6f85;
}
.tenDays a {
  color: #363636;

  padding: 5px;
  background-color: white;
  cursor: pointer;
  display: inline-block;

  border: 1px solid #dbdbdb;
  border-radius: 4px;
  margin: 5px 5px;
  /*border-radius: 5px;*/
  @media screen and (max-width: 420px) {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }

  &:hover {
    border-color: #b5b5b5;
    color: #363636;
  }
}
</style>
