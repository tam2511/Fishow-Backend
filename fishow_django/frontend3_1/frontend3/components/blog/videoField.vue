<template>
  <div>
    <b-field style="position: relative">
      <button-delete @destoy="destroyMe" />
      <b-input
        :id="counter"
        v-model="urlVideo"
        maxlength="200"
        type="text"
        placeholder="Cсылка на видео"
        :has-counter="false"
        style="width: 100%; resize: none"
      >
      </b-input>
    </b-field>
    <iframe
      width="560"
      :height="iframeHeight"
      :src="whomIsVideo(urlVideo)"
      frameborder="0"
      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
import ButtonDelete from '~/components/blog/buttonDelete'
export default {
  name: 'VideoField',
  components: { ButtonDelete },
  props: {
    counter: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      urlVideo: '',
      iframeHeight: 0,
    }
  },
  watch: {
    urlVideo(val) {
      this.iframeHeight = val ? 300 : 0
      const body = {
        type: 'video',
        body: val,
        name: this.counter,
      }
      this.$emit('input', body)
    },
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
      this.$emit('remove', this.counter)
      this.$el.remove()
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrap {
  position: relative;
}
</style>
