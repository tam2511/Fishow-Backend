import PredictionService from '~/services/PredictionService'

export const state = () => ({
  fishId: 0,
  pageScroll: 0,
  predictions: null,
})

export const mutations = {
  SET_FISHID(state, id) {
    state.fishId = id
  },
  SET_SCROLL(state, scroll) {
    state.pageScroll = scroll
  },
  SET_PREDICTION(state, predictions) {
    state.predictions = predictions
  },
}

export const actions = {
  setFishId({ commit }, id) {
    commit('SET_FISHID', id)
  },
  setScroll({ commit }, value) {
    commit('SET_SCROLL', value)
  },
  getPrediction({ commit, axios }, conf) {
    return PredictionService.getPredicitons(conf).then((response) => {
      commit('SET_PREDICTION', response.data.results[0])
    })
  },
}
