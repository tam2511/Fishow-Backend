<template>
  <div class="uv-line">
    <div
      v-for="value in line"
      :key="value.id"
      class="uv-line_item"
      :style="color(value)"
    >
      {{ value }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    line: {
      type: Array,
      required: true,
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
      console.log(colors)
      console.log(colors[value])
      console.log(value)
      return 'background-color: ' + colors[value]
    },
  },
}
</script>

<style scoped>
.uv-line {
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  justify-items: center;
  align-items: center;
}
.uv-line_item {
  padding: 0.5rem 1rem;
  background-color: #00b3ee;
}
</style>
