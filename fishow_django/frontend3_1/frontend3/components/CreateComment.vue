<template>
  <article class="media box">
    <figure class="media-left">
      <p class="image is-64x64">
        <img src="https://bulma.io/images/placeholders/128x128.png" />
      </p>
    </figure>
    <div class="media-content">
      <div class="field">
        <p class="control">
          <textarea
            v-model="commentBody"
            class="textarea"
            placeholder="Ваш комментарий..."
          ></textarea>
        </p>
      </div>
      <nav class="level">
        <div class="level-left">
          <div class="level-item">
            <b-button
              type="is-primary"
              :disabled="!$auth.user"
              @click="onSubmit"
              >Отправить</b-button
            >
          </div>
        </div>
      </nav>
    </div>
  </article>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  data() {
    return {
      commentBody: null,
    }
  },
  methods: {
    async onSubmit() {
      // this.postBlogComment(this.$route.params.slug, this.commentBody)
      try {
        await this.$axios.$post(`/blogs/${this.$route.params.slug}/comment/`, {
          body: this.commentBody,
        })
        this.$emit('update')
        this.commentBody = ''
      } catch (e) {
        // console.log('error = ', e)
      }
    },
    ...mapActions('comments', { writeComments: 'writeComments' }),
  },
}
</script>

<style scoped></style>
