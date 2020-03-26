<template>
    <div class="col-md-12 fishow-content">
        <div class="form-wrap">
            <div class="fishow-blog_image__close-button"
                 @click="destroyMe">x</div>
            <textarea
                    v-model="urlVideo"
                    class="form-input"
                    :id="counter"
                    name="text"
                    placeholder="ссылка на видео"
            ></textarea>
            <video width="320" height="240" controls>
                <source :src="urlVideo" type="video/mp4">
            </video>
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