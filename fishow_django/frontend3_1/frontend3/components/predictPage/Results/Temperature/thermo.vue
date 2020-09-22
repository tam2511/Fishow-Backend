<template>
  <div>
    <client-only>
      <fusioncharts
        :type="type"
        :width="width"
        :height="height"
        :data-format="dataFormat"
        :data-source="dataSource"
      ></fusioncharts>
    </client-only>
    <div class="columns">
      <div class="column">
        <span>Средняя {{ Math.floor(day.mean) }}&#8451;</span>
        <span>Макс {{ day.max }}&#8451; - {{ day.max_date }} августа</span>
        <span>Мин {{ day.min }}&#8451; - {{ day.min_date }} августа</span>
      </div>
      <div class="column">
        <span>Средняя {{ Math.floor(night.mean) }}&#8451;</span>
        <span>Макс {{ night.max }}&#8451; - {{ night.max_date }} августа</span>
        <span>Мин {{ night.min }}&#8451; - {{ night.min_date }} августа</span>
      </div>
    </div>
  </div>
</template>

<script>
const data = {
  chart: {
    caption: 'Countries With Most Oil Reserves [2017-18]',
    subCaption: 'In MMbbl = One Million barrels',
    xAxisName: 'Country',
    yAxisName: 'Reserves (MMbbl)',
    numberSuffix: 'K',
    theme: 'fusion',
  },
  data: [
    {
      label: 'Venezuela',
      value: '290',
    },
    {
      label: 'Saudi',
      value: '260',
    },
    {
      label: 'Canada',
      value: '180',
    },
    {
      label: 'Iran',
      value: '140',
    },
    {
      label: 'Russia',
      value: '115',
    },
    {
      label: 'UAE',
      value: '100',
    },
    {
      label: 'US',
      value: '30',
    },
    {
      label: 'China',
      value: '30',
    },
  ],
}

export default {
  props: {
    day: {
      type: Object,
      required: true,
    },
    night: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      width: '100%',
      height: '400',
      type: 'column2d',
      dataFormat: 'json',
      dataSource: data,
    }
  },
}
</script>

<style scoped>
.column {
  display: flex;
  flex-flow: column;
}
</style>
