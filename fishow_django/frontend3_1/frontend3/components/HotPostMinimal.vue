<template>
  <div class="list-post-minimal">
    <!-- Post Minimal-->
    <article class="post-minimal">
      <div class="post-classic-main">
        <p class="post-classic-title">
          <router-link :to="{ name: 'blog', params: { slug: blog.slug } }">
            {{ blog.title }}
          </router-link>
        </p>
        <div class="post-minimal_comments">
          <div class="badge badge-primary">{{ blog.category }}</div>
          <time class="post-classic-time">
            {{ blog.created_at }}
          </time>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: 'HotPostMinimal',
  props: {
    blog: {
      type: String,
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
