<template>
  <div class="warning-popin">
    <b-notification
      type="is-primary"
      has-icon
      aria-close-label="Close notification"
      class="notification-editor"
      :closable="false"
    >
      Прежде чем создавать новый блог вам необходимо авторизоваться или
      зарегистрироваться.
    </b-notification>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'Warning',
  props: {
    title: {
      type: String,
      required: true,
    },
    body: {
      type: String,
      required: true,
    },
    button: {
      type: String,
      required: true,
    },
    redirect: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState('login', ['show']),
  },
  methods: {
    ...mapMutations('login', { toggleModal: 'SET_SHOW' }),
  },
}
</script>

<style scoped>
.warning-popin {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(10, 10, 10, 0.86);
}
.notification-editor {
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin: 0;
}
</style>
