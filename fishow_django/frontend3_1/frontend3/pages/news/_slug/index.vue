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
    this.getNews()
  },
  head() {
    return {
      title: this.news && this.news.title + ' | Fishow',
    }
  },
  methods: {
    async getNews() {
      try {
        const response = await this.$axios.get(
          `/news/${this.$route.params.slug}/`
        )
        this.news = response.data
      } catch (e) {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Что то пошло не так при загрузке новости',
          type: 'is-danger',
        })
        this.$router.push({ name: 'index' })
      }
    },
  },
}
</script>

<style scoped></style>
