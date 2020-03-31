<template>
    <div>
        <!-- Section Breadcrumbs-->

        <!-- News 4-->
        <section class="section section-sm bg-gray-100">
            <div class="container">
                <div class="row row-30">
                    <div class="col-lg-8">
                        <!-- Heading Component-->
                        <article class="heading-component">
                            <div class="heading-component-inner">
                                <h5 class="heading-component-title">Последние статьи
                                </h5>
                            </div>
                        </article>

                        <div class="row row-30">
                            <articles v-for="blog in blogs"
                                      :key="blog.pk"
                                      :author="blog.author"
                                      :title="blog.title"
                                      :time="blog.created_at"
                                      :slug="blog.slug"
                                      :commentCount="blog.comments_count"   />

                        </div>
                        <nav class="pagination-wrap" aria-label="Page navigation">
                            <ul class="pagination">
                                <li class="page-item active"><a class="page-link" href="#">1</a></li>
                                <li class="page-item"><a class="page-link" href="#">2</a></li>
                                <li class="page-item"><a class="page-link" href="#">3</a></li>
                                <li class="page-item"><span class="page-link">...</span></li>
                                <li class="page-item"><a class="page-link" href="#">14</a></li>
                            </ul>
                        </nav>
                    </div>
                    <div class="col-lg-4">
                        <div class="block-aside">
                            <block-categories/>
                            <trending-news/>
                            <block-tags/>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Page Footer-->
    </div>
</template>

<script>
import { apiService } from '../common/api.service'
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
  data () {
    return {
      blogs: []
    }
  },
  methods: {
    getBlogs () {
      let endpoint = '/api/blogs/'
      if (this.next) {
        endpoint = this.next
      }
      this.loadingBlogs = true
      apiService(endpoint).then(data => {
        this.blogs.push(...data.results)
        if (data.next) {
          this.next = data.next
        } else {
          this.next = null
        }
      })
    }
  },
  created () {
    this.getBlogs()
  }
}
</script>

<style scoped>

</style>
