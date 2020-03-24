<template>
  <div class="block-aside-item">
    <!-- Heading Component-->
    <article class="heading-component">
      <div class="heading-component-inner">
        <h5 class="heading-component-title">Categories</h5>
      </div>
    </article>

    <!--Block Categories-->
    <div class="block-categories">
      <ul
        class="list-marked list-marked-categories">
        <li  v-for="category in categories">
            <a href="#">{{ category.name }}</a><span class="list-marked-counter">{{ category.count }}</span></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "blockCategories",
  data() {
    return {
        // TODO: ну тащемта это надо из АПИ получать, количество блогов и статей
      categories: [
        {
          name: "Статьи",
          count: 0
        },
        {
          name: "Блоги",
          count: 0
        }
      ]
    };
  }
};
</script>

<style scoped></style>