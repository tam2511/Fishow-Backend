<template>
  <div class="container">
    your key = {{ this.fishowKey }}
    <button type="button" @click="sendKey">send request</button>
    <div>{{ msg }}</div>
    <h3 v-if="error">{{ error }}</h3>
    <div v-if="result" class="badge-green">
      Success
    </div>
  </div>
</template>

<script>
// import { apiService } from '@/plugins/api.service'

export default {
  name: 'ConfirmEmail',
  props: {
    key: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      result: false,
      msg: '',
      error: null
    }
  },
  methods: {
    sendKey() {
      // const endpoint = `/account-confirm-email/${this.fishowKey}/`
      // apiService(endpoint, 'POST', {
      //   key: this.fishowKey
      // })
      //   .then(data => {
      //     if (data === null) {
      //       this.error = 'Что то пошло не так'
      //     } else {
      //       this.msg = data
      //       this.result = true
      //     }
      //   })
      //   .catch(e => {
      //     console.log('error = ', e)
      //   })
    }
  }
}
</script>

<style scoped>
.badge-green {
  color: white;
  text-align: center;
}
</style>
