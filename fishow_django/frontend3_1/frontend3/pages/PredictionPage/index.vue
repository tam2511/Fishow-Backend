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
      json: {
        'Алтайский край': ['Барнаул', 'Бийск', 'Рубцовск'],
        'Амурская область': ['Белогорск', 'Благовещенск', 'Свободный', 'Тында'],
        'Архангельская область': ['Архангельск', 'Котлас', 'Северодвинск'],
        'Астраханская область': ['Астрахань', 'Ахтубинск'],
        'Белгородская область': ['Белгород', 'Старый Оскол'],
        'Брянская область': ['Брянск', 'Клинцы'],
        'Владимирская область': ['Владимир', 'Ковров', 'Муром'],
        'Волгоградская область': [
          'Волгоград',
          'Волжский',
          'Камышин',
          'Михайловка',
        ],
        'Вологодская область': ['Великий устюг', 'Вологда', 'Череповец'],
        'Воронежская область': ['Воронеж', 'Лиски'],
        'Еврейская автономная область': ['Биробиджан', 'Облучье'],
        'Забайкальский край': ['Краснокаменск', 'Чита'],
        'Ивановская область': ['Иваново', 'Кинешма', 'Шуя'],
        'Иркутская область': ['Ангарск', 'Братск', 'Иркутск', 'Усть-Илимск'],
        'Кабардино-Балкарская республика': [
          'Азау',
          'Майский',
          'Нальчик',
          'Эльбрус',
        ],
        'Калининградская область': ['Калининград'],
        'Калужская область': ['Калуга', 'Обнинск'],
        'Камчатский край': ['Елизово', 'Петропаловск-Камчатский'],
        'Карачаево-Черкесская республика': ['Архыз', 'Домбай', 'Черкесск'],
        'Кемеровская область': ['Белово', 'Кемерово', 'Новокузнецк'],
        'Кировская область': ['Киров'],
        'Костромская область': ['Кострома', 'Шарья'],
        'Краснодарский край': ['Краснодар', 'Новороссийск', 'Сочи'],
        'Красноярский край': ['Ачинск', 'Красноярск', 'Норильск'],
        'Курганская область': ['Курган', 'Шадринск'],
        'Курская область': ['Железногорск', 'Курск'],
        'Ленинградская область': [
          'Всеволжск',
          'Выборг',
          'Луга',
          'Санкт-Петербург',
          'Сосновый Бор',
        ],
        'Липецкая область': ['Елец', 'Липецк'],
        'Магаданская область': ['Магадан'],
        'Московская область': [
          'Балашиха',
          'Дмитров',
          'Дубна',
          'Королев',
          'Москва',
          'Одинцово',
          'Подольск',
          'Сергиев Посад',
          'Щелково',
        ],
      },
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
