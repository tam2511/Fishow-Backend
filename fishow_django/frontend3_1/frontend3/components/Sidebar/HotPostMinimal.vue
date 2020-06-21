<template>
  <div class="card">
    <div class="card-content">
      <h6 class="title is-6">
        <nuxt-link :to="{ name: 'blog-slug', params: { slug: blog.slug } }"
          >{{ blog.title }}
        </nuxt-link>
      </h6>
    </div>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span> {{ blog.created_at }} </span>
      </p>
      <p class="card-footer-item">{{ blog.author }} / {{ blog.category }}</p>
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

<style scoped></style>
