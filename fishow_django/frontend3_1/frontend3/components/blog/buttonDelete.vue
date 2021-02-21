<template>
  <div class="field">
    <button class="remove-button" @click="destroyMe"></button>
  </div>
</template>

<script>
export default {
  methods: {
    destroyMe() {
      this.$emit('destoy')
    },
  },
}
</script>

<style lang="scss" scoped>
.field {
  position: absolute;
  right: 0;
  top: 0;
  display: flex;
  height: 100%;
  justify-content: flex-end;
}
.remove-button {
  height: 100%;
  width: 30px;
  transition: 0.5s;
  padding: 0;
  margin: 0;
  border: 0;
  cursor: pointer;
  background-color: rgb(224, 170, 170);
  z-index: 1000;
  &:hover {
    background-color: rgb(246, 95, 95);
  }
}
</style>
