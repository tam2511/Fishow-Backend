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
<!--                                <div class="post-comment post-comment-parent">-->
<!--                                    <div class="post-comment-aside"><img class="img-circle" src="images/user-4-69x69.jpg" alt="" width="69" height="69"/>-->
<!--                                    </div>-->
<!--                                    <div class="post-comment-main">-->
<!--                                        <div class="post-comment-header">-->
<!--                                            <h5 class="author-name">Linda Peterson</h5>-->
<!--                                            <time class="post-comment-time" datetime="2018">2 days ago-->
<!--                                            </time>-->
<!--                                        </div>-->
<!--                                        <div class="post-comment-text">-->
<!--                                            <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim</p>-->
<!--                                        </div>-->
<!--                                        <div class="post-comment-footer">-->
<!--                                            <div class="comment-like"><span class="icon mdi mdi-thumb-up-outline"></span><a href="#">32</a></div>-->
<!--                                            <div class="comment-reply"><span class="icon mdi mdi-comment-outline"></span><a href="#">Reply</a></div>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                                &lt;!&ndash; Post Comment&ndash;&gt;-->
<!--                                <div class="post-comment post-comment-child">-->
<!--                                    <div class="post-comment-aside"><img class="img-circle" src="images/user-5-69x69.jpg" alt="" width="69" height="69"/>-->
<!--                                    </div>-->
<!--                                    <div class="post-comment-main">-->
<!--                                        <div class="post-comment-header">-->
<!--                                            <h5 class="author-name">Erika Wood</h5>-->
<!--                                            <time class="post-comment-time" datetime="2018">2 days ago-->
<!--                                            </time>-->
<!--                                        </div>-->
<!--                                        <div class="post-comment-text">-->
<!--                                            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est</p>-->
<!--                                        </div>-->
<!--                                        <div class="post-comment-footer">-->
<!--                                            <div class="comment-like"><span class="icon mdi mdi-thumb-up-outline"></span><a href="#">32</a></div>-->
<!--                                            <div class="comment-reply"><span class="icon mdi mdi-comment-outline"></span><a href="#">Reply</a></div>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </div>-->
                                <!-- Post Comment-->
                                <div class="post-comment">
                                    <div class="post-comment-aside"><img class="img-circle" src="images/user-6-69x69.jpg" alt="" width="69" height="69"/>
                                    </div>
                                    <div class="post-comment-main">
                                        <div class="post-comment-header">
                                            <h5 class="author-name">Erik Peterson</h5>
                                            <time class="post-comment-time" datetime="2018">2 days ago
                                            </time>
                                        </div>
                                        <div class="post-comment-text">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim</p>
                                        </div>
                                        <div class="post-comment-footer">
                                            <div class="comment-like"><span class="icon mdi mdi-thumb-up-outline"></span><a href="#">32</a></div>
                                            <div class="comment-reply"><span class="icon mdi mdi-comment-outline"></span><a href="#">Reply</a></div>
                                        </div>
                                    </div>
                                </div>
                                <div class="comment-box">
                                    <div class="comment-box-aside"><img class="img-circle" src="images/user-7-69x69.jpg" alt="" width="69" height="69"/>
                                    </div>
                                    <div class="comment-box-main">
                                        <h5 class="comment-box-name">Miranda</h5>
                                        <!-- RD Mailform-->
                                        <form class="rd-mailform comment-box-form" data-form-output="form-output-global" data-form-type="contact" method="post" action="bat/rd-mailform.php">
                                            <div class="form-wrap">
                                                <label class="form-label" for="comment-message">Your comment</label>
                                                <textarea class="form-input" id="comment-message" name="message" data-constraints="@Required"></textarea>
                                            </div>
                                            <div class="form-button">
                                                <button class="button button-primary" type="submit">Submit</button>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
<!--                <div class="col-lg-4">-->
<!--                    &lt;!&ndash; Blog Alide&ndash;&gt;-->
<!--                    <div class="block-aside">-->
<!--                        <div class="block-aside-item">-->
<!--                            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--                            <article class="heading-component">-->
<!--                                <div class="heading-component-inner">-->
<!--                                    <h5 class="heading-component-title">Categories-->
<!--                                    </h5>-->
<!--                                </div>-->
<!--                            </article>-->

<!--                            &lt;!&ndash;Block Categories&ndash;&gt;-->
<!--                            <div class="block-categories">-->
<!--                                <ul class="list-marked list-marked-categories">-->
<!--                                    <li><a href="#">Basketball</a><span class="list-marked-counter">68</span></li>-->
<!--                                    <li><a href="#">The Team</a><span class="list-marked-counter">16</span></li>-->
<!--                                    <li><a href="#">League</a><span class="list-marked-counter">20</span></li>-->
<!--                                </ul>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="block-aside-item">-->
<!--                            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--                            <article class="heading-component">-->
<!--                                <div class="heading-component-inner">-->
<!--                                    <h5 class="heading-component-title">In The Spotlight-->
<!--                                    </h5><a class="button button-xs button-gray-outline" href="news.html">All News</a>-->
<!--                                </div>-->
<!--                            </article>-->

<!--                            &lt;!&ndash; List Post Classic&ndash;&gt;-->
<!--                            <div class="list-post-classic">-->
<!--                                &lt;!&ndash; Post Classic&ndash;&gt;-->
<!--                                <article class="post-classic">-->
<!--                                    <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-1-94x94.jpg" alt="" width="94" height="94"/></a></div>-->
<!--                                    <div class="post-classic-main">-->
<!--                                        <p class="post-classic-title"><a href="blog-post.html">Raheem Sterling turns the tide for Manchester</a></p>-->
<!--                                        <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>-->
<!--                                            <time datetime="2018">April 15, 2018</time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </article>-->
<!--                                &lt;!&ndash; Post Classic&ndash;&gt;-->
<!--                                <article class="post-classic">-->
<!--                                    <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-2-94x94.jpg" alt="" width="94" height="94"/></a></div>-->
<!--                                    <div class="post-classic-main">-->
<!--                                        <p class="post-classic-title"><a href="blog-post.html">Prem in 90 seconds: Chelsea's crisis is over!</a></p>-->
<!--                                        <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>-->
<!--                                            <time datetime="2018">April 15, 2018</time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </article>-->
<!--                                &lt;!&ndash; Post Classic&ndash;&gt;-->
<!--                                <article class="post-classic">-->
<!--                                    <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-3-94x94.jpg" alt="" width="94" height="94"/></a></div>-->
<!--                                    <div class="post-classic-main">-->
<!--                                        <p class="post-classic-title"><a href="blog-post.html">Good vibes back at struggling Schalke</a></p>-->
<!--                                        <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>-->
<!--                                            <time datetime="2018">April 15, 2018</time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </article>-->
<!--                                &lt;!&ndash; Post Classic&ndash;&gt;-->
<!--                                <article class="post-classic">-->
<!--                                    <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-4-94x94.jpg" alt="" width="94" height="94"/></a></div>-->
<!--                                    <div class="post-classic-main">-->
<!--                                        <p class="post-classic-title"><a href="blog-post.html">Liverpool in desperate need of backup players</a></p>-->
<!--                                        <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>-->
<!--                                            <time datetime="2018">April 15, 2018</time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </article>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="block-aside-item">-->
<!--                            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--                            <article class="heading-component">-->
<!--                                <div class="heading-component-inner">-->
<!--                                    <h5 class="heading-component-title">Latest Comments-->
<!--                                    </h5>-->
<!--                                </div>-->
<!--                            </article>-->

<!--                            &lt;!&ndash; List Comments Classic&ndash;&gt;-->
<!--                            <div class="list-comments-classic">-->
<!--                                &lt;!&ndash; Comment Classic&ndash;&gt;-->
<!--                                <div class="comment-classic">-->
<!--                                    <svg version="1.1" x="0px" y="0px" width="6.888px" height="4.68px" viewbox="0 0 6.888 4.68" enable-background="new 0 0 6.888 4.68" xml:space="preserve">-->
<!--                                          <path fill="#171617" d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"></path>-->
<!--                                        </svg>-->
<!--                                    <div class="comment-classic-header">-->
<!--                                        <div class="comment-classic-header-aside"><img src="images/user-1-63x63.jpg" alt="" width="63" height="63"/>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-header-main">-->
<!--                                            <p class="comment-classic-title">Amanda Norton</p>-->
<!--                                            <time class="comment-classic-time" datetime="2018">4 hours ago-->
<!--                                            </time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                    <div class="comment-classic-body">-->
<!--                                        <div class="comment-classic-text">-->
<!--                                            <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit</p>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-post-title"><a href="blog-post.html">WHICH TEAM WILL WIN THE WORLD CHAMPIONSHIP SERIES?</a></div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                                &lt;!&ndash; Comment Classic&ndash;&gt;-->
<!--                                <div class="comment-classic">-->
<!--                                    <svg version="1.1" x="0px" y="0px" width="6.888px" height="4.68px" viewbox="0 0 6.888 4.68" enable-background="new 0 0 6.888 4.68" xml:space="preserve">-->
<!--                                          <path fill="#171617" d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"></path>-->
<!--                                        </svg>-->
<!--                                    <div class="comment-classic-header">-->
<!--                                        <div class="comment-classic-header-aside"><img src="images/user-2-63x63.jpg" alt="" width="63" height="63"/>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-header-main">-->
<!--                                            <p class="comment-classic-title">Robert Norton</p>-->
<!--                                            <time class="comment-classic-time" datetime="2018">14 hours ago-->
<!--                                            </time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                    <div class="comment-classic-body">-->
<!--                                        <div class="comment-classic-text">-->
<!--                                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-post-title"><a href="blog-post.html">SIX BIG QUESTIONS FOR THE SPURS-ROCKETS HEAVYWEIGHT</a></div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                                &lt;!&ndash; Comment Classic&ndash;&gt;-->
<!--                                <div class="comment-classic">-->
<!--                                    <svg version="1.1" x="0px" y="0px" width="6.888px" height="4.68px" viewbox="0 0 6.888 4.68" enable-background="new 0 0 6.888 4.68" xml:space="preserve">-->
<!--                                          <path fill="#171617" d="M1.584,0h1.8L2.112,4.68H0L1.584,0z M5.112,0h1.776L5.64,4.68H3.528L5.112,0z"></path>-->
<!--                                        </svg>-->
<!--                                    <div class="comment-classic-header">-->
<!--                                        <div class="comment-classic-header-aside"><img src="images/user-3-63x63.jpg" alt="" width="63" height="63"/>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-header-main">-->
<!--                                            <p class="comment-classic-title">Rebecca Smith</p>-->
<!--                                            <time class="comment-classic-time" datetime="2018">20 hours ago-->
<!--                                            </time>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                    <div class="comment-classic-body">-->
<!--                                        <div class="comment-classic-text">-->
<!--                                            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat</p>-->
<!--                                        </div>-->
<!--                                        <div class="comment-classic-post-title"><a href="blog-post.html">VOTE: PICK THE WINNERS IN THE NBA CONFERENCE SEMIFINALS</a></div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="block-aside-item">-->
<!--                            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--                            <article class="heading-component">-->
<!--                                <div class="heading-component-inner">-->
<!--                                    <h5 class="heading-component-title">Join Our Newsletter-->
<!--                                    </h5>-->
<!--                                </div>-->
<!--                            </article>-->

<!--                            &lt;!&ndash; Mail Form Modern&ndash;&gt;-->
<!--                            <form class="rd-mailform rd-mailform-modern" data-form-output="form-output-global" data-form-type="subscribe" method="post" action="bat/rd-mailform.php">-->
<!--                                <div class="form-wrap">-->
<!--                                    <label class="form-label" for="subscribe-email">Enter Your E-mail</label>-->
<!--                                    <input class="form-input" id="subscribe-email" type="email" name="email" data-constraints="@Email @Required">-->
<!--                                </div>-->
<!--                                <div class="form-wrap">-->
<!--                                    <button class="button button-block button-primary" type="submit">Subscribe</button>-->
<!--                                </div>-->
<!--                            </form>-->
<!--                        </div>-->
<!--                        <div class="block-aside-item">-->
<!--                            &lt;!&ndash; Heading Component&ndash;&gt;-->
<!--                            <article class="heading-component">-->
<!--                                <div class="heading-component-inner">-->
<!--                                    <h5 class="heading-component-title">Tags-->
<!--                                    </h5>-->
<!--                                </div>-->
<!--                            </article>-->

<!--                            &lt;!&ndash; List Tags&ndash;&gt;-->
<!--                            <ul class="list-tags">-->
<!--                                <li><a href="#">Sport</a></li>-->
<!--                                <li><a href="#">Team</a></li>-->
<!--                                <li><a href="#">League</a></li>-->
<!--                                <li><a href="#">Cup</a></li>-->
<!--                                <li><a href="#">Basketball</a></li>-->
<!--                                <li><a href="#">Player</a></li>-->
<!--                                <li><a href="#">Championship</a></li>-->
<!--                            </ul>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
            </div>
        </div>
    </section>
</template>

<script>
    import { apiService } from "../common/api.service";
    export default {
        name: "Blog",
        props: {
            slug: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                blog: {}
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
            }
        },
        created() {
            this.getBlogData();
        }
    }
</script>

<style scoped>

</style>