<template>
  <div class="tile is-vertical is-8">
    <div class="tile is-parent is-vertical space-left0">
      <article class="tile is-child">
        <CardItem v-if="news" :liked="false" :item="news" />
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
import CardItem from '~/components/Card/CardItem'

export default {
  components: {
    CardItem,
    CommentsBlock,
    SkeletonBlogCard,
  },
  layout: 'SideBarRight',
  data() {
    return {
      news: null,
    }
  },
  mounted() {
    this.$axios.get(`/news/${this.$route.params.slug}/`).then((res) => {
      this.news = res.data
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
