<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
      <div class="fishow-blog_image__close-button" @click="destroyMe">x</div>
      <textarea
        :id="counter"
        v-model="model"
        name="text"
        placeholder="Основной текст"
        class="form-input"
        cols="30"
        rows="4"
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

<style scoped>
textarea {
  min-height: 60px;
  padding: 17px 19px;
  color: #9b9b9b;
  border: 1px solid var(--backround-color-primary);
}
</style>
