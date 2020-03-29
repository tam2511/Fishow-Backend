<template>
    <div class="col-md-12 fishow-content">
        <div class="form-wrap">
            <div class="fishow-blog_image__close-button"
                 @click="destroyMe">x</div>
            <textarea
                    v-model="urlVideo"
                    class="form-input"
                    :id="counter"
                    name="video"
                    placeholder="ссылка на видео"
            ></textarea>
            <iframe width="560" height="315" :src="urlVideo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>

    </div>

</template>

<script>
    export default {
        name: "videoField",
        props: ['counter'],
        data() {
            return {
                urlVideo: ''
            }
        },
        methods: {
            destroyMe() {
                this.$el.remove()
            }
        }
    }
</script>

<style scoped>

</style>