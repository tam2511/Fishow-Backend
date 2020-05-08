<template>
  <div class="container">
    <div class="row row-30">
      <div class="col-lg-8">
        <!-- Heading Component-->
        <article class="heading-component">
          <div class="heading-component-inner">
            <h5 class="heading-component-title">Последние статьи</h5>
          </div>
        </article>

        <div class="row row-30">
          <articles v-for="blog in blogs" :key="blog.pk" :blog="blog" />
        </div>
        <nav class="pagination-wrap" aria-label="Page navigation" v-if="next">
          <ul class="pagination">
            <li class="page-item active">
              <a class="page-link" href="#">1</a>
            </li>
            <li class="page-item"><a class="page-link" href="#" @click="checkNext">2</a></li>
          </ul>
        </nav>
      </div>
      <div class="col-lg-4">
        <div class="block-aside">
<!--          <block-categories />-->
<!--          <trending-news />-->
<!--          <block-tags />-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import blockCategories from '../components/blog/blockCategories'
import TrendingNews from '../components/TrendingNews'
import BlockTags from '../components/blog/blockTags'
import Articles from '../components/article/articles'
import {mapActions, mapState} from "vuex";
export default {
  name: 'Article',
  components: {
    Articles,
    BlockTags,
    TrendingNews,
    blockCategories,
  },

  computed: {
    ...mapState('blogs', ['blogs', 'next']),
  },
  methods: {
    setPageTitle(title) {
      document.title = title
    },
    checkNext() {
      this.$store.dispatch('blogs/fetchBlogs')
    },
    ...mapActions('blogs', ['fetchBlogs']),
  },
  created() {
    this.fetchBlogs()
    this.setPageTitle('Fishow - Все блоги')
  },
}
</script>

<style scoped></style>
