<template>
  <div>
    <div v-if="isDeviceDesktop === false" class="desktop">
      <b-navbar :fixed-top="true" class="navbar-brand-container">
        <template slot="brand">
          <b-navbar-item
            tag="nuxt-link"
            :to="{ name: 'index' }"
            class="logo"
            data-word="FISHOW"
          >
            FISHOW
          </b-navbar-item>
        </template>
        <template slot="start">
          <b-navbar-item tag="nuxt-link" :to="{ name: 'index' }">
            Главная
          </b-navbar-item>
          <b-navbar-item tag="nuxt-link" :to="{ path: '/prognoz-kleva' }">
            Прогноз
          </b-navbar-item>
          <b-navbar-item tag="nuxt-link" :to="{ path: '/blogs' }">
            Блоги
          </b-navbar-item>
        </template>
        <template slot="end">
          <b-navbar-item tag="div">
            <div v-if="!$auth.user" class="buttons">
              <a class="button is-primary" @click="toggleReg"> Регистрация </a>
              <a class="button is-light" @click="toggleLogin"> Войти </a>
              <!--          <a class="button is-light" @click="toggleLoginYandex">-->
              <!--            Войти через Яндекс-->
              <!--          </a>-->
            </div>
            <div v-else class="buttons">
              <nuxt-link to="/UserPage" class="button ip-primary">
                {{ $auth.user.login || $auth.user.username }}</nuxt-link
              >
              <a class="button is-light" @click="logout"> Выйти </a>
            </div>
          </b-navbar-item>
        </template>
      </b-navbar>
    </div>
    <div v-else class="mobile">
      <nav class="navbar-mobile">
        <div v-if="loginMode" class="navbar-mobile_wrapper">
          <div class="navbar-mobile_button">Вход</div>
          <div class="navbar-mobile_button">Регистрация</div>
          <div class="navbar-mobile_button navbar-mobile_button__close">
            <span @click="testMod">
              <navbar-icon type="Close"></navbar-icon>
            </span>
          </div>
        </div>
        <div v-else class="navbar-mobile_wrapper">
          <div
            v-for="(btn, index) in navMobButtons"
            :key="index"
            class="navbar-mobile_button"
          >
            <nuxt-link :to="btn.url">
              <navbar-icon :type="btn.type"></navbar-icon>
            </nuxt-link>
          </div>
          <div class="navbar-mobile_button">
            <span @click="testMod">
              <navbar-icon type="Person"></navbar-icon>
            </span>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import NavbarIcon from '~/components/Header/navbar/navbar-icon'
export default {
  components: { NavbarIcon },
  data() {
    return {
      navMobButtons: [
        {
          title: '',
          url: { name: 'index' },
          type: 'Home',
        },
        {
          title: '',
          url: { path: '/blogs' },
          type: 'hot',
        },
        {
          title: '',
          url: { path: '/blog-editor' },
          type: 'CreateBlog',
        },
        {
          title: '',
          url: { path: '/prognoz-kleva' },
          type: 'Terrain',
        },
      ],
      loginMode: false,
    }
  },
  computed: {
    isDeviceDesktop() {
      let result = null
      if (typeof navigator === 'object') {
        result = navigator && /mobile/i.test(navigator.userAgent)
      }
      console.log('result = ', result)
      return result
    },
    ...mapState('user', ['user']),
  },
  methods: {
    testMod() {
      console.log('test')
      this.loginMode = !this.loginMode
    },
    async logout() {
      try {
        await this.$auth.logout()
      } catch (e) {
        // console.log('e = ', e)
      }
    },
    toggleLoginYandex() {
      this.$auth.loginWith('social')
    },
    ...mapMutations('login', {
      toggleLogin: 'TOGGLE_LOGIN',
      toggleReg: 'TOGGLE_REG',
    }),
  },
}
</script>

<style lang="scss">
.navbar-mobile_button {
  position: relative;
  width: 32px;
  height: 32px;
  &__close {
    position: absolute;
    right: 25px;
  }
  svg {
    transition: 0.3s;
  }
  .nuxt-link-exact-active {
    svg {
      /*border-radius: 9px;*/
      /*width: 45px;*/
      /*height: 45px;*/
      /*position: absolute;*/
      /*background-color: #fff;*/
    }
    path {
      fill: #000;
    }
  }
}
.navbar-mobile {
  height: 60px;
  background: #f7f7f7;
  box-shadow: 0px -10px 10px rgba(0, 0, 0, 0.08);
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 10px 0;
  z-index: 100;

  &_wrapper {
    display: flex;
    justify-content: space-around;
  }
}
nav.navbar {
  background: none;
}
.logo {
  padding: 0 !important;
  color: #898989 !important;
  /*-webkit-text-stroke: 1px #fff;*/
  position: relative;
  &:after {
    content: attr(data-word);
    position: absolute;
    /*top: 0;*/
    left: 0;
    color: #74c4d3;
    cursor: initial;
    animation: waves 2s ease-in-out infinite forwards;
  }
}
a.navbar-item:hover {
  color: white;
}
@keyframes waves {
  0%,
  100% {
    clip-path: polygon(
      0 66%,
      11% 59%,
      18% 51%,
      26% 46%,
      35% 41%,
      48% 44%,
      55% 54%,
      63% 63%,
      76% 60%,
      82% 50%,
      92% 48%,
      100% 53%,
      100% 100%,
      0% 100%
    );
  }
  50% {
    clip-path: polygon(
      0 66%,
      8% 74%,
      17% 77%,
      28% 70%,
      35% 57%,
      48% 44%,
      56% 39%,
      69% 41%,
      75% 47%,
      84% 60%,
      92% 61%,
      100% 53%,
      100% 100%,
      0% 100%
    );
  }
}
.navbar-brand {
  font-size: 20px;
  font-weight: bold;
  transition: all 200ms;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  background-position: 50% 50%;
  display: grid;
  place-items: center;
  z-index: 1;
  cursor: initial;
  position: relative;
  padding: 7px;
}
</style>
