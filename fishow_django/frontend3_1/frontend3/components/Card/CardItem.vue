<template>
  <div class="container">
    <div class="card">
      <div class="card-content">
        <div class="content-container">
          <card-header
            :liked="liked"
            :type="type"
            :id-item="item.id"
            :user-dis-liked="userDisLiked"
            :user-liked="userLiked"
          />
          <card-content :item="item" />
        </div>
        <card-footer
          :author="item.author"
          :category="item.category"
          :comments-count="item.comments_count"
          :created-at="item.created_at"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CardFooter from '~/components/Card/CardFooter'
import CardHeader from '~/components/Card/CardHeader'
import CardContent from '~/components/Card/CardContent'
export default {
  components: { CardContent, CardHeader, CardFooter },
  props: {
    item: {
      type: Object,
      required: true,
    },
    liked: {
      type: Boolean,
      default() {
        return true
      },
    },
    type: {
      type: String,
      default() {
        return 'blogs'
      },
    },
  },
  data() {
    return {
      result: {},
      userLiked: this.item && this.item.user_has_votedUp,
      userDisLiked: this.item && this.item.user_has_votedDown,
      likesCounter: 0,
      dislikesCounter: 0,
    }
  },
  computed: {
    rating() {
      return this.item.likes_count - this.item.dislikes_count
    },
  },
  methods: {},
}
</script>

<style scoped lang="scss">
.blog-category {
  background-color: #1e347b;
}
.media {
  align-items: center;
  .flex figure {
    margin-left: 0;
  }
  .title {
    color: #adadad;
    font-weight: 300;
    @media screen and (max-width: 450px) {
      font-size: 20px;
    }
  }
}
.like {
  display: flex;
  flex-flow: column;
}
.flex {
  display: flex;
  align-items: center;
  @media screen and (max-width: 450px) {
    flex-flow: column;
    align-items: flex-start;
    figure {
      margin: 0;
    }
  }
  figure {
    margin: 0 20px;
  }
}
.post-text {
  padding: 1rem 0;
}
[src*='svg'] {
  max-height: 50px;
}
.content-container {
  display: flex;
  align-items: baseline;
}
.title,
.card .pre-header {
  margin: 0;
}
.title {
  color: #2aabd2;
}
.likes_counter {
  max-width: 40px;
}
.blog-author {
  align-items: center;
}
</style>
