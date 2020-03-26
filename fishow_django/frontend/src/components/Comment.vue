<template>
    <div class="post-comment">
        <div class="post-comment-aside">
            <img
                    class="img-circle"
                    src="/static/assets/images/user-6-69x69.jpg"
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

            <div class="post-comment-footer">
                <div class="comment-like">
                    <button
                            class="icon mdi "
                            @click="toggleLike"
                            :class="{
              'mdi-thumb-up': userLikedComment,
              'mdi-thumb-up-outline': !userLikedComment
            }"
                    ></button>
                    <button
                            class="icon mdi"
                            @click="toggleDislike"
                            :class="{
              'mdi-thumb-down': userDisLikedComment,
              'mdi-thumb-down-outline': !userDisLikedComment
            }"
                    ></button>
                    <a href="#">{{ likesCounter - dislikesCounter }}</a>
                </div>
                <div class="comment-reply">
                    <a href="#">Ответить</a>
                </div>
                <div v-if="isCommentAuthor">


                <div class="comment-reply">
                    <div @click="triggerDeleteComment">Удалить</div>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { apiService } from "@/common/api.service";

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
            },
            slug: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                userLikedComment: this.comment.user_has_votedUp,
                userDisLikedComment: this.comment.user_has_votedDown,
                likesCounter: this.comment.likes_count,
                dislikesCounter: this.comment.dislikes_count,
            };
        },
        computed: {
            isCommentAuthor() {
                // return true if the logged in user is also the author of the answer instance
                // return this.comment.author === this.requestUser;
                return this.comment.author === this.requestUser;
            }
        },
        methods: {
            toggleLike() {
                if (this.userLikedComment) {
                    this.unLikeComment()
                } else {
                    if (this.userDisLikedComment) {
                        this.undislikeComment()
                    } else {
                        this.likeComment()
                    }
                }
            },
            toggleDislike() {
                if (this.userDisLikedComment) {
                    this.undislikeComment()
                } else {
                    if (this.userLikedComment) {
                        this.unLikeComment()
                    } else {
                        this.dislikeComment()
                    }
                }
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
                    apiService(endpoint, "DELETE");

            },
            dislikeComment() {
                this.dislikesCounter += 1;
                this.userDisLikedComment = true;
                let endpoint = `/api/comments/${this.comment.id}/dislike/`;
                apiService(endpoint, "POST");
            },
            undislikeComment() {
                this.dislikesCounter -= 1;
                this.userDisLikedComment = false;
                let endpoint = `/api/comments/${this.comment.id}/dislike/`;
                apiService(endpoint, "DELETE");
            },

            triggerDeleteComment() {
                // emit an event to delete an answer instance
                this.$emit("deleteComment", this.comment);
            }
        }
    };
</script>

<style scoped></style>