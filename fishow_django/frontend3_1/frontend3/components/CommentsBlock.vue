<template>
  <div>
    <p class="title is-4">Комментарии</p>
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
    <p class="title is-4">Оставить комментарий</p>
    <create-comment @update="getData" />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Comment from '@/components/Comment'
import CreateComment from '~/components/CreateComment'

export default {
  components: {
    CreateComment,
    Comment,
  },
  data() {
    return {
      commentBody: null,
      error: null,
    }
  },
  computed: {
    ...mapState('comments', ['comments']),
  },
  mounted() {
    this.getData()
  },
  methods: {
    async deleteComment(comment) {
      const endpoint = `/comments/${comment.id}/`
      try {
        await this.$axios.delete(endpoint)
        this.getData()
      } catch (err) {
        console.log(err)
      }
    },
    getData() {
      this.getComment(this.$route.params.slug)
    },
    ...mapActions('comments', { getComment: 'getComments' }),
  },
}
</script>

<style scoped>
.title {
  padding-top: 1rem;
}
</style>
