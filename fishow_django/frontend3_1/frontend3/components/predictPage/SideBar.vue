<template>
  <div class="card box">
    <aside class="menu">
      <p class="menu-label">
        Главная
      </p>
      <ul class="menu-list">
        <li><a>Город</a></li>
        <li><a>Выбор рыбы</a></li>
      </ul>
      <p class="menu-label">
        Прогноз
      </p>
      <ul class="menu-list">
        <li><a>Вероятность клева</a></li>
        <li>
          <a class="is-active">Погода</a>
          <ul>
            <li><a>Температура воздуха</a></li>
            <li><a>Осадки</a></li>
          </ul>
        </li>
        <li><a>Ветер</a></li>
        <li><a>Давление</a></li>
        <li><a>Луна</a></li>
      </ul>
    </aside>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      mini: true,
    }
  },
  created() {
    this.setActive()
  },
  methods: {
    setActive() {
      if (process.browser) {
        const list = [...document.querySelectorAll('aside.menu a')]
        list.forEach((item) => {
          item.addEventListener('click', (event) => {
            document
              .querySelector('aside.menu a.is-active')
              .classList.toggle('is-active')
            event.target.classList.toggle('is-active')
          })
        })
      }
    },
  },
}
</script>

<style scoped></style>
