<template>
  <div>
    <p class="title is-4">Комментарии</p>
    <div v-if="comments" class="tile is-child is-vertical box">
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
    <p class="title is-4">Оставить комментарий</p>
    <create-comment @update="getData" />
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
      comments: null,
      error: null,
    }
  },
  mounted() {
    this.$axios
      .get(`/blogs/${this.$route.params.slug}/comments/`)
      .then((res) => {
        this.comments = res.data.results
      })
  },
  methods: {
    async deleteComment(comment) {
      const endpoint = `/comments/${comment.id}/`
      try {
        await this.$axios.delete(endpoint)
        this.getData()
      } catch (err) {
        // console.log(err)
      }
    },
    getData() {
      this.$axios
        .get(`/blogs/${this.$route.params.slug}/comments/`)
        .then((res) => {
          this.comments = res.data.results
        })
    },
  },
}
</script>

<style scoped>
.title {
  padding-top: 1rem;
}
</style>
