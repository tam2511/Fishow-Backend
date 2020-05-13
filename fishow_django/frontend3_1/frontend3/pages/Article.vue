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
        <nav v-if="next" class="pagination-wrap" aria-label="Page navigation">
          <ul class="pagination">
            <li class="page-item active">
              <a class="page-link" href="#">1</a>
            </li>
            <li class="page-item">
              <a class="page-link" href="#" @click="checkNext">2</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="col-lg-4">
        <div class="block-aside">
          <block-categories />
          <trending-news />
          <block-tags />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import blockCategories from '../components/blog/blockCategories'
import TrendingNews from '../components/TrendingNews'
import BlockTags from '../components/blog/blockTags'
import Articles from '../components/article/articles'
export default {
  name: 'Article',
  components: {
    Articles,
    BlockTags,
    TrendingNews,
    blockCategories
  },
  head() {
    return {
      title: 'Fishow - Все блоги'
    }
  },
  computed: {
    ...mapState('blogs', ['blogs', 'next'])
  },

  methods: {
    checkNext() {
      this.$store.dispatch('blogs/fetchBlogs')
    },
    ...mapActions('blogs', ['fetchBlogs'])
  },
  created() {
    this.fetchBlogs()
  }
}
</script>

<style scoped></style>
