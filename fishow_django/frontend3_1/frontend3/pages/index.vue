<template>
  <div class="tile is-vertical is-8">
    <p class="title is-4">Последние записи</p>
    <div class="tile is-parent is-vertical space-left0">
      <article v-for="blog in blogs" :key="blog.id" class="tile is-child">
        <BlogCard :blog="blog" />
      </article>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import BlogCard from '@/components/BlogCard'

export default {
  layout: 'SideBarRight',
  components: {
    BlogCard,
  },
  computed: {
    ...mapState('blogs', ['blogs']),
  },
  mounted() {
    this.getBlogs()
  },
  methods: {
    ...mapActions('blogs', { getBlogs: 'getBlogs' }),
  },
  head: {
    title: 'Fishow - Главная',
    meta: [
      {
        hid: 'description',
        name: 'description',
        content: 'Home page description',
      },
    ],
  },
}
</script>

<style lang="scss" scoped></style>
