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
import { mapState } from 'vuex'
import { apiService } from '@/plugins/api.service'

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
    // requestUser: {
    //   required: true,
    // },
    comments: {
      type: Array
    }
  },
  data() {
    return {
      blogSlug: null,
      commentBody: null,
      error: null
    }
  },
  computed: {
    ...mapState(['username'])
  },
  created() {},
  methods: {},
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    const endpoint = `/api/comments/${Number(to.params.id)}/`
    const data = await apiService(endpoint)
    return next(
      (vm) => ((vm.commentBody = data.body), (vm.blogSlug = data.blog_slug))
    )
  }
}
</script>

<style scoped>
.alert-danger {
  padding: 5px;
}
</style>
