<template>
  <div class="tile is-vertical is-8">
    <h4 class="title is-4">Последние записи</h4>
    <div class="tile is-parent is-vertical space-left0">
      <article
        v-for="blog in blogs"
        :key="blog.id"
        class="tile is-child blog-page"
      >
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
  created() {
    this.getBlogs()
  },
  methods: {
    ...mapActions('blogs', { getBlogs: 'getBlogs' }),
  },
  head: {
    title: 'Прогноз клева рыбы, общение и новости | Fishow',
    meta: [
      {
        hid: 'description',
        name: 'description',
        content:
          'Прогноз клева рыбы. Рыболовный прогноз клёва рибы с учетом температуры води и воздуха, атмосферного давления, фаз луны и уровня воды, лучший прогноз на рыбалку.',
      },
    ],
  },
}
</script>

<style lang="scss" scoped></style>
