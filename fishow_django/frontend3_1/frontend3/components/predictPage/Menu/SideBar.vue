<template>
  <div class="card box">
    <b-menu>
      <b-menu-list label="Меню">
        <b-menu-item
          icon="arrow-up"
          label="В начало"
          pack="fas"
          @click="doScroll('.breadcrumb')"
        />
        <b-menu-item
          icon="fish"
          pack="fas"
          label="Виды рыб"
          @click="doScroll('.fish')"
        />
      </b-menu-list>
      <b-menu-list v-if="predictions" label="Прогноз">
        <b-menu-item
          v-for="menu in menuPrognos"
          :key="menu.title"
          :icon="menu.icon"
          :label="menu.label"
          size="is-small"
          icon-pack="fas"
          @click="doScroll(menu.click)"
        ></b-menu-item>
      </b-menu-list>
    </b-menu>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      drawer: true,
      mini: true,
      isActive: false,
      menuPrognos: [
        {
          icon: 'percent',
          label: 'Клев',
          click: 'predic',
        },
        {
          icon: 'thermometer-quarter',
          label: 'Погодные условия',
          click: 'temp',
        },
        {
          icon: 'wind',
          label: 'Ветер',
          click: 'wind',
        },
        {
          icon: 'mountain',
          label: 'Давление',
          click: 'pressure',
        },
        {
          icon: 'moon',
          label: 'Луна',
          click: 'moon',
        },
      ],
    }
  },
  computed: {
    ...mapState('prediction', ['predictions']),
  },
  methods: {
    scroll() {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth',
      })
    },
    doScroll(value) {
      let item
      if (value === '.breadcrumb' || value === '.fish') {
        if (document.querySelector(value)) {
          item = document.querySelector(value).getBoundingClientRect().y
        }
      } else if (
        document.querySelector(`.result-container > [class*=${value}]`)
      ) {
        item = document
          .querySelector(`.result-container > [class*=${value}]`)
          .getBoundingClientRect().y
      }
      window.scrollBy({
        top: item - 70,
        behavior: 'smooth',
      })
    },
  },
}
</script>

<style scoped lang="scss">
.card.box {
  height: 100%;
}
.icon.is-small i {
  font-size: 12px;
}
</style>
