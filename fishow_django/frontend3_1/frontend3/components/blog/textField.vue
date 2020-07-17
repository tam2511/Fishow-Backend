<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
      <textarea
        :id="counter"
        name="blog_body"
        class="form-input"
        placeholder="Заголовок"
        cols="30"
        rows="4"
      >
      </textarea>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextField',
  props: {
    counter: {
      type: Number,
      required: true,
    },
  },
}
</script>

<style scoped></style>
