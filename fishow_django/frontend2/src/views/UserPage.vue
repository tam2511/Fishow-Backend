<template>
  <div class="container" v-if="username">
    <div class="row row-30">
      <div class="col-lg-8">
        <!-- Heading Component-->
        <article class="heading-component">
          <div class="heading-component-inner">
            <h5 class="heading-component-title">Player overview</h5>
            <button class="button button-gray-outline" @click="logout">
              Выйти
            </button>
          </div>
        </article>

        <!-- Player Info Corporate-->
        <user-main />
        <!--  Block Player Info-->
        <user-info />
      </div>
      <div class="col-lg-4">
        <div class="row row-30">
          <user-stat />
          <user-awards />
          <user-news />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UserStat from '@/components/UserPage/UserStat'
import UserAwards from '@/components/UserPage/UserAwards'
import UserNews from '@/components/UserPage/UserNews'
import UserInfo from '@/components/UserPage/UserInfo'
import UserMain from '@/components/UserPage/UserMain'
import { mapState } from 'vuex'
export default {
  name: 'UserPage',
  components: { UserMain, UserInfo, UserNews, UserAwards, UserStat },
  computed: {
    ...mapState('user', ['username']),
  },
  methods: {
    logout() {
      window.location = '/accounts/logout/'
    },
  },
}
</script>

<style scoped></style>
