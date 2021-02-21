<template>
  <section>
    <b-field horizontal label="Даты рыбалки">
      <b-input name="name" :value="dateStart" expanded readonly></b-input>
      <b-input
        name="name"
        :value="dateEnd"
        placeholder="Name"
        expanded
        readonly
      ></b-input>
    </b-field>

    <b-field horizontal label="Регион рыбалки">
      <b-input :value="report.areal" name="subject" expanded></b-input>
      <b-input :value="report.city" name="subject" expanded></b-input>
    </b-field>

    <b-field horizontal label="Remark">
      <b-input :value="report.remark" name="subject" expanded></b-input>
    </b-field>

    <b-field horizontal label="tags">
      <b-input :value="report.targ" name="subject" expanded></b-input>
    </b-field>

    <b-field horizontal label="Категория">
      <b-input :value="report.category" name="subject" expanded></b-input>
    </b-field>

    <b-field horizontal label="fishing">
      <b-input :value="report.fishing" name="subject" expanded></b-input>
    </b-field>
  </section>
</template>

<script>
export default {
  name: 'reportBody',
  props: {
    report: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      date: {
        start: '',
        end: '',
      },
    }
  },
  computed: {
    dateEnd() {
      return new Date(this.report.date_end).toLocaleDateString()
    },
    dateStart() {
      return new Date(this.report.date_start).toLocaleDateString()
    },
  },
  methods: {
    convertDate(date) {
      return new Date(date).toDateString()
    },
  },
}
</script>

<style lang="scss" scoped>
section {
  padding: 15px;
  .dates input {
    pointer-events: none;
  }
}
</style>
<style lang="scss">
section {
  .dates input {
    pointer-events: none;
  }
}
</style>
