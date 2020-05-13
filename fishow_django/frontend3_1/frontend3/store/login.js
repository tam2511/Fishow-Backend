import { apiService } from '@/plugins/api.service'

export const namespaced = true

export const state = () =>  ({
  show: false,
  stepReg: true,
  error: false,
  errorEmail: false
})

export const mutations = {
  SET_SHOW(state, show) {
    state.show = show
  },
  SET_STEPREG(state, step) {
    state.stepReg = step
  }
}

export const actions = {
  sendUserData({ commit }, userData) {
    const endpoint = 'api/rest-auth/login/'
    apiService(endpoint, 'POST', userData).then((info) => {
      if (info.non_field_errors) {
        this.error = true
      } else if (
        info.email &&
        info.email[0] === 'Enter a valid email address.'
      ) {
        this.errorEmail = true
      } else {
        // this.$router.push({
        //     name: 'home',
        // })
        // location.reload()
      }
    })
  },
  setShow({ commit }) {
    const show = !this.state.login.show
    commit('SET_SHOW', show)
  },
  setStep({ commit }) {
    const step = !this.state.login.stepReg
    commit('SET_STEPREG', step)
  }
}
