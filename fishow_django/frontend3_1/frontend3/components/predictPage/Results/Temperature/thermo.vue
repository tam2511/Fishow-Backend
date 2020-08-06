<template>
  <client-only>
    <fusioncharts
      :type="type"
      :width="width"
      :height="height"
      :data-format="dataFormat"
      :data-source="dataSource"
    ></fusioncharts>
  </client-only>
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

<style scoped></style>
