<template>
  <div class="tile is-vertical is-8">
    <p class="title is-4">Последние записи</p>
    <div class="tile is-parent is-vertical space-left0">
      <article class="tile is-child">
        <BlogCard :blog="blog" />
        <CommentsBlock />
      </article>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import BlogCard from '@/components/BlogCard'
import CommentsBlock from '@/components/CommentsBlock'

export default {
  layout: 'SideBarRight',
  components: {
    BlogCard,
    CommentsBlock,
  },
  computed: {
    ...mapState('blogs', ['blog']),
  },
  mounted() {
    this.getBlog(this.$route.params.slug)
  },
  methods: {
    ...mapActions('blogs', { getBlog: 'getBlog' }),
  },

  head() {
    return {
      title: 'Fishow - ' + this.blog.title,
    }
  },
}
</script>

<style scoped></style>
