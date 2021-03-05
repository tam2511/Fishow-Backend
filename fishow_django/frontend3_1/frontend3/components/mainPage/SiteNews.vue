<template>
  <div class="site-news">
    <div class="site-news__title">
      <h2 class="title">Новости</h2>
    </div>
    <div class="site-news__container">
      <div
        v-for="(item, index) in news"
        :key="index"
        class="site-news__item-container"
      >
        <div class="site-news__header">{{ item.created_at }}</div>
        <div class="site-news__body">
          <nuxt-link
            :to="{ name: 'news-slug', params: { slug: item.slug } }"
            class="site-news__link"
            >{{ item.title }}
          </nuxt-link>
        </div>
      </div>
    </div>
    <div class="site-news__footer">
      <a href="#">Все новости ></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteNews',
  data() {
    return {
      news: null,
    }
  },
  mounted() {
    this.getNews()
  },
  methods: {
    async getNews() {
      const response = await this.$axios.get('/news/')

      this.news = response.data.results.slice(0, 3)
    },
  },
}
</script>

<style scoped lang="scss">
.site-news {
  display: flex;
  flex-flow: column;
  margin: 40px 0;
  &__link {
    color: var(--color-type-brand);
    &:hover {
      color: var(--color-type-hover);
    }
  }
  &__title {
    h2 {
      font-weight: 500;
    }
  }
  &__container {
    display: flex;
    flex-flow: row wrap;
  }
  &__item-container {
    margin: 20px 0;
    width: 33%;
    padding: 10px 10px 0 0;
  }
  &__header {
    color: #878b90;
  }
  &__footer {
    padding: 10px 0;
  }
  @media screen and (max-width: 768px) {
    &__item-container {
      width: 100%;
    }
    margin: 40px 10px;
  }
}
</style>
