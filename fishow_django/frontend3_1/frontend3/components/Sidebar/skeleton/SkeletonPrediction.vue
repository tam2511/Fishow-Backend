<template>
  <section>
    <div class="media">
      <div class="media-left">
        <b-skeleton width="100px" :animated="animated"></b-skeleton>
      </div>
      <div class="media-right">
        <b-skeleton width="80px" :animated="animated"></b-skeleton>
        <b-skeleton width="100px" :animated="animated"></b-skeleton>
        <b-skeleton width="150px" :animated="animated"></b-skeleton>
      </div>
    </div>
    <div class="body">
      <b-skeleton width="80%" :animated="animated"></b-skeleton>
    </div>
    <div class="progressbar-footer">
      <b-skeleton :animated="animated"></b-skeleton>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      animated: true,
    }
  },
}
</script>

<style scoped>
.media-right {
  display: flex;
  flex-flow: column;
  align-items: flex-end;
}
.media-right .b-skeleton {
  width: initial;
  display: inline-block;
}
</style>
