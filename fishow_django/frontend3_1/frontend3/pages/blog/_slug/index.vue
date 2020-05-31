<template>
  <div class="container">
    <div class="row row-30">
      <div class="col-lg-8">
        <div class="blog-post">
          <div class="fishow-votes_container">
            <h3 class="blog-post-title">{{ blog.title }}</h3>
          </div>
          <div class="blog-post-content">
            <div v-for="p in result" :key="p.url">
              <p v-if="p.type === 'text'" class="blog-post-text">
                {{ p.body }}
              </p>
              <iframe
                v-if="p.type === 'video'"
                width="560"
                height="315"
                :src="whomIsVideo(p.url)"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              ></iframe>
              <img v-if="p.type === 'image'" :src="p.url" alt="" />
            </div>
            <ul class="list-tags">
              <li v-for="blogTag in blogTags" :key="blogTag">
                <router-link to="/">{{ blogTag }}</router-link>
              </li>
            </ul>
          </div>
        </div>
        <div class="blog-post-footer">
          <div class="blog-post-header">
            <div
              :class="{
                fishow_votes: this.$store.state.user.user,
                'fishow_votes fishow_votes_not_active': !this.$store.state.user
                  .user,
              }"
            >
              <svg
                id="Capa_1"
                :class="{
                  'fishow-votes_up__active': userLikedBlog,
                  'fishow-votes_up': !userLikedBlog,
                }"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="284.929px"
                height="284.929px"
                viewBox="0 0 284.929 284.929"
                xml:space="preserve"
                @click="toggleLike"
              >
                <path
                  d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"
                />
              </svg>
              <span data-votes-counter>{{
                likesCounter - dislikesCounter
              }}</span>
              <svg
                id="Capa_1"
                class=""
                :class="{
                  'fishow-votes_down__active': userDisLikedBlog,
                  'fishow-votes_down': !userDisLikedBlog,
                }"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="284.929px"
                height="284.929px"
                viewBox="0 0 284.929 284.929"
                xml:space="preserve"
                @click="toggleDislike"
              >
                <path
                  d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"
                />
              </svg>
            </div>
            <div class="blog-post-author">
              <img
                class="img-circle"
                src="/static/assets/images/user-3-63x63.jpg"
                alt=""
                width="25"
                height="25"
              />
              <p class="post-author">{{ blog.author }}</p>
            </div>
            <div class="blog-post-meta">
              <time class="blog-post-time" datetime="2018"
                ><span class="icon mdi mdi-clock"></span
                >{{ blog.created_at }}</time
              >
              <div class="blog-post-comment">
                <span class="icon mdi mdi-comment-outline"></span
                >{{ blog.comments_count }}
              </div>
              <div class="blog-post-view">
                <span class="icon fl-justicons-visible6"></span>0
              </div>
              <div class="badge badge-secondary">{{ blog.category }}</div>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-sm-12">
            <!-- Heading Component-->
            <article class="heading-component">
              <div class="heading-component-inner">
                <h5 class="heading-component-title">
                  {{ blog.comments_count }} комментариев
                </h5>
              </div>
            </article>

            <div class="blog-post-comments blog-space">
              <!-- Post Comment-->
              <!--              <transition-group name="slide-fade" tag="div" appear>-->
              <Comment
                v-for="(comment, index) in comments"
                :key="index"
                :comment="comment"
                :slug="$route.params.slug"
                :request-user="$auth.user"
                @deleteComment="deleteComment"
              />
              <!--              </transition-group>-->

              <div v-if="$auth.loggedIn" class="comment-box">
                <div class="comment-box-aside">
                  <img
                    class="img-circle"
                    src="/static/assets/images/user-7-69x69.jpg"
                    alt=""
                    width="69"
                    height="69"
                  />
                </div>
                <div class="comment-box-main">
                  <h5 class="comment-box-name">{{ $auth.user }}</h5>
                  <form class="comment-box-form" @submit.prevent="onSubmit">
                    <div class="form-wrap">
                      <textarea
                        id="comment-message"
                        v-model="commentBody"
                        class="form-input"
                        name="message"
                        placeholder="Ваш комментарий"
                      ></textarea>
                    </div>
                    <div v-if="error" class="alert-danger">{{ error }}</div>
                    <div class="form-button">
                      <button class="button button-primary" type="submit">
                        Отправить
                      </button>
                    </div>
                  </form>
                </div>
              </div>
              <div v-else class="comment-notUser">
                Для возможности комментирования пожалуйста авторизуйтесь
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="block-aside">
          <block-categories />
          <block-spotlight />
          <block-tags />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BlockCategories from '@/components/blog/blockCategories'
import BlockSpotlight from '@/components/blog/blockSpotlight'
import BlockTags from '@/components/blog/blockTags'
import Comment from '@/components/Comment.vue'
export default {
  scrollToTop: true,
  components: { BlockTags, BlockSpotlight, BlockCategories, Comment },
  async fetch({ store, error, params }) {
    try {
      await store.dispatch('blogs/getBlog', params.slug)
    } catch (e) {
      console.log('erorr = ', e)
      error({
        statusCode: 503,
        message: 'Unable to fetch events at this time. Please try again.',
      })
    }
  },
  data() {
    return {
      blogTags: {},
      result: {},
      id: 0,
      comments: [],
      newCommentBody: null,
      requestUser: null,
      commentBody: null,
      error: null,
      userLikedBlog: null,
      userDisLikedBlog: null,
      likesCounter: null,
      dislikesCounter: null,
    }
  },

  computed: {
    ...mapState('blogs', ['blog']),
  },
  created() {
    this.getBlogData()
    this.getCommentData()
  },
  mounted() {
    scrollTo(0, 0)
  },
  methods: {
    // whomIsVideo(fields) {
    //   const temp = fields.split('/')
    //   for (let i = 0; i < temp.length; i++) {
    //     if (temp[i] === 'youtu.be') {
    //       return 'https://www.youtube.com/embed/' + temp[temp.length - 1]
    //     }
    //     if (temp[i] === 'www.youtube.com') {
    //       return (
    //         'https://www.youtube.com/embed/' +
    //         temp[temp.length - 1].split('watch?v=')[0]
    //       )
    //     }
    //   }
    // },
    getBlogData() {
      this.result = JSON.parse(this.blog.content)
      this.result = this.result.blocks[0]
      const tags = JSON.parse(this.blog.tags)
      const result = []
      tags.forEach((tag) => result.push(tag.name))
      this.blogTags = result
      this.userLikedBlog = this.blog.user_has_votedUp
      this.userDisLikedBlog = this.blog.user_has_votedDown
      this.likesCounter = this.blog.likes_count
      this.dislikesCounter = this.blog.dislikes_count
      this.id = this.blog.id
    },
    async getCommentData() {
      const response = await this.$axios.$get(
        `/blogs/${this.$route.params.slug}/comments/`
      )
      this.comments.push(...response.results)
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
    async deleteComment(comment) {
      // delete a given answer from the answers array and make a delete request to the REST API
      // const endpoint = `/api/comments/${comment.id}/`
      // try {
      //   await apiService(endpoint, 'DELETE')
      //   this.$delete(this.comments, this.comments.indexOf(comment))
      //   this.userHasAnswered = false
      // } catch (err) {
      //   console.log(err)
      // }
    },
    async onSubmit() {
      try {
        const response = await this.$axios.$post(
          `/blogs/${this.$route.params.slug}/comment/`,
          { body: this.commentBody }
        )
        this.comments.push(response)
      } catch (e) {
        console.log('error = ', e)
      }
      // if (this.commentBody) {
      //   const endpoint = `/api/blogs/${this.slug}/comment/`
      //   apiService(endpoint, 'POST', { body: this.commentBody }).then(data => {
      //     this.comments.push(data)
      //   })
      //   this.commentBody = null
      //   if (this.error) {
      //     this.error = null
      //   }
      // } else {
      //   this.error = 'Вы не можете отправить пустой комментарий'
      // }
    },
  },
  head() {
    return {
      title: 'Fishow - ' + this.blog.title,
    }
  },
}
</script>

<style scoped lang="scss">
.blog-post-content {
  img {
    width: 100%;
  }
  p {
    white-space: pre-line;
  }
}
.blog-post-footer {
  background: var(--background-color-primary);
  border: 1px solid var(--background-color-border);
  padding: 20px;
}
.blog-post-text {
  text-align: justify;
}
.fishow-votes_up__active {
  fill: cadetblue;
}
.fishow-votes_down__active {
  fill: red;
}
.comment-notUser {
  padding: 20px;
  color: #91171c;
  text-align: center;
}
</style>
