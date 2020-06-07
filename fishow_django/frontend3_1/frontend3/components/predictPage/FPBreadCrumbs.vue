<template>
  <nav class="breadcrumb is-centered" aria-label="breadcrumbs">
    <ul>
      <li>
        <nuxt-link to="/PredictionPage">{{ areal }}</nuxt-link>
      </li>
      <li>
        <nuxt-link to="/PredictionPage">{{ city }}</nuxt-link>
      </li>
      <li>
        <a href="#">{{ fish }}</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
    areal: {
      type: String,
      required: true,
    },
    city: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
    fish: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped>
.breadcrumb {
  text-transform: capitalize;
}
</style>
