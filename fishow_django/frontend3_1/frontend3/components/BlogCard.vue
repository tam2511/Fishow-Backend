<template>
  <div class="container">
    <div class="card">
      <div class="card-content">
        <div class="content-container">
          <div v-if="liked" class="media">
            <div class="media-left">
              <div class="like">
                <b-button
                  :outlined="!userLikedBlog"
                  :type="{
                    'is-success is-light': userLikedBlog,
                    '': !userLikedBlog,
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
                  :outlined="!userDisLikedBlog"
                  :type="{
                    'is-danger is-light': userDisLikedBlog,
                    '': !userDisLikedBlog,
                  }"
                  :disabled="!$auth.user"
                  icon-pack="fa"
                  icon-right="chevron-down"
                  @click="toggleDislike"
                />
              </div>
            </div>
          </div>
          <div class="content">
            <div class="media pre-header">
              <div class="media-content">
                <h2 class="title">
                  <nuxt-link
                    :to="{ name: 'blog-slug', params: { slug: blog.slug } }"
                    >{{ blog.title }}
                  </nuxt-link>
                </h2>
              </div>
            </div>
            <div
              v-for="p in getResult"
              :key="p.id"
              :class="p.type + '_container'"
            >
              <p v-if="p.type === 'text'" class="post-text">{{ p.body }}</p>
              <iframe
                v-if="p.type === 'video'"
                width="560"
                height="315"
                :src="p.url"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
                name="video"
              ></iframe>
              <figure v-if="p.type === 'image'" class="image is-fullwidth">
                <img :src="p.url" alt="" />
              </figure>
            </div>
          </div>
        </div>
        <div class="media card-footer">
          <div class="is-flex blog-author">
            <figure class="image is-16x16">
              <img
                src="https://bulma.io/images/placeholders/96x96.png"
                alt="Placeholder image"
              />
            </figure>
            <p>{{ blog.author }}</p>
            <time datetime="2016-1-1">{{ blog.created_at }}</time>
          </div>
          <div>
            <b-field grouped group-multiline>
              <div class="control">
                <b-taglist attached>
                  <nuxt-link
                    :to="{ name: 'blog-slug', params: { slug: blog.slug } }"
                  >
                    <b-tag type="is-light">Комментариев</b-tag>
                    <b-tag type="is-primary">{{ blog.comments_count }}</b-tag>
                  </nuxt-link>
                </b-taglist>
              </div>
            </b-field>
            <b-tag class="blog-category" type="is-primary">{{
              blog.category
            }}</b-tag>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    blog: {
      type: Object,
      required: true,
    },
    liked: {
      type: Boolean,
      default() {
        return true
      },
    },
  },
  data() {
    return {
      result: {},
      userLikedBlog: this.blog && this.blog.user_has_votedUp,
      userDisLikedBlog: this.blog && this.blog.user_has_votedDown,
      likesCounter: 0,
      dislikesCounter: 0,
    }
  },
  computed: {
    getResult() {
      try {
        return JSON.parse(this.blog.content).blocks[0]
      } catch (e) {
        return null
      }
    },
    rating() {
      return this.blog.likes_count - this.blog.dislikes_count
    },
  },
  methods: {
    toggleLike() {
      if (this.userLikedBlog) {
        this.unLikeBlog()
      } else if (this.userDisLikedBlog) {
        this.undislikeBlog()
      } else {
        this.likeBlog()
      }
    },
    toggleDislike() {
      if (this.userDisLikedBlog) {
        this.undislikeBlog()
      } else if (this.userLikedBlog) {
        this.unLikeBlog()
      } else {
        this.dislikeBlog()
      }
    },
    likeBlog() {
      this.likesCounter += 1
      this.userLikedBlog = true
      this.$axios.$post(`/blogs/${this.blog.id}/like/`)
    },
    unLikeBlog() {
      this.likesCounter -= 1
      this.userLikedBlog = false
      this.$axios.$delete(`/blogs/${this.blog.id}/like/`)
    },
    dislikeBlog() {
      this.dislikesCounter -= 1
      this.userDisLikedBlog = true
      this.$axios.$post(`/blogs/${this.blog.id}/dislike/`)
    },
    undislikeBlog() {
      this.dislikesCounter += 1
      this.userDisLikedBlog = false
      this.$axios.$delete(`/blogs/${this.blog.id}/dislike/`)
    },
  },
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
.media.card-footer {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  & > div > * {
    margin: 0 10px;
  }
  padding-top: 10px;
  .field.is-grouped.is-grouped-multiline > .control:last-child {
    margin: 0;
  }
  & > * {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: space-around;
  }
}
</style>
