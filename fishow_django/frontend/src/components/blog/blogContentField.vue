<template>
    <div class="col-md-12 fishow-content">
        <div class="form-wrap">
            <div class="fishow-blog_image__close-button"
                 @click="destroyMe">x</div>
            <textarea
                    v-model="model"
                    class="form-input"
                    :id="counter"
                    name="text"
                    placeholder="Основной текст"
            ></textarea>
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "blogContentField",
        props: ['counter','value', 'val'],
        computed: {
            model: {
                get() {
                    return this.value;
                },
                set(val) {
                    this.$emit('input', val);
                },
            },
        },
        data() {
            return {
                blog_body: ''
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