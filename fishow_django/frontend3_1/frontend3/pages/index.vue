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
import { mainPage } from '~/assets/descriptions'

export default {
  components: {
    ActivityRating,
    SiteNews,
    ActionsGrid,
    PredictionSection,
    Banner,
  },
  head() {
    return {
      title: mainPage.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: mainPage.description,
        },
        {
          name: 'yandex-verification',
          content: 'cb0c04b5c0271e26',
        },
      ],
    }
  },
}
</script>
