<template>
  <div class="col-md-6 col-lg-12">
    <!-- Heading Component-->
    <article class="heading-component">
      <div class="heading-component-inner">
        <h5 class="heading-component-title">Player Awards</h5>
      </div>
    </article>

    <!-- Owl Carousel-->
    <div
      class="owl-carousel owl-carousel-dots-modern awards-carousel"
      data-items="1"
      data-autoplay="true"
      data-autoplay-speed="4000"
      data-dots="true"
      data-nav="false"
      data-stage-padding="0"
      data-loop="true"
      data-margin="0"
      data-mouse-drag="true"
    >
      <!-- Awards Item-->
      <div class="awards-item">
        <div class="awards-item-main">
          <h4 class="awards-item-title">
            <span class="text-accent">World</span>Champions
          </h4>
          <div class="divider"></div>
          <h5 class="awards-item-time">December 2014</h5>
        </div>
        <div class="awards-item-aside">
          <img
            src="/static/assets/images/thumbnail-minimal-1-67x147.png"
            alt=""
            width="67"
            height="147"
          />
        </div>
      </div>
      <!-- Awards Item-->
      <div class="awards-item">
        <div class="awards-item-main">
          <h4 class="awards-item-title">
            <span class="text-accent">Best</span>Forward
          </h4>
          <div class="divider"></div>
          <h5 class="awards-item-time">June 2015</h5>
        </div>
        <div class="awards-item-aside">
          <img
            src="/static/assets/images/thumbnail-minimal-2-68x126.png"
            alt=""
            width="68"
            height="126"
          />
        </div>
      </div>
      <!-- Awards Item-->
      <div class="awards-item">
        <div class="awards-item-main">
          <h4 class="awards-item-title">
            <span class="text-accent">Best</span>Coach
          </h4>
          <div class="divider"></div>
          <h5 class="awards-item-time">November 2016</h5>
        </div>
        <div class="awards-item-aside">
          <img
            src="/static/assets/images/thumbnail-minimal-3-73x135.png"
            alt=""
            width="73"
            height="135"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserAwards',
}
</script>

<style scoped></style>
