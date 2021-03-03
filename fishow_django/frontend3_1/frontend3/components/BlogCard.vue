<template>
  <div class="card">
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
              {{ rating }}
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
        <div class="like-line" :counter="rating"></div>
        <div class="media pre-header">
          <div class="media-content">
            <h2 class="title">
              <nuxt-link
                :to="{ name: 'blog-slug', params: { slug: blog.slug } }"
                >{{ rating }} | {{ blog.title }}
              </nuxt-link>
            </h2>
          </div>
        </div>
        <div
          v-for="item in getResult"
          :key="item.id"
          :class="item.type + '_container'"
        >
          <p v-if="item.type === 'text'" class="post-text">
            {{ item.body }}
          </p>
          <iframe
            v-if="item.type === 'video'"
            width="560"
            height="315"
            :src="item.body"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            name="video"
          ></iframe>
          <figure v-if="item.type === 'image'" class="image is-fullwidth">
            <img :src="item.body" alt="" />
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
        <b-field grouped>
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
        <div class="block">
          <b-icon icon="eye" size="is-small"></b-icon>
          {{ blog.user_views }}
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
        return false
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
  head() {
    return {
      script: [
        {
          innerHTML: this.createJsonBlog(this.blog),
          type: 'application/ld+json',
        },
      ],
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
      return (
        this.blog.likes_count -
        this.blog.dislikes_count +
        this.likesCounter +
        this.dislikesCounter
      )
    },
  },

  methods: {
    createJsonBlog(data) {
      const defaultURL = 'https://fishow.ru'
      const image = defaultURL + '/favicon-96x96.png'
      const url = defaultURL + this.$router.history.current.fullPath
      const images = []
      try {
        const items = JSON.parse(this.blog.content).blocks[0]

        items.forEach((item) => {
          if (item.type === 'image') {
            images.push(item.url)
          }
        })
      } catch (e) {}
      const blog = {
        '@context': 'https://schema.org',
        '@type': 'NewsArticle',
        mainEntityOfPage: {
          '@type': 'WebPage',
          '@id': url,
        },
        headline: data.title,
        image: images,
        datePublished: data.created_at,
        author: {
          '@type': 'Person',
          name: data.author,
        },
        publisher: {
          '@type': 'Organization',
          name: 'Fishow',
          logo: {
            '@type': 'ImageObject',
            url: image,
          },
        },
      }
      return JSON.stringify(blog)
    },
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
      this.$axios.$post(`/blogs/${this.blog.slug}/like/`)
    },
    unLikeBlog() {
      this.likesCounter -= 1
      this.userLikedBlog = false
      this.$axios.$delete(`/blogs/${this.blog.slug}/like/`)
    },
    dislikeBlog() {
      this.dislikesCounter -= 1
      this.userDisLikedBlog = true
      this.$axios.$post(`/blogs/${this.blog.slug}/dislike/`)
    },
    undislikeBlog() {
      this.dislikesCounter += 1
      this.userDisLikedBlog = false
      this.$axios.$delete(`/blogs/${this.blog.slug}/dislike/`)
    },
  },
}
</script>

<style scoped lang="scss">
.card {
  padding: 20px;
}
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
  white-space: pre-line;
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
.content {
  position: relative;
  width: 100%;
  &:hover {
    .like-line {
      opacity: 1;
    }
  }
}
.like-counter {
  opacity: 0;
}
.like-line {
  transition: 0.5s;
  height: 100%;
  width: 20%;
  position: absolute;
  right: 0;
  top: 0;
  clip-path: ellipse(20% 50% at 100% 50%);
  background: linear-gradient(
    271.4deg,
    #a0ff55 -119.32%,
    rgba(255, 255, 255, 0) 298.37%
  );
  opacity: 0;
  cursor: pointer;
  &:after {
    content: attr(counter);
    width: 30px;
    position: absolute;
    justify-content: center;
    align-items: center;
    display: flex;
    right: 0;
    height: 100%;
    top: 0;
    opacity: 0;
    transition: 0.3s;
  }
  &:hover:after {
    opacity: 1;
  }
}
</style>
