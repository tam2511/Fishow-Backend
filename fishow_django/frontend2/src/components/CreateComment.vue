<template>
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
            <!-- RD Mailform-->
            <form @submit.prevent="onSubmit" class="comment-box-form" >
                <div class="form-wrap">
                    <textarea
                            v-model="commentBody"
                            class="form-input"
                            id="comment-message"
                            name="message"
                            placeholder="Ваш комментарий"
                    ></textarea>
                </div>
                <div class="form-button">
                    <button class="button button-primary" type="submit">Submit</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { apiService } from '../common/api.service'

export default {
  name: 'CreateComment',
  props: {
    id: {
      required: true
    },
    slug: {
      type: String,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      blogSlug: null,
      commentBody: null,
      userName: '',
      error: null
    }
  },
  methods: {
    onSubmit () {
      // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
      if (this.commentBody) {
        const endpoint = `/api/blogs/${this.slug}/comment/`
        apiService(endpoint, 'POST', { body: this.commentBody })
          .then(data => {
            // this.comments.unshift(data)
            console.log(data)
            this.$router.push(
              {
                name: 'blog',
                params: { slug: data.comments_slug }
              }
            )
          })
        this.commentBody = null
        this.showForm = false
        if (this.error) {
          this.error = null
        }
      } else {
        this.error = "You can't send an empty answer!"
      }
    }
  },
  async beforeRouteEnter (to, from, next) {
    console.log('to.params.id = ', Number(to.params.id))
    // get the answer's data from the REST API and set two data properties for the component
    const endpoint = `/api/comments/${Number(to.params.id)}/`
    const data = await apiService(endpoint)
    return next(vm => (
      vm.commentBody = data.body,
      vm.blogSlug = data.blog_slug
    ))
  }
}
</script>

<style scoped></style>
