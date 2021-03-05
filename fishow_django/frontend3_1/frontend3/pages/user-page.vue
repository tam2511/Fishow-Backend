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
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { userPage } from '~/assets/descriptions'

export default {
  components: {},
  props: {
    scrollValue: {
      type: Number,
      default: 0,
    },
  },
  head() {
    return {
      title: userPage.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: userPage.description,
        },
      ],
    }
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
