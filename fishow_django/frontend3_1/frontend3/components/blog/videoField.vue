<template>
  <div class="col-md-12 fishow-content">
    <div class="form-wrap">
      <div class="fishow-blog_image__close-button" @click="destroyMe">x</div>
      <textarea
        :id="counter"
        v-model="urlVideo"
        class="form-input"
        name="video"
        placeholder="ссылка на видео"
      ></textarea>
      <iframe
        width="560"
        height="315"
        :src="whomIsVideo(urlVideo)"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoField',
  props: {
    counter: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      urlVideo: '',
    }
  },
  methods: {
    whomIsVideo(fields) {
      const temp = fields.split('/')
      let result = ''
      for (let i = 0; i < temp.length; i++) {
        if (temp[i] === 'youtu.be') {
          result = 'https://www.youtube.com/embed/' + temp[temp.length - 1]
          return result
        }
        if (temp[i] === 'www.youtube.com') {
          result =
            'https://www.youtube.com/embed/' +
            temp[temp.length - 1].split('watch?v=')[0]
          return result
        }
      }
    },
    destroyMe() {
      this.$el.remove()
    },
  },
}
</script>

<style scoped></style>
