import CommentService from '~/services/CommentService'

export const state = () => ({
  comments: [],
})

export const mutations = {
  SET_COMMENTS(state, comments) {
    state.comments = comments
  },
  ADD_COMMENT(state, comments) {
    state.comments.push(comments)
  },
}

export const actions = {
  writeComments({ commit }, value) {
    commit('ADD_COMMENT', value)
  },
  getComments({ commit }, slug) {
    return CommentService.getBlogComment(slug).then((response) => {
      commit('SET_COMMENTS', response.data.results)
    })
  },
}
