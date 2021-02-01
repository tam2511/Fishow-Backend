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
    passive: {
      type: Boolean,
      default: false,
    },
    options: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      selected: this.value || null,
    }
  },
  watch: {
    value(val) {
      this.selected = val
    },
    selected(val) {
      this.$emit('select', val)
    },
  },
}
</script>
