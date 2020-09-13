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
import { mapState, mapActions } from 'vuex'
// import axios from 'axios'
import CommentsBlock from '@/components/CommentsBlock'
import SkeletonBlogCard from '@/components/Skeleton/SkeletonBlogCard'
import BlogCard from '~/components/BlogCard'

export default {
  components: {
    BlogCard,
    CommentsBlock,
    SkeletonBlogCard,
  },
  // asyncData({ params }) {
  //   return axios
  //     .get(`http://127.0.0.1:8000/api/blogs/${params.slug}/`)
  //     .then((res) => {
  //       console.log(res.data)
  //       return { blog: res.data }
  //     })
  // },
  layout: 'SideBarRight',
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
      title: this.blog.title + ' | Fishow',
    }
  },
}
</script>

<style scoped></style>
