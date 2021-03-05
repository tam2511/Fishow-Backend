<template>
  <div class="image-form">
    <button-delete @destoy="destroyMe" />
    <b-field class="file is-primary" :class="{ 'has-name': !!file }">
      <b-upload v-model="file" expanded class="file-label" @input="sendImage">
        <span class="file-cta">
          <b-icon class="file-icon" icon="upload"></b-icon>
          <span class="file-label">Нажмите что бы загрузить</span>
        </span>
        <span v-if="file" class="file-name">
          {{ file.name }}
        </span>
      </b-upload>
    </b-field>
    <textarea :id="counter" v-model="image" name="image" style="display: none">
    </textarea>
    <figure class="image">
      <img :src="image" alt="" />
    </figure>
  </div>
</template>

<script>
import ButtonDelete from '~/components/blog/buttonDelete'
export default {
  components: { ButtonDelete },
  props: {
    counter: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      file: null,
      image: null,
    }
  },
  watch: {
    image() {
      const body = {
        type: 'image',
        body: this.image,
        name: this.counter,
      }
      this.$emit('input', body)
    },
  },
  methods: {
    destroyMe() {
      this.$emit('remove', this.counter)
      this.$el.remove()
    },
    async sendImage() {
      try {
        const formData = new FormData()
        formData.append('image', this.file)
        const { data } = await this.$axios.post('/image/', formData, {
          Accept: 'application/json',
          'Content-Type': 'multipart/form-data',
        })
        this.image = data.image
      } catch (e) {
        console.error(e)
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.image-form {
  position: relative;
  margin-bottom: 10px;
}
</style>
