<template>
  <div class="player-info-corporate">
    <div class="player-info-figure">
      <div class="block-number"><span>11</span></div>
      <div class="player-img">
        <img src="/static/assets/index.jpeg" alt="" width="200" height="200" />
      </div>
    </div>
    <div class="player-info-main">
      <h4 class="player-info-title">{{ username }}</h4>
      <p class="player-info-subtitle">Пользователь</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserMain',
  props: {
    username: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped>
.player-info-corporate .player-img img {
  max-width: initial;
  min-width: initial;
}
</style>
