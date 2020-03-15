<template>
    <section class="section section-sm bg-gray-100">
        <div class="container">
            <div class="row row-30">
                <div class="col-lg-8">
                    <div class="blog-post">
                        <!-- Badge-->
                        <div class="badge badge-secondary">The Team
                        </div>
                        <h3 class="blog-post-title">{{ blog.title }}</h3>
                        <div class="blog-post-header">
                            <div class="blog-post-author"><img class="img-circle" src="images/user-3-63x63.jpg" alt="" width="63" height="63"/>
                                <p class="post-author">{{ blog.author }}</p>
                            </div>
                            <div class="blog-post-meta">
                                <time class="blog-post-time" datetime="2018"><span class="icon mdi mdi-clock"></span>{{ blog.created_at }}</time>
                                <div class="blog-post-comment"><span class="icon mdi mdi-comment-outline"></span>{{ blog.comments_count}}</div>
                                <div class="blog-post-view"><span class="icon fl-justicons-visible6"></span>0</div>
                            </div>
                        </div>
                        <div class="blog-post-content">
                            <p>{{ blog.content }}</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <!-- Heading Component-->
                            <article class="heading-component">
                                <div class="heading-component-inner">
                                    <h5 class="heading-component-title">{{blog.comments_count}} комментариев
                                    </h5>
                                </div>
                            </article>

                            <div class="blog-post-comments">
                                <!-- Post Comment-->
                                <Comment
                                    v-for="(comment, index) in comments"
                                    :comment="comment"
                                    :key="index"
                                    :slug="slug"
                                    :requestUser="requestUser"
                                    @deleteComment="deleteComment"
                                />
                                <CreateComment
                                    :slug="slug"
                                    :id="id"
                                    :requestUser="requestUser"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import {apiService} from "@/common/api.service";
    import Comment from "@/components/Comment.vue";
    import CreateComment from "@/components/CreateComment";

    export default {
        name: "Blog",
        components: {CreateComment, Comment},
        props: {
            slug: {
                type: String,
                default: null,
                required: true
            }
        },
        data() {
            return {
                blog: {},
                id: 0,
                next: null,
                comments: [],
                newCommentBody: null,
                error: null,
                loadingAnswers: false,
                requestUser: null
            }
        },
        methods: {
            setPageTitle(title) {
                document.title = title;
            },
            getUser() {
                this.requestUser = window.localStorage.getItem("username");
            },
            getBlogData() {
                let endpoint = `/api/blogs/${this.slug}/`;
                apiService(endpoint).then(data => {
                    this.blog = data;
                    this.id = data.id;
                    console.log(this.id);
                    this.setPageTitle(data.title);
                })
            },
            getCommentData() {
                let endpoint = `/api/blogs/${this.slug}/comments/`;
                if (this.next) {
                    endpoint = this.next;
                }
                apiService(endpoint).then(data => {
                    this.comments.push(...data.results);
                    this.loadingAnswers = false;
                    if (data.next) {
                        this.next = data.next;
                    } else {
                        this.next = null;
                    }
                })
            },
            async deleteComment(comment) {
                // delete a given answer from the answers array and make a delete request to the REST API
                let endpoint = `/api/comments/${comment.id}/`;
                try {
                    await apiService(endpoint, "DELETE")
                    this.$delete(this.comments, this.comments.indexOf(comment))
                    this.userHasAnswered = false;
                }
                catch (err) {
                    console.log(err)
                }
            },
        },

        created() {
            this.getBlogData();
            this.getCommentData();
            this.getUser();
        }
    }
</script>

<style scoped>

</style>