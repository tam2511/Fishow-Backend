<template>
  <div class="head-banner">
    <div class="banner-body">
      <div class="banner_title-wrapper">
        <h1 class="banner_title">Вместе мы улучшаем качество прогноза клева</h1>
        <h3 class="banner_title">
          Ваши отчеты помогают спрогнозировать результаты рыбалки
        </h3>
        <nuxt-link :to="{ path: '/blog-editor' }" class="button is-primary">
          Оставить отчет
        </nuxt-link>
      </div>
      <div class="banner_picture">
        <img src="/61.png" height="400" alt="" />
      </div>
    </div>
    <div class="banner-statistic">
      <div
        v-for="item in banners"
        :key="item.id"
        class="banner-statistic__item"
      >
        <div class="banner-statistic__title">{{ item.title }}</div>
        <div class="banner-statistic__value">{{ item.counter }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      banners: {
        predictionCounter: {
          id: 0,
          title: 'Точность прогноза',
          counter: 0,
        },
        blogsCounter: {
          id: 1,
          title: 'Количество статей',
          counter: 0,
        },
        reportsCounter: {
          id: 2,
          title: 'Количество отчетов',
          counter: 0,
        },
        userCounter: {
          id: 3,
          title: 'К нам присоединилось',
          counter: 0,
        },
      },
    }
  },
  mounted() {
    this.getUsers()
    this.getBlogs()
    this.getReports()
  },
  methods: {
    async getUsers() {
      try {
        const { data } = await this.$axios.get('/count/user/')
        this.banners.userCounter.counter = data[0].count_user
      } catch (e) {
        console.error('errro =', e)
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Не удалось загрузить статистику по пользователям',
          type: 'is-danger',
        })
      }
    },
    async getBlogs() {
      try {
        const { data } = await this.$axios.get('/count/blogs/')
        this.banners.blogsCounter.counter = data[0].count_blogs
      } catch (e) {
        console.error('errro =', e)
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Не удалось загрузить статистику по блогам.',
          type: 'is-danger',
        })
      }
    },
    async getReports() {
      try {
        const { data } = await this.$axios.get('/count/report/')
        this.banners.reportsCounter.counter = data[0].count_report
      } catch (e) {
        console.error('errro =', e)
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Не удалось загрузить статистику по отчетам.',
          type: 'is-danger',
        })
      }
    },
  },
}
</script>

<style scoped lang="scss">
.head-banner,
.banner-body {
  position: relative;
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  align-items: center;
}
.banner-body {
  width: 100%;
  height: 300px;
  position: relative;
  overflow: hidden;
  border-radius: 0 25px 25px 0;
}
.banner_title {
  &-wrapper {
    width: 50%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    .button {
      padding: 10px 30px;
      @media screen and (max-width: 500px) {
        width: 100%;
      }
    }
  }
  @media screen and (max-width: 768px) {
    &-wrapper {
      width: 100%;
      margin: 0 10px;
    }
  }
}
h1.banner_title {
  font-size: 36px;
  line-height: 48px;
}
h3.banner_title {
  font-size: 20px;
  line-height: 32px;
}

.banner-statistic {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  justify-items: stretch;
  margin-top: 40px;
  @media screen and (max-width: 500px) {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
  }
  &__value {
    font-size: 46px;
    line-height: 62px;
    @media screen and (max-width: 500px) {
      font-size: 30px;
      line-height: 42px;
    }
  }
  &__item {
    margin: 0 10px;
    justify-self: center;
  }
}
.banner_picture {
  position: absolute;
  right: 0;
  bottom: 0;
  pointer-events: none;
  @media screen and (max-width: 880px) {
    display: none;
  }
}
</style>
