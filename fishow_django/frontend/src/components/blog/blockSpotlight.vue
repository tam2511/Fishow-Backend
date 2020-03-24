<template>
    <div class="block-aside-item">
        <!-- Heading Component-->
        <article class="heading-component">
            <div class="heading-component-inner">
                <h5 class="heading-component-title">In The Spotlight
                </h5><router-link class="button button-xs button-gray-outline" to="/" >Все новости</router-link>
            </div>
        </article>

        <!-- List Post Classic-->
        <div class="list-post-classic">
            <!-- Post Classic-->
            <article class="post-classic">
                <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-1-94x94.jpg" alt="" width="94" height="94"/></a></div>
                <div class="post-classic-main">
                    <p class="post-classic-title"><a href="blog-post.html">Raheem Sterling turns the tide for Manchester</a></p>
                    <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>
                        <time datetime="2018">April 15, 2018</time>
                    </div>
                </div>
            </article>
            <!-- Post Classic-->
            <article class="post-classic">
                <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-2-94x94.jpg" alt="" width="94" height="94"/></a></div>
                <div class="post-classic-main">
                    <p class="post-classic-title"><a href="blog-post.html">Prem in 90 seconds: Chelsea's crisis is over!</a></p>
                    <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>
                        <time datetime="2018">April 15, 2018</time>
                    </div>
                </div>
            </article>
            <!-- Post Classic-->
            <article class="post-classic">
                <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-3-94x94.jpg" alt="" width="94" height="94"/></a></div>
                <div class="post-classic-main">
                    <p class="post-classic-title"><a href="blog-post.html">Good vibes back at struggling Schalke</a></p>
                    <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>
                        <time datetime="2018">April 15, 2018</time>
                    </div>
                </div>
            </article>
            <!-- Post Classic-->
            <article class="post-classic">
                <div class="post-classic-aside"><a class="post-classic-figure" href="blog-post.html"><img src="images/blog-element-4-94x94.jpg" alt="" width="94" height="94"/></a></div>
                <div class="post-classic-main">
                    <p class="post-classic-title"><a href="blog-post.html">Liverpool in desperate need of backup players</a></p>
                    <div class="post-classic-time"><span class="icon mdi mdi-clock"></span>
                        <time datetime="2018">April 15, 2018</time>
                    </div>
                </div>
            </article>
        </div>
    </div>
</template>

<script>
    export default {
        name: "blockSpotlight"
    }
</script>

<style scoped>

</style>