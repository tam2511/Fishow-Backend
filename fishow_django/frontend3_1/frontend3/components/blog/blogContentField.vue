<template>
  <div class="field">
    <label class="label">Message</label>
    <div class="control">
      <a class="delete" @click="destroyMe"></a>
      <textarea
        class="textarea"
        :id="counter"
        v-model="model"
        placeholder="Textarea"
      ></textarea>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogContentField',
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
