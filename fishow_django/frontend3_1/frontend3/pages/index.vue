<template>
  <section>
    <div class="container">
      <Banner />
      <PredictionSection />
      <ActionsGrid />
      <SiteNews />
      <ActivityRating />
    </div>
  </section>
</template>

<script>
import Banner from '~/components/mainPage/Banner'
import PredictionSection from '~/components/mainPage/PredictionSection'
import ActionsGrid from '~/components/mainPage/ActionsGrid'
import SiteNews from '~/components/mainPage/SiteNews'
import ActivityRating from '~/components/mainPage/ActivityRating'

export default {
  components: {
    ActivityRating,
    SiteNews,
    ActionsGrid,
    PredictionSection,
    Banner,
  },
}
</script>

<style lang="scss" scoped></style>
