<template>
  <div v-if="!one" class="uvindex-box box">
    <h3 class="title">Солнечная активность</h3>
    <div class="columns">
      <div class="column max-width"></div>
      <uvindex-one-day
        v-for="(day, index) in readyDataStorage"
        :key="day.date + index"
        class="column"
        :day="day"
      >
      </uvindex-one-day>
    </div>
    <div class="grid-uv">
      <div
        v-for="(uv, key) in readyDataStorage.uv_index_desc"
        :key="uv.id"
        class=""
      >
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
  <div v-else class="unvidex-container">
    <div class="uvindex-date">
      <div class="uvindex-date__item">
        Сб 11 июля
      </div>
    </div>
    <div class="uvindex-main">
      <div class="uvindex-main__item">
        <span class="uvindex-main__head">
          Утро
        </span>
      </div>
      <div class="uvindex-main__item"></div>
      <div class="uvindex-main__item"></div>
    </div>
    <div class="uvindex_desc">
      21 августа бла бла бла
    </div>
  </div>
</template>

<script>
import readyDataStorage from '~/assets/mixins/prediction/readyDataStorage'

import UvLine from '~/components/predictPage/Results/UVindex/uv-line'
import UvindexOneDay from '~/components/predictPage/Results/UVindex/uvindexOneDay'
import Protection from '~/components/predictPage/Results/UVindex/message/protection'
export default {
  components: { UvindexOneDay, UvLine, Protection },
  mixins: [readyDataStorage],
  props: {
    one: {
      type: Boolean,
      default: false,
    },
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
.unvidex-container {
  display: flex;
  flex-flow: row;
  justify-content: space-between;
  align-items: center;
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
