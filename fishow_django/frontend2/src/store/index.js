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
      const arrayPredictions = predictions
      if (arrayPredictions) {
        Object.keys(arrayPredictions).forEach((key) => {
          if (arrayPredictions[key][0] === '[') {
            arrayPredictions[key] = arrayPredictions[key]
              .slice(1, arrayPredictions[key].length - 1)
              .split(',')
          }
        })
      }
      state.predictions = arrayPredictions
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
    async fetchPredictionTen({ commit }, endpoint) {
      // let endpoint = '/api/predictionten/'
      apiService(endpoint).then((data) => {
        commit('SET_PREDICTION', data.results[0])
      })
    },
  },
  modules: {},
})
