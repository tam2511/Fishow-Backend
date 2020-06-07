<template>
  <b-field class="box" label="Select a date">
    {{ date }}
    <b-datepicker
      :focused-date="date"
      :first-day-of-week="1"
      placeholder="Click to select..."
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
      const year = this.date2
      console.log('ere', year)
      return ''
    },
  },
  mounted() {
    this.month = this.months.filter(
      (item) => item.value === this.date.getMonth()
    )[0].name
  },
  methods: {
    selectMonth(option) {
      if (option) {
        this.date = new Date(this.date)
        this.date.setMonth(option.value)
      }
    },
  },
}
</script>
