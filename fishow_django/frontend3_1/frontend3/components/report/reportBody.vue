<template>
  <section>
    <b-field horizontal label="Даты рыбалки">
      <b-input
        name="name"
        :value="report.date_start"
        expanded
        readonly
      ></b-input>
      <b-input
        name="name"
        :value="report.date_end"
        placeholder="Name"
        expanded
        readonly
      ></b-input>
    </b-field>

    <b-field horizontal label="Регион рыбалки">
      <b-input :value="report.areal" name="subject" expanded></b-input>
    </b-field>

    <b-field horizontal label="Ближайший город">
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
}
</script>

<style lang="scss" scoped></style>
