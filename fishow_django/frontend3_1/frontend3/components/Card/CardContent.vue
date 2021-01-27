<template>
  <div class="content">
    <div class="media pre-header">
      <div class="media-content">
        <h2 class="title">
          <nuxt-link :to="{ name: '-slug', params: { slug: item.slug } }"
            >{{ item.title }}
          </nuxt-link>
        </h2>
      </div>
    </div>
    <div v-for="p in getResult" :key="p.id" :class="p.type + '_container'">
      <p v-if="p.type === 'text'" class="post-text">{{ p.body }}</p>
      <iframe
        v-if="p.type === 'video'"
        width="560"
        height="315"
        :src="p.url"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        name="video"
      ></iframe>
      <figure v-if="p.type === 'image'" class="image is-fullwidth">
        <img :src="p.url" alt="" />
      </figure>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardContent',
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  computed: {
    getResult() {
      try {
        return JSON.parse(this.item.content).blocks[0]
      } catch (e) {
        return null
      }
    },
  },
}
</script>

<style scoped></style>
