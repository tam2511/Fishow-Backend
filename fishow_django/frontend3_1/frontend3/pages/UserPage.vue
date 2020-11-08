<template>
  <div v-if="$auth.user" class="box">
    <div class="media">
      <div class="media-left">
        <figure class="image is-128x128">
          <img src="https://bulma.io/images/placeholders/128x128.png" />
        </figure>
      </div>
      <div class="media-center">
        <!--        <p class="title">{{ $auth.user }}</p>-->
        <p class="title">{{ $auth.user.login }}</p>
        <p class="title">{{ $auth.user.default_email }}</p>
      </div>
    </div>
    <div class="media">
      <div class="media-center"></div>
    </div>
    <!--    <div class="row row-30">-->
    <!--      <div class="col-lg-8">-->
    <!--        &lt;!&ndash; Heading Component&ndash;&gt;-->
    <!--        <article class="heading-component">-->
    <!--          <div class="heading-component-inner">-->
    <!--            <h5 class="heading-component-title">Личный кабинет</h5>-->
    <!--            <button class="button button-gray-outline" @click="logout">-->
    <!--              Выйти-->
    <!--            </button>-->
    <!--          </div>-->
    <!--        </article>-->

    <!--        &lt;!&ndash; Player Info Corporate&ndash;&gt;-->
    <!--    <user-main :username="$auth.user" />-->

    <!--        Block Player Info-->
    <!--        <user-info />-->
    <!--      </div>-->
    <!--      <div class="col-lg-4">-->
    <!--        <div class="row row-30">-->
    <!--          <user-stat />-->
    <!--          <user-awards />-->
    <!--          <user-news />-->
    <!--        </div>-->
    <!--      </div>-->
    <!--    </div>-->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { userPage } from '~/assets/descriptions'
// import UserStat from '@/components/UserPage/UserStat'
// import UserAwards from '@/components/UserPage/UserAwards'
// import UserNews from '@/components/UserPage/UserNews'
// import UserInfo from '@/components/UserPage/UserInfo'
// import UserMain from '@/components/UserPage/UserMain'
export default {
  components: {},
  props: {
    scrollValue: {
      type: Number,
      default: 0,
    },
  },
  computed: {
    ...mapState('user', ['user']),
  },
  mounted() {
    scrollTo(0, this.scrollValue)
  },
  methods: {
    async logout() {
      try {
        await this.$auth.logout()
      } catch (e) {
        console.log('e = ', e)
      }
    },
  },
  head() {
    return {
      title: userPage.title,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content: userPage.description,
        },
      ],
    }
  },
}
</script>

<style scoped></style>
