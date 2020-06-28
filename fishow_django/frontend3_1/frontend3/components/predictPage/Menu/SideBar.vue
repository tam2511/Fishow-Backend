<template>
  <div class="card box">
    <b-menu>
      <b-menu-list label="Меню">
        <b-menu-item
          icon="information-outline"
          label="В начало"
          @click="doScroll('.breadcrumb')"
        ></b-menu-item>
        <b-menu-item
          icon="information-outline"
          label="Рыба"
          @click="doScroll('.fish')"
        ></b-menu-item>
        <b-menu-item v-if="predictions">
          <template slot="label" slot-scope="props">
            Прогноз
            <b-icon
              class="is-pulled-right"
              :icon="props.extended ? 'menu-down' : 'menu-up'"
            >
            </b-icon>
          </template>
          <b-menu-item
            icon="account"
            label="Клев"
            @click="doScroll('predic')"
          ></b-menu-item>
        </b-menu-item>
        <b-menu-item v-if="predictions" icon="settings" :active="isActive">
          <template slot="label" slot-scope="props">
            Погода
            <b-icon
              class="is-pulled-right"
              :icon="props.expanded ? 'menu-down' : 'menu-up'"
            ></b-icon>
          </template>
          <b-menu-item
            icon="account"
            label="Температура"
            @click="doScroll('temp')"
          ></b-menu-item>
          <b-menu-item
            icon="cellphone-link"
            label="Ветер"
            @click="doScroll('wind')"
          ></b-menu-item>
        </b-menu-item>
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
  created() {},
  methods: {
    scroll() {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth',
      })
    },
    doScroll(value) {
      console.log('value = ', value)
      let item

      if (value === '.breadcrumb' || value === '.fish') {
        item = document.querySelector(value).getBoundingClientRect().y
      } else {
        item = document
          .querySelector(`.result-container > [class*=${value}]`)
          .getBoundingClientRect().y
      }
      console.log('scroll')
      window.scrollBy({
        top: item - 70,
        behavior: 'smooth',
      })
    },
  },
}
</script>

<style scoped></style>
