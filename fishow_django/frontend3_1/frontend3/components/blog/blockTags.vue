<template>
  <div class="block-aside-item">
    <!-- Heading Component-->
    <article class="heading-component">
      <div class="heading-component-inner">
        <h5 class="heading-component-title">Теги</h5>
      </div>
    </article>

    <!-- List Tags-->
    <ul class="list-tags">
      <li v-for="ctag in ctags" :key="ctag.name">
        <a href="#">{{ ctag.name }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'BlockTags',
  data() {
    return {
      // TODO: эт получать надо из блога, а не тут прописывать, но пока так.
      ctags: [
        { name: 'Снаряжение' },
        { name: 'История' },
        { name: 'Отчет' },
        { name: 'Видео' },
        { name: 'Опрос' }
      ]
    }
  }
}
</script>

<style scoped></style>
