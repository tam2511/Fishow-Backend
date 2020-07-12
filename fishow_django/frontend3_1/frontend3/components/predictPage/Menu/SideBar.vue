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
      <b-menu-list label="Прогноз">
        <b-menu-item
          icon="percent"
          pack="fas"
          label="Клев"
          @click="doScroll('predic')"
        />
        <b-menu-item
          pack="fas"
          icon="thermometer"
          label="Погодные условия"
          @click="doScroll('temp')"
        />
        <b-menu-item label="Ветер" @click="doScroll('wind')"></b-menu-item>
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
        item = document.querySelector(value).getBoundingClientRect().y
      } else {
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
</style>
