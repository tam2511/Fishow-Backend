<template>
    <!--    <div class="container mt-2">-->
    <!--        <h1 class="mb-3">Create Blog</h1>-->
    <!--        <form @submit.prevent="onsubmit">-->
    <!--            <textarea-->
    <!--                    v-model="blog_body"-->
    <!--                    name="blog_body"-->
    <!--                    class="form-control"-->
    <!--                    placeholder="Write here text of your blog"-->
    <!--                    cols="30"-->
    <!--                    rows="4">-->
    <!--            </textarea>-->
    <!--            <br>-->
    <!--            <button-->
    <!--                    type="submit"-->
    <!--                    class="btn btn-success">-->
    <!--                Publish-->
    <!--            </button>-->
    <!--        </form>-->
    <!--        <p class="muted mt-2">{{ error }}</p>-->
    <section class="section section-variant-1 bg-gray-100">
        <div class="container">
            <div class="row row-50">
                <div class="col-lg-7 col-xl-8">
                    <!-- Heading Component-->
                    <article class="heading-component">
                        <div class="heading-component-inner">
                            <h5 class="heading-component-title">Написать блог</h5>
                        </div>
                    </article>
                    <form @submit.prevent="onSubmit">
                        <div class="row row-10 row-narrow">
                            <div class="col-md-12 fishow-content_container">
                                <div class="col-md-12 fishow-content">
                                    <div class="form-wrap">
                                        <textarea
                                                v-model="blog_body"
                                                name="blog_body"
                                                class="form-control"
                                                placeholder="Write here text of your blog"
                                                cols="30"
                                                rows="4">
                                        </textarea>
                                    </div>
                                </div>
                                <div class="col-md-12 fishow-content">
                                    <div class="form-wrap">
                                        <div class="fishow-blog_image__close-button">x</div>
                                        <label class="form-label" for="form-text">Текст</label
                                        ><textarea
                                            class="form-input"
                                            id="form-text"
                                            name="text"
                                    ></textarea>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 fishow_container">
                                <div class="fishow_button_text">
                                    <div class="fishow_action_btn">Текст</div>
                                </div>
                                <div class="fishow_button_video">
                                    <div class="fishow_action_btn">Видео</div>
                                </div>
                                <div class="fishow_button_picture">
                                    <input
                                            class="form-input"
                                            id="fishow-picture1"
                                            type="file"
                                            name="picture"
                                    />
                                    <button class="fishow_action_btn"
                                            type="button">Картинка</button>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <button
                                    class="button button-lg button-google button-block"
                                    type="submit"
                                    name="send_blog"
                            >
                                Опубликовать
                            </button>
                            <button
                                type="submit"
                                class="btn btn-success">
                                Publish
                            </button>
                        </div>
                        <div class="col-md-12">
                            <button
                                    class="button button-lg button-primary button-block"
                                    type="submit"
                                    name="save_blog"
                                    onclick=""
                            >
                                Сохранить как черновик
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
    <!--    </div>-->
</template>

<script>
    import {apiService} from "../common/api.service.js";

    export default {
        name: "BlogEditor",
        props: {
            slug: {
                type: String,
                required: false
            }
        },
        data() {
            return {
                blog_body: null,
                error: null
            }
        },
        methods: {
            onSubmit() {
                if (!this.blog_body) {
                    this.error = "You can't send an empty blog!"
                } else if (this.blog_body.length > 400) {
                    this.error = "To much words in your blog"
                } else {
                    let endpoint = "/api/blogs/";
                    let method = "POST";
                    if (this.slug !== undefined) {
                        endpoint += `${ this.slug }/`;
                        method = "PUT";
                    }
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
        async beforeRouteEnter(to, from, next) {
            // if the component will be used to update a question, then get the question's data from the REST API
            if (to.params.slug !== undefined) {
                let endpoint = `/api/blogs/${ to.params.slug }/`;
                let data = await apiService(endpoint);
                return next(vm => (vm.blog_body = data.content))
            } else {
                return next();
            }
        },
        created() {
            document.title = 'Blog Editor - Fishow';
        }
    }
</script>

<style scoped>

</style>