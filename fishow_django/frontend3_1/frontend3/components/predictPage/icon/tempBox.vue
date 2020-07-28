<template>
  <svg
    width="55"
    :height="radius * 2"
    :viewBox="'0 0 55 ' + radius * 2"
    fill="none"
    :class="{ up: up, down: !up }"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect width="55" :height="radius * 2" />
  </svg>
  <!--  <svg-->
  <!--    width="55"-->
  <!--    height="35"-->
  <!--    viewBox="0 0 55 35"-->
  <!--    fill="none"-->
  <!--    xmlns="http://www.w3.org/2000/svg"-->
  <!--  >-->
  <!--    <rect-->
  <!--      x="55"-->
  <!--      y="35"-->
  <!--      width="55"-->
  <!--      height="35"-->
  <!--      transform="rotate(-180 55 35)"-->
  <!--      fill="#9BB0F9"-->
  <!--    />-->
  <!--  </svg>-->
</template>

<script>
export default {
  props: {
    up: {
      type: Boolean,
      default: true,
    },
    radius: {
      type: String,
      default: '50',
    },
  },
  computed: {
    width() {
      return this.radius * 1.5
    },
  },
}
</script>

<style scoped>
.up {
  fill: #b0e2e5;
}
.down {
  fill: #a6cad0;
}
/*'#17b1bd', '#172a3b'*/
</style>
