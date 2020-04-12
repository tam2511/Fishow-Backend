<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
      <div class="fishow-blog_image__close-button" @click="destroyMe">x</div>
      <autosize-textarea
        v-model="model"
        :id="counter"
        name="text"
        placeholder="Основной текст"
      ></autosize-textarea>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'blogContentField',
  props: ['counter', 'value', 'val'],
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
  data() {
    return {
      blog_body: '',
    }
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
  border: 1px solid #e1e1e1;
}
</style>
