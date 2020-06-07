<template>
  <div v-if="$auth.user" class="container">
    <div class="row row-30">
      <div class="col-lg-8">
        <!-- Heading Component-->
        <article class="heading-component">
          <div class="heading-component-inner">
            <h5 class="heading-component-title">Личный кабинет</h5>
            <button class="button button-gray-outline" @click="logout">
              Выйти
            </button>
          </div>
        </article>

        <!-- Player Info Corporate-->
        <user-main :username="$auth.user" />
        Block Player Info
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
import { mapState } from 'vuex'
import UserStat from '@/components/UserPage/UserStat'
import UserAwards from '@/components/UserPage/UserAwards'
import UserNews from '@/components/UserPage/UserNews'
import UserInfo from '@/components/UserPage/UserInfo'
import UserMain from '@/components/UserPage/UserMain'
export default {
  components: { UserMain, UserInfo, UserNews, UserAwards, UserStat },
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
}
</script>

<style scoped></style>
