<template>
  <b-field class="" label="Выберите дату">
    <b-datepicker
      id="pdata"
      v-model="day"
      :focused-date="date"
      :first-day-of-week="1"
      placeholder="Нажмите что бы выбрать"
      @input="goToDay"
    >
      <template slot="header">
        <b-field>
          <b-autocomplete
            v-model="month"
            open-on-focus
            readonly
            :data="months"
            field="name"
            @select="selectMonth"
          >
          </b-autocomplete>
          <p class="control">
            <!--            <span class="button is-static">{{ date.getFullYear() }}</span>-->
          </p>
        </b-field>
      </template>
    </b-datepicker>
  </b-field>
</template>

<script>
export default {
  props: {
    date2: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      month: null,
      day: null,
      date: new Date(),
      months: [
        { name: 'Январь', value: 0 },
        { name: 'Февраль', value: 1 },
        { name: 'Март', value: 2 },
        { name: 'Апрель', value: 3 },
        { name: 'Май', value: 4 },
        { name: 'Июнь', value: 5 },
        { name: 'Июль', value: 6 },
        { name: 'Август', value: 7 },
        { name: 'Сентябрь', value: 8 },
        { name: 'Октябрь', value: 9 },
        { name: 'Ноябрь', value: 10 },
        { name: 'Декабрь', value: 11 },
      ],
    }
  },
  computed: {
    rightDate() {
      const d = new Date(this.day)
      let month = '' + (d.getMonth() + 1)
      let day = '' + d.getDate()
      const year = d.getFullYear()

      if (month.length < 2) month = '0' + month
      if (day.length < 2) day = '0' + day

      return [year, month, day].join('-')
    },
  },
  mounted() {
    this.month = this.months.filter(
      (item) => item.value === this.date.getMonth()
    )[0].name
    // const newData = this.date2.split('-')
    // this.date = newData[1] + '-' + newData[2] + '-' + newData[0]
  },
  methods: {
    selectMonth(option) {
      if (option) {
        this.date = new Date(this.date)
        this.date.setMonth(option.value)
        console.log('asdasd')
      }
    },
    goToDay() {
      console.log('select')
      this.$router.push({
        name: 'PredictionPage-areal-date-city-fish',
        params: {
          areal: this.$route.params.areal,
          date: this.rightDate,
          city: this.$route.params.city,
          fish: this.$route.params.fish,
        },
        hash: '#pdata',
      })
      // fish: this.$route.params.fish,
      //   date: this.$route.params.date,
      //   city: this.$route.params.city,
      //   areal: this.$route.params.areal,
    },
  },
}
</script>
