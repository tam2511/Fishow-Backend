import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import DynamicForm from 'vue-dynamic-form-component'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import VueAutosizer from 'vue-autosizer'
import 'vue-autosizer/dist/vue-autosizer.min.css'

Vue.use(VueAutosizer)
Vue.use(ElementUI)
Vue.use(DynamicForm)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
