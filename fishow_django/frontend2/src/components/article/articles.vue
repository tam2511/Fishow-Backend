<template>
  <div class="col-md-6">
    <!-- Post Creative-->
    <article class="post-creative">
      <div class="post-creative-content">
        <div class="post-creative-header">
          <!-- Badge-->
          <div class="badge" :class="categ">{{ blog.category }}</div>
          <time class="post-creative-time" datetime="2018">{{
            blog.created_at
          }}</time>
          <div class="post-creative-view">
            <span class="icon fl-justicons-visible6"></span>234
          </div>
        </div>
        <h4 class="post-creative-title">
          <router-link :to="{ name: 'blog', params: { slug: blog.slug } }">{{
            blog.title
          }}</router-link>
        </h4>
      </div>
      <a class="post-creative-figure" href="blog-post.html"
        ><img alt="" width="370" height="279"
      /></a>
      <div class="post-creative-footer">
        <div class="post-creative-comment">
          <span class="icon mdi mdi-comment-outline"></span
          ><a href="#">{{ commentCount }} Comments</a>
        </div>
        <div class="post-creative-share">
          <div class="inline-toggle-parent">
            <span class="post-creative-share-text">Share</span>
            <div class="inline-toggle icon material-icons-share"></div>
            <div class="inline-toggle-element">
              <ul class="list">
                <li><a class="icon fa-facebook" href="#"></a></li>
                <li><a class="icon fa-twitter" href="#"></a></li>
                <li><a class="icon fa-google-plus" href="#"></a></li>
                <li><a class="icon fa-instagram" href="#"></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: 'articles',
  props: ['blog'],
  computed: {
    categ: function () {
      if (this.blog.category === 'Блоги') {
        return 'badge-secondary'
      } else {
        return 'badge-primary'
      }
    },
  },
}
</script>

<style scoped></style>
