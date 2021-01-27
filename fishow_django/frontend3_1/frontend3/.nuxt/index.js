import Vue from 'vue'
import Vuex from 'vuex'
import Meta from 'vue-meta'
import ClientOnly from 'vue-client-only'
import NoSsr from 'vue-no-ssr'
import { createRouter } from './router.js'
import NuxtChild from './components/nuxt-child.js'
import NuxtError from '../layouts/error.vue'
import Nuxt from './components/nuxt.js'
import App from './App.js'
import { setContext, getLocation, getRouteData, normalizeError } from './utils'
import { createStore } from './store.js'

/* Plugins */

import nuxt_plugin_yandexmetrikaplugin7eceb94c_3b126cce from 'nuxt_plugin_yandexmetrikaplugin7eceb94c_3b126cce' // Source: ./yandex-metrika.plugin.7eceb94c.js (mode: 'client')
import nuxt_plugin_nuxtvuemultiselect_10e659e5 from 'nuxt_plugin_nuxtvuemultiselect_10e659e5' // Source: ./nuxt-vue-multiselect.js (mode: 'all')
import nuxt_plugin_axios_8a6182a2 from 'nuxt_plugin_axios_8a6182a2' // Source: ./axios.js (mode: 'all')
import nuxt_plugin_buefy_7cae3e00 from 'nuxt_plugin_buefy_7cae3e00' // Source: ./buefy.js (mode: 'all')
import nuxt_plugin_axios_3566aa80 from 'nuxt_plugin_axios_3566aa80' // Source: ../plugins/axios (mode: 'all')
import nuxt_plugin_vueinfinitescrollclient_466e7c09 from 'nuxt_plugin_vueinfinitescrollclient_466e7c09' // Source: ../plugins/vue-infinite-scroll.client.js (mode: 'client')
import nuxt_plugin_plugin_68db66aa from 'nuxt_plugin_plugin_68db66aa' // Source: ./auth/plugin.js (mode: 'all')
import nuxt_plugin_auth_7f7561ce from 'nuxt_plugin_auth_7f7561ce' // Source: ../plugins/auth.js (mode: 'all')

// Component: <ClientOnly>
Vue.component(ClientOnly.name, ClientOnly)

// TODO: Remove in Nuxt 3: <NoSsr>
Vue.component(NoSsr.name, {
  ...NoSsr,
  render (h, ctx) {
    if (process.client && !NoSsr._warned) {
      NoSsr._warned = true

      console.warn('<no-ssr> has been deprecated and will be removed in Nuxt 3, please use <client-only> instead')
    }
    return NoSsr.render(h, ctx)
  }
})

// Component: <NuxtChild>
Vue.component(NuxtChild.name, NuxtChild)
Vue.component('NChild', NuxtChild)

// Component NuxtLink is imported in server.js or client.js

// Component: <Nuxt>
Vue.component(Nuxt.name, Nuxt)

Object.defineProperty(Vue.prototype, '$nuxt', {
  get() {
    return this.$root.$options.$nuxt
  },
  configurable: true
})

Vue.use(Meta, {"keyName":"head","attribute":"data-n-head","ssrAttribute":"data-n-head-ssr","tagIDKeyName":"hid"})

const defaultTransition = {"name":"fade","mode":"out-in","appear":false,"appearClass":"appear","appearActiveClass":"appear-active","appearToClass":"appear-to"}

const originalRegisterModule = Vuex.Store.prototype.registerModule
const baseStoreOptions = { preserveState: process.client }

function registerModule (path, rawModule, options = {}) {
  return originalRegisterModule.call(this, path, rawModule, { ...baseStoreOptions, ...options })
}

async function createApp(ssrContext, config = {}) {
  const router = await createRouter(ssrContext)

  const store = createStore(ssrContext)
  // Add this.$router into store actions/mutations
  store.$router = router

  // Fix SSR caveat https://github.com/nuxt/nuxt.js/issues/3757#issuecomment-414689141
  store.registerModule = registerModule

  // Create Root instance

  // here we inject the router and store to all child components,
  // making them available everywhere as `this.$router` and `this.$store`.
  const app = {
    head: {"meta":[{"charset":"utf-8"},{"property":"og:title","content":"Fishow - сервис прогноза клева и ваша социальная рыболовная сеть"},{"property":"og:image","content":"\u002Fms-icon-144x144.png"},{"name":"viewport","content":"width=device-width, initial-scale=1"},{"name":"yandex-verification","content":"cb7a2c560ce5c37b"},{"hid":"description","name":"description","content":"Fishow.ru - сервис прогноза клева и ваша социальная рыболовная сеть"},{"name":"msapplication-TileColor","content":"#ffffff"},{"name":"msapplication-TileImage","content":"\u002Fms-icon-144x144.png"},{"name":"theme-color","content":"#ffffff"},{"hid":"keywords","name":"keywords","content":"рыбалка, прогноз, отчеты о рыбалке, отчеты, прогноз на рыбалку, блоги о рыбалке, новости о рыбалке, ловля рыбы, клёв, хищные рыбы"}],"link":[{"rel":"icon","type":"image\u002Fx-icon","href":"\u002Ffavicon.ico"},{"rel":"stylesheet","href":"https:\u002F\u002Fcdn.materialdesignicons.com\u002F5.3.45\u002Fcss\u002Fmaterialdesignicons.min.css"},{"rel":"stylesheet","href":"https:\u002F\u002Fuse.fontawesome.com\u002Freleases\u002Fv5.5.0\u002Fcss\u002Fall.css"},{"rel":"apple-touch-icon","sizes":"57x57","type":"image\u002Fx-icon","href":"\u002Fapple-icon-57x57.png"},{"rel":"apple-touch-icon","sizes":"60x60","type":"image\u002Fx-icon","href":"\u002Fapple-icon-60x60.png"},{"rel":"apple-touch-icon","sizes":"72x72","type":"image\u002Fx-icon","href":"\u002Fapple-icon-72x72.png"},{"rel":"apple-touch-icon","sizes":"76x76","type":"image\u002Fx-icon","href":"\u002Fapple-icon-76x76.png"},{"rel":"apple-touch-icon","sizes":"114x114","type":"image\u002Fx-icon","href":"\u002Fapple-icon-114x114.png"},{"rel":"apple-touch-icon","sizes":"120x120","type":"image\u002Fx-icon","href":"\u002Fapple-icon-120x120.png"},{"rel":"apple-touch-icon","sizes":"144x144","type":"image\u002Fx-icon","href":"\u002Fapple-icon-144x144.png"},{"rel":"apple-touch-icon","sizes":"152x152","type":"image\u002Fx-icon","href":"\u002Fapple-icon-152x152.png"},{"rel":"apple-touch-icon","sizes":"180x180","type":"image\u002Fx-icon","href":"\u002Fapple-icon-180x180.png"},{"rel":"icon","type":"image\u002Fpng","sizes":"32x32","href":"\u002Ffavicon-32x32.png"},{"rel":"icon","type":"image\u002Fpng","sizes":"96x96","href":"\u002Ffavicon-96x96.png"},{"rel":"icon","type":"image\u002Fpng","sizes":"16x16","href":"\u002Ffavicon-16x16.png"},{"rel":"icon","type":"image\u002Fpng","sizes":"192x192","href":"\u002Fandroid-icon-192x192.png"},{"rel":"manifest","href":"\u002Fmanifest.json"},{"rel":"stylesheet","type":"text\u002Fcss","href":"\u002F\u002Fcdn.materialdesignicons.com\u002F5.0.45\u002Fcss\u002Fmaterialdesignicons.min.css"},{"href":"https:\u002F\u002Fmc.yandex.ru\u002Fmetrika\u002Ftag.js","rel":"preload","as":"script"}],"style":[],"script":[{"src":"https:\u002F\u002Fmc.yandex.ru\u002Fmetrika\u002Ftag.js","async":"true"}]},

    store,
    router,
    nuxt: {
      defaultTransition,
      transitions: [defaultTransition],
      setTransitions (transitions) {
        if (!Array.isArray(transitions)) {
          transitions = [transitions]
        }
        transitions = transitions.map((transition) => {
          if (!transition) {
            transition = defaultTransition
          } else if (typeof transition === 'string') {
            transition = Object.assign({}, defaultTransition, { name: transition })
          } else {
            transition = Object.assign({}, defaultTransition, transition)
          }
          return transition
        })
        this.$options.nuxt.transitions = transitions
        return transitions
      },

      err: null,
      dateErr: null,
      error (err) {
        err = err || null
        app.context._errored = Boolean(err)
        err = err ? normalizeError(err) : null
        let nuxt = app.nuxt // to work with @vue/composition-api, see https://github.com/nuxt/nuxt.js/issues/6517#issuecomment-573280207
        if (this) {
          nuxt = this.nuxt || this.$options.nuxt
        }
        nuxt.dateErr = Date.now()
        nuxt.err = err
        // Used in src/server.js
        if (ssrContext) {
          ssrContext.nuxt.error = err
        }
        return err
      }
    },
    ...App
  }

  // Make app available into store via this.app
  store.app = app

  const next = ssrContext ? ssrContext.next : location => app.router.push(location)
  // Resolve route
  let route
  if (ssrContext) {
    route = router.resolve(ssrContext.url).route
  } else {
    const path = getLocation(router.options.base, router.options.mode)
    route = router.resolve(path).route
  }

  // Set context to app.context
  await setContext(app, {
    store,
    route,
    next,
    error: app.nuxt.error.bind(app),
    payload: ssrContext ? ssrContext.payload : undefined,
    req: ssrContext ? ssrContext.req : undefined,
    res: ssrContext ? ssrContext.res : undefined,
    beforeRenderFns: ssrContext ? ssrContext.beforeRenderFns : undefined,
    ssrContext
  })

  function inject(key, value) {
    if (!key) {
      throw new Error('inject(key, value) has no key provided')
    }
    if (value === undefined) {
      throw new Error(`inject('${key}', value) has no value provided`)
    }

    key = '$' + key
    // Add into app
    app[key] = value
    // Add into context
    if (!app.context[key]) {
      app.context[key] = value
    }

    // Add into store
    store[key] = app[key]

    // Check if plugin not already installed
    const installKey = '__nuxt_' + key + '_installed__'
    if (Vue[installKey]) {
      return
    }
    Vue[installKey] = true
    // Call Vue.use() to install the plugin into vm
    Vue.use(() => {
      if (!Object.prototype.hasOwnProperty.call(Vue.prototype, key)) {
        Object.defineProperty(Vue.prototype, key, {
          get () {
            return this.$root.$options[key]
          }
        })
      }
    })
  }

  // Inject runtime config as $config
  inject('config', config)

  if (process.client) {
    // Replace store state before plugins execution
    if (window.__NUXT__ && window.__NUXT__.state) {
      store.replaceState(window.__NUXT__.state)
    }
  }

  // Add enablePreview(previewData = {}) in context for plugins
  if (process.static && process.client) {
    app.context.enablePreview = function (previewData = {}) {
      app.previewData = Object.assign({}, previewData)
      inject('preview', previewData)
    }
  }
  // Plugin execution

  if (process.client && typeof nuxt_plugin_yandexmetrikaplugin7eceb94c_3b126cce === 'function') {
    await nuxt_plugin_yandexmetrikaplugin7eceb94c_3b126cce(app.context, inject)
  }

  if (typeof nuxt_plugin_nuxtvuemultiselect_10e659e5 === 'function') {
    await nuxt_plugin_nuxtvuemultiselect_10e659e5(app.context, inject)
  }

  if (typeof nuxt_plugin_axios_8a6182a2 === 'function') {
    await nuxt_plugin_axios_8a6182a2(app.context, inject)
  }

  if (typeof nuxt_plugin_buefy_7cae3e00 === 'function') {
    await nuxt_plugin_buefy_7cae3e00(app.context, inject)
  }

  if (typeof nuxt_plugin_axios_3566aa80 === 'function') {
    await nuxt_plugin_axios_3566aa80(app.context, inject)
  }

  if (process.client && typeof nuxt_plugin_vueinfinitescrollclient_466e7c09 === 'function') {
    await nuxt_plugin_vueinfinitescrollclient_466e7c09(app.context, inject)
  }

  if (typeof nuxt_plugin_plugin_68db66aa === 'function') {
    await nuxt_plugin_plugin_68db66aa(app.context, inject)
  }

  if (typeof nuxt_plugin_auth_7f7561ce === 'function') {
    await nuxt_plugin_auth_7f7561ce(app.context, inject)
  }

  // Lock enablePreview in context
  if (process.static && process.client) {
    app.context.enablePreview = function () {
      console.warn('You cannot call enablePreview() outside a plugin.')
    }
  }

  // If server-side, wait for async component to be resolved first
  if (process.server && ssrContext && ssrContext.url) {
    await new Promise((resolve, reject) => {
      router.push(ssrContext.url, resolve, (err) => {
        // https://github.com/vuejs/vue-router/blob/v3.4.3/src/util/errors.js
        if (!err._isRouter) return reject(err)
        if (err.type !== 2 /* NavigationFailureType.redirected */) return resolve()

        // navigated to a different route in router guard
        const unregister = router.afterEach(async (to, from) => {
          ssrContext.url = to.fullPath
          app.context.route = await getRouteData(to)
          app.context.params = to.params || {}
          app.context.query = to.query || {}
          unregister()
          resolve()
        })
      })
    })
  }

  return {
    store,
    app,
    router
  }
}

export { createApp, NuxtError }
