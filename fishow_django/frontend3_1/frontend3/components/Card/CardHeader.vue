<template>
  <div v-if="liked" class="media">
    <div class="media-left">
      <div class="like">
        <b-button
          :outlined="!userLiked"
          :type="{
            'is-success is-light': userLiked,
            '': !userLiked,
          }"
          :disabled="!$auth.user"
          icon-pack="fa"
          icon-right="chevron-up"
          @click="toggleLike"
        />
        <b-button type="is-primary likes_counter">
          {{ rating + likesCounter + dislikesCounter }}
        </b-button>
        <b-button
          :outlined="!userDisLiked"
          :type="{
            'is-danger is-light': userDisLiked,
            '': !userDisLiked,
          }"
          :disabled="!$auth.user"
          icon-pack="fa"
          icon-right="chevron-down"
          @click="toggleDislike"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardHeader',
  props: {
    type: {
      type: String,
      required: true,
    },
    slug: {
      type: [String, Number],
      default() {
        return ''
      },
    },
    liked: {
      type: Boolean,
      default() {
        return true
      },
    },
    userLiked: {
      type: Boolean,
      default() {
        return false
      },
    },
    userDisLiked: {
      type: Boolean,
      default() {
        return false
      },
    },
  },
  data() {
    return {
      isUserLiked: this.userLiked || false,
      isUserDisLiked: this.userDisLiked || false,
    }
  },
  watch: {
    userLiked(value) {
      this.isUserLiked = value
    },
    userDisLiked(value) {
      this.isUserDisLiked = value
    },
  },
  methods: {
    toggleLike() {
      if (this.userLiked) {
        this.unLike()
      } else if (this.userDisLiked) {
        this.undislike()
      } else {
        this.like()
      }
    },
    toggleDislike() {
      if (this.userDisLiked) {
        this.undislike()
      } else if (this.userLiked) {
        this.unLike()
      } else {
        this.dislike()
      }
    },
    like() {
      this.likesCounter += 1
      this.isUserLiked = true
      this.$axios.$post(`/${this.type}/${this.slug}/like/`)
    },
    unLike() {
      this.likesCounter -= 1
      this.isUserLiked = false
      this.$axios.$delete(`/${this.type}/${this.slug}/like/`)
    },
    dislike() {
      this.dislikesCounter -= 1
      this.isUserDisLiked = true
      this.$axios.$post(`/${this.type}/${this.slug}/dislike/`)
    },
    undislike() {
      this.dislikesCounter += 1
      this.isUserDisLiked = false
      this.$axios.$delete(`/${this.type}/${this.slug}/dislike/`)
    },
  },
}
</script>

<style lang="scss" scoped></style>
