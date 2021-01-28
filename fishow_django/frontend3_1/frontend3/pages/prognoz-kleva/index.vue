<template>
  <div class="container prediction-select">
    <h1 class="title">Прогноз в {{ value === false ? 'России' : value }}</h1>
    <bread-crumbs-select :areal="value" @clear="value = false" />
    <div
      v-if="json && !value"
      class="is-flex is-flex-direction-row is-flex-wrap-wrap"
    >
      <div v-for="(city, key2) in json" :key="key2" class="columns is-full">
        <div class="column">
          <h2 class="title">{{ key2 }}</h2>
        </div>
        <div class="column p-1 is-size-4 is-full">
          <div
            v-for="(area, key) in city"
            :key="key"
            class="city"
            @click="value = key"
          >
            {{ key }}
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div v-for="(city2, key) in cities" :key="key" class="columns">
        <div class="column">
          <h2 class="title">{{ key }}</h2>
        </div>
        <div class="column p-1 is-size-4 is-full">
          <nuxt-link
            v-for="(area, key3) in city2"
            :key="key3"
            :to="{
              name: 'prognoz-kleva-areal-date-city-fish',
              params: {
                areal: value,
                city: area,
                date: rightDate,
                fish: 'щука',
              },
            }"
            class="city"
          >
            {{ area }}</nuxt-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import breadCrumbsSelect from '@/components/predictPage/breadCrumbsSelect'
import convert from '~/assets/js/convert'
import { predictionSelect } from '~/assets/descriptions'
import rightDate from '~/assets/mixins/prediction/rightDate'

export default {
  components: {
    breadCrumbsSelect,
  },
  mixins: [rightDate],
  data() {
    return {
      value: false,
      value2: false,
    }
  },
  head() {
    return {
      title: predictionSelect.title,
      description: predictionSelect.description,
    }
  },
  computed: {
    json() {
      return convert()
    },
    cities() {
      return this.json[this.value[0]][this.value]
    },
  },
}
</script>
