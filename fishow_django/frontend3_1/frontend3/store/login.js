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
