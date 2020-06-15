<template>
  <div class="tile is-vertical is-8">
    <p class="title">Последние записи</p>
    <div class="tile is-parent is-vertical">
      <article v-for="blog in blogs" :key="blog.id" class="tile is-child">
        <BlogCard :blog="blog" />
      </article>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import BlogCard from '@/components/BlogCard'

export default {
  layout: 'SideBarRight',
  middleware: 'auth',
  components: {
    BlogCard,
  },
  async fetch({ store, error }) {
    try {
      await store.dispatch('blogs/getBlogs')
    } catch (e) {
      error({
        statusCode: 503,
        message: 'Unable to fetch events at this time. Please try again.',
      })
    }
  },
  computed: {
    minPost() {
      return this.blogs.filter((blog, index) => index < 3)
    },
    ...mapState('blogs', ['blogs']),
  },
  created() {},
  head() {
    return {
      title: 'Fishow - Главная',
    }
  },
}
</script>

<style lang="scss" scoped></style>
