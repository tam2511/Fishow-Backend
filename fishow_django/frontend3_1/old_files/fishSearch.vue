<template>
  <el-select
    v-model="value"
    filterable
    remote
    no-data-text="Не найдено"
    loading-text="Клюет..."
    reserve-keyword
    placeholder="Введите название рыбы"
    :remote-method="remoteMethod"
    :loading="loading"
    @change="data"
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
        'щука',
        'судак',
        'окунь',
        'берш',
        'речная форель',
        'озерная форель',
        'елец',
        'чехонь',
        'сом',
        'голавль',
        'язь',
        'карп',
        'жерех',
        'лещ',
        'карась',
        'линь',
        'пескарь',
        'ротан',
        'плотва',
        'красноперка',
        'налим',
        'густера',
        'амур',
        'ерш',
        'сазан',
        'подуст',
        'толстолобик',
        'вобла',
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
            return item.label.toLowerCase().includes(query.toLowerCase())
          })
        }, 200)
      } else {
        this.options = []
      }
    },
  },
}
</script>
