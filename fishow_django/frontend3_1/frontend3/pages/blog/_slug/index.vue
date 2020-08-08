<template>
  <div class="tile is-vertical is-8">
    <p class="title is-4">Последние записи</p>
    <div class="tile is-parent is-vertical">
      <article class="tile is-child">
        <BlogCard :blog="blog" />
        <CommentsBlock />
      </article>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import BlogCard from '@/components/BlogCard'
import CommentsBlock from '@/components/CommentsBlock'

export default {
  layout: 'SideBarRight',
  components: {
    BlogCard,
    CommentsBlock,
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

  head() {
    return {
      title: 'Fishow - ' + this.blog.title,
    }
  },
}
</script>

<style scoped></style>
