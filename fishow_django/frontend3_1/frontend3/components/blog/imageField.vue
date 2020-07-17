<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
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
        v-model="image"
        name="image"
        class="textarea"
        placeholder="Например: https://peach.blender.org/wp-content/uploads/bbb-splash.png?x10518"
        cols="30"
        rows="4"
      >
      </textarea>
      <img :src="image" width="500" height="500" alt="uploaded image" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageField',
  props: {
    counter: {
      type: String,
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
