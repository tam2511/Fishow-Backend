import { apiService } from '../../common/api.service'

export const namespaced = true

export const state = {
  blogs: [],
  next: null,
}

export const mutations = {
  SET_NEXT(state, next) {
    state.next = next
  },
  SET_BLOGS(state, blogs) {
    state.blogs = blogs

  },
}

export const actions = {
  fetchBlogs({ commit }) {
    let endpoint = '/api/blogs/'

    if (this.state.blogs.next) {
      endpoint = this.state.blogs.next
    }
    let next = null;
    console.log('endpoin = ', endpoint);
    const blogs = []
    apiService(endpoint).then((data) => {
      blogs.push(...data.results)
      if (data.next) {
        next = data.next
      } else {
        next = null
      }
      commit('SET_BLOGS', blogs)
      commit('SET_NEXT', next)
    })
  },
}
