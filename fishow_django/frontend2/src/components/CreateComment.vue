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
    <h2>lalala</h2>
    <div class="comment-box-main">
      <!--      <h5 class="comment-box-name">{{ this.requestUser }}</h5>-->
      <!-- RD Mailform-->
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
          <button
            v-if="username !== undefined"
            class="button button-primary"
            type="submit"
          >
            Отправить - username = {{ username }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { apiService } from '../common/api.service'
import { mapState } from 'vuex'

export default {
  name: 'CreateComment',
  props: {
    id: {
      required: true,
    },
    slug: {
      type: String,
      required: true,
    },
    // requestUser: {
    //   required: true,
    // },
    comments: {
      type: Array,
    },
  },
  data() {
    return {
      blogSlug: null,
      commentBody: null,
      error: null,
    }
  },
  computed: {
    ...mapState(['username']),
  },
  methods: {},
  async beforeRouteEnter(to, from, next) {
    console.log('to.params.id = ', Number(to.params.id))
    // get the answer's data from the REST API and set two data properties for the component
    const endpoint = `/api/comments/${Number(to.params.id)}/`
    const data = await apiService(endpoint)
    return next(
      (vm) => ((vm.commentBody = data.body), (vm.blogSlug = data.blog_slug))
    )
  },
  created() {
    console.log('this.username =', this.username)
    // console.log('this.requestUser =', this.requestUser)
  },
}
</script>

<style scoped>
.alert-danger {
  padding: 5px;
}
</style>
