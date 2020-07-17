<template>
  <div>
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
    <create-comment />
    <!--    <div class="tile is-child is-vertical box">-->
    <!--      <div class="form-wrap">-->
    <!--        <label for="comment-message"></label>-->
    <!--        <textarea-->
    <!--          id="comment-message"-->
    <!--          v-model="commentBody"-->
    <!--          class="textarea"-->
    <!--          name="message"-->
    <!--          placeholder="Ваш комментарий"-->
    <!--        ></textarea>-->
    <!--      </div>-->
    <!--      <div v-if="error" class="alert-danger">{{ error }}</div>-->
    <!--      <div class="buttons">-->
    <!--        <b-button type="is-primary" @click="onSubmit">-->
    <!--          Отправить-->
    <!--        </b-button>-->
    <!--      </div>-->
    <!--    </div>-->
  </div>
</template>

<script>
import Comment from '@/components/Comment'
import CreateComment from '~/components/CreateComment'

export default {
  components: {
    CreateComment,
    Comment,
  },
  data() {
    return {
      comments: [],
      commentBody: null,
      error: null,
    }
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
}
</script>

<style scoped></style>
