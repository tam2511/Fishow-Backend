<template>
  <div v-show="active" class="banner_overlay">
    <div class="banner_container card">
      <section>
        <b-carousel :progress="progress" :progress-type="progressType">
          <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
            <section :class="`hero is-medium is-${carousel.color}`">
              <img :src="carousel.pic" alt="" />
            </section>
          </b-carousel-item>
        </b-carousel>
      </section>
      <div class="field">
        <b-checkbox v-model="checkbox">Больше не показывать</b-checkbox>
      </div>
      <b-button @click="close">Close</b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      active: false,
      checkbox: false,
      progress: true,
      progressType: 'is-primary',
      carousels: [
        { title: 'Slide 1', color: 'grey', pic: '/tutorial/blog.png' },
        { title: 'Slide 2', color: 'dark', pic: '/tutorial/open_blog.png' },
        { title: 'Slide 3', color: 'primary', pic: '/tutorial/prediction.png' },
      ],
    }
  },
  created() {
    if (process.browser) {
      if (
        !sessionStorage.getItem('banner_showed') &&
        !localStorage.getItem('banner_closed')
      ) {
        this.active = true
        sessionStorage.setItem('banner_showed', true)
      }
    }
  },
  methods: {
    close() {
      this.$el.remove()

      if (this.checkbox) localStorage.setItem('banner_closed', true)
    },
  },
}
</script>

<style scoped>
.banner_overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.54);

  z-index: 1000;
}
.banner_container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  min-width: 200px;
  width: 100%;
  max-width: 700px;
  height: auto;
}
</style>
