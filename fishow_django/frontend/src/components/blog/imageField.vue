<template>
    <div class="col-md-12 fishow-content">
        <div class="form-wrap">
            <div class="fishow-blog_image__close-button"
                @click="destroyMe">x</div>
            <textarea
                    name="blog_body"
                    class="form-input"
                    v-model="image"
                    :id="counter"
                    placeholder="Например: https://peach.blender.org/wp-content/uploads/bbb-splash.png?x10518"
                    cols="30"
                    rows="4"
                    >
            </textarea>
            <img :src="image" width="500" height="500">
        </div>
    </div>
</template>

<script>
    export default {
        name: "imageField",
        props: ['counter'],
        data() {
            return {
                image: ''
            }
        },
        methods: {
            destroyMe() {
                this.$el.remove()
            }
        }
    }
</script>

<style scoped lang="scss">


</style>