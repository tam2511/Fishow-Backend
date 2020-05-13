import { apiService } from '@/plugins/api.service'

export const namespaced = true

export const state = () =>  ({
  username: null
})

export const mutations = {
  SET_USERNAME(state, username) {
    state.username = username
  }
}

export const actions = {
  setUserInfo({ commit }) {
    apiService('/api/user/').then((data) => {
      commit('SET_USERNAME', data.username)
    })
  }
}
