import { apiService } from '../../common/api.service'

export const namespaced = true

export const state = {
  predictions: [],
}
export const mutations = {
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
}

export const actions = {
  async fetchPredictionTen({ commit }, endpoint) {
    // let endpoint = '/api/predictionten/'
    apiService(endpoint).then((data) => {
      commit('SET_PREDICTION', data.results[0])
    })
  },
}
