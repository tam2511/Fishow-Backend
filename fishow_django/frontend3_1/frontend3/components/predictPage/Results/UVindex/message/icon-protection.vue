<template>
  <div class="icon">
    <span> {{ value }} </span>
    <svg
      width="1017"
      height="970"
      viewBox="0 0 1017 970"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M425.497 73.1524C460.849 6.64567 556.151 6.64561 591.503 73.1524L982.843 809.38C1016.12 871.99 970.746 947.5 899.841 947.5H117.159C46.2539 947.5 0.87639 871.99 34.1564 809.38L425.497 73.1524Z"
        :fill="icon.color"
        stroke="#AEBBC2"
        stroke-width="45"
      />
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      required: true,
    },
  },
  computed: {
    icon() {
      const icons = {
        '1-2': { color: '#9CCC65' },
        '3-5': { color: '#FBC02D' },
        '6-7': { color: '#FF9800' },
        '8-10': { color: '#E64A19' },
        '11+': { color: '#CE93D8' },
      }
      return icons[this.value]
    },
  },
}
</script>

<style scoped>
.icon {
  min-width: 90px;
  height: 70px;
  position: relative;
}
.icon span {
  position: absolute;
  font-weight: 700;
  font-size: 20px;
  bottom: 6px;
}
.icon svg {
  width: 100%;
  height: 100%;
}
</style>
