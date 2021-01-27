import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from '@nuxt/ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _45720d75 = () => interopDefault(import('../pages/blog-editor.vue' /* webpackChunkName: "pages/blog-editor" */))
const _02197fd1 = () => interopDefault(import('../pages/blogs/index.vue' /* webpackChunkName: "pages/blogs/index" */))
const _87413eae = () => interopDefault(import('../pages/news/index.vue' /* webpackChunkName: "pages/news/index" */))
const _acefcefe = () => interopDefault(import('../pages/prognoz-kleva/index.vue' /* webpackChunkName: "pages/prognoz-kleva/index" */))
const _50bd4826 = () => interopDefault(import('../pages/UserPage.vue' /* webpackChunkName: "pages/UserPage" */))
const _5126afa6 = () => interopDefault(import('../pages/prognoz-kleva/convert.js' /* webpackChunkName: "pages/prognoz-kleva/convert" */))
const _bf92e7da = () => interopDefault(import('../pages/account-confirm-email/_key.vue' /* webpackChunkName: "pages/account-confirm-email/_key" */))
const _4d18c01a = () => interopDefault(import('../pages/blog/_slug/index.vue' /* webpackChunkName: "pages/blog/_slug/index" */))
const _01e67924 = () => interopDefault(import('../pages/news/_slug/index.vue' /* webpackChunkName: "pages/news/_slug/index" */))
const _7e2a6351 = () => interopDefault(import('../pages/OnePrediction/_areal/_date/_city/_fish/index.vue' /* webpackChunkName: "pages/OnePrediction/_areal/_date/_city/_fish/index" */))
const _0e524c85 = () => interopDefault(import('../pages/prognoz-kleva/_areal/_date/_city/_fish/index.vue' /* webpackChunkName: "pages/prognoz-kleva/_areal/_date/_city/_fish/index" */))
const _400c9eef = () => interopDefault(import('../pages/OnePrediction/_areal/_date/_city/_fish/transformForChart.js' /* webpackChunkName: "pages/OnePrediction/_areal/_date/_city/_fish/transformForChart" */))
const _25f2071c = () => interopDefault(import('../pages/prognoz-kleva/_areal/_date/_city/_fish/getData.js' /* webpackChunkName: "pages/prognoz-kleva/_areal/_date/_city/_fish/getData" */))
const _cd91b1e2 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/blog-editor",
    component: _45720d75,
    name: "blog-editor"
  }, {
    path: "/blogs",
    component: _02197fd1,
    name: "blogs"
  }, {
    path: "/news",
    component: _87413eae,
    name: "news"
  }, {
    path: "/prognoz-kleva",
    component: _acefcefe,
    name: "prognoz-kleva"
  }, {
    path: "/UserPage",
    component: _50bd4826,
    name: "UserPage"
  }, {
    path: "/prognoz-kleva/convert",
    component: _5126afa6,
    name: "prognoz-kleva-convert"
  }, {
    path: "/account-confirm-email/:key?",
    component: _bf92e7da,
    name: "account-confirm-email-key"
  }, {
    path: "/blog/:slug",
    component: _4d18c01a,
    name: "blog-slug"
  }, {
    path: "/news/:slug",
    component: _01e67924,
    name: "news-slug"
  }, {
    path: "/OnePrediction/:areal?/:date?/:city?/:fish",
    component: _7e2a6351,
    name: "OnePrediction-areal-date-city-fish"
  }, {
    path: "/prognoz-kleva/:areal?/:date/:city?/:fish",
    component: _0e524c85,
    name: "prognoz-kleva-areal-date-city-fish"
  }, {
    path: "/OnePrediction/:areal?/:date?/:city?/:fish?/transformForChart",
    component: _400c9eef,
    name: "OnePrediction-areal-date-city-fish-transformForChart"
  }, {
    path: "/prognoz-kleva/:areal?/:date/:city?/:fish?/getData",
    component: _25f2071c,
    name: "prognoz-kleva-areal-date-city-fish-getData"
  }, {
    path: "/",
    component: _cd91b1e2,
    name: "index"
  }],

  fallback: false
}

function decodeObj(obj) {
  for (const key in obj) {
    if (typeof obj[key] === 'string') {
      obj[key] = decode(obj[key])
    }
  }
}

export function createRouter () {
  const router = new Router(routerOptions)

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    const r = resolve(to, current, append)
    if (r && r.resolved && r.resolved.query) {
      decodeObj(r.resolved.query)
    }
    return r
  }

  return router
}
