<template>
  <section class="section section-sm bg-gray-100">
    <div class="container">
      <div class="row row-30">
        <div class="col-lg-8">
          <div class="blog-post">
            <!-- Badge-->
            <div class="badge badge-secondary">{{ blog.category }}</div>
            <h3 class="blog-post-title">{{ blog.title }}</h3>
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
              </div>
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

              <div class="blog-post-comments">
                <!-- Post Comment-->
                <Comment
                  v-for="(comment, index) in comments"
                  :comment="comment"
                  :key="index"
                  :slug="slug"
                  :requestUser="requestUser"
                  @deleteComment="deleteComment"
                />
                <div class="comment-box">
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
            console.log(data)
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
</style>
