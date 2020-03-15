<template>
    <div class="list-post-minimal">
        <!-- Post Minimal-->
        <article class="post-minimal">
            <div class="post-classic-main">
                <p class="post-classic-title">
                    <a href="#"> Hot_blog.title </a>
                </p>
                <div class="post-minimal_comments">
                    <div class="badge badge-primary">Категория</div>
                    <div class="post-corporate-author">Имя автора тут</div>
                    <time class="post-classic-time">
                        <!--                                                     Hot_blog.data_add|date:'d.m.Y' -->
                    </time>
                </div>
            </div>
        </article>
    </div>
</template>

<script>
    export default {
        name: "HotPostMinimal",
        props: {

        }
    }
</script>

<style scoped>

</style>