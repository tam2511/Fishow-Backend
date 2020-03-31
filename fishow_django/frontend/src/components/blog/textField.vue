<template>
    <div class="col-md-12 fishow-content">
        <div class="form-wrap">
                                        <textarea
                                                name="blog_body"
                                                class="form-input"
                                                :id="counter"
                                                placeholder="Заголовок"
                                                cols="30"
                                                rows="4">
                                        </textarea>

        </div>
    </div>
</template>

<script>
export default {
  name: 'textField',
  props: ['counter']
}
</script>

<style scoped>

</style>
