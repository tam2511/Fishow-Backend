<template>
    <div class="post-comment">
        <div class="post-comment-aside">
            <img
                    class="img-circle"
                    src="images/user-6-69x69.jpg"
                    alt=""
                    width="69"
                    height="69"
            />
        </div>
        <div class="post-comment-main">
            <div class="post-comment-header">
                <h5 class="author-name">{{ comment.author }}</h5>
                <time class="post-comment-time" datetime="2018">{{
                    comment.created_at
                    }}</time>
            </div>
            <div class="post-comment-text">
                <p>{{ comment.body }}</p>
            </div>
            <div v-if="isAnswerAuthor">
                <router-link
                        :to="{ name: 'Create-comment', params: { id: comment.id } }"
                        class="btn btn-sm btn-outline-secondary mr-1"
                >Edit
                </router-link>
                <button
                        class="btn btn-sm btn-outline-danger"
                        @click="triggerDeleteComment"
                >Delete
                </button>
            </div>
            <div class="post-comment-footer">
                <div class="comment-like">
                    <button
                            class="icon mdi mdi-thumb-up-outline"
                            @click="toggleLike"
                            :class="{
              'btn-danger': userLikedComment,
              'btn-outline-danger': !userLikedComment
            }"
                    ></button>
                    <a href="#">{{ likesCounter }}</a>
                </div>
                <div class="comment-reply">

                    <a href="#">Ответить</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { apiService } from "../common/api.service";

    export default {
        name: "Comment",
        props: {
            comment: {
                type: Object,
                required: true
            },
            requestUser: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                userLikedComment: this.comment.user_has_voted,
                likesCounter: this.comment.likes_count
            };
        },
        computed: {
            isAnswerAuthor() {
                // return true if the logged in user is also the author of the answer instance
                return this.comment.author === this.requestUser;
            }
        },
        methods: {
            toggleLike() {
                this.userLikedComment === false
                    ? this.likeComment()
                    : this.unLikeComment()
            },
            likeComment() {
                this.likesCounter += 1;
                this.userLikedComment = true;
                let endpoint = `/api/comments/${this.comment.id}/like/`;
                apiService(endpoint, "POST");
            },
            unLikeComment() {
                this.likesCounter -= 1;
                this.userLikedComment = false;
                let endpoint = `/api/comments/${this.comment.id}/like/`;
                apiService(endpoint, "POST");
            },
            triggerDeleteComment() {
                // emit an event to delete an answer instance
                this.$emit("delete-comment", this.comment);
            }
        }
    };
</script>

<style scoped></style>