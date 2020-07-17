<template>
  <div>
    <article class="heading-component">
      <div class="heading-component-inner">
        <h5 class="heading-component-title">Горячие новости</h5>
      </div>
    </article>

    <div id="tabs-modern" class="tabs-custom tabs-horizontal tabs-modern">
      <ul class="nav nav-tabs">
        <li class="nav-item" role="presentation">
          <a class="nav-link active" href="#tabs-modern-1" data-toggle="tab"
            >Новые</a
          >
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" href="#tabs-modern-2" data-toggle="tab"
            >Горячие</a
          >
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" href="#tabs-modern-3" data-toggle="tab"
            >Популярные</a
          >
        </li>
      </ul>
      <div class="tab-content">
        <div id="tabs-modern-1" class="tab-pane fade show active">
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-1-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html">ЗАГОЛОВОК</a>
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
          <!-- Post Classic-->
        </div>
        <div id="tabs-modern-2" class="tab-pane fade">
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-5-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html"
                  >VOTE: PICK THE WINNERS IN THE NBA CONFERENCE SEMIFINALS</a
                >
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-6-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html"
                  >WHO WAS THE MOST SURPRISING TOP-100 PLAYER</a
                >
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-7-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html"
                  >DEMAR DEROZAN HAD 42 POINTS, AND THE TORONTO RAPTORS</a
                >
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
        </div>
        <div id="tabs-modern-3" class="tab-pane fade">
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-8-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html"
                  >FORECAST: PREDICTIONS FOR EACH CONFERENCE SEMIFINAL</a
                >
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
          <!-- Post Classic-->
          <article class="post-classic">
            <div class="post-classic-aside">
              <a class="post-classic-figure" href="blog-post.html"
                ><img
                  src="images/blog-element-9-94x94.jpg"
                  alt=""
                  width="94"
                  height="94"
              /></a>
            </div>
            <div class="post-classic-main">
              <p class="post-classic-title">
                <a href="blog-post.html"
                  >WHO WAS THE MOST SURPRISING TOP-100 PLAYER</a
                >
              </p>
              <div class="post-classic-time">
                <span class="icon mdi mdi-clock"></span>
                <time datetime="2018"
                  >April 15, 2018
                  <!-- Tabs Modern with Post Classic-->
                </time>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TrendingNews',
}
</script>

<style scoped></style>
