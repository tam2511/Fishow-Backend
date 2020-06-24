<template>
  <div class="data-pick">
    <div class="buttons">
      <b-button icon-right="arrow-left" pack="fas" @mouseenter="moveLeft" />
      <div class="carousel-slides">
        <div class="slides" :style="'margin-left:' + marginLeft + 'px'">
          <b-button v-for="day in tenDays" :key="day.id" type="is-link">
            {{ day }}
          </b-button>
        </div>
      </div>
      <b-button icon-right="arrow-right" pack="fas" @mouseenter="moveRight" />
    </div>
  </div>
</template>

<script>
import getData from '~/assets/js/getData'
export default {
  props: {
    days: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      marginLeft: 0,
    }
  },
  methods: {
    moveRight() {
      this.marginLeft -= 100
    },
    moveLeft() {
      this.marginLeft += 100
    },
  },
  computed: {
    tenDays() {
      return getData(this.days, 9)
    },
  },
}
</script>

<style scoped lang="scss">
.data-pick {
  display: flex;
  flex-flow: row;
}
.is-link {
  background-color: #204a6f85;
}
.carousel-slides {
  max-width: 300px;
  overflow: hidden;
  display: flex;
  flex-flow: row;
}
.slides {
  width: 100%;
  display: flex;
}
</style>
