import Vue from 'vue'
import Vuex from 'vuex'
import * as blogs from '@/store/modules/blogs.js'
import * as prediction from '@/store/modules/prediction.js'
import * as user from '@/store/modules/user.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  getters: {},
  actions: {},
  modules: {
    blogs,
    prediction,
    user,
  },
})
