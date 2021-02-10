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
  mounted() {
    this.search('Волга', true)
  },
  methods: {
    search(val = 'Волга', once = false) {
      this.$nextTick(async () => {
        this.isLoading = true
        try {
          await this.$axios
            .get(`/waterplace_nature/?search=${val}`)
            .then(({ data }) => {
              this.waterPlaces = data.results
              if (once) {
                this.selected = this.waterPlaces[0]
                this.isLoading = false
              }
            })
        } catch (e) {
          console.error(e)
          this.$buefy.toast.open({
            duration: 5000,
            message: 'Что то пошло не так при загрузке водоёмов.',
            type: 'is-danger',
          })
        }
      })
    },
  },
}
</script>
