<template>
  <section class="section section-sm section-view">
    <div class="container">
      <div class="row row-30">
        <div class="col-lg-8">
          <div class="blog-post">
            <div class="blog-post-header">
              <div class="blog-post-author">
                <img
                  class="img-circle"
                  src="/static/assets/images/user-3-63x63.jpg"
                  alt=""
                  width="63"
                  height="63"
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
            <div class="fishow-votes_container">
              <div
                :class="{
                  fishow_votes: this.$store.state.username,
                  'fishow_votes fishow_votes_not_active': !this.$store.state
                    .username,
                }"
              >
                <svg
                  :class="{
                    'fishow-votes_up__active': userLikedBlog,
                    'fishow-votes_up': !userLikedBlog,
                  }"
                  @click="toggleLike"
                  version="1.1"
                  id="Capa_1"
                  xmlns="http://www.w3.org/2000/svg"
                  x="0px"
                  y="0px"
                  width="284.929px"
                  height="284.929px"
                  viewBox="0 0 284.929 284.929"
                  xml:space="preserve"
                >
                  <path
                    d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"
                  />
                </svg>
                <svg
                  class=""
                  :class="{
                    'fishow-votes_down__active': userDisLikedBlog,
                    'fishow-votes_down': !userDisLikedBlog,
                  }"
                  @click="toggleDislike"
                  version="1.1"
                  id="Capa_1"
                  xmlns="http://www.w3.org/2000/svg"
                  x="0px"
                  y="0px"
                  width="284.929px"
                  height="284.929px"
                  viewBox="0 0 284.929 284.929"
                  xml:space="preserve"
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
              <span data-votes-counter>{{
                likesCounter - dislikesCounter
              }}</span>

              <h3 class="blog-post-title">{{ blog.title }}</h3>
            </div>
            <div class="blog-post-content">
              <div v-for="p in result" :key="p.type">
                <p class="blog-post-text" v-if="p.type === 'text'">
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
                <Comment
                  v-for="(comment, index) in comments"
                  :comment="comment"
                  :key="index"
                  :slug="slug"
                  :requestUser="requestUser"
                  @deleteComment="deleteComment"
                />
                <div class="comment-box" v-if="userName">
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
                    <h5 class="comment-box-name">{{ this.requestUser }}</h5>
                    <form @submit.prevent="onSubmit" class="comment-box-form">
                      <div class="form-wrap">
                        <textarea
                          v-model="commentBody"
                          class="form-input"
                          id="comment-message"
                          name="message"
                          placeholder="Ваш комментарий"
                        ></textarea>
                      </div>
                      <div class="alert-danger" v-if="error">{{ error }}</div>
                      <div class="form-button">
                        <button class="button button-primary" type="submit">
                          Отправить
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
                <div v-else>
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
  </section>
</template>

<script>
import { apiService } from '@/common/api.service'
import Comment from '@/components/Comment.vue'
// import CreateComment from '@/components/CreateComment'
import BlockCategories from '../components/blog/blockCategories'
import BlockSpotlight from '../components/blog/blockSpotlight'
import BlockTags from '../components/blog/blockTags'
export default {
  name: 'Blog',
  components: { BlockTags, BlockSpotlight, BlockCategories, Comment },
  props: {
    slug: {
      type: String,
      default: null,
      required: true,
    },
  },

  data() {
    return {
      blogTags: {},
      result: {},
      blog: {},
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
    userName() {
      return this.$store.state.username
    },
  },
  methods: {
    whomIsVideo(fields) {
      const temp = fields.split('/')
      for (let i = 0; i < temp.length; i++) {
        if (temp[i] === 'youtu.be') {
          return 'https://www.youtube.com/embed/' + temp[temp.length - 1]
        }
        if (temp[i] === 'www.youtube.com') {
          return (
            'https://www.youtube.com/embed/' +
            temp[temp.length - 1].split('watch?v=')[0]
          )
        }
      }
    },
    setPageTitle(title) {
      document.title = title
    },
    getUser() {
      const wait = setInterval(() => {
        if (this.$store.state.username !== null) {
          clearInterval(wait)
          this.requestUser = this.$store.state.username
        }
      }, 100)
    },
    getBlogData() {
      const endpoint = `/api/blogs/${this.slug}/`
      apiService(endpoint).then((data) => {
        this.blog = data
        this.result = JSON.parse(data.content)
        this.result = this.result.blocks[0]
        const tags = JSON.parse(this.blog.tags)
        const result = []
        tags.forEach((tag) => result.push(tag.name))
        this.blogTags = result
        this.userLikedBlog = this.blog.user_has_votedUp
        this.userDisLikedBlog = this.blog.user_has_votedDown
        this.likesCounter = this.blog.likes_count
        this.dislikesCounter = this.blog.dislikes_count
        this.id = data.id
        this.setPageTitle('Fishow - ' + data.title)
      })
    },
    getCommentData() {
      const endpoint = `/api/blogs/${this.slug}/comments/`
      apiService(endpoint).then((data) => {
        this.comments.push(...data.results)
      })
    },
    toggleLike() {
      if (this.userLikedBlog) {
        this.unLikeBlog()
      } else {
        if (this.userDisLikedBlog) {
          this.undislikeBlog()
        } else {
          this.likeBlog()
        }
      }
    },
    toggleDislike() {
      if (this.userDisLikedBlog) {
        this.undislikeBlog()
      } else {
        if (this.userLikedBlog) {
          this.unLikeBlog()
        } else {
          this.dislikeBlog()
        }
      }
    },
    likeBlog() {
      this.likesCounter += 1
      this.userLikedBlog = true
      const endpoint = `/api/blogs/${this.blog.id}/like/`
      apiService(endpoint, 'POST')
    },
    unLikeBlog() {
      this.likesCounter -= 1
      this.userLikedBlog = false
      const endpoint = `/api/blogs/${this.blog.id}/like/`
      apiService(endpoint, 'DELETE')
    },
    dislikeBlog() {
      this.dislikesCounter += 1
      this.userDisLikedBlog = true
      const endpoint = `/api/blogs/${this.blog.id}/dislike/`
      apiService(endpoint, 'POST')
    },
    undislikeBlog() {
      this.dislikesCounter -= 1
      this.userDisLikedBlog = false
      const endpoint = `/api/blogs/${this.blog.id}/dislike/`
      apiService(endpoint, 'DELETE')
    },
    async deleteComment(comment) {
      // delete a given answer from the answers array and make a delete request to the REST API
      const endpoint = `/api/comments/${comment.id}/`
      try {
        await apiService(endpoint, 'DELETE')
        this.$delete(this.comments, this.comments.indexOf(comment))
        this.userHasAnswered = false
      } catch (err) {
        console.log(err)
      }
    },
    onSubmit() {
      if (this.commentBody) {
        const endpoint = `/api/blogs/${this.slug}/comment/`
        apiService(endpoint, 'POST', { body: this.commentBody }).then(
          (data) => {
            this.comments.unshift(data)
          }
        )
        this.commentBody = null
        if (this.error) {
          this.error = null
        }
      } else {
        this.error = 'Вы не можете отправить пустой комментарий'
      }
    },
  },

  created() {
    this.getBlogData()
    this.getCommentData()
    this.$store.dispatch('setUserInfo')
    this.getUser()
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
.blog-post-text {
  text-align: justify;
}
.fishow-votes_up__active {
  fill: cadetblue;
}
.fishow-votes_down__active {
  fill: red;
}
.fishow-votes_container {
  align-items: center;
}
.blog-post-title {
  margin-left: 30px;
  margin-top: 0;
}
</style>
