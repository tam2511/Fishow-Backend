import UserService from '~/services/UserService'

export const state = () => ({
  showStateLogin: false,
  showStateReg: false,
})

export const mutations = {
  TOGGLE_LOGIN(state) {
    state.showStateLogin = !state.showStateLogin
  },
  TOGGLE_REG(state) {
    state.showStateReg = !state.showStateReg
  },
}

export const actions = {
  sendUserData({ commit }, userData) {
    return UserService.sendUserData(userData).then((response) => {
      // console.log('response = ', response)
      // commit('SET_BLOGS', response.data.results)
      // commit('SET_NEXT', response.data.next)
    })
    // const endpoint = 'api/rest-auth/login/'
    // apiService(endpoint, 'POST', userData).then((info) => {
    //   if (info['non_field_errors']) {
    //     this.error = true
    //   } else if (
    //     info['email'] &&
    //     info['email'][0] === 'Enter a valid email address.'
    //   ) {
    //     this.errorEmail = true
    //   } else {
    //     // this.$router.push({
    //     //     name: 'home',
    //     // })
    //     // location.reload()
    //   }
    // })
  },
}
