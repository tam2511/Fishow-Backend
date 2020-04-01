import Vue from 'vue'
import Vuex from 'vuex'
import {apiService} from "../common/api.service";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 0,
    username: null
  },
  mutations: {
    increment (state) {
      state.count++
    },
  },
  getters: {
    getUserName: state => {
      return state.username
    }
  },
  actions: {
    async setUserInfo () {
      // add the username of the logged in user to localStorage
      const data = await apiService('/api/user/')
      this.state.username = data.username;
    }
  },
  modules: {
  }
})