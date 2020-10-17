import PredictionService from '~/services/PredictionService'

export const state = () => ({
  fishId: 0,
  pageScroll: 0,
  predictions: null,
  prediction: null,
  readyDataStorage: null,
  days: null,
})

export const mutations = {
  SET_FISHID(state, id) {
    state.fishId = id
  },
  SET_READYDATA(state, data) {
    state.readyDataStorage = data
  },
  SET_DAYS(state, data) {
    state.days = data
  },
  SET_SCROLL(state, scroll) {
    state.pageScroll = scroll
  },
  SET_PREDICTIONS(state, predictions) {
    state.predictions = predictions
  },
  SET_PREDICTION(state, prediction) {
    state.prediction = prediction
  },
}

export const actions = {
  setFishId({ commit }, id) {
    commit('SET_FISHID', id)
  },
  setScroll({ commit }, value) {
    commit('SET_SCROLL', value)
  },
  setReady({ commit }, data) {
    commit('SET_READYDATA', data)
  },
  setDays({ commit }, days) {
    commit('SET_DAYS', days)
  },
  getPrediction({ commit, axios }, conf) {
    return PredictionService.getPredicitons(conf).then((response) => {
      commit('SET_PREDICTIONS', response.data.results[0])
    })
  },
  getPredictionOne({ commit, axios }, conf) {
    return PredictionService.getPredicitons(conf).then((response) => {
      // console.log(response.data)
      commit('SET_PREDICTION', response.data.results[0])
    })
  },
}
