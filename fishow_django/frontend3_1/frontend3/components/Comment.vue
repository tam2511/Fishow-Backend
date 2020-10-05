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
            <a class="level-item" aria-label="trash" @click="removeComment">
              <span class="icon is-small">
                <i class="fas fa-trash" aria-hidden="true"></i>
              </span>
            </a>
            <a
              :class="{
                'level-item': !userLikedComment,
                'level-item active-up': userLikedComment,
              }"
              aria-label="like"
              @click="toggleLike"
            >
              <span class="icon is-small">
                <i class="fa fa-thumbs-up" aria-hidden="true"></i>
              </span>
            </a>
            <span class="level-item">
              {{ likesCounter - dislikesCounter }}
            </span>
            <a
              :class="{
                'level-item': !userDisLikedComment,
                'level-item active-down': userDisLikedComment,
              }"
              aria-label="dislike"
              @click="toggleDislike"
            >
              <span class="icon is-small">
                <i class="fas fa-thumbs-down" aria-hidden="true"></i>
              </span>
            </a>
          </div>
        </nav>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  props: {
    comment: {
      type: Object,
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
      return this.comment.author === this.$auth.user
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
    removeComment() {
      this.$emit('deleteComment', this.comment)
    },
  },
}
</script>

<style lang="scss" scoped>
.level-item {
  &.active-up {
    color: darkcyan;
  }
  &.active-down {
    color: brown;
  }
}
</style>
