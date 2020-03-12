<template>
    <div class="post-comment">
        <div class="post-comment-aside"><img class="img-circle" src="images/user-6-69x69.jpg" alt="" width="69" height="69"/>
        </div>
        <div class="post-comment-main">
            <div class="post-comment-header">
                <h5 class="author-name">{{ comment.author }}</h5>
                <time class="post-comment-time" datetime="2018">{{ comment.created_at }}
                </time>
            </div>
            <div class="post-comment-text">
                <p>{{ comment.body }}</p>
            </div>
            <div class="post-comment-footer">
                <div class="comment-like"><span class="icon mdi mdi-thumb-up-outline"></span><a href="#">32</a></div>
                <div class="comment-reply"><span class="icon mdi mdi-comment-outline"></span><a href="#">Reply</a></div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Comment",
        props: {
            comment: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>