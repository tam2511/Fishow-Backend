import confserver from './confserver'
import appleIcons from './icons'
export default {
  server: {
    port: 3000,
    host: '0.0.0.0',
  },
  mode: 'universal',
  /*
   ** Headers of the page
   */
  middleware: 'auth',
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
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://cdn.materialdesignicons.com/5.3.45/css/materialdesignicons.min.css',
      },
      {
        rel: 'stylesheet',
        href: 'https://use.fontawesome.com/releases/v5.5.0/css/all.css',
      },
      ...appleIcons,
    ],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  router: {
    middleware: ['auth'],
  },
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['~/plugins/axios'],
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
    hostname: 'http://fishow.ru',
    gzip: true,
    exclude: ['/secret', '/admin/**'],
    // routes: [
    //   '/page/1',
    //   '/page/2',
    //   {
    //     url: '/page/3',
    //     changefreq: 'daily',
    //     priority: 1,
    //     lastmod: '2017-06-30T13:30:00.000Z',
    //   },
    // ],
  },
  /* buefy options */
  buefy: {
    // isPrimary: '#000',
  },
  // yandexMetrika: {
  //   id: 64900765,
  //   webvisor: true,
  //   clickmap: true,
  //   // useCDN:false,
  //   trackLinks: true,
  //   accurateTrackBounce: true,
  // },
  proxy: {
    '/api': {
      target: `http://${confserver.ip}:8000/api`,
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
    baseURL: `http://${confserver.ip}:8000/api`,
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
  auth: {
    plugins: [{ src: '~/plugins/axios', ssr: true }, '~/plugins/auth.js'],
    fetchUserOnLogin: true,
    watchLoggedIn: true,
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/rest-auth/login/',
            method: 'post',
            propertyName: 'key',
          },
          registration: {
            url: '/rest-auth/registration/',
            method: 'post',
            propertyName: 'key',
          },
          logout: { url: '/rest-auth/logout/', method: 'post' },
          user: {
            url: '/rest-auth/user/',
            method: 'get',
            propertyName: 'username',
          },
        },
        tokenType: 'Token',
        tokenName: 'Authorization',
        // globalToken: true,
        // autoFetchUser: true
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
        redirect_uri: 'http://fishow.ru/',
        token_key: 'access_token',
        force_confirm: 'yes',
        state: '',
      },
    },
    redirect: false,
  },
  build: {
    extractCSS: true,
    /*
     ** You can extend webpack config here
     */
    // entry: {
    //   app: ['./app']
    // },
    // output: {
    //   path: require('path').resolve('./assets/bundles/'),
    //   filename: '[name]-[hash].js',
    //   publicPath: 'http://localhost:3000/assets/bundles/'
    // },
    // publicPath: 'static/',
    // plugins: [
    //   new BundleTracker({
    //     path: __dirname,
    //     filename: '.nuxt/webpack-stats.json'
    //   })
    // ],
    extend(config, ctx) {},
  },
}
