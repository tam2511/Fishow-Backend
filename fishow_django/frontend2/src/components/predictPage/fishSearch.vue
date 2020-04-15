<template>
  <el-select
    v-model="value"
    filterable
    remote
    @change="data"
    no-data-text="Не найдено"
    loading-text="Клюет..."
    reserve-keyword
    placeholder="Введите название рыбы"
    :remote-method="remoteMethod"
    :loading="loading"
  >
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    >
    </el-option>
  </el-select>
</template>

<script>
export default {
  data() {
    return {
      options: [],
      value: [],
      list: [],
      loading: false,

      states: [
        'Судак',
        'Ёрш',
        'Плотва',
        'Лещ',
        'Густера',
        'Сазан',
        'Карп',
        'Линь',
        'Голавль',
        'Язь',
        'Жерех',
        'Чехонь',
        'Уклейка',
        'Быстрянка',
        'Пескарь',
        'Белый',
        'Амур',
        'Толстолобик',
        'Сом',
        'Угорь',
        'Налим',
        'Вьюн',
        'Голец',
        'Минога',
        'Змееголов',
        'Стерлядь',
        'Форель ручьевая',
        'Хариус европейский',
      ],
    }
  },
  mounted() {
    this.list = this.states.map((item) => {
      return { value: `${item}`, label: `${item}` }
    })
  },
  methods: {
    data() {
      this.$emit('data', {
        value: this.value,
      })
    },
    remoteMethod(query) {
      if (query !== '') {
        this.loading = true
        setTimeout(() => {
          this.loading = false
          this.options = this.list.filter((item) => {
            return item.label.toLowerCase().indexOf(query.toLowerCase()) > -1
          })
        }, 200)
      } else {
        this.options = []
      }
    },
  },
}
</script>
