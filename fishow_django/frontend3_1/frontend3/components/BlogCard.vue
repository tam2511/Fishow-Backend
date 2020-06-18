<template>
  <div class="container">
    <div class="card">
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img
                src="https://bulma.io/images/placeholders/96x96.png"
                alt="Placeholder image"
              />
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{ blog.author }}</p>
            <p class="subtitle is-6">@{{ blog.author }}</p>
            <span data-votes-counter>{{ likesCounter - dislikesCounter }}</span>
            <button class="up" @click="toggleLike">UP</button>
            <button class="down" @click="toggleDislike">DOWN</button>
          </div>
          <b-tag class="blog-category" type="is-primary" size="is-medium">{{
            blog.category
          }}</b-tag>
        </div>
        <p class="title">
          <nuxt-link :to="{ name: 'blog-slug', params: { slug: blog.slug } }"
            >{{ blog.title }}
          </nuxt-link>
        </p>
        <div class="content">
          <div v-for="p in getResult" :key="p.id">
            <div v-if="p.type === 'text'" class="post-corporate-text">
              <p>{{ p.body }}</p>
            </div>
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
            <div v-if="p.type === 'image'" class="post-corporate-figure">
              <img :src="p.url" alt="" />
            </div>
          </div>
          <br />
          <div class="column is-one-quarter is-inline-block">
            <time datetime="2016-1-1">{{ blog.created_at }}</time>
          </div>
          <div class="is-inline-block">
            <b-field grouped group-multiline>
              <div class="control">
                <b-taglist attached>
                  <b-tag type="is-light">Комментариев</b-tag>
                  <b-tag type="is-info">{{ blog.comments_count }}</b-tag>
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
      likesCounter: this.blog.likes_count,
      dislikesCounter: this.blog.dislikes_count,
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
      this.dislikesCounter += 1
      this.userDisLikedBlog = true
      await this.$axios.$post(`/blogs/${this.blog.id}/dislike/`)
    },
    async undislikeBlog() {
      this.dislikesCounter -= 1
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
</style>
