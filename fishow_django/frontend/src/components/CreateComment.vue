<template>
    <div class="comment-box">
        <div class="comment-box-aside">
            <img
                    class="img-circle"
                    src="images/user-7-69x69.jpg"
                    alt=""
                    width="69"
                    height="69"
            />
        </div>
        <div class="comment-box-main">
            <h5 class="comment-box-name">{{ userName }}</h5>
            <!-- RD Mailform-->
            <form class="rd-mailform comment-box-form" @submit.prevent="onSubmit">
                <div class="form-wrap">
                    <label class="form-label" for="comment-message">Your comment</label>
                    <textarea
                            v-model="comment_body"
                            class="form-input"
                            id="comment-message"
                            name="message"
                    ></textarea>
                </div>
                <div class="form-button">
                    <button class="button button-primary" type="submit">Submit</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import { apiService } from "../common/api.service";

    export default {
        name: "CreateComment",
        props: {
            slug: {
                type: String,
                required: false
            }
        },
        data() {
            return {
                comment_body: null,
                userName: "",
                error: null
            };
        },
        methods: {
            getUserName() {
                let endpoint = `/api/user/`;
                apiService(endpoint).then(data => {
                    this.userName = data.username;
                });
            },
            onSubmit() {
                if (!this.comment_body) {
                    this.error = "You can't send an empty blog!";
                } else if (this.comment_body.length > 400) {
                    this.error = "To much words in your blog";
                } else {
                    let endpoint = `/api/blogs/${this.slug}/comment/`;
                    let method = "POST";
                    if (this.slug !== undefined) {
                        endpoint += `${this.slug}/`;
                        method = "PUT";
                    }
                    apiService(endpoint, method, { body: this.comment_body }).then(
                        comment_data => {
                            this.$router.push({
                                name: "blog",
                                params: { slug: comment_data.slug }
                            });
                        }
                    );
                }
            }
        },
        created() {
            this.getUserName();
        }
    };
</script>

<style scoped></style>
