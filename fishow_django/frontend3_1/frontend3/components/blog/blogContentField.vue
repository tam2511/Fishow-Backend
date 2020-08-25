<template>
  <div class="field">
    <label class="label">Текст</label>
    <div class="control">
      <button-delete @destoy="destroyMe" />

      <textarea
        :id="counter"
        v-model="model"
        name="text"
        class="textarea"
        placeholder="Textarea"
      ></textarea>
      <slot></slot>
    </div>
  </div>
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
      // required: true
      default: '',
    },
    val: {
      type: String,
      // required: true,
      default: '',
    },
  },
  data() {
    return {
      blog_body: '',
    }
  },
  computed: {
    model: {
      get() {
        return this.value
      },
      set(val) {
        this.$emit('input', val)
      },
    },
  },
  methods: {
    destroyMe() {
      this.$el.remove()
    },
  },
}
</script>

<style scoped></style>
