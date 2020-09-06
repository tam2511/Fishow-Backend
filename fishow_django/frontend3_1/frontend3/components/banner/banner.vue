<template>
  <div v-show="active" class="banner_overlay">
    <div class="banner_container card">
      <div class="banner-title">
        banner-title
      </div>
      <div class="banner-content">
        banner content
      </div>
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
    }
  },
  created() {
    if (process.browser) {
      if (
        !sessionStorage.getItem('banner_showed') &&
        !localStorage.getItem('banner_closed')
      ) {
        this.active = true
        console.log('this.active = true')
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
  height: auto;
}
</style>
