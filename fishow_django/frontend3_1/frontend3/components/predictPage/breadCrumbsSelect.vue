<template>
  <section class="hero">
    <div class="hero-body">
      <div class="container">
        <nav class="breadcrumb is-medium" aria-label="breadcrumbs">
          <ul>
            <li>
              <b-tooltip
                label="Кликнуть что бы вернуться к выбору области"
                multilined
                :always="!!areal"
                ><a href="#" @click="clear">Россия</a></b-tooltip
              >
            </li>
            <li v-if="areal" class="is-active">
              <a href="#">{{ areal }}</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    areal: {
      required: true,
    },
    city: {
      type: String,
      default: '',
    },
  },
  methods: {
    clear() {
      this.$emit('clear')
    },
  },
}
</script>

<style scoped>
.hero .breadcrumb a {
  color: #000;
}
.hero-body {
  padding-left: 0;
}
</style>
