<!--<template>-->
<!--  <div class="post-comment">-->
<!--    <div class="post-comment-aside">-->
<!--      <img-->
<!--        class="img-circle"-->
<!--        src="/static/assets/images/user-6-69x69.jpg"-->
<!--        alt=""-->
<!--        width="69"-->
<!--        height="69"-->
<!--      />-->
<!--    </div>-->
<!--    <div class="post-comment-main">-->
<!--      <div class="post-comment-header">-->
<!--        <h5 class="author-name">{{ comment.author }}</h5>-->
<!--        <time class="post-comment-time" datetime="2018">{{-->
<!--          comment.created_at-->
<!--        }}</time>-->
<!--      </div>-->
<!--      <div class="post-comment-text">-->
<!--        <p>{{ comment.body }}</p>-->
<!--      </div>-->

<!--      <div class="post-comment-footer">-->
<!--        <div class="comment-like">-->
<!--          <button-->
<!--            class="icon mdi"-->
<!--            :class="{-->
<!--              'mdi-thumb-up': userLikedComment,-->
<!--              'mdi-thumb-up-outline': !userLikedComment,-->
<!--            }"-->
<!--            @click="toggleLike"-->
<!--          ></button>-->
<!--          <span class="comment-like-counter">{{-->
<!--            likesCounter - dislikesCounter-->
<!--          }}</span>-->
<!--          <button-->
<!--            class="icon mdi"-->
<!--            :class="{-->
<!--              'mdi-thumb-down': userDisLikedComment,-->
<!--              'mdi-thumb-down-outline': !userDisLikedComment,-->
<!--            }"-->
<!--            @click="toggleDislike"-->
<!--          ></button>-->
<!--        </div>-->
<!--        <div class="comment-reply">-->
<!--          <a href="#">Ответить</a>-->
<!--        </div>-->
<!--        <div v-if="isCommentAuthor" class="comment-reply-parent">-->
<!--          <div class="comment-reply">-->
<!--            <button type="button" @click="triggerDeleteComment">Удалить</button>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<template>
  <div class="box">
    <article class="media">
      <div class="media-left">
        <figure class="image is-64x64">
          <img
            src="https://bulma.io/images/placeholders/128x128.png"
            alt="Image"
          />
        </figure>
      </div>
      <div class="media-content">
        <div class="content">
          <p>
            <strong>{{ comment.author }}</strong>
            <small>@{{ comment.author }}</small>
            <small>{{ comment.created_at }}</small>
            <br />
            {{ comment.body }}
          </p>
        </div>
        <nav class="level is-mobile">
          <div class="level-left">
            <a class="level-item" aria-label="reply">
              <span class="icon is-small">
                <i class="fas fa-reply" aria-hidden="true"></i>
              </span>
            </a>
            <a class="level-item" aria-label="retweet">
              <span class="icon is-small">
                <i class="fas fa-retweet" aria-hidden="true"></i>
              </span>
            </a>
            <a class="level-item" aria-label="like">
              <span class="icon is-small">
                <i class="fas fa-heart" aria-hidden="true"></i>
              </span>
            </a>
          </div>
        </nav>
      </div>
    </article>
  </div>
</template>

<script>
// import { apiService } from '@/plugins/api.service'

export default {
  props: {
    comment: {
      type: Object,
      required: true,
    },
    requestUser: {
      type: String,
      required: true,
    },
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      userLikedComment: this.comment.user_has_votedUp,
      userDisLikedComment: this.comment.user_has_votedDown,
      likesCounter: this.comment.likes_count,
      dislikesCounter: this.comment.dislikes_count,
    }
  },
  computed: {
    isCommentAuthor() {
      // return true if the logged in user is also the author of the answer instance
      // return this.comment.author === this.requestUser;
      return this.comment.author === this.requestUser
    },
  },
  methods: {
    toggleLike() {
      if (this.userLikedComment) {
        this.unLikeComment()
      } else if (this.userDisLikedComment) {
        this.undislikeComment()
      } else {
        this.likeComment()
      }
    },
    toggleDislike() {
      if (this.userDisLikedComment) {
        this.undislikeComment()
      } else if (this.userLikedComment) {
        this.unLikeComment()
      } else {
        this.dislikeComment()
      }
    },
    async likeComment() {
      this.likesCounter += 1
      this.userLikedComment = true
      await this.$axios.$post(`/comments/${this.comment.id}/like/`)
    },
    async unLikeComment() {
      this.likesCounter -= 1
      this.userLikedComment = false
      await this.$axios.$delete(`/comments/${this.comment.id}/like/`)
    },
    async dislikeComment() {
      this.dislikesCounter += 1
      this.userDisLikedComment = true
      await this.$axios.$post(`/comments/${this.comment.id}/dislike/`)
    },
    async undislikeComment() {
      this.dislikesCounter -= 1
      this.userDisLikedComment = false
      await this.$axios.$delete(`/comments/${this.comment.id}/dislike/`)
    },
    triggerDeleteComment() {
      // emit an event to delete an answer instance
      this.$emit('deleteComment', this.comment)
    },
  },
}
</script>

<style scoped lang="scss">
button {
  padding: 5px 10px;
  border: none;
  transition-duration: 0.2s;
  &:hover {
    box-shadow: 0 5px 5px rgba(0, 0, 0, 0.2);
  }
}
.comment-like-counter {
  padding-right: 10px;
  padding-left: 10px;
}
.comment-reply {
  button,
  a {
    color: var(--color-typo-primary);
    background: none;
    &:hover {
      /*color: #a80000;*/
    }
  }
}
.comment-reply-parent {
  margin-left: 10px;
}
.mdi-thumb-down {
  color: #a80000;
  &-outline {
    color: #a80000;
  }
}
.mdi-thumb-up {
  color: #005e00;
  &-outline {
    color: #005e00;
  }
}
</style>
