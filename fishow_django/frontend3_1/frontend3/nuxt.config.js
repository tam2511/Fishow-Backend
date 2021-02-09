import confserver from './confserver'
import appleIcons from './icons'
export default {
  server: {
    port: 3000,
    host: '0.0.0.0',
  },
  /*
   ** Headers of the page
   */
  middleware: ['auth', 'loggedIn'],
  head: {
    meta: [
      { charset: 'utf-8' },
      {
        property: 'og:title',
        content:
          'Fishow - сервис прогноза клева и ваша социальная рыболовная сеть',
      },
      { property: 'og:image', content: '/ms-icon-144x144.png' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'yandex-verification', content: 'cb7a2c560ce5c37b' },
      {
        hid: 'description',
        name: 'description',
        content:
          'Fishow.ru - сервис прогноза клева и ваша социальная рыболовная сеть',
      },
      { name: 'msapplication-TileColor', content: '#ffffff' },
      { name: 'msapplication-TileImage', content: '/ms-icon-144x144.png' },
      { name: 'theme-color', content: '#ffffff' },
      {
        hid: 'keywords',
        name: 'keywords',
        content:
          'рыбалка, прогноз, отчеты о рыбалке, отчеты, прогноз на рыбалку, блоги о рыбалке, новости о рыбалке, ловля рыбы, клёв, хищные рыбы',
      },
    ],
    link: [...appleIcons],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['~/plugins/axios', '@/plugins/vue-infinite-scroll.client.js'],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
    'nuxt-buefy',
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    // 'bootstrap-vue/nuxt',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/auth',
    '@nuxtjs/axios',
    '@nuxtjs/proxy',
    '@nuxtjs/sitemap',
    'nuxt-vue-multiselect',
    [
      '@nuxtjs/yandex-metrika',
      {
        id: '64900765',
        webvisor: true,
        clickmap: true,
        // useCDN:false,
        trackLinks: true,
        accurateTrackBounce: true,
      },
    ],
    '@nuxtjs/robots',
  ],
  sitemap: {
    hostname: 'https://fishow.ru',
    gzip: true,
    exclude: ['/secret', '/admin/**'],
  },
  /* buefy options */
  buefy: {
    css: false,
  },

  proxy: {
    '/api': {
      target: confserver.ip,
      pathRewrite: {
        '^/api': '/',
      },
    },
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    withCredentials: true,
    baseURL: confserver.ip,
  },
  robots: [
    {
      UserAgent: 'Googlebot',
      Disallow: ['/api', '/user'],
    },
    {
      UserAgent: '*',
      Disallow: '/api',
    },
  ],
  transition: {
    name: 'fade',
    mode: 'out-in',
  },
  // router: {
  //   middleware: ['loggedIn'],
  // },
  auth: {
    plugins: [{ src: '~/plugins/axios', ssr: true }, '~/plugins/auth.js'],
    fetchUserOnLogin: true,
    watchLoggedIn: true,
    cookie: {
      options: {
        expires: 7,
      },
    },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/dj-rest-auth/login/',
            method: 'post',
            propertyName: false,
          },
          logout: { url: '/dj-rest-auth/logout/', method: 'post' },
          user: {
            url: '/dj-rest-auth/user/',
            method: 'get',
            propertyName: false,
          },
        },
      },
      social: {
        _scheme: 'oauth2',
        response_type: 'code',
        client_id: '1fbb5875a4d54eacb428597945516e2b',
        client_secret: '80a0332f48ce47e5a2025c469601b9a2',
        authorization_endpoint: 'https://oauth.yandex.ru/authorize?',
        userinfo_endpoint: 'https://login.yandex.ru/info?',
        scope: ['login:avatar', 'login:email', 'login:info', 'login:birthday'],
        access_type: 'offline',
        access_token_endpoint: 'https://oauth.yandex.ru/token?',
        token_type: 'Bearer',
        grant_type: 'authorization_code',
        redirect_uri: 'https://fishow.ru/',
        token_key: 'access_token',
        force_confirm: 'yes',
        state: '',
      },
    },
    redirect: false,
  },
  build: {
    // parallel: true, // don't know, if it works, maybe
    cache: true, // don't know, if it works, maybe
    optimization: {
      minimize: true,
      runtimeChunk: true,
      concatenateModules: true,
      splitChunks: {
        chunks: 'all',
        minSize: 30000,
        maxSize: 0,
        minChunks: 1,
        maxAsyncRequests: 20,
        maxInitialRequests: 3,
        automaticNameDelimiter: '~',
        name: true,
        cacheGroups: {
          vendors: {
            test: /[\\/]node_modules[\\/]/,
            priority: -10,
          },
          default: {
            minChunks: 2,
            priority: -20,
            reuseExistingChunk: true,
          },
        },
      },
    },
    // hardSource: true, // don't know, if it works, maybe
    // extractCSS: true,
    optimizeCSS: true,

    extend(config, ctx) {},
  },
  css: [
    '../src/styles/main.scss',
    '../assets/all.css',
    '../assets/materialdesignicons.min.css',
  ],
}
