<template lang="pug">
    .container.prediciton-select
      h1.title Прогноз в {{ value === false ? "России" : value }}
      bread-crumbs-select(:areal="value" @clear="value = false")
      .list-areals(v-if="json && !value")
        div.columns(v-for="(city, key2) in json" :key="key2")
          .column
            h2.title {{ key2 }}
          .column.list-areals_item.is-full
            .item-city(v-for="(area, key) in city"
              :key="key" v-if="!value" @click="value = key")  {{ key }}
      div(v-if="value")
        div.columns(v-for="(city2, key) in json[value[0]][value]" :key="key")
          .column
            h2.title {{ key }}
          .column.list-areals_item.is-full
            nuxt-link.item-city(
              v-for="(area, key3) in city2"
              :key="key3"
              :to="{name: 'prognoz-kleva-areal-date-city-fish',params: { areal: value, city: area, date: rightDate, fish: 'щука'}}") {{ area }}
</template>

<script>
import convert from '~/pages/prognoz-kleva/convert'
import breadCrumbsSelect from '@/components/predictPage/breadCrumbsSelect'
export default {
  components: {
    breadCrumbsSelect,
  },
  data() {
    return {
      value: false,
      value2: false,
    }
  },
  computed: {
    rightDate() {
      const d = new Date()
      let month = '' + (d.getMonth() + 1)
      let day = '' + d.getDate()
      const year = d.getFullYear()

      if (month.length < 2) month = '0' + month
      if (day.length < 2) day = '0' + day

      return [year, month, day].join('-')
    },
    json() {
      return convert()
    },
  },
  head() {
    return {
      title: 'Fishow - Прогноз',
    }
  },
}
</script>

<style scoped lang="scss">
.columns {
  padding: 20px 0;
  width: 100%;
}
.item-city {
  cursor: pointer;
  padding: 5px;
  transition: color 0.3s;
  &:hover {
    color: #d58815;
  }
}
.prediciton-select {
  padding: 10px;
}
.list-areals {
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
  &_item {
    font-size: 20px;
    padding: 5px;
  }
}
</style>
