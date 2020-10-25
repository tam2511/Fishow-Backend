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
        <div
          v-for="data in uvindexcuted"
          :key="data.gust"
          class="uvindex-main__head"
        >
          <div>{{ data.time }}</div>
          <div>
            <div
              v-for="(value, index) in data.value"
              :key="index"
              class="uvindex-main__item_one"
            >
              <span>{{ titles[data.time][index] }}</span>
              <span class="uv-line_item" :style="color(value)">{{
                value
              }}</span>
            </div>
          </div>
        </div>
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
  data() {
    return {
      titles: {
        Утро: ['6:00', '9:00'],
        День: ['12:00', '15:00'],
        Вечер: ['18:00', '21:00'],
      },
    }
  },
  computed: {
    uvindexcuted() {
      const data = []

      this.readyDataStorage.forEach((item) => {
        data.push(item.uv_index)
      })

      return [
        { time: 'Утро', value: data.splice(0, 2) },
        { time: 'День', value: data.splice(0, 2) },
        { time: 'Вечер', value: data.splice(0, 2) },
      ]
    },
  },
  methods: {
    color(value) {
      const colors = {
        0: '#ebf5db',
        1: '#DEF2BC',
        2: '#DEF2BC',
        3: '#F2EABC',
        4: '#F2EABC',
        5: '#EADC96',
        6: '#ef9460',
        7: '#F3752E',
        8: '#f14f1d',
        9: '#ef420d',
        10: '#ea3400',
        11: '#b046ef',
      }
      return 'background-color: ' + colors[value]
    },
  },
}
</script>

<style scoped lang="scss">
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
.uv-line_item {
  padding: 0.1rem 1.7rem;
  background-color: #00b3ee;

  margin-top: 11px;

  font-weight: 700;
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
.uvindex-main {
  width: 50%;
}
.uvindex-main__item {
  display: flex;
  justify-content: space-around;
  &_one {
    margin-top: 10px;
  }
}
.uvindex-main__head > div:first-child {
  font-weight: 700;
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
