import BlogsService from '~/services/BlogsService'

export const state = () => ({
  blogs: [],
  blog: {},
  next: null,
  minPost: [],
})

export const mutations = {
  SET_NEXT(state, next) {
    state.next = next
  },
  SET_BLOGS(state, blogs) {
    state.blogs = blogs
  },
  SET_BLOG(state, blog) {
    state.blog = blog
  },
  SET_MIN(state, blog) {
    state.minPost = blog
  },
}

export const actions = {
  getBlogs({ dispatch, commit }) {
    return BlogsService.getBlogs().then((response) => {
      commit('SET_BLOGS', response.data.results)
      commit('SET_NEXT', response.data.next)
      dispatch('lastBLogs', response.data.results)
    })
  },
  getBlog({ commit }, slug) {
    return BlogsService.getBlog(slug).then((response) => {
      commit('SET_BLOG', response.data)
    })
  },
  lastBLogs({ commit }, blogs) {
    commit('SET_MIN', blogs && blogs.filter((blog, index) => index < 3))
  },
}
