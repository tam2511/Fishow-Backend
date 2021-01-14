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
      <transition
        name="custom-classes-transition"
        enter-active-class="animated tada"
        leave-active-class="animated bounceOutRight"
      >
        <div class="banner_picture">
          <img src="/placeholder.png" width="400px" alt="" />
        </div>
      </transition>
    </div>

    <div class="banner-statistic"></div>
    <div v-for="item in banners" :key="item.id" class="banner-statistic__item">
      <div class="banner-statistic__title">{{ item.title }}</div>
      <div class="banner-statistic__value">{{ item.counter }}</div>
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
          title: 'Статей и блогов',
          counter: 0,
        },
        reportsCounter: {
          id: 2,
          title: 'Количество прогнозов',
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
  mounted() {},
}
</script>

<style scoped lang="scss">
.head-banner,
.banner-body {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  align-items: center;
}
.banner-body {
  width: 100%;
}
.banner_title {
  &-wrapper {
    width: 50%;
    max-height: 500px;
    & > * {
      margin: 10px 0;
    }
    .button {
      background: var(--main-color);
      border: 2px solid var(--main-color);
      box-sizing: border-box;
      border-radius: 4px;
      padding: 10px 30px;
      font-size: 16px;
      line-height: 26px;
      color: #fff;
      text-align: center;
      margin-top: 50px;
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
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  margin: 40px 0;
  &__title {
  }
  &__value {
    font-size: 46px;
    line-height: 62px;
  }
  &__item {
    margin: 0 10px;
  }
}
</style>
