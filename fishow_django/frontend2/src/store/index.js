import Vue from 'vue'
import Vuex from 'vuex'
import { apiService } from '../common/api.service'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    blogs: [],
    username: null,
    next: null,
    predictions: [],
  },
  mutations: {
    SET_BLOGS(state, blogs) {
      state.blogs = blogs
    },
    SET_PREDICTION(state, predictions) {
      state.predictions = predictions
    },
  },
  getters: {
    getUserName: (state) => {
      return state.username
    },
  },
  actions: {
    async setUserInfo() {
      // add the username of the logged in user to localStorage
      const data = await apiService('/api/user/')
      this.state.username = data.username
    },
    async fetchBlogs({ commit }) {
      let endpoint = '/api/blogs/'
      if (this.state.next) {
        endpoint = this.state.next
      }
      const blogs = []
      apiService(endpoint).then((data) => {
        blogs.push(...data.results)
        if (data.next) {
          this.state.next = data.next
        } else {
          this.state.next = null
        }
        commit('SET_BLOGS', blogs)
      })
    },
    async fetchPredictionTen({ commit }) {
      let endpoint = '/api/predictionten/'
      const predictions = []
      apiService(endpoint).then((data) => {
        predictions.push(...data.results)
        commit('SET_PREDICTION', predictions)
      })
    },
  },
  modules: {},
})
