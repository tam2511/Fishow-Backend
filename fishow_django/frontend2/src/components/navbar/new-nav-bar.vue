<template>
  <vue-navigation-bar :options="navbarOptions" />
</template>

<script>
export default {
  data() {
    return {
      navbarOptions: {
        elementId: 'main-navbar',
        isUsingVueRouter: true,
        mobileBreakpoint: 992,
        brandImagePath: './',
        // brandImage: require('/lockup-color.png'),
        brandImageAltText: 'brand-image',
        // collapseButtonImageOpen: require('/collapse-menu-dark.png'),
        // collapseButtonImageClose: require('/times.png'),
        showBrandImageInMobilePopup: true,
        ariaLabelMainNav: 'Main Navigation',
        tooltipAnimationType: 'shift-away',
        menuOptionsLeft: [
          {
            type: 'link',
            text: 'Fishow',
            subMenuOptions: [
              {
                type: 'link',
                text: 'Главная',
                path: '/',
              },
              {
                type: 'hr',
              },
              {
                isLinkAction: true,
                type: 'link',
                text: 'О нас',
                subText: 'Тут пока нету страницы :)',
                path: '/about-us',
                iconLeft: '<i class="fa fa-star fa-fw"></i>',
              },
            ],
          },
          {
            type: 'link',
            text: 'Блоги',
            subMenuOptions: [
              {
                type: 'link',
                text: 'Создать блог',
                path: '/blog-editor',
              },
              {
                type: 'link',
                text: 'Все блоги',
                path: '/article',
              },
            ],
          },
          {
            type: 'link',
            text: 'Прогноз',
            path: '/predict-page',
            // iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
          },
          {
            type: 'link',
            text: 'Вики',
            path: '/Wiki',
          },
          {
            type: 'link',
            text: 'Форум',
            path: '/Forum',
          },
        ],
        menuOptionsRight: [
          {
            type: 'button',
            text: 'Signup',
            path: '/signup',
          },
          {
            type: 'button',
            text: 'Login',
            path: '/login',
            iconRight:
              '<svg id="i-arrow-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"> <path d="M22 6 L30 16 22 26 M30 16 L2 16" /> </svg>',
          },
        ],
      },
    }
  },
  computed: {
    userName() {
      return this.$store.state.username
    },
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
    },
    logout() {
      window.location = '/accounts/logout/'
    },
  },
  created() {
    this.$store.dispatch('setUserInfo')
  },
}
</script>

<style lang="scss">
#app .vnb {
  background-color: var(--background-color-brand);
  text-transform: uppercase;
  position: sticky;
  top: 0;
  color: #fff !important;
  z-index: 5;
  padding: 20px 0 20px;
  &-button {
    color: var(--color-typo-primary);
    background: var(--background-color-default);
    &:hover {
      background: var(--background-color-border);
    }
  }
  .vnb__menu-options__option__link[aria-label='Fishow'] {
    font-size: 28px;
  }
  .vnb__menu-options__option__link {
    font-weight: 800;
    color: white;
  }
  .vnb-image {
    width: 200px;
    height: 200px;
  }
}
</style>
