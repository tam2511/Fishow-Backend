<template>
  <div class="tile is-vertical is-8">
    <p class="title">Последние записи</p>
    <div class="tile is-parent is-vertical">
      <article class="tile is-child">
        <BlogCard :blog="blog" />
        <p class="title">Комментарии</p>
        <div class="tile is-child is-vertical box">
          <p v-if="(comments.length === 0)">Ваш комментарий будет первым</p>
          <Comment
            v-for="(comment, index) in comments"
            :key="index"
            :comment="comment"
            :slug="$route.params.slug"
            :request-user="$auth.user"
            @deleteComment="deleteComment"
          />
        </div>
        <p class="title">Оставить комментарий</p>
        <div class="tile is-child is-vertical box">
          <div class="form-wrap">
            <label for="comment-message"></label>
            <textarea
              id="comment-message"
              v-model="commentBody"
              class="textarea"
              name="message"
              placeholder="Ваш комментарий"
            ></textarea>
          </div>
          <div v-if="error" class="alert-danger">{{ error }}</div>
          <div class="buttons">
            <b-button type="is-primary" @click="onSubmit">
              Отправить
            </b-button>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import BlogCard from '@/components/BlogCard'
import Comment from '@/components/Comment'

export default {
  layout: 'SideBarRight',
  components: {
    BlogCard,
    Comment,
  },
  data() {
    return {
      comments: [],
      commentBody: null,
      error: null,
    }
  },
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
  computed: {
    ...mapState('blogs', ['blog']),
  },
  created() {
    this.getCommentData()
  },
  methods: {
    async getCommentData() {
      const response = await this.$axios.$get(
        `/blogs/${this.$route.params.slug}/comments/`
      )
      this.comments.push(...response.results)
    },
    async onSubmit() {
      try {
        const response = await this.$axios.$post(
          `/blogs/${this.$route.params.slug}/comment/`,
          { body: this.commentBody }
        )
        this.comments.push(response)
        this.commentBody = ''
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
  },
  head() {
    return {
      title: 'Fishow - ' + this.blog.title,
    }
  },
}
</script>

<style scoped></style>
