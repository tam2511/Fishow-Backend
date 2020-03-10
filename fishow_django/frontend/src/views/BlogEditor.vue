<template>
    <div class="container mt-2">
        <h1 class="mb-3">Create Blog</h1>
        <form @submit.prevent="onsubmit">
            <textarea
                    v-model="blog_body"
                    name="blog_body"
                    class="form-control"
                    placeholder="Write here text of your blog"
                    cols="30"
                    rows="4">
            </textarea>
            <br>
            <button
                    type="submit"
                    class="btn btn-success">
                Publish
            </button>
        </form>
        <p class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "BlogEditor",
        data() {
            return {
                blog_body: null,
                error: null
            }
        },
        methods: {
            onSubmir() {
                if (!this.blog_body) {
                    this.error = "You can't send an empty blog!"
                } else if (this.blog_body.length > 400) {
                    this.error = "To much words in your blog"
                } else {
                    let endpoint = "/api/blogs/";
                    let method = "POST";
                    apiService(endpoint, method, {content: this.blog_body})
                        .then(blog_data => {
                            this.$router.push(
                                {
                                    name: 'blog',
                                    params: { slug: blog_data.slug}
                                }
                            )
                        })
                }
            }
        },
        created() {
            document.title = 'Blog Editor - Fishow';
        }
    }
</script>

<style scoped>

</style>