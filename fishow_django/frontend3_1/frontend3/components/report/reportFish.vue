<template>
  <div class="fishTemplate-section">
    <section>
      <multiselect
        v-model="fishTemplate.name"
        tag-placeholder="Добавьте новый тег"
        placeholder="Выберите рыбу из списка"
        label="title"
        :options="fishList"
        :multiple="false"
        :taggable="false"
      >
      </multiselect>
    </section>

    <div class="main-fish-info">
      <section>
        <b-field>
          <b-input
            v-model="fishTemplate.activity"
            placeholder="Активность рыбы"
          >
          </b-input>
        </b-field>
      </section>

      <section>
        <b-field>
          <b-input
            v-model="fishTemplate.weight"
            placeholder="Суммарный вес улова"
          >
          </b-input>
        </b-field>
      </section>

      <section>
        <b-field>
          <b-input
            v-model="fishTemplate.count"
            placeholder="Число экземпляров"
          ></b-input>
        </b-field>
      </section>
    </div>

    <section>
      <b-field>
        <b-input
          v-model="fishTemplate.methods"
          placeholder="Перечислите способы ловли"
        ></b-input>
      </b-field>
    </section>

    <section>
      <b-field>
        <b-input
          v-model="fishTemplate.moreEffectiveTips"
          placeholder="Укажите наиболее эффективные насадки"
        ></b-input>
      </b-field>
    </section>

    <section>
      <b-field>
        <b-input
          v-model="fishTemplate.activityHours"
          placeholder="Перечислите примерные часы активности рыбы"
        ></b-input>
      </b-field>
    </section>

    <section>
      <b-field>
        <b-input
          v-model="fishTemplate.horizons"
          placeholder="Укажите самые результативные горизонты ловли"
        ></b-input>
      </b-field>
    </section>

    <section>
      <b-field>
        <b-input
          v-model="fishTemplate.depths"
          placeholder="На каких глубинах чаще всего клевало"
        ></b-input>
      </b-field>
    </section>
  </div>
</template>

<script>
import fishList from '~/assets/data/fishList'
export default {
  name: 'ReportFish',
  props: {
    name: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      fishList,
      fishTemplate: {
        name: '',
        activity: '',
        weight: null,
        count: null,
        methods: '',
        moreEffectiveTips: '',
        activityHours: '',
        horizons: '',
        depths: '',
      },
    }
  },
  watch: {
    fishTemplate: {
      deep: true,
      handler() {
        const readyData = {
          id: this.name,
          ...this.fishTemplate,
        }
        this.$emit('input', readyData)
      },
    },
  },
}
</script>

<style lang="scss" scoped>
.main-fish-info {
  display: flex;
  justify-content: space-around;
  & > section {
    width: 33%;
  }
}
.fishTemplate-section {
  margin: 30px 0;
  section {
    margin-bottom: 10px;
  }
}
</style>
