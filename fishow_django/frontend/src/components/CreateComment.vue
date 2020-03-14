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
            <form @submit.prevent="onSubmit" class="comment-box-form" >
                <div class="form-wrap">
                    <textarea
                            v-model="commentBody"
                            class="form-input"
                            id="comment-message"
                            name="message"
                            placeholder="Ваш комментарий"
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
            id: {
                type: Number,
                required: true
            },
            slug: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                blogSlug: null,
                commentBody: null,
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
                // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
                console.log('${this.slug} = ', this.blogSlug);
                if (this.commentBody) {
                    console.log('${this.slug} = ', this.slug);
                    let endpoint = `/api/blogs/${this.slug}/comment/`;
                    apiService(endpoint, "POST", { body: this.commentBody })
                        .then(data => {
                            this.comments.unshift(data)
                        })
                    this.commentBody = null;
                    this.showForm = false;
                    // this.userHasAnswered = true;
                    if (this.error) {
                        this.error = null;
                    }
                } else {
                    this.error = "You can't send an empty answer!";
                }
            }
        },
        async beforeRouteEnter(to, from, next) {
            // get the answer's data from the REST API and set two data properties for the component
            let endpoint = `/api/comments/${to.params.id}/`;
            let data = await apiService(endpoint);
            return next(vm => (
                vm.commentBody = data.body,
                vm.blogSlug = data.blog_slug
            ));
        },
        created() {
            this.getUserName();
        }
    };
</script>

<style scoped></style>
