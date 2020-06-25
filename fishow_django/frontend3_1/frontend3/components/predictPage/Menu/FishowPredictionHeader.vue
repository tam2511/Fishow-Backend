<template>
  <div class="card box">
    <div class="columns">
      <div class="column">
        <slot></slot>
      </div>
      <div class="column">
        <p class="title">Прогноз клева на {{ niceDays }}</p>
        <span>
          Планируйте и наслаждайтесь рыбалкой в {{ $route.params.city }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      niceDays: null,
    }
  },
  created() {
    this.convertDays()
  },
  methods: {
    convertDays() {
      const whatMonth = {
        '01': 'Января',
        '02': 'Февраля',
        '03': 'Марта',
        '04': 'Апреля',
        '05': 'Мая',
        '06': 'Июня',
        '07': 'Июля',
        '08': 'Августа',
        '09': 'Сентября',
        '10': 'Октября',
        '11': 'Ноября',
        '12': 'Декабря',
      }
      const day = this.$route.params.date.split('-')
      const result = whatMonth[day[1]]
      this.niceDays = day[2] + ' ' + result
    },
  },
}
</script>

<style scoped>
.card {
  min-height: 200px;

  background: url('/background_header.png') no-repeat center;
  background-size: cover;
}
.title,
.column span {
  color: #fff;
}
</style>
