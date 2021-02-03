<template>
  <div class="actions-grid">
    <nuxt-link
      v-for="(item, index) in gridItems"
      :key="index"
      class="actions-grid__item"
      :to="item.url"
    >
      <div class="grid__item_svg">
        <img :src="item.svg" alt="" />
      </div>
      <div class="grid__item_title">{{ item.title }}</div>
      <div class="grid__item_body">{{ item.body }}</div>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gridItems: [
        {
          title: 'Создать свою статью',
          body: 'Опишите свои впечатления о рыбалке и поделитесь опытом!',
          url: { path: '/blog-editor' },
          svg: '/main-page/55.svg',
        },
        {
          title: 'Отчеты о рыбалке',
          body: 'Опишите свои впечатления о рыбалке и поделитесь опытом!',
          url: { path: '/blog-editor' },
          svg: '/main-page/44.svg',
        },
        {
          title: 'Статьи и блоги других авторов',
          body: 'Читайте интересные истории товарищей по рыбалке',
          url: { path: '/blogs' },
          svg: '/main-page/22.svg',
        },
        {
          title: 'База знаний рыбалова',
          body: 'Крупнейшее вики рыбаловного сообщества',
          url: { path: '/wiki' },
          svg: '/main-page/33.svg',
        },
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.nuxt-link-active {
  color: #0d0a0a;
}
.actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 15px;
  row-gap: 15px;
  @media screen and (max-width: 768px) {
    grid-template-columns: 1fr;
  }
  &__item {
    position: relative;
    min-height: 250px;
    background-color: #fff;
    background-position: right;
    background-repeat: no-repeat;
    background-size: 200px;
    padding: 20px;

    border: 1px solid rgba(206, 209, 213, 0.4);
    box-sizing: border-box;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
    transition: 0.35s;
    cursor: pointer;
    &:hover {
      box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.18);
    }
  }
}
.grid__item_title {
  font-size: 19px;
  line-height: 32px;
  width: 50%;
  font-weight: 400;
  z-index: 6;
}
.grid__item_body {
  text-align: left;
  width: 70%;
  font-weight: 300;
  z-index: 6;
}
.grid__item_svg {
  z-index: 0;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  img {
    max-height: 250px;
  }
}
</style>
