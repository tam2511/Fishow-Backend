<template>
  <div class="tile is-vertical is-8">
    <div class="tile is-parent is-vertical space-left0">
      <article class="tile is-child">
        <!--        <pre class="language-json"><code>{{ blog  }}</code></pre>-->
        <report-card v-if="report" :report="report" />
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
import ReportCard from '~/components/ReportCard'

export default {
  components: {
    ReportCard,
    CommentsBlock,
    SkeletonBlogCard,
  },
  layout: 'sideBarRight',
  data() {
    return {
      report: null,
    }
  },
  head() {
    return {
      title: this.report && this.report.title + ' | Fishow',
    }
  },
  async mounted() {
    await this.$axios.get(`/report/${this.$route.params.slug}/`).then((res) => {
      this.report = res.data
    })
  },
}
</script>

<style scoped></style>
