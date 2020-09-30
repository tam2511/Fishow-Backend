<template>
  <div class="uvindex-box box">
    <h3 class="title">Солнечная активность</h3>
    <div class="columns">
      <div class="column max-width"></div>
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
        <span v-if="key === '6'">Утро</span>
        <span v-if="key === '12'">День</span>
        <span v-if="key === '18'">Вечер</span>
        <div class="grid-uv-child">
          <div class="uv-key">{{ key }}:00</div>
          <uv-line :line="uv" />
        </div>
      </div>
    </div>
    <protection />
  </div>
</template>

<script>
import readyData from '~/assets/mixins/prediction/readyData'
import UvLine from '~/components/predictPage/Results/UVindex/uv-line'
import UvindexOneDay from '~/components/predictPage/Results/UVindex/uvindexOneDay'
import Protection from '~/components/predictPage/Results/UVindex/message/protection'
export default {
  components: { UvindexOneDay, UvLine, Protection },
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
.grid-uv span {
  font-weight: 700;
}
.grid-uv-child {
  display: grid;
  grid-template-columns: auto 1fr;
}
.uv-key {
  min-width: 40px;
  text-align: center;
  margin: auto 10px auto 0;
}
.column {
  text-align: center;
}
.max-width {
  max-width: 45px;
}
.uv-table {
  padding-top: 30px;
}
.uvindex-box.box::after {
  content: '';
  position: absolute;
  top: 50%;
  right: 0;
  height: 30px;
  width: 30px;
  display: block;
  background-color: #00b3ee;
}

@media screen and (max-width: 768px) {
  div.columns {
    display: flex;
  }
  .uvindex-box.box {
    overflow: auto;
  }
}
</style>
