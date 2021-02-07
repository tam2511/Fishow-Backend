<template>
  <section>
    <b-notification
      v-if="!$route.params.key"
      type="is-danger"
      has-icon
      :closable="false"
      aria-close-label="Close notification"
      role="alert"
    >
      Вы не указали ключ подтверждения
    </b-notification>
    <b-notification v-else :closable="false">
      <b-notification
        v-if="success"
        type="is-success"
        has-icon
        aria-close-label="Close notification"
        :closable="false"
      >
        Аккаунт успешно подтвержден!
      </b-notification>

      <b-notification
        v-if="error"
        type="is-warning"
        has-icon
        aria-close-label="Close notification"
        role="alert"
      >
        Что пошло не так, возможно неверный код
      </b-notification>

      <b-loading
        :is-full-page="isFullPage"
        :active.sync="isLoading"
        :can-cancel="true"
      >
      </b-loading>
    </b-notification>
  </section>
</template>

<script>
import confserver from '~/confserver'
export default {
  data() {
    return {
      key: this.$route.params.key,
      isLoading: true,
      isFullPage: true,
      success: false,
      error: null,
    }
  },
  mounted() {
    this.sendKey()
  },
  methods: {
    openLoading() {
      this.isLoading = true
      setTimeout(() => {
        this.isLoading = false
      }, 5 * 1000)
    },
    async sendKey() {
      try {
        const response = await this.$axios.$post(
          `/account-confirm-email/${this.key}/`,
          { key: this.key },
          {
            baseURL: `https://${confserver.ip}/`,
            withCredentials: false,
          }
        )
        if (response.detail === 'ok') {
          this.success = true
          this.isLoading = false
        }
      } catch (e) {
        this.error = true
        this.isLoading = false
      }
    },
  },
}
</script>

<style scoped></style>
