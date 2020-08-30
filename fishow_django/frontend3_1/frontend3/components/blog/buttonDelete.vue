<template>
  <div class="field">
    <button class="button is-danger is-outlined" @click="destroyMe">
      <span>Удалить</span>
      <span class="icon is-small">
        <i class="fas fa-times"></i>
      </span>
    </button>
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

<style scoped>
.field {
  display: flex;
  justify-content: flex-end;
}
</style>
