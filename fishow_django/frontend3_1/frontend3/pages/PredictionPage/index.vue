<template lang="pug">
    .container.prediciton-select
      .row.row-50
        .col-lg-12
          .main-component
            article.heading-component
              .heading-component-inner
                h5.heading-component-title {{ value ? "Город " : "Область"}}
                .buttons-nav(v-if='value')
                  .button.button-xs.button-primary(@click="value = false") Назад
          .list-areals
            .list-areals_item(v-for="(area, key) in json" :key="key" v-if="!value")
              span.item-city(@click="value = key") {{ key }}
            .list-areals_item(v-for="city in json[value]" :key="city" v-if="!value2")
              nuxt-link.item-city(:to="{name: 'PredictionPage-areal-date-city-fish',params: { areal: value, city, date: rightDate, fish: 'щука'}}") {{ city }}
</template>

<script>
import data from '~/pages/PredictionPage/data'
export default {
  data() {
    return {
      value: false,
      value2: false,
      areal: ['Московская-область', 'Ленинградская область'],
      cities: ['Москва', 'Санкт-Петербург'],
      options: [
        'Select option',
        'options',
        'selected',
        'mulitple',
        'label',
        'searchable',
        'clearOnSelect',
        'hideSelected',
        'maxHeight',
        'allowEmpty',
        'showLabels',
        'onChange',
        'touched',
      ],
      json: data,
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
  },
  head() {
    return {
      title: 'Fishow - Прогноз',
    }
  },
}
</script>

<style scoped lang="scss">
.item-city {
  cursor: pointer;
  padding: 5px;
  transition: color 0.3s;
  &:hover {
    color: #d58815;
  }
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
