<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
      <div class="fishow-blog_image__close-button" @click="destroyMe">x</div>
      <textarea
        :id="counter"
        v-model="image"
        name="image"
        class="form-input"
        placeholder="Например: https://peach.blender.org/wp-content/uploads/bbb-splash.png?x10518"
        cols="30"
        rows="4"
      >
      </textarea>
      <img :src="image" width="500" height="500" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageField',
  props: {
    counter: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      image: '',
    }
  },
  methods: {
    destroyMe() {
      this.$el.remove()
    },
  },
}
</script>

<style scoped lang="scss"></style>
