<template>
  <div>
    <div v-for="n in 3" :key="n" class="card">
      <div class="card-content">
        <h6 class="title is-6">
          <b-skeleton width="150px" :animated="animated"></b-skeleton>
        </h6>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <span>
            <b-skeleton width="100px" :animated="animated"></b-skeleton>
          </span>
        </p>
        <p class="card-footer-item">
          <b-skeleton width="50px" :animated="animated"></b-skeleton>
          <span>/</span>
          <b-skeleton width="70px" :animated="animated"></b-skeleton>
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SkeletonHotPost',
  data() {
    return {
      animated: true,
    }
  },
}
</script>

<style scoped>
.card-footer-item {
  justify-content: space-between;
  padding-left: 1.5rem;
}
.card-footer-item .b-skeleton {
  width: initial;
}
</style>
