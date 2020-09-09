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
      <b-menu-list v-if="predictions || prediction" label="Прогноз">
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
      <b-menu-list v-if="predictions" label="Опции">
        <b-menu-item
          icon="fish"
          pack="fa"
          label="Поделиться прогнозом"
          @click="copyToClip"
        >
        </b-menu-item>
      </b-menu-list>
    </b-menu>
    <b-message
      v-if="link"
      id="message-link"
      title="Ваша ссылка скопирована"
      type="is-success"
      aria-close-label="Close message"
      @close="link = null"
    >
      {{ link }}
    </b-message>
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
      link: null,
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
        {
          icon: 'sun',
          label: 'Солнечная активность',
          click: 'uvindex',
        },
      ],
    }
  },
  computed: {
    ...mapState('prediction', ['predictions', 'prediction']),
  },
  methods: {
    scroll() {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth',
      })
    },
    copyToClip() {
      const fish = this.predictions.fish
      const date = this.predictions.date
      const city = this.predictions.city
      const areal = this.predictions.areal
      this.link = `http://fishow.ru/prognoz-kleva/${areal}/${date}/${city}/${fish}`
      const copyElem = document.createElement('textarea')
      copyElem.value = this.link
      copyElem.style.position = 'absolute'
      copyElem.style.left = '-9999px'
      document.body.appendChild(copyElem)
      copyElem.focus()
      copyElem.select()
      copyElem.setSelectionRange(0, 9999)
      try {
        const successful = document.execCommand('copy')
        const msg = successful ? 'successful' : 'unsuccessful'
        console.log('Fallback: Copying text command was ' + msg)
      } catch (err) {
        console.error('Fallback: Oops, unable to copy', err)
      }
      copyElem.remove()
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
