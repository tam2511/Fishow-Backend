import BlogsService from '~/services/BlogsService'

export const state = () => ({
  blogs: [],
  blog: {},
  next: null,
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
}

export const actions = {
  getBlogs({ commit }) {
    return BlogsService.getBlogs().then((response) => {
      commit('SET_BLOGS', response.data.results)
      commit('SET_NEXT', response.data.next)
    })
  },
  getBlog({ commit }, slug) {
    return BlogsService.getBlog(slug).then((response) => {
      commit('SET_BLOG', response.data)
    })
  },
  likeBlog({ commit }, id) {},
}
