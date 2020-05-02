<template>
  <div class="container">
    your key = {{ this.fishowKey }}
    <button type="button" @click="sendKey">send request</button>
    <div>{{ msg }}</div>
    <h3 v-if="error">{{ error }}</h3>
    <div class="badge-green" v-if="result">
      Success
    </div>
  </div>
</template>

<script>
import { apiService } from '../common/api.service'

export default {
  name: 'confirmEmail',
  data() {
    return {
      result: false,
      msg: '',
      error: null,
    }
  },
  props: ['fishowKey'],
  methods: {
    sendKey() {
      const endpoint = `/account-confirm-email/${this.fishowKey}/`
      apiService(endpoint, 'POST', {
        key: this.fishowKey,
      })
        .then((data) => {
          if (data === null) {
            this.error = 'Что то пошло не так'
          } else {
            this.msg = data
            this.result = true
            console.log('this.data = ', data)
          }
        })
        .catch((e) => {
          console.log('error = ', e)
        })
    },
  },
}
</script>

<style scoped>
.badge-green {
  color: white;
  text-align: center;
}
</style>
