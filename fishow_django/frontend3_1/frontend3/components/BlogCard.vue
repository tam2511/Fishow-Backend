<!--<template>-->
<!--  <article class="post-corporate">-->
<!--    <div class="post-corporate-content">-->
<!--      <div class="fishow-votes_container">-->
<!--        <div class="fishow_votes">-->
<!--          <svg-->
<!--            id="Capa_1"-->
<!--            class=""-->
<!--            :class="{-->
<!--              'fishow-votes_up__active': userLikedBlog,-->
<!--              'fishow-votes_up': !userLikedBlog,-->
<!--            }"-->
<!--            version="1.1"-->
<!--            xmlns="http://www.w3.org/2000/svg"-->
<!--            x="0px"-->
<!--            y="0px"-->
<!--            width="16"-->
<!--            height="16"-->
<!--            xml:space="preserve"-->
<!--            @click="toggleLike"-->
<!--          >-->
<!--            <path-->
<!--              d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285-->
<!--		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854-->
<!--		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848-->
<!--		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566-->
<!--		C284.929,199.378,283.984,197.188,282.082,195.285z"-->
<!--            />-->
<!--          </svg>-->
<!--          <span data-votes-counter>{{ likesCounter - dislikesCounter }}</span>-->
<!--          <svg-->
<!--            id="Capa_1"-->
<!--            :class="{-->
<!--              'fishow-votes_down__active': userDisLikedBlog,-->
<!--              'fishow-votes_down': !userDisLikedBlog,-->
<!--            }"-->
<!--            version="1.1"-->
<!--            xmlns="http://www.w3.org/2000/svg"-->
<!--            x="0px"-->
<!--            y="0px"-->
<!--            width="16"-->
<!--            height="16"-->
<!--            xml:space="preserve"-->
<!--            @click="toggleDislike"-->
<!--          >-->
<!--            <path-->
<!--              d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285-->
<!--		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854-->
<!--		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848-->
<!--		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566-->
<!--		C284.929,199.378,283.984,197.188,282.082,195.285z"-->
<!--            />-->
<!--          </svg>-->
<!--        </div>-->
<!--        <div class="post-corporate-header">-->
<!--          &lt;!&ndash; Badge&ndash;&gt;-->
<!--          <div class="badge badge-primary">{{ blog.category }}</div>-->
<!--          <time class="post-corporate-time"> {{ blog.created_at }} </time>-->
<!--          <div class="post-corporate-author">-->
<!--            Автор:-->
<!--            <span>{{ blog.author }}</span>-->
<!--          </div>-->
<!--          <div class="post-corporate-view">-->
<!--            <span class="icon fl-justicons-visible6"></span>-->
<!--            0-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->

<!--      <h4 class="post-corporate-title">-->
<!--        <nuxt-link :to="{ name: 'blog-slug', params: { slug: blog.slug } }">{{-->
<!--          blog.title-->
<!--        }}</nuxt-link>-->
<!--      </h4>-->
<!--      <div class="post-corporate-blog">-->

<!--      </div>-->
<!--    </div>-->
<!--    <div class="post-corporate-footer">-->
<!--      <div class="post-corporate-comment">-->
<!--        <span class="icon mdi mdi-comment-outline"></span>-->
<!--        <nuxt-link :to="{ name: 'blog-slug', params: { slug: blog.slug } }"-->
<!--          >{{ blog.comments_count }} Комментариев</nuxt-link-->
<!--        >-->
<!--      </div>-->
<!--      <div class="post-corporate-share">-->
<!--        <ul class="group">-->
<!--          <li>Поделиться</li>-->
<!--          <li><a class="icon fa-facebook" href="#"></a></li>-->
<!--          <li><a class="icon fa-twitter" href="#"></a></li>-->
<!--          <li><a class="icon fa-google-plus" href="#"></a></li>-->
<!--          <li><a class="icon fa-instagram" href="#"></a></li>-->
<!--        </ul>-->
<!--      </div>-->
<!--    </div>-->
<!--  </article>-->
<!--</template>-->
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
          </div>
        </div>
        <b-tag class="blog-category" type="is-primary" size="is-medium">{{
          blog.category
        }}</b-tag>
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
  //   data() {
  //     return {
  //       result: {},
  //       userLikedBlog: this.blog.user_has_votedUp,
  //       userDisLikedBlog: this.blog.user_has_votedDown,
  //       likesCounter: this.blog.likes_count,
  //       dislikesCounter: this.blog.dislikes_count,
  //     }
  //   },
  computed: {
    getResult() {
      try {
        return JSON.parse(this.blog.content).blocks[0]
      } catch (e) {
        return null
      }
    },
  },
  //   methods: {
  //     toggleLike() {
  //       if (this.userLikedBlog) {
  //         this.unLikeBlog()
  //       } else if (this.userDisLikedBlog) {
  //         this.undislikeBlog()
  //       } else {
  //         this.likeBlog()
  //       }
  //     },
  //     toggleDislike() {
  //       if (this.userDisLikedBlog) {
  //         this.undislikeBlog()
  //       } else if (this.userLikedBlog) {
  //         this.unLikeBlog()
  //       } else {
  //         this.dislikeBlog()
  //       }
  //     },
  //     async likeBlog() {
  //       this.likesCounter += 1
  //       this.userLikedBlog = true
  //       await this.$axios.$post(`/blogs/${this.blog.id}/like/`)
  //     },
  //     async unLikeBlog() {
  //       this.likesCounter -= 1
  //       this.userLikedBlog = false
  //       await this.$axios.$delete(`/blogs/${this.blog.id}/like/`)
  //     },
  //     async dislikeBlog() {
  //       this.dislikesCounter += 1
  //       this.userDisLikedBlog = true
  //       await this.$axios.$post(`/blogs/${this.blog.id}/dislike/`)
  //     },
  //     async undislikeBlog() {
  //       this.dislikesCounter -= 1
  //       this.userDisLikedBlog = false
  //       await this.$axios.$delete(`/blogs/${this.blog.id}/dislike/`)
  //     },
  //   },
}
</script>

<style scoped lang="scss">
.blog-category {
  background-color: #1e347b;
  font-size: 45px;
}
</style>
