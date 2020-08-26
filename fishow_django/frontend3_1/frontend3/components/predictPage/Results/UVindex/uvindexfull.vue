<template>
  <div class="uvindex-box box">
    <h3 class="title">Солнечная активность</h3>

    <div class="columns">
      <uvindex-one-day
        v-for="(day, index) in readyData"
        :key="day.date + index"
        class="column"
        :day="day"
      >
      </uvindex-one-day>
    </div>
    <div class="grid-uv">
      <div v-for="(uv, key) in readyData.uv_index_desc" :key="uv.id" class="">
        {{ key === '6' ? 'Утро' : '' }}
        {{ key === '12' ? 'День' : '' }}
        {{ key === '18' ? 'Вечер' : '' }}
        <div class="grid-uv-child">
          <div class="uv-key">{{ key }}:00</div>
          <uv-line :line="uv" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import readyData from '~/assets/mixins/prediction/readyData'
import UvLine from '~/components/predictPage/Results/UVindex/uv-line'
import UvindexOneDay from '~/components/predictPage/Results/UVindex/uvindexOneDay'
export default {
  components: { UvindexOneDay, UvLine },
  mixins: [readyData],
  props: {
    days: {
      type: Array,
      required: true,
    },
  },
  methods: {
    getNormalDates() {},
  },
}
</script>

<style scoped>
.grid-uv {
}
.grid-uv-child {
  display: grid;
  grid-template-columns: auto 1fr;
}
.uv-key {
  min-width: 40px;
  margin: auto 0;
  text-align: center;
}
</style>
