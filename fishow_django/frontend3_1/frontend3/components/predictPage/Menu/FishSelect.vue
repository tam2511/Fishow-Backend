<template>
  <b-field>
    <multiselect
      v-model="selected"
      :options="fishList"
      placeholder="Выберите рыбу"
      label="title"
      track-by="title"
      select-label=""
      @input="info"
    ></multiselect>
  </b-field>
</template>

<script>
import fishList from '~/assets/data/fishList'
export default {
  name: 'FishSelect',
  props: {
    options: {
      type: [Array, Object],
      default() {
        return fishList
      },
    },
  },
  data() {
    return {
      fishList: this.options,
      selected: {
        image: '/fish_green/щука.jpg',
        title: 'щука',
      },
    }
  },
  methods: {
    info(value) {
      this.selected = value
      this.$emit('select', value.title)
    },
  },
}
</script>

<style scoped></style>
