<template>
  <div class="icon-pogoda">
    <span>
      {{ data }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'Temperatura',
  props: {
    data: {
      type: String,
      required: true,
    },
  },
  computed: {},
}
</script>

<style scoped lang="scss">
.icon-pogoda {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: baseline;
  justify-content: center;
  text-align: center;
  position: relative;
  span {
    position: absolute;
  }
}
</style>
