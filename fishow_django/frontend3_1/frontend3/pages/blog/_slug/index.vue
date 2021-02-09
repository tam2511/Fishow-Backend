<template>
  <div class="tile is-vertical is-8">
    <div class="tile is-parent is-vertical space-left0">
      <article class="tile is-child">
        <!--        <pre class="language-json"><code>{{ blog  }}</code></pre>-->
        <BlogCard v-if="blog" :blog="blog" />
        <div v-else>
          <SkeletonBlogCard />
        </div>
        <CommentsBlock />
      </article>
    </div>
  </div>
</template>

<script>
import CommentsBlock from '@/components/CommentsBlock'
import SkeletonBlogCard from '@/components/Skeleton/SkeletonBlogCard'
import BlogCard from '~/components/BlogCard'

export default {
  components: {
    BlogCard,
    CommentsBlock,
    SkeletonBlogCard,
  },
  layout: 'sideBarRight',
  data() {
    return {
      blog: null,
    }
  },
  mounted() {
    this.$axios.get(`/blogs/${this.$route.params.slug}/`).then((res) => {
      this.blog = res.data
    })
  },
  head() {
    return {
      title: this.blog && this.blog.title + ' | Fishow',
    }
  },
}
</script>

<style scoped></style>
