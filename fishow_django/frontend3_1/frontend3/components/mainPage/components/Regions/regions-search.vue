<template>
  <div>
    <multiselect
      v-model="selected"
      :options="options"
      placeholder="Выберите регион"
      label="name"
      track-by="name"
      select-label=""
      selected-label="выбрано"
      deselect-label="удалить"
      :allow-empty="false"
    >
    </multiselect>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Object,
      required: true,
    },
    passive: {
      type: Boolean,
      default: false,
    },
    options: {
      type: Array,
      required: true,
    },
    select: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  data() {
    return {
      selected: this.value,
    }
  },
  watch: {
    value: {
      immediate: true,
      handler(val) {
        this.selected = val
      },
    },
    selected(val) {
      this.$emit('select', val)
    },
  },
}
</script>
