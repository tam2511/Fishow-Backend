<template>
  <nav class="fishow_navbar">
    <nuxt-link class="fishow_navbar-brand" to="/">Fishow</nuxt-link>
    <div class="fishow_navbar-nav">
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/">Главная</nuxt-link>
      </span>
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/predict-page"
          >Прогноз</nuxt-link
        >
      </span>
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/blog-editor"
          >Создать блог</nuxt-link
        >
      </span>
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/article">Все блоги</nuxt-link>
      </span>
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/wiki">Вики</nuxt-link>
      </span>
      <span class="fishow_nav-item">
        <nuxt-link class="fishow_nav-link" to="/forum">Форум</nuxt-link>
      </span>
    </div>
    <!--    <a @click="setShow" v-if="!username">-->
    <!--      <div class="fishow_navbar_menu">-->
    <!--&lt;!&ndash;        <img src="./user.png" alt="" />&ndash;&gt;-->
    <!--      </div>-->
    <!--    </a>-->
    <!--    <nuxt-link-->
    <!--      :to="{ name: 'UserPage', params: { username: username } }"-->
    <!--      v-else-->
    <!--    >-->
    <div class="fishow_navbar_menu">
      <!--      <img src="./user.png" alt="" />-->
    </div>
    <!--    </nuxt-link>-->
  </nav>
</template>

<script>
// import { mapState, mapActions } from 'vuex'
export default {
  data() {
    return {
      active: false,
      step: false
    }
  },
  computed: {
    // ...mapState('user', ['username']),
    // ...mapState('login', ['show','stepReg','error'])
  },
  created() {
    // this.setUserInfo()
  },
  methods: {
    // actiLog() {
    //     this.active = !this.active
    // },
    // changeStep() {
    // },
    // ...mapActions('user', ['setUserInfo']),
    // ...mapActions('login', ['setShow', 'setStep'])
  }
}
</script>

<style scoped></style>
