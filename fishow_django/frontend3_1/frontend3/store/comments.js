export const state = () => ({
  comments: [],
})

export const mutations = {
  SET_COMMENTS(state, comments) {
    state.comments = comments
  },
}

export const actions = {
  writeComments({ dispatch, commit }) {},
}
