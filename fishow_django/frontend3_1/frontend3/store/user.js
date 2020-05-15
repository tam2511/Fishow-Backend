import UserService from '~/services/UserService'

export const state = () => ({
  user: null,
  userBlogs: null,
  userComments: null,
  userRating: null,
})

export const mutations = {
  SET_USER(state, user) {
    state.user = user
  },
  SET_USERBLOGS(state, blogs) {
    state.userBlogs = blogs
  },
  SET_USERCOMMENTS(state, comments) {
    state.userComments = comments
  },
  SET_USERRATING(state, rating) {
    state.userRating = rating
  },
}

export const actions = {
  getUser({ commit }) {
    return UserService.getUserData().then((response) => {
      console.log('response', response.data)
      commit('SET_USER', response.data.username)
      commit('SET_USERBLOGS', response.data.blogs)
      commit('SET_USERCOMMENTS', response.data.comments)
      commit('SET_USERRATING', response.data.rating)
    })
  },
}
