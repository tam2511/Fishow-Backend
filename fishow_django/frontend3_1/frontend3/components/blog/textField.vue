<template>
  <b-field style="position: relative">
    <b-input
      :id="counter"
      v-model="model"
      maxlength="200"
      type="textarea"
      placeholder="Введите текст"
      :has-counter="false"
      style="width: 100%; resize: none"
    >
    </b-input>
    <button-delete @destoy="destroyMe" />
  </b-field>
</template>

<script>
import ButtonDelete from '~/components/blog/buttonDelete'
export default {
  components: { ButtonDelete },
  props: {
    counter: {
      type: String,
      required: true,
    },
    value: {
      type: String,
      default: '',
    },
    val: {
      type: String,
      default: '',
    },
  },
  computed: {
    model: {
      get() {
        return this.value
      },
      set(val) {
        const body = {
          type: 'text',
          body: val,
          name: this.counter,
        }
        this.$emit('input', body)
      },
    },
  },
  methods: {
    destroyMe() {
      this.$emit('remove', this.counter)
      this.$el.remove()
    },
  },
}
</script>

<style lang="scss" scoped></style>
