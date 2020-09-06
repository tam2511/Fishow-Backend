<template>
  <div class="container">
    <div class="card">
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <div class="flex">
              <div class="is-flex">
                <figure class="image is-32x32">
                  <img
                    src="https://bulma.io/images/placeholders/96x96.png"
                    alt="Placeholder image"
                  />
                </figure>

                <p class="title is-4">{{ blog.author }}</p>
              </div>
            </div>
          </div>
          <div class="media-right">
            <b-tag class="blog-category" type="is-primary" size="is-medium">{{
              blog.category
            }}</b-tag>
          </div>
        </div>
        <div class="content-container">
          <div class="media">
            <div class="media-left">
              <div class="like">
                <b-button
                  outlined
                  :disabled="!$auth.user"
                  icon-pack="fa"
                  icon-right="chevron-up"
                  @click="toggleLike"
                />
                <b-button type="is-primary likes_counter">
                  {{ rating + likesCounter + dislikesCounter }}
                </b-button>
                <b-button
                  outlined
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
                frameborder="0"
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
          <div class="column is-one-quarter is-inline-block">
            <time datetime="2016-1-1">{{ blog.created_at }}</time>
          </div>
          <div class="is-inline-block">
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
  },
  data() {
    return {
      result: {},
      userLikedBlog: this.blog.user_has_votedUp,
      userDisLikedBlog: this.blog.user_has_votedDown,
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
    async likeBlog() {
      this.likesCounter += 1
      this.userLikedBlog = true
      await this.$axios.$post(`/blogs/${this.blog.id}/like/`)
    },
    async unLikeBlog() {
      this.likesCounter -= 1
      this.userLikedBlog = false
      await this.$axios.$delete(`/blogs/${this.blog.id}/like/`)
    },
    async dislikeBlog() {
      this.dislikesCounter -= 1
      this.userDisLikedBlog = true
      await this.$axios.$post(`/blogs/${this.blog.id}/dislike/`)
    },
    async undislikeBlog() {
      this.dislikesCounter += 1
      this.userDisLikedBlog = false
      await this.$axios.$delete(`/blogs/${this.blog.id}/dislike/`)
    },
  },
}
</script>

<style scoped lang="scss">
.blog-category {
  background-color: #1e347b;
  font-size: 45px;
}
.image_container {
  padding: 20px 0;
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
</style>
