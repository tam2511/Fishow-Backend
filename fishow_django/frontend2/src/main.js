import Vue from 'vue'
import App from './App.vue'

import './registerServiceWorker'
import router from './router'
import store from './store'

import 'element-ui/lib/theme-chalk/index.css'
import 'vue-autosizer/dist/vue-autosizer.min.css'
import 'vue-navigation-bar/dist/vue-navigation-bar.css'
import VueAutosizer from 'vue-autosizer'
import VueNavigationBar from 'vue-navigation-bar'
import VueApexCharts from 'vue-apexcharts'


import {
  Button,
  Select,
  Form,
  FormItem,
  Input,
  Option,
  Switch,
  Steps,
  Step,
  Loading,
} from 'element-ui'
Vue.component('dynamic-form', (resolve) => {
  import('vue-dynamic-form-component').then((DynamicForm) => {
    resolve(DynamicForm.default)
  })
})

Vue.component(Button.name, Button)
Vue.component(Select.name, Select)
Vue.component(Form.name, Form)
Vue.component(FormItem.name, FormItem)
Vue.component(Input.name, Input)
Vue.component(Option.name, Option)
Vue.component(Steps.name, Steps)
Vue.component(Step.name, Step)
Vue.component(Switch.name, Switch)
Vue.component('vue-navigation-bar', VueNavigationBar)
Vue.use(VueApexCharts)
Vue.use(VueAutosizer)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
