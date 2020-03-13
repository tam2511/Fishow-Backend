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
<!--                        <div class="blog-post-author-quote">-->
<!--                            <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute</p>-->
<!--                        </div>-->
<!--                        <div class="blog-post-share">-->
<!--                            <p>Share this post</p>-->
<!--                            <ul class="group">-->
<!--                                <li><a class="icon fa-facebook" href="#"></a></li>-->
<!--                                <li><a class="icon fa-twitter" href="#"></a></li>-->
<!--                                <li><a class="icon fa-google-plus" href="#"></a></li>-->
<!--                                <li><a class="icon fa-instagram" href="#"></a></li>-->
<!--                            </ul>-->
<!--                        </div>-->
                        <div class="blog-post-content">
                            <p>{{ blog.content }}</p>
                            <!-- Quote Default-->
<!--                            <article class="quote-default">-->
<!--                                <div class="quote-default-text">-->
<!--                                    <p class="q">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore</p>-->
<!--                                </div>-->
<!--                            </article>-->
<!--                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint</p>-->
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
                                />
                                <CreateComment/>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
</template>

<script>
    import { apiService } from "../common/api.service";
    import Comment from "../components/Comment.vue";
    import CreateComment from "../components/CreateComment";
    export default {
        name: "Blog",
        components: {CreateComment, Comment},
        props: {
            slug: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                blog: {},
                next: null,
                comments: [],
                loadingAnswers: false
            }
        },
        methods: {
            setPageTitle(title) {
                document.title = title;
            },
            getBlogData() {
                let endpoint = `/api/blogs/${this.slug}/`;
                apiService(endpoint).then(data => {
                    this.blog = data;
                    this.setPageTitle(data.title);
                })
            },
            getCommentData() {
                console.log(this.slug);
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
            }
        },
        created() {
            this.getBlogData();
            this.getCommentData();
        }
    }
</script>

<style scoped>

</style>