<template>
  <div class="field">
    <label class="label">Message</label>
    <div class="control">
      <div class="field">
        <button class="button is-danger is-outlined" @click="destroyMe">
          <span>Delete</span>
          <span class="icon is-small">
            <i class="fas fa-times"></i>
          </span>
        </button>
      </div>

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
export default {
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
