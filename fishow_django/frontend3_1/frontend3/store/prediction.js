export const state = () => ({
  fishId: 0,
  pageScroll: 0,
})

export const mutations = {
  SET_FISHID(state, id) {
    state.fishId = id
  },
  SET_SCROLL(state, scroll) {
    state.pageScroll = scroll
  },
}

export const actions = {
  setFishId({ commit }, id) {
    commit('SET_FISHID', id)
  },
  setScroll({ commit }, value) {
    commit('SET_SCROLL', value)
  },
}
