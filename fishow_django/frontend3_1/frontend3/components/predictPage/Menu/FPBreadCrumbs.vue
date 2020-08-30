<template>
  <div class="breadcrumb box">
    <div class="columns">
      <div class="column">
        <nav aria-label="breadcrumbs">
          <ul>
            <li>
              <a> Россия </a>
            </li>
            <li>
              <nuxt-link to="/PredictionPage">{{ areal }}</nuxt-link>
            </li>
            <li>
              <nuxt-link to="/PredictionPage">{{ city }}</nuxt-link>
            </li>
          </ul>
        </nav>
      </div>
      <div class="column">
        <city-search />
      </div>
    </div>
  </div>
</template>

<script>
import CitySearch from '@/components/predictPage/Menu/CitySearch'
export default {
  components: {
    CitySearch,
  },
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
  margin-top: 1rem;
  text-transform: capitalize;
  /*background-color: rgba(0, 0, 0, 0.25098);*/
}
.breadcrumb a {
  color: #000000;
}
</style>
