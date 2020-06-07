<template>
  <div class="card box">
    <div class="columns">
      <div class="column is-three-fifths">
        <p class="title">Прогноз на 9 дней</p>
        Наслаждайтесь максимально хорошо спланированной рыбалкой
      </div>
      <div class="column">
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-primary">
              <p class="subtitle">Вероятность клева</p>
            </article>
            <article class="tile is-child notification is-warning">
              <p class="subtitle">Погодные условия</p>
            </article>
          </div>
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-info">
              <p class="subtitle">Влажность</p>
            </article>
            <article class="tile is-child notification is-primary">
              <p class="subtitle">Луна</p>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped></style>
