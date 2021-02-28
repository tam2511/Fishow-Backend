<template>
  <div>
    <div class="desktop">
      <b-navbar class="navbar-brand-container">
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
          <b-navbar-item
            v-for="item in desktopButtons"
            :key="item._uid"
            tag="nuxt-link"
            :to="item.url"
            :class="getMenuClass(item.disabled)"
          >
            {{ item.title }}
          </b-navbar-item>
        </template>
        <template slot="end">
          <b-navbar-item tag="div">
            <div v-if="!$auth.user" class="buttons">
              <a class="button is-primary" @click="toggleReg"> Регистрация </a>
              <a class="button is-light" @click="toggleLogin"> Войти </a>
            </div>
            <div v-else class="buttons">
              <nuxt-link :to="{ name: 'user-page' }" class="button ip-primary">
                {{ $auth.user.login || $auth.user.username }}</nuxt-link
              >
              <a class="button is-light" @click="logout"> Выйти </a>
            </div>
          </b-navbar-item>
        </template>
      </b-navbar>
    </div>
    <div class="mobile">
      <nav class="navbar-mobile">
        <div class="navbar-mobile_wrapper">
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
      desktopButtons: [
        {
          title: 'Главная',
          url: { name: 'index' },
          type: 'Home',
        },
        {
          title: 'Прогноз клёва',
          url: { path: '/prognoz-kleva' },
          type: 'Prediction',
        },
        {
          title: 'Водоемы',
          url: { path: '/Water-place' },
          type: 'Water-place',
          disabled: true,
        },
        {
          title: 'Отчеты',
          url: { path: '/reports' },
          type: 'Reports',
        },
        {
          title: 'Статьи',
          url: { path: '/blogs' },
          type: 'Blogs',
        },
        {
          title: 'Вики',
          url: { path: '/Wiki' },
          type: 'Wiki',
          disabled: true,
        },
      ],
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
    ...mapState('user', ['user']),
  },
  methods: {
    getMenuClass(disabled) {
      return disabled ? 'is-disabled' : ''
    },
    testMod() {
      if (this.$auth.user) {
        console.log('go to cabinet')
        this.$router.push({ name: 'UserPage' })
      } else {
        this.toggleLogin()
      }
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
    path {
      fill: var(--color-type-brand);
    }
  }
}
.navbar-mobile {
  height: 60px;
  background: var(--color-bg-acent);
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
.logo {
  padding: 0 !important;
  color: #898989 !important;
  position: relative;
  &:after {
    content: attr(data-word);
    position: absolute;
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
.desktop {
  box-shadow: 0 4px 56px rgba(0, 0, 0, 0.12);
  background-color: #fff;
  @media screen and (max-width: 500px) {
    display: none;
  }
}
.mobile {
  @media screen and (min-width: 500px) {
    display: none;
  }
}
.navbar-brand-container {
  max-width: 1344px;
  margin: 0 auto;
}
.is-disabled {
  pointer-events: none;
  opacity: 0.5;
}
</style>
