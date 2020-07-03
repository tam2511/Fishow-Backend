import confserver from './confserver'

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
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'yandex-verification', content: 'cb7a2c560ce5c37b' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || '',
      },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon2.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://cdn.materialdesignicons.com/5.3.45/css/materialdesignicons.min.css',
      },
      {
        rel: 'stylesheet',
        href: 'https://use.fontawesome.com/releases/v5.2.0/css/all.css',
      },
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
    'nuxt-vue-multiselect',
    '@nuxtjs/yandex-metrika',
    '@nuxtjs/robots',
  ],
  yandexMetrika: {
    id: '64900765',
    webvisor: true,
    // clickmap:true,
    // useCDN:false,
    // trackLinks:true,
    // accurateTrackBounce:true,
  },
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
    watchLoggedIn: false,
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
