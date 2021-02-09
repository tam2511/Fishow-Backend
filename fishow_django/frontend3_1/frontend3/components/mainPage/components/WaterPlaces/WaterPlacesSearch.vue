<template>
  <div>
    <multiselect
      v-model="selected"
      :options="waterPlaces"
      placeholder="Начните вводить название"
      label="name"
      track-by="name"
      select-label=""
      selected-label="выбрано"
      deselect-label="удалить"
      :searchable="true"
      :loading="isLoading"
      @search-change="search"
    >
    </multiselect>
  </div>
</template>

<script>
export default {
  name: 'WaterPlacesSearch',
  data() {
    return {
      selected: null,
      waterPlaces: [],
      isLoading: false,
    }
  },
  watch: {
    selected(val) {
      this.$emit('selected', val)
    },
  },
  methods: {
    search(val) {
      this.$nextTick(() => {
        this.isLoading = true
        this.$axios
          .get(`/waterplace_nature/?search=${val}`)
          .then(({ data }) => {
            this.waterPlaces = data.results
          })
        this.isLoading = false
      })
    },
  },
}
</script>
