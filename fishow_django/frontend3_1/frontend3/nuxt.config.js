// eslint-disable-next-line nuxt/no-cjs-in-config
import BundleTracker from 'webpack-bundle-tracker'
export default {
  context: __dirname,
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [

  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    'bootstrap-vue/nuxt',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/proxy',
    'nuxt-vue-multiselect'
  ],
  proxy: {
    // ** is important here, * probably means it won't go more than one level deep
    // '/api/**': {
    //   target:
    //     process.env.PRODUCTION === 'true'
    //       ? process.env.HEROKU_BACKEND_API_URL
    //       : process.env.LOCAL_API_URL,
    //   pathRewrite: { '^/api': '' }
    // }
    '/api': {
      target: 'http://localhost:3000/',
      pathRewrite: {
        '^/api': '/'
      }
    }
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: 'http://localhost:8000/api'
  },
  /*
   ** Build configuration
   */
  // build: {
  //   plugins: [
  //     new BundleTracker({
  //       path: __dirname,
  //       filename: './assets/webpack-stats.json'
  //     })
  //   ],
  //   /*
  //
  //    ** You can extend webpack config here
  //    */
  //   extend(config, ctx) {}
  // }
  build: {
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
    extend(config, ctx) {}
  }
}
