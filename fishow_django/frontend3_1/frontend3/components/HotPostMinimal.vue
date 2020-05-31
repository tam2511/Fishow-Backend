<template>
  <div class="card">
    <div class="card-content">
      <p class="title">“{{ blog.title }}”</p>
      <p class="subtitle">
        {{ blog.author }}
      </p>
    </div>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span>
          {{ blog.created_at }}
        </span>
      </p>
      <p class="card-footer-item">
        {{ blog.category }}
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HotPostMinimal',
  props: {
    blog: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.list-post-minimal {
  margin-bottom: 10px;
}
</style>
