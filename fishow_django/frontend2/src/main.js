import Vue from 'vue'
import App from './App.vue'

import './registerServiceWorker'
import router from './router'
import store from './store'

import 'element-ui/lib/theme-chalk/index.css'
import 'vue-autosizer/dist/vue-autosizer.min.css'
import 'vue-navigation-bar/dist/vue-navigation-bar.css'

import ElementUI from 'element-ui'
import VueAutosizer from 'vue-autosizer'
import DynamicForm from 'vue-dynamic-form-component'
import VueNavigationBar from 'vue-navigation-bar'

Vue.component('vue-navigation-bar', VueNavigationBar)
Vue.use(VueAutosizer)
Vue.use(ElementUI)
Vue.use(DynamicForm)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
