<template>
    <div class="list-post-minimal">
        <!-- Post Minimal-->
        <article class="post-minimal">
            <div class="post-classic-main">
                <p class="post-classic-title">
                    <router-link :to="{ name: 'blog', params: { slug: slug } }"> {{ title }} </router-link>
                </p>
                <div class="post-minimal_comments">
                    <div class="badge badge-primary">Категория</div>
                    <div class="post-corporate-author"> Автор: {{author}} </div>
                    <time class="post-classic-time">
                        {{ time }}
                    </time>
                </div>
            </div>
        </article>
    </div>
</template>

<script>
    export default {
        name: "HotPostMinimal",
        props: ['title','author','content','time','slug'],
    }
</script>

<style scoped>

</style>