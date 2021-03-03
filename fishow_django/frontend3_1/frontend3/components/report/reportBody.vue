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
      <b-input :value="report.areal" name="subject" expanded readonly></b-input>
      <b-input :value="report.city" name="subject" expanded readonly></b-input>
    </b-field>

    <b-field horizontal label="Remark">
      <b-input
        :value="report.remark"
        name="subject"
        expanded
        readonly
      ></b-input>
    </b-field>

    <b-field horizontal label="tags">
      <b-input :value="report.targ" name="subject" expandedr eadonly></b-input>
    </b-field>

    <b-field horizontal label="Категория">
      <b-input
        :value="report.category"
        name="subject"
        expanded
        readonly
      ></b-input>
    </b-field>

    <div v-for="value in fishList" :key="value.id">
      <section>
        <h3>{{ value.body.name.title }}</h3>

        <b-field label="Активность рыбы">
          <b-input
            :value="value.body.activity"
            name="subject"
            expanded
            readonly
          ></b-input>
        </b-field>

        <b-field label="Суммарный вес улова">
          <b-input v-model="value.body.weight" expanded readonly> </b-input>
        </b-field>

        <b-field label="Число экземпляров">
          <b-input v-model="value.body.count" expanded readonly> </b-input>
        </b-field>

        <b-field label="Перечислите способы ловли">
          <b-input v-model="value.body.methods" expanded readonly> </b-input>
        </b-field>

        <b-field label="Укажите наиболее эффективные насадки">
          <b-input v-model="value.body.moreEffectiveTips" expanded readonly>
          </b-input>
        </b-field>

        <b-field label="Перечислите примерные часы активности рыбы">
          <b-input v-model="value.body.activityHours" expanded readonly>
          </b-input>
        </b-field>

        <b-field label="Укажите самые результативные горизонты ловли">
          <b-input v-model="value.body.horizons" expanded readonly> </b-input>
        </b-field>

        <b-field label="На каких глубинах чаще всего клевало">
          <b-input v-model="value.body.depths" expanded readonly> </b-input>
        </b-field>
      </section>
    </div>
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
    fishList() {
      if (!this.report.fishing) {
        return []
      }
      let result = []
      console.log('fishing = ', this.report.fishing)
      try {
        const body = JSON.parse(this.report.fishing)
        result = body
      } catch (e) {
        console.error('error = ', e)
      }
      return result
    },
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
